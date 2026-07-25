---
field: fn_oth_income_loss_derivatives_qualifying_as_hedges_of_tax_a
dataset: fundamental2
best_template: neg_rank_level
best_sharpe: 0.95
best_fitness: 0.62
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
negated_best_sharpe: 0.95
negated_best_template: neg_rank_level
negated_best_fitness: 0.62
n_negated_sims: 10
direction_gap: 0.96
---
# fn_oth_income_loss_derivatives_qualifying_as_hedges_of_tax_a (fundamental2)

*Amount after tax and reclassification adjustments, of increase (decrease) in accumulated gain (loss) from derivative instruments designated and qualifying as the effective portion of cash flow hedges and an entity's share of an equity investee's increase (decrease) in deferred hedging gain (loss).*

## Signal Profile
- `rank(fn_oth_income_loss_derivatives_qualifying_as_hedges_of_tax_a)`: S=-0.15, F=-0.03, T=1.0%, INFERIOR (TOP1000)
- `rank(fn_oth_income_loss_derivatives_qualifying_as_hedges_of_tax_a / close)`: S=-0.22, F=-0.05, T=1.1%, INFERIOR (TOP1000)
- `rank(ts_delta(fn_oth_income_loss_derivatives_qualifying_as_hedges_of_tax_a, 5))`: S=-0.06, F=-0.01, T=11.5%, INFERIOR (TOP200)
- `-rank(fn_oth_income_loss_derivatives_qualifying_as_hedges_of_tax_a)`: S=0.15, F=0.03, T=1.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_oth_income_loss_derivatives_qualifying_as_hedges_of_tax_a, 5))`: S=0.24, F=0.11, T=11.3%, INFERIOR (TOP3000)
- `-ts_zscore(fn_oth_income_loss_derivatives_qualifying_as_hedges_of_tax_a, 63)`: S=-0.01, F=0.00, T=8.6%, INFERIOR (TOP3000)
- `ts_mean(fn_oth_income_loss_derivatives_qualifying_as_hedges_of_tax_a, 10)`: S=-0.01, F=0.00, T=0.7%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_oth_income_loss_derivatives_qualifying_as_hedges_of_tax_a, 22))`: S=-0.29, F=-0.14, T=12.0%, INFERIOR (TOP3000)
- `rank(-1 * fn_oth_income_loss_derivatives_qualifying_as_hedges_of_tax_a)`: S=0.95, F=0.62, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * fn_oth_income_loss_derivatives_qualifying_as_hedges_of_tax_a / close)`: S=0.86, F=0.54, T=1.7%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 17F/3P
- LOW_TURNOVER: 7F/25P

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
Best negated: `rank(-1 * fn_oth_income_loss_derivatives_qualifying_as_hedges_of_tax_a)` S=0.95, F=0.62, INFERIOR
Direction gap: +0.96 (negated - positive best Sharpe). NEGATION DOMINANT — field is significantly stronger when reversed.

Negated template variants:
- `rank(-1 * fn_oth_income_loss_derivatives_qualifying_as_hedges_of_tax_a)`: S=0.95, F=0.62, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * fn_oth_income_loss_derivatives_qualifying_as_hedges_of_tax_a / close)`: S=0.86, F=0.54, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_oth_income_loss_derivatives_qualifying_as_hedges_of_tax_a, 5))`: S=0.24, F=0.11, T=11.3%, INFERIOR (TOP3000)

## Variation Breakdown
No per-variation PnL data available for this field.

## Correlation Notes
No correlation data available for this field.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
