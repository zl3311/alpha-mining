---
field: news_low_exc_stddev
dataset: news12
best_template: rank_delta
best_sharpe: 0.93
best_fitness: 0.22
best_universe: TOP500
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 20
regime_profile: mixed
n_variations_with_pnl: 6
max_drawdown: 0.0845
ann_vol: 0.0703
hit_rate: 0.5279
rolling_sharpe_min: -0.599
rolling_sharpe_max: 2.397
top_merge_partner: net_profit_adjusted_min_guidance
redundancy_cluster: 42
negated_best_sharpe: 0.14
negated_best_template: neg_rank_level
negated_best_fitness: 0.01
n_negated_sims: 3
direction_gap: -0.79
---
# news_low_exc_stddev (news12)

*Standardized measure of price movement from last price in time-of-news window to end-of-day low, divided by 30-day closing price standard deviation*

## Signal Profile
- `rank(news_low_exc_stddev)`: S=0.53, F=0.09, T=110.2%, INFERIOR (TOP1000)
- `rank(news_low_exc_stddev / close)`: S=0.24, F=0.04, T=93.1%, INFERIOR (TOP3000)
- `rank(ts_delta(news_low_exc_stddev, 5))`: S=0.93, F=0.22, T=122.0%, INFERIOR (TOP500)
- `-rank(news_low_exc_stddev)`: S=-0.53, F=-0.09, T=110.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(news_low_exc_stddev, 5))`: S=-0.65, F=-0.11, T=144.6%, INFERIOR (TOP3000)
- `ts_zscore(news_low_exc_stddev, 22)`: S=0.42, F=0.06, T=109.3%, INFERIOR (TOP3000)
- `ts_mean(news_low_exc_stddev, 10)`: S=-0.52, F=-0.19, T=22.9%, INFERIOR (TOP3000)
- `rank(ts_rank(news_low_exc_stddev, 22))`: S=0.61, F=0.10, T=113.2%, INFERIOR (TOP3000)
- `rank(-1 * news_low_exc_stddev)`: S=0.14, F=0.01, T=126.0%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 19F/1P
- HIGH_TURNOVER: 19F/1P
- LOW_FITNESS: 20F/0P
- LOW_SHARPE: 20F/0P
- LOW_SUB_UNIVERSE_SHARPE: 8F/10P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.94, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=1.89 (strong), ret=+11.8%
  - 2020: S=-0.14 (negative), ret=-1.0%
  - 2021: S=1.66 (strong), ret=+14.3%
  - 2022: S=0.99 (moderate), ret=+7.4%
  - 2023: S=-0.06 (negative), ret=-0.3%

## Risk & Drawdown
- Max drawdown: 8.45% over 257 days (recovered)
- Annualized: return +6.6%, volatility 7.0% (fraction of booksize)
- Hit rate: 52.8% positive days
- Tail shape: skew +0.14, excess kurtosis +1.43

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.60, max 2.40, latest -0.06

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2020
Best month: +5.07%; worst month: -6.52%
Positive months: 61%

## Regime Profile
Regime profile: **mixed**
- Bull: S=1.48
- Sideways: S=1.00
- Bear: S=0.29

## Negated Direction
Best negated: `rank(-1 * news_low_exc_stddev)` S=0.14, F=0.01, INFERIOR
Direction gap: -0.79 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * news_low_exc_stddev)`: S=0.14, F=0.01, T=126.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(news_low_exc_stddev, 5))`: S=-0.65, F=-0.11, T=144.6%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(news_low_exc_stddev, 5))` | TOP500 | 0.94 | 0.22 | 8.5% | 60% | mixed |
| `rank(ts_delta(news_low_exc_stddev, 5))` | TOP1000 | 0.88 | 0.19 | 9.2% | 80% | mixed |
| `rank(ts_delta(news_low_exc_stddev, 5))` | TOP3000 | 0.65 | 0.11 | 16.3% | 80% | mixed |
| `rank(ts_delta(news_low_exc_stddev, 5))` | TOP200 | 0.49 | 0.10 | 11.0% | 80% | mixed |
| `rank(news_low_exc_stddev)` | TOP1000 | 0.50 | 0.09 | 6.9% | 80% | bull-only |
| `rank(news_low_exc_stddev)` | TOP500 | 0.31 | 0.05 | 8.3% | 60% | mixed |

## Correlation Notes
Top correlates:
- news_max_dn_amt: 0.772 (strongly positively correlated)
- news_max_dn_ret: 0.517 (moderately positively correlated)
- news_range_stddev: 0.329 (weakly positively correlated)
- news_atr_ratio: 0.318 (weakly positively correlated)
- news_session_range: 0.316 (weakly positively correlated)

Redundancy cluster #42: 2 similar fields, mean |rho| 0.772 (representative). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| net_profit_adjusted_min_guidance | analyst4 | -0.02 | 1.33 | +0.39 | -0.78 | yes |
| fnd6_newqv1300_acomincq | fundamental6 | -0.09 | 1.34 | +0.39 | -0.48 | yes |
| fnd6_idesindq_curcd | fundamental6 | -0.07 | 1.31 | +0.38 | -0.60 | yes |
| fnd2_a_sbcpnargmpmtwopsffesip | fundamental2 | -0.04 | 1.27 | +0.34 | -0.94 | yes |
| implied_volatility_mean_skew_270 | option8 | -0.10 | 1.46 | +0.43 | +0.74 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
