---
field: implied_volatility_mean_skew_180
dataset: option8
best_template: ts_mean
best_sharpe: 0.71
best_fitness: 0.59
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 27
regime_profile: bull-only
n_variations_with_pnl: 5
max_drawdown: 0.1872
ann_vol: 0.0793
hit_rate: 0.5312
rolling_sharpe_min: -2.397
rolling_sharpe_max: 3.019
top_merge_partner: news_open_vol
redundancy_cluster: 13
negated_best_sharpe: 0.53
negated_best_template: rank_neg_delta
negated_best_fitness: 0.09
n_negated_sims: 10
direction_gap: -0.18
---
# implied_volatility_mean_skew_180 (option8)

*Skew steepness for the implied volatility duration of 180 calendar days by subtracting the mean implied volatility of the call and put options with strikes at 110% of the money from the mean implied volatility of the call and put options with strikes at 90% of the money*

## Signal Profile
- `rank(implied_volatility_mean_skew_180)`: S=1.07, F=0.50, T=38.8%, INFERIOR (TOP3000)
- `rank(implied_volatility_mean_skew_180 / close)`: S=0.74, F=0.44, T=17.4%, INFERIOR (TOP3000)
- `rank(ts_delta(implied_volatility_mean_skew_180, 5))`: S=0.12, F=0.02, T=55.8%, INFERIOR (TOP200)
- `-rank(implied_volatility_mean_skew_180)`: S=-0.39, F=-0.16, T=23.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(implied_volatility_mean_skew_180, 5))`: S=0.53, F=0.09, T=64.4%, INFERIOR (TOP3000)
- `-ts_zscore(implied_volatility_mean_skew_180, 63)`: S=0.38, F=0.08, T=34.0%, INFERIOR (TOP3000)
- `ts_mean(implied_volatility_mean_skew_180, 10)`: S=0.71, F=0.59, T=9.4%, INFERIOR (TOP3000)
- `rank(ts_rank(implied_volatility_mean_skew_180, 22))`: S=-0.73, F=-0.19, T=42.8%, INFERIOR (TOP3000)
- `rank(-1 * implied_volatility_mean_skew_180)`: S=-0.39, F=-0.16, T=23.0%, INFERIOR (TOP3000)
- `rank(-1 * implied_volatility_mean_skew_180 / close)`: S=-0.74, F=-0.44, T=17.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 26F/1P
- HIGH_TURNOVER: 1F/26P
- LOW_FITNESS: 27F/0P
- LOW_SHARPE: 27F/0P
- LOW_SUB_UNIVERSE_SHARPE: 15F/10P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 1.06, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=2.19 (strong), ret=+5.9%
  - 2020: S=-0.89 (negative), ret=-4.5%
  - 2021: S=1.11 (moderate), ret=+13.2%
  - 2022: S=2.27 (strong), ret=+23.3%
  - 2023: S=0.66 (moderate), ret=+3.5%

## Risk & Drawdown
- Max drawdown: 18.72% over 386 days (recovered)
- Annualized: return +8.5%, volatility 7.9% (fraction of booksize)
- Hit rate: 53.1% positive days
- Tail shape: skew +0.71, excess kurtosis +6.67

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.40, max 3.02, latest 0.65

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +9.73%; worst month: -7.40%
Positive months: 68%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.91
- Sideways: S=1.29
- Bear: S=-1.47

## Negated Direction
Best negated: `rank(-1 * ts_delta(implied_volatility_mean_skew_180, 5))` S=0.53, F=0.09, INFERIOR
Direction gap: -0.18 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * implied_volatility_mean_skew_180)`: S=-0.39, F=-0.16, T=23.0%, INFERIOR (TOP3000)
- `rank(-1 * implied_volatility_mean_skew_180 / close)`: S=-0.74, F=-0.44, T=17.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(implied_volatility_mean_skew_180, 5))`: S=0.53, F=0.09, T=64.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(implied_volatility_mean_skew_180)` | TOP3000 | 1.06 | 0.50 | 18.7% | 80% | bull-only |
| `rank(implied_volatility_mean_skew_180)` | TOP500 | 0.40 | 0.19 | 19.1% | 60% | bull-only |
| `rank(implied_volatility_mean_skew_180)` | TOP1000 | 0.39 | 0.16 | 26.5% | 80% | bull-only |
| `rank(implied_volatility_mean_skew_180)` | TOP200 | 0.09 | 0.02 | 36.9% | 80% | bull-only |
| `rank(ts_delta(implied_volatility_mean_skew_180, 5))` | TOP200 | 0.15 | 0.02 | 18.5% | 60% | mixed |

## Correlation Notes
Top correlates:
- implied_volatility_mean_skew_270: 0.962 (strongly positively correlated)
- implied_volatility_mean_skew_150: 0.944 (strongly positively correlated)
- implied_volatility_mean_skew_360: 0.916 (strongly positively correlated)
- implied_volatility_mean_skew_120: 0.914 (strongly positively correlated)
- implied_volatility_mean_skew_90: 0.904 (strongly positively correlated)

Redundancy cluster #13: 127 similar fields, mean |rho| 0.82 (representative: anl4_bvps_flag). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| news_open_vol | news12 | -0.53 | 2.06 | +0.99 | +0.15 | yes |
| anl4_rd_exp_flag | analyst4 | -0.42 | 1.90 | +0.83 | -0.98 | yes |
| anl4_afv4_dts_spe | analyst4 | -0.47 | 1.98 | +0.92 | -0.01 | yes |
| fnd6_cshtr | fundamental6 | -0.34 | 1.76 | +0.69 | -0.57 | yes |
| rank(fnd6_acdo) + rank(open/close - 1) | unknown | -0.31 | 2.68 | +0.66 | -0.75 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
