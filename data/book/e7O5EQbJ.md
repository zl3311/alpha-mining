---
alpha_id: "e7O5EQbJ"
status: "ACTIVE"
grade: "EXCELLENT"
sharpe: 2.50
fitness: 2.31
turnover: 0.112
returns: 0.1068
family: "coverage_breadth_deferred_revenue_value"
expression: "ts_decay_linear(rank(sales_estimate_count_quarterly) + rank(fnd6_drc / close) + rank(open/close - 1) + rank(fnd6_acdo / close), 5)"
neutralization: "SUBINDUSTRY"
decay: 6
universe: "TOP3000"
region: "USA"
self_corr_max: 0.577
self_corr_peer: "zq5RLWO8"
self_corr_result: "PASS"
brain_url: "https://platform.worldquantbrain.com/alpha/e7O5EQbJ"
session: "20260627-002"
discovered: "2026-06-27"
---

# e7O5EQbJ — Coverage Breadth × Deferred Revenue × Overnight Gap × ACDO

## Expression

```
ts_decay_linear(rank(sales_estimate_count_quarterly) + rank(fnd6_drc / close) + rank(open/close - 1) + rank(fnd6_acdo / close), 5)
```

## Economic Mechanism

4-factor blend combining:
1. **Analyst coverage breadth** (`sales_estimate_count_quarterly`): Higher analyst coverage
   signals institutional attention and information quality. Well-covered firms have
   more efficient pricing but also attract informed flow.
2. **Deferred revenue value** (`fnd6_drc / close`): Deferred revenue normalized by price
   captures business model quality — firms with high deferred revenue have more
   predictable future cash flows (SaaS, subscription models).
3. **Overnight gap** (`open/close - 1`): Captures informed institutional trading
   occurring overnight / after-hours, reflecting order flow from informed participants.
4. **Asset disposal value** (`fnd6_acdo / close`): Accumulated depreciation and other
   charges normalized by price — signals capital intensity and reinvestment quality.

## Submission Checks

All 7 computable BRAIN checks PASS (f=0). Self-correlation PASS at 0.577 (limit 0.70).
Top correlated peer: zq5RLWO8 (S=1.79) at correlation 0.577.

## Session Context

Discovered in session 20260627-002 (EXPLORE — Novel Cross-Family Interactions).
Base template (`sales_estimate_count_quarterly + fnd6_drc/close + open/close-1`)
found in batch_r1, then iterated in batch_r2 with 4th factor additions.
Adding `fnd6_acdo/close` raised Sharpe from 2.35 to 2.50 while lowering self-corr
from 0.590 to 0.577.
