---
field: pcr_vol_10
dataset: option9
best_template: rank_level
best_sharpe: 1.25
best_fitness: 0.48
best_universe: TOP500
grade: INFERIOR
submittability: blocked_LOW_FITNESS
n_sims: 20
regime_profile: mixed
n_variations_with_pnl: 8
max_drawdown: 0.0815
ann_vol: 0.0564
hit_rate: 0.5457
rolling_sharpe_min: -0.433
rolling_sharpe_max: 3.397
top_merge_partner: fn_comp_options_forfeitures_and_expirations_a
negated_best_sharpe: -0.11
negated_best_template: neg_rank_value_norm
negated_best_fitness: -0.01
n_negated_sims: 4
direction_gap: -1.36
---
# pcr_vol_10 (option9)

*Ratio of total put option volume to call option volume for options expiring in 10 days, reflecting very short-term sentiment flow*

## Signal Profile
- `rank(pcr_vol_10)`: S=1.25, F=0.48, T=46.8%, INFERIOR (TOP500)
- `rank(ts_delta(pcr_vol_10, 5))`: S=0.91, F=0.21, T=69.6%, INFERIOR (TOP500)
- `-rank(pcr_vol_10)`: S=-1.34, F=-0.45, T=49.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(pcr_vol_10, 5))`: S=-0.37, F=-0.04, T=84.1%, INFERIOR (TOP3000)
- `ts_zscore(pcr_vol_10, 22)`: S=1.07, F=0.29, T=57.5%, INFERIOR (TOP3000)
- `ts_mean(pcr_vol_10, 10)`: S=0.23, F=0.07, T=18.1%, INFERIOR (TOP3000)
- `rank(ts_rank(pcr_vol_10, 22))`: S=1.03, F=0.26, T=60.9%, INFERIOR (TOP3000)
- `rank(-1 * pcr_vol_10)`: S=-0.63, F=-0.13, T=59.9%, INFERIOR (TOP3000)
- `rank(-1 * pcr_vol_10 / close)`: S=-0.11, F=-0.01, T=57.9%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 20F/0P
- HIGH_TURNOVER: 5F/15P
- LOW_FITNESS: 20F/0P
- LOW_SHARPE: 16F/4P
- LOW_SUB_UNIVERSE_SHARPE: 7F/11P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 1.25, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.83 (moderate), ret=+2.5%
  - 2020: S=0.61 (moderate), ret=+2.9%
  - 2021: S=2.38 (strong), ret=+19.9%
  - 2022: S=1.15 (moderate), ret=+6.8%
  - 2023: S=0.65 (moderate), ret=+2.5%

## Risk & Drawdown
- Max drawdown: 8.15% over 167 days (recovered)
- Annualized: return +7.1%, volatility 5.6% (fraction of booksize)
- Hit rate: 54.6% positive days
- Tail shape: skew +0.08, excess kurtosis +2.60

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.43, max 3.40, latest 0.63

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2020
Best month: +6.53%; worst month: -4.84%
Positive months: 75%

## Regime Profile
Regime profile: **mixed**
- Bull: S=2.53
- Sideways: S=1.03
- Bear: S=0.12

## Negated Direction
Best negated: `rank(-1 * pcr_vol_10 / close)` S=-0.11, F=-0.01, INFERIOR
Direction gap: -1.36 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * pcr_vol_10)`: S=-0.63, F=-0.13, T=59.9%, INFERIOR (TOP3000)
- `rank(-1 * pcr_vol_10 / close)`: S=-0.11, F=-0.01, T=57.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(pcr_vol_10, 5))`: S=-0.37, F=-0.04, T=84.1%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(pcr_vol_10)` | TOP500 | 1.25 | 0.48 | 8.2% | 100% | mixed |
| `rank(pcr_vol_10)` | TOP1000 | 1.33 | 0.45 | 8.8% | 100% | mixed |
| `rank(pcr_vol_10)` | TOP200 | 0.75 | 0.27 | 14.8% | 60% | mixed |
| `rank(ts_delta(pcr_vol_10, 5))` | TOP500 | 0.91 | 0.21 | 4.9% | 100% | all-weather |
| `rank(ts_delta(pcr_vol_10, 5))` | TOP200 | 0.74 | 0.20 | 10.3% | 60% | all-weather |
| `rank(ts_delta(pcr_vol_10, 5))` | TOP1000 | 0.95 | 0.19 | 4.0% | 100% | mixed |
| `rank(pcr_vol_10)` | TOP3000 | 0.64 | 0.13 | 7.2% | 80% | mixed |
| `rank(ts_delta(pcr_vol_10, 5))` | TOP3000 | 0.40 | 0.04 | 5.6% | 40% | bull-only |

## Correlation Notes
Top correlates:
- pcr_vol_20: 0.652 (moderately positively correlated)
- pcr_vol_all: 0.645 (moderately positively correlated)
- pcr_vol_30: 0.597 (moderately positively correlated)
- implied_volatility_mean_skew_20: 0.594 (moderately positively correlated)
- pcr_oi_60: 0.515 (moderately positively correlated)

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| fn_comp_options_forfeitures_and_expirations_a | fundamental2 | -0.19 | 1.90 | +0.64 | -0.57 | yes |
| news_open_vol | news12 | -0.30 | 1.79 | +0.54 | -0.84 | yes |
| anl4_afv4_dts_spe | analyst4 | -0.33 | 1.78 | +0.52 | -0.92 | yes |
| anl4_epsr_flag | analyst4 | -0.12 | 1.74 | +0.48 | -0.96 | yes |
| anl4_qf_az_wol_spfc | analyst4 | -0.02 | 1.94 | +0.49 | -0.71 | yes |

## Actionability
Blocked by LOW_FITNESS. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, rank_value_norm, trade_when
