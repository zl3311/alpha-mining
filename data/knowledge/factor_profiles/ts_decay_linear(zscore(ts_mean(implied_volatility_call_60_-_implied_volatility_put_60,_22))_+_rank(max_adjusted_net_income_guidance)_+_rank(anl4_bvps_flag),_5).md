---
field: ts_decay_linear(zscore(ts_mean(implied_volatility_call_60 - implied_volatility_put_60,
  22)) + rank(max_adjusted_net_income_guidance) + rank(anl4_bvps_flag), 5)
dataset: unknown
best_template: unknown
best_sharpe: 3.09
best_fitness: 5.14
best_universe: TOP3000
grade: SPECTACULAR
submittability: potentially_submittable
n_sims: 1
---
# ts_decay_linear(zscore(ts_mean(implied_volatility_call_60 - implied_volatility_put_60, 22)) + rank(max_adjusted_net_income_guidance) + rank(anl4_bvps_flag), 5) (unknown)


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
Passes all non-self-corr checks. Candidate for submission pending self-corr verification.
Untried templates: decay_linear, rank_delta, rank_level, rank_value_norm, trade_when
