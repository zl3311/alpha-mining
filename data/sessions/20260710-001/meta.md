---
id: "20260710-001"
date: "2026-07-10"
strategy: "HYPOTHESIS"
research_question: "Can the untested singleton fields from negation-blend-candidates.md (min_tangible_book_value_per_share_guidance_2, anl4_qf_az_wol_spfc/vid, fn_comp_options_forfeitures_and_expirations_a, fn_prepaid_expense_q) plus never-tested negated tax fields (fnd6_txw, fnd6_txdbca) produce a decorrelated EXCELLENT+ alpha?"
budget_used: 70
budget_cap: null
trigger: "manual (user-initiated, no budget constraint, satisfice on first EXCELLENT+ submittable; do not submit, present + draft PR)"
gate_passers: 22
submissions: 1
submitted: ["WjGVJ7bN"]
submitted_date: "2026-07-10"
submittable_candidates: 1
status: "productive"
tags:
  - "session_20260710-001"
  - "hypothesis"
  - "event_magnitude"
candidates:
  - id: "WjGVJ7bN"
    grade: "SPECTACULAR"
    sharpe: 2.63
    fitness: 2.68
    self_corr_value: 0.7096
    self_corr_result: "PASS"
    verdict: "SUBMITTED"
    status: "ACTIVE (submitted 2026-07-10 by human)"
---

# Session 20260710-001: HYPOTHESIS — Untested Negation-Sweep Singleton Fields

## Research Question

`data/knowledge/opportunities/negation-blend-candidates.md` (priority: high,
status: untested) lists a 10-factor set-cover result and 5 negated-fundamental
building blocks from the 2026-07-05 negation profiling session. Of these:

- Item 1 (IV60 spread + guidance + bvps_flag) is now saturated —
  `kq3PVLXK`/`QPaG3OGM` (PENDING) already claim this near-exact structure.
- Item 3 (itci event-magnitude + negated leverage + drlt) and its extensions
  to tlcf/ppegtq/mrct/dcvsub are claimed across 3 unmerged draft PRs
  (#80 `2rLRzov8`, #81 `wpl5eP5v`, #82 `rKlo39p1`).
- Item 7 (`anl4_netprofit_flag`) is already ACTIVE as `vRmlGnkv`.
- Items 4-6, 8, 10 (`min_tangible_book_value_per_share_guidance_2`,
  `anl4_qf_az_wol_spfc`, `anl4_qf_az_wol_vid`, `fn_comp_options_forfeitures_and_expirations_a`,
  `fn_prepaid_expense_q`) are genuinely untested — zero coverage in
  `data/factors/` or `data/book/`.
- The negated-fundamental building blocks `fnd6_txw` and `fnd6_txdbca` are
  also genuinely untested standalone (only `fnd6_intc`/`fnd6_acqgdwl`/`fnd6_dcvsub`
  negated variants have been touched, and only in blends that hit a self-corr
  wall via `anl4_ptpr_flag`).

This session targets the untested items with proven blend/product templates,
paired with fresh analyst-forecast partners (not `ptpr`/`bvps`/`netdebt`/`cfi`
flags, which dominate existing book correlation) to maximize the chance of a
genuinely decorrelated EXCELLENT+ find.

## Pre-Existing Backlog (context, not part of this session's diff)

Three draft PRs are already open and unreviewed with EXCELLENT SAFE candidates
from the last 3 days: `2rLRzov8` (self-corr 0.6495, PR #80), `wpl5eP5v`
(0.6676, PR #81), `rKlo39p1` (0.6262, PR #82). This session proceeds with net-new
mining per the user's explicit request, targeting fields orthogonal to all three.

## Strategy

HYPOTHESIS mode (untested opportunity backlog item, priority: high, not closed).
Falls back to EXPLORE-style structural novelty for >=50% of the round per
`novelty-required.md`.

## Outcome

4 rounds, 70 simulations. Rounds 1-3 (46 sims) confirmed the untested
singleton fields are weak in level/rank/zscore/product form (capped AVERAGE,
new dead zone recorded). Round 4 (10 sims) pivoted to applying the proven
`event-magnitude + leverage + ivaco + drlt` template to the same fresh fields
and found **`WjGVJ7bN`** (`fnd6_txw` excise-tax event-magnitude + leverage +
ivaco + drlt + buzz stabilizer) — **SPECTACULAR, S=2.63, F=2.68, T=10.9%**,
self-corr 0.7096 vs ACTIVE `wpl5eP5v` (PASS via Sharpe premium). All 7 computable BRAIN checks
PASS. See `data/book/WjGVJ7bN.md` for full self-corr analysis (including the
`/check` endpoint's `ERROR` response for `SELF_CORRELATION` and why both
possible resolutions are safe).

**Update 2026-07-10 (post-review):** submitted by the human and confirmed
ACTIVE on the BRAIN platform. `data/book/WjGVJ7bN.md` and
`submit-wjgvj7bn.md` updated accordingly.
