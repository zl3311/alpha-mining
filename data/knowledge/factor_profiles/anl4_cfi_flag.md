---
field: anl4_cfi_flag
dataset: analyst4
best_template: rank_level
best_sharpe: 1.18
best_fitness: 1.07
best_universe: TOP3000
grade: AVERAGE
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: all-weather
n_variations_with_pnl: 8
max_drawdown: 0.1002
ann_vol: 0.0872
hit_rate: 0.532
rolling_sharpe_min: -0.104
rolling_sharpe_max: 2.291
top_merge_partner: fn_comp_options_forfeitures_and_expirations_a
redundancy_cluster: 18
negated_best_sharpe: 0.25
negated_best_template: rank_neg_delta
negated_best_fitness: 0.13
n_negated_sims: 10
direction_gap: -0.93
---
# anl4_cfi_flag (analyst4)

*Cash Flow From Investing - forecast type (revision/new/...)*

## Signal Profile
- `rank(anl4_cfi_flag)`: S=1.18, F=1.07, T=2.9%, AVERAGE (TOP3000)
- `rank(anl4_cfi_flag / close)`: S=0.33, F=0.18, T=3.4%, INFERIOR (TOP200)
- `rank(ts_delta(anl4_cfi_flag, 5))`: S=0.65, F=0.76, T=11.8%, INFERIOR (TOP200)
- `-rank(anl4_cfi_flag)`: S=-0.82, F=-0.82, T=4.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_cfi_flag, 5))`: S=0.25, F=0.13, T=33.4%, INFERIOR (TOP3000)
- `-ts_zscore(anl4_cfi_flag, 63)`: S=-0.05, F=-0.02, T=6.6%, INFERIOR (TOP3000)
- `ts_mean(anl4_cfi_flag, 10)`: S=0.81, F=0.80, T=3.9%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_cfi_flag, 22))`: S=0.27, F=0.22, T=18.2%, INFERIOR (TOP3000)
- `rank(-1 * anl4_cfi_flag)`: S=-1.18, F=-1.07, T=2.9%, INFERIOR (TOP3000)
- `rank(-1 * anl4_cfi_flag / close)`: S=0.09, F=0.03, T=2.7%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 14F/18P
- LOW_FITNESS: 31F/1P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 12F/17P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 1.17, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=1.60 (strong), ret=+9.1%
  - 2020: S=0.72 (moderate), ret=+5.3%
  - 2021: S=1.08 (moderate), ret=+12.0%
  - 2022: S=1.40 (moderate), ret=+14.6%
  - 2023: S=1.31 (moderate), ret=+9.0%

## Risk & Drawdown
- Max drawdown: 10.02% over 181 days (recovered)
- Annualized: return +10.2%, volatility 8.7% (fraction of booksize)
- Hit rate: 53.2% positive days
- Tail shape: skew -0.42, excess kurtosis +4.82

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.10, max 2.29, latest 1.45

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2020
Best month: +6.18%; worst month: -4.23%
Positive months: 73%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=1.60
- Sideways: S=1.23
- Bear: S=0.63

## Negated Direction
Best negated: `rank(-1 * ts_delta(anl4_cfi_flag, 5))` S=0.25, F=0.13, INFERIOR
Direction gap: -0.93 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * anl4_cfi_flag)`: S=-1.18, F=-1.07, T=2.9%, INFERIOR (TOP3000)
- `rank(-1 * anl4_cfi_flag / close)`: S=0.09, F=0.03, T=2.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_cfi_flag, 5))`: S=0.25, F=0.13, T=33.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_cfi_flag)` | TOP3000 | 1.17 | 1.07 | 10.0% | 100% | all-weather |
| `rank(anl4_cfi_flag)` | TOP1000 | 0.83 | 0.82 | 17.7% | 80% | all-weather |
| `rank(ts_delta(anl4_cfi_flag, 5))` | TOP200 | 0.64 | 0.76 | 33.3% | 80% | bull-only |
| `rank(ts_delta(anl4_cfi_flag, 5))` | TOP500 | 0.64 | 0.71 | 60.8% | 80% | mixed |
| `rank(anl4_cfi_flag)` | TOP500 | 0.64 | 0.65 | 36.5% | 60% | mixed |
| `rank(anl4_cfi_flag / close)` | TOP200 | 0.33 | 0.18 | 23.3% | 60% | mixed |
| `rank(ts_delta(anl4_cfi_flag, 5))` | TOP1000 | 0.20 | 0.11 | 94.8% | 60% | weak |
| `rank(anl4_cfi_flag)` | TOP200 | 0.06 | 0.03 | 68.8% | 60% | bull-only |

## Correlation Notes
Top correlates:
- anl4_cff_flag: 0.983 (strongly positively correlated)
- anl4_totassets_flag: 0.911 (strongly positively correlated)
- anl4_cfo_flag: 0.904 (strongly positively correlated)
- anl4_fcf_flag: 0.810 (strongly positively correlated)
- anl4_capex_flag: 0.800 (strongly positively correlated)

Redundancy cluster #18: 7 similar fields, mean |rho| 0.818 (representative: anl4_totassets_flag). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| fn_comp_options_forfeitures_and_expirations_a | fundamental2 | -0.17 | 1.78 | +0.61 | -0.67 | yes |
| anl4_afv4_dts_spe | analyst4 | -0.26 | 1.77 | +0.60 | +0.38 | yes |
| anl4_rd_exp_flag | analyst4 | -0.17 | 1.68 | +0.51 | -0.90 | yes |
| rank(scl12_buzz * (-1 * returns)) | socialmedia12 | -0.17 | 2.18 | +0.55 | -0.49 | yes |
| rank(fnd6_acdo) * rank(-1 * returns) | unknown | -0.15 | 2.38 | +0.51 | -0.67 | yes |

## Actionability
Cataloged as active factor but not yet in submitted book.
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
