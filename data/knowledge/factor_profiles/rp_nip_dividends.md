---
field: rp_nip_dividends
dataset: news18
best_template: rank_level
best_sharpe: 0.21
best_fitness: 0.02
best_universe: TOP1000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 21
negated_best_sharpe: 0.25
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.02
n_negated_sims: 4
direction_gap: 0.04
---
# rp_nip_dividends (news18)

*News impact projection of dividends news*

## Signal Profile
- `rank(rp_nip_dividends)`: S=0.21, F=0.02, T=146.1%, INFERIOR (TOP1000)
- `rank(rp_nip_dividends / close)`: S=0.16, F=0.01, T=143.5%, INFERIOR (TOP3000)
- `rank(ts_delta(rp_nip_dividends, 5))`: S=-0.19, F=-0.02, T=173.5%, INFERIOR (TOP3000)
- `-rank(rp_nip_dividends)`: S=-0.21, F=-0.02, T=146.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(rp_nip_dividends, 5))`: S=0.19, F=0.02, T=173.5%, INFERIOR (TOP3000)
- `-ts_zscore(rp_nip_dividends, 63)`: S=0.25, F=0.02, T=152.6%, INFERIOR (TOP3000)
- `ts_mean(rp_nip_dividends, 10)`: S=-0.06, F=-0.01, T=24.4%, INFERIOR (TOP3000)
- `rank(ts_rank(rp_nip_dividends, 22))`: S=-0.44, F=-0.06, T=154.5%, INFERIOR (TOP3000)
- `rank(-1 * rp_nip_dividends)`: S=0.06, F=0.00, T=155.9%, INFERIOR (TOP3000)
- `rank(-1 * rp_nip_dividends / close)`: S=0.25, F=0.02, T=155.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 17F/4P
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
Best negated: `rank(-1 * rp_nip_dividends / close)` S=0.25, F=0.02, INFERIOR
Direction gap: +0.04 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * rp_nip_dividends)`: S=0.06, F=0.00, T=155.9%, INFERIOR (TOP3000)
- `rank(-1 * rp_nip_dividends / close)`: S=0.25, F=0.02, T=155.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(rp_nip_dividends, 5))`: S=0.19, F=0.02, T=173.5%, INFERIOR (TOP3000)

## Variation Breakdown
No per-variation PnL data available for this field.

## Correlation Notes
No correlation data available for this field.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
