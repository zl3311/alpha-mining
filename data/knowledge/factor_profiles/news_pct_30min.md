---
field: news_pct_30min
dataset: news12
best_template: rank_level
best_sharpe: 0.52
best_fitness: 0.11
best_universe: TOP200
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 21
regime_profile: mixed
n_variations_with_pnl: 1
max_drawdown: 0.1638
ann_vol: 0.0935
hit_rate: 0.4988
rolling_sharpe_min: -1.286
rolling_sharpe_max: 2.463
negated_best_sharpe: 0.54
negated_best_template: neg_rank
negated_best_fitness: 0.09
n_negated_sims: 4
direction_gap: 0.02
---
# news_pct_30min (news12)

*Percent change in price during the first 30 minutes following the news release*

## Signal Profile
- `rank(news_pct_30min)`: S=0.52, F=0.11, T=98.9%, INFERIOR (TOP200)
- `rank(news_pct_30min / close)`: S=-0.49, F=-0.08, T=116.7%, INFERIOR (TOP3000)
- `rank(ts_delta(news_pct_30min, 5))`: S=-0.28, F=-0.04, T=145.5%, INFERIOR (TOP3000)
- `-rank(news_pct_30min)`: S=0.54, F=0.09, T=116.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(news_pct_30min, 5))`: S=0.28, F=0.04, T=145.5%, INFERIOR (TOP3000)
- `-ts_zscore(news_pct_30min, 63)`: S=0.37, F=0.05, T=113.0%, INFERIOR (TOP3000)
- `ts_mean(news_pct_30min, 10)`: S=-0.32, F=-0.09, T=26.5%, INFERIOR (TOP3000)
- `rank(ts_rank(news_pct_30min, 22))`: S=-0.48, F=-0.07, T=118.2%, INFERIOR (TOP3000)
- `rank(-1 * news_pct_30min)`: S=-0.15, F=-0.01, T=125.0%, INFERIOR (TOP3000)
- `rank(-1 * news_pct_30min / close)`: S=-0.11, F=-0.01, T=126.1%, INFERIOR (TOP3000)

## Check Summary
- HIGH_TURNOVER: 20F/1P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 21F/0P
- LOW_SUB_UNIVERSE_SHARPE: 12F/7P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.52, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.98 (moderate), ret=+7.3%
  - 2020: S=0.76 (moderate), ret=+7.7%
  - 2021: S=0.03 (weak), ret=+0.4%
  - 2022: S=1.96 (strong), ret=+16.6%
  - 2023: S=-1.33 (negative), ret=-8.2%

## Risk & Drawdown
- Max drawdown: 16.38% over 229 days (recovered)
- Annualized: return +4.9%, volatility 9.3% (fraction of booksize)
- Hit rate: 49.9% positive days
- Tail shape: skew +0.17, excess kurtosis +3.58

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.29, max 2.46, latest -1.29

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2023
Best month: +7.90%; worst month: -7.05%
Positive months: 54%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.16
- Sideways: S=0.11
- Bear: S=1.24

## Negated Direction
Best negated: `-rank(news_pct_30min)` S=0.54, F=0.09, INFERIOR
Direction gap: +0.02 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * news_pct_30min)`: S=-0.15, F=-0.01, T=125.0%, INFERIOR (TOP3000)
- `rank(-1 * news_pct_30min / close)`: S=-0.11, F=-0.01, T=126.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(news_pct_30min, 5))`: S=0.28, F=0.04, T=145.5%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(news_pct_30min)` | TOP200 | 0.52 | 0.11 | 16.4% | 80% | mixed |

## Correlation Notes
Top correlates:
- news_pct_10min: 0.588 (moderately positively correlated)
- news_pct_5_min: 0.484 (moderately positively correlated)
- fnd6_prcl: -0.225 (weakly negatively correlated)
- fnd6_prcc: -0.211 (weakly negatively correlated)
- fnd6_prclq: -0.193 (weakly negatively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
