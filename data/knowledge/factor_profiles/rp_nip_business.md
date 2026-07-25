---
field: rp_nip_business
dataset: news18
best_template: ts_mean
best_sharpe: 0.35
best_fitness: 0.11
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 21
negated_best_sharpe: 0.54
negated_best_template: rank_neg_delta
negated_best_fitness: 0.06
n_negated_sims: 4
direction_gap: 0.19
---
# rp_nip_business (news18)

*News impact projection of business-related news*

## Signal Profile
- `rank(rp_nip_business)`: S=0.12, F=0.01, T=107.9%, INFERIOR (TOP3000)
- `rank(rp_nip_business / close)`: S=-0.18, F=-0.03, T=58.9%, INFERIOR (TOP3000)
- `rank(ts_delta(rp_nip_business, 5))`: S=-0.33, F=-0.03, T=110.0%, INFERIOR (TOP1000)
- `-rank(rp_nip_business)`: S=0.02, F=0.00, T=81.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(rp_nip_business, 5))`: S=0.54, F=0.06, T=133.6%, INFERIOR (TOP3000)
- `-ts_zscore(rp_nip_business, 63)`: S=0.36, F=0.04, T=89.6%, INFERIOR (TOP3000)
- `ts_mean(rp_nip_business, 10)`: S=0.35, F=0.11, T=15.9%, INFERIOR (TOP3000)
- `rank(ts_rank(rp_nip_business, 22))`: S=-0.39, F=-0.05, T=92.5%, INFERIOR (TOP3000)
- `rank(-1 * rp_nip_business)`: S=-0.12, F=-0.01, T=107.9%, INFERIOR (TOP3000)
- `rank(-1 * rp_nip_business / close)`: S=-0.05, F=0.00, T=88.6%, INFERIOR (TOP3000)

## Check Summary
- HIGH_TURNOVER: 17F/4P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 21F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/5P

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
Best negated: `rank(-1 * ts_delta(rp_nip_business, 5))` S=0.54, F=0.06, INFERIOR
Direction gap: +0.19 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * rp_nip_business)`: S=-0.12, F=-0.01, T=107.9%, INFERIOR (TOP3000)
- `rank(-1 * rp_nip_business / close)`: S=-0.05, F=0.00, T=88.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(rp_nip_business, 5))`: S=0.54, F=0.06, T=133.6%, INFERIOR (TOP3000)

## Variation Breakdown
No per-variation PnL data available for this field.

## Correlation Notes
No correlation data available for this field.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
