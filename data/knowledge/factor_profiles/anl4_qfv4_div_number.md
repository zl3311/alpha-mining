---
field: anl4_qfv4_div_number
dataset: analyst4
best_template: rank_value_norm
best_sharpe: 0.62
best_fitness: 0.42
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
negated_best_sharpe: 0.37
negated_best_template: rank_neg_delta
negated_best_fitness: 0.08
n_negated_sims: 10
direction_gap: -0.25
---
# anl4_qfv4_div_number (analyst4)

*Dividend - number of estimations*

## Signal Profile
- `rank(anl4_qfv4_div_number)`: S=0.19, F=0.06, T=3.7%, INFERIOR (TOP200)
- `rank(anl4_qfv4_div_number / close)`: S=0.62, F=0.42, T=1.8%, INFERIOR (TOP3000)
- `rank(ts_delta(anl4_qfv4_div_number, 5))`: S=0.19, F=0.05, T=34.5%, INFERIOR (TOP200)
- `-rank(anl4_qfv4_div_number)`: S=-0.25, F=-0.06, T=2.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_qfv4_div_number, 5))`: S=0.37, F=0.08, T=35.9%, INFERIOR (TOP3000)
- `ts_zscore(anl4_qfv4_div_number, 22)`: S=0.35, F=0.12, T=33.9%, INFERIOR (TOP3000)
- `ts_mean(anl4_qfv4_div_number, 10)`: S=0.30, F=0.09, T=2.7%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_qfv4_div_number, 22))`: S=0.36, F=0.12, T=13.5%, INFERIOR (TOP3000)
- `rank(-1 * anl4_qfv4_div_number)`: S=-0.21, F=-0.04, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * anl4_qfv4_div_number / close)`: S=-0.62, F=-0.42, T=1.8%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 6F/26P
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
Best negated: `rank(-1 * ts_delta(anl4_qfv4_div_number, 5))` S=0.37, F=0.08, INFERIOR
Direction gap: -0.25 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * anl4_qfv4_div_number)`: S=-0.21, F=-0.04, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * anl4_qfv4_div_number / close)`: S=-0.62, F=-0.42, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_qfv4_div_number, 5))`: S=0.37, F=0.08, T=35.9%, INFERIOR (TOP3000)

## Variation Breakdown
No per-variation PnL data available for this field.

## Correlation Notes
No correlation data available for this field.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
