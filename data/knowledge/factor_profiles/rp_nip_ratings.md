---
field: rp_nip_ratings
dataset: news18
best_template: ts_zscore
best_sharpe: 0.93
best_fitness: 0.16
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 20
negated_best_sharpe: 0.35
negated_best_template: neg_rank
negated_best_fitness: 0.04
n_negated_sims: 4
direction_gap: -0.58
---
# rp_nip_ratings (news18)

*News impact projection of analyst ratings-related news*

## Signal Profile
- `rank(rp_nip_ratings)`: S=0.12, F=0.01, T=149.4%, INFERIOR (TOP3000)
- `rank(ts_delta(rp_nip_ratings, 5))`: S=-0.08, F=0.00, T=171.2%, INFERIOR (TOP3000)
- `-rank(rp_nip_ratings)`: S=0.35, F=0.04, T=137.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(rp_nip_ratings, 5))`: S=0.08, F=0.00, T=171.2%, INFERIOR (TOP3000)
- `-ts_zscore(rp_nip_ratings, 63)`: S=0.93, F=0.16, T=142.7%, INFERIOR (TOP3000)
- `ts_mean(rp_nip_ratings, 10)`: S=0.25, F=0.05, T=19.3%, INFERIOR (TOP3000)
- `rank(ts_rank(rp_nip_ratings, 22))`: S=-0.57, F=-0.07, T=144.7%, INFERIOR (TOP3000)
- `rank(-1 * rp_nip_ratings)`: S=-0.12, F=-0.01, T=149.4%, INFERIOR (TOP3000)
- `rank(-1 * rp_nip_ratings / close)`: S=0.08, F=0.01, T=141.6%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 6F/14P
- HIGH_TURNOVER: 19F/1P
- LOW_FITNESS: 20F/0P
- LOW_SHARPE: 20F/0P
- LOW_SUB_UNIVERSE_SHARPE: 11F/7P

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
Best negated: `-rank(rp_nip_ratings)` S=0.35, F=0.04, INFERIOR
Direction gap: -0.58 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * rp_nip_ratings)`: S=-0.12, F=-0.01, T=149.4%, INFERIOR (TOP3000)
- `rank(-1 * rp_nip_ratings / close)`: S=0.08, F=0.01, T=141.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(rp_nip_ratings, 5))`: S=0.08, F=0.00, T=171.2%, INFERIOR (TOP3000)

## Variation Breakdown
No per-variation PnL data available for this field.

## Correlation Notes
No correlation data available for this field.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, rank_value_norm, trade_when
