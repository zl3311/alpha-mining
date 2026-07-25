---
field: fnd6_txdc
dataset: fundamental6
best_template: neg_rank
best_sharpe: 0.64
best_fitness: 0.29
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
negated_best_sharpe: 0.64
negated_best_template: neg_rank
negated_best_fitness: 0.29
n_negated_sims: 10
direction_gap: 0.4
---
# fnd6_txdc (fundamental6)

*Deferred Taxes (Cash Flow)*

## Signal Profile
- `rank(fnd6_txdc)`: S=-0.14, F=-0.04, T=2.6%, INFERIOR (TOP200)
- `rank(fnd6_txdc / close)`: S=-0.12, F=-0.03, T=2.8%, INFERIOR (TOP200)
- `rank(ts_delta(fnd6_txdc, 5))`: S=-0.07, F=-0.02, T=30.1%, INFERIOR (TOP200)
- `-rank(fnd6_txdc)`: S=0.64, F=0.29, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_txdc, 5))`: S=0.60, F=0.29, T=34.6%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_txdc, 22)`: S=0.24, F=0.11, T=26.0%, INFERIOR (TOP3000)
- `ts_mean(fnd6_txdc, 10)`: S=-0.33, F=-0.14, T=1.7%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_txdc, 22))`: S=0.21, F=0.07, T=15.7%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_txdc)`: S=0.64, F=0.29, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_txdc / close)`: S=0.51, F=0.21, T=2.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
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
Best negated: `-rank(fnd6_txdc)` S=0.64, F=0.29, INFERIOR
Direction gap: +0.40 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fnd6_txdc)`: S=0.64, F=0.29, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_txdc / close)`: S=0.51, F=0.21, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_txdc, 5))`: S=0.60, F=0.29, T=34.6%, INFERIOR (TOP3000)

## Variation Breakdown
No per-variation PnL data available for this field.

## Correlation Notes
No correlation data available for this field.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
