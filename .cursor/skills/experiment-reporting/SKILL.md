---
name: experiment-reporting
description: >-
  End-of-session recording. Creates session files, updates knowledge base,
  creates/updates factor and book entries, and opens a PR. Trigger on:
  report, record, document, end session, wrap up, create PR.
---

# Experiment Reporting — Session Recording

End-of-session skill. Creates all artifacts, updates the knowledge base, and
opens a PR with the session's findings.

## Step 1: Create Session Directory

Create `data/sessions/YYYYMMDD-NNN/` with three files.

### meta.md

```markdown
---
id: "YYYYMMDD-NNN"
date: "YYYY-MM-DD"
strategy: "<HYPOTHESIS | EXPLOIT | EXPLORE | RECOMBINE | REFINE>"
research_question: "<one sentence describing what this session investigated>"
budget_used: <number of simulations consumed>
budget_cap: <100 for cloud, null for manual>
trigger: "<cloud_automation | manual>"
gate_passers: <count of expressions that passed Sharpe/Fitness gates>
submissions: <count of alphas submitted to BRAIN, usually 0>
submittable_candidates: <count of SAFE/RISKY candidates>
status: "<productive | inconclusive | dead_end>"
tags:
  - "<session_tag>"
  - "<strategy_tag>"
candidates:
  - id: "<8-char BRAIN alpha ID>"
    grade: "<SPECTACULAR | EXCELLENT | GOOD | AVERAGE>"
    sharpe: <value>
    fitness: <value>
    self_corr_value: <BRAIN self-corr value from /check>
    self_corr_result: "<PASS | FAIL>"
    verdict: "<SAFE | RISKY | BLOCKED | REDUNDANT>"
---

# Session YYYYMMDD-NNN: <Title>

## Research Question
<Expanded description of what was tested and why>

## Strategy Rationale
<Why this strategy was chosen, what context led to it>

## Key Findings
<Bullet list of the most important discoveries>

## Next Steps
<What should the next session do based on these findings?>
```

### results.md

```markdown
---
id: "YYYYMMDD-NNN-results"
session: "YYYYMMDD-NNN"
total_expressions: <count>
gate_passers: <count>
best_sharpe: <value>
best_fitness: <value>
best_alpha_id: "<id or null>"
---

# Results: Session YYYYMMDD-NNN

## Summary Metrics

| Metric | Value |
|--------|-------|
| Expressions tested | X |
| Gate-passers (S>=1.25, F>=1.0) | Y |
| Best Sharpe | Z |
| Best Fitness | W |
| Budget used | N / cap |

## Gate-Passers

| # | Alpha ID | Expression | Sharpe | Fitness | Turnover | Family | Verdict |
|---|----------|-----------|--------|---------|----------|--------|---------|
| 1 | ...      | ...       | ...    | ...     | ...      | ...    | ...     |

## All Expressions Tested

| # | Expression | Sharpe | Fitness | Turnover | Status |
|---|-----------|--------|---------|----------|--------|
| 1 | ...       | ...    | ...     | ...      | GATE_PASS / BELOW_GATE / ERROR |

## BRAIN Check Results (if applicable)

| Alpha ID | LOW_SHARPE | LOW_FITNESS | LOW_TURNOVER | HIGH_TURNOVER | CONCENTRATED_WEIGHT | LOW_SUB_UNIVERSE_SHARPE | SELF_CORRELATION | MATCHES_COMPETITION |
|----------|------------|-------------|--------------|---------------|---------------------|-------------------------|------------------|---------------------|
| ...      | PASS       | PASS        | PASS         | PASS          | PASS                | PASS                    | PENDING          | PASS                |
```

### learnings.md

```markdown
---
id: "YYYYMMDD-NNN-learnings"
session: "YYYYMMDD-NNN"
category: "<discovery | dead_end | refinement | pattern | rule>"
confidence: "<high | medium | low>"
actionable: <true | false>
---

# Learnings: Session YYYYMMDD-NNN

## What Worked
<Bullet list of approaches that produced signal>

## What Didn't Work
<Bullet list of approaches that failed, with why>

## New Rules Discovered
<Any hard constraints found — these get promoted to data/knowledge/rules/>

## New Dead Zones
<Any datasets/fields/families proven dead — promoted to data/knowledge/dead_zones/>

## New Patterns
<Any techniques that worked well — promoted to data/knowledge/patterns/>

## Mechanism Insights
<What was learned about the economic mechanism being tested>
```

