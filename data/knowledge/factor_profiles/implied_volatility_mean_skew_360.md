---
field: implied_volatility_mean_skew_360
dataset: option8
best_template: rank_level
best_sharpe: 1.1
best_fitness: 0.46
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 27
regime_profile: bull-only
n_variations_with_pnl: 4
max_drawdown: 0.142
ann_vol: 0.0651
hit_rate: 0.5352
rolling_sharpe_min: -1.969
rolling_sharpe_max: 2.763
top_merge_partner: news_open_vol
redundancy_cluster: 28
negated_best_sharpe: 0.26
negated_best_template: rank_neg_delta
negated_best_fitness: 0.03
n_negated_sims: 10
direction_gap: -0.84
---
# implied_volatility_mean_skew_360 (option8)

*Skew steepness for the implied volatility duration of 360 calendar days by subtracting the mean implied volatility of the call and put options with strikes at 110% of the money from the mean implied volatility of the call and put options with strikes at 90% of the money*

## Signal Profile
- `rank(implied_volatility_mean_skew_360)`: S=1.10, F=0.46, T=40.6%, INFERIOR (TOP3000)
- `rank(implied_volatility_mean_skew_360 / close)`: S=0.82, F=0.46, T=19.5%, INFERIOR (TOP3000)
- `rank(ts_delta(implied_volatility_mean_skew_360, 5))`: S=0.03, F=0.00, T=80.1%, INFERIOR (TOP3000)
- `-rank(implied_volatility_mean_skew_360)`: S=-0.50, F=-0.20, T=23.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(implied_volatility_mean_skew_360, 5))`: S=0.26, F=0.03, T=65.4%, INFERIOR (TOP3000)
- `-ts_zscore(implied_volatility_mean_skew_360, 63)`: S=0.13, F=0.02, T=34.8%, INFERIOR (TOP3000)
- `ts_mean(implied_volatility_mean_skew_360, 10)`: S=0.48, F=0.30, T=10.0%, INFERIOR (TOP3000)
- `rank(ts_rank(implied_volatility_mean_skew_360, 22))`: S=-0.34, F=-0.06, T=44.2%, INFERIOR (TOP3000)
- `rank(-1 * implied_volatility_mean_skew_360)`: S=-0.50, F=-0.20, T=23.8%, INFERIOR (TOP3000)
- `rank(-1 * implied_volatility_mean_skew_360 / close)`: S=-0.82, F=-0.46, T=19.5%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 26F/1P
- HIGH_TURNOVER: 1F/26P
- LOW_FITNESS: 27F/0P
- LOW_SHARPE: 27F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/11P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 1.10, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=2.34 (strong), ret=+6.3%
  - 2020: S=-0.88 (negative), ret=-4.1%
  - 2021: S=1.40 (moderate), ret=+13.6%
  - 2022: S=1.74 (strong), ret=+13.4%
  - 2023: S=1.24 (moderate), ret=+5.9%

## Risk & Drawdown
- Max drawdown: 14.20% over 327 days (recovered)
- Annualized: return +7.2%, volatility 6.5% (fraction of booksize)
- Hit rate: 53.5% positive days
- Tail shape: skew +0.17, excess kurtosis +1.74

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.97, max 2.76, latest 1.20

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2020
Best month: +6.32%; worst month: -4.96%
Positive months: 64%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.41
- Sideways: S=1.48
- Bear: S=-0.76

## Negated Direction
Best negated: `rank(-1 * ts_delta(implied_volatility_mean_skew_360, 5))` S=0.26, F=0.03, INFERIOR
Direction gap: -0.84 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * implied_volatility_mean_skew_360)`: S=-0.50, F=-0.20, T=23.8%, INFERIOR (TOP3000)
- `rank(-1 * implied_volatility_mean_skew_360 / close)`: S=-0.82, F=-0.46, T=19.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(implied_volatility_mean_skew_360, 5))`: S=0.26, F=0.03, T=65.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(implied_volatility_mean_skew_360)` | TOP3000 | 1.10 | 0.46 | 14.2% | 80% | bull-only |
| `rank(implied_volatility_mean_skew_360)` | TOP1000 | 0.51 | 0.20 | 19.1% | 60% | bull-only |
| `rank(implied_volatility_mean_skew_360)` | TOP500 | 0.46 | 0.20 | 15.3% | 60% | bull-only |
| `rank(implied_volatility_mean_skew_360)` | TOP200 | 0.11 | 0.03 | 30.6% | 60% | bull-only |

## Correlation Notes
Top correlates:
- implied_volatility_mean_skew_270: 0.985 (strongly positively correlated)
- implied_volatility_mean_skew_720: 0.964 (strongly positively correlated)
- implied_volatility_mean_skew_150: 0.960 (strongly positively correlated)
- implied_volatility_mean_skew_1080: 0.959 (strongly positively correlated)
- implied_volatility_mean_skew_120: 0.948 (strongly positively correlated)

Redundancy cluster #28: 4 similar fields, mean |rho| 0.904 (representative). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| news_open_vol | news12 | -0.58 | 2.20 | +1.10 | +0.12 | yes |
| anl4_rd_exp_flag | analyst4 | -0.42 | 1.84 | +0.74 | -0.96 | yes |
| fnd6_cshtr | fundamental6 | -0.38 | 1.89 | +0.78 | -0.48 | yes |
| fn_comp_options_forfeitures_and_expirations_a | fundamental2 | -0.25 | 1.85 | +0.68 | -0.83 | yes |
| anl4_afv4_dts_spe | analyst4 | -0.42 | 1.86 | +0.76 | +0.06 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
