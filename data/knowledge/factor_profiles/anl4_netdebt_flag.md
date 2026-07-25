---
field: anl4_netdebt_flag
dataset: analyst4
cluster: analyst4_balance_sheet_liab
coverage: 0.8602
community_alphas: 13084
best_template: rank_level
best_sharpe: 1.28
best_fitness: 1.11
best_universe: TOP3000
grade: AVERAGE
submittability: needs_upgrade
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 4
max_drawdown: 0.1975
ann_vol: 0.0741
hit_rate: 0.5279
rolling_sharpe_min: -2.684
rolling_sharpe_max: 3.421
top_merge_partner: rank(scl12_buzz * (-1 * returns))
redundancy_cluster: 13
negated_best_sharpe: 0.88
negated_best_template: rank_neg_delta
negated_best_fitness: 0.96
n_negated_sims: 10
direction_gap: -0.4
---
# anl4_netdebt_flag (analyst4)

*Net debt - forecast type (revision/new/...)*

## Signal Profile
- `rank(anl4_netdebt_flag)`: S=1.28, F=1.11, T=2.2%, AVERAGE (TOP3000)
- `rank(anl4_netdebt_flag / close)`: S=0.30, F=0.17, T=3.9%, INFERIOR (TOP200)
- `rank(ts_delta(anl4_netdebt_flag, 5))`: S=-0.16, F=-0.06, T=32.6%, INFERIOR (TOP3000)
- `-rank(anl4_netdebt_flag)`: S=-0.44, F=-0.33, T=3.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_netdebt_flag, 5))`: S=0.88, F=0.96, T=20.7%, INFERIOR (TOP3000)
- `-ts_zscore(anl4_netdebt_flag, 63)`: S=0.15, F=0.11, T=5.6%, INFERIOR (TOP3000)
- `ts_mean(anl4_netdebt_flag, 10)`: S=0.43, F=0.32, T=3.4%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_netdebt_flag, 22))`: S=-0.37, F=-0.34, T=18.3%, INFERIOR (TOP3000)
- `rank(-1 * anl4_netdebt_flag)`: S=-0.48, F=-0.43, T=3.8%, INFERIOR (TOP3000)
- `rank(-1 * anl4_netdebt_flag / close)`: S=0.12, F=0.04, T=3.6%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 17F/15P
- LOW_FITNESS: 31F/1P
- LOW_SHARPE: 31F/1P
- LOW_SUB_UNIVERSE_SHARPE: 13F/16P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 1.28, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=1.09 (moderate), ret=+4.5%
  - 2020: S=-1.39 (negative), ret=-7.0%
  - 2021: S=1.80 (strong), ret=+18.8%
  - 2022: S=2.88 (strong), ret=+25.5%
  - 2023: S=0.77 (moderate), ret=+4.5%

## Risk & Drawdown
- Max drawdown: 19.75% over 713 days (recovered)
- Annualized: return +9.4%, volatility 7.4% (fraction of booksize)
- Hit rate: 52.8% positive days
- Tail shape: skew +0.02, excess kurtosis +2.88

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.68, max 3.42, latest 0.63

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +7.33%; worst month: -4.38%
Positive months: 64%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.82
- Sideways: S=1.60
- Bear: S=-0.98

## Negated Direction
Best negated: `rank(-1 * ts_delta(anl4_netdebt_flag, 5))` S=0.88, F=0.96, INFERIOR
Direction gap: -0.40 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * anl4_netdebt_flag)`: S=-0.48, F=-0.43, T=3.8%, INFERIOR (TOP3000)
- `rank(-1 * anl4_netdebt_flag / close)`: S=0.12, F=0.04, T=3.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_netdebt_flag, 5))`: S=0.88, F=0.96, T=20.7%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_netdebt_flag)` | TOP3000 | 1.28 | 1.11 | 19.8% | 80% | bull-only |
| `rank(anl4_netdebt_flag)` | TOP500 | 0.49 | 0.43 | 66.0% | 60% | bull-only |
| `rank(anl4_netdebt_flag)` | TOP1000 | 0.44 | 0.33 | 52.8% | 60% | bull-only |
| `rank(anl4_netdebt_flag / close)` | TOP200 | 0.30 | 0.17 | 24.4% | 60% | mixed |

## Correlation Notes
Top correlates:
- anl4_bvps_flag: 0.856 (strongly positively correlated)
- rel_num_all: 0.834 (strongly positively correlated)
- anl4_ptpr_flag: 0.814 (strongly positively correlated)
- rel_num_comp: 0.813 (strongly positively correlated)
- pv13_com_page_rank: 0.811 (strongly positively correlated)

Redundancy cluster #13: 127 similar fields, mean |rho| 0.82 (representative: anl4_bvps_flag). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| rank(scl12_buzz * (-1 * returns)) | socialmedia12 | -0.31 | 2.48 | +0.85 | -0.60 | yes |
| rank(fnd6_acdo) + rank(open/close - 1) | unknown | -0.33 | 2.87 | +0.85 | -0.46 | yes |
| anl4_afv4_dts_spe | analyst4 | -0.46 | 2.11 | +0.83 | -0.33 | yes |
| rank(fnd6_acdo) * rank(-1 * returns) | unknown | -0.30 | 2.66 | +0.79 | -0.52 | yes |
| fn_comp_options_forfeitures_and_expirations_a | fundamental2 | -0.24 | 1.98 | +0.71 | -0.69 | yes |

## Actionability
Cataloged as active factor but not yet in submitted book.
Needs grade upgrade. Try decay_linear wrap, value normalization, or blend with complementary factor.
Untried templates: decay_linear, trade_when
