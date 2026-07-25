---
id: "20260713-001"
date: "2026-07-13"
strategy: "EXPLORE"
trigger: "manual (user-initiated, no budget constraint, find minimal submittable EXCELLENT+; do not submit, present + draft PR)"
status: "productive"
budget: "unlimited"
budget_used: 67
rounds: 8
research_question: "Can genuinely novel operator-tree shapes explicitly flagged as untested by prior sessions (directional gating by a SLOW fundamental's own trend rather than price/volume, ts_arg_max/ts_arg_min recency-of-extreme, multi-horizon regime-divergence spreads, dynamic correlation between two non-return fundamental series, quantile() bucketing) combined with fresh untested anchor fields (fnd6_newqv1300_msaq, current_ratio, anl4_ffo_flag) produce a decorrelated EXCELLENT+ alpha, per novelty-required.md?"
gate_passers: 35
submissions: 1
submitted: ["O0Z6NE0b"]
submitted_date: "2026-07-14"
submittable_candidates: 1
target: "EXCELLENT+ submittable (minimal viable candidate, satisfice)"
outcome: "Found EXCELLENT submittable candidate O0Z6NE0b (local self-corr estimate 0.528, SAFE; BRAIN authoritative check PENDING at session end). Presented to user + draft PR opened. Not submitted by the agent per instructions. Human submitted 2026-07-14; BRAIN confirms status ACTIVE, all checks PASS."
best_alpha: "O0Z6NE0b"
best_grade: "EXCELLENT"
best_sharpe: 2.10
best_fitness: 2.02
best_self_corr: 0.528
best_self_corr_result: "SAFE (local PnL estimate; BRAIN /check PENDING)"
tags:
  - "session_20260713-001"
  - "EXPLORE"
  - "novel_structure"
  - "event_magnitude"
  - "market_neutral"
candidates:
  - id: "O0Z6NE0b"
    grade: "EXCELLENT"
    sharpe: 2.10
    fitness: 2.02
    self_corr_value: 0.528
    self_corr_result: "PASS (confirmed post-submission: BRAIN status ACTIVE, ALL PASS)"
    verdict: "SUBMITTED"
    status: "ACTIVE (submitted 2026-07-14 by human)"
  - id: "QPVWnxKK"
    grade: "GOOD"
    sharpe: 2.53
    fitness: 1.71
    self_corr_value: 0.5667
    self_corr_result: "PASS (BRAIN authoritative)"
    verdict: "SAFE (below EXCELLENT grade target, not primary candidate)"
  - id: "KP9V7YLz"
    grade: "EXCELLENT"
    sharpe: 2.83
    fitness: 2.49
    self_corr_value: 0.646
    self_corr_result: "RISKY (local estimate)"
    verdict: "RISKY (superseded by MARKET-neutral variant O0Z6NE0b)"
  - id: "vRlY5MPd"
    grade: "EXCELLENT"
    sharpe: 2.59
    fitness: 2.43
    self_corr_value: 0.8827
    self_corr_result: "FAIL (BRAIN authoritative)"
    verdict: "BLOCKED"
---

# Session 20260713-001: EXPLORE — Novel Structures + MARKET-Neutral Escape from the Event-Magnitude Skeleton

## Research Question

See frontmatter. Full context-gather phase read all 13 rules, 20 dead zones,
22 patterns in `data/knowledge/`, all 60 `data/book/` entries, and the last 5
sessions' `meta.md` before generating any signals.

## Strategy Rationale

Decision tree evaluated top-to-bottom: no active HYPOTHESIS-mode opportunity
(all `data/knowledge/opportunities/` items are either closed/exhausted or
already-submitted queue entries); EXPLORE had run in 2 of the last 3 sessions
but remains the DEFAULT since no RECOMBINE/EXPLOIT/REFINE trigger fired (the
24h HF gate-passers were all variants within the already-6x-exploited
event-magnitude family, explicitly excluded from EXPLOIT per the decision
tree). Selected 3 fresh anchor fields via a bulk scan of 1,669
`data/knowledge/factor_profiles/` entries for standalone Sharpe >= 0.9,
excluding fields already used in `data/book/` (grepped) and dead-zone
datasets/families.

## Key Findings

1. **New dead zone**: `ts_arg_max` recency, `quantile()` bucketing, non-return
   `ts_corr`, multi-horizon spreads, and cross-dataset ratios all failed
   uniformly on fresh fundamental fields (best F=0.64) — see
   `data/knowledge/dead_zones/template-arg-max-recency-quantile-dynamic-corr.md`.
2. **New pattern (validated, self-corr PASS confirmed)**: directional gating
   of a fundamental anchor by the trend direction of a SECOND slow fundamental
   (not price/volume) is a genuinely novel, safe structure — but caps at GOOD
   grade (F<=1.88) regardless of tuning. See
   `data/knowledge/patterns/directional-gating-by-fundamental-trend.md`.
3. **New rule**: the event-magnitude family's `leverage + ivaco + buzz`
   stabilizer skeleton is now fully saturated — a fresh anchor's economic
   distinctness does NOT protect against high self-corr if the stabilizer legs
   are shared verbatim with 3+ existing siblings. `current_ratio` (liquidity,
   economically unrelated to the family) correlated WORSE (0.922) than
   `fnd6_newqv1300_msaq` (0.789-0.883). See
   `data/knowledge/rules/event-magnitude-leverage-ivaco-skeleton-saturated.md`.
4. **New pattern (the breakthrough)**: dropping `leverage` from the blend and
   switching to MARKET neutralization escapes the saturated skeleton at a
   moderate, EXCELLENT-preserving fitness cost. This produced the session's
   submittable candidate. See
   `data/knowledge/patterns/market-neutral-event-magnitude-escape.md`.
5. **Platform observation**: BRAIN's authoritative `SELF_CORRELATION` sub-check
   (`/alphas/{id}/check` and `/correlations/self`) returned `PENDING` for every
   freshly-simulated candidate this session despite 10-retry polling across
   multiple attempts — consistent with the latency pattern first documented in
   session 20260711-001. Local PnL correlation (with awareness of the
   documented 1.0x-1.6x shared-field inflation range) remains the practical
   fallback.

## Next Steps

- Re-poll `/alphas/O0Z6NE0b/check` before submission to confirm the
  authoritative `SELF_CORRELATION` result.
- The leverage-free, MARKET-neutralized event-magnitude sub-family has more
  headroom: only `ivaco+drlt+ffo_flag+buzz` on `fnd6_newqv1300_msaq` has been
  tried. Other stabilizer combinations (e.g. `fatl`, `dlto`, `current_ratio` in
  place of `drlt`) and other anchors (`fn_liab_fair_val_l2_q` under this same
  leverage-free MARKET recipe) are untested.
- The directional-gating-by-fundamental-trend pattern's GOOD-grade ceiling
  could potentially be broken by a 3-way gate (product of two `sign()` gates
  on two different slow fundamentals) — untested this session.
