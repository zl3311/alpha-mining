---
field: news_pct_1min
dataset: news12
best_template: ts_zscore
best_sharpe: 0.67
best_fitness: 0.13
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 21
regime_profile: mixed
n_variations_with_pnl: 3
max_drawdown: 0.3866
ann_vol: 0.1261
hit_rate: 0.5101
rolling_sharpe_min: -2.862
rolling_sharpe_max: 3.188
negated_best_sharpe: 0.52
negated_best_template: neg_rank_level
negated_best_fitness: 0.09
n_negated_sims: 4
direction_gap: -0.15
---
# news_pct_1min (news12)

*Percent change in price during the first minute following the news release*

## Signal Profile
- `rank(news_pct_1min)`: S=0.10, F=0.01, T=109.5%, INFERIOR (TOP200)
- `rank(news_pct_1min / close)`: S=-0.38, F=-0.06, T=129.8%, INFERIOR (TOP3000)
- `rank(ts_delta(news_pct_1min, 5))`: S=0.50, F=0.10, T=150.9%, INFERIOR (TOP3000)
- `-rank(news_pct_1min)`: S=0.48, F=0.08, T=128.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(news_pct_1min, 5))`: S=-0.50, F=-0.10, T=150.9%, INFERIOR (TOP3000)
- `-ts_zscore(news_pct_1min, 63)`: S=0.67, F=0.13, T=124.5%, INFERIOR (TOP3000)
- `ts_mean(news_pct_1min, 10)`: S=-0.39, F=-0.12, T=28.3%, INFERIOR (TOP3000)
- `rank(ts_rank(news_pct_1min, 22))`: S=-0.29, F=-0.03, T=133.3%, INFERIOR (TOP3000)
- `rank(-1 * news_pct_1min)`: S=0.52, F=0.09, T=136.2%, INFERIOR (TOP3000)
- `rank(-1 * news_pct_1min / close)`: S=0.38, F=0.06, T=138.4%, INFERIOR (TOP3000)

## Check Summary
- HIGH_TURNOVER: 20F/1P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 21F/0P
- LOW_SUB_UNIVERSE_SHARPE: 8F/11P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.51, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=2.20 (strong), ret=+28.3%
  - 2020: S=-0.32 (negative), ret=-4.6%
  - 2021: S=-2.01 (negative), ret=-23.7%
  - 2022: S=1.36 (moderate), ret=+16.2%
  - 2023: S=1.44 (moderate), ret=+14.9%

## Risk & Drawdown
- Max drawdown: 38.66% over 1071 days (recovered)
- Annualized: return +6.4%, volatility 12.6% (fraction of booksize)
- Hit rate: 51.0% positive days
- Tail shape: skew +0.08, excess kurtosis +2.87

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.86, max 3.19, latest 1.48

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2021
Best month: +8.22%; worst month: -7.96%
Positive months: 56%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.51
- Sideways: S=1.56
- Bear: S=-0.45

## Negated Direction
Best negated: `rank(-1 * news_pct_1min)` S=0.52, F=0.09, INFERIOR
Direction gap: -0.15 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * news_pct_1min)`: S=0.52, F=0.09, T=136.2%, INFERIOR (TOP3000)
- `rank(-1 * news_pct_1min / close)`: S=0.38, F=0.06, T=138.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(news_pct_1min, 5))`: S=-0.50, F=-0.10, T=150.9%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(news_pct_1min, 5))` | TOP3000 | 0.51 | 0.10 | 38.7% | 60% | mixed |
| `rank(ts_delta(news_pct_1min, 5))` | TOP500 | 0.22 | 0.03 | 38.3% | 40% | weak |
| `rank(ts_delta(news_pct_1min, 5))` | TOP200 | 0.18 | 0.02 | 33.4% | 60% | weak |

## Correlation Notes
Top correlates:
- news_pct_30sec: 0.420 (moderately positively correlated)
- implied_volatility_put_360: -0.103 (weakly negatively correlated)
- implied_volatility_put_180: -0.100 (weakly negatively correlated)
- implied_volatility_put_270: -0.099 (weakly negatively correlated)
- implied_volatility_put_720: -0.097 (weakly negatively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
