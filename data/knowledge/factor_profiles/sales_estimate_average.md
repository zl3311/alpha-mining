---
field: sales_estimate_average
dataset: analyst4
best_template: rank_value_norm
best_sharpe: 0.75
best_fitness: 0.49
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
negated_best_sharpe: 0.52
negated_best_template: rank_neg_delta
negated_best_fitness: 0.18
n_negated_sims: 10
direction_gap: -0.23
---
# sales_estimate_average (analyst4)

*Sales - mean of estimations with a delay of 1 quarter*

## Signal Profile
- `rank(sales_estimate_average)`: S=0.63, F=0.46, T=1.0%, INFERIOR (TOP3000)
- `rank(sales_estimate_average / close)`: S=0.75, F=0.49, T=1.4%, INFERIOR (TOP3000)
- `rank(ts_delta(sales_estimate_average, 5))`: S=-0.10, F=-0.01, T=35.0%, INFERIOR (TOP3000)
- `-rank(sales_estimate_average)`: S=-0.30, F=-0.16, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(sales_estimate_average, 5))`: S=0.52, F=0.18, T=36.1%, INFERIOR (TOP3000)
- `ts_zscore(sales_estimate_average, 22)`: S=0.27, F=0.06, T=34.3%, INFERIOR (TOP3000)
- `ts_mean(sales_estimate_average, 10)`: S=-0.01, F=0.00, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_rank(sales_estimate_average, 22))`: S=-0.20, F=-0.05, T=15.3%, INFERIOR (TOP3000)
- `rank(-1 * sales_estimate_average)`: S=0.06, F=0.02, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * sales_estimate_average / close)`: S=-0.06, F=-0.01, T=2.2%, INFERIOR (TOP3000)

## Check Summary
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/6P
- LOW_TURNOVER: 1F/31P

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
Best negated: `rank(-1 * ts_delta(sales_estimate_average, 5))` S=0.52, F=0.18, INFERIOR
Direction gap: -0.23 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * sales_estimate_average)`: S=0.06, F=0.02, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * sales_estimate_average / close)`: S=-0.06, F=-0.01, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(sales_estimate_average, 5))`: S=0.52, F=0.18, T=36.1%, INFERIOR (TOP3000)

## Variation Breakdown
No per-variation PnL data available for this field.

## Correlation Notes
No correlation data available for this field.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
