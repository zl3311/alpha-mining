---
field: fn_op_lease_min_pay_due_in_2y_a
dataset: fundamental2
best_template: rank_neg_delta
best_sharpe: 1.06
best_fitness: 0.71
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 7
max_drawdown: 0.1623
ann_vol: 0.0803
hit_rate: 0.5206
rolling_sharpe_min: -1.875
rolling_sharpe_max: 2.338
redundancy_cluster: 13
negated_best_sharpe: 1.06
negated_best_template: rank_neg_delta
negated_best_fitness: 0.71
n_negated_sims: 10
direction_gap: 0.26
---
# fn_op_lease_min_pay_due_in_2y_a (fundamental2)

*Amount of required minimum rental payments for operating leases having an initial or remaining non-cancelable lease term in excess of 1 year due in the 2nd fiscal year following the latest fiscal year. Excludes interim and annual periods when interim periods are reported on a rolling approach, from latest balance sheet date.*

## Signal Profile
- `rank(fn_op_lease_min_pay_due_in_2y_a)`: S=0.80, F=0.57, T=0.9%, INFERIOR (TOP3000)
- `rank(fn_op_lease_min_pay_due_in_2y_a / close)`: S=0.82, F=0.56, T=1.3%, INFERIOR (TOP3000)
- `rank(ts_delta(fn_op_lease_min_pay_due_in_2y_a, 5))`: S=0.34, F=0.15, T=31.6%, INFERIOR (TOP200)
- `-rank(fn_op_lease_min_pay_due_in_2y_a)`: S=-0.47, F=-0.28, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_op_lease_min_pay_due_in_2y_a, 5))`: S=1.06, F=0.71, T=34.6%, INFERIOR (TOP3000)
- `-ts_zscore(fn_op_lease_min_pay_due_in_2y_a, 63)`: S=-0.17, F=-0.06, T=16.9%, INFERIOR (TOP3000)
- `ts_mean(fn_op_lease_min_pay_due_in_2y_a, 10)`: S=0.58, F=0.39, T=0.8%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_op_lease_min_pay_due_in_2y_a, 22))`: S=-0.68, F=-0.44, T=14.7%, INFERIOR (TOP3000)
- `rank(-1 * fn_op_lease_min_pay_due_in_2y_a)`: S=-0.47, F=-0.28, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * fn_op_lease_min_pay_due_in_2y_a / close)`: S=-0.50, F=-0.28, T=1.6%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 13F/19P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 12F/17P
- LOW_TURNOVER: 2F/30P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.79, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=1.17 (moderate), ret=+4.7%
  - 2020: S=-0.26 (negative), ret=-1.5%
  - 2021: S=1.04 (moderate), ret=+12.4%
  - 2022: S=1.34 (moderate), ret=+12.5%
  - 2023: S=0.53 (moderate), ret=+3.1%

## Risk & Drawdown
- Max drawdown: 16.23% over 400 days (recovered)
- Annualized: return +6.4%, volatility 8.0% (fraction of booksize)
- Hit rate: 52.1% positive days
- Tail shape: skew -0.00, excess kurtosis +2.02

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.88, max 2.34, latest 0.33

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +5.52%; worst month: -4.31%
Positive months: 64%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.83
- Sideways: S=1.47
- Bear: S=-2.38

## Negated Direction
Best negated: `rank(-1 * ts_delta(fn_op_lease_min_pay_due_in_2y_a, 5))` S=1.06, F=0.71, INFERIOR
Direction gap: +0.26 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fn_op_lease_min_pay_due_in_2y_a)`: S=-0.47, F=-0.28, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * fn_op_lease_min_pay_due_in_2y_a / close)`: S=-0.50, F=-0.28, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_op_lease_min_pay_due_in_2y_a, 5))`: S=1.06, F=0.71, T=34.6%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fn_op_lease_min_pay_due_in_2y_a)` | TOP3000 | 0.79 | 0.57 | 16.2% | 80% | bull-only |
| `rank(fn_op_lease_min_pay_due_in_2y_a / close)` | TOP3000 | 0.81 | 0.56 | 8.9% | 100% | all-weather |
| `rank(fn_op_lease_min_pay_due_in_2y_a)` | TOP1000 | 0.47 | 0.28 | 23.4% | 60% | bull-only |
| `rank(fn_op_lease_min_pay_due_in_2y_a / close)` | TOP1000 | 0.50 | 0.28 | 8.7% | 60% | bull-only |
| `rank(ts_delta(fn_op_lease_min_pay_due_in_2y_a, 5))` | TOP200 | 0.34 | 0.15 | 25.1% | 60% | bull-only |
| `rank(fn_op_lease_min_pay_due_in_2y_a / close)` | TOP500 | 0.19 | 0.07 | 18.1% | 60% | bull-only |
| `rank(fn_op_lease_min_pay_due_in_2y_a)` | TOP500 | 0.07 | 0.02 | 35.1% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fn_op_lease_min_pay_due_in_3y_a: 0.996 (strongly positively correlated)
- fn_op_lease_min_pay_due_in_4y_a: 0.989 (strongly positively correlated)
- fnd6_mrc2: 0.982 (strongly positively correlated)
- fnd6_mrc3: 0.979 (strongly positively correlated)
- fnd6_mrc4: 0.974 (strongly positively correlated)

Redundancy cluster #13: 127 similar fields, mean |rho| 0.82 (representative: anl4_bvps_flag). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
