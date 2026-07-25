---
field: news_mins_10_chg
dataset: news12
best_template: ts_zscore
best_sharpe: 1.39
best_fitness: 1.34
best_universe: TOP3000
grade: AVERAGE
submittability: blocked_HIGH_TURNOVER
n_sims: 21
regime_profile: mixed
n_variations_with_pnl: 6
max_drawdown: 0.8658
ann_vol: 0.4451
hit_rate: 0.115
rolling_sharpe_min: -1.558
rolling_sharpe_max: 2.861
negated_best_sharpe: 0.29
negated_best_template: rank_neg_delta
negated_best_fitness: 0.16
n_negated_sims: 4
direction_gap: -1.1
---
# news_mins_10_chg (news12)

*Minimum value among L or S for each minute bucket, indicating the fastest reaction time at the 10th percentile*

## Signal Profile
- `rank(news_mins_10_chg)`: S=0.75, F=0.32, T=164.0%, INFERIOR (TOP3000)
- `rank(news_mins_10_chg / close)`: S=0.65, F=0.35, T=134.8%, INFERIOR (TOP3000)
- `rank(ts_delta(news_mins_10_chg, 5))`: S=0.63, F=0.66, T=26.2%, INFERIOR (TOP1000)
- `-rank(news_mins_10_chg)`: S=-0.53, F=-0.25, T=136.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(news_mins_10_chg, 5))`: S=0.29, F=0.16, T=86.0%, INFERIOR (TOP3000)
- `ts_zscore(news_mins_10_chg, 22)`: S=1.39, F=1.34, T=103.8%, AVERAGE (TOP3000)
- `ts_mean(news_mins_10_chg, 10)`: S=0.54, F=0.29, T=41.6%, INFERIOR (TOP3000)
- `rank(ts_rank(news_mins_10_chg, 22))`: S=0.06, F=0.01, T=128.3%, INFERIOR (TOP3000)
- `rank(-1 * news_mins_10_chg)`: S=-0.75, F=-0.32, T=164.0%, INFERIOR (TOP3000)
- `rank(-1 * news_mins_10_chg / close)`: S=-0.02, F=0.00, T=161.5%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 21F/0P
- HIGH_TURNOVER: 14F/7P
- LOW_FITNESS: 20F/1P
- LOW_SHARPE: 20F/1P
- LOW_SUB_UNIVERSE_SHARPE: 9F/10P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.62, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=1.19 (moderate), ret=+7.2%
  - 2020: S=1.98 (strong), ret=+107.2%
  - 2021: S=1.04 (moderate), ret=+45.8%
  - 2022: S=-0.26 (negative), ret=-10.3%
  - 2023: S=-0.27 (negative), ret=-14.4%

## Risk & Drawdown
- Max drawdown: 86.58% over 954 days (not yet recovered, ongoing at window end)
- Annualized: return +27.6%, volatility 44.5% (fraction of booksize)
- Hit rate: 11.5% positive days
- Tail shape: skew -0.18, excess kurtosis +42.74

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.56, max 2.86, latest -0.27

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2023
Best month: +69.47%; worst month: -31.14%
Positive months: 60%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.16
- Sideways: S=-0.14
- Bear: S=1.81

## Negated Direction
Best negated: `rank(-1 * ts_delta(news_mins_10_chg, 5))` S=0.29, F=0.16, INFERIOR
Direction gap: -1.10 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * news_mins_10_chg)`: S=-0.75, F=-0.32, T=164.0%, INFERIOR (TOP3000)
- `rank(-1 * news_mins_10_chg / close)`: S=-0.02, F=0.00, T=161.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(news_mins_10_chg, 5))`: S=0.29, F=0.16, T=86.0%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(news_mins_10_chg, 5))` | TOP1000 | 0.62 | 0.66 | 86.6% | 60% | mixed |
| `rank(news_mins_10_chg)` | TOP3000 | 0.78 | 0.32 | 68.2% | 60% | all-weather |
| `rank(news_mins_10_chg)` | TOP1000 | 0.54 | 0.25 | 113.9% | 80% | all-weather |
| `rank(ts_delta(news_mins_10_chg, 5))` | TOP500 | 0.24 | 0.23 | 71.0% | 40% | mixed |
| `rank(ts_delta(news_mins_10_chg, 5))` | TOP200 | 0.22 | 0.19 | 22.9% | 20% | bear-only |
| `rank(news_mins_10_chg)` | TOP500 | 0.33 | 0.14 | 81.3% | 80% | mixed |

## Correlation Notes
Top correlates:
- fnd6_donr: -0.139 (weakly negatively correlated)
- news_mins_20_pct_dn: 0.126 (weakly positively correlated)
- news_mins_3_pct_up: 0.111 (weakly positively correlated)
- historical_volatility_90: -0.111 (weakly negatively correlated)
- rp_nip_credit: -0.109 (weakly negatively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by HIGH_TURNOVER. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
