---
field: anl4_qfv4_div_low
dataset: analyst4
best_template: rank_neg_delta
best_sharpe: 1.36
best_fitness: 0.92
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_FITNESS
n_sims: 32
negated_best_sharpe: 1.36
negated_best_template: rank_neg_delta
negated_best_fitness: 0.92
n_negated_sims: 10
direction_gap: 0.99
---
# anl4_qfv4_div_low (analyst4)

*Dividend per share - The lowest estimation*

## Signal Profile
- `rank(anl4_qfv4_div_low)`: S=-0.12, F=-0.03, T=1.3%, INFERIOR (TOP1000)
- `rank(anl4_qfv4_div_low / close)`: S=0.37, F=0.18, T=1.9%, INFERIOR (TOP1000)
- `rank(ts_delta(anl4_qfv4_div_low, 5))`: S=0.39, F=0.09, T=37.1%, INFERIOR (TOP3000)
- `-rank(anl4_qfv4_div_low)`: S=0.12, F=0.03, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_qfv4_div_low, 5))`: S=1.36, F=0.92, T=34.0%, INFERIOR (TOP3000)
- `ts_zscore(anl4_qfv4_div_low, 22)`: S=0.13, F=0.03, T=33.3%, INFERIOR (TOP3000)
- `ts_mean(anl4_qfv4_div_low, 10)`: S=0.10, F=0.02, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_qfv4_div_low, 22))`: S=0.26, F=0.07, T=13.5%, INFERIOR (TOP3000)
- `rank(-1 * anl4_qfv4_div_low)`: S=0.59, F=0.39, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * anl4_qfv4_div_low / close)`: S=0.63, F=0.47, T=2.5%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 9F/23P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 29F/3P
- LOW_SUB_UNIVERSE_SHARPE: 10F/10P
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
Best negated: `rank(-1 * ts_delta(anl4_qfv4_div_low, 5))` S=1.36, F=0.92, INFERIOR
Direction gap: +0.99 (negated - positive best Sharpe). NEGATION DOMINANT — field is significantly stronger when reversed.

Negated template variants:
- `rank(-1 * anl4_qfv4_div_low)`: S=0.59, F=0.39, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * anl4_qfv4_div_low / close)`: S=0.63, F=0.47, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_qfv4_div_low, 5))`: S=1.36, F=0.92, T=34.0%, INFERIOR (TOP3000)

## Variation Breakdown
No per-variation PnL data available for this field.

## Correlation Notes
No correlation data available for this field.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_FITNESS. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
