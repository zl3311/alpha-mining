---
id: 20260614-001
date: 2026-06-14
strategy: EXPLOIT
research_question: "Can the fresh fundamental2 share-based compensation tax-benefit ts_zscore anomaly be repaired for BRAIN concentration and sub-universe checks?"
budget_used: 22
budget_cap: null
trigger: local manual mining session via Cursor
gate_passers: 2
submissions: 1
submittable_candidates: 1
status: completed_submitted
branch: exp/20260613-001-accrual-analyst-buzz
tags:
  - "20260614-001"
  - "tax_benefit_refine"
  - "fundamental2_sparse_block"
candidates:
  - id: "JjdJxrnx"
    grade: "SPECTACULAR"
    sharpe: 1.39
    fitness: 3.06
    self_corr_value: null
    self_corr_result: "not_checked_concentration_fail"
    verdict: "BLOCKED_CONCENTRATED_WEIGHT"
  - id: "pw7e5w06"
    grade: "SPECTACULAR"
    sharpe: 1.39
    fitness: 3.06
    self_corr_value: null
    self_corr_result: "not_checked_concentration_fail"
    verdict: "BLOCKED_CONCENTRATED_WEIGHT"
  - id: "xAn2kvOp"
    grade: "EXCELLENT"
    sharpe: 1.75
    fitness: 2.21
    self_corr_value: 0.5963
    self_corr_result: "PASS"
    verdict: "SUBMITTED_ACTIVE"
---

# Session 20260614-001

Local manual mining session started from the existing dirty workspace. `git fetch
origin` succeeded, but branch-changing sync to latest `main` was skipped to avoid
disrupting in-progress session/book/server changes on the current branch.

## Phase 0 Context

STRATEGY: EXPLOIT

TARGET: Fresh share-based compensation tax-benefit anomaly from the HF server,
anchored on `ts_zscore(fn_excess_tax_benefit_from_share_based_comp_fin_activities_a, 22)`.

BUDGET: Start with 12 simulations. Iterate only if results either preserve the
SPECTACULAR annual signal or find a lower-correlation companion from related
share-based compensation fields.

CONSTRAINTS: Respect the fundamental2 dead-zone warning by treating this as a
specific template anomaly, not a broad dataset sweep. Avoid IV270, PV reversal,
volume-weighted fundamentals, `flag * (-ret)`, and negated duplicates. Use
SUBINDUSTRY/default decay first unless a BRAIN check failure points elsewhere.

RATIONALE: No active non-submit opportunity remains open. Recent sessions already
covered EXPLORE and then heavily exploited event/guidance families; the fresh
24h HF discoveries include a genuinely new fundamental2 tax-benefit mechanism
with SPECTACULAR metrics (annual S=4.10, F=10.75), making EXPLOIT the first
matching strategy in the decision tree.

## Phase 1 Candidate Slate

The raw anchor `RRroP5ra` is not directly submittable: BRAIN reports
`CONCENTRATED_WEIGHT` 0.50 vs 0.10 and `LOW_SUB_UNIVERSE_SHARPE` -1.95 vs 2.17.
Round 1 therefore tests ranking, group-ranking, and broad stabilizer blends to
diffuse weights while preserving the annual tax-benefit timing signal.

Batch tag: `tax_benefit_refine_r1`

