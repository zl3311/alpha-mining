---
field: rp_css_society
dataset: news18
best_template: ts_zscore
best_sharpe: 0.7
best_fitness: 0.17
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 20
negated_best_sharpe: 0.59
negated_best_template: neg_rank
negated_best_fitness: 0.13
n_negated_sims: 4
direction_gap: -0.11
---
# rp_css_society (news18)

*Composite sentiment score of society-related news*

## Signal Profile
- `rank(rp_css_society)`: S=0.04, F=0.00, T=147.9%, INFERIOR (TOP3000)
- `rank(ts_delta(rp_css_society, 5))`: S=0.11, F=0.01, T=151.3%, INFERIOR (TOP3000)
- `-rank(rp_css_society)`: S=0.59, F=0.13, T=145.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(rp_css_society, 5))`: S=-0.11, F=-0.01, T=151.3%, INFERIOR (TOP3000)
- `-ts_zscore(rp_css_society, 63)`: S=0.70, F=0.17, T=145.3%, INFERIOR (TOP3000)
- `ts_mean(rp_css_society, 10)`: S=-0.22, F=-0.05, T=30.8%, INFERIOR (TOP3000)
- `rank(ts_rank(rp_css_society, 22))`: S=-0.54, F=-0.11, T=149.9%, INFERIOR (TOP3000)
- `rank(-1 * rp_css_society)`: S=-0.04, F=0.00, T=147.9%, INFERIOR (TOP3000)
- `rank(-1 * rp_css_society / close)`: S=0.01, F=0.00, T=146.7%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 19F/1P
- HIGH_TURNOVER: 19F/1P
- LOW_FITNESS: 20F/0P
- LOW_SHARPE: 20F/0P
- LOW_SUB_UNIVERSE_SHARPE: 10F/8P

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
Best negated: `-rank(rp_css_society)` S=0.59, F=0.13, INFERIOR
Direction gap: -0.11 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * rp_css_society)`: S=-0.04, F=0.00, T=147.9%, INFERIOR (TOP3000)
- `rank(-1 * rp_css_society / close)`: S=0.01, F=0.00, T=146.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(rp_css_society, 5))`: S=-0.11, F=-0.01, T=151.3%, INFERIOR (TOP3000)

## Variation Breakdown
No per-variation PnL data available for this field.

## Correlation Notes
No correlation data available for this field.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, rank_value_norm, trade_when
