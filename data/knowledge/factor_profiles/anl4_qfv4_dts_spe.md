---
field: anl4_qfv4_dts_spe
dataset: analyst4
best_template: rank_level
best_sharpe: 1.18
best_fitness: 0.73
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
negated_best_sharpe: 0.2
negated_best_template: rank_neg_delta
negated_best_fitness: 0.05
n_negated_sims: 10
direction_gap: -0.98
---
# anl4_qfv4_dts_spe (analyst4)

*Earnings per share - standard deviation of estimations*

## Signal Profile
- `rank(anl4_qfv4_dts_spe)`: S=1.18, F=0.73, T=4.6%, INFERIOR (TOP3000)
- `rank(anl4_qfv4_dts_spe / close)`: S=0.53, F=0.36, T=7.4%, INFERIOR (TOP200)
- `rank(ts_delta(anl4_qfv4_dts_spe, 5))`: S=0.45, F=0.12, T=39.1%, INFERIOR (TOP500)
- `-rank(anl4_qfv4_dts_spe)`: S=-0.33, F=-0.12, T=5.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_qfv4_dts_spe, 5))`: S=0.20, F=0.05, T=38.1%, INFERIOR (TOP3000)
- `ts_zscore(anl4_qfv4_dts_spe, 22)`: S=0.50, F=0.14, T=33.5%, INFERIOR (TOP3000)
- `ts_mean(anl4_qfv4_dts_spe, 10)`: S=0.12, F=0.04, T=4.3%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_qfv4_dts_spe, 22))`: S=0.43, F=0.13, T=17.0%, INFERIOR (TOP3000)
- `rank(-1 * anl4_qfv4_dts_spe)`: S=-0.25, F=-0.11, T=6.8%, INFERIOR (TOP3000)
- `rank(-1 * anl4_qfv4_dts_spe / close)`: S=-0.53, F=-0.36, T=7.4%, INFERIOR (TOP3000)

## Check Summary
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 5F/15P

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
Best negated: `rank(-1 * ts_delta(anl4_qfv4_dts_spe, 5))` S=0.20, F=0.05, INFERIOR
Direction gap: -0.98 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * anl4_qfv4_dts_spe)`: S=-0.25, F=-0.11, T=6.8%, INFERIOR (TOP3000)
- `rank(-1 * anl4_qfv4_dts_spe / close)`: S=-0.53, F=-0.36, T=7.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_qfv4_dts_spe, 5))`: S=0.20, F=0.05, T=38.1%, INFERIOR (TOP3000)

## Variation Breakdown
No per-variation PnL data available for this field.

## Correlation Notes
No correlation data available for this field.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
