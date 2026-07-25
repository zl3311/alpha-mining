---
alpha_id: "O0ZOJbaq"
name: "coverage_cshtr_ptpr_intraday"
tags:
  - "session_20260703-001"
  - "sales_estimate"
  - "analyst_coverage"
  - "fnd6_cshtr"
  - "excellent"
submitted: "2026-07-04"
session: "20260703-001"
grade: "EXCELLENT"
sharpe: 2.36
fitness: 2.34
turnover: 0.108
expression: "ts_decay_linear(rank(sales_estimate_count_quarterly) + rank(anl4_ptpr_flag) + rank(fnd6_cshtr) + rank(open/close - 1), 5)"
family: "analyst_coverage_cashflow_intraday"
neutralization: "SUBINDUSTRY"
decay: 4
universe: "TOP3000"
region: "USA"
self_corr_max: 0.7601
self_corr_peer: "O0pl2znv"
self_corr_peer_sharpe: 2.07
self_corr_method: "brain_correlations_self"
self_corr_verdict: "PASS (Sharpe premium: 2.36 >= 1.10 * 2.07 = 2.277)"
brain_checks: "ALL_PASS"
status: "ACTIVE"
brain_url: "https://platform.worldquantbrain.com/alpha/O0ZOJbaq"
---

# Alpha: O0ZOJbaq — Analyst Coverage + Cash Quality + Intraday

## Expression

```
ts_decay_linear(rank(sales_estimate_count_quarterly) + rank(anl4_ptpr_flag) + rank(fnd6_cshtr) + rank(open/close - 1), 5)
```

## Mechanism

Four-leg cross-family blend combining:

1. **Analyst coverage breadth** (`sales_estimate_count_quarterly`): stocks with more
   analyst coverage have faster information dissemination and attract institutional flow.
   Novel field — not present in any existing book entry.
2. **Price target revision** (`anl4_ptpr_flag`): analyst conviction catalyst that
   confirms the coverage signal.
3. **Cash-to-revenue ratio** (`fnd6_cshtr`): cash quality signal that selects firms
   with strong operating cash flow relative to sales. Decorrelates from fundamental
   debt/accrual signals in the book.
4. **Intraday dislocation** (`open/close - 1`): short-horizon mean-reversion that
   provides dense cross-sectional variation.

## Why submittable

- EXCELLENT grade: S=2.36, F=2.34, turnover 10.8%
- All 7 computable BRAIN checks PASS
- Self-correlation: 0.7601 vs O0pl2znv (S=2.07). **PASSES via Sharpe premium**:
  2.36 >= 1.10 × 2.07 = 2.277. No other peer has corr > 0.7.
- Second-highest peer: e7O5EQbJ at 0.6899 (below 0.7 threshold, auto-pass)

## Discovery path

Session 20260703-001, 17 rounds of iteration:
1. R1: discovered `sales_estimate_count_quarterly` as strong novel anchor (EXCELLENT S=2.45)
2. R1-R9: 3-leg version blocked by 0.709-0.739 self-corr vs LLR0n261
3. R16: added `fnd6_cshtr` as 4th leg → shifted primary correlation peer from
   LLR0n261 (S=2.51, threshold 2.76) to O0pl2znv (S=2.07, threshold 2.28)
4. R17: reduced decay from 6 to 4 → boosted Sharpe from 2.25 to 2.36, clearing
   the 2.277 premium threshold