1. `rank(ts_zscore(fn_excess_tax_benefit_from_share_based_comp_fin_activities_a, 22))`
2. `group_rank(ts_zscore(fn_excess_tax_benefit_from_share_based_comp_fin_activities_a, 22), subindustry)`
3. `ts_decay_linear(rank(ts_zscore(fn_excess_tax_benefit_from_share_based_comp_fin_activities_a, 22)), 3)`
4. `rank(ts_zscore(fn_excess_tax_benefit_from_share_based_comp_fin_activities_a, 22)) + rank(-1 * equity / assets)`
5. `rank(ts_zscore(fn_excess_tax_benefit_from_share_based_comp_fin_activities_a, 22)) + rank(fnd6_drlt / close)`
6. `rank(ts_zscore(fn_excess_tax_benefit_from_share_based_comp_fin_activities_a, 22)) + rank(-1 * equity / assets) + rank(fnd6_drlt / close)`
7. `rank(ts_zscore(fn_excess_tax_benefit_from_share_based_comp_fin_activities_a, 22)) + rank(ts_mean(scl12_buzz, 5) * (-1 * returns))`
8. `rank(ts_zscore(fn_excess_tax_benefit_from_share_based_comp_fin_activities_a, 22)) + rank(-1 * equity / assets) + rank(ts_mean(scl12_buzz, 5) * (-1 * returns))`
9. `ts_decay_linear(rank(ts_zscore(fn_excess_tax_benefit_from_share_based_comp_fin_activities_a, 22)) + rank(-1 * equity / assets) + rank(fnd6_drlt / close), 3)`
10. `rank(ts_zscore(fn_excess_tax_benefit_from_share_based_comp_fin_activities_q, 22)) + rank(-1 * equity / assets) + rank(fnd6_drlt / close)`
11. `rank(ts_zscore(fn_excess_tax_benefit_from_share_based_comp_fin_activities_a, 10)) + rank(-1 * equity / assets) + rank(fnd6_drlt / close)`
12. `rank(ts_zscore(fn_excess_tax_benefit_from_share_based_comp_fin_activities_a, 63)) + rank(-1 * equity / assets) + rank(fnd6_drlt / close)`

Submitted 12 jobs to the HF queue with tags `20260614-001` and
`tax_benefit_refine_r1`, priority 5, decay 6, SUBINDUSTRY, USA TOP3000.

## Phase 2 Round 1 Results

Batch completed with 12/12 simulations done, 0 failures, and 1 gate-passer.

| Alpha | Grade | S | F | Turnover | BRAIN Checks | Verdict |
|-------|-------|---|---|----------|--------------|---------|
| JjdJxrnx | SPECTACULAR | 1.39 | 3.06 | 10.0% | `CONCENTRATED_WEIGHT` FAIL (0.50 vs 0.10); sub-universe PASS | BLOCKED |

Expression:

`rank(ts_zscore(fn_excess_tax_benefit_from_share_based_comp_fin_activities_q, 22)) + rank(-1 * equity / assets) + rank(fnd6_drlt / close)`

### Key Finding

Adding broad leverage and deferred revenue components repaired the raw anchor's
sub-universe failure, but did not repair concentration. This suggests the
fundamental2 tax-benefit field's missing-value pattern dominates the tradable
universe: additive blends still propagate NaNs from the sparse tax field.

## Phase 3 Candidate Slate

Round 2 tests one targeted hypothesis: backfill the sparse tax-benefit field
before the z-score transform so more names receive valid weights. If this still
fails `CONCENTRATED_WEIGHT`, the family is likely structurally blocked.

Batch tag: `tax_benefit_backfill_r2`

