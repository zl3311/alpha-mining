---
field: anl4_epsr_flag
dataset: analyst4
best_template: ts_mean
best_sharpe: 1.22
best_fitness: 1.61
best_universe: TOP3000
grade: GOOD
submittability: blocked_LOW_SHARPE
n_sims: 35
regime_profile: mixed
n_variations_with_pnl: 7
max_drawdown: 0.1316
ann_vol: 0.0992
hit_rate: 0.5336
rolling_sharpe_min: -0.172
rolling_sharpe_max: 3.29
top_merge_partner: fnd6_cptmfmq_dlttq
negated_best_sharpe: 0.58
negated_best_template: neg_rank_level
negated_best_fitness: 0.29
n_negated_sims: 10
direction_gap: -0.64
---
# anl4_epsr_flag (analyst4)

*GAAP Earnings - estimation type (revision/new/...), per share*

## Signal Profile
- `rank(anl4_epsr_flag)`: S=1.19, F=1.15, T=4.0%, AVERAGE (TOP500)
- `rank(anl4_epsr_flag / close)`: S=0.32, F=0.17, T=2.5%, INFERIOR (TOP200)
- `rank(ts_delta(anl4_epsr_flag, 5))`: S=0.14, F=0.05, T=34.0%, INFERIOR (TOP500)
- `ts_decay_linear(rank(anl4_epsr_flag), 5)`: S=-0.55, F=-0.27, T=2.9%, INFERIOR (TOP3000)
- `-rank(anl4_epsr_flag)`: S=-0.53, F=-0.30, T=3.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_epsr_flag, 5))`: S=0.09, F=0.02, T=37.7%, INFERIOR (TOP3000)
- `-ts_zscore(anl4_epsr_flag, 63)`: S=0.12, F=0.05, T=18.1%, INFERIOR (TOP3000)
- `ts_mean(anl4_epsr_flag, 10)`: S=1.22, F=1.61, T=5.6%, GOOD (TOP3000)
- `rank(ts_rank(anl4_epsr_flag, 22))`: S=0.44, F=0.28, T=17.0%, INFERIOR (TOP3000)
- `rank(-1 * anl4_epsr_flag)`: S=0.58, F=0.29, T=3.0%, INFERIOR (TOP3000)
- `rank(-1 * anl4_epsr_flag / close)`: S=0.02, F=0.00, T=1.8%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 14F/21P
- LOW_FITNESS: 33F/2P
- LOW_SHARPE: 35F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/19P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 1.18, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=1.21 (moderate), ret=+8.2%
  - 2020: S=1.65 (strong), ret=+18.6%
  - 2021: S=0.50 (moderate), ret=+6.1%
  - 2022: S=1.21 (moderate), ret=+11.6%
  - 2023: S=1.67 (strong), ret=+12.8%

## Risk & Drawdown
- Max drawdown: 13.16% over 194 days (recovered)
- Annualized: return +11.7%, volatility 9.9% (fraction of booksize)
- Hit rate: 53.4% positive days
- Tail shape: skew -0.06, excess kurtosis +1.66

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.17, max 3.29, latest 1.58

## Yearly & Monthly Returns
Best year (by Sharpe): 2023; worst year: 2021
Best month: +5.82%; worst month: -7.91%
Positive months: 64%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.45
- Sideways: S=2.04
- Bear: S=1.15

## Negated Direction
Best negated: `rank(-1 * anl4_epsr_flag)` S=0.58, F=0.29, INFERIOR
Direction gap: -0.64 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * anl4_epsr_flag)`: S=0.58, F=0.29, T=3.0%, INFERIOR (TOP3000)
- `rank(-1 * anl4_epsr_flag / close)`: S=0.02, F=0.00, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_epsr_flag, 5))`: S=0.09, F=0.02, T=37.7%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_epsr_flag)` | TOP500 | 1.18 | 1.15 | 13.2% | 100% | mixed |
| `rank(anl4_epsr_flag)` | TOP1000 | 0.53 | 0.30 | 17.3% | 80% | bear-only |
| `rank(anl4_epsr_flag)` | TOP200 | 0.28 | 0.18 | 34.5% | 40% | weak |
| `rank(anl4_epsr_flag / close)` | TOP200 | 0.33 | 0.17 | 18.3% | 80% | mixed |
| `rank(anl4_epsr_flag / close)` | TOP500 | 0.17 | 0.06 | 28.5% | 60% | bear-only |
| `rank(ts_delta(anl4_epsr_flag, 5))` | TOP500 | 0.14 | 0.05 | 74.8% | 80% | weak |
| `rank(ts_delta(anl4_epsr_flag, 5))` | TOP200 | 0.11 | 0.04 | 32.4% | 40% | mixed |

## Correlation Notes
Top correlates:
- anl4_adjusted_netincome_ft: 0.560 (moderately positively correlated)
- fn_interest_paid_net_a: -0.388 (weakly negatively correlated)
- fn_comp_options_exercises_weighted_avg_a: -0.387 (weakly negatively correlated)
- fn_op_lease_rent_exp_a: -0.386 (weakly negatively correlated)
- fnd6_optprcex: -0.385 (weakly negatively correlated)

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| fnd6_cptmfmq_dlttq | fundamental6 | -0.36 | 2.07 | +0.89 | -0.84 | yes |
| debt_lt | fundamental6 | -0.36 | 2.08 | +0.88 | -0.84 | yes |
| fnd6_cptnewqv1300_dlttq | fundamental6 | -0.36 | 2.08 | +0.88 | -0.84 | yes |
| fnd6_newa1v1300_dltt | fundamental6 | -0.36 | 2.07 | +0.87 | -0.71 | yes |
| fnd6_dd1q | fundamental6 | -0.35 | 1.98 | +0.81 | -0.96 | yes |

## Actionability
Cataloged as active factor but not yet in submitted book.
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: trade_when
