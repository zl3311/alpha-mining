---
field: fnd6_newqv1300_ltmibq
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 1.03
best_fitness: 0.84
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 7
max_drawdown: 0.0841
ann_vol: 0.0814
hit_rate: 0.4923
rolling_sharpe_min: -0.749
rolling_sharpe_max: 2.722
top_merge_partner: anl4_epsr_flag
redundancy_cluster: 1
negated_best_sharpe: 0.03
negated_best_template: neg_rank_level
negated_best_fitness: 0.01
n_negated_sims: 10
direction_gap: -1.0
---
# fnd6_newqv1300_ltmibq (fundamental6)

*Liabilities - Total and Noncontrolling Interest*

## Signal Profile
- `rank(fnd6_newqv1300_ltmibq)`: S=0.81, F=0.68, T=1.4%, INFERIOR (TOP3000)
- `rank(fnd6_newqv1300_ltmibq / close)`: S=1.03, F=0.84, T=1.7%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_newqv1300_ltmibq, 5))`: S=-0.03, F=0.00, T=37.5%, INFERIOR (TOP3000)
- `-rank(fnd6_newqv1300_ltmibq)`: S=-0.40, F=-0.26, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_ltmibq, 5))`: S=0.07, F=0.01, T=37.7%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_newqv1300_ltmibq, 63)`: S=0.59, F=0.23, T=18.8%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newqv1300_ltmibq, 10)`: S=0.26, F=0.11, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newqv1300_ltmibq, 22))`: S=-0.26, F=-0.07, T=16.7%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_ltmibq)`: S=0.03, F=0.01, T=2.7%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_ltmibq / close)`: S=-0.14, F=-0.06, T=2.9%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 9F/23P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 8F/12P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 1.02, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.25 (weak), ret=+1.2%
  - 2020: S=0.55 (moderate), ret=+5.4%
  - 2021: S=1.73 (strong), ret=+18.3%
  - 2022: S=1.63 (strong), ret=+11.9%
  - 2023: S=0.72 (moderate), ret=+3.9%

## Risk & Drawdown
- Max drawdown: 8.41% over 236 days (recovered)
- Annualized: return +8.3%, volatility 8.1% (fraction of booksize)
- Hit rate: 49.2% positive days
- Tail shape: skew +0.61, excess kurtosis +3.46

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.75, max 2.72, latest 0.81

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2019
Best month: +8.99%; worst month: -3.46%
Positive months: 58%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.98
- Sideways: S=0.37
- Bear: S=-0.76

## Negated Direction
Best negated: `rank(-1 * fnd6_newqv1300_ltmibq)` S=0.03, F=0.01, INFERIOR
Direction gap: -1.00 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_newqv1300_ltmibq)`: S=0.03, F=0.01, T=2.7%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_ltmibq / close)`: S=-0.14, F=-0.06, T=2.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_ltmibq, 5))`: S=0.07, F=0.01, T=37.7%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newqv1300_ltmibq / close)` | TOP3000 | 1.02 | 0.84 | 8.4% | 100% | bull-only |
| `rank(fnd6_newqv1300_ltmibq)` | TOP3000 | 0.80 | 0.68 | 25.9% | 80% | bull-only |
| `rank(fnd6_newqv1300_ltmibq / close)` | TOP1000 | 0.62 | 0.45 | 14.6% | 60% | bull-only |
| `rank(fnd6_newqv1300_ltmibq / close)` | TOP500 | 0.45 | 0.29 | 21.5% | 60% | bull-only |
| `rank(fnd6_newqv1300_ltmibq)` | TOP1000 | 0.40 | 0.26 | 32.4% | 60% | bull-only |
| `rank(fnd6_newqv1300_ltmibq)` | TOP500 | 0.20 | 0.11 | 47.0% | 60% | bull-only |
| `rank(fnd6_newqv1300_ltmibq / close)` | TOP200 | 0.14 | 0.06 | 31.8% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_cptnewqv1300_ltq: 1.000 (strongly positively correlated)
- liabilities: 1.000 (strongly positively correlated)
- fnd6_newa1v1300_lt: 0.992 (strongly positively correlated)
- fnd6_mfma1_at: 0.978 (strongly positively correlated)
- fnd6_newa1v1300_at: 0.978 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_epsr_flag | analyst4 | -0.36 | 1.94 | +0.76 | -0.66 | yes |
| rp_ess_revenue | news18 | -0.34 | 1.64 | +0.62 | -0.71 | yes |
| anl4_rd_exp_flag | analyst4 | -0.24 | 1.64 | +0.62 | -0.35 | yes |
| net_profit_adjusted_min_guidance | analyst4 | -0.18 | 1.54 | +0.52 | -0.68 | yes |
| max_gross_income_guidance_2 | analyst4 | -0.28 | 1.49 | +0.47 | -0.88 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
