---
field: dividend_estimate_minimum
dataset: analyst4
best_template: rank_neg_delta
best_sharpe: 1.24
best_fitness: 0.62
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
negated_best_sharpe: 1.24
negated_best_template: rank_neg_delta
negated_best_fitness: 0.62
n_negated_sims: 10
direction_gap: 0.87
---
# dividend_estimate_minimum (analyst4)

*Dividend per share - The lowest value among forecasts - D1*

## Signal Profile
- `rank(dividend_estimate_minimum)`: S=-0.12, F=-0.03, T=1.3%, INFERIOR (TOP1000)
- `rank(dividend_estimate_minimum / close)`: S=0.37, F=0.18, T=1.9%, INFERIOR (TOP1000)
- `rank(ts_delta(dividend_estimate_minimum, 5))`: S=-0.04, F=0.00, T=36.6%, INFERIOR (TOP500)
- `-rank(dividend_estimate_minimum)`: S=0.12, F=0.03, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(dividend_estimate_minimum, 5))`: S=1.24, F=0.62, T=34.4%, INFERIOR (TOP3000)
- `-ts_zscore(dividend_estimate_minimum, 63)`: S=0.37, F=0.11, T=18.9%, INFERIOR (TOP3000)
- `ts_mean(dividend_estimate_minimum, 10)`: S=0.09, F=0.02, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_rank(dividend_estimate_minimum, 22))`: S=0.04, F=0.00, T=13.3%, INFERIOR (TOP3000)
- `rank(-1 * dividend_estimate_minimum)`: S=0.59, F=0.39, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * dividend_estimate_minimum / close)`: S=0.63, F=0.47, T=2.5%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 5F/27P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 11F/9P
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
Best negated: `rank(-1 * ts_delta(dividend_estimate_minimum, 5))` S=1.24, F=0.62, INFERIOR
Direction gap: +0.87 (negated - positive best Sharpe). NEGATION DOMINANT — field is significantly stronger when reversed.

Negated template variants:
- `rank(-1 * dividend_estimate_minimum)`: S=0.59, F=0.39, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * dividend_estimate_minimum / close)`: S=0.63, F=0.47, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(dividend_estimate_minimum, 5))`: S=1.24, F=0.62, T=34.4%, INFERIOR (TOP3000)

## Variation Breakdown
No per-variation PnL data available for this field.

## Correlation Notes
No correlation data available for this field.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
