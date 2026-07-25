---
field: dividend_estimate_median_value
dataset: analyst4
best_template: neg_rank_value_norm
best_sharpe: 0.56
best_fitness: 0.4
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
negated_best_sharpe: 0.56
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.4
n_negated_sims: 10
direction_gap: 0.1
---
# dividend_estimate_median_value (analyst4)

*Dividend per share - median of estimations*

## Signal Profile
- `rank(dividend_estimate_median_value)`: S=-0.09, F=-0.02, T=1.3%, INFERIOR (TOP1000)
- `rank(dividend_estimate_median_value / close)`: S=0.46, F=0.25, T=1.9%, INFERIOR (TOP1000)
- `rank(ts_delta(dividend_estimate_median_value, 5))`: S=0.11, F=0.01, T=36.5%, INFERIOR (TOP500)
- `-rank(dividend_estimate_median_value)`: S=0.09, F=0.02, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(dividend_estimate_median_value, 5))`: S=0.89, F=0.37, T=34.8%, INFERIOR (TOP3000)
- `-ts_zscore(dividend_estimate_median_value, 63)`: S=0.43, F=0.13, T=18.5%, INFERIOR (TOP3000)
- `ts_mean(dividend_estimate_median_value, 10)`: S=0.10, F=0.02, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_rank(dividend_estimate_median_value, 22))`: S=0.04, F=0.00, T=13.4%, INFERIOR (TOP3000)
- `rank(-1 * dividend_estimate_median_value)`: S=0.51, F=0.32, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * dividend_estimate_median_value / close)`: S=0.56, F=0.40, T=2.6%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 4F/28P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 10F/10P
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
Best negated: `rank(-1 * dividend_estimate_median_value / close)` S=0.56, F=0.40, INFERIOR
Direction gap: +0.10 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * dividend_estimate_median_value)`: S=0.51, F=0.32, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * dividend_estimate_median_value / close)`: S=0.56, F=0.40, T=2.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(dividend_estimate_median_value, 5))`: S=0.89, F=0.37, T=34.8%, INFERIOR (TOP3000)

## Variation Breakdown
No per-variation PnL data available for this field.

## Correlation Notes
No correlation data available for this field.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
