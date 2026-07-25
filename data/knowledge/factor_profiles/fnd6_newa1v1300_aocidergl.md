---
field: fnd6_newa1v1300_aocidergl
dataset: fundamental6
best_template: neg_rank_value_norm
best_sharpe: 0.68
best_fitness: 0.29
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
negated_best_sharpe: 0.68
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.29
n_negated_sims: 10
direction_gap: 0.4
---
# fnd6_newa1v1300_aocidergl (fundamental6)

*Accum Other Comp Inc - Derivatives Unrealized Gain/Loss*

## Signal Profile
- `rank(fnd6_newa1v1300_aocidergl)`: S=-0.01, F=0.00, T=2.4%, INFERIOR (TOP1000)
- `rank(fnd6_newa1v1300_aocidergl / close)`: S=-0.07, F=-0.01, T=2.4%, INFERIOR (TOP1000)
- `rank(ts_delta(fnd6_newa1v1300_aocidergl, 5))`: S=0.03, F=0.00, T=24.6%, INFERIOR (TOP200)
- `-rank(fnd6_newa1v1300_aocidergl)`: S=0.01, F=0.00, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa1v1300_aocidergl, 5))`: S=0.32, F=0.11, T=38.7%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_newa1v1300_aocidergl, 22)`: S=-0.45, F=-0.29, T=18.6%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newa1v1300_aocidergl, 10)`: S=-0.38, F=-0.24, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newa1v1300_aocidergl, 22))`: S=0.28, F=0.11, T=19.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_aocidergl)`: S=0.56, F=0.22, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_aocidergl / close)`: S=0.68, F=0.29, T=1.8%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 13F/19P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 21F/8P

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
Best negated: `rank(-1 * fnd6_newa1v1300_aocidergl / close)` S=0.68, F=0.29, INFERIOR
Direction gap: +0.40 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fnd6_newa1v1300_aocidergl)`: S=0.56, F=0.22, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_aocidergl / close)`: S=0.68, F=0.29, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa1v1300_aocidergl, 5))`: S=0.32, F=0.11, T=38.7%, INFERIOR (TOP3000)

## Variation Breakdown
No per-variation PnL data available for this field.

## Correlation Notes
No correlation data available for this field.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
