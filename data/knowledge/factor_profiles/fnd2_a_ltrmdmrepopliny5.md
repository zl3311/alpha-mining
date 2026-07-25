---
field: fnd2_a_ltrmdmrepopliny5
dataset: fundamental2
best_template: ts_zscore
best_sharpe: 0.65
best_fitness: 0.53
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: all-weather
n_variations_with_pnl: 7
max_drawdown: 0.0587
ann_vol: 0.0439
hit_rate: 0.5045
rolling_sharpe_min: -1.17
rolling_sharpe_max: 2.578
top_merge_partner: anl4_epsr_flag
redundancy_cluster: 46
negated_best_sharpe: 0.33
negated_best_template: neg_rank_level
negated_best_fitness: 0.15
n_negated_sims: 10
direction_gap: -0.32
---
# fnd2_a_ltrmdmrepopliny5 (fundamental2)

*Amount of long-term debt payable, sinking fund requirements, and other securities issued that are redeemable by holder at fixed or determinable prices and dates maturing in the 5th fiscal year following the latest fiscal year. Excludes interim and annual periods when interim periods are reported on a rolling approach, from latest balance sheet date.*

## Signal Profile
- `rank(fnd2_a_ltrmdmrepopliny5)`: S=0.39, F=0.14, T=0.9%, INFERIOR (TOP3000)
- `rank(fnd2_a_ltrmdmrepopliny5 / close)`: S=0.87, F=0.48, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd2_a_ltrmdmrepopliny5, 5))`: S=0.41, F=0.18, T=31.9%, INFERIOR (TOP500)
- `-rank(fnd2_a_ltrmdmrepopliny5)`: S=-0.34, F=-0.12, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_a_ltrmdmrepopliny5, 5))`: S=0.00, F=0.00, T=26.3%, INFERIOR (TOP3000)
- `ts_zscore(fnd2_a_ltrmdmrepopliny5, 22)`: S=0.65, F=0.53, T=14.3%, INFERIOR (TOP3000)
- `ts_mean(fnd2_a_ltrmdmrepopliny5, 10)`: S=0.65, F=0.33, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd2_a_ltrmdmrepopliny5, 22))`: S=0.72, F=0.52, T=15.3%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_a_ltrmdmrepopliny5)`: S=0.33, F=0.15, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_a_ltrmdmrepopliny5 / close)`: S=0.23, F=0.09, T=2.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/6P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.86, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=-0.00 (negative), ret=-0.0%
  - 2020: S=1.38 (moderate), ret=+9.1%
  - 2021: S=1.49 (moderate), ret=+5.4%
  - 2022: S=0.88 (moderate), ret=+3.3%
  - 2023: S=0.26 (weak), ret=+0.8%

## Risk & Drawdown
- Max drawdown: 5.87% over 230 days (recovered)
- Annualized: return +3.8%, volatility 4.4% (fraction of booksize)
- Hit rate: 50.4% positive days
- Tail shape: skew +0.81, excess kurtosis +5.14

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.17, max 2.58, latest 0.34

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2019
Best month: +3.23%; worst month: -2.25%
Positive months: 56%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=1.81
- Sideways: S=0.21
- Bear: S=0.56

## Negated Direction
Best negated: `rank(-1 * fnd2_a_ltrmdmrepopliny5)` S=0.33, F=0.15, INFERIOR
Direction gap: -0.32 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd2_a_ltrmdmrepopliny5)`: S=0.33, F=0.15, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_a_ltrmdmrepopliny5 / close)`: S=0.23, F=0.09, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_a_ltrmdmrepopliny5, 5))`: S=0.00, F=0.00, T=26.3%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd2_a_ltrmdmrepopliny5 / close)` | TOP3000 | 0.86 | 0.48 | 5.9% | 80% | all-weather |
| `rank(fnd2_a_ltrmdmrepopliny5 / close)` | TOP1000 | 0.65 | 0.35 | 9.7% | 80% | all-weather |
| `rank(ts_delta(fnd2_a_ltrmdmrepopliny5, 5))` | TOP500 | 0.40 | 0.18 | 31.2% | 80% | bull-only |
| `rank(ts_delta(fnd2_a_ltrmdmrepopliny5, 5))` | TOP1000 | 0.38 | 0.17 | 20.7% | 80% | bull-only |
| `rank(fnd2_a_ltrmdmrepopliny5)` | TOP3000 | 0.37 | 0.14 | 6.9% | 40% | bull-only |
| `rank(fnd2_a_ltrmdmrepopliny5)` | TOP1000 | 0.32 | 0.12 | 8.6% | 60% | bull-only |
| `rank(fnd2_a_ltrmdmrepopliny5 / close)` | TOP500 | 0.26 | 0.10 | 11.9% | 40% | bull-only |

## Correlation Notes
Top correlates:
- fnd2_a_ltrmdmrepoplinyfour: 0.825 (strongly positively correlated)
- fn_line_of_credit_facility_max_borrowing_capacity_a: 0.796 (strongly positively correlated)
- fn_line_of_credit_facility_max_borrowing_capacity_q: 0.793 (strongly positively correlated)
- fn_debt_instrument_face_amount_a: 0.788 (strongly positively correlated)
- fn_interest_paid_net_a: 0.788 (strongly positively correlated)

Redundancy cluster #46: 6 similar fields, mean |rho| 0.737 (representative: fn_op_lease_min_pay_due_after_5y_a). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_epsr_flag | analyst4 | -0.35 | 1.66 | +0.48 | -0.39 | yes |
| cashflow_per_share_minimum | analyst4 | -0.12 | 1.30 | +0.43 | -0.71 | yes |
| anl4_capex_high | analyst4 | -0.17 | 1.39 | +0.46 | -0.29 | yes |
| fnd6_newqv1300_miiq | fundamental6 | -0.15 | 1.29 | +0.42 | +0.02 | yes |
| sales_min_guidance_quarterly | analyst4 | -0.15 | 1.27 | +0.40 | -0.14 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