1. `rank(ts_zscore(ts_backfill(fn_excess_tax_benefit_from_share_based_comp_fin_activities_a, 252), 22))`
2. `rank(ts_zscore(ts_backfill(fn_excess_tax_benefit_from_share_based_comp_fin_activities_a, 252), 22)) + rank(-1 * equity / assets) + rank(fnd6_drlt / close)`
3. `ts_decay_linear(rank(ts_zscore(ts_backfill(fn_excess_tax_benefit_from_share_based_comp_fin_activities_a, 252), 22)) + rank(-1 * equity / assets) + rank(fnd6_drlt / close), 3)`
4. `group_rank(ts_zscore(ts_backfill(fn_excess_tax_benefit_from_share_based_comp_fin_activities_a, 252), 22), subindustry)`
5. `rank(ts_zscore(group_backfill(fn_excess_tax_benefit_from_share_based_comp_fin_activities_a, subindustry, 252), 22)) + rank(-1 * equity / assets) + rank(fnd6_drlt / close)`
6. `rank(ts_zscore(ts_backfill(fn_excess_tax_benefit_from_share_based_comp_fin_activities_q, 63), 22)) + rank(-1 * equity / assets) + rank(fnd6_drlt / close)`
7. `rank(ts_zscore(ts_backfill(fn_excess_tax_benefit_from_share_based_comp_fin_activities_a, 504), 22)) + rank(-1 * equity / assets) + rank(fnd6_drlt / close)`
8. `rank(winsorize(ts_zscore(ts_backfill(fn_excess_tax_benefit_from_share_based_comp_fin_activities_a, 252), 22))) + rank(-1 * equity / assets) + rank(fnd6_drlt / close)`
9. `rank(ts_zscore(ts_mean(ts_backfill(fn_excess_tax_benefit_from_share_based_comp_fin_activities_a, 252), 5), 22)) + rank(-1 * equity / assets) + rank(fnd6_drlt / close)`
10. `rank(ts_zscore(ts_backfill(fn_excess_tax_benefit_from_share_based_comp_fin_activities_a, 252), 22)) * rank(-1 * equity / assets) + rank(fnd6_drlt / close)`

Submitted 10 jobs to the HF queue with tags `20260614-001` and
`tax_benefit_backfill_r2`, priority 5, decay 6, SUBINDUSTRY, USA TOP3000.

## Phase 4 Round 2 Results

Batch completed with 10/10 simulations done, 0 failures, and 1 gate-passer.

| Alpha | Grade | S | F | Turnover | BRAIN Checks | Verdict |
|-------|-------|---|---|----------|--------------|---------|
| pw7e5w06 | SPECTACULAR | 1.39 | 3.06 | 10.0% | `CONCENTRATED_WEIGHT` FAIL (0.50 vs 0.10); sub-universe PASS | BLOCKED |

Expression:

`rank(ts_zscore(ts_backfill(fn_excess_tax_benefit_from_share_based_comp_fin_activities_q, 63), 22)) + rank(-1 * equity / assets) + rank(fnd6_drlt / close)`

### Final Verdict

The tax-benefit anomaly is structurally blocked for submission. The raw annual
anchor (`RRroP5ra`) fails both concentration and sub-universe; the quarterly
blend variants repair sub-universe but still fail concentration at the same
0.50 value. Backfill did not change the binding concentration failure.

Additional fresh 24h candidates (`le0YNxQ5`, `npWl5kpx`, `qMXpAZNK`, `YPAO7zGq`,
`O09gJVxY`, `omYZEwKl`) were checked directly and were also blocked before
self-correlation, mostly by `CONCENTRATED_WEIGHT` 0.50 and/or sub-universe /
Sharpe failures.

No alpha from this session should be queued for manual submission.

## Autonomous Continuation

The user requested autonomous iteration without a quota cap until at least one
EXCELLENT+ submittable alpha was found. Before spending more simulations, the
existing queued EXCELLENT+ candidates were revalidated against the current BRAIN
checks and self-correlation.

### Stop Condition Met

`xAn2kvOp` is an unsubmitted EXCELLENT alpha that remains submittable:

- BRAIN checks: all computable checks PASS.
- Self-correlation: PASS, 0.5963 vs `xAn1LqXm`, below the raw 0.70 threshold.
- Metrics: S=1.75, F=2.21, turnover 6.47%.
- Expression:
  `rank(abs(ts_delta(fnd6_itci / close, 3))) + rank(-1 * equity / assets) + rank(fnd6_fatl / close) + zscore(ts_sum(anl4_netprofit_flag, 22))`

The local book and submission queue records for `xAn2kvOp` were corrected to
match BRAIN's authoritative expression, and metadata was pushed to the BRAIN
platform with `scripts/brain_metadata.py`.

## Session Wrap-Up

User submitted `xAn2kvOp` on BRAIN on 2026-06-14. The local book entry was
marked `ACTIVE`, the submission queue entry was marked `SUBMITTED`, and this
session is closed.
