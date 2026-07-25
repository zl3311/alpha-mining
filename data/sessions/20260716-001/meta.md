---
id: "20260716-001"
date: "2026-07-16"
strategy: "EXPLORE"
research_question: "The event-magnitude-abs-ts-delta + {ivaco/drlt/fatl/anl4_*_flag/buzz*(-ret)} stabilizer skeleton is now CONFIRMED BLOCKED at self-corr 0.796 regardless of anchor (sessions 20260715-002/003, unmerged draft PRs #91/#92, 101 combined sims). Can genuinely different operator-tree structures (multi-horizon spread, moving-average crossover, ts_zscore regime divergence, product interaction, pure decay-linear wrap, leverage-free minimal stabilizer sets) on fresh, small-redundancy-cluster anchors NOT previously used in any book/factor entry (fnd6_cld2, fn_op_lease_min_pay_due_in_5y_a, fnd6_fopo, snt_social_value, unsystematic_risk_last_360_days) produce a decorrelated EXCELLENT+ alpha while avoiding every confirmed-dead skeleton component?"
budget_used: 88
budget_cap: null
trigger: "manual (user-initiated, no budget constraint, find minimal submittable EXCELLENT+; do not submit, present + draft PR)"
gate_passers: 48
submissions: 1
submitted: ["aknmG1M6"]
submitted_date: "2026-07-16"
submittable_candidates: 1
status: "productive"
tags:
  - "session_20260716-001"
  - "EXPLORE"
  - "novel_structure"
  - "post-density-wall"
  - "leverage-free"
candidates:
  - id: "aknmG1M6"
    grade: "EXCELLENT"
    sharpe: 2.29
    fitness: 2.26
    self_corr_value: 0.6181
    self_corr_result: "PASS (AUTHORITATIVE, confirmed via BRAIN /check post-submission, vs WjGVJ7bN S=2.63; local pre-submission estimate 0.618 matched almost exactly)"
    verdict: "SUBMITTED"
    status: "ACTIVE (submitted 2026-07-16 by human)"
  - id: "GrLjgZrx"
    grade: "EXCELLENT"
    sharpe: 2.16
    fitness: 2.21
    self_corr_value: 0.926
    self_corr_result: "BLOCKED (local estimate, far above threshold, vs rKlo39p1)"
    verdict: "BLOCKED"
  - id: "mLbnoxP2"
    grade: "EXCELLENT"
    sharpe: 2.01
    fitness: 2.03
    self_corr_value: 0.776
    self_corr_result: "BLOCKED (local estimate, vs WjGVJ7bN)"
    verdict: "BLOCKED"
  - id: "aknmGlax"
    grade: "EXCELLENT"
    sharpe: 2.23
    fitness: 2.13
    self_corr_value: 0.641
    self_corr_result: "UNCONFIRMED (local estimate; 0.93 mutual corr with aknmG1M6 -- redundant, not an independent second candidate)"
    verdict: "REDUNDANT (superseded by aknmG1M6, same family, lower fitness)"
best_alpha: "aknmG1M6"
best_grade: "EXCELLENT"
best_sharpe: 2.29
best_fitness: 2.26
best_self_corr: 0.6181
best_self_corr_peer: "WjGVJ7bN (S=2.63)"
best_self_corr_method: "AUTHORITATIVE BRAIN /alphas/aknmG1M6/check endpoint (SELF_CORRELATION: {result: PASS, value: 0.6181, limit: 0.70}), confirmed post-submission. During discovery the endpoint returned PENDING/timed out across 8+ polls over 20+ minutes and briefly threw httpx.ConnectTimeout (transient platform degradation, matching sessions 20260715-002/003's same-week reports); it resolved cleanly once retried after submission. Pre-submission local PnL estimate (0.618) matched the authoritative value almost exactly."
---

# Session 20260716-001: EXPLORE — Leverage-Free Fresh-Anchor Blend (Post Density-Wall)

> **Correction (added 20260719-001).** This session's research question opened
> from the premise that the stabilizer skeleton was "CONFIRMED BLOCKED at
> self-corr 0.796 regardless of anchor". That 0.796 was `oml0kV52`'s value,
> misattributed to `N1rlJ7mq` (true value **0.6903 PASS**, now ACTIVE), so the
> skeleton was never blocked regardless of anchor — the leverage leg is the
> load-bearing correlate. This does not affect the session's own result:
> `aknmG1M6` is independently confirmed at 0.6181 PASS and is ACTIVE. See
> `data/knowledge/rules/pstkrv-family-multiplier-exception.md`.

