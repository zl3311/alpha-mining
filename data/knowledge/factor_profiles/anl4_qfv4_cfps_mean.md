---
field: anl4_qfv4_cfps_mean
dataset: analyst4
best_template: rank_value_norm
best_sharpe: 0.78
best_fitness: 0.55
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
negated_best_sharpe: 0.4
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.25
n_negated_sims: 10
direction_gap: -0.38
---
# anl4_qfv4_cfps_mean (analyst4)

*Cash Flow Per Share - average of estimations*

## Signal Profile
- `rank(anl4_qfv4_cfps_mean)`: S=0.30, F=0.13, T=0.9%, INFERIOR (TOP3000)
- `rank(anl4_qfv4_cfps_mean / close)`: S=0.78, F=0.55, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_delta(anl4_qfv4_cfps_mean, 5))`: S=0.64, F=0.21, T=36.2%, INFERIOR (TOP3000)
- `-rank(anl4_qfv4_cfps_mean)`: S=-0.01, F=0.00, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_qfv4_cfps_mean, 5))`: S=-0.30, F=-0.11, T=34.8%, INFERIOR (TOP3000)
- `-ts_zscore(anl4_qfv4_cfps_mean, 63)`: S=0.21, F=0.06, T=16.2%, INFERIOR (TOP3000)
- `ts_mean(anl4_qfv4_cfps_mean, 10)`: S=-0.06, F=-0.01, T=1.4%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_qfv4_cfps_mean, 22))`: S=0.06, F=0.01, T=14.0%, INFERIOR (TOP3000)
- `rank(-1 * anl4_qfv4_cfps_mean)`: S=0.33, F=0.16, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * anl4_qfv4_cfps_mean / close)`: S=0.40, F=0.25, T=2.7%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 6F/26P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/7P
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
Best negated: `rank(-1 * anl4_qfv4_cfps_mean / close)` S=0.40, F=0.25, INFERIOR
Direction gap: -0.38 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * anl4_qfv4_cfps_mean)`: S=0.33, F=0.16, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * anl4_qfv4_cfps_mean / close)`: S=0.40, F=0.25, T=2.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_qfv4_cfps_mean, 5))`: S=-0.30, F=-0.11, T=34.8%, INFERIOR (TOP3000)

## Variation Breakdown
No per-variation PnL data available for this field.

## Correlation Notes
No correlation data available for this field.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
