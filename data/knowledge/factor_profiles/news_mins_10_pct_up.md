---
field: news_mins_10_pct_up
dataset: news12
best_template: ts_zscore
best_sharpe: 0.57
best_fitness: 0.44
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 20
regime_profile: all-weather
n_variations_with_pnl: 3
max_drawdown: 0.5392
ann_vol: 0.313
hit_rate: 0.1571
rolling_sharpe_min: -0.774
rolling_sharpe_max: 2.089
negated_best_sharpe: 0.42
negated_best_template: neg_rank
negated_best_fitness: 0.22
n_negated_sims: 4
direction_gap: -0.15
---
# news_mins_10_pct_up (news12)

*Number of minutes before the price increased by at least 10 percent after the news release*

## Signal Profile
- `rank(news_mins_10_pct_up)`: S=0.50, F=0.34, T=33.5%, INFERIOR (TOP200)
- `rank(ts_delta(news_mins_10_pct_up, 5))`: S=0.38, F=0.27, T=4.2%, INFERIOR (TOP200)
- `-rank(news_mins_10_pct_up)`: S=0.42, F=0.22, T=103.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(news_mins_10_pct_up, 5))`: S=0.00, F=0.00, T=38.9%, INFERIOR (TOP3000)
- `ts_zscore(news_mins_10_pct_up, 22)`: S=0.57, F=0.44, T=64.0%, INFERIOR (TOP3000)
- `ts_mean(news_mins_10_pct_up, 10)`: S=0.33, F=0.16, T=44.9%, INFERIOR (TOP3000)
- `rank(ts_rank(news_mins_10_pct_up, 22))`: S=-0.13, F=-0.04, T=92.9%, INFERIOR (TOP3000)
- `rank(-1 * news_mins_10_pct_up)`: S=-0.12, F=-0.03, T=164.2%, INFERIOR (TOP3000)
- `rank(-1 * news_mins_10_pct_up / close)`: S=-0.30, F=-0.10, T=163.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 20F/0P
- HIGH_TURNOVER: 9F/11P
- LOW_FITNESS: 20F/0P
- LOW_SHARPE: 20F/0P
- LOW_SUB_UNIVERSE_SHARPE: 12F/6P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.50, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.22 (weak), ret=+1.8%
  - 2020: S=0.57 (moderate), ret=+25.0%
  - 2021: S=1.55 (strong), ret=+64.4%
  - 2022: S=-0.45 (negative), ret=-12.0%
  - 2023: S=-0.21 (negative), ret=-2.9%

## Risk & Drawdown
- Max drawdown: 53.92% over 766 days (not yet recovered, ongoing at window end)
- Annualized: return +15.6%, volatility 31.3% (fraction of booksize)
- Hit rate: 15.7% positive days
- Tail shape: skew +0.29, excess kurtosis +21.00

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.77, max 2.09, latest -0.21

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2022
Best month: +25.53%; worst month: -40.01%
Positive months: 58%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=0.56
- Sideways: S=0.06
- Bear: S=0.79

## Negated Direction
Best negated: `-rank(news_mins_10_pct_up)` S=0.42, F=0.22, INFERIOR
Direction gap: -0.15 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * news_mins_10_pct_up)`: S=-0.12, F=-0.03, T=164.2%, INFERIOR (TOP3000)
- `rank(-1 * news_mins_10_pct_up / close)`: S=-0.30, F=-0.10, T=163.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(news_mins_10_pct_up, 5))`: S=0.00, F=0.00, T=38.9%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(news_mins_10_pct_up)` | TOP200 | 0.50 | 0.34 | 53.9% | 60% | all-weather |
| `rank(ts_delta(news_mins_10_pct_up, 5))` | TOP200 | 0.26 | 0.27 | 17.8% | 40% | bear-only |
| `rank(news_mins_10_pct_up)` | TOP3000 | 0.13 | 0.03 | 156.0% | 40% | all-weather |

## Correlation Notes
Top correlates:
- news_mins_20_pct_up: 0.118 (weakly positively correlated)
- news_mins_20_chg: 0.118 (weakly positively correlated)
- fnd6_optfvgr: 0.118 (weakly positively correlated)
- fnd6_newqv1300_ciotherq: 0.099 (weakly positively correlated)
- fnd6_cptnewqv1300_req: 0.093 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, rank_value_norm, trade_when
