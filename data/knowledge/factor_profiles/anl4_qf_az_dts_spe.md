---
field: anl4_qf_az_dts_spe
dataset: analyst4
best_template: rank_level
best_sharpe: 1.18
best_fitness: 0.73
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 10
max_drawdown: 0.0951
ann_vol: 0.0405
hit_rate: 0.5409
rolling_sharpe_min: -1.806
rolling_sharpe_max: 4.336
top_merge_partner: pv13_ompetitorgraphrank_hub_rank
redundancy_cluster: 22
negated_best_sharpe: 0.2
negated_best_template: rank_neg_delta
negated_best_fitness: 0.05
n_negated_sims: 10
direction_gap: -0.98
---
# anl4_qf_az_dts_spe (analyst4)

*Earnings per share - std of estimations*

## Signal Profile
- `rank(anl4_qf_az_dts_spe)`: S=1.18, F=0.73, T=4.6%, INFERIOR (TOP3000)
- `rank(anl4_qf_az_dts_spe / close)`: S=0.53, F=0.36, T=7.4%, INFERIOR (TOP200)
- `rank(ts_delta(anl4_qf_az_dts_spe, 5))`: S=0.45, F=0.12, T=39.1%, INFERIOR (TOP500)
- `-rank(anl4_qf_az_dts_spe)`: S=-0.33, F=-0.12, T=5.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_qf_az_dts_spe, 5))`: S=0.20, F=0.05, T=38.1%, INFERIOR (TOP3000)
- `ts_zscore(anl4_qf_az_dts_spe, 22)`: S=0.50, F=0.14, T=33.5%, INFERIOR (TOP3000)
- `ts_mean(anl4_qf_az_dts_spe, 10)`: S=0.12, F=0.04, T=4.3%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_qf_az_dts_spe, 22))`: S=0.43, F=0.13, T=17.0%, INFERIOR (TOP3000)
- `rank(-1 * anl4_qf_az_dts_spe)`: S=-0.25, F=-0.11, T=6.8%, INFERIOR (TOP3000)
- `rank(-1 * anl4_qf_az_dts_spe / close)`: S=-0.53, F=-0.36, T=7.4%, INFERIOR (TOP3000)

## Check Summary
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 5F/15P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 1.18, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.70 (moderate), ret=+2.2%
  - 2020: S=-0.63 (negative), ret=-2.4%
  - 2021: S=0.80 (moderate), ret=+4.0%
  - 2022: S=3.55 (strong), ret=+15.0%
  - 2023: S=1.37 (moderate), ret=+4.8%

## Risk & Drawdown
- Max drawdown: 9.51% over 638 days (recovered)
- Annualized: return +4.8%, volatility 4.0% (fraction of booksize)
- Hit rate: 54.1% positive days
- Tail shape: skew +0.04, excess kurtosis +1.02

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.81, max 4.34, latest 1.14

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +3.75%; worst month: -2.73%
Positive months: 66%

## Regime Profile
Regime profile: **mixed**
- Bull: S=3.29
- Sideways: S=0.45
- Bear: S=-0.48

## Negated Direction
Best negated: `rank(-1 * ts_delta(anl4_qf_az_dts_spe, 5))` S=0.20, F=0.05, INFERIOR
Direction gap: -0.98 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * anl4_qf_az_dts_spe)`: S=-0.25, F=-0.11, T=6.8%, INFERIOR (TOP3000)
- `rank(-1 * anl4_qf_az_dts_spe / close)`: S=-0.53, F=-0.36, T=7.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_qf_az_dts_spe, 5))`: S=0.20, F=0.05, T=38.1%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_qf_az_dts_spe)` | TOP3000 | 1.18 | 0.73 | 9.5% | 80% | mixed |
| `rank(anl4_qf_az_dts_spe / close)` | TOP200 | 0.53 | 0.36 | 13.9% | 80% | all-weather |
| `rank(anl4_qf_az_dts_spe / close)` | TOP3000 | 0.48 | 0.28 | 16.0% | 60% | mixed |
| `rank(anl4_qf_az_dts_spe / close)` | TOP500 | 0.47 | 0.28 | 11.9% | 80% | all-weather |
| `rank(anl4_qf_az_dts_spe)` | TOP500 | 0.42 | 0.20 | 15.8% | 60% | bull-only |
| `rank(anl4_qf_az_dts_spe / close)` | TOP1000 | 0.34 | 0.17 | 15.7% | 40% | mixed |
| `rank(anl4_qf_az_dts_spe)` | TOP1000 | 0.32 | 0.12 | 13.4% | 80% | bull-only |
| `rank(ts_delta(anl4_qf_az_dts_spe, 5))` | TOP500 | 0.44 | 0.12 | 11.5% | 80% | all-weather |
| `rank(anl4_qf_az_dts_spe)` | TOP200 | 0.23 | 0.11 | 14.5% | 60% | mixed |
| `rank(ts_delta(anl4_qf_az_dts_spe, 5))` | TOP1000 | 0.36 | 0.08 | 5.8% | 80% | all-weather |

## Correlation Notes
Top correlates:
- anl4_qfd1_az_dts_spe: 1.000 (strongly positively correlated)
- anl4_dts_rspe: 0.715 (strongly positively correlated)
- anl4_dts_ptp: 0.669 (moderately positively correlated)
- anl4_ebit_std: 0.658 (moderately positively correlated)
- sales_estimate_stddev_quarterly: 0.651 (moderately positively correlated)

Redundancy cluster #22: 3 similar fields, mean |rho| 0.81 (representative: anl4_qfd1_az_dts_spe). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| pv13_ompetitorgraphrank_hub_rank | pv13 | -0.10 | 1.75 | +0.56 | -0.45 | yes |
| fnd6_rank | fundamental6 | -0.12 | 1.76 | +0.58 | +0.05 | yes |
| fn_comp_options_forfeitures_and_expirations_a | fundamental2 | -0.09 | 1.70 | +0.51 | -0.32 | yes |
| rank(scl12_sentiment * (-1 * returns)) | socialmedia12 | +0.00 | 1.64 | +0.46 | -0.20 | yes |
| fn_def_tax_assets_liab_net_a | fundamental2 | -0.14 | 1.61 | +0.43 | -0.40 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
