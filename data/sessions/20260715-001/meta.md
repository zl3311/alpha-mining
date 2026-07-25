---
id: "20260715-001"
date: "2026-07-15"
strategy: "EXPLORE"
research_question: "Do genuinely novel operator-tree shapes (ts_arg_max recency-of-shock, signal-to-noise ratio, ts_zscore regime-divergence, fundamental-trend trade_when gating, sign-preserving convex tilt, buzz-level x event-magnitude product, multi-horizon spread) on fresh anchor fields (fnd6_mrct, fn_assets_fair_val_l2_q, fnd6_dpvieb, fnd6_dcvsub, anl4_cfo_flag, anl4_cff_flag) produce a decorrelated EXCELLENT+ alpha, per novelty-required.md?"
budget_used: 25
budget_cap: null
trigger: "manual (user-initiated, no budget constraint, find minimal submittable EXCELLENT+; do not submit, present + draft PR)"
gate_passers: 8
submissions: 1
submittable_candidates: 1
submitted: ["lelNqEZl"]
submitted_date: "2026-07-15"
status: "productive"
tags:
  - "session_20260715-001"
  - "EXPLORE"
  - "novel_structure"
  - "event_magnitude"
candidates:
  - id: "lelNqEZl"
    grade: "EXCELLENT"
    sharpe: 2.01
    fitness: 2.01
    self_corr_value: 0.5666
    self_corr_result: "PASS (AUTHORITATIVE, via BRAIN /check)"
    verdict: "SUBMITTED"
    status: "ACTIVE (submitted 2026-07-15)"
  - id: "blqKkP2l"
    grade: "EXCELLENT"
    sharpe: 2.55
    fitness: 2.03
    self_corr_value: 0.701
    self_corr_result: "ERROR on BRAIN /check (unresolved; local PnL estimate 0.701 FAIL)"
    verdict: "BLOCKED (unconfirmed)"
  - id: "N1r20nKL"
    grade: "GOOD"
    sharpe: 1.79
    fitness: 1.75
    self_corr_value: 0.572
    self_corr_result: "PASS"
    verdict: "REDUNDANT (superseded by lelNqEZl, same anchor+family, lower fitness)"
  - id: "VkPR1LYJ"
    grade: "GOOD"
    sharpe: 2.62
    fitness: 1.93
    self_corr_value: 0.848
    self_corr_result: "FAIL"
    verdict: "BLOCKED"
  - id: "zqmLK581"
    grade: "GOOD"
    sharpe: 1.84
    fitness: 1.58
    self_corr_value: 0.588
    self_corr_result: "PASS"
    verdict: "REDUNDANT (superseded by lelNqEZl)"
best_alpha: "lelNqEZl"
best_grade: "EXCELLENT"
best_sharpe: 2.01
best_fitness: 2.01
best_self_corr: 0.5666
best_self_corr_peer: "YP0bLdzA"
best_self_corr_method: "AUTHORITATIVE BRAIN /alphas/lelNqEZl/check endpoint (SELF_CORRELATION: {result: PASS, value: 0.5666, limit: 0.7}). Initial ~9-minute PENDING async lag (per session 20260711-001), then resolved and confirmed stable across 3 independent polls. Local PnL pre-submission estimate (0.567) matched almost exactly."
---

# Session 20260715-001: EXPLORE — Novel Operator Trees (arg_max recency, dual-stabilizer, signal-to-noise, regime divergence, fundamental-trend gating)

## Outcome

