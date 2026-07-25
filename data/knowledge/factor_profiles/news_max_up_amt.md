---
field: news_max_up_amt
dataset: news12
best_template: rank_neg_delta
best_sharpe: 1.51
best_fitness: 0.37
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_FITNESS
n_sims: 21
negated_best_sharpe: 1.51
negated_best_template: rank_neg_delta
negated_best_fitness: 0.37
n_negated_sims: 4
direction_gap: 0.51
---
# news_max_up_amt (news12)

*After-news high minus the price at the time of the news*

## Signal Profile
- `rank(news_max_up_amt)`: S=-0.34, F=-0.05, T=109.0%, INFERIOR (TOP3000)
- `rank(news_max_up_amt / close)`: S=-0.64, F=-0.17, T=108.9%, INFERIOR (TOP3000)
- `rank(ts_delta(news_max_up_amt, 5))`: S=-0.89, F=-0.19, T=123.8%, INFERIOR (TOP500)
- `-rank(news_max_up_amt)`: S=0.58, F=0.13, T=93.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(news_max_up_amt, 5))`: S=1.51, F=0.37, T=143.4%, INFERIOR (TOP3000)
- `-ts_zscore(news_max_up_amt, 63)`: S=1.00, F=0.25, T=110.2%, INFERIOR (TOP3000)
- `ts_mean(news_max_up_amt, 10)`: S=-0.17, F=-0.06, T=11.5%, INFERIOR (TOP3000)
- `rank(ts_rank(news_max_up_amt, 22))`: S=-1.34, F=-0.33, T=116.7%, INFERIOR (TOP3000)
- `rank(-1 * news_max_up_amt)`: S=0.34, F=0.05, T=109.0%, INFERIOR (TOP3000)
- `rank(-1 * news_max_up_amt / close)`: S=0.58, F=0.13, T=122.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 1F/20P
- HIGH_TURNOVER: 19F/2P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 20F/1P
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
Best negated: `rank(-1 * ts_delta(news_max_up_amt, 5))` S=1.51, F=0.37, INFERIOR
Direction gap: +0.51 (negated - positive best Sharpe). NEGATION DOMINANT — field is significantly stronger when reversed.

Negated template variants:
- `rank(-1 * news_max_up_amt)`: S=0.34, F=0.05, T=109.0%, INFERIOR (TOP3000)
- `rank(-1 * news_max_up_amt / close)`: S=0.58, F=0.13, T=122.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(news_max_up_amt, 5))`: S=1.51, F=0.37, T=143.4%, INFERIOR (TOP3000)

## Variation Breakdown
No per-variation PnL data available for this field.

## Correlation Notes
No correlation data available for this field.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_FITNESS. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
