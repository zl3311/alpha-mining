---
field: sales_estimate_count_quarterly
dataset: analyst4
best_template: rank_level
best_sharpe: 1.59
best_fitness: 0.88
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_FITNESS
n_sims: 32
regime_profile: all-weather
n_variations_with_pnl: 8
max_drawdown: 0.0296
ann_vol: 0.0245
hit_rate: 0.536
rolling_sharpe_min: -0.543
rolling_sharpe_max: 3.309
top_merge_partner: implied_volatility_call_1080
redundancy_cluster: 5
negated_best_sharpe: 0.52
negated_best_template: neg_rank_level
negated_best_fitness: 0.28
n_negated_sims: 10
direction_gap: -1.07
---
# sales_estimate_count_quarterly (analyst4)

*Sales - number of estimations*

## Signal Profile
- `rank(sales_estimate_count_quarterly)`: S=1.59, F=0.88, T=3.0%, INFERIOR (TOP3000)
- `rank(sales_estimate_count_quarterly / close)`: S=0.28, F=0.13, T=3.1%, INFERIOR (TOP1000)
- `rank(ts_delta(sales_estimate_count_quarterly, 5))`: S=0.42, F=0.09, T=34.8%, INFERIOR (TOP3000)
- `-rank(sales_estimate_count_quarterly)`: S=-1.16, F=-0.63, T=4.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(sales_estimate_count_quarterly, 5))`: S=0.45, F=0.17, T=34.1%, INFERIOR (TOP3000)
- `ts_zscore(sales_estimate_count_quarterly, 22)`: S=0.38, F=0.11, T=37.7%, INFERIOR (TOP3000)
- `ts_mean(sales_estimate_count_quarterly, 10)`: S=1.01, F=0.57, T=3.6%, INFERIOR (TOP3000)
- `rank(ts_rank(sales_estimate_count_quarterly, 22))`: S=0.42, F=0.15, T=13.1%, INFERIOR (TOP3000)
- `rank(-1 * sales_estimate_count_quarterly)`: S=0.52, F=0.28, T=4.9%, INFERIOR (TOP3000)
- `rank(-1 * sales_estimate_count_quarterly / close)`: S=-0.12, F=-0.04, T=3.9%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 4F/28P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 31F/1P
- LOW_SUB_UNIVERSE_SHARPE: 8F/12P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 1.59, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.94 (moderate), ret=+1.9%
  - 2020: S=1.18 (moderate), ret=+2.7%
  - 2021: S=2.18 (strong), ret=+6.0%
  - 2022: S=2.09 (strong), ret=+5.6%
  - 2023: S=1.36 (moderate), ret=+3.0%

## Risk & Drawdown
- Max drawdown: 2.96% over 427 days (recovered)
- Annualized: return +3.9%, volatility 2.5% (fraction of booksize)
- Hit rate: 53.6% positive days
- Tail shape: skew +0.08, excess kurtosis +0.80

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.54, max 3.31, latest 1.37

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2019
Best month: +1.89%; worst month: -1.51%
Positive months: 70%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=2.36
- Sideways: S=1.20
- Bear: S=1.15

## Negated Direction
Best negated: `rank(-1 * sales_estimate_count_quarterly)` S=0.52, F=0.28, INFERIOR
Direction gap: -1.07 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * sales_estimate_count_quarterly)`: S=0.52, F=0.28, T=4.9%, INFERIOR (TOP3000)
- `rank(-1 * sales_estimate_count_quarterly / close)`: S=-0.12, F=-0.04, T=3.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(sales_estimate_count_quarterly, 5))`: S=0.45, F=0.17, T=34.1%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(sales_estimate_count_quarterly)` | TOP3000 | 1.59 | 0.88 | 3.0% | 100% | all-weather |
| `rank(sales_estimate_count_quarterly)` | TOP1000 | 1.17 | 0.63 | 4.3% | 100% | all-weather |
| `rank(sales_estimate_count_quarterly / close)` | TOP1000 | 0.29 | 0.13 | 25.7% | 40% | bear-only |
| `rank(sales_estimate_count_quarterly / close)` | TOP500 | 0.25 | 0.10 | 23.8% | 80% | bear-only |
| `rank(ts_delta(sales_estimate_count_quarterly, 5))` | TOP3000 | 0.46 | 0.09 | 7.9% | 60% | mixed |
| `rank(sales_estimate_count_quarterly / close)` | TOP3000 | 0.15 | 0.06 | 39.5% | 40% | bear-only |
| `rank(sales_estimate_count_quarterly)` | TOP500 | 0.21 | 0.05 | 11.8% | 80% | mixed |
| `rank(sales_estimate_count_quarterly / close)` | TOP200 | 0.13 | 0.04 | 17.9% | 60% | mixed |

## Correlation Notes
Top correlates:
- anl4_qfd1_az_eps_number: 0.801 (strongly positively correlated)
- anl4_qf_az_eps_number: 0.800 (strongly positively correlated)
- anl4_netprofit_number: 0.776 (strongly positively correlated)
- anl4_ebit_number: 0.758 (strongly positively correlated)
- anl4_epsr_number: 0.603 (moderately positively correlated)

Redundancy cluster #5: 5 similar fields, mean |rho| 0.774 (representative). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| implied_volatility_call_1080 | option8 | +0.08 | 2.12 | +0.51 | +0.81 | yes |
| implied_volatility_call_720 | option8 | +0.08 | 2.10 | +0.50 | +0.70 | yes |
| fnd6_rank | fundamental6 | -0.19 | 2.08 | +0.48 | +0.21 | yes |
| implied_volatility_call_30 - implied_volatility_put_30 | option8 | +0.10 | 2.24 | +0.48 | +0.79 | yes |
| implied_volatility_call_360 | option8 | +0.09 | 2.06 | +0.47 | +0.59 | yes |

## Actionability
Blocked by LOW_FITNESS. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
