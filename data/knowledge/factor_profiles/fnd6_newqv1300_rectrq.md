---
field: fnd6_newqv1300_rectrq
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 0.99
best_fitness: 0.83
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 6
max_drawdown: 0.1145
ann_vol: 0.0889
hit_rate: 0.4899
rolling_sharpe_min: -1.417
rolling_sharpe_max: 2.789
top_merge_partner: anl4_rd_exp_flag
redundancy_cluster: 1
negated_best_sharpe: 0.79
negated_best_template: rank_neg_delta
negated_best_fitness: 0.32
n_negated_sims: 10
direction_gap: -0.2
---
# fnd6_newqv1300_rectrq (fundamental6)

*Receivables - Trade*

## Signal Profile
- `rank(fnd6_newqv1300_rectrq)`: S=0.76, F=0.67, T=2.0%, INFERIOR (TOP3000)
- `rank(fnd6_newqv1300_rectrq / close)`: S=0.99, F=0.83, T=2.3%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_newqv1300_rectrq, 5))`: S=-0.25, F=-0.08, T=39.4%, INFERIOR (TOP200)
- `-rank(fnd6_newqv1300_rectrq)`: S=-0.43, F=-0.31, T=3.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_rectrq, 5))`: S=0.79, F=0.32, T=38.3%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_newqv1300_rectrq, 22)`: S=-0.01, F=0.00, T=39.9%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newqv1300_rectrq, 10)`: S=0.36, F=0.20, T=2.7%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newqv1300_rectrq, 22))`: S=-0.25, F=-0.07, T=17.3%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_rectrq)`: S=-0.43, F=-0.31, T=3.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_rectrq / close)`: S=-0.71, F=-0.57, T=3.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 10F/22P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 12F/17P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.98, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.19 (weak), ret=+0.9%
  - 2020: S=-0.29 (negative), ret=-2.8%
  - 2021: S=1.88 (strong), ret=+23.1%
  - 2022: S=1.84 (strong), ret=+17.4%
  - 2023: S=0.86 (moderate), ret=+3.9%

## Risk & Drawdown
- Max drawdown: 11.45% over 483 days (recovered)
- Annualized: return +8.7%, volatility 8.9% (fraction of booksize)
- Hit rate: 49.0% positive days
- Tail shape: skew +0.37, excess kurtosis +2.88

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.42, max 2.79, latest 0.84

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2020
Best month: +9.75%; worst month: -3.63%
Positive months: 56%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.61
- Sideways: S=0.28
- Bear: S=-1.78

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_newqv1300_rectrq, 5))` S=0.79, F=0.32, INFERIOR
Direction gap: -0.20 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_newqv1300_rectrq)`: S=-0.43, F=-0.31, T=3.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_rectrq / close)`: S=-0.71, F=-0.57, T=3.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_rectrq, 5))`: S=0.79, F=0.32, T=38.3%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newqv1300_rectrq / close)` | TOP3000 | 0.98 | 0.83 | 11.5% | 80% | bull-only |
| `rank(fnd6_newqv1300_rectrq)` | TOP3000 | 0.76 | 0.67 | 33.3% | 80% | bull-only |
| `rank(fnd6_newqv1300_rectrq / close)` | TOP1000 | 0.70 | 0.57 | 17.2% | 80% | bull-only |
| `rank(fnd6_newqv1300_rectrq / close)` | TOP500 | 0.47 | 0.33 | 29.5% | 80% | bull-only |
| `rank(fnd6_newqv1300_rectrq)` | TOP1000 | 0.43 | 0.31 | 39.3% | 80% | bull-only |
| `rank(fnd6_newqv1300_rectrq)` | TOP500 | 0.21 | 0.12 | 53.0% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_rectr: 0.989 (strongly positively correlated)
- receivable: 0.987 (strongly positively correlated)
- fnd6_cptnewqv1300_rectq: 0.987 (strongly positively correlated)
- fnd6_newa2v1300_rect: 0.975 (strongly positively correlated)
- revenue: 0.971 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_rd_exp_flag | analyst4 | -0.38 | 1.79 | +0.77 | -0.64 | yes |
| rp_ess_revenue | news18 | -0.35 | 1.63 | +0.66 | -0.84 | yes |
| anl4_epsr_flag | analyst4 | -0.31 | 1.84 | +0.66 | -0.67 | yes |
| net_profit_adjusted_min_guidance | analyst4 | -0.27 | 1.59 | +0.62 | -0.85 | yes |
| max_gross_income_guidance_2 | analyst4 | -0.32 | 1.51 | +0.54 | -0.71 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
