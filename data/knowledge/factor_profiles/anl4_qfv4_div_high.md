---
field: anl4_qfv4_div_high
dataset: analyst4
best_template: neg_rank_value_norm
best_sharpe: 0.56
best_fitness: 0.4
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
negated_best_sharpe: 0.56
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.4
n_negated_sims: 10
direction_gap: 0.01
---
# anl4_qfv4_div_high (analyst4)

*Dividend per share - The highest estimation*

## Signal Profile
- `rank(anl4_qfv4_div_high)`: S=-0.07, F=-0.01, T=1.3%, INFERIOR (TOP1000)
- `rank(anl4_qfv4_div_high / close)`: S=0.46, F=0.25, T=1.9%, INFERIOR (TOP1000)
- `rank(ts_delta(anl4_qfv4_div_high, 5))`: S=0.55, F=0.25, T=33.6%, INFERIOR (TOP200)
- `-rank(anl4_qfv4_div_high)`: S=0.07, F=0.01, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_qfv4_div_high, 5))`: S=-0.55, F=-0.25, T=33.6%, INFERIOR (TOP3000)
- `ts_zscore(anl4_qfv4_div_high, 22)`: S=0.48, F=0.18, T=33.6%, INFERIOR (TOP3000)
- `ts_mean(anl4_qfv4_div_high, 10)`: S=0.12, F=0.03, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_qfv4_div_high, 22))`: S=0.15, F=0.03, T=13.4%, INFERIOR (TOP3000)
- `rank(-1 * anl4_qfv4_div_high)`: S=0.46, F=0.28, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * anl4_qfv4_div_high / close)`: S=0.56, F=0.40, T=2.6%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 9F/23P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 9F/11P
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
Best negated: `rank(-1 * anl4_qfv4_div_high / close)` S=0.56, F=0.40, INFERIOR
Direction gap: +0.01 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * anl4_qfv4_div_high)`: S=0.46, F=0.28, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * anl4_qfv4_div_high / close)`: S=0.56, F=0.40, T=2.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_qfv4_div_high, 5))`: S=-0.55, F=-0.25, T=33.6%, INFERIOR (TOP3000)

## Variation Breakdown
No per-variation PnL data available for this field.

## Correlation Notes
No correlation data available for this field.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
