---
name: context-gather
description: >-
  Phase 0 of every mining session. Reads current state from files and server,
  assesses the landscape, and recommends a strategy. Always run this before
  signal generation. Trigger on: context, gather, session start, assess state.
---

# Context Gather — State Assessment

Phase 0 of every mining session. Execute this skill completely before generating
any signals. The output is a strategy recommendation with justification.

## What to Read (in order)

Execute these steps sequentially. Each builds on the previous.

### 1. Submitted Book

Read all files in `data/book/`. For each entry, note:
- Alpha ID, grade (SPECTACULAR / EXCELLENT / GOOD / AVERAGE)
- Signal family (reversal, fundamental, analyst, sentiment, options, blend)
- Key fields used in the expression

Count: total submitted, by grade, by family. Identify which families are
saturated (3+ entries) vs underrepresented (0-1 entries).

### 2. Hard Rules

Read ALL files in `data/knowledge/rules/`. These are inviolable constraints.
Violations waste budget. Common rules:
- Self-corr thresholds
- Flag-ret correlation limits
- Volume interaction restrictions
- Saturation limits per family

### 3. Dead Zones

Read ALL files in `data/knowledge/dead_zones/`. These are datasets, fields,
families, or approaches proven to produce no signal. Never test these again
unless the hypothesis explicitly explains why prior tests were insufficient.

### 4. Opportunities

Read ALL files in `data/knowledge/opportunities/`. Distinguish between:
- **Hypothesis/idea items** (high-priority mechanisms to test) — these drive
  HYPOTHESIS mode if present and not closed/exhausted.
- **Submit-candidate files** (`type: submit-candidate` / `submit-*.md`) — these
  are the submission queue, NOT exploration ideas. Ignore them for strategy selection.

Skip any files with `status: closed` or `priority: exhausted/resolved`.

### 5. Recent Sessions

Read `meta.md` from the 3-5 most recent `data/sessions/*/` directories
(sorted by date descending). Understand:
- What was tried recently
- What worked and what didn't
- Whether there's a multi-session arc in progress
- Budget consumption trend

### 6. HF Server Health

Run:
```bash
uv run python3 scripts/hf_query.py --stats
```

Note: total jobs queued, running, completed. Check daily budget remaining.
If server is unhealthy or queue is full, adjust plan accordingly.

### 7. New Discoveries

Run:
```bash
uv run python3 scripts/hf_query.py --new-24h
```

Check for new gate-passers that appeared since the last session. Note the
mechanism family of each. Only gate-passers from **genuinely new mechanism
families** (not IV-spread, analyst revision, or fundamental blend) are
candidates for EXPLOIT mode. Gate-passers from known families are useful
context but should not override the EXPLORE-first default.

### 8. Novelty Rule

Read `data/knowledge/rules/novelty-required.md`. This defines the structural
novelty gate that applies to all EXPLORE sessions (the default mode).

## Strategy Assessment

Based on what you read, recommend ONE strategy. Evaluate top-to-bottom (first
match wins). The canonical decision tree lives in `mining-session/SKILL.md`;
this table is a summary:

| Priority | Strategy | Trigger | Description |
|----------|----------|---------|-------------|
| 1 | HYPOTHESIS | Active hypothesis/idea opportunity exists (not submit-candidate, not closed) | Test a specific economic mechanism |
| 2 | EXPLORE | No EXPLORE in last 3 sessions, OR default when no other trigger matches | Novel templates and cross-family interactions (see `novelty-required.md`) |
| 3 | RECOMBINE | 2+ gate-passers from UNEXPLOITED distinct mechanism families | Crossover blend of novel combinations |
| 4 | EXPLOIT | Gate-passer from a genuinely NEW family (not IV-spread, analyst revision, fundamental blend) | Directed mutations of a novel winner |
| 5 | REFINE | Gate-passer exists but fails BRAIN checks | Targeted fix for specific failure |

**Key principle**: EXPLORE is the default. The book is near saturation with known
patterns; novel expression structures are the highest-value use of budget.

## Output

State the following before proceeding to signal generation:

```
STRATEGY: <one of the five modes>
TARGET: <specific template structure / mechanism interaction / opportunity being addressed>
BUDGET: <number of simulations allocated to this session>
CONSTRAINTS: <key rules that apply (include novelty-required if EXPLORE)>
RATIONALE: <1-2 sentences explaining why this strategy was chosen and which
            decision-tree step matched>
```
