---
id: "20260620-001"
date: "2026-06-20"
strategy: "EXPLORE"
research_question: "Can novel structural templates (multiplicative cross-field interactions, cross-dataset fundamental×options blends) unlock decorrelated SPECTACULAR alphas?"
budget_used: 78
budget_cap: null
trigger: "local_manual_mining_session"
gate_passers: 30
submissions: 0
submittable_candidates: 4
status: "completed_queued"
branch: "session/20260620-001-explore-novel"
tags:
  - "20260620-001"
  - "explore_novel"
  - "cross_dataset"
  - "multiplicative"
candidates:
  - id: "88z7MM37"
    grade: "SPECTACULAR"
    sharpe: 2.78
    fitness: 3.99
    self_corr_value: 0.6606
    self_corr_result: "PASS"
    verdict: "WINNER"
  - id: "mL8JEG7x"
    grade: "SPECTACULAR"
    sharpe: 2.53
    fitness: 3.73
    self_corr_value: 0.6637
    self_corr_result: "PASS"
    verdict: "BACKUP"
  - id: "58w3POwJ"
    grade: "SPECTACULAR"
    sharpe: 2.31
    fitness: 3.47
    self_corr_value: 0.6528
    self_corr_result: "PASS"
    verdict: "BACKUP_MARKET"
  - id: "npgYLmvM"
    grade: "SPECTACULAR"
    sharpe: 2.42
    fitness: 3.45
    self_corr_value: 0.7585
    self_corr_result: "PASS_PREMIUM"
    verdict: "BACKUP"
---

# Session 20260620-001: EXPLORE — Novel Structural Templates

## Phase 0 Context

STRATEGY: EXPLORE
TARGET: Structurally novel operator trees — multiplicative interactions, cross-dataset fundamental6×IV60 blends, non-linear combinations
BUDGET: No cap (iterate until SPECTACULAR submittable found)
CONSTRAINTS: novelty-required (>=50% novel templates), avoid saturated families (PV reversal, flag*(-ret), IV270 without premium), avoid dead zones
RATIONALE: Default EXPLORE — all opportunities are closed/exhausted, no genuinely new mechanism family in 24h discoveries (all IV60 variants from last session), book is near saturation requiring structural novelty

## Round 1: Pure Novel Structures (20 sims, 1 gate-passer)

Tested 20 structurally novel candidates across untested datasets (model51 beta/risk, option9 PCR, option8 IV-realized spread) and novel structures (multiplicative, multi-horizon spreads, conditional).

**Results:** All novel standalone datasets INFERIOR. Only `rank(fnd6_acdo/close)^2` (convex accrual) gate-passed at AVERAGE (S=1.36).

**Key learning:** Novel datasets (beta, PCR, IV-realized spread, idiosyncratic risk) are dead on BRAIN — well-arbitraged by community. Non-linear combinations of proven fields are the viable path.

## Round 2: Multiplicative & Additive Combos (20 sims, 9 gate-passers)

Tested multiplicative `rank(F1/close) * rank(F2/close)` and additive blends of proven fundamental6 fields.

**Gate-passers (6 EXCELLENT):**
| Alpha | Grade | S | F | Expression |
|-------|-------|---|---|-----------|
| N1pq2RE7 | EXCELLENT | 2.44 | 2.27 | itci + acdo + drlt additive |
| vRLxozYr | EXCELLENT | 2.31 | 2.20 | itci + acdo (decay=5) |
| 88z7Xx1X | EXCELLENT | 2.28 | 2.19 | itci × acdo multiplicative |
| MPpqVe78 | EXCELLENT | 2.25 | 2.16 | itci × drlt multiplicative |
| MPpqVe78 passes ALL BRAIN checks; others fail LOW_SUB_UNIVERSE_SHARPE.

**Key learning:** Multiplicative `rank(F1) * rank(F2)` is structurally novel and produces EXCELLENT signals. itci×drlt is the strongest ALL-PASS combination.

## Round 3-4: Refinement & Decorrelation Attempts (25 sims)

- MARKET neutralization kills all pure fundamental signals
- itci×fatl, itci×ivaco, itci×dlto: GOOD but not EXCELLENT
- Higher platform decay doesn't meaningfully reduce self-correlation at 2% turnover
- Self-corr check: MPpqVe78 has corr=0.7289 vs 0m8GV1Pp → BLOCKED

## Round 5b: Cross-Dataset Breakthrough (10 sims, 8 gate-passers)

Combined proven fundamental6 multiplicative with IV60 options data.

**ALL 8 gate-passers are SPECTACULAR (S=1.86-2.75, F=2.41-4.03)!**

## Round 6: Sub-Universe Fix (10 sims, 10 gate-passers, ALL SPECTACULAR)

Added 4th factor coverage and tuned IV60 smoothing to fix sub-universe checks.

**Winner: 88z7MM37**

Expression:
```
ts_decay_linear(rank(fnd6_itci / close) + zscore(ts_mean(implied_volatility_call_60 - implied_volatility_put_60, 44)) + rank(fnd6_drlt / close) + rank(fnd6_acdo / close), 5)
```

Settings: decay=6, SUBINDUSTRY, USA TOP3000

Metrics:
- Grade: SPECTACULAR (S=2.78, F=3.99, T=5.6%, Ret=25.7%)
- All computable BRAIN checks: PASS (sub-universe: 1.20 vs 1.20 limit)
- Self-correlation: 0.6606 vs npWYoqQz (below 0.70 threshold, AUTO PASS)
- Correlation with 0m8GV1Pp (event-magnitude): only 0.46 (IV60 completely decorrelates)

Mechanism: 4-factor additive blend combining:
1. Inventory/total capital investment level (fnd6_itci/close) — balance sheet quality
2. IV60 call-put skew 44-day smoothed zscore — options market directional sentiment
3. Deferred revenue/total liabilities (fnd6_drlt/close) — revenue quality/timing
4. Accumulated depreciation/close (fnd6_acdo/close) — capital intensity value

The cross-dataset combination of fundamental6 (50% coverage, slow-changing) with option8 IV60 (97% coverage, fast-changing) creates a structurally decorrelated alpha that captures both value AND sentiment dimensions simultaneously.

## Summary Statistics

| Metric | Value |
|--------|-------|
| Total sims | 78 |
| Gate-passers | 30 |
| SPECTACULAR candidates | 18 |
| Submittable (ALL PASS + self-corr PASS) | 4 |
| Best alpha | 88z7MM37 SPECTACULAR S=2.78 F=3.99 |
| Self-corr margin | 0.039 (below 0.70 threshold) |
