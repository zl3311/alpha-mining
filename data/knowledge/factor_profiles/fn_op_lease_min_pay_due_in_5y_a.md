---
field: fn_op_lease_min_pay_due_in_5y_a
dataset: fundamental2
best_template: rank_value_norm
best_sharpe: 0.9
best_fitness: 0.61
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: all-weather
n_variations_with_pnl: 7
max_drawdown: 0.0921
ann_vol: 0.0649
hit_rate: 0.4858
rolling_sharpe_min: -1.203
rolling_sharpe_max: 2.847
top_merge_partner: anl4_epsr_flag
redundancy_cluster: 33
negated_best_sharpe: 0.8
negated_best_template: rank_neg_delta
negated_best_fitness: 0.42
n_negated_sims: 10
direction_gap: -0.1
---
# fn_op_lease_min_pay_due_in_5y_a (fundamental2)

*Amount of required minimum rental payments for operating leases having an initial or remaining non-cancelable lease term in excess of 1 year due in the 5th fiscal year following the latest fiscal year. Excludes interim and annual periods when interim periods are reported on a rolling approach, from latest balance sheet date.*

## Signal Profile
- `rank(fn_op_lease_min_pay_due_in_5y_a)`: S=0.89, F=0.60, T=0.9%, INFERIOR (TOP3000)
- `rank(fn_op_lease_min_pay_due_in_5y_a / close)`: S=0.90, F=0.61, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_delta(fn_op_lease_min_pay_due_in_5y_a, 5))`: S=-0.19, F=-0.05, T=34.7%, INFERIOR (TOP1000)
- `-rank(fn_op_lease_min_pay_due_in_5y_a)`: S=-0.53, F=-0.30, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_op_lease_min_pay_due_in_5y_a, 5))`: S=0.80, F=0.42, T=34.4%, INFERIOR (TOP3000)
- `-ts_zscore(fn_op_lease_min_pay_due_in_5y_a, 63)`: S=0.22, F=0.10, T=17.0%, INFERIOR (TOP3000)
- `ts_mean(fn_op_lease_min_pay_due_in_5y_a, 10)`: S=0.57, F=0.38, T=0.8%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_op_lease_min_pay_due_in_5y_a, 22))`: S=0.64, F=0.39, T=14.8%, INFERIOR (TOP3000)
- `rank(-1 * fn_op_lease_min_pay_due_in_5y_a)`: S=-0.89, F=-0.60, T=0.9%, INFERIOR (TOP3000)
- `rank(-1 * fn_op_lease_min_pay_due_in_5y_a / close)`: S=-0.90, F=-0.61, T=1.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 13F/19P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 15F/14P
- LOW_TURNOVER: 5F/27P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.90, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=1.03 (moderate), ret=+4.4%
  - 2020: S=1.81 (strong), ret=+15.0%
  - 2021: S=1.71 (strong), ret=+9.2%
  - 2022: S=-0.18 (negative), ret=-1.2%
  - 2023: S=0.16 (weak), ret=+1.0%

## Risk & Drawdown
- Max drawdown: 9.21% over 640 days (not yet recovered, ongoing at window end)
- Annualized: return +5.8%, volatility 6.5% (fraction of booksize)
- Hit rate: 48.6% positive days
- Tail shape: skew +0.85, excess kurtosis +3.78

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.20, max 2.85, latest 0.33

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2022
Best month: +6.40%; worst month: -3.32%
Positive months: 58%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=1.51
- Sideways: S=-0.08
- Bear: S=1.17

## Negated Direction
Best negated: `rank(-1 * ts_delta(fn_op_lease_min_pay_due_in_5y_a, 5))` S=0.80, F=0.42, INFERIOR
Direction gap: -0.10 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fn_op_lease_min_pay_due_in_5y_a)`: S=-0.89, F=-0.60, T=0.9%, INFERIOR (TOP3000)
- `rank(-1 * fn_op_lease_min_pay_due_in_5y_a / close)`: S=-0.90, F=-0.61, T=1.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_op_lease_min_pay_due_in_5y_a, 5))`: S=0.80, F=0.42, T=34.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fn_op_lease_min_pay_due_in_5y_a / close)` | TOP3000 | 0.90 | 0.61 | 9.2% | 80% | all-weather |
| `rank(fn_op_lease_min_pay_due_in_5y_a)` | TOP3000 | 0.89 | 0.60 | 13.0% | 80% | bull-only |
| `rank(fn_op_lease_min_pay_due_in_5y_a)` | TOP1000 | 0.53 | 0.30 | 18.2% | 80% | bull-only |
| `rank(fn_op_lease_min_pay_due_in_5y_a / close)` | TOP1000 | 0.54 | 0.29 | 6.8% | 80% | mixed |
| `rank(fn_op_lease_min_pay_due_in_5y_a / close)` | TOP500 | 0.20 | 0.07 | 13.1% | 60% | bull-only |
| `rank(fn_op_lease_min_pay_due_in_5y_a)` | TOP500 | 0.14 | 0.05 | 28.9% | 80% | bull-only |
| `rank(fn_op_lease_min_pay_due_in_5y_a)` | TOP200 | 0.09 | 0.03 | 32.0% | 40% | bull-only |

## Correlation Notes
Top correlates:
- fn_op_lease_min_pay_due_a: 0.965 (strongly positively correlated)
- fn_op_lease_min_pay_due_after_5y_a: 0.962 (strongly positively correlated)
- fnd2_oprlsfmpdcurr: 0.957 (strongly positively correlated)
- fnd2_dfdtxastxdfdexpcompbnf: 0.901 (strongly positively correlated)
- fn_op_lease_rent_exp_a: 0.877 (strongly positively correlated)

Redundancy cluster #33: 12 similar fields, mean |rho| 0.787 (representative: anl4_afv4_eps_high). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_epsr_flag | analyst4 | -0.35 | 1.79 | +0.61 | -0.30 | yes |
| rp_css_revenue | news18 | -0.27 | 1.42 | +0.52 | -0.20 | yes |
| eps_guidance_value_quarterly | analyst4 | -0.17 | 1.34 | +0.44 | -0.71 | yes |
| anl4_capex_high | analyst4 | -0.20 | 1.43 | +0.50 | +0.43 | yes |
| rp_css_ptg | news18 | -0.24 | 1.50 | +0.50 | +0.52 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
