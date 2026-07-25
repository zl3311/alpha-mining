---
field: implied_volatility_mean_skew_270
dataset: option8
best_template: rank_level
best_sharpe: 1.03
best_fitness: 0.43
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 27
regime_profile: bull-only
n_variations_with_pnl: 3
max_drawdown: 0.1729
ann_vol: 0.07
hit_rate: 0.5328
rolling_sharpe_min: -2.458
rolling_sharpe_max: 2.885
top_merge_partner: news_open_vol
redundancy_cluster: 13
negated_best_sharpe: 0.39
negated_best_template: rank_neg_delta
negated_best_fitness: 0.09
n_negated_sims: 10
direction_gap: -0.64
---
# implied_volatility_mean_skew_270 (option8)

*Skew steepness for the implied volatility duration of 270 calendar days by subtracting the mean implied volatility of the call and put options with strikes at 110% of the money from the mean implied volatility of the call and put options with strikes at 90% of the money*

## Signal Profile
- `rank(implied_volatility_mean_skew_270)`: S=1.03, F=0.43, T=40.3%, INFERIOR (TOP3000)
- `rank(implied_volatility_mean_skew_270 / close)`: S=0.70, F=0.38, T=18.4%, INFERIOR (TOP3000)
- `rank(ts_delta(implied_volatility_mean_skew_270, 5))`: S=-0.14, F=-0.01, T=64.9%, INFERIOR (TOP1000)
- `-rank(implied_volatility_mean_skew_270)`: S=-0.39, F=-0.15, T=23.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(implied_volatility_mean_skew_270, 5))`: S=0.39, F=0.09, T=57.1%, INFERIOR (TOP3000)
- `-ts_zscore(implied_volatility_mean_skew_270, 63)`: S=0.46, F=0.11, T=34.3%, INFERIOR (TOP3000)
- `ts_mean(implied_volatility_mean_skew_270, 10)`: S=0.44, F=0.28, T=9.8%, INFERIOR (TOP3000)
- `rank(ts_rank(implied_volatility_mean_skew_270, 22))`: S=-0.49, F=-0.10, T=43.3%, INFERIOR (TOP3000)
- `rank(-1 * implied_volatility_mean_skew_270)`: S=-0.06, F=-0.01, T=17.4%, INFERIOR (TOP3000)
- `rank(-1 * implied_volatility_mean_skew_270 / close)`: S=-0.35, F=-0.19, T=12.6%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 26F/1P
- HIGH_TURNOVER: 1F/26P
- LOW_FITNESS: 27F/0P
- LOW_SHARPE: 27F/0P
- LOW_SUB_UNIVERSE_SHARPE: 9F/7P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 1.03, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=2.44 (strong), ret=+6.5%
  - 2020: S=-1.12 (negative), ret=-5.4%
  - 2021: S=1.21 (moderate), ret=+12.9%
  - 2022: S=1.91 (strong), ret=+15.8%
  - 2023: S=1.09 (moderate), ret=+5.4%

## Risk & Drawdown
- Max drawdown: 17.29% over 395 days (recovered)
- Annualized: return +7.2%, volatility 7.0% (fraction of booksize)
- Hit rate: 53.3% positive days
- Tail shape: skew +0.18, excess kurtosis +1.95

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.46, max 2.88, latest 1.07

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2020
Best month: +7.34%; worst month: -6.53%
Positive months: 68%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.63
- Sideways: S=1.49
- Bear: S=-1.26

## Negated Direction
Best negated: `rank(-1 * ts_delta(implied_volatility_mean_skew_270, 5))` S=0.39, F=0.09, INFERIOR
Direction gap: -0.64 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * implied_volatility_mean_skew_270)`: S=-0.06, F=-0.01, T=17.4%, INFERIOR (TOP3000)
- `rank(-1 * implied_volatility_mean_skew_270 / close)`: S=-0.35, F=-0.19, T=12.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(implied_volatility_mean_skew_270, 5))`: S=0.39, F=0.09, T=57.1%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(implied_volatility_mean_skew_270)` | TOP3000 | 1.03 | 0.43 | 17.3% | 80% | bull-only |
| `rank(implied_volatility_mean_skew_270)` | TOP1000 | 0.40 | 0.15 | 23.5% | 80% | bull-only |
| `rank(implied_volatility_mean_skew_270)` | TOP500 | 0.36 | 0.15 | 17.5% | 60% | bull-only |

## Correlation Notes
Top correlates:
- implied_volatility_mean_skew_360: 0.985 (strongly positively correlated)
- implied_volatility_mean_skew_150: 0.973 (strongly positively correlated)
- implied_volatility_mean_skew_180: 0.962 (strongly positively correlated)
- implied_volatility_mean_skew_120: 0.955 (strongly positively correlated)
- implied_volatility_mean_skew_90: 0.945 (strongly positively correlated)

Redundancy cluster #13: 127 similar fields, mean |rho| 0.82 (representative: anl4_bvps_flag). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| news_open_vol | news12 | -0.56 | 2.09 | +1.06 | +0.17 | yes |
| anl4_rd_exp_flag | analyst4 | -0.43 | 1.83 | +0.81 | -0.97 | yes |
| anl4_afv4_dts_spe | analyst4 | -0.45 | 1.87 | +0.84 | +0.09 | yes |
| fnd6_cshtr | fundamental6 | -0.35 | 1.77 | +0.74 | -0.53 | yes |
| net_profit_adjusted_min_guidance | analyst4 | -0.32 | 1.67 | +0.64 | -0.76 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
