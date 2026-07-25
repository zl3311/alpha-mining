---
field: implied_volatility_mean_skew_1080
dataset: option8
best_template: ts_mean
best_sharpe: 0.87
best_fitness: 0.64
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 27
regime_profile: mixed
n_variations_with_pnl: 3
max_drawdown: 0.0962
ann_vol: 0.0539
hit_rate: 0.5304
rolling_sharpe_min: -1.361
rolling_sharpe_max: 2.669
top_merge_partner: news_open_vol
redundancy_cluster: 28
negated_best_sharpe: 0.9
negated_best_template: rank_neg_delta
negated_best_fitness: 0.19
n_negated_sims: 10
direction_gap: 0.03
---
# implied_volatility_mean_skew_1080 (option8)

*Skew steepness for the implied volatility duration of 1080 calendar days by subtracting the mean implied volatility of the call and put options with strikes at 110% of the money from the mean implied volatility of the call and put options with strikes at 90% of the money*

## Signal Profile
- `rank(implied_volatility_mean_skew_1080)`: S=1.01, F=0.37, T=40.9%, INFERIOR (TOP3000)
- `rank(implied_volatility_mean_skew_1080 / close)`: S=0.60, F=0.24, T=23.7%, INFERIOR (TOP3000)
- `rank(ts_delta(implied_volatility_mean_skew_1080, 5))`: S=-0.02, F=0.00, T=80.2%, INFERIOR (TOP3000)
- `-rank(implied_volatility_mean_skew_1080)`: S=-0.41, F=-0.13, T=25.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(implied_volatility_mean_skew_1080, 5))`: S=0.90, F=0.19, T=66.9%, INFERIOR (TOP3000)
- `-ts_zscore(implied_volatility_mean_skew_1080, 63)`: S=0.14, F=0.02, T=37.3%, INFERIOR (TOP3000)
- `ts_mean(implied_volatility_mean_skew_1080, 10)`: S=0.87, F=0.64, T=10.3%, INFERIOR (TOP3000)
- `rank(ts_rank(implied_volatility_mean_skew_1080, 22))`: S=-0.56, F=-0.11, T=46.8%, INFERIOR (TOP3000)
- `rank(-1 * implied_volatility_mean_skew_1080)`: S=-0.41, F=-0.13, T=25.1%, INFERIOR (TOP3000)
- `rank(-1 * implied_volatility_mean_skew_1080 / close)`: S=-0.60, F=-0.24, T=23.7%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 26F/1P
- HIGH_TURNOVER: 1F/26P
- LOW_FITNESS: 27F/0P
- LOW_SHARPE: 27F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/12P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 1.02, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=1.18 (moderate), ret=+3.3%
  - 2020: S=-0.42 (negative), ret=-1.8%
  - 2021: S=1.66 (strong), ret=+12.6%
  - 2022: S=1.45 (moderate), ret=+9.0%
  - 2023: S=0.90 (moderate), ret=+3.7%

## Risk & Drawdown
- Max drawdown: 9.62% over 180 days (recovered)
- Annualized: return +5.5%, volatility 5.4% (fraction of booksize)
- Hit rate: 53.0% positive days
- Tail shape: skew +0.11, excess kurtosis +1.59

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.36, max 2.67, latest 0.88

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2020
Best month: +4.71%; worst month: -3.82%
Positive months: 58%

## Regime Profile
Regime profile: **mixed**
- Bull: S=2.09
- Sideways: S=1.01
- Bear: S=-0.22

## Negated Direction
Best negated: `rank(-1 * ts_delta(implied_volatility_mean_skew_1080, 5))` S=0.90, F=0.19, INFERIOR
Direction gap: +0.03 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * implied_volatility_mean_skew_1080)`: S=-0.41, F=-0.13, T=25.1%, INFERIOR (TOP3000)
- `rank(-1 * implied_volatility_mean_skew_1080 / close)`: S=-0.60, F=-0.24, T=23.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(implied_volatility_mean_skew_1080, 5))`: S=0.90, F=0.19, T=66.9%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(implied_volatility_mean_skew_1080)` | TOP3000 | 1.02 | 0.37 | 9.6% | 80% | mixed |
| `rank(implied_volatility_mean_skew_1080)` | TOP500 | 0.57 | 0.22 | 8.5% | 40% | bull-only |
| `rank(implied_volatility_mean_skew_1080)` | TOP1000 | 0.42 | 0.13 | 12.7% | 60% | bull-only |

## Correlation Notes
Top correlates:
- implied_volatility_mean_skew_720: 0.999 (strongly positively correlated)
- implied_volatility_mean_skew_360: 0.959 (strongly positively correlated)
- implied_volatility_mean_skew_270: 0.923 (strongly positively correlated)
- implied_volatility_mean_skew_150: 0.891 (strongly positively correlated)
- implied_volatility_mean_skew_120: 0.882 (strongly positively correlated)

Redundancy cluster #28: 4 similar fields, mean |rho| 0.904 (representative: implied_volatility_mean_skew_360). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| news_open_vol | news12 | -0.60 | 2.08 | +1.07 | -0.35 | yes |
| fnd6_cshtr | fundamental6 | -0.41 | 1.87 | +0.86 | -0.26 | yes |
| anl4_rd_exp_flag | analyst4 | -0.39 | 1.67 | +0.65 | -0.90 | yes |
| fn_comp_options_forfeitures_and_expirations_a | fundamental2 | -0.23 | 1.76 | +0.59 | -0.81 | yes |
| anl4_afv4_dts_spe | analyst4 | -0.36 | 1.64 | +0.63 | -0.37 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
