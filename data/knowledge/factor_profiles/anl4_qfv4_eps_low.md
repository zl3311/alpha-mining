---
field: anl4_qfv4_eps_low
dataset: analyst4
best_template: rank_value_norm
best_sharpe: 0.81
best_fitness: 0.64
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
negated_best_sharpe: 0.13
negated_best_template: rank_neg_delta
negated_best_fitness: 0.02
n_negated_sims: 10
direction_gap: -0.68
---
# anl4_qfv4_eps_low (analyst4)

*Earnings per share - The lowest estimation*

## Signal Profile
- `rank(anl4_qfv4_eps_low)`: S=0.38, F=0.23, T=1.3%, INFERIOR (TOP3000)
- `rank(anl4_qfv4_eps_low / close)`: S=0.81, F=0.64, T=2.3%, INFERIOR (TOP3000)
- `rank(ts_delta(anl4_qfv4_eps_low, 5))`: S=0.49, F=0.17, T=35.9%, INFERIOR (TOP200)
- `-rank(anl4_qfv4_eps_low)`: S=-0.16, F=-0.06, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_qfv4_eps_low, 5))`: S=0.13, F=0.02, T=37.2%, INFERIOR (TOP3000)
- `ts_zscore(anl4_qfv4_eps_low, 22)`: S=0.25, F=0.05, T=34.8%, INFERIOR (TOP3000)
- `ts_mean(anl4_qfv4_eps_low, 10)`: S=-0.11, F=-0.03, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_qfv4_eps_low, 22))`: S=-0.11, F=-0.02, T=14.0%, INFERIOR (TOP3000)
- `rank(-1 * anl4_qfv4_eps_low)`: S=-0.06, F=-0.01, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * anl4_qfv4_eps_low / close)`: S=-0.03, F=-0.01, T=3.2%, INFERIOR (TOP3000)

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
Best negated: `rank(-1 * ts_delta(anl4_qfv4_eps_low, 5))` S=0.13, F=0.02, INFERIOR
Direction gap: -0.68 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * anl4_qfv4_eps_low)`: S=-0.06, F=-0.01, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * anl4_qfv4_eps_low / close)`: S=-0.03, F=-0.01, T=3.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_qfv4_eps_low, 5))`: S=0.13, F=0.02, T=37.2%, INFERIOR (TOP3000)

## Variation Breakdown
No per-variation PnL data available for this field.

## Correlation Notes
No correlation data available for this field.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
