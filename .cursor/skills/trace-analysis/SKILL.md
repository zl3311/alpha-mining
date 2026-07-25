---
name: trace-analysis
description: >-
  Deep-dive analysis of a single session (cloud or local). Pulls the full trace
  or transcript, walks through agent decisions, identifies failure modes, and
  recommends skill/prompt refinements. Trigger on: analyze run, trace audit,
  why did this run fail, deep dive, trace analysis, analyze session.
---

# Trace Analysis — Single-Session Deep Dive

Use this skill when you want to understand **WHY** a specific session (cloud or
local) behaved the way it did — beyond summary metrics.

## When to Use

- A cloud-agent PR's audit comment shows a compliance failure.
- A run wasted sim budget with few gate-passers.
- You want to verify whether a skill/prompt change actually changed agent behavior.
- A local session went down an unexpected path and you want to understand why.

## Step 1: Identify the target session

The user provides one of:
- A PR number (e.g., "deep dive PR #21")
- A Cursor agent ID (e.g., "analyze bc-7c8329a6-...")
- A local transcript UUID (e.g., "analyze 474c9e21-...")
- A session directory (e.g., "analyze 20260604-001")
- "the latest cloud run" or "the latest session"

### Determine session type

| Identifier | Type | Trace source |
|-----------|------|-------------|
| `bc-*` | Cloud | Cursor API SSE stream or HF file storage |
| PR number with `cloud-agent` label | Cloud | Same as above (extract `bc-*` from PR body) |
| UUID (36 chars with dashes) | Local | `agent-transcripts/<uuid>/<uuid>.jsonl` |
| `YYYYMMDD-NNN` | Local | `data/sessions/<id>/` + find matching transcript by date |

## Step 2: Pull the trace

### Cloud sessions

```bash
uv run python3 scripts/audit_cloud_trace.py \
  --agent-id <bc-id> \
  --output /tmp/trace.json
```

If the trace is expired (0 events), check the HF storage bucket:

```bash
# List available traces in the bucket
hf buckets ls <hf-user>/alpha-mining-traces/traces/
```

Or in Python:
```python
from huggingface_hub import list_bucket_files
for f in list_bucket_files('<hf-user>/alpha-mining-traces', path_prefix='traces/'):
    if 'bc-' in f.path:
        print(f.path)
```

If the trace is gone entirely, work from the PR body, audit comment, and git diff.

### Local sessions

Read the transcript JSONL directly:

```bash
TRANSCRIPT="agent-transcripts/<uuid>/<uuid>.jsonl"
wc -l "$TRANSCRIPT"  # message count
```

Extract tool calls:
```python
import json
tools = []
with open('<path>.jsonl') as f:
    for line in f:
        d = json.loads(line)
        if d.get('role') == 'assistant':
            for item in (d.get('message',{}).get('content',[]) or []):
                if isinstance(item, dict) and item.get('type') == 'tool_use':
                    tools.append({'name': item['name'], 'input': item['input']})
print(f'{len(tools)} tool calls')
for t in tools:
    name = t['name']
    inp = t['input']
    if name == 'Shell':
        print(f"  Shell: {inp.get('command','')[:120]}")
    elif name == 'Read':
        print(f"  Read: {inp.get('path','')}")
    elif name in ('StrReplace', 'Write'):
        print(f"  {name}: {inp.get('path','')}")
    else:
        print(f"  {name}: {json.dumps(inp)[:120]}")
```

Also read the session artifacts if they exist:
- `data/sessions/<id>/meta.md` — strategy and research question
- `data/sessions/<id>/results.md` — what was tested
- `data/sessions/<id>/learnings.md` — what the agent concluded

## Step 3: Reconstruct the decision timeline

Walk through the trace/transcript chronologically. Focus on:

**Context gathering phase:**
- What did the agent read first? Did it read `mining-session` before acting?
- Did it read `data/knowledge/rules/` and `data/knowledge/dead_zones/`?
- Did it check the current `data/book/` for the self-corr baseline?
- Did it consult `data/factors/` for prior coverage?

**Strategy selection:**
- What strategy did it choose and why?
- Did it follow the adaptive strategy decision tree in `mining-session`?

**Signal generation phase:**
- How many simulation batches were submitted?
- What families/templates did it explore?
- Did it waste sims on families in `data/knowledge/dead_zones/`?
- Did it respect the "3 variants same BRAIN failure -> pivot" stop condition?

**Polling and results:**
- Did it use `hf_poll.py` or ad-hoc `--stats` loops?
- How long did it wait for results?

**Verification:**
- Did it run `pnl_correlation.py --vs-book` for every candidate?
- Did it correctly interpret `SELF_CORRELATION: PENDING` from `brain_check`?
- Did it create `submit-*.md` queue entries for verified candidates?

**Reporting:**
- Did it follow the `experiment-reporting` template?
- Was the diff append-only V2 (cloud) or properly scoped (local)?

## Step 4: Classify failure modes

Map each issue to an actionable fix:

| Failure Mode | Fix Category | Action |
|-------------|-------------|--------|
| Didn't read a required skill | Prompt gap | Add explicit instruction to dispatcher |
| Read/edited V1 files | Knowledge gap + prompt | Ensure dispatcher forbids V1 |
| Wasted sims on dead family | Knowledge gap | Create/update `data/knowledge/dead_zones/` |
| Ignored a stop condition | Skill gap | Strengthen language in `mining-session` |
| Used ad-hoc polling | Skill gap | Strengthen `hf-server` skill |
| Didn't verify self-corr | Skill gap | Strengthen `result-analysis` gate |
| Missing PR metadata | Skill gap | Strengthen `experiment-reporting` template |
| Tool error / script bug | Tool gap | File a fix (separate PR) |
| Went down a rabbit hole | Context gap | Add a rule or pattern to prevent |

## Step 5: Present findings

Summarize the analysis:

1. **Timeline**: what the agent did, in what order, with time estimates
2. **Budget efficiency**: sims used vs gate-passers found
3. **Failure modes**: classified list with recommended fixes
4. **Proposed changes**: specific edits to skills, prompt, or knowledge files

The user decides which fixes to apply. Changes are committed in the current
local session.
