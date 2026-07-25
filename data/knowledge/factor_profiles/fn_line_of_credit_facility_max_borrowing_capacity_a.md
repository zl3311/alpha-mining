---
field: fn_line_of_credit_facility_max_borrowing_capacity_a
dataset: fundamental2
best_template: ts_zscore
best_sharpe: 0.61
best_fitness: 0.78
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 5
max_drawdown: 0.0602
ann_vol: 0.0516
hit_rate: 0.4939
rolling_sharpe_min: -1.299
rolling_sharpe_max: 3.082
top_merge_partner: anl4_epsr_flag
redundancy_cluster: 1
negated_best_sharpe: 0.65
negated_best_template: rank_neg_delta
negated_best_fitness: 0.51
n_negated_sims: 10
direction_gap: 0.04
---
# fn_line_of_credit_facility_max_borrowing_capacity_a (fundamental2)

*Maximum borrowing capacity under the credit facility without consideration of any current restrictions on the amount that could be borrowed or the amounts currently outstanding under the facility.*

## Signal Profile
- `rank(fn_line_of_credit_facility_max_borrowing_capacity_a)`: S=0.47, F=0.22, T=0.7%, INFERIOR (TOP3000)
- `rank(fn_line_of_credit_facility_max_borrowing_capacity_a / close)`: S=1.07, F=0.71, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_delta(fn_line_of_credit_facility_max_borrowing_capacity_a, 5))`: S=0.16, F=0.05, T=26.7%, INFERIOR (TOP500)
- `-rank(fn_line_of_credit_facility_max_borrowing_capacity_a)`: S=-0.11, F=-0.02, T=1.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_line_of_credit_facility_max_borrowing_capacity_a, 5))`: S=0.65, F=0.51, T=16.4%, INFERIOR (TOP3000)
- `-ts_zscore(fn_line_of_credit_facility_max_borrowing_capacity_a, 63)`: S=0.61, F=0.78, T=11.4%, INFERIOR (TOP3000)
- `ts_mean(fn_line_of_credit_facility_max_borrowing_capacity_a, 10)`: S=-0.23, F=-0.08, T=0.9%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_line_of_credit_facility_max_borrowing_capacity_a, 22))`: S=-0.62, F=-0.46, T=15.3%, INFERIOR (TOP3000)
- `rank(-1 * fn_line_of_credit_facility_max_borrowing_capacity_a)`: S=0.05, F=0.01, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * fn_line_of_credit_facility_max_borrowing_capacity_a / close)`: S=-0.04, F=-0.01, T=2.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 13F/19P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 10F/10P
- LOW_TURNOVER: 2F/30P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 1.07, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.65 (moderate), ret=+2.3%
  - 2020: S=1.49 (moderate), ret=+11.2%
  - 2021: S=1.68 (strong), ret=+7.9%
  - 2022: S=0.92 (moderate), ret=+4.0%
  - 2023: S=0.41 (weak), ret=+1.6%

## Risk & Drawdown
- Max drawdown: 6.02% over 590 days (not yet recovered, ongoing at window end)
- Annualized: return +5.5%, volatility 5.2% (fraction of booksize)
- Hit rate: 49.4% positive days
- Tail shape: skew +0.88, excess kurtosis +4.75

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.30, max 3.08, latest 0.54

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2023
Best month: +4.77%; worst month: -2.34%
Positive months: 58%

## Regime Profile
Regime profile: **mixed**
- Bull: S=2.52
- Sideways: S=0.44
- Bear: S=0.18

## Negated Direction
Best negated: `rank(-1 * ts_delta(fn_line_of_credit_facility_max_borrowing_capacity_a, 5))` S=0.65, F=0.51, INFERIOR
Direction gap: +0.04 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fn_line_of_credit_facility_max_borrowing_capacity_a)`: S=0.05, F=0.01, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * fn_line_of_credit_facility_max_borrowing_capacity_a / close)`: S=-0.04, F=-0.01, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_line_of_credit_facility_max_borrowing_capacity_a, 5))`: S=0.65, F=0.51, T=16.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fn_line_of_credit_facility_max_borrowing_capacity_a / close)` | TOP3000 | 1.07 | 0.71 | 6.0% | 100% | mixed |
| `rank(fn_line_of_credit_facility_max_borrowing_capacity_a / close)` | TOP1000 | 0.68 | 0.40 | 7.2% | 80% | mixed |
| `rank(fn_line_of_credit_facility_max_borrowing_capacity_a)` | TOP3000 | 0.46 | 0.22 | 13.0% | 60% | bull-only |
| `rank(fn_line_of_credit_facility_max_borrowing_capacity_a / close)` | TOP500 | 0.25 | 0.09 | 15.7% | 60% | bull-only |
| `rank(ts_delta(fn_line_of_credit_facility_max_borrowing_capacity_a, 5))` | TOP500 | 0.15 | 0.05 | 31.1% | 40% | bull-only |

## Correlation Notes
Top correlates:
- fn_line_of_credit_facility_max_borrowing_capacity_q: 0.929 (strongly positively correlated)
- fn_op_lease_rent_exp_a: 0.887 (strongly positively correlated)
- fn_interest_paid_net_a: 0.885 (strongly positively correlated)
- fnd2_a_bnsacqproformarvn: 0.870 (strongly positively correlated)
- fnd2_dfdtxastxdfdexprssaccrs: 0.862 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_epsr_flag | analyst4 | -0.38 | 1.85 | +0.67 | -0.53 | yes |
| anl4_capex_flag | analyst4 | -0.09 | 1.60 | +0.51 | -0.65 | yes |
| pv13_ompetitorgraphrank_hub_rank | pv13 | -0.20 | 1.71 | +0.55 | +0.63 | yes |
| pcr_vol_20 | option9 | -0.07 | 1.61 | +0.48 | -0.45 | yes |
| anl4_cfo_flag | analyst4 | -0.08 | 1.60 | +0.49 | -0.34 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
