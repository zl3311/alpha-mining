---
field: fnd6_txw
dataset: fundamental6
best_template: neg_rank_level
best_sharpe: 0.89
best_fitness: 1.66
best_universe: TOP3000
grade: GOOD
submittability: blocked_LOW_SHARPE
n_sims: 32
negated_best_sharpe: 0.89
negated_best_template: neg_rank_level
negated_best_fitness: 1.66
n_negated_sims: 10
direction_gap: 0.59
---
# fnd6_txw (fundamental6)

*Excise Taxes*

## Signal Profile
- `rank(fnd6_txw)`: S=-0.20, F=-0.16, T=8.2%, INFERIOR (TOP200)
- `rank(fnd6_txw / close)`: S=-0.18, F=-0.13, T=8.9%, INFERIOR (TOP200)
- `rank(ts_delta(fnd6_txw, 5))`: S=-0.39, F=-0.28, T=12.2%, INFERIOR (TOP3000)
- `-rank(fnd6_txw)`: S=0.26, F=0.27, T=2.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_txw, 5))`: S=0.68, F=0.60, T=7.9%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_txw, 22)`: S=-0.12, F=-0.04, T=1.7%, INFERIOR (TOP3000)
- `ts_mean(fnd6_txw, 10)`: S=0.30, F=0.19, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_txw, 22))`: S=-0.77, F=-0.84, T=9.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_txw)`: S=0.89, F=1.66, T=5.9%, GOOD (TOP3000)
- `rank(-1 * fnd6_txw / close)`: S=0.88, F=1.62, T=6.4%, GOOD (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 32F/0P
- LOW_FITNESS: 26F/6P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 18F/11P

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
Best negated: `rank(-1 * fnd6_txw)` S=0.89, F=1.66, GOOD
Direction gap: +0.59 (negated - positive best Sharpe). NEGATION DOMINANT — field is significantly stronger when reversed.

Negated template variants:
- `rank(-1 * fnd6_txw)`: S=0.89, F=1.66, T=5.9%, GOOD (TOP3000)
- `rank(-1 * fnd6_txw / close)`: S=0.88, F=1.62, T=6.4%, GOOD (TOP3000)
- `rank(-1 * ts_delta(fnd6_txw, 5))`: S=0.68, F=0.60, T=7.9%, INFERIOR (TOP3000)

## Variation Breakdown
No per-variation PnL data available for this field.

## Correlation Notes
No correlation data available for this field.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