## Outcome

**Found:** [aknmG1M6](https://platform.worldquantbrain.com/alpha/aknmG1M6) —
`ts_decay_linear(rank(fnd6_cld2 / close) + rank(fnd6_fopo / close) + 2 * rank(fnd6_ivaco / close) + 2 * rank(ts_mean(scl12_buzz, 10) * (-1 * returns)), 5)`
— EXCELLENT, S=2.29, F=2.26, T=11.9%, all 8 BRAIN checks PASS, including
SELF_CORRELATION, confirmed **AUTHORITATIVELY** via BRAIN's
`/alphas/aknmG1M6/check` endpoint: `{result: PASS, value: 0.6181, limit:
0.70}` vs `WjGVJ7bN` (S=2.63) — comfortably below the 0.70 auto-pass
threshold, no Sharpe premium needed. This is the lowest self-corr of any
EXCELLENT-grade candidate found this session, well below the 0.775-0.926
range confirmed BLOCKED for every full-stabilizer-stack variant tested in
parallel. The endpoint had returned `PENDING`/timed out for the first ~20+
minutes post-discovery (transient platform degradation, matching sessions
20260715-002/003) before resolving; the pre-resolution local PnL estimate
(0.618) matched the authoritative value almost exactly. **Presented to the
user via draft PR without submitting** (per user instruction) — labeled on
BRAIN (metadata only) pending review.

**Update 2026-07-16 (post-review):** submitted by the human and confirmed
**ACTIVE** on the BRAIN platform. `/alphas/aknmG1M6/check` returns `status:
ACTIVE`, all 8 checks PASS. `data/book/aknmG1M6.md` and
`submit-aknmg1m6.md` updated accordingly.

## Context Assessment (Phase 0)

- Book: 46 ACTIVE + 10 PENDING across 53 mechanism families.
- **Critical update discovered at session start**: two unmerged cloud-
  automation sessions ran overnight (`20260715-002` PR #91, `20260715-003`
  PR #92, 101 combined sims) and confirmed the proven event-magnitude
  stabilizer skeleton is BLOCKED at self-corr 0.796 (human-confirmed)
  regardless of anchor, and that the block generalizes to essentially any
  sufficiently-strong secondary leg drawn from the book's dominant families.
- No open HYPOTHESIS-priority opportunities; EXPLORE selected as default
  (2 of last 3 sessions were EXPLORE, but the proven architecture was newly
  confirmed exhausted, warranting a fresh EXPLORE push per
  `novelty-required.md` rather than pivoting to EXPLOIT/RECOMBINE on
  effectively-dead leads).
- HF server healthy at session start (53347 results, 0 pending, budget
  4888); BRAIN platform itself began showing degradation (429s, then
  ConnectTimeout) partway through the session when checking self-corr.

## Discovery Path (14 rounds, 88 simulations)

1. **Round 1 (18 sims)**: tested genuinely novel operator-tree shapes
   (multi-horizon spread, MA crossover, `ts_zscore` regime divergence, pure
   `ts_decay_linear` wrap, fresh+fresh additive/product blends, negation
   direction, fresh sentiment `snt_social_value`) on 3 fresh anchors
   (`fnd6_cld2`, `fn_op_lease_min_pay_due_in_5y_a`, `fnd6_fopo`). All
   INFERIOR — best F=0.94 (pure decay wrap on `fnd6_cld2`).
2. **Round 2 (12 sims)**: pivoted to the completely untapped `model51`
   dataset (idiosyncratic/systematic risk vs SPY) as a genuinely fresh
   dimension. All INFERIOR — turnover 28-56% regardless of `decay_linear`
   wrapping, capping fitness despite decent Sharpe (0.8-1.4).
3. **Rounds 3-4 (16 sims)**: tested fresh anchors + `-1*equity/assets`
   (leverage) ONLY, no ivaco/drlt/flag/buzz — reached AVERAGE (F up to 1.19,
   product form).
4. **Round 5 (6 sims)**: tested the FULL proven stabilizer stack
   (leverage+ivaco+drlt+buzz) on the fresh anchors — reached EXCELLENT
   (F=2.00-2.21) for the first time this session. Local self-corr check
   revealed all 3 EXCELLENT variants BLOCKED (0.775-0.926) — confirming and
   extending the `pstkrv-mibnq-generic-stabilizer` finding to two more
   anchors.
5. **Round 6-7 (7 sims)**: tried MARKET neutralization as the proven
   decorrelation escape — reduced local corr to 0.66-0.68 but dropped grade
   to GOOD (F=1.86-1.87), not a viable EXCELLENT+ path.
6. **Round 8 (6 sims)**: isolated which single shared leg drives
   fitness/correlation by testing minimal 2-leg combinations. Found that
   dropping BOTH leverage and drlt (keeping only ivaco+drlt+buzz, no
   leverage) reached GOOD F=1.93 with local corr already down to 0.637 —
   the key breakthrough direction.
7. **Rounds 9-14 (35 sims)**: systematically tuned leg weighting (2x/3x on
   ivaco and/or buzz) and buzz window (5/10/20) around the leverage-free,
   drlt-free 4-leg skeleton (2 fresh anchors + ivaco + buzz). Found
   **`aknmG1M6`** (2x ivaco, 2x buzz window=10): EXCELLENT F=2.26, the
   session's best fitness AND lowest self-corr (0.618) simultaneously.

## Key Findings

1. **The classic event-magnitude stabilizer stack is now confirmed BLOCKED
   for self-corr regardless of anchor** — this session independently
   reproduced the `pstkrv-mibnq` finding on TWO more anchors (`fnd6_cld2`,
   `fnd6_fopo`), landing at local self-corr 0.775-0.926 with the full stack.
   See new rule `stabilizer-stack-block-generalizes-beyond-pstkrv.md`.
2. **Dropping `-1*equity/assets` and `fnd6_drlt` entirely, then
   double-weighting the remaining `fnd6_ivaco` and
   `ts_mean(scl12_buzz,10)*(-1*returns)` legs while using TWO fresh anchors
   instead of one, is a genuine free lunch**: local self-corr dropped from
   0.775 to 0.618 (-0.157) while fitness IMPROVED from 2.03 to 2.26. See new
   pattern `leverage-free-fresh-anchor-decorrelation.md`.
3. **Multi-horizon spread, MA crossover, and `ts_zscore` regime divergence
   are all dead structural templates** for fundamental fields — differencing
   two windowed statistics of a slow discrete-update fundamental produces
   near-zero signal at 15-21% turnover regardless of which specific
   fundamental field is used. New dead zone recorded.
4. **The completely untapped `model51` dataset (idiosyncratic/systematic
   risk vs SPY) is dead as a standalone alpha anchor** — its rolling-
   regression nature makes it behave like a dense daily series for
   turnover purposes (28-56%), unlike fundamentals. New dead zone recorded.
5. **BRAIN's authoritative self-correlation check can be transiently
   unreliable during platform degradation, but resolves once conditions
   clear** — repeated `/check` polls over 20+ minutes (8 attempts, mix of
   `async pending`, `429 rate-limited`, and briefly `httpx.ConnectTimeout`)
   did not resolve during the discovery window, matching session
   `20260715-002`'s independent report of the same symptom the same week.
   A retry after the human's manual submission resolved cleanly to PASS at
   0.6181 — confirming the outage was transient platform load, not a
   property of this candidate. Lesson: treat an unresolved check as
   "retry later," not as evidence against the candidate.
6. **The local PnL correlation estimate (0.618) matched the authoritative
   BRAIN value (0.6181) almost exactly for this candidate** — the closest
   local-to-authoritative match observed this week, and a useful data point
   for calibrating `self-corr-pnl-gap.md`'s underestimation warning: the
   gap appears smaller when fewer legs are shared verbatim with book peers
   (this candidate shares only `ivaco` + `buzz*(-1*returns)`, vs 3-4 shared
   legs in the confirmed-BLOCKED full-stack cases).

## Next Steps

- **Re-verify `aknmG1M6`'s authoritative BRAIN self-corr** once the platform
  API stabilizes, before any submission decision.
- If BLOCKED, the next lever to try is a THIRD fresh anchor in place of
  further leg-dropping (round 9's 3-fresh-anchor variant reached only
  AVERAGE, but that was before the 2x-weighting insight — worth retrying
  3-fresh + 2x-ivaco + 2x-buzz).
- `fnd6_cld2` and `fnd6_fopo` are both now "used" factors; future sessions
  should not re-explore their level/rank/event-magnitude forms without a
  genuinely new combination angle.
- The negation direction (`direction-diversification.md`) remains largely
  untapped this session (only 1 negation test on `fnd6_cld2`, which was
  INFERIOR) — worth a dedicated future session given the book-density wall
  now confirmed for the positive-direction additive-blend architecture.
