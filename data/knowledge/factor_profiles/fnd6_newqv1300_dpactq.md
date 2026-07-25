---
field: fnd6_newqv1300_dpactq
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 1.3
best_fitness: 1.3
best_universe: TOP3000
grade: AVERAGE
submittability: needs_upgrade
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 7
max_drawdown: 0.1024
ann_vol: 0.0971
hit_rate: 0.5182
rolling_sharpe_min: -0.928
rolling_sharpe_max: 2.841
top_merge_partner: anl4_rd_exp_flag
redundancy_cluster: 12
negated_best_sharpe: 1.18
negated_best_template: rank_neg_delta
negated_best_fitness: 0.8
n_negated_sims: 10
direction_gap: -0.12
---
# fnd6_newqv1300_dpactq (fundamental6)

*Depreciation, Depletion and Amortization (Accumulated)*

## Signal Profile
- `rank(fnd6_newqv1300_dpactq)`: S=0.87, F=0.84, T=5.9%, INFERIOR (TOP3000)
- `rank(fnd6_newqv1300_dpactq / close)`: S=1.30, F=1.30, T=5.9%, AVERAGE (TOP3000)
- `rank(ts_delta(fnd6_newqv1300_dpactq, 5))`: S=-0.26, F=-0.07, T=43.5%, INFERIOR (TOP3000)
- `-rank(fnd6_newqv1300_dpactq)`: S=-0.62, F=-0.52, T=7.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_dpactq, 5))`: S=1.18, F=0.80, T=48.0%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_newqv1300_dpactq, 63)`: S=0.01, F=0.00, T=24.8%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newqv1300_dpactq, 10)`: S=0.33, F=0.17, T=3.4%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newqv1300_dpactq, 22))`: S=-0.50, F=-0.21, T=22.3%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_dpactq)`: S=-0.62, F=-0.52, T=7.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_dpactq / close)`: S=-0.88, F=-0.80, T=7.5%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 10F/22P
- LOW_FITNESS: 31F/1P
- LOW_SHARPE: 31F/1P
- LOW_SUB_UNIVERSE_SHARPE: 12F/17P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 1.29, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.91 (moderate), ret=+4.9%
  - 2020: S=0.10 (weak), ret=+1.0%
  - 2021: S=1.99 (strong), ret=+26.6%
  - 2022: S=1.99 (strong), ret=+21.6%
  - 2023: S=1.42 (moderate), ret=+7.2%

## Risk & Drawdown
- Max drawdown: 10.24% over 204 days (recovered)
- Annualized: return +12.5%, volatility 9.7% (fraction of booksize)
- Hit rate: 51.8% positive days
- Tail shape: skew +0.38, excess kurtosis +2.92

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.93, max 2.84, latest 1.36

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2020
Best month: +11.22%; worst month: -3.95%
Positive months: 73%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.44
- Sideways: S=0.54
- Bear: S=-0.80

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_newqv1300_dpactq, 5))` S=1.18, F=0.80, INFERIOR
Direction gap: -0.12 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_newqv1300_dpactq)`: S=-0.62, F=-0.52, T=7.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_dpactq / close)`: S=-0.88, F=-0.80, T=7.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_dpactq, 5))`: S=1.18, F=0.80, T=48.0%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newqv1300_dpactq / close)` | TOP3000 | 1.29 | 1.30 | 10.2% | 100% | bull-only |
| `rank(fnd6_newqv1300_dpactq)` | TOP3000 | 0.86 | 0.84 | 28.9% | 80% | bull-only |
| `rank(fnd6_newqv1300_dpactq / close)` | TOP1000 | 0.88 | 0.80 | 11.5% | 100% | bull-only |
| `rank(fnd6_newqv1300_dpactq)` | TOP1000 | 0.62 | 0.52 | 25.9% | 60% | bull-only |
| `rank(fnd6_newqv1300_dpactq / close)` | TOP500 | 0.63 | 0.47 | 16.2% | 80% | bull-only |
| `rank(fnd6_newqv1300_dpactq)` | TOP500 | 0.37 | 0.23 | 31.7% | 80% | bull-only |
| `rank(fnd6_newqv1300_dpactq / close)` | TOP200 | 0.19 | 0.09 | 22.9% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_newa1v1300_dpact: 0.961 (strongly positively correlated)
- fnd6_dpvieb: 0.960 (strongly positively correlated)
- fnd6_newqv1300_ppegtq: 0.957 (strongly positively correlated)
- fnd6_newa2v1300_ppegt: 0.940 (strongly positively correlated)
- fn_accum_depr_depletion_and_amortization_ppne_q: 0.939 (strongly positively correlated)

Redundancy cluster #12: 12 similar fields, mean |rho| 0.749 (representative: fnd6_dlto). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_rd_exp_flag | analyst4 | -0.40 | 2.10 | +0.81 | -0.76 | yes |
| anl4_epsr_flag | analyst4 | -0.30 | 2.08 | +0.80 | -0.63 | yes |
| rank(scl12_buzz * (-1 * returns)) | socialmedia12 | -0.24 | 2.35 | +0.73 | -0.41 | yes |
| rank(fnd6_acdo) * rank(-1 * returns) | unknown | -0.24 | 2.59 | +0.72 | -0.29 | yes |
| rp_ess_revenue | news18 | -0.36 | 1.93 | +0.64 | -0.86 | yes |

## Actionability
Already in submitted book (alpha: unknown).
Needs grade upgrade. Try decay_linear wrap, value normalization, or blend with complementary factor.
Untried templates: decay_linear, trade_when
