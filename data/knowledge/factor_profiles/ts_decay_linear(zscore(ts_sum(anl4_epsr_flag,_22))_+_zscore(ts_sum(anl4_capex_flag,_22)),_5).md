---
field: ts_decay_linear(zscore(ts_sum(anl4_epsr_flag, 22)) + zscore(ts_sum(anl4_capex_flag,
  22)), 5)
dataset: unknown
best_template: unknown
best_sharpe: 1.5
best_fitness: 1.47
best_universe: TOP3000
grade: AVERAGE
submittability: needs_upgrade
n_sims: 1
---
# ts_decay_linear(zscore(ts_sum(anl4_epsr_flag, 22)) + zscore(ts_sum(anl4_capex_flag, 22)), 5) (unknown)


## Signal Profile
- No simulation data available

## Check Summary
No check failures observed across simulations.

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
Needs grade upgrade. Try decay_linear wrap, value normalization, or blend with complementary factor.
Untried templates: decay_linear, rank_delta, rank_level, rank_value_norm, trade_when
