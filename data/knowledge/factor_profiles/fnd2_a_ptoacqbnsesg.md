---
field: fnd2_a_ptoacqbnsesg
dataset: fundamental2
best_template: rank_neg_delta
best_sharpe: 0.94
best_fitness: 0.71
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 4
max_drawdown: 0.048
ann_vol: 0.0441
hit_rate: 0.5004
rolling_sharpe_min: -1.148
rolling_sharpe_max: 1.985
redundancy_cluster: 33
negated_best_sharpe: 0.94
negated_best_template: rank_neg_delta
negated_best_fitness: 0.71
n_negated_sims: 10
direction_gap: 0.29
---
# fnd2_a_ptoacqbnsesg (fundamental2)

*The cash outflow associated with the acquisition of business during the period. The cash portion only of the acquisition price.*

## Signal Profile
- `rank(fnd2_a_ptoacqbnsesg)`: S=0.43, F=0.17, T=0.7%, INFERIOR (TOP3000)
- `rank(fnd2_a_ptoacqbnsesg / close)`: S=0.72, F=0.36, T=1.0%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd2_a_ptoacqbnsesg, 5))`: S=0.29, F=0.13, T=24.1%, INFERIOR (TOP500)
- `-rank(fnd2_a_ptoacqbnsesg)`: S=-0.04, F=-0.01, T=1.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_a_ptoacqbnsesg, 5))`: S=0.94, F=0.71, T=31.2%, INFERIOR (TOP3000)
- `ts_zscore(fnd2_a_ptoacqbnsesg, 22)`: S=0.08, F=0.02, T=8.0%, INFERIOR (TOP3000)
- `ts_mean(fnd2_a_ptoacqbnsesg, 10)`: S=0.22, F=0.08, T=0.9%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd2_a_ptoacqbnsesg, 22))`: S=0.65, F=0.50, T=16.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_a_ptoacqbnsesg)`: S=-0.43, F=-0.17, T=0.7%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_a_ptoacqbnsesg / close)`: S=-0.72, F=-0.36, T=1.0%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 20F/9P
- LOW_TURNOVER: 5F/27P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.71, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=1.10 (moderate), ret=+3.3%
  - 2020: S=1.06 (moderate), ret=+6.2%
  - 2021: S=0.64 (moderate), ret=+2.9%
  - 2022: S=0.74 (moderate), ret=+3.0%
  - 2023: S=-0.00 (negative), ret=-0.0%

## Risk & Drawdown
- Max drawdown: 4.80% over 582 days (not yet recovered, ongoing at window end)
- Annualized: return +3.1%, volatility 4.4% (fraction of booksize)
- Hit rate: 50.0% positive days
- Tail shape: skew +0.72, excess kurtosis +4.63

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.15, max 1.99, latest 0.26

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2023
Best month: +3.16%; worst month: -2.64%
Positive months: 56%

## Regime Profile
Regime profile: **mixed**
- Bull: S=1.29
- Sideways: S=0.46
- Bear: S=0.33

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd2_a_ptoacqbnsesg, 5))` S=0.94, F=0.71, INFERIOR
Direction gap: +0.29 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fnd2_a_ptoacqbnsesg)`: S=-0.43, F=-0.17, T=0.7%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_a_ptoacqbnsesg / close)`: S=-0.72, F=-0.36, T=1.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_a_ptoacqbnsesg, 5))`: S=0.94, F=0.71, T=31.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd2_a_ptoacqbnsesg / close)` | TOP3000 | 0.71 | 0.36 | 4.8% | 80% | mixed |
| `rank(fnd2_a_ptoacqbnsesg)` | TOP3000 | 0.43 | 0.17 | 11.9% | 60% | bull-only |
| `rank(ts_delta(fnd2_a_ptoacqbnsesg, 5))` | TOP500 | 0.28 | 0.13 | 34.1% | 60% | bull-only |
| `rank(fnd2_a_ptoacqbnsesg / close)` | TOP1000 | 0.17 | 0.05 | 14.2% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fn_business_combination_purchase_price_a: 0.846 (strongly positively correlated)
- fnd2_oprlsfmpdcurr: 0.829 (strongly positively correlated)
- fnd2_a_flintasamt1expnext12m: 0.824 (strongly positively correlated)
- fn_op_lease_min_pay_due_a: 0.818 (strongly positively correlated)
- fnd2_a_flintasamt1expytwo: 0.816 (strongly positively correlated)

Redundancy cluster #33: 12 similar fields, mean |rho| 0.787 (representative: anl4_afv4_eps_high). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
