---
field: news_indx_perf
dataset: news12
best_template: neg_rank
best_sharpe: 1.37
best_fitness: 0.41
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_FITNESS
n_sims: 23
negated_best_sharpe: 1.37
negated_best_template: neg_rank
negated_best_fitness: 0.41
n_negated_sims: 4
direction_gap: 0.22
---
# news_indx_perf (news12)

*Difference in percent return between the stock and the S&P 500 ETF over the session: ((EODClose - TONLast) / TONLast) - ((SPYClose - SPYLast) / SPYLast)*

## Signal Profile
- `rank(news_indx_perf)`: S=-0.39, F=-0.05, T=120.1%, INFERIOR (TOP3000)
- `rank(news_indx_perf / close)`: S=-1.37, F=-0.41, T=110.6%, INFERIOR (TOP3000)
- `rank(ts_delta(news_indx_perf, 5))`: S=-0.59, F=-0.15, T=111.1%, INFERIOR (TOP200)
- `-rank(news_indx_perf)`: S=1.37, F=0.41, T=109.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(news_indx_perf, 5))`: S=1.13, F=0.27, T=140.7%, INFERIOR (TOP3000)
- `-ts_zscore(news_indx_perf, 63)`: S=1.15, F=0.32, T=105.5%, INFERIOR (TOP3000)
- `ts_mean(news_indx_perf, 10)`: S=-0.60, F=-0.29, T=25.5%, INFERIOR (TOP3000)
- `rank(ts_rank(news_indx_perf, 22))`: S=-1.40, F=-0.38, T=110.2%, INFERIOR (TOP3000)
- `rank(-1 * news_indx_perf)`: S=0.39, F=0.05, T=120.1%, INFERIOR (TOP3000)
- `rank(-1 * news_indx_perf / close)`: S=0.34, F=0.04, T=121.7%, INFERIOR (TOP3000)

## Check Summary
- HIGH_TURNOVER: 22F/1P
- LOW_FITNESS: 23F/0P
- LOW_SHARPE: 22F/1P
- LOW_SUB_UNIVERSE_SHARPE: 15F/6P

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
Best negated: `-rank(news_indx_perf)` S=1.37, F=0.41, INFERIOR
Direction gap: +0.22 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * news_indx_perf)`: S=0.39, F=0.05, T=120.1%, INFERIOR (TOP3000)
- `rank(-1 * news_indx_perf / close)`: S=0.34, F=0.04, T=121.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(news_indx_perf, 5))`: S=1.13, F=0.27, T=140.7%, INFERIOR (TOP3000)

## Variation Breakdown
No per-variation PnL data available for this field.

## Correlation Notes
No correlation data available for this field.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_FITNESS. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
