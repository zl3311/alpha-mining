"""Audit a cloud agent run: pull trace, analyze compliance, output summary.

Fetches the full SSE conversation trace from the Cursor API for a given
cloud agent ID, classifies tool calls and file accesses for V1/V2 compliance,
checks skill-chain adherence, and outputs a structured markdown audit summary
alongside a raw JSON trace file.

Usage (local):
    uv run python3 scripts/audit_cloud_trace.py --agent-id bc-XXXX --output trace.json

Usage (CI):
    Reads CURSOR_API_KEY from the environment and prints the markdown summary to
    stdout for capture as a PR comment. This was driven by a GitHub Actions
    workflow that was removed when the project was archived; wire it into your own
    automation if you want the same behaviour.

The --summary-only flag skips the raw trace export and only prints the
markdown summary (useful for re-auditing from an existing trace file).
"""

import argparse
import json
import os
import re
import sys
from pathlib import Path

import httpx

BASE = "https://api.cursor.com/v1"

V1_PATHS = {
    "factor_inventory.json",
    "hypothesis_backlog.md",
    "brain_availability_matrix.md",
    "data/experiments/",
}

REQUIRED_SKILLS = [
    "mining-session",
    "context-gather",
    "signal-generation",
    "result-analysis",
    "experiment-reporting",
]

SHELL_CATEGORIES = {
    "hf_query": re.compile(r"hf_query\.py"),
    "hf_submit": re.compile(r"hf_submit\.py"),
    "hf_poll": re.compile(r"hf_poll\.py"),
    "brain_check": re.compile(r"brain_check\.py"),
    "pnl_correlation": re.compile(r"pnl_correlation\.py"),
    "brain_metadata": re.compile(r"brain_metadata\.py"),
    "parse_frontmatter": re.compile(r"parse_frontmatter\.py"),
    "git": re.compile(r"\bgit\b"),
    "pytest": re.compile(r"pytest"),
    "ad_hoc_poll": re.compile(r"hf_query.*--stats"),
}


def get_api_key() -> str:
    key = os.environ.get("CURSOR_API_KEY", "")
    if not key:
        try:
            from dotenv import load_dotenv
            load_dotenv(Path(__file__).resolve().parent.parent / ".env")
            key = os.environ.get("CURSOR_API_KEY", "")
        except ImportError:
            pass
    if not key:
        print("ERROR: CURSOR_API_KEY not set", file=sys.stderr)
        sys.exit(1)
    return key


def get_headers(api_key: str) -> dict:
    return {"Authorization": f"Bearer {api_key}"}


def get_run_info(agent_id: str, headers: dict) -> dict | None:
    """Fetch agent + run metadata from the REST API."""
    r = httpx.get(f"{BASE}/agents/{agent_id}", headers=headers, timeout=15)
    if r.status_code != 200:
        return None
    agent_info = r.json()

    r2 = httpx.get(f"{BASE}/agents/{agent_id}/runs", headers=headers, timeout=15)
    if r2.status_code != 200:
        return None
    runs = r2.json().get("items", [])
    if not runs:
        return None

    run = runs[0]
    branches = run.get("git", {}).get("branches", [])
    first_branch = branches[0] if branches else {}
    return {
        "agent_id": agent_id,
        "agent_name": agent_info.get("name"),
        "run_id": run["id"],
        "status": run.get("status"),
        "created": run.get("createdAt"),
        "duration_ms": run.get("durationMs"),
        "result": run.get("result"),
        "pr_url": first_branch.get("prUrl"),
        "branch": first_branch.get("branch"),
    }


def stream_trace(agent_id: str, run_id: str, headers: dict) -> list[dict]:
    """Stream the full SSE trace for a run."""
    url = f"{BASE}/agents/{agent_id}/runs/{run_id}/stream"
    events = []

    with httpx.stream("GET", url, headers={
        **headers, "Accept": "text/event-stream"
    }, timeout=180) as resp:
        current_event = None
        current_data: list[str] = []

        for line in resp.iter_lines():
            if line.startswith("event: "):
                current_event = line[7:]
                current_data = []
            elif line.startswith("data: "):
                current_data.append(line[6:])
            elif line == "" and current_event:
                data_str = "\n".join(current_data)
                try:
                    data = json.loads(data_str)
                except (json.JSONDecodeError, ValueError):
                    data = data_str
                events.append({"event": current_event, "data": data})
                current_event = None
                current_data = []

    return events


