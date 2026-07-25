---
field: dividend_estimate_count
dataset: analyst4
best_template: rank_value_norm
best_sharpe: 0.62
best_fitness: 0.42
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
negated_best_sharpe: 0.66
negated_best_template: rank_neg_delta
negated_best_fitness: 0.16
n_negated_sims: 10
direction_gap: 0.04
---
# dividend_estimate_count (analyst4)

*Dividend per share - number of estimations with a delay of 1 quarter*

## Signal Profile
- `rank(dividend_estimate_count)`: S=0.19, F=0.06, T=3.7%, INFERIOR (TOP200)
- `rank(dividend_estimate_count / close)`: S=0.62, F=0.42, T=1.8%, INFERIOR (TOP3000)
- `rank(ts_delta(dividend_estimate_count, 5))`: S=-0.01, F=0.00, T=36.0%, INFERIOR (TOP1000)
- `-rank(dividend_estimate_count)`: S=-0.25, F=-0.06, T=2.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(dividend_estimate_count, 5))`: S=0.66, F=0.16, T=33.9%, INFERIOR (TOP3000)
- `ts_zscore(dividend_estimate_count, 22)`: S=0.19, F=0.04, T=38.1%, INFERIOR (TOP3000)
- `ts_mean(dividend_estimate_count, 10)`: S=0.23, F=0.06, T=2.8%, INFERIOR (TOP3000)
- `rank(ts_rank(dividend_estimate_count, 22))`: S=0.35, F=0.10, T=13.4%, INFERIOR (TOP3000)
- `rank(-1 * dividend_estimate_count)`: S=-0.21, F=-0.04, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * dividend_estimate_count / close)`: S=-0.62, F=-0.42, T=1.8%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 2F/30P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 17F/12P

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
Best negated: `rank(-1 * ts_delta(dividend_estimate_count, 5))` S=0.66, F=0.16, INFERIOR
Direction gap: +0.04 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * dividend_estimate_count)`: S=-0.21, F=-0.04, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * dividend_estimate_count / close)`: S=-0.62, F=-0.42, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(dividend_estimate_count, 5))`: S=0.66, F=0.16, T=33.9%, INFERIOR (TOP3000)

## Variation Breakdown
No per-variation PnL data available for this field.

## Correlation Notes
No correlation data available for this field.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
