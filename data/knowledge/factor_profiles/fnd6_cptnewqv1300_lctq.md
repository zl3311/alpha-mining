---
field: fnd6_cptnewqv1300_lctq
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 0.96
best_fitness: 0.75
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 7
max_drawdown: 0.0899
ann_vol: 0.0806
hit_rate: 0.485
rolling_sharpe_min: -0.883
rolling_sharpe_max: 2.636
top_merge_partner: anl4_epsr_flag
redundancy_cluster: 1
negated_best_sharpe: 0.26
negated_best_template: rank_neg_delta
negated_best_fitness: 0.06
n_negated_sims: 10
direction_gap: -0.7
---
# fnd6_cptnewqv1300_lctq (fundamental6)

*Current Liabilities - Total*

## Signal Profile
- `rank(fnd6_cptnewqv1300_lctq)`: S=0.75, F=0.64, T=1.6%, INFERIOR (TOP3000)
- `rank(fnd6_cptnewqv1300_lctq / close)`: S=0.96, F=0.75, T=2.0%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_cptnewqv1300_lctq, 5))`: S=0.15, F=0.03, T=37.6%, INFERIOR (TOP200)
- `-rank(fnd6_cptnewqv1300_lctq)`: S=-0.35, F=-0.21, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_cptnewqv1300_lctq, 5))`: S=0.26, F=0.06, T=37.2%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_cptnewqv1300_lctq, 22)`: S=0.23, F=0.06, T=38.5%, INFERIOR (TOP3000)
- `ts_mean(fnd6_cptnewqv1300_lctq, 10)`: S=0.09, F=0.03, T=1.3%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_cptnewqv1300_lctq, 22))`: S=0.18, F=0.04, T=16.6%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_cptnewqv1300_lctq)`: S=-0.35, F=-0.21, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_cptnewqv1300_lctq / close)`: S=-0.54, F=-0.36, T=2.5%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 9F/23P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 10F/19P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.95, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.02 (weak), ret=+0.1%
  - 2020: S=0.33 (weak), ret=+2.9%
  - 2021: S=1.77 (strong), ret=+18.8%
  - 2022: S=1.48 (moderate), ret=+11.6%
  - 2023: S=0.79 (moderate), ret=+4.2%

## Risk & Drawdown
- Max drawdown: 8.99% over 491 days (recovered)
- Annualized: return +7.7%, volatility 8.1% (fraction of booksize)
- Hit rate: 48.5% positive days
- Tail shape: skew +0.48, excess kurtosis +2.32

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.88, max 2.64, latest 0.88

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2019
Best month: +9.29%; worst month: -4.17%
Positive months: 58%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.10
- Sideways: S=0.17
- Bear: S=-0.98

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_cptnewqv1300_lctq, 5))` S=0.26, F=0.06, INFERIOR
Direction gap: -0.70 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_cptnewqv1300_lctq)`: S=-0.35, F=-0.21, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_cptnewqv1300_lctq / close)`: S=-0.54, F=-0.36, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_cptnewqv1300_lctq, 5))`: S=0.26, F=0.06, T=37.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_cptnewqv1300_lctq / close)` | TOP3000 | 0.95 | 0.75 | 9.0% | 100% | bull-only |
| `rank(fnd6_cptnewqv1300_lctq)` | TOP3000 | 0.75 | 0.64 | 30.0% | 80% | bull-only |
| `rank(fnd6_cptnewqv1300_lctq / close)` | TOP1000 | 0.53 | 0.36 | 13.8% | 60% | bull-only |
| `rank(fnd6_cptnewqv1300_lctq)` | TOP1000 | 0.35 | 0.21 | 35.4% | 60% | bull-only |
| `rank(fnd6_cptnewqv1300_lctq / close)` | TOP500 | 0.29 | 0.15 | 22.8% | 60% | bull-only |
| `rank(fnd6_cptnewqv1300_lctq)` | TOP500 | 0.09 | 0.03 | 50.9% | 60% | bull-only |
| `rank(ts_delta(fnd6_cptnewqv1300_lctq, 5))` | TOP200 | 0.16 | 0.03 | 36.0% | 80% | mixed |

## Correlation Notes
Top correlates:
- liabilities_curr: 1.000 (strongly positively correlated)
- fnd6_cptmfmq_lctq: 1.000 (strongly positively correlated)
- fnd6_newa1v1300_lct: 0.989 (strongly positively correlated)
- fnd6_newqv1300_ltmibq: 0.975 (strongly positively correlated)
- liabilities: 0.975 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_epsr_flag | analyst4 | -0.33 | 1.84 | +0.66 | -0.65 | yes |
| rp_ess_revenue | news18 | -0.33 | 1.57 | +0.62 | -0.75 | yes |
| net_profit_adjusted_min_guidance | analyst4 | -0.16 | 1.47 | +0.51 | -0.69 | yes |
| anl4_rd_exp_flag | analyst4 | -0.20 | 1.56 | +0.53 | -0.34 | yes |
| max_gross_income_guidance_2 | analyst4 | -0.27 | 1.43 | +0.47 | -0.91 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
