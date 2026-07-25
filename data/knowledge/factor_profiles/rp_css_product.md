---
field: rp_css_product
dataset: news18
best_template: ts_mean
best_sharpe: 0.26
best_fitness: 0.06
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 20
negated_best_sharpe: 0.19
negated_best_template: rank_neg_delta
negated_best_fitness: 0.02
n_negated_sims: 4
direction_gap: -0.07
---
# rp_css_product (news18)

*Composite sentiment score of product and service-related news*

## Signal Profile
- `rank(rp_css_product)`: S=0.20, F=0.02, T=136.6%, INFERIOR (TOP1000)
- `rank(ts_delta(rp_css_product, 5))`: S=-0.10, F=-0.01, T=121.4%, INFERIOR (TOP200)
- `-rank(rp_css_product)`: S=-0.20, F=-0.02, T=136.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(rp_css_product, 5))`: S=0.19, F=0.02, T=144.8%, INFERIOR (TOP3000)
- `-ts_zscore(rp_css_product, 63)`: S=-0.02, F=0.00, T=135.8%, INFERIOR (TOP3000)
- `ts_mean(rp_css_product, 10)`: S=0.26, F=0.06, T=28.5%, INFERIOR (TOP3000)
- `rank(ts_rank(rp_css_product, 22))`: S=-0.13, F=-0.01, T=139.3%, INFERIOR (TOP3000)
- `rank(-1 * rp_css_product)`: S=0.03, F=0.00, T=147.4%, INFERIOR (TOP3000)
- `rank(-1 * rp_css_product / close)`: S=-0.01, F=0.00, T=145.0%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 1F/19P
- HIGH_TURNOVER: 19F/1P
- LOW_FITNESS: 20F/0P
- LOW_SHARPE: 20F/0P
- LOW_SUB_UNIVERSE_SHARPE: 12F/6P

## Temporal Behavior
No PnL time series data available for this field.

## Risk & Drawdown
No PnL risk data available for this field.

## Rolling Sharpe
No rolling Sharpe data available for this field.

## Yearly & Monthly Returns
No return distribution data available for this field.

## Regime Profile
No regime analysis data available for this field.

## Negated Direction
Best negated: `rank(-1 * ts_delta(rp_css_product, 5))` S=0.19, F=0.02, INFERIOR
Direction gap: -0.07 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * rp_css_product)`: S=0.03, F=0.00, T=147.4%, INFERIOR (TOP3000)
- `rank(-1 * rp_css_product / close)`: S=-0.01, F=0.00, T=145.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(rp_css_product, 5))`: S=0.19, F=0.02, T=144.8%, INFERIOR (TOP3000)

## Variation Breakdown
No per-variation PnL data available for this field.

## Correlation Notes
No correlation data available for this field.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, rank_value_norm, trade_when
