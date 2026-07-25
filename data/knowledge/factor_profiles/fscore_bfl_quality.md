---
field: fscore_bfl_quality
dataset: model16
best_template: neg_rank_level
best_sharpe: 0.61
best_fitness: 0.35
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 20
negated_best_sharpe: 0.61
negated_best_template: neg_rank_level
negated_best_fitness: 0.35
n_negated_sims: 4
direction_gap: -0.02
---
# fscore_bfl_quality (model16)

*Composite measuring earnings quality, stability, and balance-sheet resilience*

## Signal Profile
- `rank(fscore_bfl_quality)`: S=-0.46, F=-0.25, T=2.4%, INFERIOR (TOP500)
- `rank(ts_delta(fscore_bfl_quality, 5))`: S=-0.04, F=0.00, T=15.5%, INFERIOR (TOP500)
- `-rank(fscore_bfl_quality)`: S=0.49, F=0.26, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fscore_bfl_quality, 5))`: S=-0.34, F=-0.13, T=15.4%, INFERIOR (TOP3000)
- `-ts_zscore(fscore_bfl_quality, 63)`: S=0.63, F=0.25, T=9.6%, INFERIOR (TOP3000)
- `ts_mean(fscore_bfl_quality, 10)`: S=-0.49, F=-0.26, T=1.8%, INFERIOR (TOP3000)
- `rank(ts_rank(fscore_bfl_quality, 22))`: S=-0.79, F=-0.34, T=9.0%, INFERIOR (TOP3000)
- `rank(-1 * fscore_bfl_quality)`: S=0.61, F=0.35, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * fscore_bfl_quality / close)`: S=-0.17, F=-0.05, T=1.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 9F/11P
- LOW_FITNESS: 20F/0P
- LOW_SHARPE: 20F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/5P

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
Best negated: `rank(-1 * fscore_bfl_quality)` S=0.61, F=0.35, INFERIOR
Direction gap: -0.02 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fscore_bfl_quality)`: S=0.61, F=0.35, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * fscore_bfl_quality / close)`: S=-0.17, F=-0.05, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fscore_bfl_quality, 5))`: S=-0.34, F=-0.13, T=15.4%, INFERIOR (TOP3000)

## Variation Breakdown
No per-variation PnL data available for this field.

## Correlation Notes
No correlation data available for this field.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, rank_value_norm, trade_when
