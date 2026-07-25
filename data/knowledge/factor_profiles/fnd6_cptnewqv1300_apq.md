---
field: fnd6_cptnewqv1300_apq
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 0.81
best_fitness: 0.56
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 8
max_drawdown: 0.0893
ann_vol: 0.073
hit_rate: 0.4915
rolling_sharpe_min: -1.157
rolling_sharpe_max: 2.484
top_merge_partner: rp_ess_revenue
redundancy_cluster: 1
negated_best_sharpe: 0.55
negated_best_template: rank_neg_delta
negated_best_fitness: 0.18
n_negated_sims: 10
direction_gap: -0.26
---
# fnd6_cptnewqv1300_apq (fundamental6)

*Accounts Payable/Creditors - Trade*

## Signal Profile
- `rank(fnd6_cptnewqv1300_apq)`: S=0.69, F=0.53, T=2.1%, INFERIOR (TOP3000)
- `rank(fnd6_cptnewqv1300_apq / close)`: S=0.81, F=0.56, T=2.3%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_cptnewqv1300_apq, 5))`: S=0.07, F=0.01, T=38.4%, INFERIOR (TOP500)
- `-rank(fnd6_cptnewqv1300_apq)`: S=-0.43, F=-0.28, T=2.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_cptnewqv1300_apq, 5))`: S=0.55, F=0.18, T=38.6%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_cptnewqv1300_apq, 63)`: S=0.18, F=0.03, T=18.7%, INFERIOR (TOP3000)
- `ts_mean(fnd6_cptnewqv1300_apq, 10)`: S=0.21, F=0.09, T=1.7%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_cptnewqv1300_apq, 22))`: S=-0.52, F=-0.19, T=17.3%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_cptnewqv1300_apq)`: S=-0.43, F=-0.28, T=2.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_cptnewqv1300_apq / close)`: S=-0.58, F=-0.39, T=2.9%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 9F/23P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/16P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.80, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=-0.28 (negative), ret=-1.3%
  - 2020: S=0.19 (weak), ret=+1.6%
  - 2021: S=1.64 (strong), ret=+15.7%
  - 2022: S=1.39 (moderate), ret=+9.6%
  - 2023: S=0.73 (moderate), ret=+3.1%

## Risk & Drawdown
- Max drawdown: 8.93% over 237 days (recovered)
- Annualized: return +5.8%, volatility 7.3% (fraction of booksize)
- Hit rate: 49.1% positive days
- Tail shape: skew +0.54, excess kurtosis +2.92

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.16, max 2.48, latest 0.81

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2019
Best month: +7.50%; worst month: -3.78%
Positive months: 58%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.22
- Sideways: S=-0.13
- Bear: S=-1.33

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_cptnewqv1300_apq, 5))` S=0.55, F=0.18, INFERIOR
Direction gap: -0.26 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_cptnewqv1300_apq)`: S=-0.43, F=-0.28, T=2.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_cptnewqv1300_apq / close)`: S=-0.58, F=-0.39, T=2.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_cptnewqv1300_apq, 5))`: S=0.55, F=0.18, T=38.6%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_cptnewqv1300_apq / close)` | TOP3000 | 0.80 | 0.56 | 8.9% | 80% | bull-only |
| `rank(fnd6_cptnewqv1300_apq)` | TOP3000 | 0.68 | 0.53 | 26.8% | 80% | bull-only |
| `rank(fnd6_cptnewqv1300_apq / close)` | TOP1000 | 0.57 | 0.39 | 13.8% | 60% | bull-only |
| `rank(fnd6_cptnewqv1300_apq)` | TOP1000 | 0.43 | 0.28 | 28.9% | 60% | bull-only |
| `rank(fnd6_cptnewqv1300_apq / close)` | TOP500 | 0.41 | 0.25 | 21.7% | 60% | bull-only |
| `rank(fnd6_cptnewqv1300_apq)` | TOP500 | 0.26 | 0.13 | 33.5% | 60% | bull-only |
| `rank(fnd6_cptnewqv1300_apq / close)` | TOP200 | 0.18 | 0.07 | 23.0% | 60% | bull-only |
| `rank(fnd6_cptnewqv1300_apq)` | TOP200 | 0.12 | 0.04 | 39.5% | 80% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_newa1v1300_ap: 0.988 (strongly positively correlated)
- fnd6_cptnewqv1300_ltq: 0.971 (strongly positively correlated)
- liabilities: 0.971 (strongly positively correlated)
- fnd6_newqv1300_ltmibq: 0.970 (strongly positively correlated)
- fnd6_newqv1300_cogsq: 0.969 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| rp_ess_revenue | news18 | -0.35 | 1.46 | +0.57 | -0.70 | yes |
| max_gross_income_guidance_2 | analyst4 | -0.31 | 1.33 | +0.53 | -0.93 | yes |
| anl4_epsr_flag | analyst4 | -0.34 | 1.73 | +0.55 | -0.58 | yes |
| min_gross_income_guidance | analyst4 | -0.22 | 1.31 | +0.44 | -0.75 | yes |
| max_gross_income_guidance | analyst4 | -0.22 | 1.33 | +0.44 | -0.75 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
