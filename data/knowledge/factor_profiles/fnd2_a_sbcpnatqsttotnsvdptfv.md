---
field: fnd2_a_sbcpnatqsttotnsvdptfv
dataset: fundamental2
best_template: rank_value_norm
best_sharpe: 0.79
best_fitness: 0.47
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: all-weather
n_variations_with_pnl: 7
max_drawdown: 0.1208
ann_vol: 0.0557
hit_rate: 0.5077
rolling_sharpe_min: -1.675
rolling_sharpe_max: 2.916
redundancy_cluster: 46
negated_best_sharpe: 0.11
negated_best_template: rank_neg_delta
negated_best_fitness: 0.03
n_negated_sims: 10
direction_gap: -0.68
---
# fnd2_a_sbcpnatqsttotnsvdptfv (fundamental2)

*Fair value of share-based awards for which the grantee gained the right by satisfying service and performance requirements, to receive or retain shares or units, other instruments, or cash.*

## Signal Profile
- `rank(fnd2_a_sbcpnatqsttotnsvdptfv)`: S=0.29, F=0.11, T=1.3%, INFERIOR (TOP1000)
- `rank(fnd2_a_sbcpnatqsttotnsvdptfv / close)`: S=0.79, F=0.47, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd2_a_sbcpnatqsttotnsvdptfv, 5))`: S=0.03, F=0.00, T=32.1%, INFERIOR (TOP500)
- `-rank(fnd2_a_sbcpnatqsttotnsvdptfv)`: S=-0.29, F=-0.11, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_a_sbcpnatqsttotnsvdptfv, 5))`: S=0.11, F=0.03, T=26.1%, INFERIOR (TOP3000)
- `ts_zscore(fnd2_a_sbcpnatqsttotnsvdptfv, 22)`: S=0.15, F=0.06, T=17.5%, INFERIOR (TOP3000)
- `ts_mean(fnd2_a_sbcpnatqsttotnsvdptfv, 10)`: S=0.37, F=0.25, T=0.6%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd2_a_sbcpnatqsttotnsvdptfv, 22))`: S=-0.01, F=0.00, T=15.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_a_sbcpnatqsttotnsvdptfv)`: S=-0.11, F=-0.03, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_a_sbcpnatqsttotnsvdptfv / close)`: S=-0.15, F=-0.05, T=2.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 10F/10P
- LOW_TURNOVER: 2F/30P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.79, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.39 (weak), ret=+1.5%
  - 2020: S=2.02 (strong), ret=+12.9%
  - 2021: S=1.54 (strong), ret=+6.9%
  - 2022: S=-0.72 (negative), ret=-4.3%
  - 2023: S=0.81 (moderate), ret=+4.8%

## Risk & Drawdown
- Max drawdown: 12.08% over 640 days (not yet recovered, ongoing at window end)
- Annualized: return +4.4%, volatility 5.6% (fraction of booksize)
- Hit rate: 50.8% positive days
- Tail shape: skew +0.38, excess kurtosis +2.20

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.68, max 2.92, latest 0.91

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2022
Best month: +4.82%; worst month: -3.00%
Positive months: 56%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=1.26
- Sideways: S=0.27
- Bear: S=0.83

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd2_a_sbcpnatqsttotnsvdptfv, 5))` S=0.11, F=0.03, INFERIOR
Direction gap: -0.68 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd2_a_sbcpnatqsttotnsvdptfv)`: S=-0.11, F=-0.03, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_a_sbcpnatqsttotnsvdptfv / close)`: S=-0.15, F=-0.05, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_a_sbcpnatqsttotnsvdptfv, 5))`: S=0.11, F=0.03, T=26.1%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd2_a_sbcpnatqsttotnsvdptfv / close)` | TOP3000 | 0.79 | 0.47 | 12.1% | 80% | all-weather |
| `rank(fnd2_a_sbcpnatqsttotnsvdptfv / close)` | TOP1000 | 0.49 | 0.23 | 7.9% | 80% | bull-only |
| `rank(fnd2_a_sbcpnatqsttotnsvdptfv)` | TOP1000 | 0.29 | 0.11 | 19.2% | 80% | bull-only |
| `rank(fnd2_a_sbcpnatqsttotnsvdptfv / close)` | TOP200 | 0.16 | 0.05 | 34.3% | 60% | bull-only |
| `rank(fnd2_a_sbcpnatqsttotnsvdptfv / close)` | TOP500 | 0.15 | 0.04 | 19.8% | 60% | bull-only |
| `rank(fnd2_a_sbcpnatqsttotnsvdptfv)` | TOP200 | 0.12 | 0.03 | 33.0% | 80% | bull-only |
| `rank(fnd2_a_sbcpnatqsttotnsvdptfv)` | TOP3000 | 0.09 | 0.02 | 16.2% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fn_op_lease_min_pay_due_in_5y_a: 0.801 (strongly positively correlated)
- fnd2_oprlsfmpdcurr: 0.800 (strongly positively correlated)
- fn_op_lease_min_pay_due_a: 0.794 (strongly positively correlated)
- fn_allocated_share_based_compensation_expense_a: 0.791 (strongly positively correlated)
- est_sga: 0.788 (strongly positively correlated)

Redundancy cluster #46: 6 similar fields, mean |rho| 0.737 (representative: fn_op_lease_min_pay_due_after_5y_a). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