## Step 2: Update data/factors/

For any **newly discovered factor** (a field that gate-passed for the first time):

Create `data/factors/<field_name>.md`:

```markdown
---
field: "<exact BRAIN field name>"
dataset: "<dataset name>"
family: "<mechanism family>"
discovery_session: "YYYYMMDD-NNN"
best_sharpe: <value>
best_fitness: <value>
best_expression: "<expression string>"
mechanism: "<1-line economic mechanism>"
status: "<active | exhausted | dead>"
---

# Factor: <field_name>

## Economic Mechanism
<2-3 sentences explaining WHY this factor predicts returns>

## Best Known Expression
<The highest-performing expression using this factor>

## Lessons
<What works and what doesn't with this factor>
```

For existing factors with new results: do NOT edit the factor file. The session
`results.md` serves as the record of new results.

## Step 3: Update data/knowledge/

Create new knowledge files as warranted by session findings:

### Rules (data/knowledge/rules/)

Create when a hard constraint is discovered — something that ALWAYS fails.

```markdown
---
rule: "<concise rule statement>"
discovered: "YYYYMMDD-NNN"
confidence: "<high | medium>"
evidence: "<brief evidence>"
---

# Rule: <title>

<Explanation of the rule, why it exists, and what happens when violated>
```

### Dead Zones (data/knowledge/dead_zones/)

Create when a dataset, field, or family is proven to produce no signal.

```markdown
---
scope: "<dataset-X | field-Y | family-Z>"
discovered: "YYYYMMDD-NNN"
expressions_tested: <count>
best_sharpe: <value, showing it's below threshold>
---

# Dead Zone: <scope>

<Why this is dead. What was tried. Why further testing is not warranted.>
```

### Patterns (data/knowledge/patterns/)

Create when a technique works well and should be reused.

```markdown
---
pattern: "<concise pattern name>"
discovered: "YYYYMMDD-NNN"
applicable_to: "<families or contexts where this works>"
---

# Pattern: <title>

## Template
<The reusable expression template with placeholders>

## When to Use
<Conditions under which this pattern is effective>

## Example
<A concrete example that gate-passed using this pattern>
```

### Remove Consumed Opportunities

If an opportunity from `data/knowledge/opportunities/` was tested in this session,
delete or archive the file (move content into the session learnings). The opportunity
has been consumed regardless of whether it succeeded or failed.

## Step 4: Update data/book/

Create `data/book/<alpha_id>.md` in EITHER of these cases:

- **PENDING**: a SAFE/RISKY candidate that passed all checks and is recommended
  for submission but not yet submitted (the usual end state for a productive
  session — the human submits manually).
- **ACTIVE**: an alpha actually submitted to BRAIN and accepted.

Before opening the PR, for every PENDING/ACTIVE entry you MUST have pushed the
name/tags/description to the BRAIN platform (the HF queue path leaves alphas
unlabeled). If `result-analysis` Step 7 was skipped, do it now:

```bash
uv run python3 scripts/brain_metadata.py --alpha-id <alpha_id> --from-book data/book/<alpha_id>.md
```

Frontmatter template (include `name`, `tags`, and `brain_url` so the local
record matches what is on the platform):

```markdown
---
alpha_id: "<8-char BRAIN ID>"
name: "<platform display name>"
tags:
  - "<tag>"
  - "session_YYYYMMDD-NNN"
submitted: "YYYY-MM-DD or null if PENDING"
session: "YYYYMMDD-NNN"
grade: "<SPECTACULAR | EXCELLENT | GOOD | AVERAGE>"
sharpe: <value>
fitness: <value>
turnover: <value>
expression: "<full FASTEXPR expression>"
family: "<mechanism family>"
neutralization: "<MARKET | SUBINDUSTRY | INDUSTRY>"
decay: <value>
self_corr_max: <value at submission time>
status: "<ACTIVE | PENDING | REJECTED | SUPERSEDED>"
brain_url: "https://platform.worldquantbrain.com/alpha/<alpha_id>"
---

# Alpha: <alpha_id>

## Expression
```
<full expression>
```

## Mechanism
<Why this alpha works — economic reasoning>

## Self-Correlation Profile
<Which existing book entries it correlates with, and at what level>

## Post-Submission
<For PENDING: after the human submits on BRAIN, flip status to ACTIVE and set the submitted date.>
```

