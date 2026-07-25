---
field: rp_css_legal
dataset: news18
best_template: ts_zscore
best_sharpe: 0.8
best_fitness: 0.22
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 20
negated_best_sharpe: 0.59
negated_best_template: neg_rank
negated_best_fitness: 0.14
n_negated_sims: 4
direction_gap: -0.21
---
# rp_css_legal (news18)

*Composite sentiment score of legal news*

## Signal Profile
- `rank(rp_css_legal)`: S=-0.10, F=-0.01, T=147.9%, INFERIOR (TOP3000)
- `rank(ts_delta(rp_css_legal, 5))`: S=-0.20, F=-0.04, T=150.7%, INFERIOR (TOP3000)
- `-rank(rp_css_legal)`: S=0.59, F=0.14, T=146.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(rp_css_legal, 5))`: S=0.20, F=0.04, T=150.7%, INFERIOR (TOP3000)
- `-ts_zscore(rp_css_legal, 63)`: S=0.80, F=0.22, T=146.0%, INFERIOR (TOP3000)
- `ts_mean(rp_css_legal, 10)`: S=-0.08, F=-0.01, T=31.6%, INFERIOR (TOP3000)
- `rank(ts_rank(rp_css_legal, 22))`: S=-0.31, F=-0.05, T=150.2%, INFERIOR (TOP3000)
- `rank(-1 * rp_css_legal)`: S=0.10, F=0.01, T=147.9%, INFERIOR (TOP3000)
- `rank(-1 * rp_css_legal / close)`: S=0.21, F=0.03, T=146.6%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 19F/1P
- HIGH_TURNOVER: 19F/1P
- LOW_FITNESS: 20F/0P
- LOW_SHARPE: 20F/0P
- LOW_SUB_UNIVERSE_SHARPE: 6F/12P

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
Best negated: `-rank(rp_css_legal)` S=0.59, F=0.14, INFERIOR
Direction gap: -0.21 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * rp_css_legal)`: S=0.10, F=0.01, T=147.9%, INFERIOR (TOP3000)
- `rank(-1 * rp_css_legal / close)`: S=0.21, F=0.03, T=146.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(rp_css_legal, 5))`: S=0.20, F=0.04, T=150.7%, INFERIOR (TOP3000)

## Variation Breakdown
No per-variation PnL data available for this field.

## Correlation Notes
No correlation data available for this field.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, rank_value_norm, trade_when
