---
field: anl4_qfv4_median_eps
dataset: analyst4
best_template: rank_value_norm
best_sharpe: 0.9
best_fitness: 0.74
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
negated_best_sharpe: 0.16
negated_best_template: rank_neg_delta
negated_best_fitness: 0.03
n_negated_sims: 10
direction_gap: -0.74
---
# anl4_qfv4_median_eps (analyst4)

*Earnings per share - median of estimations*

## Signal Profile
- `rank(anl4_qfv4_median_eps)`: S=0.40, F=0.25, T=1.2%, INFERIOR (TOP3000)
- `rank(anl4_qfv4_median_eps / close)`: S=0.90, F=0.74, T=2.2%, INFERIOR (TOP3000)
- `rank(ts_delta(anl4_qfv4_median_eps, 5))`: S=0.41, F=0.09, T=36.7%, INFERIOR (TOP1000)
- `-rank(anl4_qfv4_median_eps)`: S=-0.16, F=-0.06, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_qfv4_median_eps, 5))`: S=0.16, F=0.03, T=36.9%, INFERIOR (TOP3000)
- `ts_zscore(anl4_qfv4_median_eps, 22)`: S=0.24, F=0.05, T=33.7%, INFERIOR (TOP3000)
- `ts_mean(anl4_qfv4_median_eps, 10)`: S=-0.10, F=-0.03, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_qfv4_median_eps, 22))`: S=0.08, F=0.01, T=14.3%, INFERIOR (TOP3000)
- `rank(-1 * anl4_qfv4_median_eps)`: S=-0.08, F=-0.02, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * anl4_qfv4_median_eps / close)`: S=-0.14, F=-0.05, T=3.0%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 2F/30P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 19F/10P

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
Best negated: `rank(-1 * ts_delta(anl4_qfv4_median_eps, 5))` S=0.16, F=0.03, INFERIOR
Direction gap: -0.74 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * anl4_qfv4_median_eps)`: S=-0.08, F=-0.02, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * anl4_qfv4_median_eps / close)`: S=-0.14, F=-0.05, T=3.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_qfv4_median_eps, 5))`: S=0.16, F=0.03, T=36.9%, INFERIOR (TOP3000)

## Variation Breakdown
No per-variation PnL data available for this field.

## Correlation Notes
No correlation data available for this field.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
