---
name: mining-session
description: >-
  Master orchestrator for alpha mining sessions. Entry point for both cloud
  automation and local manual use. Reads state, selects adaptive strategy,
  chains other skills. Trigger on: session start, daily automation, mine,
  alpha mining, start mining, run session.
---

# Mining Session — Master Orchestrator

This is the entry point for every alpha mining session. Read this skill first;
it chains all other skills in the correct order.

## Session Start Protocol

1. Read THIS skill completely before doing anything else.
2. Determine whether this is a **cloud automation** or **local manual** session.
3. **Sync to latest `main` BEFORE branching** (mandatory for cloud, strongly
   recommended for local):
   ```bash
   git fetch origin && git checkout main && git pull --ff-only
   ```
   This guarantees the experiment counter, the submitted book (`data/book/`), and
   the self-corr baseline are current. Skipping this is what caused duplicate
   rediscovery and a frozen experiment counter (every run re-branched from stale
   state and re-found the same families). If `pull --ff-only` fails, stop and
   surface the conflict rather than proceeding from stale state.
4. Assign a session ID (see format below) — derive `NNN` from the freshly-synced
   `data/sessions/` so the counter actually advances.
5. **Create the session directory now** (Phase 0.5, do not defer to recording):
   create `data/sessions/YYYYMMDD-NNN/meta.md` with at least `id`, `date`,
   `strategy` (best guess, update later), and `trigger`. This guarantees an
   audit trail even if the session is interrupted. Append to it as you go.
6. Chain through the workflow in order. The workflow starts with context-gather
   (Phase 0), then applies the adaptive strategy selection (next section) to
   choose a mode, then continues through signal generation and beyond.

## Adaptive Strategy Selection

After reading context (via `context-gather` skill), select a strategy using this
decision tree evaluated top-to-bottom — first match wins:

```
READ data/knowledge/opportunities/  (ignore type: submit-candidate files —
                                     those are the submission queue, not ideas)
  └─ High-priority hypothesis/idea items exist?
       YES → HYPOTHESIS mode (test the opportunity)

CHECK: Has the agent run EXPLORE mode in the last 3 sessions?
  └─ NO → EXPLORE mode (novel templates and cross-family interactions)
       (Book is near saturation; novel structures are the highest-value use
        of budget. See data/knowledge/rules/novelty-required.md.)

CHECK multiple gate-passers from different families
  └─ 2+ gate-passers from UNEXPLOITED distinct mechanism families?
       YES → RECOMBINE mode (crossover blending of novel combos)

QUERY HF server for new gate-passers (via hf-server skill)
  └─ New gate-passer from a GENUINELY NEW mechanism family
     (not IV-spread, not analyst revision, not fundamental blend)?
       YES → EXPLOIT mode (directed mutation of the gate-passer)

CHECK existing gate-passers with BRAIN check failures
  └─ Gate-passer exists but fails one or more BRAIN checks?
       YES → REFINE mode (targeted fix for the specific failure)

DEFAULT → EXPLORE mode
```

**Key change from prior behavior**: EXPLORE and RECOMBINE now take priority over
EXPLOIT. The book is saturated with known pattern families. EXPLOIT should only
trigger for genuinely novel gate-passers from unexplored mechanism families —
NOT for more IV-spread or fundamental-blend variants.

## Workflow Chain

For every session, regardless of mode, execute these phases in order:

1. **Context Gather** — Read and execute `.cursor/skills/context-gather/SKILL.md`.
   This produces a state assessment and confirms the strategy.

2. **Signal Generation** — Read and execute `.cursor/skills/signal-generation/SKILL.md`
   with the chosen strategy mode. This produces candidate expressions.

3. **Submit Candidates** — Submit expressions to the HF server:
   ```bash
   uv run python3 scripts/hf_submit.py --expressions "expr1" "expr2" \
     --priority 5 --tags <session_tag> <batch_tag>
   ```
   Then poll the batch to completion with the canonical poller (do NOT write
   ad-hoc heredoc poll loops):
   ```bash
   uv run python3 scripts/hf_poll.py --tag <session_tag>
   ```

4. **Result Analysis** — Read and execute `.cursor/skills/result-analysis/SKILL.md`.
   This produces verdicts on each candidate AND, for any SAFE/RISKY candidate,
   labels it on the BRAIN platform via `scripts/brain_metadata.py` (the HF queue
   path leaves alphas unlabeled otherwise) and records a `status: PENDING`
   `data/book/<id>.md` entry.

5. **Iterate or Stop** — If a SAFE/RISKY candidate already meets the session's
   grade target, STOP and proceed to recording (satisficing — see AGENTS.md).
   Otherwise, if budget remains AND the improvement trend continues (at least
   one gate-passer in this round OR metrics improved over last round), return to
   step 2 with updated context (winners inform the next generation).

6. **Record** — Read and execute `.cursor/skills/experiment-reporting/SKILL.md`.
   This creates session files, updates knowledge, and opens a PR.

7. **Cleanup** — After the PR is created, the `experiment-reporting` skill's
   Step 6 handles switching back to `main` and restoring any stashed changes.
   Verify the repo is on `main` with a clean working tree before ending the session.

## Cloud vs Local Differences

| Aspect | Cloud Automation | Local Manual |
|--------|-----------------|--------------|
| Budget cap | 100 simulations per run | No hard cap (human decides) |
| End-of-session | Auto-PR (draft, never merged) | Human decides when to stop |
| BRAIN submission | NEVER submit — provide platform URLs only | Human may submit via platform URL |
| Self-corr check | Read `self_corr` from server (`hf_query --gate-passers`) | `pnl_correlation.py --vs-book` (direct BRAIN PnL) |
| Job tagging | `daily_YYYYMMDD` + batch tags | Session ID + descriptive tags |
| Trigger | Noon PT daily Cursor Automation | Human invokes skill or starts chat |
| Iteration limit | Max 5 rounds or budget exhausted | No limit |

## Session IDs

Format: `YYYYMMDD-NNN` where NNN is a zero-padded 3-digit counter.

To assign the next ID:
1. List existing directories in `data/sessions/`.
2. Filter for entries matching today's date prefix `YYYYMMDD-`.
3. Take the highest NNN found for today, increment by 1.
4. If none exist for today, start at `001`.

Example: if `data/sessions/20260603-001/` exists, the next is `20260603-002`.

## Stop Conditions

Terminate the session (proceed to recording phase) when ANY of these is true:

- **Viable candidate found** (DEFAULT for autonomous sessions): A SAFE or RISKY
  candidate exists that meets the user's grade threshold (e.g., EXCELLENT+). The
  session goal is to find ONE viable candidate, not the best possible one. Once
  found, proceed immediately to recording/PR. Only continue iterating if the user
  explicitly requested multiple candidates or specified a budget to exhaust.
- **Budget exhausted**: simulation count >= budget cap
- **Diminishing returns**: 3 consecutive rounds with zero gate-passers
- **Family blocked**: 3+ variants of the same expression family hit the SAME
  BRAIN check failure (e.g. `CONCENTRATED_WEIGHT`). Stop mutating that family
  and pivot to a structurally different template — do not keep burning sims on
  a structural block. (Lesson from 20260604-001: `group_neutralize(IV spread)`
  was EXCELLENT but always failed CONCENTRATED_WEIGHT + SUB_UNIVERSE across all
  variants; the `zscore(ts_mean(...))` template broke through.)
- **Exploration complete**: all planned directions have been tested
- **Explicit human stop**: user says to stop (local mode only)
- **Clock limit**: cloud automation has been running > 45 minutes
