---
field: rp_ess_equity
dataset: news18
best_template: neg_rank
best_sharpe: 0.6
best_fitness: 0.09
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 20
negated_best_sharpe: 0.6
negated_best_template: neg_rank
negated_best_fitness: 0.09
n_negated_sims: 4
direction_gap: -0.02
---
# rp_ess_equity (news18)

*Event sentiment score of equity action news*

## Signal Profile
- `rank(rp_ess_equity)`: S=-0.24, F=-0.02, T=142.2%, INFERIOR (TOP3000)
- `rank(ts_delta(rp_ess_equity, 5))`: S=0.00, F=0.00, T=134.1%, INFERIOR (TOP200)
- `-rank(rp_ess_equity)`: S=0.60, F=0.09, T=127.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(rp_ess_equity, 5))`: S=0.28, F=0.03, T=162.3%, INFERIOR (TOP3000)
- `-ts_zscore(rp_ess_equity, 63)`: S=0.62, F=0.09, T=128.4%, INFERIOR (TOP3000)
- `ts_mean(rp_ess_equity, 10)`: S=-0.08, F=-0.01, T=20.4%, INFERIOR (TOP3000)
- `rank(ts_rank(rp_ess_equity, 22))`: S=-0.87, F=-0.15, T=131.1%, INFERIOR (TOP3000)
- `rank(-1 * rp_ess_equity)`: S=0.24, F=0.02, T=142.2%, INFERIOR (TOP3000)
- `rank(-1 * rp_ess_equity / close)`: S=-0.04, F=0.00, T=128.8%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 3F/17P
- HIGH_TURNOVER: 19F/1P
- LOW_FITNESS: 20F/0P
- LOW_SHARPE: 20F/0P
- LOW_SUB_UNIVERSE_SHARPE: 9F/9P

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
Best negated: `-rank(rp_ess_equity)` S=0.60, F=0.09, INFERIOR
Direction gap: -0.02 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * rp_ess_equity)`: S=0.24, F=0.02, T=142.2%, INFERIOR (TOP3000)
- `rank(-1 * rp_ess_equity / close)`: S=-0.04, F=0.00, T=128.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(rp_ess_equity, 5))`: S=0.28, F=0.03, T=162.3%, INFERIOR (TOP3000)

## Variation Breakdown
No per-variation PnL data available for this field.

## Correlation Notes
No correlation data available for this field.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, rank_value_norm, trade_when
