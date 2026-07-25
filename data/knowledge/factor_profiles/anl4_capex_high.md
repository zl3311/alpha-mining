---
field: anl4_capex_high
dataset: analyst4
cluster: analyst4_cashflow
coverage: 0.6173
community_alphas: 8228
best_template: rank_delta
best_sharpe: 0.89
best_fitness: 0.32
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 35
regime_profile: mixed
n_variations_with_pnl: 7
max_drawdown: 0.06
ann_vol: 0.0524
hit_rate: 0.5296
rolling_sharpe_min: -0.289
rolling_sharpe_max: 3.093
top_merge_partner: fnd2_a_bnsacqproformarvn
redundancy_cluster: 45
negated_best_sharpe: 0.32
negated_best_template: neg_rank_level
negated_best_fitness: 0.19
n_negated_sims: 10
direction_gap: -0.57
---
# anl4_capex_high (analyst4)

*Capital Expenditures - The highest estimation*

## Signal Profile
- `rank(anl4_capex_high)`: S=0.29, F=0.14, T=1.3%, INFERIOR (TOP3000)
- `rank(anl4_capex_high / close)`: S=0.37, F=0.17, T=1.7%, INFERIOR (TOP3000)
- `rank(ts_delta(anl4_capex_high, 5))`: S=0.89, F=0.32, T=36.9%, INFERIOR (TOP3000)
- `ts_decay_linear(rank(anl4_capex_high), 5)`: S=0.29, F=0.14, T=1.3%, INFERIOR (TOP3000)
- `-rank(anl4_capex_high)`: S=-0.12, F=-0.04, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_capex_high, 5))`: S=-0.11, F=-0.02, T=33.8%, INFERIOR (TOP3000)
- `ts_zscore(anl4_capex_high, 22)`: S=0.27, F=0.07, T=35.1%, INFERIOR (TOP3000)
- `ts_mean(anl4_capex_high, 10)`: S=-0.06, F=-0.01, T=1.4%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_capex_high, 22))`: S=0.29, F=0.09, T=13.6%, INFERIOR (TOP3000)
- `rank(-1 * anl4_capex_high)`: S=0.32, F=0.19, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * anl4_capex_high / close)`: S=0.23, F=0.11, T=2.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 8F/27P
- LOW_FITNESS: 35F/0P
- LOW_SHARPE: 35F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/9P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.93, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=2.63 (strong), ret=+11.6%
  - 2020: S=0.36 (weak), ret=+2.3%
  - 2021: S=1.66 (strong), ret=+8.5%
  - 2022: S=0.11 (weak), ret=+0.6%
  - 2023: S=0.20 (weak), ret=+0.9%

## Risk & Drawdown
- Max drawdown: 6.00% over 328 days (recovered)
- Annualized: return +4.9%, volatility 5.2% (fraction of booksize)
- Hit rate: 53.0% positive days
- Tail shape: skew -0.15, excess kurtosis +1.48

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.29, max 3.09, latest 0.09

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2022
Best month: +3.69%; worst month: -2.33%
Positive months: 66%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.37
- Sideways: S=1.36
- Bear: S=1.05

## Negated Direction
Best negated: `rank(-1 * anl4_capex_high)` S=0.32, F=0.19, INFERIOR
Direction gap: -0.57 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * anl4_capex_high)`: S=0.32, F=0.19, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * anl4_capex_high / close)`: S=0.23, F=0.11, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_capex_high, 5))`: S=-0.11, F=-0.02, T=33.8%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(anl4_capex_high, 5))` | TOP3000 | 0.93 | 0.32 | 6.0% | 100% | mixed |
| `rank(anl4_capex_high / close)` | TOP3000 | 0.36 | 0.17 | 9.9% | 80% | bull-only |
| `rank(anl4_capex_high)` | TOP3000 | 0.29 | 0.14 | 31.8% | 80% | bull-only |
| `ts_decay_linear(rank(anl4_capex_high), 5)` | TOP3000 | 0.28 | 0.14 | 31.8% | 80% | bull-only |
| `rank(ts_delta(anl4_capex_high, 5))` | TOP1000 | 0.35 | 0.08 | 6.6% | 60% | mixed |
| `rank(anl4_capex_high)` | TOP1000 | 0.11 | 0.04 | 32.7% | 60% | bull-only |
| `rank(ts_delta(anl4_capex_high, 5))` | TOP200 | 0.10 | 0.02 | 24.0% | 40% | bear-only |

## Correlation Notes
Top correlates:
- anl4_median_capexp: 0.831 (strongly positively correlated)
- fnd6_prcl: -0.232 (weakly negatively correlated)
- fnd6_prcc: -0.230 (weakly negatively correlated)
- fnd6_newa1v1300_bkvlps: -0.227 (weakly negatively correlated)
- book_value_per_share_reported_value: -0.225 (weakly negatively correlated)

Redundancy cluster #45: 2 similar fields, mean |rho| 0.831 (representative). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| fnd2_a_bnsacqproformarvn | fundamental2 | -0.19 | 1.61 | +0.49 | -0.75 | yes |
| fn_line_of_credit_facility_max_borrowing_capacity_q | fundamental2 | -0.21 | 1.54 | +0.53 | -0.12 | yes |
| fnd2_a_blgandiprtsg | fundamental2 | -0.15 | 1.46 | +0.49 | -0.40 | yes |
| fn_op_lease_min_pay_due_after_5y_a | fundamental2 | -0.20 | 1.46 | +0.53 | +0.46 | yes |
| fnd6_xopr | fundamental6 | -0.18 | 1.43 | +0.48 | -0.50 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: trade_when
