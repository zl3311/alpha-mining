---
field: anl4_totassets_flag
dataset: analyst4
cluster: analyst4_balance_sheet_assets
coverage: 0.8122
community_alphas: 11280
best_template: rank_level
best_sharpe: 1.28
best_fitness: 1.27
best_universe: TOP3000
grade: AVERAGE
submittability: needs_upgrade
n_sims: 32
regime_profile: all-weather
n_variations_with_pnl: 4
max_drawdown: 0.116
ann_vol: 0.096
hit_rate: 0.5304
rolling_sharpe_min: -0.455
rolling_sharpe_max: 2.966
top_merge_partner: rank(scl12_buzz * (-1 * returns))
redundancy_cluster: 18
negated_best_sharpe: 0.56
negated_best_template: rank_neg_delta
negated_best_fitness: 0.44
n_negated_sims: 10
direction_gap: -0.72
---
# anl4_totassets_flag (analyst4)

*Total Assets - forecast type (revision/new/...)*

## Signal Profile
- `rank(anl4_totassets_flag)`: S=1.28, F=1.27, T=3.0%, AVERAGE (TOP3000)
- `rank(anl4_totassets_flag / close)`: S=0.30, F=0.16, T=3.2%, INFERIOR (TOP200)
- `rank(ts_delta(anl4_totassets_flag, 5))`: S=-0.05, F=-0.02, T=21.5%, INFERIOR (TOP1000)
- `-rank(anl4_totassets_flag)`: S=-0.69, F=-0.77, T=5.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_totassets_flag, 5))`: S=0.56, F=0.44, T=34.0%, INFERIOR (TOP3000)
- `-ts_zscore(anl4_totassets_flag, 63)`: S=-0.09, F=-0.06, T=8.7%, INFERIOR (TOP3000)
- `ts_mean(anl4_totassets_flag, 10)`: S=0.65, F=0.70, T=4.9%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_totassets_flag, 22))`: S=0.35, F=0.31, T=18.8%, INFERIOR (TOP3000)
- `rank(-1 * anl4_totassets_flag)`: S=-1.28, F=-1.27, T=3.0%, INFERIOR (TOP3000)
- `rank(-1 * anl4_totassets_flag / close)`: S=-0.03, F=-0.01, T=2.9%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 14F/18P
- LOW_FITNESS: 31F/1P
- LOW_SHARPE: 31F/1P
- LOW_SUB_UNIVERSE_SHARPE: 13F/16P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 1.27, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=1.64 (strong), ret=+9.7%
  - 2020: S=0.46 (weak), ret=+3.5%
  - 2021: S=1.66 (strong), ret=+20.8%
  - 2022: S=1.62 (strong), ret=+19.4%
  - 2023: S=0.89 (moderate), ret=+6.6%

## Risk & Drawdown
- Max drawdown: 11.60% over 174 days (recovered)
- Annualized: return +12.2%, volatility 9.6% (fraction of booksize)
- Hit rate: 53.0% positive days
- Tail shape: skew -0.56, excess kurtosis +6.20

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.46, max 2.97, latest 0.89

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2020
Best month: +7.29%; worst month: -4.02%
Positive months: 73%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=1.83
- Sideways: S=0.81
- Bear: S=1.03

## Negated Direction
Best negated: `rank(-1 * ts_delta(anl4_totassets_flag, 5))` S=0.56, F=0.44, INFERIOR
Direction gap: -0.72 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * anl4_totassets_flag)`: S=-1.28, F=-1.27, T=3.0%, INFERIOR (TOP3000)
- `rank(-1 * anl4_totassets_flag / close)`: S=-0.03, F=-0.01, T=2.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_totassets_flag, 5))`: S=0.56, F=0.44, T=34.0%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_totassets_flag)` | TOP3000 | 1.27 | 1.27 | 11.6% | 100% | all-weather |
| `rank(anl4_totassets_flag)` | TOP1000 | 0.69 | 0.77 | 32.0% | 80% | mixed |
| `rank(anl4_totassets_flag)` | TOP500 | 0.48 | 0.57 | 69.9% | 60% | mixed |
| `rank(anl4_totassets_flag / close)` | TOP200 | 0.31 | 0.16 | 22.0% | 60% | mixed |

## Correlation Notes
Top correlates:
- anl4_cff_flag: 0.912 (strongly positively correlated)
- anl4_cfi_flag: 0.911 (strongly positively correlated)
- anl4_cfo_flag: 0.847 (strongly positively correlated)
- anl4_fcf_flag: 0.811 (strongly positively correlated)
- anl4_fcfps_flag: 0.809 (strongly positively correlated)

Redundancy cluster #18: 7 similar fields, mean |rho| 0.818 (representative). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| rank(scl12_buzz * (-1 * returns)) | socialmedia12 | -0.22 | 2.31 | +0.69 | -0.90 | yes |
| rank(fnd6_acdo) * rank(-1 * returns) | unknown | -0.20 | 2.51 | +0.64 | -0.86 | yes |
| anl4_afv4_dts_spe | analyst4 | -0.32 | 1.94 | +0.67 | -0.38 | yes |
| rank(fnd6_acdo) + rank(open/close - 1) | unknown | -0.21 | 2.64 | +0.61 | -0.81 | yes |
| fn_comp_options_forfeitures_and_expirations_a | fundamental2 | -0.19 | 1.88 | +0.60 | -0.96 | yes |

## Actionability
Cataloged as active factor but not yet in submitted book.
Needs grade upgrade. Try decay_linear wrap, value normalization, or blend with complementary factor.
Untried templates: decay_linear, trade_when
