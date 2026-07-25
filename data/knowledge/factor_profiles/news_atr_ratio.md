---
field: news_atr_ratio
dataset: news12
cluster: news12_ratio
coverage: 0.7967
community_alphas: 2304
best_template: rank_delta
best_sharpe: 0.66
best_fitness: 0.16
best_universe: TOP200
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 21
regime_profile: bull-only
n_variations_with_pnl: 2
max_drawdown: 0.0859
ann_vol: 0.0911
hit_rate: 0.5206
rolling_sharpe_min: -0.51
rolling_sharpe_max: 2.734
redundancy_cluster: 62
negated_best_sharpe: 0.73
negated_best_template: neg_rank_level
negated_best_fitness: 0.13
n_negated_sims: 4
direction_gap: 0.07
---
# news_atr_ratio (news12)

*Ratio of current day's price range to 20-day average true range*

## Signal Profile
- `rank(news_atr_ratio)`: S=0.13, F=0.01, T=91.0%, INFERIOR (TOP500)
- `rank(news_atr_ratio / close)`: S=0.02, F=0.00, T=76.8%, INFERIOR (TOP3000)
- `rank(ts_delta(news_atr_ratio, 5))`: S=0.66, F=0.16, T=101.5%, INFERIOR (TOP200)
- `-rank(news_atr_ratio)`: S=0.10, F=0.01, T=99.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(news_atr_ratio, 5))`: S=0.53, F=0.08, T=135.3%, INFERIOR (TOP3000)
- `-ts_zscore(news_atr_ratio, 63)`: S=-0.15, F=-0.01, T=101.1%, INFERIOR (TOP3000)
- `ts_mean(news_atr_ratio, 10)`: S=-0.01, F=0.00, T=22.4%, INFERIOR (TOP3000)
- `rank(ts_rank(news_atr_ratio, 22))`: S=-0.01, F=0.00, T=107.6%, INFERIOR (TOP3000)
- `rank(-1 * news_atr_ratio)`: S=0.73, F=0.13, T=113.2%, INFERIOR (TOP3000)
- `rank(-1 * news_atr_ratio / close)`: S=0.37, F=0.08, T=92.0%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 20F/1P
- HIGH_TURNOVER: 20F/1P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 21F/0P
- LOW_SUB_UNIVERSE_SHARPE: 5F/14P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.67, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.37 (weak), ret=+2.4%
  - 2020: S=-0.04 (negative), ret=-0.4%
  - 2021: S=0.17 (weak), ret=+1.8%
  - 2022: S=1.50 (strong), ret=+16.0%
  - 2023: S=1.62 (strong), ret=+10.1%

## Risk & Drawdown
- Max drawdown: 8.59% over 433 days (recovered)
- Annualized: return +6.1%, volatility 9.1% (fraction of booksize)
- Hit rate: 52.1% positive days
- Tail shape: skew +0.23, excess kurtosis +3.74

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.51, max 2.73, latest 1.58

## Yearly & Monthly Returns
Best year (by Sharpe): 2023; worst year: 2020
Best month: +8.95%; worst month: -5.73%
Positive months: 59%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=1.72
- Sideways: S=0.74
- Bear: S=-0.61

## Negated Direction
Best negated: `rank(-1 * news_atr_ratio)` S=0.73, F=0.13, INFERIOR
Direction gap: +0.07 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * news_atr_ratio)`: S=0.73, F=0.13, T=113.2%, INFERIOR (TOP3000)
- `rank(-1 * news_atr_ratio / close)`: S=0.37, F=0.08, T=92.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(news_atr_ratio, 5))`: S=0.53, F=0.08, T=135.3%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(news_atr_ratio, 5))` | TOP200 | 0.67 | 0.16 | 8.6% | 80% | bull-only |
| `rank(ts_delta(news_atr_ratio, 5))` | TOP500 | 0.50 | 0.08 | 11.8% | 60% | bull-only |

## Correlation Notes
Top correlates:
- news_range_stddev: 0.942 (strongly positively correlated)
- news_session_range: 0.829 (strongly positively correlated)
- news_vol_stddev: 0.476 (moderately positively correlated)
- news_tot_ticks: 0.390 (weakly positively correlated)
- snt_buzz: -0.358 (weakly negatively correlated)

Redundancy cluster #62: 3 similar fields, mean |rho| 0.864 (representative: news_session_range). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
