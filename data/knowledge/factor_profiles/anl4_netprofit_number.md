---
field: anl4_netprofit_number
dataset: analyst4
best_template: rank_level
best_sharpe: 1.18
best_fitness: 0.58
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: all-weather
n_variations_with_pnl: 9
max_drawdown: 0.0498
ann_vol: 0.0254
hit_rate: 0.5328
rolling_sharpe_min: -1.258
rolling_sharpe_max: 3.456
top_merge_partner: fnd6_rank
redundancy_cluster: 5
negated_best_sharpe: 0.32
negated_best_template: neg_rank_level
negated_best_fitness: 0.14
n_negated_sims: 10
direction_gap: -0.86
---
# anl4_netprofit_number (analyst4)

*Net profit - number of estimations*

## Signal Profile
- `rank(anl4_netprofit_number)`: S=1.18, F=0.58, T=3.1%, INFERIOR (TOP3000)
- `rank(anl4_netprofit_number / close)`: S=0.36, F=0.18, T=3.5%, INFERIOR (TOP500)
- `rank(ts_delta(anl4_netprofit_number, 5))`: S=0.28, F=0.05, T=35.2%, INFERIOR (TOP3000)
- `-rank(anl4_netprofit_number)`: S=-0.86, F=-0.40, T=4.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_netprofit_number, 5))`: S=-0.06, F=-0.01, T=34.4%, INFERIOR (TOP3000)
- `ts_zscore(anl4_netprofit_number, 22)`: S=0.00, F=0.00, T=37.0%, INFERIOR (TOP3000)
- `ts_mean(anl4_netprofit_number, 10)`: S=0.88, F=0.47, T=3.6%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_netprofit_number, 22))`: S=-0.08, F=-0.01, T=13.3%, INFERIOR (TOP3000)
- `rank(-1 * anl4_netprofit_number)`: S=0.32, F=0.14, T=5.0%, INFERIOR (TOP3000)
- `rank(-1 * anl4_netprofit_number / close)`: S=-0.20, F=-0.08, T=3.9%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 4F/28P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 5F/15P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 1.19, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=-0.01 (negative), ret=-0.0%
  - 2020: S=0.08 (weak), ret=+0.2%
  - 2021: S=1.54 (strong), ret=+4.1%
  - 2022: S=2.99 (strong), ret=+8.2%
  - 2023: S=0.90 (moderate), ret=+2.2%

## Risk & Drawdown
- Max drawdown: 4.98% over 863 days (recovered)
- Annualized: return +3.0%, volatility 2.5% (fraction of booksize)
- Hit rate: 53.3% positive days
- Tail shape: skew +0.08, excess kurtosis +0.98

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.26, max 3.46, latest 0.87

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2019
Best month: +2.39%; worst month: -1.01%
Positive months: 59%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=1.77
- Sideways: S=1.12
- Bear: S=0.64

## Negated Direction
Best negated: `rank(-1 * anl4_netprofit_number)` S=0.32, F=0.14, INFERIOR
Direction gap: -0.86 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * anl4_netprofit_number)`: S=0.32, F=0.14, T=5.0%, INFERIOR (TOP3000)
- `rank(-1 * anl4_netprofit_number / close)`: S=-0.20, F=-0.08, T=3.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_netprofit_number, 5))`: S=-0.06, F=-0.01, T=34.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_netprofit_number)` | TOP3000 | 1.19 | 0.58 | 5.0% | 80% | all-weather |
| `rank(anl4_netprofit_number)` | TOP1000 | 0.88 | 0.40 | 9.5% | 60% | all-weather |
| `rank(anl4_netprofit_number)` | TOP500 | 0.62 | 0.28 | 12.1% | 80% | all-weather |
| `rank(anl4_netprofit_number / close)` | TOP500 | 0.37 | 0.18 | 21.6% | 80% | bear-only |
| `rank(anl4_netprofit_number / close)` | TOP1000 | 0.27 | 0.12 | 23.5% | 40% | bear-only |
| `rank(anl4_netprofit_number / close)` | TOP200 | 0.22 | 0.08 | 20.1% | 80% | mixed |
| `rank(anl4_netprofit_number / close)` | TOP3000 | 0.14 | 0.05 | 38.8% | 40% | bear-only |
| `rank(ts_delta(anl4_netprofit_number, 5))` | TOP3000 | 0.30 | 0.05 | 13.0% | 60% | mixed |
| `rank(ts_delta(anl4_netprofit_number, 5))` | TOP500 | 0.14 | 0.02 | 12.3% | 60% | mixed |

## Correlation Notes
Top correlates:
- anl4_ebit_number: 0.915 (strongly positively correlated)
- sales_estimate_count_quarterly: 0.776 (strongly positively correlated)
- anl4_qfd1_az_eps_number: 0.684 (moderately positively correlated)
- anl4_qf_az_eps_number: 0.683 (moderately positively correlated)
- anl4_epsr_number: 0.621 (moderately positively correlated)

Redundancy cluster #5: 5 similar fields, mean |rho| 0.774 (representative: sales_estimate_count_quarterly). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| fnd6_rank | fundamental6 | -0.19 | 1.82 | +0.63 | +0.08 | yes |
| fn_repayments_of_lt_debt_a | fundamental2 | -0.12 | 1.68 | +0.50 | -0.16 | yes |
| fn_repayments_of_debt_a | fundamental2 | -0.12 | 1.70 | +0.51 | +0.91 | yes |
| fn_line_of_credit_facility_amount_out_q | fundamental2 | -0.06 | 1.69 | +0.50 | +0.39 | yes |
| fn_repayments_of_debt_q | fundamental2 | -0.17 | 1.64 | +0.45 | -0.30 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
