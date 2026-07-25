---
field: news_prev_day_ret
dataset: news12
best_template: neg_rank
best_sharpe: 1.53
best_fitness: 0.56
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_FITNESS
n_sims: 21
negated_best_sharpe: 1.53
negated_best_template: neg_rank
negated_best_fitness: 0.56
n_negated_sims: 4
direction_gap: 0.26
---
# news_prev_day_ret (news12)

*Percent change between previous day's open and close price*

## Signal Profile
- `rank(news_prev_day_ret)`: S=-0.68, F=-0.21, T=83.8%, INFERIOR (TOP200)
- `rank(news_prev_day_ret / close)`: S=-1.42, F=-0.50, T=96.8%, INFERIOR (TOP3000)
- `rank(ts_delta(news_prev_day_ret, 5))`: S=-0.67, F=-0.18, T=101.5%, INFERIOR (TOP200)
- `-rank(news_prev_day_ret)`: S=1.53, F=0.56, T=96.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(news_prev_day_ret, 5))`: S=0.93, F=0.22, T=127.2%, INFERIOR (TOP3000)
- `-ts_zscore(news_prev_day_ret, 63)`: S=1.27, F=0.39, T=96.2%, INFERIOR (TOP3000)
- `ts_mean(news_prev_day_ret, 10)`: S=-0.88, F=-0.56, T=25.2%, INFERIOR (TOP3000)
- `rank(ts_rank(news_prev_day_ret, 22))`: S=-1.17, F=-0.31, T=98.1%, INFERIOR (TOP3000)
- `rank(-1 * news_prev_day_ret)`: S=1.55, F=0.53, T=102.7%, INFERIOR (TOP3000)
- `rank(-1 * news_prev_day_ret / close)`: S=1.52, F=0.52, T=102.8%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 21F/0P
- HIGH_TURNOVER: 20F/1P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 17F/4P
- LOW_SUB_UNIVERSE_SHARPE: 14F/5P

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
Best negated: `-rank(news_prev_day_ret)` S=1.53, F=0.56, INFERIOR
Direction gap: +0.26 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * news_prev_day_ret)`: S=1.55, F=0.53, T=102.7%, INFERIOR (TOP3000)
- `rank(-1 * news_prev_day_ret / close)`: S=1.52, F=0.52, T=102.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(news_prev_day_ret, 5))`: S=0.93, F=0.22, T=127.2%, INFERIOR (TOP3000)

## Variation Breakdown
No per-variation PnL data available for this field.

## Correlation Notes
No correlation data available for this field.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_FITNESS. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
