---
field: anl4_bvps_flag
dataset: analyst4
cluster: analyst4_balance_sheet_equity
coverage: 0.8223
community_alphas: 15619
best_template: rank_level
best_sharpe: 1.31
best_fitness: 1.2
best_universe: TOP3000
grade: AVERAGE
submittability: needs_upgrade
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 6
max_drawdown: 0.1702
ann_vol: 0.0809
hit_rate: 0.5206
rolling_sharpe_min: -2.383
rolling_sharpe_max: 3.17
top_merge_partner: rank(scl12_buzz * (-1 * returns))
redundancy_cluster: 13
negated_best_sharpe: 0.29
negated_best_template: neg_rank_level
negated_best_fitness: 0.26
n_negated_sims: 10
direction_gap: -1.02
---
# anl4_bvps_flag (analyst4)

*Book value per share - forecast type (revision/new/...)*

## Signal Profile
- `rank(anl4_bvps_flag)`: S=1.31, F=1.20, T=2.1%, AVERAGE (TOP3000)
- `rank(anl4_bvps_flag / close)`: S=0.09, F=0.03, T=3.1%, INFERIOR (TOP200)
- `rank(ts_delta(anl4_bvps_flag, 5))`: S=0.69, F=0.68, T=16.2%, INFERIOR (TOP500)
- `-rank(anl4_bvps_flag)`: S=-0.54, F=-0.45, T=3.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_bvps_flag, 5))`: S=0.27, F=0.19, T=10.4%, INFERIOR (TOP3000)
- `ts_zscore(anl4_bvps_flag, 22)`: S=0.16, F=0.09, T=2.5%, INFERIOR (TOP3000)
- `ts_mean(anl4_bvps_flag, 10)`: S=0.53, F=0.43, T=3.5%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_bvps_flag, 22))`: S=0.27, F=0.20, T=17.5%, INFERIOR (TOP3000)
- `rank(-1 * anl4_bvps_flag)`: S=0.29, F=0.26, T=4.3%, INFERIOR (TOP3000)
- `rank(-1 * anl4_bvps_flag / close)`: S=-0.09, F=-0.03, T=3.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 16F/16P
- LOW_FITNESS: 31F/1P
- LOW_SHARPE: 31F/1P
- LOW_SUB_UNIVERSE_SHARPE: 5F/15P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 1.30, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=1.88 (strong), ret=+7.5%
  - 2020: S=-1.25 (negative), ret=-6.3%
  - 2021: S=1.85 (strong), ret=+22.3%
  - 2022: S=2.48 (strong), ret=+24.8%
  - 2023: S=0.61 (moderate), ret=+3.4%

## Risk & Drawdown
- Max drawdown: 17.02% over 462 days (recovered)
- Annualized: return +10.5%, volatility 8.1% (fraction of booksize)
- Hit rate: 52.1% positive days
- Tail shape: skew +0.10, excess kurtosis +3.24

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.38, max 3.17, latest 0.39

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +7.08%; worst month: -4.83%
Positive months: 63%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.85
- Sideways: S=1.33
- Bear: S=-0.89

## Negated Direction
Best negated: `rank(-1 * anl4_bvps_flag)` S=0.29, F=0.26, INFERIOR
Direction gap: -1.02 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * anl4_bvps_flag)`: S=0.29, F=0.26, T=4.3%, INFERIOR (TOP3000)
- `rank(-1 * anl4_bvps_flag / close)`: S=-0.09, F=-0.03, T=3.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_bvps_flag, 5))`: S=0.27, F=0.19, T=10.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_bvps_flag)` | TOP3000 | 1.30 | 1.20 | 17.0% | 80% | bull-only |
| `rank(ts_delta(anl4_bvps_flag, 5))` | TOP500 | 0.69 | 0.68 | 28.8% | 80% | mixed |
| `rank(anl4_bvps_flag)` | TOP1000 | 0.53 | 0.45 | 37.8% | 60% | bull-only |
| `rank(anl4_bvps_flag)` | TOP500 | 0.30 | 0.23 | 73.6% | 60% | bull-only |
| `rank(ts_delta(anl4_bvps_flag, 5))` | TOP3000 | 0.29 | 0.15 | 42.3% | 60% | mixed |
| `rank(anl4_bvps_flag / close)` | TOP200 | 0.10 | 0.03 | 30.3% | 60% | mixed |

## Correlation Notes
Top correlates:
- rel_num_all: 0.880 (strongly positively correlated)
- rel_num_comp: 0.858 (strongly positively correlated)
- anl4_netdebt_flag: 0.856 (strongly positively correlated)
- rel_num_part: 0.856 (strongly positively correlated)
- anl4_ptpr_flag: 0.846 (strongly positively correlated)

Redundancy cluster #13: 127 similar fields, mean |rho| 0.82 (representative). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| rank(scl12_buzz * (-1 * returns)) | socialmedia12 | -0.34 | 2.55 | +0.93 | -0.76 | yes |
| rank(fnd6_acdo) + rank(open/close - 1) | unknown | -0.35 | 2.96 | +0.93 | -0.68 | yes |
| rank(fnd6_acdo) * rank(-1 * returns) | unknown | -0.33 | 2.74 | +0.87 | -0.73 | yes |
| anl4_afv4_dts_spe | analyst4 | -0.48 | 2.21 | +0.90 | -0.27 | yes |
| fn_comp_options_forfeitures_and_expirations_a | fundamental2 | -0.25 | 2.00 | +0.70 | -0.86 | yes |

## Actionability
Cataloged as active factor but not yet in submitted book.
Needs grade upgrade. Try decay_linear wrap, value normalization, or blend with complementary factor.
Untried templates: decay_linear, trade_when
