---
field: news_mins_1_chg
dataset: news12
best_template: ts_zscore
best_sharpe: 1.53
best_fitness: 0.39
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_FITNESS
n_sims: 20
negated_best_sharpe: 1.1
negated_best_template: rank_neg_delta
negated_best_fitness: 0.23
n_negated_sims: 4
direction_gap: -0.43
---
# news_mins_1_chg (news12)

*Minimum number of minutes taken for price to move (up or down) 1 percentage point after the event*

## Signal Profile
- `rank(news_mins_1_chg)`: S=0.09, F=0.01, T=125.2%, INFERIOR (TOP3000)
- `rank(ts_delta(news_mins_1_chg, 5))`: S=-0.24, F=-0.03, T=124.6%, INFERIOR (TOP200)
- `-rank(news_mins_1_chg)`: S=0.64, F=0.13, T=115.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(news_mins_1_chg, 5))`: S=1.10, F=0.23, T=149.5%, INFERIOR (TOP3000)
- `-ts_zscore(news_mins_1_chg, 63)`: S=1.53, F=0.39, T=117.1%, INFERIOR (TOP3000)
- `ts_mean(news_mins_1_chg, 10)`: S=-0.36, F=-0.10, T=22.5%, INFERIOR (TOP3000)
- `rank(ts_rank(news_mins_1_chg, 22))`: S=-1.05, F=-0.21, T=121.5%, INFERIOR (TOP3000)
- `rank(-1 * news_mins_1_chg)`: S=-0.09, F=-0.01, T=125.2%, INFERIOR (TOP3000)
- `rank(-1 * news_mins_1_chg / close)`: S=0.03, F=0.00, T=118.7%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 3F/17P
- HIGH_TURNOVER: 19F/1P
- LOW_FITNESS: 20F/0P
- LOW_SHARPE: 19F/1P
- LOW_SUB_UNIVERSE_SHARPE: 8F/10P

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
Best negated: `rank(-1 * ts_delta(news_mins_1_chg, 5))` S=1.10, F=0.23, INFERIOR
Direction gap: -0.43 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * news_mins_1_chg)`: S=-0.09, F=-0.01, T=125.2%, INFERIOR (TOP3000)
- `rank(-1 * news_mins_1_chg / close)`: S=0.03, F=0.00, T=118.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(news_mins_1_chg, 5))`: S=1.10, F=0.23, T=149.5%, INFERIOR (TOP3000)

## Variation Breakdown
No per-variation PnL data available for this field.

## Correlation Notes
No correlation data available for this field.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_FITNESS. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, rank_value_norm, trade_when
