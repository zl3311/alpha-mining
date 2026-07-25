---
field: cashflow_per_share_estimate_count
dataset: analyst4
best_template: rank_neg_delta
best_sharpe: 0.93
best_fitness: 0.49
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
negated_best_sharpe: 0.93
negated_best_template: rank_neg_delta
negated_best_fitness: 0.49
n_negated_sims: 10
direction_gap: 0.45
---
# cashflow_per_share_estimate_count (analyst4)

*Cash Flow Per Share - number of estimations - delay1*

## Signal Profile
- `rank(cashflow_per_share_estimate_count)`: S=-0.01, F=0.00, T=1.6%, INFERIOR (TOP3000)
- `rank(cashflow_per_share_estimate_count / close)`: S=0.48, F=0.29, T=1.9%, INFERIOR (TOP1000)
- `rank(ts_delta(cashflow_per_share_estimate_count, 5))`: S=-0.29, F=-0.06, T=35.3%, INFERIOR (TOP1000)
- `-rank(cashflow_per_share_estimate_count)`: S=0.01, F=0.00, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(cashflow_per_share_estimate_count, 5))`: S=0.93, F=0.49, T=33.1%, INFERIOR (TOP3000)
- `-ts_zscore(cashflow_per_share_estimate_count, 63)`: S=-0.19, F=-0.06, T=18.2%, INFERIOR (TOP3000)
- `ts_mean(cashflow_per_share_estimate_count, 10)`: S=0.40, F=0.18, T=2.6%, INFERIOR (TOP3000)
- `rank(ts_rank(cashflow_per_share_estimate_count, 22))`: S=-0.24, F=-0.07, T=12.8%, INFERIOR (TOP3000)
- `rank(-1 * cashflow_per_share_estimate_count)`: S=0.12, F=0.04, T=4.2%, INFERIOR (TOP3000)
- `rank(-1 * cashflow_per_share_estimate_count / close)`: S=0.04, F=0.01, T=2.8%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 10F/22P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 11F/9P

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
Best negated: `rank(-1 * ts_delta(cashflow_per_share_estimate_count, 5))` S=0.93, F=0.49, INFERIOR
Direction gap: +0.45 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * cashflow_per_share_estimate_count)`: S=0.12, F=0.04, T=4.2%, INFERIOR (TOP3000)
- `rank(-1 * cashflow_per_share_estimate_count / close)`: S=0.04, F=0.01, T=2.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(cashflow_per_share_estimate_count, 5))`: S=0.93, F=0.49, T=33.1%, INFERIOR (TOP3000)

## Variation Breakdown
No per-variation PnL data available for this field.

## Correlation Notes
No correlation data available for this field.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
