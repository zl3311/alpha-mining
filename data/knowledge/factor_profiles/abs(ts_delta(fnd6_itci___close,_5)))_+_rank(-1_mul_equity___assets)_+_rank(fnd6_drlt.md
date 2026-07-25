---
field: abs(ts_delta(fnd6_itci / close, 5))) + rank(-1 * equity / assets) + rank(fnd6_drlt
dataset: unknown
best_template: rank_value_norm
best_sharpe: 2.62
best_fitness: 2.74
best_universe: TOP3000
grade: SPECTACULAR
submittability: potentially_submittable
n_sims: 5
---
# abs(ts_delta(fnd6_itci / close, 5))) + rank(-1 * equity / assets) + rank(fnd6_drlt (unknown)


## Signal Profile
- `rank(abs(ts_delta(fnd6_itci / close, 5))) + rank(-1 * equity / assets) + rank(fnd6_drlt / close)`: S=2.62, F=2.74, T=4.4%, SPECTACULAR (TOP3000)

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
Untried templates: decay_linear, rank_delta, rank_level, trade_when
