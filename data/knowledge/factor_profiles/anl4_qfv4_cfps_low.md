---
field: anl4_qfv4_cfps_low
dataset: analyst4
best_template: rank_delta
best_sharpe: 1.44
best_fitness: 0.74
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_FITNESS
n_sims: 32
negated_best_sharpe: 0.38
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.23
n_negated_sims: 10
direction_gap: -1.06
---
# anl4_qfv4_cfps_low (analyst4)

*Cash Flow Per Share - The lowest estimation*

## Signal Profile
- `rank(anl4_qfv4_cfps_low)`: S=0.29, F=0.12, T=0.9%, INFERIOR (TOP3000)
- `rank(anl4_qfv4_cfps_low / close)`: S=0.78, F=0.55, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_delta(anl4_qfv4_cfps_low, 5))`: S=1.44, F=0.74, T=36.5%, INFERIOR (TOP3000)
- `-rank(anl4_qfv4_cfps_low)`: S=-0.01, F=0.00, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_qfv4_cfps_low, 5))`: S=-0.51, F=-0.25, T=34.7%, INFERIOR (TOP3000)
- `ts_zscore(anl4_qfv4_cfps_low, 22)`: S=0.22, F=0.06, T=30.9%, INFERIOR (TOP3000)
- `ts_mean(anl4_qfv4_cfps_low, 10)`: S=-0.05, F=-0.01, T=1.4%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_qfv4_cfps_low, 22))`: S=0.17, F=0.04, T=13.9%, INFERIOR (TOP3000)
- `rank(-1 * anl4_qfv4_cfps_low)`: S=0.36, F=0.18, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * anl4_qfv4_cfps_low / close)`: S=0.38, F=0.23, T=2.8%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 9F/23P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 31F/1P
- LOW_SUB_UNIVERSE_SHARPE: 11F/9P
- LOW_TURNOVER: 1F/31P

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
Best negated: `rank(-1 * anl4_qfv4_cfps_low / close)` S=0.38, F=0.23, INFERIOR
Direction gap: -1.06 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * anl4_qfv4_cfps_low)`: S=0.36, F=0.18, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * anl4_qfv4_cfps_low / close)`: S=0.38, F=0.23, T=2.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_qfv4_cfps_low, 5))`: S=-0.51, F=-0.25, T=34.7%, INFERIOR (TOP3000)

## Variation Breakdown
No per-variation PnL data available for this field.

## Correlation Notes
No correlation data available for this field.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_FITNESS. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
