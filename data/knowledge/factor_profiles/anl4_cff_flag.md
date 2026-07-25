---
field: anl4_cff_flag
dataset: analyst4
best_template: decay_linear
best_sharpe: 1.14
best_fitness: 0.99
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 35
regime_profile: all-weather
n_variations_with_pnl: 8
max_drawdown: 0.1166
ann_vol: 0.084
hit_rate: 0.5352
rolling_sharpe_min: -0.329
rolling_sharpe_max: 2.332
top_merge_partner: fn_comp_options_forfeitures_and_expirations_a
redundancy_cluster: 18
negated_best_sharpe: 0.32
negated_best_template: rank_neg_delta
negated_best_fitness: 0.19
n_negated_sims: 10
direction_gap: -0.82
---
# anl4_cff_flag (analyst4)

*Cash Flow From Financing Activities - forecast type (revision/new/...)*

## Signal Profile
- `rank(anl4_cff_flag)`: S=1.13, F=0.98, T=2.9%, INFERIOR (TOP3000)
- `rank(anl4_cff_flag / close)`: S=0.21, F=0.09, T=3.4%, INFERIOR (TOP200)
- `rank(ts_delta(anl4_cff_flag, 5))`: S=0.71, F=0.86, T=16.2%, INFERIOR (TOP500)
- `ts_decay_linear(rank(anl4_cff_flag), 5)`: S=1.14, F=0.99, T=2.9%, INFERIOR (TOP3000)
- `-rank(anl4_cff_flag)`: S=-0.79, F=-0.79, T=4.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_cff_flag, 5))`: S=0.32, F=0.19, T=33.6%, INFERIOR (TOP3000)
- `-ts_zscore(anl4_cff_flag, 63)`: S=-0.07, F=-0.04, T=6.0%, INFERIOR (TOP3000)
- `ts_mean(anl4_cff_flag, 10)`: S=0.78, F=0.76, T=3.8%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_cff_flag, 22))`: S=0.22, F=0.16, T=19.3%, INFERIOR (TOP3000)
- `rank(-1 * anl4_cff_flag)`: S=-1.13, F=-0.98, T=2.9%, INFERIOR (TOP3000)
- `rank(-1 * anl4_cff_flag / close)`: S=0.07, F=0.02, T=2.8%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 15F/20P
- LOW_FITNESS: 35F/0P
- LOW_SHARPE: 35F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/19P

## Temporal Behavior
Headline (decay_linear): Overall Sharpe 1.13, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=1.91 (strong), ret=+10.3%
  - 2020: S=0.55 (moderate), ret=+3.8%
  - 2021: S=1.06 (moderate), ret=+11.4%
  - 2022: S=1.30 (moderate), ret=+13.4%
  - 2023: S=1.15 (moderate), ret=+7.6%

## Risk & Drawdown
- Max drawdown: 11.66% over 174 days (recovered)
- Annualized: return +9.5%, volatility 8.4% (fraction of booksize)
- Hit rate: 53.5% positive days
- Tail shape: skew -0.47, excess kurtosis +5.51

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.33, max 2.33, latest 1.29

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2020
Best month: +5.99%; worst month: -3.98%
Positive months: 68%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=1.49
- Sideways: S=1.28
- Bear: S=0.58

## Negated Direction
Best negated: `rank(-1 * ts_delta(anl4_cff_flag, 5))` S=0.32, F=0.19, INFERIOR
Direction gap: -0.82 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * anl4_cff_flag)`: S=-1.13, F=-0.98, T=2.9%, INFERIOR (TOP3000)
- `rank(-1 * anl4_cff_flag / close)`: S=0.07, F=0.02, T=2.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_cff_flag, 5))`: S=0.32, F=0.19, T=33.6%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `ts_decay_linear(rank(anl4_cff_flag), 5)` | TOP3000 | 1.13 | 0.99 | 11.7% | 100% | all-weather |
| `rank(anl4_cff_flag)` | TOP3000 | 1.13 | 0.98 | 11.7% | 100% | all-weather |
| `rank(ts_delta(anl4_cff_flag, 5))` | TOP500 | 0.71 | 0.86 | 51.7% | 100% | mixed |
| `rank(anl4_cff_flag)` | TOP1000 | 0.81 | 0.79 | 19.3% | 80% | all-weather |
| `rank(anl4_cff_flag)` | TOP500 | 0.44 | 0.38 | 41.6% | 60% | mixed |
| `rank(ts_delta(anl4_cff_flag, 5))` | TOP200 | 0.24 | 0.18 | 39.3% | 80% | bull-only |
| `rank(ts_delta(anl4_cff_flag, 5))` | TOP1000 | 0.23 | 0.15 | 91.7% | 40% | mixed |
| `rank(anl4_cff_flag / close)` | TOP200 | 0.21 | 0.09 | 25.5% | 80% | mixed |

## Correlation Notes
Top correlates:
- anl4_cfi_flag: 0.983 (strongly positively correlated)
- anl4_totassets_flag: 0.912 (strongly positively correlated)
- anl4_cfo_flag: 0.903 (strongly positively correlated)
- anl4_fcf_flag: 0.817 (strongly positively correlated)
- anl4_capex_flag: 0.802 (strongly positively correlated)

Redundancy cluster #18: 7 similar fields, mean |rho| 0.818 (representative: anl4_totassets_flag). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| fn_comp_options_forfeitures_and_expirations_a | fundamental2 | -0.17 | 1.75 | +0.58 | -0.78 | yes |
| rank(scl12_buzz * (-1 * returns)) | socialmedia12 | -0.17 | 2.15 | +0.53 | -0.65 | yes |
| rank(fnd6_acdo) * rank(-1 * returns) | unknown | -0.15 | 2.35 | +0.48 | -0.84 | yes |
| rank(fnd6_acdo) + rank(open/close - 1) | unknown | -0.17 | 2.49 | +0.47 | -0.82 | yes |
| fnd2_a_sbcpnargmpmtwopsffesip | fundamental2 | -0.22 | 1.57 | +0.44 | -0.73 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: trade_when
