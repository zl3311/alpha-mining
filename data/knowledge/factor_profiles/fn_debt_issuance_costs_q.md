---
field: fn_debt_issuance_costs_q
dataset: fundamental2
best_template: neg_rank
best_sharpe: 0.57
best_fitness: 0.24
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
negated_best_sharpe: 0.57
negated_best_template: neg_rank
negated_best_fitness: 0.24
n_negated_sims: 10
direction_gap: 0.28
---
# fn_debt_issuance_costs_q (fundamental2)

*Amount of debt issuance costs (for example, but not limited to, legal, accounting, broker, and regulatory fees).*

## Signal Profile
- `rank(fn_debt_issuance_costs_q)`: S=-0.34, F=-0.09, T=1.6%, INFERIOR (TOP3000)
- `rank(fn_debt_issuance_costs_q / close)`: S=-0.16, F=-0.03, T=1.7%, INFERIOR (TOP3000)
- `rank(ts_delta(fn_debt_issuance_costs_q, 5))`: S=-0.04, F=-0.01, T=36.1%, INFERIOR (TOP500)
- `-rank(fn_debt_issuance_costs_q)`: S=0.57, F=0.24, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_debt_issuance_costs_q, 5))`: S=0.17, F=0.05, T=35.4%, INFERIOR (TOP3000)
- `-ts_zscore(fn_debt_issuance_costs_q, 63)`: S=0.29, F=0.13, T=15.9%, INFERIOR (TOP3000)
- `ts_mean(fn_debt_issuance_costs_q, 10)`: S=-0.02, F=0.00, T=2.3%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_debt_issuance_costs_q, 22))`: S=-0.32, F=-0.14, T=16.4%, INFERIOR (TOP3000)
- `rank(-1 * fn_debt_issuance_costs_q)`: S=0.57, F=0.24, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * fn_debt_issuance_costs_q / close)`: S=0.42, F=0.16, T=2.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 13F/19P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 15F/14P

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
Best negated: `-rank(fn_debt_issuance_costs_q)` S=0.57, F=0.24, INFERIOR
Direction gap: +0.28 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fn_debt_issuance_costs_q)`: S=0.57, F=0.24, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * fn_debt_issuance_costs_q / close)`: S=0.42, F=0.16, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_debt_issuance_costs_q, 5))`: S=0.17, F=0.05, T=35.4%, INFERIOR (TOP3000)

## Variation Breakdown
No per-variation PnL data available for this field.

## Correlation Notes
No correlation data available for this field.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
