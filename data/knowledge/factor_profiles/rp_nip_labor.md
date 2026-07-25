---
field: rp_nip_labor
dataset: news18
best_template: rank_value_norm
best_sharpe: 0.41
best_fitness: 0.08
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 21
negated_best_sharpe: 0.18
negated_best_template: neg_rank
negated_best_fitness: 0.02
n_negated_sims: 4
direction_gap: -0.23
---
# rp_nip_labor (news18)

*News impact projection of labor issues news*

## Signal Profile
- `rank(rp_nip_labor)`: S=0.00, F=0.00, T=141.1%, INFERIOR (TOP200)
- `rank(rp_nip_labor / close)`: S=0.41, F=0.08, T=141.3%, INFERIOR (TOP3000)
- `rank(ts_delta(rp_nip_labor, 5))`: S=0.05, F=0.00, T=157.4%, INFERIOR (TOP3000)
- `-rank(rp_nip_labor)`: S=0.18, F=0.02, T=156.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(rp_nip_labor, 5))`: S=-0.05, F=0.00, T=157.4%, INFERIOR (TOP3000)
- `-ts_zscore(rp_nip_labor, 63)`: S=0.45, F=0.08, T=154.4%, INFERIOR (TOP3000)
- `ts_mean(rp_nip_labor, 10)`: S=-0.25, F=-0.05, T=32.0%, INFERIOR (TOP3000)
- `rank(ts_rank(rp_nip_labor, 22))`: S=-0.53, F=-0.10, T=158.7%, INFERIOR (TOP3000)
- `rank(-1 * rp_nip_labor)`: S=0.08, F=0.01, T=162.5%, INFERIOR (TOP3000)
- `rank(-1 * rp_nip_labor / close)`: S=-0.66, F=-0.16, T=151.5%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 20F/1P
- HIGH_TURNOVER: 20F/1P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 21F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/6P

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
Best negated: `-rank(rp_nip_labor)` S=0.18, F=0.02, INFERIOR
Direction gap: -0.23 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * rp_nip_labor)`: S=0.08, F=0.01, T=162.5%, INFERIOR (TOP3000)
- `rank(-1 * rp_nip_labor / close)`: S=-0.66, F=-0.16, T=151.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(rp_nip_labor, 5))`: S=-0.05, F=0.00, T=157.4%, INFERIOR (TOP3000)

## Variation Breakdown
No per-variation PnL data available for this field.

## Correlation Notes
No correlation data available for this field.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
