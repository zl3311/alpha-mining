---
name: session-review
description: >-
  On-demand review orchestrator for both cloud agent runs and local manual
  sessions. Aggregates recent sessions, reads traces/transcripts, identifies
  lessons to promote to the knowledge base. Trigger on: review sessions,
  review cloud runs, review local sessions, session review, audit sessions,
  what did the agent do, weekly review.
---

# Session Review — Unified Audit Orchestrator

This is the review-side counterpart to `mining-session`. While `mining-session`
drives the mining workflow, `session-review` drives the human review of what any
session (cloud or local) produced.

## Session types and their data sources

| Session Type | Trace Source | Artifacts |
|-------------|-------------|-----------|
| **Cloud agent** | SSE trace via Cursor API (`scripts/audit_cloud_trace.py`), archived on HF (`<hf-user>/alpha-mining-traces`) | Draft PR (never merged, `cloud-agent` label), GHA audit comment |
| **Local manual** | JSONL transcript in `agent-transcripts/<uuid>/` | Merged PR, `data/sessions/<id>/` artifacts |

Both types produce the same kinds of findings: factors, knowledge, candidates,
patterns, and failure modes. The review process is the same regardless of source.

## When to Use

Trigger this skill whenever you want to review recent sessions. There is no fixed
cadence — run it after a batch of cloud runs, after a productive local session, or
on a regular schedule if you prefer.

## Workflow

### Step 1: Gather sessions to review

**Cloud sessions** — list unreviewed cloud-agent PRs:
```bash
gh pr list --label cloud-agent --state open --json number,title,createdAt
```

Optionally aggregate with the review script:
```bash
uv run python3 scripts/weekly_review.py --days 7
```

**Local sessions** — list recent session directories:
```bash
ls -lt data/sessions/ | head -10
```

And list recent local transcripts:
```bash
ls -lt agent-transcripts/ | head -10
```

Cross-reference session directories with transcripts by date/content to identify
which sessions to review.

### Step 2: Read session outputs

**For cloud sessions**: read the GHA-posted audit summary comment on each PR. It
covers compliance metrics, tool usage, V1/V2 regression, and verification gate.
The PR body's `CLOUD-AGENT-METADATA` block has structured data (strategy, budget,
candidates).

**For local sessions**: read the session artifacts:
- `data/sessions/<id>/meta.md` — strategy, research question, status
- `data/sessions/<id>/results.md` — expressions tested, gate-passers
- `data/sessions/<id>/learnings.md` — what worked, what didn't

For deeper investigation, read the local transcript JSONL:
```bash
# List tool calls in a local session
python3 -c "
import json
with open('agent-transcripts/<uuid>/<uuid>.jsonl') as f:
    for line in f:
        d = json.loads(line)
        if d.get('role') == 'assistant':
            for item in (d.get('message',{}).get('content',[]) or []):
                if isinstance(item, dict) and item.get('type') == 'tool_use':
                    print(f'{item[\"name\"]}: {json.dumps(item[\"input\"])[:120]}')
"
```

Or use the `trace-analysis` skill for a structured deep dive.

### Step 3: Identify findings to promote

For each session, determine what is worth promoting to the knowledge base:

- **New factors**: field gate-passed for the first time and no
  `data/factors/<field>.md` exists. Create using `experiment-reporting` Step 2.
- **New rules**: hard constraint discovered (always fails). Create
  `data/knowledge/rules/<name>.md`.
- **New dead zones**: dataset/field/family proven dead. Create
  `data/knowledge/dead_zones/<name>.md`.
- **New patterns**: technique that works well and should be reused. Create
  `data/knowledge/patterns/<name>.md`.
- **Skill/prompt fixes**: audit flagged a recurring failure mode. Draft edits to
  the relevant skill or note a prompt update for the dispatcher.

Present proposed promotions to the user for confirmation before creating files.

### Step 4: For deeper investigation

If a specific session (cloud or local) needs a deep dive, use the
`trace-analysis` skill:

```
Read .cursor/skills/trace-analysis/SKILL.md and analyze <session identifier>
```

The session identifier can be a PR number, agent ID, transcript UUID, or session
directory name.

### Step 5: Close reviewed cloud PRs

Cloud-agent PRs are audit-only. After extracting lessons, close each with a
summary comment:

```bash
gh pr comment <N> --body "Reviewed <date>. Lessons promoted: <list or 'none'>. Closing."
gh pr close <N>
```

Local session PRs are already merged — no action needed.

### Step 6: Commit knowledge updates

If any knowledge files were created/updated, commit them:

```bash
git add data/factors/ data/knowledge/
git commit -m "Session review: promote findings (<date>)"
```

## Script Reference

| Script | Purpose |
|--------|---------|
| `scripts/weekly_review.py` | Aggregate cloud-agent PR audit summaries into digest |
| `scripts/audit_cloud_trace.py` | Pull and audit a single cloud run's trace |
