---
field: anl4_ptpr_flag
dataset: analyst4
best_template: rank_level
best_sharpe: 1.3
best_fitness: 1.04
best_universe: TOP3000
grade: AVERAGE
submittability: needs_upgrade
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 9
max_drawdown: 0.0976
ann_vol: 0.0621
hit_rate: 0.5328
rolling_sharpe_min: -1.371
rolling_sharpe_max: 3.008
top_merge_partner: rank(scl12_buzz * (-1 * returns))
redundancy_cluster: 13
negated_best_sharpe: 0.19
negated_best_template: rank_neg_delta
negated_best_fitness: 0.08
n_negated_sims: 10
direction_gap: -1.11
---
# anl4_ptpr_flag (analyst4)

*Reported Pretax income - forecast type (revision/new/...)*

## Signal Profile
- `rank(anl4_ptpr_flag)`: S=1.30, F=1.04, T=2.0%, AVERAGE (TOP3000)
- `rank(anl4_ptpr_flag / close)`: S=0.25, F=0.12, T=3.5%, INFERIOR (TOP200)
- `rank(ts_delta(anl4_ptpr_flag, 5))`: S=0.38, F=0.28, T=23.3%, INFERIOR (TOP500)
- `-rank(anl4_ptpr_flag)`: S=-0.75, F=-0.67, T=3.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_ptpr_flag, 5))`: S=0.19, F=0.08, T=33.5%, INFERIOR (TOP3000)
- `-ts_zscore(anl4_ptpr_flag, 63)`: S=0.37, F=0.47, T=6.8%, INFERIOR (TOP3000)
- `ts_mean(anl4_ptpr_flag, 10)`: S=0.65, F=0.55, T=3.2%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_ptpr_flag, 22))`: S=-0.15, F=-0.07, T=18.4%, INFERIOR (TOP3000)
- `rank(-1 * anl4_ptpr_flag)`: S=-1.30, F=-1.04, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * anl4_ptpr_flag / close)`: S=0.08, F=0.02, T=2.5%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 13F/19P
- LOW_FITNESS: 31F/1P
- LOW_SHARPE: 31F/1P
- LOW_SUB_UNIVERSE_SHARPE: 14F/15P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 1.28, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=1.86 (strong), ret=+6.1%
  - 2020: S=-0.32 (negative), ret=-1.3%
  - 2021: S=1.70 (strong), ret=+15.6%
  - 2022: S=1.98 (strong), ret=+14.7%
  - 2023: S=0.89 (moderate), ret=+4.0%

## Risk & Drawdown
- Max drawdown: 9.76% over 537 days (recovered)
- Annualized: return +8.0%, volatility 6.2% (fraction of booksize)
- Hit rate: 53.3% positive days
- Tail shape: skew -0.09, excess kurtosis +3.74

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.37, max 3.01, latest 0.72

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +5.93%; worst month: -2.23%
Positive months: 71%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.53
- Sideways: S=1.86
- Bear: S=-0.91

## Negated Direction
Best negated: `rank(-1 * ts_delta(anl4_ptpr_flag, 5))` S=0.19, F=0.08, INFERIOR
Direction gap: -1.11 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * anl4_ptpr_flag)`: S=-1.30, F=-1.04, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * anl4_ptpr_flag / close)`: S=0.08, F=0.02, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_ptpr_flag, 5))`: S=0.19, F=0.08, T=33.5%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_ptpr_flag)` | TOP3000 | 1.28 | 1.04 | 9.8% | 80% | bull-only |
| `rank(anl4_ptpr_flag)` | TOP1000 | 0.75 | 0.67 | 18.5% | 60% | bull-only |
| `rank(anl4_ptpr_flag)` | TOP500 | 0.60 | 0.57 | 48.0% | 80% | bull-only |
| `rank(ts_delta(anl4_ptpr_flag, 5))` | TOP500 | 0.38 | 0.28 | 74.1% | 80% | mixed |
| `rank(ts_delta(anl4_ptpr_flag, 5))` | TOP1000 | 0.40 | 0.27 | 69.6% | 60% | all-weather |
| `rank(anl4_ptpr_flag / close)` | TOP200 | 0.26 | 0.12 | 21.1% | 80% | mixed |
| `rank(anl4_ptpr_flag)` | TOP200 | 0.19 | 0.12 | 74.8% | 80% | bull-only |
| `rank(anl4_ptpr_flag / close)` | TOP1000 | 0.10 | 0.03 | 38.4% | 40% | bear-only |
| `rank(anl4_ptpr_flag / close)` | TOP500 | 0.09 | 0.02 | 33.5% | 60% | bear-only |

## Correlation Notes
Top correlates:
- rel_num_all: 0.854 (strongly positively correlated)
- anl4_bvps_flag: 0.846 (strongly positively correlated)
- anl4_tot_gw_ft: 0.826 (strongly positively correlated)
- rel_num_comp: 0.823 (strongly positively correlated)
- rel_num_part: 0.821 (strongly positively correlated)

Redundancy cluster #13: 127 similar fields, mean |rho| 0.82 (representative: anl4_bvps_flag). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| rank(scl12_buzz * (-1 * returns)) | socialmedia12 | -0.31 | 2.45 | +0.82 | -0.79 | yes |
| rank(fnd6_acdo) + rank(open/close - 1) | unknown | -0.32 | 2.83 | +0.81 | -0.74 | yes |
| fn_comp_options_forfeitures_and_expirations_a | fundamental2 | -0.26 | 2.01 | +0.73 | -0.89 | yes |
| rank(fnd6_acdo) * rank(-1 * returns) | unknown | -0.29 | 2.60 | +0.73 | -0.79 | yes |
| anl4_afv4_dts_spe | analyst4 | -0.49 | 2.06 | +0.78 | -0.23 | yes |

## Actionability
Cataloged as active factor but not yet in submitted book.
Needs grade upgrade. Try decay_linear wrap, value normalization, or blend with complementary factor.
Untried templates: decay_linear, trade_when
