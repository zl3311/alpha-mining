---
field: fnd6_newqv1300_invtq
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 0.83
best_fitness: 0.55
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 8
max_drawdown: 0.0791
ann_vol: 0.0671
hit_rate: 0.4964
rolling_sharpe_min: -0.943
rolling_sharpe_max: 2.421
top_merge_partner: rp_ess_revenue
redundancy_cluster: 1
negated_best_sharpe: 0.41
negated_best_template: rank_neg_delta
negated_best_fitness: 0.1
n_negated_sims: 10
direction_gap: -0.42
---
# fnd6_newqv1300_invtq (fundamental6)

*Inventories - Total*

## Signal Profile
- `rank(fnd6_newqv1300_invtq)`: S=0.62, F=0.41, T=1.9%, INFERIOR (TOP3000)
- `rank(fnd6_newqv1300_invtq / close)`: S=0.83, F=0.55, T=2.1%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_newqv1300_invtq, 5))`: S=0.50, F=0.20, T=37.5%, INFERIOR (TOP500)
- `-rank(fnd6_newqv1300_invtq)`: S=-0.24, F=-0.11, T=2.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_invtq, 5))`: S=0.41, F=0.10, T=37.7%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_newqv1300_invtq, 63)`: S=0.28, F=0.07, T=19.6%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newqv1300_invtq, 10)`: S=0.17, F=0.06, T=3.2%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newqv1300_invtq, 22))`: S=-0.06, F=-0.01, T=17.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_invtq)`: S=-0.62, F=-0.41, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_invtq / close)`: S=-0.83, F=-0.55, T=2.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 6F/26P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 9F/20P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.82, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.04 (weak), ret=+0.2%
  - 2020: S=0.13 (weak), ret=+0.9%
  - 2021: S=1.55 (strong), ret=+13.7%
  - 2022: S=1.31 (moderate), ret=+10.0%
  - 2023: S=0.52 (moderate), ret=+2.2%

## Risk & Drawdown
- Max drawdown: 7.91% over 371 days (recovered)
- Annualized: return +5.5%, volatility 6.7% (fraction of booksize)
- Hit rate: 49.6% positive days
- Tail shape: skew +0.05, excess kurtosis +1.69

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.94, max 2.42, latest 0.43

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2019
Best month: +7.24%; worst month: -3.38%
Positive months: 58%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.54
- Sideways: S=-0.05
- Bear: S=-1.71

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_newqv1300_invtq, 5))` S=0.41, F=0.10, INFERIOR
Direction gap: -0.42 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_newqv1300_invtq)`: S=-0.62, F=-0.41, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_invtq / close)`: S=-0.83, F=-0.55, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_invtq, 5))`: S=0.41, F=0.10, T=37.7%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newqv1300_invtq / close)` | TOP3000 | 0.82 | 0.55 | 7.9% | 100% | bull-only |
| `rank(fnd6_newqv1300_invtq)` | TOP3000 | 0.61 | 0.41 | 20.6% | 80% | bull-only |
| `rank(fnd6_newqv1300_invtq / close)` | TOP500 | 0.43 | 0.24 | 13.4% | 80% | bull-only |
| `rank(ts_delta(fnd6_newqv1300_invtq, 5))` | TOP500 | 0.52 | 0.20 | 12.8% | 60% | all-weather |
| `rank(fnd6_newqv1300_invtq)` | TOP500 | 0.34 | 0.18 | 22.2% | 80% | bull-only |
| `rank(fnd6_newqv1300_invtq / close)` | TOP1000 | 0.32 | 0.15 | 11.8% | 80% | bull-only |
| `rank(fnd6_newqv1300_invtq)` | TOP1000 | 0.23 | 0.11 | 23.8% | 60% | bull-only |
| `rank(ts_delta(fnd6_newqv1300_invtq, 5))` | TOP200 | 0.26 | 0.08 | 29.8% | 40% | mixed |

## Correlation Notes
Top correlates:
- inventory: 1.000 (strongly positively correlated)
- fnd6_newa1v1300_invt: 0.987 (strongly positively correlated)
- fnd6_invfg: 0.923 (strongly positively correlated)
- revenue: 0.919 (strongly positively correlated)
- fnd6_newqv1300_revtq: 0.919 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| rp_ess_revenue | news18 | -0.30 | 1.41 | +0.52 | -0.80 | yes |
| anl4_rd_exp_flag | analyst4 | -0.34 | 1.57 | +0.55 | -0.43 | yes |
| max_gross_income_guidance_2 | analyst4 | -0.29 | 1.31 | +0.49 | -0.85 | yes |
| max_adjusted_net_profit_guidance | analyst4 | -0.27 | 1.32 | +0.50 | -0.66 | yes |
| net_profit_adjusted_min_guidance | analyst4 | -0.24 | 1.43 | +0.48 | -0.76 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
