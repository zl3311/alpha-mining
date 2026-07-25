---
field: rel_ret_cust
dataset: pv13
best_template: neg_rank_level
best_sharpe: 1.21
best_fitness: 0.28
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 25
negated_best_sharpe: 1.21
negated_best_template: neg_rank_level
negated_best_fitness: 0.28
n_negated_sims: 10
direction_gap: 0.72
---
# rel_ret_cust (pv13)

*averaged one-day-return of the instrument's customers*

## Signal Profile
- `rank(rel_ret_cust)`: S=-0.39, F=-0.07, T=71.3%, INFERIOR (TOP500)
- `rank(rel_ret_cust / close)`: S=-0.42, F=-0.07, T=72.5%, INFERIOR (TOP3000)
- `rank(ts_delta(rel_ret_cust, 5))`: S=-0.15, F=-0.02, T=76.9%, INFERIOR (TOP500)
- `-rank(rel_ret_cust)`: S=0.62, F=0.12, T=72.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(rel_ret_cust, 5))`: S=0.91, F=0.18, T=78.5%, INFERIOR (TOP3000)
- `-ts_zscore(rel_ret_cust, 63)`: S=0.67, F=0.15, T=70.2%, INFERIOR (TOP3000)
- `ts_mean(rel_ret_cust, 10)`: S=0.49, F=0.16, T=23.0%, INFERIOR (TOP3000)
- `rank(ts_rank(rel_ret_cust, 22))`: S=-0.46, F=-0.07, T=73.2%, INFERIOR (TOP3000)
- `rank(-1 * rel_ret_cust)`: S=1.21, F=0.28, T=73.5%, INFERIOR (TOP3000)
- `rank(-1 * rel_ret_cust / close)`: S=0.94, F=0.20, T=73.8%, INFERIOR (TOP3000)

## Check Summary
- HIGH_TURNOVER: 24F/1P
- LOW_FITNESS: 25F/0P
- LOW_SHARPE: 25F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/10P

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
Best negated: `rank(-1 * rel_ret_cust)` S=1.21, F=0.28, INFERIOR
Direction gap: +0.72 (negated - positive best Sharpe). NEGATION DOMINANT — field is significantly stronger when reversed.

Negated template variants:
- `rank(-1 * rel_ret_cust)`: S=1.21, F=0.28, T=73.5%, INFERIOR (TOP3000)
- `rank(-1 * rel_ret_cust / close)`: S=0.94, F=0.20, T=73.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(rel_ret_cust, 5))`: S=0.91, F=0.18, T=78.5%, INFERIOR (TOP3000)

## Variation Breakdown
No per-variation PnL data available for this field.

## Correlation Notes
No correlation data available for this field.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
