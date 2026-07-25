"""Format a session's meta.md into an email digest.

Reads the session meta.md file (YAML frontmatter + markdown body), extracts
structured candidate data from the frontmatter, converts the body to HTML,
and writes email subject/body files for the GHA to send via Resend.

Usage (GHA):
    python3 scripts/format_email_digest.py \
        --meta-file data/sessions/20260606-001/meta.md \
        --pr-url https://github.com/.../pull/35

Usage (local test):
    python3 scripts/format_email_digest.py \
        --meta-file data/sessions/20260606-001/meta.md \
        --pr-url https://github.com/...

Exit codes:
    0 — success (email files written) or graceful skip (empty files written)
    1 — meta-file not found (hard failure)
"""

import argparse
import sys
from pathlib import Path

import markdown
import yaml

BRAIN_ALPHA_URL = "https://platform.worldquantbrain.com/alpha"


def parse_meta_file(path: Path) -> tuple[dict, str]:
    """Parse a frontmatter markdown file into (frontmatter_dict, body_str)."""
    text = path.read_text()
    if not text.startswith("---"):
        return {}, text

    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}, text

    try:
        fm = yaml.safe_load(parts[1]) or {}
    except yaml.YAMLError:
        fm = {}

    body = parts[2].strip()
    return fm, body


def format_subject(meta: dict) -> str:
    """Build a one-line email subject from frontmatter fields."""
    session = meta.get("id", "unknown")
    strategy = meta.get("strategy", "?")
    candidates = meta.get("candidates") or []
    n = len(candidates)

    best_fitness = 0.0
    for c in candidates:
        if not isinstance(c, dict):
            continue
        f = c.get("fitness")
        if f is not None:
            try:
                best_fitness = max(best_fitness, float(f))
            except (TypeError, ValueError):
                pass

    if best_fitness > 0:
        return f"[Alpha Mining] {session}: {strategy} — {n} candidates (best F={best_fitness:.2f})"
    return f"[Alpha Mining] {session}: {strategy} — {n} candidates"


def format_html(meta: dict, body: str, pr_url: str) -> str:
    """Render a mobile-friendly HTML email from frontmatter + markdown body."""
    session = meta.get("id", "unknown")
    strategy = meta.get("strategy", "?")
    budget = meta.get("budget_used", "?")
    budget_cap = meta.get("budget_cap", "100") or "100"
    gate_passers = meta.get("gate_passers", "?")
    status = meta.get("status", "?")
    candidates = meta.get("candidates") or []

    rows = ""
    for c in candidates:
        if not isinstance(c, dict):
            continue
        aid = c.get("id", "?")
        grade = c.get("grade", "?")
        fitness = c.get("fitness", 0)
        sc_value = c.get("self_corr_value", "?")
        sc_result = c.get("self_corr_result", "?")
        verdict = c.get("verdict", "?")
        url = f"{BRAIN_ALPHA_URL}/{aid}"

        is_good = verdict in ("SUBMITTABLE", "SAFE", "RISKY") and sc_result != "FAIL"
        verdict_color = "#2e7d32" if is_good else "#f57c00"

        try:
            fitness_str = f"{float(fitness):.2f}"
        except (TypeError, ValueError):
            fitness_str = str(fitness)

        rows += (
            f'<tr>'
            f'<td><a href="{url}" style="color:#1976d2;text-decoration:none;'
            f'font-weight:bold">{aid}</a></td>'
            f'<td>{grade}</td>'
            f'<td><strong>{fitness_str}</strong></td>'
            f'<td>{sc_value} ({sc_result})</td>'
            f'<td style="color:{verdict_color}">{verdict}</td>'
            f'</tr>\n'
        )

    if not candidates:
        candidates_html = "<p style='color:#888'>No submission candidates this run.</p>"
    else:
        candidates_html = f"""<table>
<tr>
  <th>Alpha</th><th>Grade</th><th>Fitness</th><th>Self-Corr</th><th>Verdict</th>
</tr>
{rows}
</table>"""

    body_html = (
        markdown.markdown(body, extensions=["tables", "fenced_code"])
        if body
        else "<em>No details available.</em>"
    )

    return f"""<!DOCTYPE html>
<html>
<head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<style>
  table {{ border-collapse:collapse; width:100%; font-size:14px; margin:8px 0 }}
  th, td {{ border:1px solid #ddd; padding:6px 8px; text-align:left }}
  th {{ background:#f5f5f5; font-weight:bold }}
  pre {{ background:#f5f5f5; padding:10px; border-radius:4px; overflow-x:auto; font-size:13px }}
  code {{ font-family:'SF Mono',Menlo,Monaco,monospace; font-size:13px }}
  pre code {{ background:none; padding:0 }}
  p code {{ background:#f0f0f0; padding:2px 5px; border-radius:3px }}
</style>
</head>
<body style="font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;
             max-width:600px;margin:0 auto;padding:16px;color:#222">

<h2 style="margin:0 0 4px 0;font-size:18px">Alpha Mining Digest</h2>
<p style="margin:0 0 16px 0;color:#666;font-size:14px">
  Session <strong>{session}</strong> &middot; {strategy} &middot;
  {budget}/{budget_cap} budget &middot; {gate_passers} gate-passers &middot;
  <em>{status}</em>
</p>

<h3 style="margin:0 0 8px 0;font-size:15px">Submission Candidates</h3>
{candidates_html}

<h3 style="margin:16px 0 8px 0;font-size:15px">Session Details</h3>
<div style="font-size:14px;line-height:1.5">{body_html}</div>

<p style="margin-top:20px;font-size:13px;color:#666">
  <a href="{pr_url}" style="color:#1976d2">View full PR on GitHub</a>
</p>

</body>
</html>"""


def main():
    parser = argparse.ArgumentParser(description="Format mining email digest from meta.md")
    parser.add_argument("--meta-file", required=True, help="Path to the session meta.md file")
    parser.add_argument("--pr-url", required=True, help="URL of the GitHub PR")
    parser.add_argument("--output-dir", default="/tmp", help="Directory for output files")
    args = parser.parse_args()

    meta_path = Path(args.meta_file)
    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    if not meta_path.exists():
        print(f"ERROR: meta.md not found at {meta_path}", file=sys.stderr)
        sys.exit(1)

    meta, body = parse_meta_file(meta_path)

    if not meta.get("id"):
        print("ERROR: meta.md has no 'id' field in frontmatter", file=sys.stderr)
        sys.exit(1)

    subject = format_subject(meta)
    html = format_html(meta, body, args.pr_url)

    (out_dir / "email_subject.txt").write_text(subject)
    (out_dir / "email_body.html").write_text(html)

    print(f"Email formatted: {subject}", file=sys.stderr)


if __name__ == "__main__":
    main()
