---
field: fnd2_oprlsfmpdcurr
dataset: fundamental2
cluster: fundamental2_analyst_rating
coverage: 0.6378
community_alphas: 1264
best_template: rank_value_norm
best_sharpe: 0.79
best_fitness: 0.53
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 5
max_drawdown: 0.0957
ann_vol: 0.0721
hit_rate: 0.481
rolling_sharpe_min: -1.262
rolling_sharpe_max: 2.701
redundancy_cluster: 1
negated_best_sharpe: 0.61
negated_best_template: rank_neg_delta
negated_best_fitness: 0.31
n_negated_sims: 10
direction_gap: -0.18
---
# fnd2_oprlsfmpdcurr (fundamental2)

*Amount of required minimum rental payments for operating leases having an initial or remaining non-cancelable lease term in excess of 1 year due in the next fiscal year following the latest fiscal year. Excludes interim and annual periods when interim periods are reported on a rolling approach, from latest balance sheet date.*

## Signal Profile
- `rank(fnd2_oprlsfmpdcurr)`: S=0.73, F=0.51, T=0.9%, INFERIOR (TOP3000)
- `rank(fnd2_oprlsfmpdcurr / close)`: S=0.79, F=0.53, T=1.3%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd2_oprlsfmpdcurr, 5))`: S=-0.08, F=-0.02, T=31.1%, INFERIOR (TOP200)
- `-rank(fnd2_oprlsfmpdcurr)`: S=-0.37, F=-0.20, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_oprlsfmpdcurr, 5))`: S=0.61, F=0.31, T=34.5%, INFERIOR (TOP3000)
- `ts_zscore(fnd2_oprlsfmpdcurr, 22)`: S=0.09, F=0.03, T=23.8%, INFERIOR (TOP3000)
- `ts_mean(fnd2_oprlsfmpdcurr, 10)`: S=0.41, F=0.23, T=0.9%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd2_oprlsfmpdcurr, 22))`: S=-0.13, F=-0.04, T=14.7%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_oprlsfmpdcurr)`: S=-0.37, F=-0.20, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_oprlsfmpdcurr / close)`: S=-0.42, F=-0.22, T=1.6%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 13F/19P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 17F/12P
- LOW_TURNOVER: 2F/30P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.79, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.39 (weak), ret=+1.8%
  - 2020: S=1.49 (moderate), ret=+13.9%
  - 2021: S=1.22 (moderate), ret=+8.4%
  - 2022: S=0.23 (weak), ret=+1.5%
  - 2023: S=0.32 (weak), ret=+2.2%

## Risk & Drawdown
- Max drawdown: 9.57% over 591 days (not yet recovered, ongoing at window end)
- Annualized: return +5.7%, volatility 7.2% (fraction of booksize)
- Hit rate: 48.1% positive days
- Tail shape: skew +0.85, excess kurtosis +3.82

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.26, max 2.70, latest 0.49

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2022
Best month: +6.13%; worst month: -3.83%
Positive months: 59%

## Regime Profile
Regime profile: **mixed**
- Bull: S=1.86
- Sideways: S=-0.12
- Bear: S=0.47

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd2_oprlsfmpdcurr, 5))` S=0.61, F=0.31, INFERIOR
Direction gap: -0.18 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd2_oprlsfmpdcurr)`: S=-0.37, F=-0.20, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_oprlsfmpdcurr / close)`: S=-0.42, F=-0.22, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_oprlsfmpdcurr, 5))`: S=0.61, F=0.31, T=34.5%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd2_oprlsfmpdcurr / close)` | TOP3000 | 0.79 | 0.53 | 9.6% | 100% | mixed |
| `rank(fnd2_oprlsfmpdcurr)` | TOP3000 | 0.72 | 0.51 | 18.0% | 80% | bull-only |
| `rank(fnd2_oprlsfmpdcurr / close)` | TOP1000 | 0.41 | 0.22 | 9.6% | 60% | bull-only |
| `rank(fnd2_oprlsfmpdcurr)` | TOP1000 | 0.36 | 0.20 | 26.5% | 60% | bull-only |
| `rank(fnd2_oprlsfmpdcurr / close)` | TOP500 | 0.10 | 0.03 | 20.3% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fn_op_lease_min_pay_due_a: 0.982 (strongly positively correlated)
- fn_op_lease_min_pay_due_in_5y_a: 0.957 (strongly positively correlated)
- fn_op_lease_rent_exp_a: 0.941 (strongly positively correlated)
- fn_op_lease_min_pay_due_after_5y_a: 0.937 (strongly positively correlated)
- fnd2_dfdtxastxdfdexpcompbnf: 0.930 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
