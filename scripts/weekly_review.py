"""Weekly review: aggregate cloud-agent PR audits into a digest.

Lists all open PRs labeled 'cloud-agent', reads each audit summary comment,
aggregates metrics, and outputs a markdown digest of trends, failure modes,
and findings worth promoting to the knowledge base.

Usage:
    uv run python3 scripts/weekly_review.py
    uv run python3 scripts/weekly_review.py --days 14  # look back 14 days
    uv run python3 scripts/weekly_review.py --output digest.md

Requires `gh` CLI to be authenticated.
"""

import argparse
import json
import re
import subprocess
import sys
from datetime import datetime, timedelta, timezone


def run_gh(args: list[str]) -> str:
    """Run a gh CLI command and return stdout."""
    result = subprocess.run(
        ["gh"] + args,
        capture_output=True, text=True, timeout=30,
    )
    if result.returncode != 0:
        print(f"gh error: {result.stderr}", file=sys.stderr)
    return result.stdout


def list_cloud_prs(days: int) -> list[dict]:
    """List cloud-agent PRs from the past N days."""
    raw = run_gh([
        "pr", "list",
        "--label", "cloud-agent",
        "--state", "all",
        "--limit", "50",
        "--json", "number,title,state,createdAt,closedAt,headRefName,body",
    ])
    if not raw.strip():
        return []

    prs = json.loads(raw)
    cutoff = datetime.now(timezone.utc) - timedelta(days=days)
    return [
        pr for pr in prs
        if datetime.fromisoformat(pr["createdAt"].replace("Z", "+00:00")) >= cutoff
    ]


def get_audit_comment(pr_number: int) -> str | None:
    """Find the audit summary comment on a PR (posted by the GHA)."""
    raw = run_gh([
        "pr", "view", str(pr_number),
        "--json", "comments",
        "-q", ".comments[].body",
    ])
    for comment in raw.split("\n\n"):
        if "## Cloud Agent Trace Audit" in comment:
            return comment
    return None


def parse_audit_comment(comment: str) -> dict:
    """Extract structured data from an audit summary comment."""
    metrics = {
        "events": _extract_int(comment, r"Events \| (\d+)"),
        "tool_calls": _extract_int(comment, r"Tool calls \| (\d+)"),
        "duration_min": _extract_int(comment, r"Duration \| (\d+) min"),
        "skill_chain_pass": "PASS" in _extract_section(comment, "Skill Chain Compliance"),
        "v1_regression": "REGRESSION" in _extract_section(comment, "V1/V2 Compliance"),
        "pnl_corr_pass": "`pnl_correlation.py --vs-book`: PASS" in comment,
        "hf_poll_pass": "`hf_poll.py` (canonical poller): PASS" in comment,
        "ad_hoc_polls": _extract_int(comment, r"Ad-hoc.*?(\d+)"),
        "trace_expired": "Trace expired" in comment,
    }
    return metrics


def _extract_int(text: str, pattern: str) -> int:
    m = re.search(pattern, text)
    return int(m.group(1)) if m else 0


def _extract_section(text: str, heading: str) -> str:
    pattern = rf"### {re.escape(heading)}\n(.*?)(?=\n### |\Z)"
    m = re.search(pattern, text, re.DOTALL)
    return m.group(1).strip() if m else ""


def parse_pr_metadata(body: str) -> dict:
    """Extract CLOUD-AGENT-METADATA from PR body."""
    m = re.search(r"<!-- CLOUD-AGENT-METADATA\n(.*?)-->", body, re.DOTALL)
    if not m:
        return {}
    try:
        import yaml
        return yaml.safe_load(m.group(1)) or {}
    except Exception:
        return {}