def _is_v1_path(path: str) -> bool:
    """Check if a file path references a deprecated V1 artifact."""
    normalized = path.replace("/workspace/", "")
    for v1 in V1_PATHS:
        if v1 in normalized:
            return True
    return False


def _classify_shell(cmd: str) -> str:
    """Classify a shell command into a known category."""
    if SHELL_CATEGORIES["ad_hoc_poll"].search(cmd):
        return "ad_hoc_poll"
    for cat, pattern in SHELL_CATEGORIES.items():
        if cat == "ad_hoc_poll":
            continue
        if pattern.search(cmd):
            return cat
    return "other"


def extract_summary(events: list[dict]) -> dict:
    """Extract structured audit metrics from the raw event stream."""
    thinking_chars = 0
    assistant_chars = 0
    tool_calls = []
    user_messages = []
    errors = []
    shell_commands = []
    files_read = []
    files_edited = []

    for ev in events:
        etype = ev.get("event")
        data = ev.get("data", {})
        if not isinstance(data, dict):
            continue

        if etype == "thinking":
            thinking_chars += len(data.get("text", ""))
        elif etype == "assistant":
            assistant_chars += len(data.get("text", ""))
        elif etype == "error":
            errors.append(str(data)[:500])
        elif etype == "interaction_update":
            itype = data.get("type", "")

            if itype == "user-message-appended":
                msg = data.get("userMessage", {})
                user_messages.append(msg.get("text", "")[:1000])

            elif itype == "tool-call-started":
                tc = data.get("toolCall", {})
                call_id = data.get("callId", "")
                tool_type = tc.get("type", "unknown")
                args = tc.get("args", {})

                entry = {"type": tool_type, "id": call_id}

                if tool_type == "shell":
                    cmd = args.get("command", "")
                    entry["command"] = cmd[:500]
                    entry["category"] = _classify_shell(cmd)
                    shell_commands.append({"command": cmd[:300], "category": entry["category"]})
                elif tool_type == "read":
                    path = args.get("path", "")
                    entry["path"] = path
                    entry["is_v1"] = _is_v1_path(path)
                    files_read.append({"path": path, "is_v1": entry["is_v1"]})
                elif tool_type == "edit":
                    path = args.get("path", "")
                    entry["path"] = path
                    entry["is_v1"] = _is_v1_path(path)
                    files_edited.append({"path": path, "is_v1": entry["is_v1"]})
                elif tool_type == "glob":
                    entry["pattern"] = args.get("pattern", "")

                tool_calls.append(entry)

    # Aggregate metrics
    tool_type_counts = {}
    for tc in tool_calls:
        t = tc.get("type", "unknown")
        tool_type_counts[t] = tool_type_counts.get(t, 0) + 1

    shell_category_counts = {}
    for sc in shell_commands:
        c = sc["category"]
        shell_category_counts[c] = shell_category_counts.get(c, 0) + 1

    v1_reads = [f for f in files_read if f["is_v1"]]
    v1_edits = [f for f in files_edited if f["is_v1"]]

    # Skill chain compliance: check if mining-session was read
    skills_read = []
    for f in files_read:
        path = f["path"]
        for skill in REQUIRED_SKILLS:
            if f"skills/{skill}" in path:
                skills_read.append(skill)
    skills_read = list(dict.fromkeys(skills_read))

    # Verification compliance
    ran_pnl_corr = shell_category_counts.get("pnl_correlation", 0) > 0
    ran_hf_poll = shell_category_counts.get("hf_poll", 0) > 0
    ad_hoc_polls = shell_category_counts.get("ad_hoc_poll", 0)

    return {
        "total_events": len(events),
        "thinking_chars": thinking_chars,
        "assistant_chars": assistant_chars,
        "tool_call_count": len(tool_calls),
        "tool_type_breakdown": tool_type_counts,
        "shell_category_breakdown": shell_category_counts,
        "shell_commands": shell_commands,
        "files_read": files_read,
        "files_edited": files_edited,
        "v1_reads": v1_reads,
        "v1_edits": v1_edits,
        "v1_regression": len(v1_reads) > 0 or len(v1_edits) > 0,
        "skills_read": skills_read,
        "skill_chain_compliant": "mining-session" in skills_read,
        "ran_pnl_correlation": ran_pnl_corr,
        "ran_hf_poll": ran_hf_poll,
        "ad_hoc_poll_count": ad_hoc_polls,
        "user_message_count": len(user_messages),
        "user_messages": user_messages,
        "error_count": len(errors),
        "errors": errors[:10],
    }


