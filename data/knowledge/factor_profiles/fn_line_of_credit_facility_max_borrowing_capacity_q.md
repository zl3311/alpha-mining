---
field: fn_line_of_credit_facility_max_borrowing_capacity_q
dataset: fundamental2
best_template: rank_value_norm
best_sharpe: 1.01
best_fitness: 0.7
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 9
max_drawdown: 0.0715
ann_vol: 0.059
hit_rate: 0.4883
rolling_sharpe_min: -1.299
rolling_sharpe_max: 2.859
top_merge_partner: anl4_epsr_flag
redundancy_cluster: 1
negated_best_sharpe: 0.09
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.02
n_negated_sims: 10
direction_gap: -0.92
---
# fn_line_of_credit_facility_max_borrowing_capacity_q (fundamental2)

*Maximum borrowing capacity under the credit facility without consideration of any current restrictions on the amount that could be borrowed or the amounts currently outstanding under the facility.*

## Signal Profile
- `rank(fn_line_of_credit_facility_max_borrowing_capacity_q)`: S=0.51, F=0.27, T=0.8%, INFERIOR (TOP3000)
- `rank(fn_line_of_credit_facility_max_borrowing_capacity_q / close)`: S=1.01, F=0.70, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_delta(fn_line_of_credit_facility_max_borrowing_capacity_q, 5))`: S=0.44, F=0.25, T=24.0%, INFERIOR (TOP200)
- `-rank(fn_line_of_credit_facility_max_borrowing_capacity_q)`: S=-0.36, F=-0.15, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_line_of_credit_facility_max_borrowing_capacity_q, 5))`: S=-0.72, F=-0.52, T=24.0%, INFERIOR (TOP3000)
- `-ts_zscore(fn_line_of_credit_facility_max_borrowing_capacity_q, 63)`: S=-0.13, F=-0.05, T=15.0%, INFERIOR (TOP3000)
- `ts_mean(fn_line_of_credit_facility_max_borrowing_capacity_q, 10)`: S=0.14, F=0.04, T=1.3%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_line_of_credit_facility_max_borrowing_capacity_q, 22))`: S=-0.17, F=-0.05, T=17.2%, INFERIOR (TOP3000)
- `rank(-1 * fn_line_of_credit_facility_max_borrowing_capacity_q)`: S=0.05, F=0.01, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * fn_line_of_credit_facility_max_borrowing_capacity_q / close)`: S=0.09, F=0.02, T=2.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 13F/19P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 11F/9P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 1.00, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.24 (weak), ret=+1.1%
  - 2020: S=1.27 (moderate), ret=+11.1%
  - 2021: S=1.95 (strong), ret=+10.0%
  - 2022: S=1.03 (moderate), ret=+5.0%
  - 2023: S=0.44 (weak), ret=+1.9%

## Risk & Drawdown
- Max drawdown: 7.15% over 154 days (recovered)
- Annualized: return +5.9%, volatility 5.9% (fraction of booksize)
- Hit rate: 48.8% positive days
- Tail shape: skew +0.92, excess kurtosis +5.96

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.30, max 2.86, latest 0.56

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2019
Best month: +4.82%; worst month: -3.06%
Positive months: 63%

## Regime Profile
Regime profile: **mixed**
- Bull: S=2.36
- Sideways: S=0.12
- Bear: S=0.41

## Negated Direction
Best negated: `rank(-1 * fn_line_of_credit_facility_max_borrowing_capacity_q / close)` S=0.09, F=0.02, INFERIOR
Direction gap: -0.92 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fn_line_of_credit_facility_max_borrowing_capacity_q)`: S=0.05, F=0.01, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * fn_line_of_credit_facility_max_borrowing_capacity_q / close)`: S=0.09, F=0.02, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_line_of_credit_facility_max_borrowing_capacity_q, 5))`: S=-0.72, F=-0.52, T=24.0%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fn_line_of_credit_facility_max_borrowing_capacity_q / close)` | TOP3000 | 1.00 | 0.70 | 7.1% | 100% | mixed |
| `rank(fn_line_of_credit_facility_max_borrowing_capacity_q / close)` | TOP1000 | 0.70 | 0.42 | 8.7% | 100% | mixed |
| `rank(fn_line_of_credit_facility_max_borrowing_capacity_q)` | TOP3000 | 0.51 | 0.27 | 18.5% | 80% | bull-only |
| `rank(ts_delta(fn_line_of_credit_facility_max_borrowing_capacity_q, 5))` | TOP200 | 0.44 | 0.25 | 20.5% | 80% | mixed |
| `rank(fn_line_of_credit_facility_max_borrowing_capacity_q)` | TOP1000 | 0.36 | 0.15 | 19.2% | 80% | bull-only |
| `rank(ts_delta(fn_line_of_credit_facility_max_borrowing_capacity_q, 5))` | TOP500 | 0.28 | 0.12 | 39.7% | 60% | mixed |
| `rank(ts_delta(fn_line_of_credit_facility_max_borrowing_capacity_q, 5))` | TOP3000 | 0.30 | 0.11 | 35.8% | 40% | mixed |
| `rank(fn_line_of_credit_facility_max_borrowing_capacity_q / close)` | TOP500 | 0.25 | 0.09 | 14.4% | 60% | bull-only |
| `rank(fn_line_of_credit_facility_max_borrowing_capacity_q)` | TOP500 | 0.08 | 0.02 | 24.5% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fn_line_of_credit_facility_max_borrowing_capacity_a: 0.929 (strongly positively correlated)
- fn_op_lease_rent_exp_a: 0.895 (strongly positively correlated)
- fn_interest_paid_net_a: 0.884 (strongly positively correlated)
- fnd2_a_bnsacqproformarvn: 0.873 (strongly positively correlated)
- fnd2_dfdtxastxdfdexprssaccrs: 0.867 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_epsr_flag | analyst4 | -0.38 | 1.87 | +0.69 | -0.62 | yes |
| rp_ess_revenue | news18 | -0.33 | 1.51 | +0.51 | -0.43 | yes |
| anl4_capex_high | analyst4 | -0.21 | 1.54 | +0.53 | -0.12 | yes |
| anl4_rd_exp_flag | analyst4 | -0.22 | 1.54 | +0.51 | +0.29 | yes |
| rp_css_ptg | news18 | -0.19 | 1.50 | +0.49 | +0.94 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
