---
field: ts_sum(anl4_ptp_flag, 22
dataset: unknown
best_template: decay_linear
best_sharpe: 1.88
best_fitness: 1.91
best_universe: TOP3000
grade: GOOD
submittability: potentially_submittable
n_sims: 1
---
# ts_sum(anl4_ptp_flag, 22 (unknown)


## Signal Profile
- `ts_decay_linear(rank(ts_sum(anl4_ptp_flag, 22)) + rank(ts_sum(anl4_netdebt_flag, 22)), 5)`: S=1.88, F=1.91, T=2.9%, GOOD (TOP3000)

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
Passes all non-self-corr checks. Candidate for submission pending self-corr verification.
Untried templates: rank_delta, rank_level, rank_value_norm, trade_when