## Step 5: Open PR

### Append-only / conflict-free contract (CRITICAL)

A session PR MUST only **add new per-file V2 artifacts** — never edit shared or
monolithic files. This is what keeps daily PRs mergeable without conflicts. The
session branch must have been cut from a freshly-synced `main` (see
`mining-session` Session Start step 3).

Allowed changes:

- New `data/sessions/YYYYMMDD-NNN/*.md`
- New `data/factors/<field>.md` (only for first-time factors; never edit existing)
- New `data/knowledge/**` files (rules/dead_zones/patterns), and removing a
  consumed `data/knowledge/opportunities/*.md`
- New `data/book/<alpha_id>.md` and new `data/knowledge/opportunities/submit-*.md`

Forbidden in a session PR:

- Editing any existing factor/book/knowledge file that another in-flight session
  might also touch
- Touching deprecated V1 files (`data/reference/factor_inventory.json`,
  `data/reference/hypothesis_backlog.md`,
  `data/reference/brain_availability_matrix.md`, anything under
  `data/experiments/`) — these are dead; do not read or write them
- Editing code, skills, `AGENTS.md`, or `README.md` (open a separate, clearly
  labeled PR if a tooling/skill fix is genuinely needed)

### Steps

0. **Isolate unrelated changes** (if any): If `git status` shows modifications
   outside `data/` (e.g., `server/`, `src/`, `tests/`, `scripts/`), stash them
   before creating the session branch to avoid accidentally including them:
   ```bash
   git stash push -m "pre-session: unrelated changes" -- server/ src/ tests/ scripts/
   ```

1. Create a new branch named with the real session ID:
   ```bash
   git checkout -b exp/YYYYMMDD-NNN-<short_description>
   ```

2. Stage all new/changed files under `data/`:
   ```bash
   git add data/
   ```

3. Sanity-check the diff is append-only (no monolith/V1 edits) before committing:
   ```bash
   git status --short
   ```

4. Commit:
   ```bash
   git commit -m "Exp YYYYMMDD-NNN: <strategy> - <one-line summary>"
   ```

5. Push and open PR (draft for cloud automation runs):
   ```bash
   git push -u origin HEAD
   gh pr create --draft --title "Exp YYYYMMDD-NNN: <strategy> - <one-line summary>" --body "$(cat <<'EOF'
   ## Summary

   <!-- 1-3 sentences: what was discovered, key breakthrough if any -->

   ## Results

   - Expressions tested:
   - Gate-passers:
   - Best Sharpe: / Best Fitness:
   - Strategy:
   - Budget: / 100 simulations

   ## Submission Candidates

   | Alpha ID | Grade | Fitness | Self-Corr (BRAIN) | Verdict |
   |----------|-------|---------|-------------------|---------|
   | | | | | |

   (State "None this session" if no submittable candidate.)

   ## Learnings

   **What worked:**
   -

   **What didn't work:**
   -

   ## Next Steps

   -
   EOF
   )"
   ```

PR title format: `Exp YYYYMMDD-NNN: <STRATEGY> - <one-line summary>` (use the full
session ID, not a bare counter, so titles are unique across days).

All structured data for the email digest is read from `data/sessions/YYYYMMDD-NNN/meta.md`
(specifically the frontmatter `candidates` list). The PR body is human-readable only —
no machine-parseable metadata is needed there.

**Cloud PRs are audit-only** — they are never merged. The GHA auto-labels them
`cloud-agent`, posts a trace audit comment, and archives the full trace. The human
reviews them via the `session-review` skill (`.cursor/skills/cloud-review/SKILL.md`) and closes them after extracting lessons.

## Step 6: Post-PR Cleanup (Git Hygiene)

After the PR is created, restore the repo to a clean state on `main`:

1. Switch back to main:
   ```bash
   git checkout main
   ```

2. Restore any stashed unrelated changes (only if stashed in Step 5.0):
   ```bash
   git stash pop
   ```

3. Verify clean state:
   ```bash
   git status
   ```

The session branch remains on the remote (the draft PR references it). Do NOT
delete the local branch — `git checkout main` is sufficient.

**This step is mandatory.** Never end a session with the repo on an experiment
branch. The next session's `git pull --ff-only` on `main` (see `mining-session`
Step 3) will fail if the repo is on the wrong branch.
