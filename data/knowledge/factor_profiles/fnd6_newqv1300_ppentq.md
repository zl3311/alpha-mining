---
field: fnd6_newqv1300_ppentq
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 0.96
best_fitness: 0.77
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 8
max_drawdown: 0.0859
ann_vol: 0.0829
hit_rate: 0.4858
rolling_sharpe_min: -0.933
rolling_sharpe_max: 2.729
top_merge_partner: anl4_epsr_flag
redundancy_cluster: 1
negated_best_sharpe: 0.47
negated_best_template: rank_neg_delta
negated_best_fitness: 0.14
n_negated_sims: 10
direction_gap: -0.49
---
# fnd6_newqv1300_ppentq (fundamental6)

*Property Plant and Equipment - Total (Net)*

## Signal Profile
- `rank(fnd6_newqv1300_ppentq)`: S=0.79, F=0.67, T=1.9%, INFERIOR (TOP3000)
- `rank(fnd6_newqv1300_ppentq / close)`: S=0.96, F=0.77, T=2.2%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_newqv1300_ppentq, 5))`: S=0.23, F=0.07, T=37.6%, INFERIOR (TOP200)
- `-rank(fnd6_newqv1300_ppentq)`: S=-0.37, F=-0.23, T=2.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_ppentq, 5))`: S=0.47, F=0.14, T=38.2%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_newqv1300_ppentq, 63)`: S=0.35, F=0.11, T=19.3%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newqv1300_ppentq, 10)`: S=0.08, F=0.02, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newqv1300_ppentq, 22))`: S=-0.72, F=-0.33, T=17.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_ppentq)`: S=-0.37, F=-0.23, T=2.6%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_ppentq / close)`: S=-0.55, F=-0.37, T=2.8%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 9F/23P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 12F/17P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.96, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.16 (weak), ret=+0.8%
  - 2020: S=0.42 (weak), ret=+3.8%
  - 2021: S=1.80 (strong), ret=+20.6%
  - 2022: S=1.09 (moderate), ret=+8.1%
  - 2023: S=0.95 (moderate), ret=+5.6%

## Risk & Drawdown
- Max drawdown: 8.59% over 211 days (recovered)
- Annualized: return +7.9%, volatility 8.3% (fraction of booksize)
- Hit rate: 48.6% positive days
- Tail shape: skew +0.58, excess kurtosis +3.04

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.93, max 2.73, latest 1.04

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2019
Best month: +8.90%; worst month: -3.51%
Positive months: 58%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.82
- Sideways: S=0.20
- Bear: S=-0.68

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_newqv1300_ppentq, 5))` S=0.47, F=0.14, INFERIOR
Direction gap: -0.49 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_newqv1300_ppentq)`: S=-0.37, F=-0.23, T=2.6%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_ppentq / close)`: S=-0.55, F=-0.37, T=2.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_ppentq, 5))`: S=0.47, F=0.14, T=38.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newqv1300_ppentq / close)` | TOP3000 | 0.96 | 0.77 | 8.6% | 100% | bull-only |
| `rank(fnd6_newqv1300_ppentq)` | TOP3000 | 0.79 | 0.67 | 27.5% | 80% | bull-only |
| `rank(fnd6_newqv1300_ppentq / close)` | TOP1000 | 0.55 | 0.37 | 13.1% | 60% | bull-only |
| `rank(fnd6_newqv1300_ppentq / close)` | TOP500 | 0.39 | 0.24 | 24.4% | 80% | bull-only |
| `rank(fnd6_newqv1300_ppentq)` | TOP1000 | 0.36 | 0.23 | 34.4% | 80% | bull-only |
| `rank(fnd6_newqv1300_ppentq)` | TOP500 | 0.18 | 0.08 | 45.8% | 60% | bull-only |
| `rank(ts_delta(fnd6_newqv1300_ppentq, 5))` | TOP200 | 0.23 | 0.07 | 21.3% | 80% | weak |
| `rank(ts_delta(fnd6_newqv1300_ppentq, 5))` | TOP500 | 0.13 | 0.03 | 20.2% | 60% | weak |

## Correlation Notes
Top correlates:
- ppent: 1.000 (strongly positively correlated)
- fnd6_newa2v1300_ppent: 0.986 (strongly positively correlated)
- depre_amort: 0.977 (strongly positively correlated)
- fnd6_cptnewqv1300_dpq: 0.977 (strongly positively correlated)
- fnd6_cptmfmq_dpq: 0.977 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_epsr_flag | analyst4 | -0.33 | 1.85 | +0.67 | -0.68 | yes |
| rp_ess_revenue | news18 | -0.34 | 1.59 | +0.63 | -0.80 | yes |
| anl4_rd_exp_flag | analyst4 | -0.24 | 1.60 | +0.57 | -0.23 | yes |
| net_profit_adjusted_min_guidance | analyst4 | -0.18 | 1.49 | +0.53 | -0.67 | yes |
| max_gross_income_guidance_2 | analyst4 | -0.28 | 1.44 | +0.48 | -0.92 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
