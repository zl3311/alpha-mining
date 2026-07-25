---
field: news_ls
dataset: news12
best_template: neg_rank
best_sharpe: 1.61
best_fitness: 0.39
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_FITNESS
n_sims: 21
negated_best_sharpe: 1.61
negated_best_template: neg_rank
negated_best_fitness: 0.39
n_negated_sims: 4
direction_gap: 0.02
---
# news_ls (news12)

*Indicates if a long or short position would have been more advantageous, based on comparison of (EODHigh - Last) and (Last - EODLow)*

## Signal Profile
- `rank(news_ls)`: S=-0.22, F=-0.02, T=127.8%, INFERIOR (TOP3000)
- `rank(news_ls / close)`: S=-1.42, F=-0.37, T=114.7%, INFERIOR (TOP3000)
- `rank(ts_delta(news_ls, 5))`: S=-0.83, F=-0.15, T=144.4%, INFERIOR (TOP3000)
- `-rank(news_ls)`: S=1.61, F=0.39, T=115.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(news_ls, 5))`: S=0.83, F=0.15, T=144.4%, INFERIOR (TOP3000)
- `-ts_zscore(news_ls, 63)`: S=1.59, F=0.39, T=113.8%, INFERIOR (TOP3000)
- `ts_mean(news_ls, 10)`: S=-0.54, F=-0.15, T=25.2%, INFERIOR (TOP3000)
- `rank(ts_rank(news_ls, 22))`: S=-1.38, F=-0.31, T=114.4%, INFERIOR (TOP3000)
- `rank(-1 * news_ls)`: S=0.22, F=0.02, T=127.8%, INFERIOR (TOP3000)
- `rank(-1 * news_ls / close)`: S=-0.08, F=0.00, T=128.1%, INFERIOR (TOP3000)

## Check Summary
- HIGH_TURNOVER: 20F/1P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 19F/2P
- LOW_SUB_UNIVERSE_SHARPE: 12F/7P

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
Best negated: `-rank(news_ls)` S=1.61, F=0.39, INFERIOR
Direction gap: +0.02 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * news_ls)`: S=0.22, F=0.02, T=127.8%, INFERIOR (TOP3000)
- `rank(-1 * news_ls / close)`: S=-0.08, F=0.00, T=128.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(news_ls, 5))`: S=0.83, F=0.15, T=144.4%, INFERIOR (TOP3000)

## Variation Breakdown
No per-variation PnL data available for this field.

## Correlation Notes
No correlation data available for this field.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_FITNESS. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
