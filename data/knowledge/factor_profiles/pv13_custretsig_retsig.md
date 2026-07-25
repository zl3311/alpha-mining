---
field: pv13_custretsig_retsig
dataset: pv13
best_template: neg_rank_level
best_sharpe: 1.9
best_fitness: 0.92
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_FITNESS
n_sims: 26
negated_best_sharpe: 1.9
negated_best_template: neg_rank_level
negated_best_fitness: 0.92
n_negated_sims: 11
direction_gap: 0.62
---
# pv13_custretsig_retsig (pv13)

*Sign of customer return*

## Signal Profile
- `rank(pv13_custretsig_retsig)`: S=-1.24, F=-0.56, T=69.4%, INFERIOR (TOP200)
- `rank(pv13_custretsig_retsig / close)`: S=-1.31, F=-0.58, T=69.8%, INFERIOR (TOP3000)
- `rank(ts_delta(pv13_custretsig_retsig, 5))`: S=-1.19, F=-0.47, T=75.9%, INFERIOR (TOP200)
- `-rank(pv13_custretsig_retsig)`: S=1.67, F=0.81, T=69.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(pv13_custretsig_retsig, 5))`: S=1.82, F=0.75, T=77.2%, INFERIOR (TOP3000)
- `-ts_zscore(pv13_custretsig_retsig, 63)`: S=1.28, F=0.58, T=65.5%, INFERIOR (TOP3000)
- `ts_mean(pv13_custretsig_retsig, 10)`: S=-0.41, F=-0.17, T=23.2%, INFERIOR (TOP3000)
- `rank(ts_rank(pv13_custretsig_retsig, 22))`: S=-1.82, F=-0.86, T=69.4%, INFERIOR (TOP3000)
- `rank(-1 * pv13_custretsig_retsig)`: S=1.90, F=0.92, T=70.0%, INFERIOR (TOP3000)
- `rank(-1 * pv13_custretsig_retsig / close)`: S=1.31, F=0.55, T=70.6%, INFERIOR (TOP3000)

## Check Summary
- HIGH_TURNOVER: 16F/10P
- LOW_FITNESS: 26F/0P
- LOW_SHARPE: 14F/12P
- LOW_SUB_UNIVERSE_SHARPE: 10F/14P

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
Best negated: `rank(-1 * pv13_custretsig_retsig)` S=1.90, F=0.92, INFERIOR
Direction gap: +0.62 (negated - positive best Sharpe). NEGATION DOMINANT — field is significantly stronger when reversed.

Negated template variants:
- `rank(-1 * pv13_custretsig_retsig)`: S=1.90, F=0.92, T=70.0%, INFERIOR (TOP3000)
- `rank(-1 * pv13_custretsig_retsig / close)`: S=1.31, F=0.55, T=70.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(pv13_custretsig_retsig, 5))`: S=1.82, F=0.75, T=77.2%, INFERIOR (TOP3000)

## Variation Breakdown
No per-variation PnL data available for this field.

## Correlation Notes
No correlation data available for this field.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_FITNESS. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
