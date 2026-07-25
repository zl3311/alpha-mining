---
field: fn_op_lease_min_pay_due_after_5y_a
dataset: fundamental2
best_template: rank_value_norm
best_sharpe: 0.93
best_fitness: 0.6
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: all-weather
n_variations_with_pnl: 11
max_drawdown: 0.0662
ann_vol: 0.0567
hit_rate: 0.5069
rolling_sharpe_min: -0.889
rolling_sharpe_max: 2.431
top_merge_partner: anl4_epsr_flag
redundancy_cluster: 46
negated_best_sharpe: 0.44
negated_best_template: rank_neg_delta
negated_best_fitness: 0.18
n_negated_sims: 10
direction_gap: -0.49
---
# fn_op_lease_min_pay_due_after_5y_a (fundamental2)

*Amount of required minimum rental payments for operating leases having an initial or remaining non-cancelable lease term in excess of one year due after the 5th fiscal year following the latest fiscal year. Excludes interim and annual periods when interim periods are reported on a rolling approach, from latest balance sheet date.*

## Signal Profile
- `rank(fn_op_lease_min_pay_due_after_5y_a)`: S=0.79, F=0.48, T=0.8%, INFERIOR (TOP3000)
- `rank(fn_op_lease_min_pay_due_after_5y_a / close)`: S=0.93, F=0.60, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_delta(fn_op_lease_min_pay_due_after_5y_a, 5))`: S=0.48, F=0.24, T=34.2%, INFERIOR (TOP500)
- `-rank(fn_op_lease_min_pay_due_after_5y_a)`: S=-0.45, F=-0.22, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_op_lease_min_pay_due_after_5y_a, 5))`: S=0.44, F=0.18, T=34.4%, INFERIOR (TOP3000)
- `-ts_zscore(fn_op_lease_min_pay_due_after_5y_a, 63)`: S=0.05, F=0.01, T=16.8%, INFERIOR (TOP3000)
- `ts_mean(fn_op_lease_min_pay_due_after_5y_a, 10)`: S=0.51, F=0.31, T=0.9%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_op_lease_min_pay_due_after_5y_a, 22))`: S=-0.04, F=-0.01, T=14.8%, INFERIOR (TOP3000)
- `rank(-1 * fn_op_lease_min_pay_due_after_5y_a)`: S=-0.79, F=-0.48, T=0.8%, INFERIOR (TOP3000)
- `rank(-1 * fn_op_lease_min_pay_due_after_5y_a / close)`: S=-0.93, F=-0.60, T=1.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 13F/19P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 16F/13P
- LOW_TURNOVER: 5F/27P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.92, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=1.25 (moderate), ret=+4.5%
  - 2020: S=1.72 (strong), ret=+12.4%
  - 2021: S=1.15 (moderate), ret=+6.2%
  - 2022: S=0.11 (weak), ret=+0.6%
  - 2023: S=0.34 (weak), ret=+1.9%

## Risk & Drawdown
- Max drawdown: 6.62% over 701 days (not yet recovered, ongoing at window end)
- Annualized: return +5.2%, volatility 5.7% (fraction of booksize)
- Hit rate: 50.7% positive days
- Tail shape: skew +0.85, excess kurtosis +4.26

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.89, max 2.43, latest 0.49

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2022
Best month: +5.01%; worst month: -2.77%
Positive months: 52%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=1.83
- Sideways: S=0.23
- Bear: S=0.59

## Negated Direction
Best negated: `rank(-1 * ts_delta(fn_op_lease_min_pay_due_after_5y_a, 5))` S=0.44, F=0.18, INFERIOR
Direction gap: -0.49 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fn_op_lease_min_pay_due_after_5y_a)`: S=-0.79, F=-0.48, T=0.8%, INFERIOR (TOP3000)
- `rank(-1 * fn_op_lease_min_pay_due_after_5y_a / close)`: S=-0.93, F=-0.60, T=1.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_op_lease_min_pay_due_after_5y_a, 5))`: S=0.44, F=0.18, T=34.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fn_op_lease_min_pay_due_after_5y_a / close)` | TOP3000 | 0.92 | 0.60 | 6.6% | 100% | all-weather |
| `rank(fn_op_lease_min_pay_due_after_5y_a)` | TOP3000 | 0.78 | 0.48 | 13.5% | 80% | bull-only |
| `rank(fn_op_lease_min_pay_due_after_5y_a / close)` | TOP1000 | 0.51 | 0.27 | 6.5% | 80% | bull-only |
| `rank(ts_delta(fn_op_lease_min_pay_due_after_5y_a, 5))` | TOP500 | 0.49 | 0.24 | 51.5% | 60% | all-weather |
| `rank(fn_op_lease_min_pay_due_after_5y_a)` | TOP1000 | 0.44 | 0.22 | 16.2% | 60% | bull-only |
| `rank(ts_delta(fn_op_lease_min_pay_due_after_5y_a, 5))` | TOP200 | 0.36 | 0.17 | 36.6% | 80% | mixed |
| `rank(fn_op_lease_min_pay_due_after_5y_a / close)` | TOP500 | 0.30 | 0.13 | 10.0% | 60% | bull-only |
| `rank(fn_op_lease_min_pay_due_after_5y_a / close)` | TOP200 | 0.22 | 0.09 | 21.8% | 60% | bull-only |
| `rank(fn_op_lease_min_pay_due_after_5y_a)` | TOP200 | 0.17 | 0.06 | 26.4% | 60% | bull-only |
| `rank(fn_op_lease_min_pay_due_after_5y_a)` | TOP500 | 0.15 | 0.05 | 24.7% | 60% | bull-only |
| `rank(ts_delta(fn_op_lease_min_pay_due_after_5y_a, 5))` | TOP1000 | 0.14 | 0.03 | 33.1% | 40% | all-weather |

## Correlation Notes
Top correlates:
- fn_op_lease_min_pay_due_in_5y_a: 0.962 (strongly positively correlated)
- fn_op_lease_min_pay_due_a: 0.962 (strongly positively correlated)
- fnd2_oprlsfmpdcurr: 0.937 (strongly positively correlated)
- fnd2_dfdtxastxdfdexpcompbnf: 0.879 (strongly positively correlated)
- fn_op_lease_rent_exp_a: 0.871 (strongly positively correlated)

Redundancy cluster #46: 6 similar fields, mean |rho| 0.737 (representative). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_epsr_flag | analyst4 | -0.35 | 1.77 | +0.59 | -0.06 | yes |
| anl4_capex_high | analyst4 | -0.20 | 1.46 | +0.53 | +0.46 | yes |
| rp_css_revenue | news18 | -0.25 | 1.39 | +0.47 | -0.22 | yes |
| rp_ess_revenue | news18 | -0.26 | 1.39 | +0.47 | +0.30 | yes |
| est_rd_expense | analyst4 | -0.16 | 1.57 | +0.46 | +0.62 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
