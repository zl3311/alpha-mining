---
field: news_mins_4_pct_up
dataset: news12
best_template: rank_delta
best_sharpe: 0.61
best_fitness: 0.36
best_universe: TOP200
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 20
regime_profile: mixed
n_variations_with_pnl: 4
max_drawdown: 0.6225
ann_vol: 0.4075
hit_rate: 0.2996
rolling_sharpe_min: -0.771
rolling_sharpe_max: 2.315
negated_best_sharpe: -0.06
negated_best_template: rank_neg_delta
negated_best_fitness: -0.01
n_negated_sims: 4
direction_gap: -0.67
---
# news_mins_4_pct_up (news12)

*Number of minutes before the price increased by at least 4 percent after the news release*

## Signal Profile
- `rank(news_mins_4_pct_up)`: S=0.41, F=0.08, T=156.3%, INFERIOR (TOP3000)
- `rank(ts_delta(news_mins_4_pct_up, 5))`: S=0.61, F=0.36, T=74.2%, INFERIOR (TOP200)
- `-rank(news_mins_4_pct_up)`: S=-0.34, F=-0.08, T=161.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(news_mins_4_pct_up, 5))`: S=-0.06, F=-0.01, T=172.7%, INFERIOR (TOP3000)
- `-ts_zscore(news_mins_4_pct_up, 63)`: S=0.05, F=0.00, T=163.6%, INFERIOR (TOP3000)
- `ts_mean(news_mins_4_pct_up, 10)`: S=-0.30, F=-0.08, T=34.5%, INFERIOR (TOP3000)
- `rank(ts_rank(news_mins_4_pct_up, 22))`: S=-0.10, F=-0.01, T=163.7%, INFERIOR (TOP3000)
- `rank(-1 * news_mins_4_pct_up)`: S=-0.41, F=-0.08, T=156.3%, INFERIOR (TOP3000)
- `rank(-1 * news_mins_4_pct_up / close)`: S=-0.39, F=-0.08, T=151.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 19F/1P
- HIGH_TURNOVER: 19F/1P
- LOW_FITNESS: 20F/0P
- LOW_SHARPE: 20F/0P
- LOW_SUB_UNIVERSE_SHARPE: 4F/14P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.61, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.97 (moderate), ret=+2.9%
  - 2020: S=0.98 (moderate), ret=+54.4%
  - 2021: S=1.13 (moderate), ret=+55.6%
  - 2022: S=0.66 (moderate), ret=+24.6%
  - 2023: S=-0.50 (negative), ret=-15.5%

## Risk & Drawdown
- Max drawdown: 62.25% over 178 days (recovered)
- Annualized: return +24.9%, volatility 40.8% (fraction of booksize)
- Hit rate: 30.0% positive days
- Tail shape: skew -0.43, excess kurtosis +21.86

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.77, max 2.31, latest -0.63

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2023
Best month: +19.97%; worst month: -37.02%
Positive months: 62%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.49
- Sideways: S=0.20
- Bear: S=1.02

## Negated Direction
Best negated: `rank(-1 * ts_delta(news_mins_4_pct_up, 5))` S=-0.06, F=-0.01, INFERIOR
Direction gap: -0.67 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * news_mins_4_pct_up)`: S=-0.41, F=-0.08, T=156.3%, INFERIOR (TOP3000)
- `rank(-1 * news_mins_4_pct_up / close)`: S=-0.39, F=-0.08, T=151.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(news_mins_4_pct_up, 5))`: S=-0.06, F=-0.01, T=172.7%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(news_mins_4_pct_up, 5))` | TOP200 | 0.61 | 0.36 | 62.3% | 80% | mixed |
| `rank(news_mins_4_pct_up)` | TOP1000 | 0.37 | 0.08 | 36.0% | 60% | mixed |
| `rank(news_mins_4_pct_up)` | TOP3000 | 0.45 | 0.08 | 27.7% | 60% | mixed |
| `rank(ts_delta(news_mins_4_pct_up, 5))` | TOP500 | 0.12 | 0.03 | 92.1% | 40% | weak |

## Correlation Notes
Top correlates:
- news_mins_3_pct_up: 0.165 (weakly positively correlated)
- unsystematic_risk_last_90_days: -0.103 (weakly negatively correlated)
- fnd6_newqv1300_aociderglq: -0.101 (weakly negatively correlated)
- fnd6_newa1v1300_aol2: -0.096 (weakly negatively correlated)
- fn_assets_fair_val_l2_a: -0.095 (weakly negatively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, rank_value_norm, trade_when
