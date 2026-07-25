---
field: rp_css_marketing
dataset: news18
best_template: neg_rank
best_sharpe: 0.9
best_fitness: 0.37
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 20
negated_best_sharpe: 0.9
negated_best_template: neg_rank
negated_best_fitness: 0.37
n_negated_sims: 4
direction_gap: 0.12
---
# rp_css_marketing (news18)

*Composite sentiment score of marketing news*

## Signal Profile
- `rank(rp_css_marketing)`: S=-0.32, F=-0.08, T=166.3%, INFERIOR (TOP3000)
- `rank(ts_delta(rp_css_marketing, 5))`: S=0.00, F=0.00, T=68.4%, INFERIOR (TOP200)
- `-rank(rp_css_marketing)`: S=0.90, F=0.37, T=152.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(rp_css_marketing, 5))`: S=0.33, F=0.09, T=90.3%, INFERIOR (TOP3000)
- `-ts_zscore(rp_css_marketing, 63)`: S=0.78, F=0.30, T=146.2%, INFERIOR (TOP3000)
- `ts_mean(rp_css_marketing, 10)`: S=-0.35, F=-0.11, T=37.5%, INFERIOR (TOP3000)
- `rank(ts_rank(rp_css_marketing, 22))`: S=-0.56, F=-0.18, T=153.2%, INFERIOR (TOP3000)
- `rank(-1 * rp_css_marketing)`: S=0.32, F=0.08, T=166.3%, INFERIOR (TOP3000)
- `rank(-1 * rp_css_marketing / close)`: S=0.09, F=0.01, T=165.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 20F/0P
- HIGH_TURNOVER: 18F/2P
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
Best negated: `-rank(rp_css_marketing)` S=0.90, F=0.37, INFERIOR
Direction gap: +0.12 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * rp_css_marketing)`: S=0.32, F=0.08, T=166.3%, INFERIOR (TOP3000)
- `rank(-1 * rp_css_marketing / close)`: S=0.09, F=0.01, T=165.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(rp_css_marketing, 5))`: S=0.33, F=0.09, T=90.3%, INFERIOR (TOP3000)

## Variation Breakdown
No per-variation PnL data available for this field.

## Correlation Notes
No correlation data available for this field.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, rank_value_norm, trade_when
