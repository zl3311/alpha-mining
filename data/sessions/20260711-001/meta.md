---
id: "20260711-001"
date: "2026-07-11"
strategy: "EXPLORE"
trigger: "manual (user-initiated, no budget constraint, find minimal submittable EXCELLENT+; do not submit, present + draft PR)"
status: "productive"
budget: "unlimited"
budget_used: 84
target: "EXCELLENT+ submittable (minimal viable candidate, satisfice)"
research_question: "Can genuinely novel operator-tree shapes (non-volatility trade_when gating, cross-dataset ratios, ts_arg_max/ts_arg_min recency, dynamic correlation between non-return series, nonlinear rank-power tilts, multi-horizon spreads) combined with fresh untested anchor fields (fn_liab_fair_val_l2_q, anl4_gric_flag, fnd6_dltis) produce a decorrelated EXCELLENT+ alpha, per novelty-required.md?"
rounds: 9
gate_passers: 57
submissions: 1
submittable_candidates: 1
submitted: ["YP0bLdzA"]
tags:
  - "session_20260711-001"
  - "EXPLORE"
  - "novel_structure"
  - "event_magnitude"
best_alpha: "YP0bLdzA"
best_grade: "EXCELLENT"
best_sharpe: 2.32
best_fitness: 2.22
best_self_corr: 0.673
best_self_corr_peer: "WjGVJ7bN"
best_self_corr_method: "local_pnl_correlation (BRAIN /check and /correlations/self both timed out repeatedly, PENDING)"
candidates:
  - id: "YP0bLdzA"
    grade: "EXCELLENT"
    sharpe: 2.32
    fitness: 2.22
    self_corr_value: 0.673
    self_corr_result: "PASS (local pre-submission estimate; confirmed via platform acceptance)"
    verdict: "SUBMITTED"
    status: "ACTIVE (submitted 2026-07-11 by human)"
  - id: "P03ZkrkW"
    grade: "EXCELLENT"
    sharpe: 2.16
    fitness: 2.33
    self_corr_value: 0.696
    self_corr_result: "?"
    verdict: "BLOCKED"
  - id: "3qR9JvXX"
    grade: "SPECTACULAR"
    sharpe: 2.50
    fitness: 2.76
    self_corr_value: 0.797
    self_corr_result: "FAIL"
    verdict: "BLOCKED"
  - id: "RR8Vz96o"
    grade: "SPECTACULAR"
    sharpe: 2.37
    fitness: 2.54
    self_corr_value: 0.801
    self_corr_result: "FAIL"
    verdict: "BLOCKED"
  - id: "WjGPr2xd"
    grade: "SPECTACULAR"
    sharpe: 2.54
    fitness: 2.59
    self_corr_value: 0.709
    self_corr_result: "?"
    verdict: "BLOCKED"
---

# Session 20260711-001: EXPLORE — Novel Operator Trees + Fresh Anchors

## Outcome

