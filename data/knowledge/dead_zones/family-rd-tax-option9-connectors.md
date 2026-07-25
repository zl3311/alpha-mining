---
category: "dead_zone"
entity_type: "family"
family: "rd_tax_option9_connectors"
discovered: "20260617-001"
expressions_tested: 12
best_sharpe: 1.19
best_fitness: 0.67
status: "dead_end"
confidence: "medium"
---

# R&D-Tax / Option9 Connector Wrappers

Session `20260617-001` tested the remaining factor/theme-blend connector branch
around:

- `anl4_rd_exp_flag` with `fnd6_txs / close`, `fnd6_dn / close`, and
  `implied_volatility_mean_skew_180`
- `pcr_vol_20` with `fnd2_dfdtxasoprlcarryfwd / close`
- `relative_valuation_rank_derivative` with `implied_volatility_mean_skew_180`

The tested wrappers included additive blends, products, volatility-regime
`trade_when` gates, and dynamic correlation.

## Evidence

Best candidate:

`ts_decay_linear(rank(implied_volatility_mean_skew_180) * rank(anl4_rd_exp_flag), 5)`

This reached only S=1.19, F=0.67, turnover 23.33%, below both aggregate gates.
All 12 tested expressions were INFERIOR and no candidate qualified for BRAIN
checks or self-correlation analysis.

## Rule

Do not retest this exact connector family with simple additive, product,
volatility-gated, or dynamic-correlation wrappers. A future test needs a genuinely
new mechanism, not just another field/window swap inside the same R&D-tax,
option9/deferred-tax, or model16/options connector branch.

