---
field: fscore_bfl_profitability
dataset: model16
best_template: neg_rank_level
best_sharpe: 0.35
best_fitness: 0.15
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 20
negated_best_sharpe: 0.35
negated_best_template: neg_rank_level
negated_best_fitness: 0.15
n_negated_sims: 4
direction_gap: 0.21
---
# fscore_bfl_profitability (model16)

*Profitability composite ranking firms by ability to generate cash flows and operational efficiency; higher is better (0–100)*

## Signal Profile
- `rank(fscore_bfl_profitability)`: S=-0.07, F=-0.01, T=2.4%, INFERIOR (TOP500)
- `rank(ts_delta(fscore_bfl_profitability, 5))`: S=0.04, F=0.00, T=15.5%, INFERIOR (TOP500)
- `-rank(fscore_bfl_profitability)`: S=0.15, F=0.04, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fscore_bfl_profitability, 5))`: S=-0.06, F=-0.01, T=15.2%, INFERIOR (TOP3000)
- `-ts_zscore(fscore_bfl_profitability, 63)`: S=0.14, F=0.03, T=9.3%, INFERIOR (TOP3000)
- `ts_mean(fscore_bfl_profitability, 10)`: S=-0.07, F=-0.01, T=1.8%, INFERIOR (TOP3000)
- `rank(ts_rank(fscore_bfl_profitability, 22))`: S=-0.26, F=-0.07, T=8.7%, INFERIOR (TOP3000)
- `rank(-1 * fscore_bfl_profitability)`: S=0.35, F=0.15, T=1.2%, INFERIOR (TOP3000)
- `rank(-1 * fscore_bfl_profitability / close)`: S=-0.49, F=-0.26, T=1.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 9F/11P
- LOW_FITNESS: 20F/0P
- LOW_SHARPE: 20F/0P
- LOW_SUB_UNIVERSE_SHARPE: 5F/13P

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
Best negated: `rank(-1 * fscore_bfl_profitability)` S=0.35, F=0.15, INFERIOR
Direction gap: +0.21 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fscore_bfl_profitability)`: S=0.35, F=0.15, T=1.2%, INFERIOR (TOP3000)
- `rank(-1 * fscore_bfl_profitability / close)`: S=-0.49, F=-0.26, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fscore_bfl_profitability, 5))`: S=-0.06, F=-0.01, T=15.2%, INFERIOR (TOP3000)

## Variation Breakdown
No per-variation PnL data available for this field.

## Correlation Notes
No correlation data available for this field.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, rank_value_norm, trade_when
