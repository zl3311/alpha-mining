---
field: rp_nip_marketing
dataset: news18
best_template: rank_neg_delta
best_sharpe: 1.05
best_fitness: 0.49
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 21
negated_best_sharpe: 1.05
negated_best_template: rank_neg_delta
negated_best_fitness: 0.49
n_negated_sims: 4
direction_gap: 0.55
---
# rp_nip_marketing (news18)

*News impact projection of marketing news*

## Signal Profile
- `rank(rp_nip_marketing)`: S=-0.01, F=0.00, T=167.7%, INFERIOR (TOP3000)
- `rank(rp_nip_marketing / close)`: S=-0.24, F=-0.05, T=151.3%, INFERIOR (TOP3000)
- `rank(ts_delta(rp_nip_marketing, 5))`: S=-0.47, F=-0.15, T=69.0%, INFERIOR (TOP500)
- `-rank(rp_nip_marketing)`: S=0.16, F=0.03, T=156.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(rp_nip_marketing, 5))`: S=1.05, F=0.49, T=90.5%, INFERIOR (TOP3000)
- `-ts_zscore(rp_nip_marketing, 63)`: S=0.50, F=0.15, T=150.5%, INFERIOR (TOP3000)
- `ts_mean(rp_nip_marketing, 10)`: S=-0.13, F=-0.03, T=37.9%, INFERIOR (TOP3000)
- `rank(ts_rank(rp_nip_marketing, 22))`: S=-0.55, F=-0.17, T=154.8%, INFERIOR (TOP3000)
- `rank(-1 * rp_nip_marketing)`: S=0.01, F=0.00, T=167.7%, INFERIOR (TOP3000)
- `rank(-1 * rp_nip_marketing / close)`: S=0.45, F=0.13, T=163.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 21F/0P
- HIGH_TURNOVER: 18F/3P
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
Best negated: `rank(-1 * ts_delta(rp_nip_marketing, 5))` S=1.05, F=0.49, INFERIOR
Direction gap: +0.55 (negated - positive best Sharpe). NEGATION DOMINANT — field is significantly stronger when reversed.

Negated template variants:
- `rank(-1 * rp_nip_marketing)`: S=0.01, F=0.00, T=167.7%, INFERIOR (TOP3000)
- `rank(-1 * rp_nip_marketing / close)`: S=0.45, F=0.13, T=163.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(rp_nip_marketing, 5))`: S=1.05, F=0.49, T=90.5%, INFERIOR (TOP3000)

## Variation Breakdown
No per-variation PnL data available for this field.

## Correlation Notes
No correlation data available for this field.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