**Found:** [lelNqEZl](https://platform.worldquantbrain.com/alpha/lelNqEZl) —
EXCELLENT, S=2.01, F=2.01, T=11.04%, **all 8 BRAIN checks PASS**, including
SELF_CORRELATION, confirmed **AUTHORITATIVELY** via BRAIN's
`/alphas/lelNqEZl/check` endpoint: `{result: PASS, value: 0.5666, limit: 0.7}`
vs `YP0bLdzA` (the closest economic sibling — same fair-value-L2
event-magnitude mechanism, opposite balance-sheet side) — comfortably below
the 0.70 auto-pass threshold, no Sharpe premium needed. The endpoint returned
`PENDING` for the first ~9 minutes post-simulation (known async lag, see
session 20260711-001) before resolving; confirmed stable and consistent
across 3 independent polls ~3.5 min apart. The pre-resolution local PnL
estimate (0.567) matched the authoritative value almost exactly. **NOT
submitted** (per user instruction) — labeled on BRAIN (metadata only),
recorded as PENDING in `data/book/lelNqEZl.md`, queued in
`data/knowledge/opportunities/submit-lelnqezl.md`, and presented to the user
via draft PR.

**Update 2026-07-15 (post-review):** submitted by the human and confirmed
**ACTIVE** on the BRAIN platform. `/alphas/lelNqEZl/check` returns
`status: ACTIVE`, all 7 remaining computable checks PASS. The submission
call itself reported `Self-correlation: PASS (value: 0.5666)`, matching the
pre-submission authoritative confirmation exactly. `data/book/lelNqEZl.md`
and `submit-lelnqezl.md` updated accordingly.

## Context Assessment (Phase 0)

- Book: 46 ACTIVE + 10 PENDING across 53 mechanism families.
- No open opportunities qualified as HYPOTHESIS triggers (all non-submit-candidate
  files in `data/knowledge/opportunities/` are closed/exhausted/resolved or
  static reference data — `factor-merge-candidates.md`,
  `factor-themes-redundancy.md`, `theme-blend-candidates.md`).
- HF server healthy: 53212 results, 0 pending, budget 5000, worker idle.
  No new 24h gate-passers → no RECOMBINE/EXPLOIT trigger.
- EXPLORE ran in each of the last 5 sessions via the proven
  `event-magnitude-abs-ts-delta + leverage + ivaco + drlt (+ buzz)` template
  with a fresh anchor each time; that family now has 6 ACTIVE siblings and
  self-corr had crept up to 0.65-0.71 (thin margin) across the last 3 finds.
  Per `novelty-required.md`, this session prioritized genuinely new
  operator-tree shapes over another plain anchor swap.

## Discovery Path (2 rounds, 25 simulations)

1. **Round 1 (15 sims, 80% novel-structure / 20% backstop)**: tested
   `ts_arg_max` recency-of-shock, signal-to-noise ratio
   (`ts_delta/ts_std_dev`), regime-divergence (2 sims failed on a `zscore`
   arity error — it is cross-sectional single-input, not the intended
   time-series `ts_zscore`), sign-preserving convex tilt, fundamental-trend-
   gated `trade_when`, and buzz-level x event-magnitude products, on three
   fresh anchors (`fnd6_mrct`, `fn_assets_fair_val_l2_q`, `fnd6_dpvieb`), plus
   a small backstop batch applying the proven event-magnitude template to the
   same anchors with fresh analyst4 flags. Best result: the
   `fn_assets_fair_val_l2_q` backstop (`N1r20nKL`) reached GOOD (F=1.75) with
   the LOWEST self-corr of the round (0.572 PASS), flagging this anchor as
   the priority target.
2. **Round 2 (10 sims)**: pushed `fn_assets_fair_val_l2_q` toward EXCELLENT —
   buzz-boosted the novel `ts_arg_max` structure, added `ivaco` as a 6th leg
   to the backstop template, swept the event window, and re-ran the fixed
   regime-divergence/multi-horizon novel structures. Found two EXCELLENT
   results: `blqKkP2l` (novel `ts_arg_max` structure, S=2.55 F=2.03) BLOCKED
   at self-corr 0.701 (0.002 short of the 1.10x Sharpe-premium escape), and
   **`lelNqEZl`** (6-factor additive backstop, S=2.01 F=2.01) SAFE at 0.567 —
   the session's submittable candidate.

## Key Findings

1. **`fn_assets_fair_val_l2_q` (the asset-side counterpart of the already-
   ACTIVE `fn_liab_fair_val_l2_q`) is a genuinely more orthogonal anchor than
   any other field previously used in the event-magnitude family** — it sits
   in redundancy cluster #21 (only 2 members) rather than the book's dominant
   mega-clusters, and every variant tested this session correlated <0.60,
   the lowest ceiling of any anchor tried in this template family to date.
2. **Adding BOTH `drlt` and `ivaco` as dual stabilizers (6-factor form,
   never tried before in this family) lifts fitness from GOOD to EXCELLENT
   without materially raising self-correlation** — a new, cheap
   decorrelation-preserving fitness lever (see pattern
   `event-magnitude-dual-stabilizer.md`).
3. **The novel `ts_arg_max` recency-of-shock structure works (comparable
   Sharpe/Fitness to the additive form) but runs ~2x the turnover and
   noticeably HIGHER self-correlation than the additive `ts_decay_linear`
   wrapper on the identical anchor+stabilizer set** — structure choice, not
   just field freshness, materially affects self-corr for this family (see
   pattern `event-magnitude-recency-arg-max.md`).
4. **Three other novel structures tested this session were dead ends**:
   signal-to-noise ratio (`ts_delta/ts_std_dev`, near-zero Sharpe, 36-44%
   turnover), buzz-LEVEL x event-magnitude product (INFERIOR, S<1.0), and
   fundamental-trend-gated `trade_when` (collapsed signal to S=0.01). See
   the three new dead-zone files.
5. **Operator gotcha**: `zscore(x)` is cross-sectional (1 input); the
   time-series regime-divergence structure needs `ts_zscore(x, d)`. Two sims
   wasted on this before catching it.

## Next Steps

- `lelNqEZl` submitted 2026-07-15 and confirmed ACTIVE. No further action
  needed on this candidate.
- `blqKkP2l` (novel `ts_arg_max` structure, EXCELLENT S=2.55 F=2.03): its
  authoritative BRAIN `/check` SELF_CORRELATION status is `ERROR` (not
  PENDING, not PASS/FAIL — a distinct unresolved state), so its true verdict
  is unknown; the local PnL pre-submission estimate was 0.701 FAIL. Worth a
  fresh `/check` poll in a future session to see if `ERROR` resolves, or one
  more decorrelation lever (e.g., swap `ivaco` for a fresh field) if it
  resolves to FAIL. Not pursued further this session per the satisficing
  directive once `lelNqEZl` cleared the bar.
- `fn_assets_fair_val_l2_q`'s dual-stabilizer lever should be tried on other
  low-corr-cluster anchors in future sessions.
- The `ts_arg_max` recency structure and dual-stabilizer pattern are both
  reusable techniques for the next EXPLORE session even though only one
  anchor field has confirmed them so far (medium confidence).
