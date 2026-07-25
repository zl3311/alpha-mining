---
field: fnd6_dudd
dataset: fundamental6
best_template: neg_rank_value_norm
best_sharpe: 0.83
best_fitness: 0.46
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
negated_best_sharpe: 0.83
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.46
n_negated_sims: 10
direction_gap: 0.9
---
# fnd6_dudd (fundamental6)

*Debt - Unamortized Debt Discount and Other*

## Signal Profile
- `rank(fnd6_dudd)`: S=-0.45, F=-0.20, T=2.7%, INFERIOR (TOP500)
- `rank(fnd6_dudd / close)`: S=-0.44, F=-0.20, T=2.8%, INFERIOR (TOP500)
- `rank(ts_delta(fnd6_dudd, 5))`: S=-0.07, F=-0.01, T=35.9%, INFERIOR (TOP3000)
- `-rank(fnd6_dudd)`: S=0.55, F=0.26, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_dudd, 5))`: S=0.17, F=0.05, T=36.5%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_dudd, 22)`: S=-0.04, F=-0.01, T=10.9%, INFERIOR (TOP3000)
- `ts_mean(fnd6_dudd, 10)`: S=-0.92, F=-0.70, T=1.5%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_dudd, 22))`: S=-0.25, F=-0.11, T=20.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_dudd)`: S=0.79, F=0.43, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_dudd / close)`: S=0.83, F=0.46, T=1.8%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 13F/19P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 19F/10P

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
Best negated: `rank(-1 * fnd6_dudd / close)` S=0.83, F=0.46, INFERIOR
Direction gap: +0.90 (negated - positive best Sharpe). NEGATION DOMINANT — field is significantly stronger when reversed.

Negated template variants:
- `rank(-1 * fnd6_dudd)`: S=0.79, F=0.43, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_dudd / close)`: S=0.83, F=0.46, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_dudd, 5))`: S=0.17, F=0.05, T=36.5%, INFERIOR (TOP3000)

## Variation Breakdown
No per-variation PnL data available for this field.

## Correlation Notes
No correlation data available for this field.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
