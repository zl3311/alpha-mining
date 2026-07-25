---
field: anl4_qfv4_cfps_number
dataset: analyst4
best_template: rank_value_norm
best_sharpe: 0.48
best_fitness: 0.29
best_universe: TOP1000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
negated_best_sharpe: 0.53
negated_best_template: rank_neg_delta
negated_best_fitness: 0.26
n_negated_sims: 10
direction_gap: 0.05
---
# anl4_qfv4_cfps_number (analyst4)

*Cash Flow Per Share - number of estimations*

## Signal Profile
- `rank(anl4_qfv4_cfps_number)`: S=-0.01, F=0.00, T=1.6%, INFERIOR (TOP3000)
- `rank(anl4_qfv4_cfps_number / close)`: S=0.48, F=0.29, T=1.9%, INFERIOR (TOP1000)
- `rank(ts_delta(anl4_qfv4_cfps_number, 5))`: S=-0.27, F=-0.12, T=31.8%, INFERIOR (TOP200)
- `-rank(anl4_qfv4_cfps_number)`: S=0.01, F=0.00, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_qfv4_cfps_number, 5))`: S=0.53, F=0.26, T=32.1%, INFERIOR (TOP3000)
- `ts_zscore(anl4_qfv4_cfps_number, 22)`: S=-0.12, F=-0.04, T=29.2%, INFERIOR (TOP3000)
- `ts_mean(anl4_qfv4_cfps_number, 10)`: S=0.40, F=0.18, T=2.6%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_qfv4_cfps_number, 22))`: S=0.13, F=0.04, T=13.8%, INFERIOR (TOP3000)
- `rank(-1 * anl4_qfv4_cfps_number)`: S=0.01, F=0.00, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * anl4_qfv4_cfps_number / close)`: S=-0.48, F=-0.29, T=1.9%, INFERIOR (TOP3000)

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
Best negated: `rank(-1 * ts_delta(anl4_qfv4_cfps_number, 5))` S=0.53, F=0.26, INFERIOR
Direction gap: +0.05 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * anl4_qfv4_cfps_number)`: S=0.01, F=0.00, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * anl4_qfv4_cfps_number / close)`: S=-0.48, F=-0.29, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_qfv4_cfps_number, 5))`: S=0.53, F=0.26, T=32.1%, INFERIOR (TOP3000)

## Variation Breakdown
No per-variation PnL data available for this field.

## Correlation Notes
No correlation data available for this field.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