def render_digest(prs: list[dict], audits: dict[int, dict],
                  metadata: dict[int, dict]) -> str:
    """Render the weekly digest as markdown."""
    lines = []
    lines.append("# Weekly Cloud Agent Review Digest")
    lines.append("")
    lines.append(f"Period: {len(prs)} cloud-agent PRs reviewed")
    lines.append(f"Generated: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}")
    lines.append("")

    # Aggregate metrics
    total_runs = len(prs)
    audited = [n for n, a in audits.items() if a]
    skill_pass = sum(1 for a in audits.values() if a and a.get("skill_chain_pass"))
    v1_regressions = sum(1 for a in audits.values() if a and a.get("v1_regression"))
    pnl_pass = sum(1 for a in audits.values() if a and a.get("pnl_corr_pass"))
    poll_pass = sum(1 for a in audits.values() if a and a.get("hf_poll_pass"))
    expired = sum(1 for a in audits.values() if a and a.get("trace_expired"))

    total_budget = sum(m.get("budget_used", 0) for m in metadata.values() if m)
    total_gate = sum(m.get("gate_passers", 0) for m in metadata.values() if m)

    lines.append("## Summary Metrics")
    lines.append("")
    lines.append("| Metric | Value |")
    lines.append("|--------|-------|")
    lines.append(f"| Total runs | {total_runs} |")
    lines.append(f"| Audited (trace available) | {len(audited)} |")
    lines.append(f"| Trace expired | {expired} |")
    lines.append(f"| Skill chain compliant | {skill_pass}/{len(audited)} |")
    lines.append(f"| V1 regressions | {v1_regressions} |")
    lines.append(f"| PnL correlation verified | {pnl_pass}/{len(audited)} |")
    lines.append(f"| Used canonical hf_poll | {poll_pass}/{len(audited)} |")
    lines.append(f"| Total sim budget used | {total_budget} |")
    lines.append(f"| Total gate-passers | {total_gate} |")
    if total_budget > 0:
        lines.append(f"| Gate-passer rate | {total_gate/total_budget*100:.1f}% |")
    lines.append("")

    # Per-PR breakdown
    lines.append("## Per-Run Breakdown")
    lines.append("")
    lines.append("| PR | Date | Strategy | Budget | Gate | Skill | V1 | PnL | State |")
    lines.append("|----|------|----------|--------|------|-------|----|-----|-------|")
    for pr in prs:
        n = pr["number"]
        date = pr["createdAt"][:10]
        m = metadata.get(n, {})
        a = audits.get(n, {})
        strategy = m.get("strategy", "?")
        budget = m.get("budget_used", "?")
        gate = m.get("gate_passers", "?")
        skill = "PASS" if a.get("skill_chain_pass") else "FAIL" if a else "?"
        v1 = "REGR" if a.get("v1_regression") else "OK" if a else "?"
        pnl = "PASS" if a.get("pnl_corr_pass") else "FAIL" if a else "?"
        state = pr["state"]
        lines.append(f"| #{n} | {date} | {strategy} | {budget} | {gate} | {skill} | {v1} | {pnl} | {state} |")
    lines.append("")

    # Failure patterns
    issues = []
    if v1_regressions > 0:
        issues.append(f"- **V1 regressions** in {v1_regressions} run(s): the agent still touched "
                       "deprecated V1 files. Check if the dispatcher prompt has been updated.")
    if skill_pass < len(audited):
        issues.append(f"- **Skill chain bypass** in {len(audited) - skill_pass} run(s): "
                       "`mining-session` was not read.")
    if pnl_pass < len(audited):
        issues.append(f"- **Self-corr not verified** in {len(audited) - pnl_pass} run(s): "
                       "`pnl_correlation.py --vs-book` was not run.")
    if poll_pass < len(audited):
        issues.append(f"- **Ad-hoc polling** in {len(audited) - poll_pass} run(s): "
                       "used `--stats` loops instead of `hf_poll.py`.")

    if issues:
        lines.append("## Failure Patterns")
        lines.append("")
        lines.extend(issues)
        lines.append("")
    else:
        lines.append("## Failure Patterns")
        lines.append("")
        lines.append("No compliance failures detected.")
        lines.append("")

    # Candidates summary
    all_candidates = []
    for n, m in metadata.items():
        for c in m.get("candidates", []):
            c["pr"] = n
            all_candidates.append(c)

    if all_candidates:
        lines.append("## Candidates Found")
        lines.append("")
        lines.append("| PR | Alpha | Grade | S | F | Self-Corr | Verdict |")
        lines.append("|----|-------|-------|---|---|-----------|---------|")
        for c in all_candidates:
            lines.append(f"| #{c['pr']} | {c.get('id','?')} | {c.get('grade','?')} | "
                          f"{c.get('sharpe','?')} | {c.get('fitness','?')} | "
                          f"{c.get('self_corr_max','?')} | {c.get('verdict','?')} |")
        lines.append("")

    # Recommendations
    lines.append("## Recommendations")
    lines.append("")
    lines.append("Review the per-run breakdown above. For each run with findings:")
    lines.append("- Promote new factors to `data/factors/` if not already captured")
    lines.append("- Add new rules/dead_zones/patterns to `data/knowledge/`")
    lines.append("- Close the PR with a summary comment after review")
    lines.append("")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Weekly cloud-agent review digest")
    parser.add_argument("--days", type=int, default=7, help="Look back N days (default: 7)")
    parser.add_argument("--output", default=None, help="Write digest to file (default: stdout)")
    args = parser.parse_args()

    print(f"Fetching cloud-agent PRs from the past {args.days} days...", file=sys.stderr)
    prs = list_cloud_prs(args.days)
    print(f"  Found {len(prs)} PRs", file=sys.stderr)

    if not prs:
        print("No cloud-agent PRs found in the given period.", file=sys.stderr)
        return

    audits = {}
    metadata = {}
    for pr in prs:
        n = pr["number"]
        print(f"  Reading PR #{n}...", file=sys.stderr)
        comment = get_audit_comment(n)
        audits[n] = parse_audit_comment(comment) if comment else {}
        metadata[n] = parse_pr_metadata(pr.get("body", ""))

    digest = render_digest(prs, audits, metadata)

    if args.output:
        with open(args.output, "w") as f:
            f.write(digest)
        print(f"  Digest written to {args.output}", file=sys.stderr)
    else:
        print(digest)


if __name__ == "__main__":
    main()