**Found:** [YP0bLdzA](https://platform.worldquantbrain.com/alpha/YP0bLdzA) —
EXCELLENT, S=2.32, F=2.22, T=10.66%, all 7 computable BRAIN checks PASS. Max
local PnL correlation vs the full 44-alpha ACTIVE universe (39 main book + 5
recently human-submitted alphas from unmerged draft PRs #80-84) was **0.673**
vs `WjGVJ7bN` — comfortably below the 0.70 auto-pass threshold. Presented to
the user via draft PR (not submitted by the agent per instructions); labeled
on BRAIN (metadata only) pending review.

**Update 2026-07-11 (post-review):** submitted by the human and confirmed
**ACTIVE** on the BRAIN platform. `/alphas/YP0bLdzA/check` returns
`status: ACTIVE`, all 7 computable checks PASS (including
`LOW_SUB_UNIVERSE_SHARPE` resolved to 1.22 vs limit 1.0). BRAIN's
`SELF_CORRELATION` sub-check had returned `PENDING` throughout the discovery
session (10-retry polling timed out 6+ times over ~90 minutes, including for
control queries against already-ACTIVE alphas) and is no longer listed
post-submission — the platform's acceptance is itself the authoritative
confirmation that the local-PnL-based 0.673 estimate was directionally
correct. `data/book/YP0bLdzA.md` and `submit-yp0bldza.md` updated accordingly.

## Context Assessment (Phase 0)

- Book (main): 39 ACTIVE + 11 PENDING across 47+ mechanism families.
- 6 open draft PRs (#79-84) not yet merged to main; 5 of their candidates were
  already manually submitted by the human and are confirmed ACTIVE on the live
  BRAIN account (`ZYpjKeKx`, `WjGVJ7bN`, `rKlo39p1`, `wpl5eP5v`, `2rLRzov8`) —
  treated as part of the correlation universe throughout this session even
  though `main`'s `data/book/` doesn't yet reflect them. Only `GrLJLGN5` (PR
  #79) remains genuinely PENDING/unsubmitted.
- `negation-blend-candidates.md` opportunity effectively exhausted (per session
  20260710-001 notes). No RECOMBINE/EXPLOIT trigger (24h gate-passers were all
  variants within the already-5x-exploited event-magnitude family). Default:
  EXPLORE, with novelty-required.md's >=50% structural-novelty budget rule.
- Selected 3 fresh anchor fields via bulk scan of 1,669
  `data/knowledge/factor_profiles/` entries for standalone Sharpe 0.9-1.5,
  excluding all used fields/dead-zone datasets: `fn_liab_fair_val_l2_q`
  (fundamental2), `anl4_gric_flag` (analyst4), `fnd6_dltis` (fundamental6).

## Discovery Path (9 rounds, 84 simulations)

1. **Rounds 1-2 (40 sims)**: novel operator-tree shapes + proven-template
   backstops, all combined with the standard `open/close-1 + {ptpr_flag|
   netdebt_flag}` catalyst pair. Produced 2 SPECTACULAR + 5 EXCELLENT
   candidates with strong aggregate metrics, but ALL showed local PnL
   correlation 0.74-0.91 vs the book. Root-caused: several book entries
   (`LLR0n261`, `6Xzm6PQP`, `78w5d35x`, `O0ZOJbaq`) share this exact 2-leg
   skeleton verbatim — the skeleton itself, not the anchor, drives the
   correlation. Recorded as a new rule:
   `data/knowledge/rules/overnight-gap-flag-skeleton-saturated.md`.
2. **Round 3 (14 sims)**: pivoted to pure-fresh combinations (fresh anchors +
   fresh catalysts, avoiding the saturated skeleton entirely). Confirmed
   decorrelated (implicitly, by using zero shared legs) but capped at AVERAGE
   grade (F~1.0-1.14) — insufficient fitness without the proven catalyst legs.
3. **Round 4 (6 sims)**: pivoted to the proven `event-magnitude-abs-ts-delta +
   leverage + ivaco + drlt (+ buzz)` template (previously validated on
   itci/ppegtq/tlcf/txw only). Both `fn_liab_fair_val_l2_q` and `fnd6_dltis`
   reached SPECTACULAR (S=2.45-2.54) immediately. `fnd6_dltis` correlated 0.94
   with `WjGVJ7bN` (dead end, recorded in
   `data/knowledge/dead_zones/field-dltis-event-magnitude.md`); `fn_liab_fair_val_l2_q`
   correlated a more promising 0.71.
4. **Rounds 5-8 (~23 sims)**: fixed `LOW_SUB_UNIVERSE_SHARPE` (fails without a
   stabilizer) and attempted to push `fn_liab_fair_val_l2_q`'s correlation
   below 0.70 via stabilizer substitution (`fatl`/`dlto` for `drlt`) — best
   result `P03ZkrkW`/`VkPavmgJ` (S=2.16, F=2.33) still sat at 0.694-0.696, an
   uncomfortably thin margin. `trade_when` realized-vol gating (the standard
   `LOW_SUB_UNIVERSE_SHARPE` fix) failed permanently with a BRAIN unit-type
   error on this expression shape (4/4 variants) — abandoned, not resolved.
5. **Round 9 (3 sims)**: swapped the `drlt`/`fatl`/`dlto` stabilizer leg for
   the fresh, never-used-in-this-family `anl4_gric_flag`. Produced
   **`YP0bLdzA`** — EXCELLENT, S=2.32, F=2.22, correlation dropped to **0.673**
   (comfortable margin) while Sharpe/Fitness simultaneously *improved* over
   the fatl/dlto variants. Recorded as a new pattern:
   `data/knowledge/patterns/event-magnitude-fresh-stabilizer.md`.

## Key Findings

1. **A fresh anchor field is not sufficient for decorrelation if the rest of
   the blend's legs are shared verbatim with existing book entries.** The
   `open/close-1 + analyst_flag` skeleton is fully saturated; any new anchor
   on it inherits 0.74-0.91 correlation regardless of anchor novelty.
2. **Within an already-5x-exploited template family (event-magnitude +
   leverage + ivaco/drlt/buzz), substituting ONE shared stabilizer leg for a
   genuinely unused field (here, an analyst4 flag in place of a second
   fundamental6 field) is an effective and cheap decorrelation lever** — it
   dropped peer correlation from ~0.70 to 0.67 while improving fitness, not
   trading it off.
3. **Anchor-field economic proximity to existing family members predicts
   correlation better than raw field freshness**: `fnd6_dltis` (debt issuance)
   correlated 0.94 with the `fnd6_txw` (excise tax)-anchored sibling — both are
   flow items with similar event dynamics — while `fn_liab_fair_val_l2_q`
   (fair-value liability re-marking, economically distinct) correlated only
   0.67-0.71 with the same sibling on an identical template.
4. **BRAIN's authoritative self-correlation check can lag simulation
   completion by well over 90 minutes** — both `/alphas/{id}/check`'s
   `SELF_CORRELATION` sub-check and `/alphas/{id}/correlations/self` returned
   `PENDING`/timed-out for every candidate tested this session, including
   already-ACTIVE control alphas. Local PnL correlation remains the only
   practical fallback in this situation.

## Next Steps

- Re-verify `YP0bLdzA`'s BRAIN self-corr with a fresh `/check` poll before
  submission (should have resolved by the time a human reviews this PR).
- The `event-magnitude-fresh-stabilizer` pattern (swap a shared leg for an
  unused cross-dataset field) is worth applying to the other 3 borderline
  candidates from this session (`P03ZkrkW`, `VkPavmgJ`, `WjGPr2xd`) if a lower-
  corr variant is wanted later — not pursued further this session per the
  satisficing directive once `YP0bLdzA` cleared the bar.
- `fn_liab_fair_val_l2_q` still has headroom: only the event-magnitude
  transform + this one stabilizer combination has been tried; other proven
  templates (product-interaction, overnight-gap without the saturated flag)
  are untested for this specific field.
