---
field: fn_debt_instrument_face_amount_a
dataset: fundamental2
best_template: ts_zscore
best_sharpe: 0.77
best_fitness: 0.97
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 4
max_drawdown: 0.0774
ann_vol: 0.0568
hit_rate: 0.5004
rolling_sharpe_min: -1.297
rolling_sharpe_max: 2.818
top_merge_partner: anl4_epsr_flag
redundancy_cluster: 1
negated_best_sharpe: 0.89
negated_best_template: rank_neg_delta
negated_best_fitness: 0.94
n_negated_sims: 10
direction_gap: 0.12
---
# fn_debt_instrument_face_amount_a (fundamental2)

*Debt face amount*

## Signal Profile
- `rank(fn_debt_instrument_face_amount_a)`: S=0.24, F=0.09, T=0.7%, INFERIOR (TOP3000)
- `rank(fn_debt_instrument_face_amount_a / close)`: S=0.82, F=0.50, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_delta(fn_debt_instrument_face_amount_a, 5))`: S=-0.13, F=-0.04, T=22.4%, INFERIOR (TOP3000)
- `-rank(fn_debt_instrument_face_amount_a)`: S=-0.05, F=-0.01, T=1.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_debt_instrument_face_amount_a, 5))`: S=0.89, F=0.94, T=15.5%, INFERIOR (TOP3000)
- `-ts_zscore(fn_debt_instrument_face_amount_a, 63)`: S=0.77, F=0.97, T=12.2%, INFERIOR (TOP3000)
- `ts_mean(fn_debt_instrument_face_amount_a, 10)`: S=-1.15, F=-1.29, T=2.5%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_debt_instrument_face_amount_a, 22))`: S=0.58, F=0.47, T=12.1%, INFERIOR (TOP3000)
- `rank(-1 * fn_debt_instrument_face_amount_a)`: S=0.39, F=0.23, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * fn_debt_instrument_face_amount_a / close)`: S=0.34, F=0.18, T=2.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 13F/19P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 17F/3P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.82, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.33 (weak), ret=+1.5%
  - 2020: S=0.64 (moderate), ret=+5.2%
  - 2021: S=2.00 (strong), ret=+10.8%
  - 2022: S=1.76 (strong), ret=+7.8%
  - 2023: S=-0.67 (negative), ret=-2.6%

## Risk & Drawdown
- Max drawdown: 7.74% over 424 days (recovered)
- Annualized: return +4.6%, volatility 5.7% (fraction of booksize)
- Hit rate: 50.0% positive days
- Tail shape: skew +0.68, excess kurtosis +3.71

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.30, max 2.82, latest -0.55

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2023
Best month: +4.09%; worst month: -2.82%
Positive months: 56%

## Regime Profile
Regime profile: **mixed**
- Bull: S=2.09
- Sideways: S=-0.19
- Bear: S=0.44

## Negated Direction
Best negated: `rank(-1 * ts_delta(fn_debt_instrument_face_amount_a, 5))` S=0.89, F=0.94, INFERIOR
Direction gap: +0.12 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fn_debt_instrument_face_amount_a)`: S=0.39, F=0.23, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * fn_debt_instrument_face_amount_a / close)`: S=0.34, F=0.18, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_debt_instrument_face_amount_a, 5))`: S=0.89, F=0.94, T=15.5%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fn_debt_instrument_face_amount_a / close)` | TOP3000 | 0.82 | 0.50 | 7.7% | 80% | mixed |
| `rank(fn_debt_instrument_face_amount_a / close)` | TOP1000 | 0.77 | 0.47 | 6.5% | 80% | mixed |
| `rank(fn_debt_instrument_face_amount_a / close)` | TOP500 | 0.35 | 0.15 | 8.8% | 60% | bull-only |
| `rank(fn_debt_instrument_face_amount_a)` | TOP3000 | 0.23 | 0.09 | 20.5% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fn_op_lease_rent_exp_a: 0.870 (strongly positively correlated)
- fn_debt_instrument_carrying_amount_a: 0.865 (strongly positively correlated)
- fn_interest_paid_net_a: 0.864 (strongly positively correlated)
- fn_debt_instrument_carrying_amount_q: 0.863 (strongly positively correlated)
- fn_line_of_credit_facility_max_borrowing_capacity_q: 0.852 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_epsr_flag | analyst4 | -0.38 | 1.74 | +0.56 | -0.78 | yes |
| rp_ess_revenue | news18 | -0.32 | 1.38 | +0.49 | -0.55 | yes |
| max_gross_income_guidance_2 | analyst4 | -0.25 | 1.24 | +0.43 | -0.61 | yes |
| rp_css_revenue | news18 | -0.24 | 1.32 | +0.47 | +0.40 | yes |
| min_gross_income_guidance | analyst4 | -0.22 | 1.28 | +0.41 | -0.38 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
