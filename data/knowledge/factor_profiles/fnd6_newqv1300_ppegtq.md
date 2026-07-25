---
field: fnd6_newqv1300_ppegtq
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 1.26
best_fitness: 1.21
best_universe: TOP3000
grade: AVERAGE
submittability: needs_upgrade
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 7
max_drawdown: 0.0978
ann_vol: 0.0919
hit_rate: 0.5028
rolling_sharpe_min: -0.859
rolling_sharpe_max: 2.85
top_merge_partner: anl4_epsr_flag
redundancy_cluster: 1
negated_best_sharpe: 0.73
negated_best_template: rank_neg_delta
negated_best_fitness: 0.37
n_negated_sims: 10
direction_gap: -0.53
---
# fnd6_newqv1300_ppegtq (fundamental6)

*Property, Plant and Equipment - Total (Gross) - Quarterly*

## Signal Profile
- `rank(fnd6_newqv1300_ppegtq)`: S=0.91, F=0.88, T=5.9%, INFERIOR (TOP3000)
- `rank(fnd6_newqv1300_ppegtq / close)`: S=1.26, F=1.21, T=6.0%, AVERAGE (TOP3000)
- `rank(ts_delta(fnd6_newqv1300_ppegtq, 5))`: S=0.06, F=0.01, T=44.2%, INFERIOR (TOP3000)
- `-rank(fnd6_newqv1300_ppegtq)`: S=-0.63, F=-0.52, T=7.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_ppegtq, 5))`: S=0.73, F=0.37, T=51.5%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_newqv1300_ppegtq, 22)`: S=0.27, F=0.09, T=43.2%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newqv1300_ppegtq, 10)`: S=0.40, F=0.22, T=3.5%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newqv1300_ppegtq, 22))`: S=0.04, F=0.00, T=22.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_ppegtq)`: S=-0.39, F=-0.25, T=8.6%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_ppegtq / close)`: S=-0.63, F=-0.46, T=8.5%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 10F/22P
- LOW_FITNESS: 31F/1P
- LOW_SHARPE: 31F/1P
- LOW_SUB_UNIVERSE_SHARPE: 14F/15P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 1.26, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.78 (moderate), ret=+4.4%
  - 2020: S=0.42 (weak), ret=+4.3%
  - 2021: S=2.02 (strong), ret=+25.4%
  - 2022: S=1.67 (strong), ret=+14.3%
  - 2023: S=1.37 (moderate), ret=+8.3%

## Risk & Drawdown
- Max drawdown: 9.78% over 204 days (recovered)
- Annualized: return +11.6%, volatility 9.2% (fraction of booksize)
- Hit rate: 50.3% positive days
- Tail shape: skew +0.50, excess kurtosis +2.78

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.86, max 2.85, latest 1.41

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2020
Best month: +10.38%; worst month: -3.93%
Positive months: 63%

## Regime Profile
Regime profile: **mixed**
- Bull: S=3.13
- Sideways: S=0.40
- Bear: S=-0.27

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_newqv1300_ppegtq, 5))` S=0.73, F=0.37, INFERIOR
Direction gap: -0.53 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_newqv1300_ppegtq)`: S=-0.39, F=-0.25, T=8.6%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_ppegtq / close)`: S=-0.63, F=-0.46, T=8.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_ppegtq, 5))`: S=0.73, F=0.37, T=51.5%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newqv1300_ppegtq / close)` | TOP3000 | 1.26 | 1.21 | 9.8% | 100% | mixed |
| `rank(fnd6_newqv1300_ppegtq)` | TOP3000 | 0.91 | 0.88 | 26.3% | 80% | bull-only |
| `rank(fnd6_newqv1300_ppegtq / close)` | TOP1000 | 0.88 | 0.78 | 10.4% | 80% | bull-only |
| `rank(fnd6_newqv1300_ppegtq)` | TOP1000 | 0.63 | 0.52 | 26.8% | 80% | bull-only |
| `rank(fnd6_newqv1300_ppegtq / close)` | TOP500 | 0.63 | 0.46 | 15.8% | 80% | bull-only |
| `rank(fnd6_newqv1300_ppegtq)` | TOP500 | 0.39 | 0.25 | 32.2% | 80% | bull-only |
| `rank(fnd6_newqv1300_ppegtq / close)` | TOP200 | 0.18 | 0.08 | 22.0% | 80% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_newqv1300_dpactq: 0.957 (strongly positively correlated)
- fnd6_newa2v1300_ppegt: 0.951 (strongly positively correlated)
- fnd6_ppeveb: 0.950 (strongly positively correlated)
- fnd6_newqv1300_ppentq: 0.950 (strongly positively correlated)
- ppent: 0.950 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_epsr_flag | analyst4 | -0.32 | 2.08 | +0.82 | -0.69 | yes |
| anl4_rd_exp_flag | analyst4 | -0.30 | 1.92 | +0.66 | -0.59 | yes |
| rp_ess_revenue | news18 | -0.34 | 1.86 | +0.60 | -0.89 | yes |
| rank(scl12_buzz * (-1 * returns)) | socialmedia12 | -0.17 | 2.24 | +0.61 | -0.34 | yes |
| implied_volatility_put_10 | option8 | -0.08 | 1.87 | +0.58 | -0.63 | yes |

## Actionability
Cataloged as active factor but not yet in submitted book.
Needs grade upgrade. Try decay_linear wrap, value normalization, or blend with complementary factor.
Untried templates: decay_linear, trade_when
