---
alpha_id: "GrwrVP5G"
name: "exp20260616-001_event_product_fatl_market"
tags:
  - "session_20260616-001"
  - "event-product"
  - "market-neutral"
submitted: "2026-06-17"
session: "20260616-001"
grade: "EXCELLENT"
sharpe: 2.04
fitness: 2.29
turnover: 0.0289
expression: "ts_decay_linear(rank(abs(ts_delta(fnd6_itci / close, 3))) + rank(-1 * equity / assets) * rank(fnd6_fatl / close), 5)"
family: "event_leverage_capital_intensity_product"
neutralization: "MARKET"
decay: 6
self_corr_max: 0.5735
self_corr_method: "brain_self_correlation_breakdown"
self_corr_verdict: "SAFE"
status: "ACTIVE"
brain_url: "https://platform.worldquantbrain.com/alpha/GrwrVP5G"
---

# Alpha: GrwrVP5G

## Expression
```
ts_decay_linear(rank(abs(ts_delta(fnd6_itci / close, 3))) + rank(-1 * equity / assets) * rank(fnd6_fatl / close), 5)
```

## Mechanism

This alpha keeps the proven inventory/tax-credit event-magnitude signal but uses
MARKET neutralization and a product between leverage and capital intensity. The
product form reduces broad additive overlap with the active event/leverage book
while preserving an economically coherent distress/asset-intensity confirmation.

## Self-Correlation Profile

BRAIN self-correlation breakdown on 2026-06-17 showed max correlation 0.5735
against `d5Q3ZmWv`, below the 0.70 self-correlation gate. All computable BRAIN
checks pass, so this is SAFE for human submission review.

## Post-Submission

ACTIVE. User reported this alpha was officially submitted on 2026-06-17.
