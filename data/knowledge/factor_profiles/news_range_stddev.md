---
field: news_range_stddev
dataset: news12
best_template: neg_rank_level
best_sharpe: 0.91
best_fitness: 0.18
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 20
regime_profile: bull-only
n_variations_with_pnl: 4
max_drawdown: 0.0957
ann_vol: 0.0947
hit_rate: 0.5158
rolling_sharpe_min: -0.573
rolling_sharpe_max: 2.463
redundancy_cluster: 62
negated_best_sharpe: 0.91
negated_best_template: neg_rank_level
negated_best_fitness: 0.18
n_negated_sims: 4
direction_gap: 0.25
---
# news_range_stddev (news12)

*Z-score of current day's trading range compared to 30-day average range, using 30-day range standard deviation*

## Signal Profile
- `rank(news_range_stddev)`: S=0.31, F=0.05, T=93.5%, INFERIOR (TOP500)
- `rank(ts_delta(news_range_stddev, 5))`: S=0.66, F=0.16, T=101.9%, INFERIOR (TOP200)
- `-rank(news_range_stddev)`: S=0.22, F=0.02, T=101.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(news_range_stddev, 5))`: S=0.53, F=0.08, T=135.0%, INFERIOR (TOP3000)
- `ts_zscore(news_range_stddev, 22)`: S=0.12, F=0.01, T=102.7%, INFERIOR (TOP3000)
- `ts_mean(news_range_stddev, 10)`: S=0.12, F=0.02, T=24.3%, INFERIOR (TOP3000)
- `rank(ts_rank(news_range_stddev, 22))`: S=0.21, F=0.02, T=104.9%, INFERIOR (TOP3000)
- `rank(-1 * news_range_stddev)`: S=0.91, F=0.18, T=112.7%, INFERIOR (TOP3000)
- `rank(-1 * news_range_stddev / close)`: S=0.32, F=0.05, T=104.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 19F/1P
- HIGH_TURNOVER: 19F/1P
- LOW_FITNESS: 20F/0P
- LOW_SHARPE: 20F/0P
- LOW_SUB_UNIVERSE_SHARPE: 4F/14P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.67, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.36 (weak), ret=+2.4%
  - 2020: S=-0.05 (negative), ret=-0.5%
  - 2021: S=0.49 (weak), ret=+5.4%
  - 2022: S=1.84 (strong), ret=+21.1%
  - 2023: S=0.42 (weak), ret=+2.8%

## Risk & Drawdown
- Max drawdown: 9.57% over 134 days (recovered)
- Annualized: return +6.4%, volatility 9.5% (fraction of booksize)
- Hit rate: 51.6% positive days
- Tail shape: skew +0.42, excess kurtosis +5.62

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.57, max 2.46, latest 0.39

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +11.21%; worst month: -8.44%
Positive months: 58%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=1.66
- Sideways: S=0.70
- Bear: S=-0.54

## Negated Direction
Best negated: `rank(-1 * news_range_stddev)` S=0.91, F=0.18, INFERIOR
Direction gap: +0.25 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * news_range_stddev)`: S=0.91, F=0.18, T=112.7%, INFERIOR (TOP3000)
- `rank(-1 * news_range_stddev / close)`: S=0.32, F=0.05, T=104.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(news_range_stddev, 5))`: S=0.53, F=0.08, T=135.0%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(news_range_stddev, 5))` | TOP200 | 0.67 | 0.16 | 9.6% | 80% | bull-only |
| `rank(ts_delta(news_range_stddev, 5))` | TOP500 | 0.61 | 0.12 | 11.0% | 60% | bull-only |
| `rank(news_range_stddev)` | TOP500 | 0.31 | 0.05 | 26.3% | 40% | bull-only |
| `rank(news_range_stddev)` | TOP200 | 0.14 | 0.02 | 26.7% | 60% | bull-only |

## Correlation Notes
Top correlates:
- news_atr_ratio: 0.942 (strongly positively correlated)
- news_session_range: 0.820 (strongly positively correlated)
- news_vol_stddev: 0.542 (moderately positively correlated)
- news_tot_ticks: 0.424 (moderately positively correlated)
- snt_buzz: -0.357 (weakly negatively correlated)

Redundancy cluster #62: 3 similar fields, mean |rho| 0.864 (representative: news_session_range). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, rank_value_norm, trade_when
