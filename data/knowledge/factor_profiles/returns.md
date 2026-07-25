---
field: returns
dataset: pv1
best_template: neg_rank
best_sharpe: 1.65
best_fitness: 0.9
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_FITNESS
n_sims: 20
negated_best_sharpe: 1.65
negated_best_template: neg_rank
negated_best_fitness: 0.9
n_negated_sims: 4
direction_gap: 0.22
---
# returns (pv1)

*Daily returns*

## Signal Profile
- `rank(returns)`: S=-1.09, F=-0.52, T=70.7%, INFERIOR (TOP200)
- `rank(ts_delta(returns, 5))`: S=-1.03, F=-0.43, T=76.0%, INFERIOR (TOP200)
- `-rank(returns)`: S=1.65, F=0.90, T=70.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(returns, 5))`: S=1.59, F=0.71, T=77.7%, INFERIOR (TOP3000)
- `-ts_zscore(returns, 63)`: S=1.43, F=0.70, T=67.5%, INFERIOR (TOP3000)
- `ts_mean(returns, 10)`: S=-0.71, F=-0.56, T=23.9%, INFERIOR (TOP3000)
- `rank(ts_rank(returns, 22))`: S=-1.86, F=-0.90, T=70.6%, INFERIOR (TOP3000)
- `rank(-1 * returns)`: S=1.70, F=0.90, T=71.2%, INFERIOR (TOP3000)
- `rank(-1 * returns / close)`: S=1.44, F=0.68, T=72.3%, INFERIOR (TOP3000)

## Check Summary
- HIGH_TURNOVER: 17F/3P
- LOW_FITNESS: 20F/0P
- LOW_SHARPE: 15F/5P
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
Best negated: `-rank(returns)` S=1.65, F=0.90, INFERIOR
Direction gap: +0.22 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * returns)`: S=1.70, F=0.90, T=71.2%, INFERIOR (TOP3000)
- `rank(-1 * returns / close)`: S=1.44, F=0.68, T=72.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(returns, 5))`: S=1.59, F=0.71, T=77.7%, INFERIOR (TOP3000)

## Variation Breakdown
No per-variation PnL data available for this field.

## Correlation Notes
No correlation data available for this field.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_FITNESS. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, rank_value_norm, trade_when
