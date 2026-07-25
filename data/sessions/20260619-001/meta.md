---
id: "20260619-001"
date: "2026-06-19"
strategy: "EXPLORE"
research_question: "Can structurally novel operator trees (multi-horizon spreads, dynamic correlation, directional gating, signal-to-noise ratios, inter-field ratios) and IV60 blend repairs unlock SPECTACULAR decorrelated alphas?"
budget_used: 48
budget_cap: null
trigger: "local_manual_mining_session"
gate_passers: 8
submissions: 0
submittable_candidates: 3
status: "completed_queued"
branch: "session/20260619-001-explore-novel"
tags:
  - "20260619-001"
  - "explore_novel"
  - "iv60_blend"
candidates:
  - id: "ZYpk2kx8"
    grade: "SPECTACULAR"
    sharpe: 1.71
    fitness: 2.52
    self_corr_value: 0.6358
    self_corr_result: "PASS"
    verdict: "QUEUED"
  - id: "kq3eLwQl"
    grade: "EXCELLENT"
    sharpe: 1.58
    fitness: 2.20
    self_corr_value: 0.6719
    self_corr_result: "PASS"
    verdict: "REDUNDANT_vs_ZYpk2kx8"
  - id: "LLpOX73M"
    grade: "EXCELLENT"
    sharpe: 1.55
    fitness: 2.13
    self_corr_value: 0.6743
    self_corr_result: "PASS"
    verdict: "REDUNDANT_vs_ZYpk2kx8"
---

# Session 20260619-001: EXPLORE — Novel Operator Trees + IV60 Blend

## Phase 0 Context

STRATEGY: EXPLORE
TARGET: Structurally novel operator trees and IV60 spread blend repairs
BUDGET: No cap (iterate until SPECTACULAR submittable found)
CONSTRAINTS: novelty-required (>=50% novel templates), avoid saturated families
RATIONALE: No EXPLORE in last 3 sessions on main. Book at 26 ACTIVE, near saturation.

## Round 1: Pure Novel Structures (20 sims, 1 gate-passer)

Tested 19 structurally novel candidates (multi-horizon momentum spreads, dynamic
correlation, signal-to-noise ratios, inter-field ratios, convex combinations,
cross-family interactions) plus 1 IV60 MARKET fix.

**Results:**
- Novel fundamental structures (ebitda, operating_income, cashflow_op, enterprise_value
  as standalone anchors): ALL INFERIOR. Best S=1.15 (operating income MA crossover).
- Dynamic correlation (`ts_corr(F, returns, d)`): Negative or near-zero alpha.
- Signal-to-noise ratios: Low fitness despite moderate Sharpe.
- IV60 MARKET standalone: SPECTACULAR S=2.56 F=4.07 but CONCENTRATED_WEIGHT FAIL (0.50).
- 2 `trade_when` expressions failed with unit errors.

**Key learning:** Novel structures require fields with genuine predictive power,
not just well-known value factors (ebitda/EV, ROA). BRAIN has saturated coverage
of simple fundamental value.

## Round 2: IV60 Blend Repairs + Cross-Family (18 sims, 5 gate-passers)

Added dense fundamental legs to IV60 to fix CONCENTRATED_WEIGHT. Also tested
supply chain (pv13), Ravenpack news, beta, and convex accruals.

**Gate-passers:**
| Alpha | Grade | S | F | Self-Corr | Verdict |
|-------|-------|---|---|-----------|---------|
| LLpOX73M | EXCELLENT | 1.55 | 2.13 | 0.6743 PASS | SUBMITTABLE |
| A1wqagEY | GOOD | 1.28 | 1.63 | — | Lower priority |
| 2r7PnEkb | AVERAGE | 1.38 | 1.33 | — | Lower priority |
| zq9XonWd | AVERAGE | 1.65 | 1.02 | 0.7396 FAIL | BLOCKED |

**Key learning:** Adding `rank(operating_income/close)` to IV60 zscore fixes
CONCENTRATED_WEIGHT while preserving EXCELLENT grade.

## Round 3: IV60 Refinement (10 sims, 6 gate-passers)

Swept decay (3, 5, 10), IV smoothing window (10, 22, 44), and quality variant
(operating_income/close vs /assets vs cashflow_op).

**Gate-passers:**
| Alpha | Grade | S | F | Self-Corr | Verdict |
|-------|-------|---|---|-----------|---------|
| ZYpk2kx8 | SPECTACULAR | 1.71 | 2.52 | 0.6358 PASS | **WINNER** |
| 58wNa766 | EXCELLENT | 1.64 | 2.22 | 0.7139 FAIL | BLOCKED |
| kq3eLwQl | EXCELLENT | 1.58 | 2.20 | 0.6719 PASS | REDUNDANT |
| pw6Q13XX | EXCELLENT | 1.54 | 2.11 | — | Same family |
| akdXWpK9 | GOOD | 1.37 | 1.75 | — | Lower grade |
| A1wqgb6X | GOOD | 1.39 | 1.74 | — | Lower grade |

**Key learning:** 44-day IV smoothing window beats 22-day for both Sharpe
(1.71 vs 1.55), fitness (2.52 vs 2.13), AND self-correlation (0.6358 vs 0.6743).
Longer smoothing reduces alignment with the IV90 peer (Gro21wWG).

## Winner: ZYpk2kx8

**Expression:**
```
ts_decay_linear(zscore(ts_mean(implied_volatility_call_60 - implied_volatility_put_60, 44)) + rank(operating_income / close), 5)
```

**Settings:** MARKET, decay=5, USA TOP3000

**Metrics:**
- Grade: SPECTACULAR (S=1.71, F=2.52, T=4.6%)
- All computable BRAIN checks: PASS
- Self-correlation: 0.6358 PASS (top peer Gro21wWG at 0.636, margin 0.064)

**Mechanism:** Short-term implied volatility call-put skew (60-day) captures near-term
directional options market sentiment. The 44-day smoothing filters noise. Operating
income / price acts as quality anchor, directing positions toward profitable firms.
MARKET neutralization resolves IV60's sparse coverage concentration.

## Summary Statistics

| Metric | Value |
|--------|-------|
| Total sims | 48 |
| Gate-passers | 8 (across all rounds) |
| Submittable | 3 (ZYpk2kx8, kq3eLwQl, LLpOX73M) |
| Best alpha | ZYpk2kx8 SPECTACULAR S=1.71 F=2.52 |
| Self-corr margin | 0.064 |
| Novel template success | 0% (standalone novel fundamentals INFERIOR) |
| IV60 blend success | 60% (6/10 gate-passed, 3 submittable) |
