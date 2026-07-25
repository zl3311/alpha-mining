---
field: ts_mean(scl12_buzz, 5
dataset: unknown
best_template: decay_linear
best_sharpe: 2.21
best_fitness: 3.63
best_universe: TOP3000
grade: SPECTACULAR
submittability: potentially_submittable
n_sims: 4
---
# ts_mean(scl12_buzz, 5 (unknown)


## Signal Profile
- `ts_decay_linear(rank(ts_mean(scl12_buzz, 5)) * zscore(ts_mean(implied_volatility_call_270 - implied_volatility_put_270, 60)), 5)`: S=2.21, F=3.63, T=8.2%, SPECTACULAR (TOP3000)

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
