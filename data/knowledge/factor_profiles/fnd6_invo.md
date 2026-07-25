---
field: fnd6_invo
dataset: fundamental6
best_template: neg_rank_value_norm
best_sharpe: 1.06
best_fitness: 1.08
best_universe: TOP3000
grade: AVERAGE
submittability: blocked_LOW_SHARPE
n_sims: 32
negated_best_sharpe: 1.06
negated_best_template: neg_rank_value_norm
negated_best_fitness: 1.08
n_negated_sims: 10
direction_gap: 0.61
---
# fnd6_invo (fundamental6)

*Inventories - Other*

## Signal Profile
- `rank(fnd6_invo)`: S=-0.05, F=-0.01, T=2.4%, INFERIOR (TOP200)
- `rank(fnd6_invo / close)`: S=-0.05, F=-0.01, T=2.4%, INFERIOR (TOP200)
- `rank(ts_delta(fnd6_invo, 5))`: S=-0.04, F=-0.01, T=11.9%, INFERIOR (TOP500)
- `-rank(fnd6_invo)`: S=0.68, F=0.45, T=2.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_invo, 5))`: S=-0.09, F=-0.03, T=12.0%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_invo, 63)`: S=-0.02, F=0.00, T=4.5%, INFERIOR (TOP3000)
- `ts_mean(fnd6_invo, 10)`: S=0.32, F=0.15, T=1.8%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_invo, 22))`: S=0.45, F=0.45, T=17.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_invo)`: S=1.05, F=1.07, T=3.4%, AVERAGE (TOP3000)
- `rank(-1 * fnd6_invo / close)`: S=1.06, F=1.08, T=3.4%, AVERAGE (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 14F/18P
- LOW_FITNESS: 26F/6P
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
Best negated: `rank(-1 * fnd6_invo / close)` S=1.06, F=1.08, AVERAGE
Direction gap: +0.61 (negated - positive best Sharpe). NEGATION DOMINANT — field is significantly stronger when reversed.

Negated template variants:
- `rank(-1 * fnd6_invo)`: S=1.05, F=1.07, T=3.4%, AVERAGE (TOP3000)
- `rank(-1 * fnd6_invo / close)`: S=1.06, F=1.08, T=3.4%, AVERAGE (TOP3000)
- `rank(-1 * ts_delta(fnd6_invo, 5))`: S=-0.09, F=-0.03, T=12.0%, INFERIOR (TOP3000)

## Variation Breakdown
No per-variation PnL data available for this field.

## Correlation Notes
No correlation data available for this field.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
