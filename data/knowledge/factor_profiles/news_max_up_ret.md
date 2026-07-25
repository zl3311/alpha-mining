---
field: news_max_up_ret
dataset: news12
best_template: rank_neg_delta
best_sharpe: 1.06
best_fitness: 0.24
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 23
negated_best_sharpe: 1.06
negated_best_template: rank_neg_delta
negated_best_fitness: 0.24
n_negated_sims: 4
direction_gap: 0.35
---
# news_max_up_ret (news12)

*Percent change from price at time of news to highest price after news*

## Signal Profile
- `rank(news_max_up_ret)`: S=-0.14, F=-0.02, T=86.4%, INFERIOR (TOP200)
- `rank(news_max_up_ret / close)`: S=-0.22, F=-0.04, T=88.8%, INFERIOR (TOP3000)
- `rank(ts_delta(news_max_up_ret, 5))`: S=-0.56, F=-0.11, T=124.2%, INFERIOR (TOP500)
- `-rank(news_max_up_ret)`: S=0.65, F=0.17, T=109.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(news_max_up_ret, 5))`: S=1.06, F=0.24, T=146.0%, INFERIOR (TOP3000)
- `-ts_zscore(news_max_up_ret, 63)`: S=0.71, F=0.14, T=110.9%, INFERIOR (TOP3000)
- `ts_mean(news_max_up_ret, 10)`: S=-0.58, F=-0.42, T=21.0%, INFERIOR (TOP3000)
- `rank(ts_rank(news_max_up_ret, 22))`: S=-1.04, F=-0.22, T=116.9%, INFERIOR (TOP3000)
- `rank(-1 * news_max_up_ret)`: S=0.60, F=0.14, T=122.2%, INFERIOR (TOP3000)
- `rank(-1 * news_max_up_ret / close)`: S=0.26, F=0.05, T=103.1%, INFERIOR (TOP3000)

## Check Summary
- HIGH_TURNOVER: 22F/1P
- LOW_FITNESS: 23F/0P
- LOW_SHARPE: 23F/0P
- LOW_SUB_UNIVERSE_SHARPE: 8F/13P

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
Best negated: `rank(-1 * ts_delta(news_max_up_ret, 5))` S=1.06, F=0.24, INFERIOR
Direction gap: +0.35 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * news_max_up_ret)`: S=0.60, F=0.14, T=122.2%, INFERIOR (TOP3000)
- `rank(-1 * news_max_up_ret / close)`: S=0.26, F=0.05, T=103.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(news_max_up_ret, 5))`: S=1.06, F=0.24, T=146.0%, INFERIOR (TOP3000)

## Variation Breakdown
No per-variation PnL data available for this field.

## Correlation Notes
No correlation data available for this field.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