def render_markdown(run_info: dict, summary: dict) -> str:
    """Render the audit summary as a markdown PR comment."""
    lines = []
    lines.append("## Cloud Agent Trace Audit")
    lines.append("")

    dur_min = (run_info.get("duration_ms") or 0) / 60000
    lines.append("### Run Overview")
    lines.append("")
    lines.append("| Field | Value |")
    lines.append("|-------|-------|")
    lines.append(f"| Agent | `{run_info.get('agent_id', '?')}` |")
    lines.append(f"| Run | `{run_info.get('run_id', '?')}` |")
    lines.append(f"| Status | {run_info.get('status', '?')} |")
    lines.append(f"| Duration | {dur_min:.0f} min |")
    lines.append(f"| Branch | `{run_info.get('branch', '?')}` |")
    lines.append(f"| Events | {summary['total_events']} |")
    lines.append(f"| Tool calls | {summary['tool_call_count']} |")
    lines.append("")

    if summary["total_events"] == 0:
        lines.append("> **Trace expired.** The SSE stream returned 0 events; the "
                      "trace has been purged from the Cursor API (typical retention "
                      "is ~2-3 days). Only run metadata is available.")
        lines.append("")
        if run_info.get("result"):
            lines.append("### Agent Self-Reported Result")
            lines.append("")
            lines.append(run_info["result"][:2000])
            lines.append("")
        return "\n".join(lines)

    # Skill chain compliance
    compliant = summary["skill_chain_compliant"]
    lines.append("### Skill Chain Compliance")
    lines.append("")
    if compliant:
        lines.append("PASS: `mining-session` was read.")
    else:
        lines.append("**FAIL**: `mining-session` was NOT read. The agent bypassed the skill chain.")
    lines.append(f"- Skills read: {', '.join(summary['skills_read']) or 'none'}")
    lines.append(f"- Expected: {', '.join(REQUIRED_SKILLS)}")
    lines.append("")

    # V1/V2 compliance
    v1_reg = summary["v1_regression"]
    lines.append("### V1/V2 Compliance")
    lines.append("")
    if v1_reg:
        lines.append("**REGRESSION**: V1 files were accessed.")
        for f in summary["v1_reads"]:
            lines.append(f"- READ (V1): `{f['path']}`")
        for f in summary["v1_edits"]:
            lines.append(f"- EDIT (V1): `{f['path']}`")
    else:
        lines.append("PASS: No V1 files accessed.")
    lines.append(f"- Total files read: {len(summary['files_read'])}")
    lines.append(f"- Total files edited: {len(summary['files_edited'])}")
    lines.append("")

    # Tool usage
    lines.append("### Tool Usage")
    lines.append("")
    lines.append("| Tool Type | Count |")
    lines.append("|-----------|-------|")
    for t, c in sorted(summary["tool_type_breakdown"].items(), key=lambda x: -x[1]):
        lines.append(f"| {t} | {c} |")
    lines.append("")

    lines.append("| Shell Category | Count |")
    lines.append("|----------------|-------|")
    for c, n in sorted(summary["shell_category_breakdown"].items(), key=lambda x: -x[1]):
        flag = " **WARNING**" if c == "ad_hoc_poll" and n > 2 else ""
        lines.append(f"| {c} | {n} |{flag}")
    lines.append("")

    # Verification gate
    lines.append("### Verification Gate")
    lines.append("")
    pnl_status = "PASS" if summary["ran_pnl_correlation"] else "**FAIL**"
    poll_status = "PASS" if summary["ran_hf_poll"] else "**FAIL**"
    lines.append(f"- `pnl_correlation.py --vs-book`: {pnl_status}")
    lines.append(f"- `hf_poll.py` (canonical poller): {poll_status}")
    if summary["ad_hoc_poll_count"] > 0:
        lines.append(f"- Ad-hoc `--stats` polling loops: {summary['ad_hoc_poll_count']} "
                      "(should use `hf_poll.py` instead)")
    lines.append("")

    # Errors
    if summary["error_count"] > 0:
        lines.append("### Errors")
        lines.append("")
        lines.append(f"{summary['error_count']} error(s) detected:")
        for e in summary["errors"]:
            lines.append(f"- `{e[:200]}`")
        lines.append("")

    # Efficiency
    lines.append("### Efficiency")
    lines.append("")
    lines.append(f"- Thinking: {summary['thinking_chars']:,} chars")
    lines.append(f"- Assistant output: {summary['assistant_chars']:,} chars")
    sim_count = summary["shell_category_breakdown"].get("hf_submit", 0)
    lines.append(f"- Simulation batches submitted: {sim_count}")
    lines.append("")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Audit a cloud agent trace")
    parser.add_argument("--agent-id", required=True, help="Cursor cloud agent ID (bc-*)")
    parser.add_argument("--output", default=None, help="Path to write raw trace JSON")
    parser.add_argument("--summary-only", action="store_true",
                        help="Skip trace export, only print markdown summary from existing --output file")
    parser.add_argument("--hf-upload", default=None,
                        help="HF storage bucket to upload trace (e.g. <hf-user>/alpha-mining-traces)")
    args = parser.parse_args()

    api_key = get_api_key()
    headers = get_headers(api_key)

    if args.summary_only and args.output:
        data = json.loads(Path(args.output).read_text())
        md = render_markdown(data["run_info"], data["summary"])
        print(md)
        return

    print(f"Auditing agent {args.agent_id}...", file=sys.stderr)

    run_info = get_run_info(args.agent_id, headers)
    if not run_info:
        print(f"ERROR: No run found for agent {args.agent_id}", file=sys.stderr)
        sys.exit(1)

    run_id = run_info["run_id"]
    dur_min = (run_info.get("duration_ms") or 0) / 60000
    print(f"  Run: {run_id} ({dur_min:.0f}min, {run_info['status']})", file=sys.stderr)

    events = stream_trace(args.agent_id, run_id, headers)
    summary = extract_summary(events)
    print(f"  Trace: {len(events)} events, {summary['tool_call_count']} tool calls", file=sys.stderr)

    trace_data = {
        "run_info": run_info,
        "summary": summary,
        "events": events,
    }

    if args.output:
        Path(args.output).write_text(json.dumps(trace_data, indent=2, default=str))
        print(f"  Saved: {args.output}", file=sys.stderr)

    if args.hf_upload and args.output:
        _upload_to_hf(args.hf_upload, args.output, run_info)

    md = render_markdown(run_info, summary)
    print(md)


def _upload_to_hf(bucket_id: str, trace_path: str, run_info: dict):
    """Upload trace JSON to a HuggingFace storage bucket (non-versioned, S3-like)."""
    try:
        from huggingface_hub import batch_bucket_files
    except ImportError:
        print("  WARNING: huggingface_hub not installed, skipping HF upload", file=sys.stderr)
        return

    hf_token = os.environ.get("HF_TOKEN", "")
    if not hf_token:
        print("  WARNING: HF_TOKEN not set, skipping HF upload", file=sys.stderr)
        return

    created = run_info.get("created", "")
    date_part = created[:10].replace("-", "") if created else "unknown"
    agent_id = run_info.get("agent_id", "unknown")
    run_id = run_info.get("run_id", "unknown")
    remote_path = f"traces/{date_part}/{agent_id}_{run_id}.json"

    try:
        batch_bucket_files(
            bucket_id,
            add=[(trace_path, remote_path)],
            token=hf_token,
        )
        print(f"  Uploaded to HF bucket: {bucket_id}/{remote_path}", file=sys.stderr)
    except Exception as e:
        print(f"  WARNING: HF bucket upload failed: {e}", file=sys.stderr)


if __name__ == "__main__":
    main()
