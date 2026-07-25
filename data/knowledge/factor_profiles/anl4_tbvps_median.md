---
field: anl4_tbvps_median
dataset: analyst4
best_template: rank_value_norm
best_sharpe: 1.07
best_fitness: 0.81
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: all-weather
n_variations_with_pnl: 6
max_drawdown: 0.0817
ann_vol: 0.0669
hit_rate: 0.5158
rolling_sharpe_min: -1.11
rolling_sharpe_max: 3.302
top_merge_partner: anl4_epsr_flag
redundancy_cluster: 29
negated_best_sharpe: 0.38
negated_best_template: rank_neg_delta
negated_best_fitness: 0.14
n_negated_sims: 10
direction_gap: -0.69
---
# anl4_tbvps_median (analyst4)

*Tangible Book Value per Share - median of estimations*

## Signal Profile
- `rank(anl4_tbvps_median)`: S=0.53, F=0.31, T=2.1%, INFERIOR (TOP500)
- `rank(anl4_tbvps_median / close)`: S=1.07, F=0.81, T=2.2%, INFERIOR (TOP3000)
- `rank(ts_delta(anl4_tbvps_median, 5))`: S=0.43, F=0.11, T=35.9%, INFERIOR (TOP3000)
- `-rank(anl4_tbvps_median)`: S=-0.16, F=-0.05, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_tbvps_median, 5))`: S=0.38, F=0.14, T=33.8%, INFERIOR (TOP3000)
- `-ts_zscore(anl4_tbvps_median, 63)`: S=0.27, F=0.09, T=15.9%, INFERIOR (TOP3000)
- `ts_mean(anl4_tbvps_median, 10)`: S=-0.24, F=-0.13, T=1.8%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_tbvps_median, 22))`: S=-0.34, F=-0.13, T=14.4%, INFERIOR (TOP3000)
- `rank(-1 * anl4_tbvps_median)`: S=-0.53, F=-0.31, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * anl4_tbvps_median / close)`: S=-0.87, F=-0.73, T=2.8%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 10F/22P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/16P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 1.06, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=-0.38 (negative), ret=-1.6%
  - 2020: S=1.21 (moderate), ret=+11.4%
  - 2021: S=1.92 (strong), ret=+9.9%
  - 2022: S=1.84 (strong), ret=+9.9%
  - 2023: S=0.74 (moderate), ret=+5.1%

## Risk & Drawdown
- Max drawdown: 8.17% over 184 days (recovered)
- Annualized: return +7.1%, volatility 6.7% (fraction of booksize)
- Hit rate: 51.6% positive days
- Tail shape: skew +0.60, excess kurtosis +5.14

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.11, max 3.30, latest 0.82

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2019
Best month: +4.60%; worst month: -3.27%
Positive months: 59%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=1.94
- Sideways: S=0.39
- Bear: S=0.89

## Negated Direction
Best negated: `rank(-1 * ts_delta(anl4_tbvps_median, 5))` S=0.38, F=0.14, INFERIOR
Direction gap: -0.69 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * anl4_tbvps_median)`: S=-0.53, F=-0.31, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * anl4_tbvps_median / close)`: S=-0.87, F=-0.73, T=2.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_tbvps_median, 5))`: S=0.38, F=0.14, T=33.8%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_tbvps_median / close)` | TOP3000 | 1.06 | 0.81 | 8.2% | 80% | all-weather |
| `rank(anl4_tbvps_median / close)` | TOP500 | 0.88 | 0.73 | 16.1% | 60% | mixed |
| `rank(anl4_tbvps_median / close)` | TOP1000 | 0.67 | 0.44 | 9.6% | 80% | all-weather |
| `rank(anl4_tbvps_median)` | TOP500 | 0.53 | 0.31 | 16.4% | 60% | mixed |
| `rank(ts_delta(anl4_tbvps_median, 5))` | TOP3000 | 0.42 | 0.11 | 12.1% | 60% | weak |
| `rank(anl4_tbvps_median)` | TOP1000 | 0.14 | 0.05 | 10.8% | 40% | bull-only |

## Correlation Notes
Top correlates:
- anl4_tbvps_mean: 1.000 (strongly positively correlated)
- anl4_tbvps_low: 0.999 (strongly positively correlated)
- anl4_tbvps_high: 0.999 (strongly positively correlated)
- anl4_bvps_low: 0.752 (strongly positively correlated)
- anl4_bvps_median: 0.752 (strongly positively correlated)

Redundancy cluster #29: 5 similar fields, mean |rho| 0.883 (representative: anl4_tbvps_high). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_epsr_flag | analyst4 | -0.26 | 1.80 | +0.62 | -0.39 | no |
| pcr_vol_20 | option9 | -0.11 | 1.59 | +0.46 | -0.46 | yes |
| anl4_netdebt_flag | analyst_revision | -0.13 | 1.77 | +0.50 | +0.29 | yes |
| pcr_vol_30 | option9 | -0.11 | 1.59 | +0.46 | -0.26 | yes |
| rp_css_ptg | news18 | -0.17 | 1.54 | +0.49 | +0.84 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
