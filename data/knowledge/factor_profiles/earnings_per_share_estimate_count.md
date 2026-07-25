---
field: earnings_per_share_estimate_count
dataset: analyst4
best_template: rank_level
best_sharpe: 1.36
best_fitness: 0.71
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_FITNESS
n_sims: 32
negated_best_sharpe: 0.83
negated_best_template: neg_rank_level
negated_best_fitness: 0.58
n_negated_sims: 10
direction_gap: -0.53
---
# earnings_per_share_estimate_count (analyst4)

*Earnings per share - number of estimations*

## Signal Profile
- `rank(earnings_per_share_estimate_count)`: S=1.36, F=0.71, T=2.9%, INFERIOR (TOP3000)
- `rank(earnings_per_share_estimate_count / close)`: S=0.25, F=0.11, T=3.1%, INFERIOR (TOP1000)
- `rank(ts_delta(earnings_per_share_estimate_count, 5))`: S=-0.21, F=-0.03, T=33.3%, INFERIOR (TOP3000)
- `-rank(earnings_per_share_estimate_count)`: S=-0.68, F=-0.30, T=4.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(earnings_per_share_estimate_count, 5))`: S=0.98, F=0.47, T=35.8%, INFERIOR (TOP3000)
- `ts_zscore(earnings_per_share_estimate_count, 22)`: S=0.23, F=0.05, T=38.3%, INFERIOR (TOP3000)
- `ts_mean(earnings_per_share_estimate_count, 10)`: S=0.75, F=0.38, T=3.6%, INFERIOR (TOP3000)
- `rank(ts_rank(earnings_per_share_estimate_count, 22))`: S=-0.11, F=-0.02, T=13.5%, INFERIOR (TOP3000)
- `rank(-1 * earnings_per_share_estimate_count)`: S=0.83, F=0.58, T=4.9%, INFERIOR (TOP3000)
- `rank(-1 * earnings_per_share_estimate_count / close)`: S=0.03, F=0.00, T=3.9%, INFERIOR (TOP3000)

## Check Summary
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 31F/1P
- LOW_SUB_UNIVERSE_SHARPE: 14F/6P

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
Best negated: `rank(-1 * earnings_per_share_estimate_count)` S=0.83, F=0.58, INFERIOR
Direction gap: -0.53 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * earnings_per_share_estimate_count)`: S=0.83, F=0.58, T=4.9%, INFERIOR (TOP3000)
- `rank(-1 * earnings_per_share_estimate_count / close)`: S=0.03, F=0.00, T=3.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(earnings_per_share_estimate_count, 5))`: S=0.98, F=0.47, T=35.8%, INFERIOR (TOP3000)

## Variation Breakdown
No per-variation PnL data available for this field.

## Correlation Notes
No correlation data available for this field.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_FITNESS. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
