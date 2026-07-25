---
field: fnd6_newqv1300_glceeps12
dataset: fundamental6
best_template: rank_level
best_sharpe: 0.0
best_fitness: 0.0
best_universe: TOP3000
grade: UNKNOWN
submittability: blocked_LOW_SHARPE
n_sims: 26
negated_best_sharpe: 0.0
negated_best_template: neg_rank
negated_best_fitness: 0.0
n_negated_sims: 4
direction_gap: 0.0
---
# fnd6_newqv1300_glceeps12 (fundamental6)

*Gain/Loss on Sale (Core Earnings Adjusted) Basic EPS Effect 12MM*

## Signal Profile
- `rank(fnd6_newqv1300_glceeps12)`: S=0.00, F=0.00, T=0.0%, UNKNOWN (TOP3000)
- `rank(fnd6_newqv1300_glceeps12 / close)`: S=0.00, F=0.00, T=0.0%, UNKNOWN (TOP3000)
- `rank(ts_delta(fnd6_newqv1300_glceeps12, 5))`: S=0.00, F=0.00, T=0.0%, UNKNOWN (TOP3000)
- `-rank(fnd6_newqv1300_glceeps12)`: S=0.00, F=0.00, T=0.0%, UNKNOWN (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_glceeps12, 5))`: S=0.00, F=0.00, T=0.0%, UNKNOWN (TOP3000)
- `ts_zscore(fnd6_newqv1300_glceeps12, 22)`: S=0.00, F=0.00, T=0.0%, UNKNOWN (TOP3000)
- `ts_mean(fnd6_newqv1300_glceeps12, 10)`: S=0.00, F=0.00, T=0.0%, UNKNOWN (TOP3000)
- `rank(ts_rank(fnd6_newqv1300_glceeps12, 22))`: S=0.00, F=0.00, T=0.0%, UNKNOWN (TOP3000)
- `rank(-1 * fnd6_newqv1300_glceeps12)`: S=0.00, F=0.00, T=0.0%, UNKNOWN (TOP3000)
- `rank(-1 * fnd6_newqv1300_glceeps12 / close)`: S=0.00, F=0.00, T=0.0%, UNKNOWN (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 26F/0P
- LOW_SHARPE: 26F/0P
- LOW_TURNOVER: 26F/0P

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
Best negated: `-rank(fnd6_newqv1300_glceeps12)` S=0.00, F=0.00, UNKNOWN
Direction gap: +0.00 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_newqv1300_glceeps12)`: S=0.00, F=0.00, T=0.0%, UNKNOWN (TOP3000)
- `rank(-1 * fnd6_newqv1300_glceeps12 / close)`: S=0.00, F=0.00, T=0.0%, UNKNOWN (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_glceeps12, 5))`: S=0.00, F=0.00, T=0.0%, UNKNOWN (TOP3000)

## Variation Breakdown
No per-variation PnL data available for this field.

## Correlation Notes
No correlation data available for this field.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
