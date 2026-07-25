---
field: cash_flow_from_operations
dataset: analyst4
best_template: rank_value_norm
best_sharpe: 0.41
best_fitness: 0.26
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 4
max_drawdown: 0.3163
ann_vol: 0.1208
hit_rate: 0.5061
rolling_sharpe_min: -3.135
rolling_sharpe_max: 2.447
negated_best_sharpe: 0.36
negated_best_template: rank_neg_delta
negated_best_fitness: 0.08
n_negated_sims: 10
direction_gap: -0.05
---
# cash_flow_from_operations (analyst4)

*Cash Flow from Operations - Value for the annual period*

## Signal Profile
- `rank(cash_flow_from_operations)`: S=0.14, F=0.06, T=1.1%, INFERIOR (TOP3000)
- `rank(cash_flow_from_operations / close)`: S=0.41, F=0.26, T=1.5%, INFERIOR (TOP3000)
- `rank(ts_delta(cash_flow_from_operations, 5))`: S=0.16, F=0.03, T=34.1%, INFERIOR (TOP200)
- `-rank(cash_flow_from_operations)`: S=-0.01, F=0.00, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(cash_flow_from_operations, 5))`: S=0.36, F=0.08, T=35.7%, INFERIOR (TOP3000)
- `-ts_zscore(cash_flow_from_operations, 63)`: S=0.24, F=0.07, T=20.5%, INFERIOR (TOP3000)
- `ts_mean(cash_flow_from_operations, 10)`: S=-0.16, F=-0.06, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_rank(cash_flow_from_operations, 22))`: S=-0.28, F=-0.09, T=13.4%, INFERIOR (TOP3000)
- `rank(-1 * cash_flow_from_operations)`: S=-0.14, F=-0.06, T=1.1%, INFERIOR (TOP3000)
- `rank(-1 * cash_flow_from_operations / close)`: S=-0.41, F=-0.26, T=1.5%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 2F/30P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 17F/12P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.40, Consistency 40% positive years (2/5)
Yearly breakdown:
  - 2019: S=-0.01 (negative), ret=-0.1%
  - 2020: S=-2.23 (negative), ret=-18.8%
  - 2021: S=1.16 (moderate), ret=+16.6%
  - 2022: S=1.58 (strong), ret=+27.0%
  - 2023: S=-0.07 (negative), ret=-0.8%

## Risk & Drawdown
- Max drawdown: 31.63% over 795 days (recovered)
- Annualized: return +4.9%, volatility 12.1% (fraction of booksize)
- Hit rate: 50.6% positive days
- Tail shape: skew -0.01, excess kurtosis +1.32

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -3.13, max 2.45, latest -0.27

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +9.81%; worst month: -5.86%
Positive months: 48%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.34
- Sideways: S=0.54
- Bear: S=-3.60

## Negated Direction
Best negated: `rank(-1 * ts_delta(cash_flow_from_operations, 5))` S=0.36, F=0.08, INFERIOR
Direction gap: -0.05 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * cash_flow_from_operations)`: S=-0.14, F=-0.06, T=1.1%, INFERIOR (TOP3000)
- `rank(-1 * cash_flow_from_operations / close)`: S=-0.41, F=-0.26, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(cash_flow_from_operations, 5))`: S=0.36, F=0.08, T=35.7%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(cash_flow_from_operations / close)` | TOP3000 | 0.40 | 0.26 | 31.6% | 40% | bull-only |
| `rank(cash_flow_from_operations / close)` | TOP1000 | 0.17 | 0.08 | 32.9% | 60% | bull-only |
| `rank(cash_flow_from_operations)` | TOP3000 | 0.13 | 0.06 | 49.0% | 60% | bull-only |
| `rank(ts_delta(cash_flow_from_operations, 5))` | TOP200 | 0.15 | 0.03 | 30.5% | 60% | bull-only |

## Correlation Notes
Top correlates:
- operating_profit_before_interest_tax: 0.979 (strongly positively correlated)
- fnd6_mfma2_oancf: 0.977 (strongly positively correlated)
- cashflow_op: 0.977 (strongly positively correlated)
- fnd6_newa2v1300_oancf: 0.977 (strongly positively correlated)
- net_income_adjusted: 0.974 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
