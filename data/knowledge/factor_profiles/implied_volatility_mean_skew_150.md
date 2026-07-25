---
field: implied_volatility_mean_skew_150
dataset: option8
best_template: ts_mean
best_sharpe: 0.79
best_fitness: 0.7
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 27
regime_profile: bull-only
n_variations_with_pnl: 3
max_drawdown: 0.1917
ann_vol: 0.0798
hit_rate: 0.5279
rolling_sharpe_min: -2.609
rolling_sharpe_max: 2.476
top_merge_partner: news_open_vol
redundancy_cluster: 13
negated_best_sharpe: 0.5
negated_best_template: rank_neg_delta
negated_best_fitness: 0.09
n_negated_sims: 10
direction_gap: -0.29
---
# implied_volatility_mean_skew_150 (option8)

*Skew steepness for the implied volatility duration of 150 calendar days by subtracting the mean implied volatility of the call and put options with strikes at 110% of the money from the mean implied volatility of the call and put options with strikes at 90% of the money*

## Signal Profile
- `rank(implied_volatility_mean_skew_150)`: S=0.86, F=0.36, T=38.7%, INFERIOR (TOP3000)
- `rank(implied_volatility_mean_skew_150 / close)`: S=0.65, F=0.37, T=17.1%, INFERIOR (TOP3000)
- `rank(ts_delta(implied_volatility_mean_skew_150, 5))`: S=0.07, F=0.01, T=55.3%, INFERIOR (TOP200)
- `-rank(implied_volatility_mean_skew_150)`: S=-0.35, F=-0.13, T=22.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(implied_volatility_mean_skew_150, 5))`: S=0.50, F=0.09, T=64.2%, INFERIOR (TOP3000)
- `-ts_zscore(implied_volatility_mean_skew_150, 63)`: S=0.44, F=0.11, T=33.9%, INFERIOR (TOP3000)
- `ts_mean(implied_volatility_mean_skew_150, 10)`: S=0.79, F=0.70, T=9.2%, INFERIOR (TOP3000)
- `rank(ts_rank(implied_volatility_mean_skew_150, 22))`: S=-0.70, F=-0.18, T=42.6%, INFERIOR (TOP3000)
- `rank(-1 * implied_volatility_mean_skew_150)`: S=-0.35, F=-0.13, T=22.9%, INFERIOR (TOP3000)
- `rank(-1 * implied_volatility_mean_skew_150 / close)`: S=-0.65, F=-0.37, T=17.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 26F/1P
- HIGH_TURNOVER: 1F/26P
- LOW_FITNESS: 27F/0P
- LOW_SHARPE: 27F/0P
- LOW_SUB_UNIVERSE_SHARPE: 16F/9P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.85, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=1.75 (strong), ret=+4.9%
  - 2020: S=-1.17 (negative), ret=-6.0%
  - 2021: S=1.08 (moderate), ret=+13.3%
  - 2022: S=1.69 (strong), ret=+16.4%
  - 2023: S=0.90 (moderate), ret=+4.9%

## Risk & Drawdown
- Max drawdown: 19.17% over 603 days (recovered)
- Annualized: return +6.8%, volatility 8.0% (fraction of booksize)
- Hit rate: 52.8% positive days
- Tail shape: skew +0.19, excess kurtosis +2.36

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.61, max 2.48, latest 0.87

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2020
Best month: +8.02%; worst month: -7.57%
Positive months: 64%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.63
- Sideways: S=1.22
- Bear: S=-1.62

## Negated Direction
Best negated: `rank(-1 * ts_delta(implied_volatility_mean_skew_150, 5))` S=0.50, F=0.09, INFERIOR
Direction gap: -0.29 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * implied_volatility_mean_skew_150)`: S=-0.35, F=-0.13, T=22.9%, INFERIOR (TOP3000)
- `rank(-1 * implied_volatility_mean_skew_150 / close)`: S=-0.65, F=-0.37, T=17.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(implied_volatility_mean_skew_150, 5))`: S=0.50, F=0.09, T=64.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(implied_volatility_mean_skew_150)` | TOP3000 | 0.85 | 0.36 | 19.2% | 80% | bull-only |
| `rank(implied_volatility_mean_skew_150)` | TOP500 | 0.36 | 0.16 | 20.8% | 60% | bull-only |
| `rank(implied_volatility_mean_skew_150)` | TOP1000 | 0.35 | 0.13 | 27.4% | 80% | bull-only |

## Correlation Notes
Top correlates:
- implied_volatility_mean_skew_120: 0.993 (strongly positively correlated)
- implied_volatility_mean_skew_90: 0.983 (strongly positively correlated)
- implied_volatility_mean_skew_270: 0.973 (strongly positively correlated)
- implied_volatility_mean_skew_60: 0.969 (strongly positively correlated)
- implied_volatility_mean_skew_360: 0.960 (strongly positively correlated)

Redundancy cluster #13: 127 similar fields, mean |rho| 0.82 (representative: anl4_bvps_flag). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| news_open_vol | news12 | -0.55 | 1.86 | +0.94 | +0.05 | yes |
| anl4_rd_exp_flag | analyst4 | -0.43 | 1.75 | +0.72 | -0.99 | yes |
| anl4_afv4_dts_spe | analyst4 | -0.48 | 1.80 | +0.81 | -0.00 | yes |
| max_adjusted_net_profit_guidance | analyst4 | -0.39 | 1.50 | +0.64 | -0.92 | yes |
| net_profit_adjusted_min_guidance | analyst4 | -0.34 | 1.57 | +0.62 | -0.82 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
