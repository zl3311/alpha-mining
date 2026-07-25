---
field: unsystematic_risk_last_360_days - unsystematic_risk_last_90_days
dataset: model51
best_template: rank_neg_delta
best_sharpe: 0.27
best_fitness: 0.04
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 3
negated_best_sharpe: 0.27
negated_best_template: rank_neg_delta
negated_best_fitness: 0.04
n_negated_sims: 2
direction_gap: 0.71
---
# unsystematic_risk_last_360_days - unsystematic_risk_last_90_days (model51)


## Signal Profile
- `rank(unsystematic_risk_last_360_days - unsystematic_risk_last_90_days)`: S=-0.44, F=-0.17, T=21.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(unsystematic_risk_last_360_days - unsystematic_risk_last_90_days, 5))`: S=0.27, F=0.04, T=58.4%, INFERIOR (TOP3000)
- `rank(-1 * unsystematic_risk_last_360_days - unsystematic_risk_last_90_days)`: S=0.04, F=0.01, T=15.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 3F/0P
- LOW_FITNESS: 3F/0P
- LOW_SHARPE: 3F/0P
- LOW_SUB_UNIVERSE_SHARPE: 2F/1P

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
Best negated: `rank(-1 * ts_delta(unsystematic_risk_last_360_days - unsystematic_risk_last_90_days, 5))` S=0.27, F=0.04, INFERIOR
Direction gap: +0.71 (negated - positive best Sharpe). NEGATION DOMINANT — field is significantly stronger when reversed.

Negated template variants:
- `rank(-1 * unsystematic_risk_last_360_days - unsystematic_risk_last_90_days)`: S=0.04, F=0.01, T=15.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(unsystematic_risk_last_360_days - unsystematic_risk_last_90_days, 5))`: S=0.27, F=0.04, T=58.4%, INFERIOR (TOP3000)

## Variation Breakdown
No per-variation PnL data available for this field.

## Correlation Notes
No correlation data available for this field.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, rank_delta, rank_value_norm, trade_when
