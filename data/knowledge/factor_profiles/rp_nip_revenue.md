---
field: rp_nip_revenue
dataset: news18
best_template: ts_zscore
best_sharpe: 0.56
best_fitness: 0.08
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 21
negated_best_sharpe: 0.53
negated_best_template: rank_neg_delta
negated_best_fitness: 0.08
n_negated_sims: 4
direction_gap: -0.03
---
# rp_nip_revenue (news18)

*News impact projection of revenue news*

## Signal Profile
- `rank(rp_nip_revenue)`: S=-0.07, F=0.00, T=134.0%, INFERIOR (TOP1000)
- `rank(rp_nip_revenue / close)`: S=-0.31, F=-0.04, T=127.6%, INFERIOR (TOP3000)
- `rank(ts_delta(rp_nip_revenue, 5))`: S=0.05, F=0.00, T=137.3%, INFERIOR (TOP200)
- `-rank(rp_nip_revenue)`: S=0.07, F=0.00, T=134.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(rp_nip_revenue, 5))`: S=0.53, F=0.08, T=167.2%, INFERIOR (TOP3000)
- `-ts_zscore(rp_nip_revenue, 63)`: S=0.56, F=0.08, T=139.8%, INFERIOR (TOP3000)
- `ts_mean(rp_nip_revenue, 10)`: S=0.14, F=0.02, T=20.5%, INFERIOR (TOP3000)
- `rank(ts_rank(rp_nip_revenue, 22))`: S=-0.34, F=-0.04, T=142.1%, INFERIOR (TOP3000)
- `rank(-1 * rp_nip_revenue)`: S=0.23, F=0.02, T=149.0%, INFERIOR (TOP3000)
- `rank(-1 * rp_nip_revenue / close)`: S=0.29, F=0.04, T=146.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 8F/13P
- HIGH_TURNOVER: 20F/1P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 21F/0P
- LOW_SUB_UNIVERSE_SHARPE: 12F/7P

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
Best negated: `rank(-1 * ts_delta(rp_nip_revenue, 5))` S=0.53, F=0.08, INFERIOR
Direction gap: -0.03 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * rp_nip_revenue)`: S=0.23, F=0.02, T=149.0%, INFERIOR (TOP3000)
- `rank(-1 * rp_nip_revenue / close)`: S=0.29, F=0.04, T=146.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(rp_nip_revenue, 5))`: S=0.53, F=0.08, T=167.2%, INFERIOR (TOP3000)

## Variation Breakdown
No per-variation PnL data available for this field.

## Correlation Notes
No correlation data available for this field.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
