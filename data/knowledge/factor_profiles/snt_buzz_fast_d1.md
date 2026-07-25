---
field: snt_buzz_fast_d1
dataset: socialmedia12
best_template: ts_mean
best_sharpe: 0.4
best_fitness: 0.2
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 26
negated_best_sharpe: 0.58
negated_best_template: neg_rank_level
negated_best_fitness: 0.17
n_negated_sims: 10
direction_gap: 0.18
---
# snt_buzz_fast_d1 (socialmedia12)

*Negative relative sentiment volume measure for current day, with missing values filled as 0*

## Signal Profile
- `rank(snt_buzz_fast_d1)`: S=0.04, F=0.00, T=41.1%, INFERIOR (TOP1000)
- `rank(ts_delta(snt_buzz_fast_d1, 5))`: S=0.09, F=0.01, T=67.1%, INFERIOR (TOP3000)
- `-rank(snt_buzz_fast_d1)`: S=-0.04, F=0.00, T=41.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(snt_buzz_fast_d1, 5))`: S=0.20, F=0.03, T=62.3%, INFERIOR (TOP3000)
- `-ts_zscore(snt_buzz_fast_d1, 63)`: S=0.38, F=0.08, T=53.2%, INFERIOR (TOP3000)
- `ts_mean(snt_buzz_fast_d1, 10)`: S=0.40, F=0.20, T=19.8%, INFERIOR (TOP3000)
- `rank(ts_rank(snt_buzz_fast_d1, 22))`: S=-0.02, F=0.00, T=58.9%, INFERIOR (TOP3000)
- `rank(-1 * snt_buzz_fast_d1)`: S=0.58, F=0.17, T=54.8%, INFERIOR (TOP3000)
- `rank(-1 * snt_buzz_fast_d1 / close)`: S=0.39, F=0.16, T=24.6%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 1F/25P
- LOW_FITNESS: 26F/0P
- LOW_SHARPE: 26F/0P
- LOW_SUB_UNIVERSE_SHARPE: 9F/6P

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
Best negated: `rank(-1 * snt_buzz_fast_d1)` S=0.58, F=0.17, INFERIOR
Direction gap: +0.18 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * snt_buzz_fast_d1)`: S=0.58, F=0.17, T=54.8%, INFERIOR (TOP3000)
- `rank(-1 * snt_buzz_fast_d1 / close)`: S=0.39, F=0.16, T=24.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(snt_buzz_fast_d1, 5))`: S=0.20, F=0.03, T=62.3%, INFERIOR (TOP3000)

## Variation Breakdown
No per-variation PnL data available for this field.

## Correlation Notes
No correlation data available for this field.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, rank_value_norm, trade_when
