---
field: fn_op_lease_min_pay_due_a
dataset: fundamental2
cluster: fundamental2_other
coverage: 0.6027
community_alphas: 1464
best_template: rank_value_norm
best_sharpe: 0.81
best_fitness: 0.54
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: all-weather
n_variations_with_pnl: 6
max_drawdown: 0.0933
ann_vol: 0.0698
hit_rate: 0.4915
rolling_sharpe_min: -1.281
rolling_sharpe_max: 2.545
redundancy_cluster: 12
negated_best_sharpe: 0.58
negated_best_template: rank_neg_delta
negated_best_fitness: 0.31
n_negated_sims: 10
direction_gap: -0.23
---
# fn_op_lease_min_pay_due_a (fundamental2)

*Amount of required minimum rental payments for leases having an initial or remaining non-cancelable letter-terms in excess of 1 year.*

## Signal Profile
- `rank(fn_op_lease_min_pay_due_a)`: S=0.74, F=0.50, T=0.9%, INFERIOR (TOP3000)
- `rank(fn_op_lease_min_pay_due_a / close)`: S=0.81, F=0.54, T=1.3%, INFERIOR (TOP3000)
- `rank(ts_delta(fn_op_lease_min_pay_due_a, 5))`: S=0.29, F=0.12, T=30.4%, INFERIOR (TOP200)
- `-rank(fn_op_lease_min_pay_due_a)`: S=-0.41, F=-0.22, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_op_lease_min_pay_due_a, 5))`: S=0.58, F=0.31, T=34.8%, INFERIOR (TOP3000)
- `-ts_zscore(fn_op_lease_min_pay_due_a, 63)`: S=0.55, F=0.38, T=16.7%, INFERIOR (TOP3000)
- `ts_mean(fn_op_lease_min_pay_due_a, 10)`: S=0.49, F=0.30, T=0.8%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_op_lease_min_pay_due_a, 22))`: S=0.20, F=0.07, T=14.8%, INFERIOR (TOP3000)
- `rank(-1 * fn_op_lease_min_pay_due_a)`: S=-0.05, F=-0.01, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * fn_op_lease_min_pay_due_a / close)`: S=-0.20, F=-0.07, T=1.9%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 13F/19P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 21F/8P
- LOW_TURNOVER: 2F/30P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.80, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.71 (moderate), ret=+3.2%
  - 2020: S=1.65 (strong), ret=+14.3%
  - 2021: S=1.23 (moderate), ret=+8.6%
  - 2022: S=-0.11 (negative), ret=-0.7%
  - 2023: S=0.29 (weak), ret=+1.9%

## Risk & Drawdown
- Max drawdown: 9.33% over 701 days (not yet recovered, ongoing at window end)
- Annualized: return +5.6%, volatility 7.0% (fraction of booksize)
- Hit rate: 49.1% positive days
- Tail shape: skew +0.82, excess kurtosis +3.77

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.28, max 2.54, latest 0.45

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2022
Best month: +5.85%; worst month: -3.43%
Positive months: 59%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=1.82
- Sideways: S=-0.10
- Bear: S=0.50

## Negated Direction
Best negated: `rank(-1 * ts_delta(fn_op_lease_min_pay_due_a, 5))` S=0.58, F=0.31, INFERIOR
Direction gap: -0.23 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fn_op_lease_min_pay_due_a)`: S=-0.05, F=-0.01, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * fn_op_lease_min_pay_due_a / close)`: S=-0.20, F=-0.07, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_op_lease_min_pay_due_a, 5))`: S=0.58, F=0.31, T=34.8%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fn_op_lease_min_pay_due_a / close)` | TOP3000 | 0.80 | 0.54 | 9.3% | 80% | all-weather |
| `rank(fn_op_lease_min_pay_due_a)` | TOP3000 | 0.73 | 0.50 | 17.0% | 80% | bull-only |
| `rank(fn_op_lease_min_pay_due_a / close)` | TOP1000 | 0.49 | 0.28 | 7.8% | 80% | bull-only |
| `rank(fn_op_lease_min_pay_due_a)` | TOP1000 | 0.41 | 0.22 | 23.5% | 60% | bull-only |
| `rank(ts_delta(fn_op_lease_min_pay_due_a, 5))` | TOP200 | 0.29 | 0.12 | 32.0% | 80% | mixed |
| `rank(fn_op_lease_min_pay_due_a / close)` | TOP500 | 0.20 | 0.07 | 16.5% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd2_oprlsfmpdcurr: 0.982 (strongly positively correlated)
- fn_op_lease_min_pay_due_in_5y_a: 0.965 (strongly positively correlated)
- fn_op_lease_min_pay_due_after_5y_a: 0.962 (strongly positively correlated)
- fnd2_dfdtxastxdfdexpcompbnf: 0.918 (strongly positively correlated)
- fn_op_lease_rent_exp_a: 0.911 (strongly positively correlated)

Redundancy cluster #12: 12 similar fields, mean |rho| 0.749 (representative: fnd6_dlto). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
