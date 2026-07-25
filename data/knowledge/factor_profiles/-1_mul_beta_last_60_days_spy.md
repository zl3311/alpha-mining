---
field: -1 * beta_last_60_days_spy
dataset: model51
best_template: decay_linear
best_sharpe: 0.01
best_fitness: 0.0
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 1
---
# -1 * beta_last_60_days_spy (model51)


## Signal Profile
- `ts_decay_linear(rank(-1 * beta_last_60_days_spy), 5)`: S=0.01, F=0.00, T=13.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 1F/0P
- LOW_FITNESS: 1F/0P
- LOW_SHARPE: 1F/0P

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
No negated-direction simulations available for this field.

## Variation Breakdown
No per-variation PnL data available for this field.

## Correlation Notes
No correlation data available for this field.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: rank_delta, rank_level, rank_value_norm, trade_when
