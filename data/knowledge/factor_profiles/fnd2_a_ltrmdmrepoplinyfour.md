---
field: fnd2_a_ltrmdmrepoplinyfour
dataset: fundamental2
best_template: rank_value_norm
best_sharpe: 0.91
best_fitness: 0.52
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: all-weather
n_variations_with_pnl: 5
max_drawdown: 0.0541
ann_vol: 0.0456
hit_rate: 0.5215
rolling_sharpe_min: -1.002
rolling_sharpe_max: 2.692
top_merge_partner: anl4_epsr_flag
redundancy_cluster: 1
negated_best_sharpe: 0.49
negated_best_template: rank_neg_delta
negated_best_fitness: 0.21
n_negated_sims: 10
direction_gap: -0.42
---
# fnd2_a_ltrmdmrepoplinyfour (fundamental2)

*Amount of long-term debt payable, sinking fund requirements, and other securities issued that are redeemable by holder at fixed or determinable prices and dates maturing in the 4th fiscal year following the latest fiscal year. Excludes interim and annual periods when interim periods are reported on a rolling approach, from latest balance sheet date.*

## Signal Profile
- `rank(fnd2_a_ltrmdmrepoplinyfour)`: S=0.51, F=0.22, T=1.0%, INFERIOR (TOP3000)
- `rank(fnd2_a_ltrmdmrepoplinyfour / close)`: S=0.91, F=0.52, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd2_a_ltrmdmrepoplinyfour, 5))`: S=0.06, F=0.01, T=26.8%, INFERIOR (TOP200)
- `-rank(fnd2_a_ltrmdmrepoplinyfour)`: S=-0.13, F=-0.03, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_a_ltrmdmrepoplinyfour, 5))`: S=0.49, F=0.21, T=34.8%, INFERIOR (TOP3000)
- `-ts_zscore(fnd2_a_ltrmdmrepoplinyfour, 63)`: S=-0.15, F=-0.06, T=14.7%, INFERIOR (TOP3000)
- `ts_mean(fnd2_a_ltrmdmrepoplinyfour, 10)`: S=0.16, F=0.04, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd2_a_ltrmdmrepoplinyfour, 22))`: S=-0.07, F=-0.02, T=15.7%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_a_ltrmdmrepoplinyfour)`: S=-0.51, F=-0.22, T=1.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_a_ltrmdmrepoplinyfour / close)`: S=-0.91, F=-0.52, T=1.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 13F/19P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/16P
- LOW_TURNOVER: 4F/28P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.90, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.09 (weak), ret=+0.3%
  - 2020: S=1.18 (moderate), ret=+7.9%
  - 2021: S=1.87 (strong), ret=+7.4%
  - 2022: S=1.19 (moderate), ret=+5.0%
  - 2023: S=-0.12 (negative), ret=-0.4%

## Risk & Drawdown
- Max drawdown: 5.41% over 154 days (recovered)
- Annualized: return +4.1%, volatility 4.6% (fraction of booksize)
- Hit rate: 52.1% positive days
- Tail shape: skew +0.73, excess kurtosis +4.19

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.00, max 2.69, latest -0.03

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2023
Best month: +3.46%; worst month: -2.08%
Positive months: 58%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=1.73
- Sideways: S=0.29
- Bear: S=0.66

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd2_a_ltrmdmrepoplinyfour, 5))` S=0.49, F=0.21, INFERIOR
Direction gap: -0.42 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd2_a_ltrmdmrepoplinyfour)`: S=-0.51, F=-0.22, T=1.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_a_ltrmdmrepoplinyfour / close)`: S=-0.91, F=-0.52, T=1.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_a_ltrmdmrepoplinyfour, 5))`: S=0.49, F=0.21, T=34.8%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd2_a_ltrmdmrepoplinyfour / close)` | TOP3000 | 0.90 | 0.52 | 5.4% | 80% | all-weather |
| `rank(fnd2_a_ltrmdmrepoplinyfour)` | TOP3000 | 0.49 | 0.22 | 7.3% | 60% | bull-only |
| `rank(fnd2_a_ltrmdmrepoplinyfour / close)` | TOP1000 | 0.47 | 0.22 | 7.1% | 60% | mixed |
| `rank(fnd2_a_ltrmdmrepoplinyfour / close)` | TOP500 | 0.25 | 0.09 | 10.4% | 60% | mixed |
| `rank(fnd2_a_ltrmdmrepoplinyfour)` | TOP1000 | 0.12 | 0.03 | 9.0% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fn_interest_paid_net_a: 0.840 (strongly positively correlated)
- fnd2_a_ltrmdmrepoplinythree: 0.834 (strongly positively correlated)
- fn_line_of_credit_facility_max_borrowing_capacity_q: 0.833 (strongly positively correlated)
- fn_line_of_credit_facility_max_borrowing_capacity_a: 0.829 (strongly positively correlated)
- fnd6_newa2v1300_xint: 0.826 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_epsr_flag | analyst4 | -0.38 | 1.71 | +0.54 | -0.65 | yes |
| anl4_capex_high | analyst4 | -0.14 | 1.40 | +0.47 | -0.08 | yes |
| cashflow_per_share_minimum | analyst4 | -0.10 | 1.31 | +0.41 | -0.64 | yes |
| rp_ess_revenue | news18 | -0.28 | 1.33 | +0.43 | -0.40 | yes |
| pcr_vol_60 | option9 | -0.04 | 1.27 | +0.37 | -0.77 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
