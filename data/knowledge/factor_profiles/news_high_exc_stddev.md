---
field: news_high_exc_stddev
dataset: news12
best_template: rank_neg_delta
best_sharpe: 1.43
best_fitness: 0.34
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_FITNESS
n_sims: 21
negated_best_sharpe: 1.43
negated_best_template: rank_neg_delta
negated_best_fitness: 0.34
n_negated_sims: 4
direction_gap: 0.34
---
# news_high_exc_stddev (news12)

*Standardized measure of price movement from end-of-day high to last price in the time-of-news window, divided by 30-day closing price standard deviation*

## Signal Profile
- `rank(news_high_exc_stddev)`: S=-0.69, F=-0.20, T=82.3%, INFERIOR (TOP200)
- `rank(news_high_exc_stddev / close)`: S=-0.38, F=-0.08, T=91.2%, INFERIOR (TOP3000)
- `rank(ts_delta(news_high_exc_stddev, 5))`: S=-0.39, F=-0.06, T=120.8%, INFERIOR (TOP500)
- `-rank(news_high_exc_stddev)`: S=1.25, F=0.33, T=108.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(news_high_exc_stddev, 5))`: S=1.43, F=0.34, T=143.3%, INFERIOR (TOP3000)
- `-ts_zscore(news_high_exc_stddev, 63)`: S=1.09, F=0.27, T=105.0%, INFERIOR (TOP3000)
- `ts_mean(news_high_exc_stddev, 10)`: S=-0.40, F=-0.14, T=22.6%, INFERIOR (TOP3000)
- `rank(ts_rank(news_high_exc_stddev, 22))`: S=-1.07, F=-0.24, T=110.7%, INFERIOR (TOP3000)
- `rank(-1 * news_high_exc_stddev)`: S=1.15, F=0.25, T=123.2%, INFERIOR (TOP3000)
- `rank(-1 * news_high_exc_stddev / close)`: S=0.40, F=0.08, T=106.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 20F/1P
- HIGH_TURNOVER: 20F/1P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 19F/2P
- LOW_SUB_UNIVERSE_SHARPE: 9F/10P

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
Best negated: `rank(-1 * ts_delta(news_high_exc_stddev, 5))` S=1.43, F=0.34, INFERIOR
Direction gap: +0.34 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * news_high_exc_stddev)`: S=1.15, F=0.25, T=123.2%, INFERIOR (TOP3000)
- `rank(-1 * news_high_exc_stddev / close)`: S=0.40, F=0.08, T=106.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(news_high_exc_stddev, 5))`: S=1.43, F=0.34, T=143.3%, INFERIOR (TOP3000)

## Variation Breakdown
No per-variation PnL data available for this field.

## Correlation Notes
No correlation data available for this field.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_FITNESS. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
