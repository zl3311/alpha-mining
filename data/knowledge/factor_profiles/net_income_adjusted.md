---
field: net_income_adjusted
dataset: analyst4
best_template: rank_value_norm
best_sharpe: 0.32
best_fitness: 0.17
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 4
max_drawdown: 0.2858
ann_vol: 0.1085
hit_rate: 0.4947
rolling_sharpe_min: -3.306
rolling_sharpe_max: 2.178
negated_best_sharpe: 0.41
negated_best_template: rank_neg_delta
negated_best_fitness: 0.09
n_negated_sims: 10
direction_gap: 0.09
---
# net_income_adjusted (analyst4)

*Adjusted net income- announced financial value for annual frequency*

## Signal Profile
- `rank(net_income_adjusted)`: S=0.09, F=0.03, T=1.0%, INFERIOR (TOP3000)
- `rank(net_income_adjusted / close)`: S=0.32, F=0.17, T=1.3%, INFERIOR (TOP3000)
- `rank(ts_delta(net_income_adjusted, 5))`: S=0.12, F=0.02, T=36.8%, INFERIOR (TOP500)
- `-rank(net_income_adjusted)`: S=0.06, F=0.02, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(net_income_adjusted, 5))`: S=0.41, F=0.09, T=34.7%, INFERIOR (TOP3000)
- `-ts_zscore(net_income_adjusted, 63)`: S=0.36, F=0.12, T=21.4%, INFERIOR (TOP3000)
- `ts_mean(net_income_adjusted, 10)`: S=-0.13, F=-0.04, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_rank(net_income_adjusted, 22))`: S=0.06, F=0.01, T=13.3%, INFERIOR (TOP3000)
- `rank(-1 * net_income_adjusted)`: S=-0.09, F=-0.03, T=1.0%, INFERIOR (TOP3000)
- `rank(-1 * net_income_adjusted / close)`: S=-0.32, F=-0.17, T=1.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 2F/30P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/16P
- LOW_TURNOVER: 4F/28P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.30, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.20 (weak), ret=+1.0%
  - 2020: S=-2.20 (negative), ret=-15.0%
  - 2021: S=0.79 (moderate), ret=+10.3%
  - 2022: S=1.34 (moderate), ret=+20.8%
  - 2023: S=-0.09 (negative), ret=-0.9%

## Risk & Drawdown
- Max drawdown: 28.58% over 818 days (recovered)
- Annualized: return +3.3%, volatility 10.8% (fraction of booksize)
- Hit rate: 49.5% positive days
- Tail shape: skew +0.00, excess kurtosis +1.53

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -3.31, max 2.18, latest -0.27

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +8.49%; worst month: -5.81%
Positive months: 49%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.03
- Sideways: S=0.60
- Bear: S=-3.70

## Negated Direction
Best negated: `rank(-1 * ts_delta(net_income_adjusted, 5))` S=0.41, F=0.09, INFERIOR
Direction gap: +0.09 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * net_income_adjusted)`: S=-0.09, F=-0.03, T=1.0%, INFERIOR (TOP3000)
- `rank(-1 * net_income_adjusted / close)`: S=-0.32, F=-0.17, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(net_income_adjusted, 5))`: S=0.41, F=0.09, T=34.7%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(net_income_adjusted / close)` | TOP3000 | 0.30 | 0.17 | 28.6% | 60% | bull-only |
| `rank(net_income_adjusted / close)` | TOP1000 | 0.10 | 0.04 | 33.0% | 60% | bull-only |
| `rank(net_income_adjusted)` | TOP3000 | 0.08 | 0.03 | 43.1% | 60% | bull-only |
| `rank(ts_delta(net_income_adjusted, 5))` | TOP500 | 0.12 | 0.02 | 12.6% | 60% | bull-only |

## Correlation Notes
Top correlates:
- pretax_income_total: 0.989 (strongly positively correlated)
- operating_profit_before_interest_tax: 0.988 (strongly positively correlated)
- net_income_total_2: 0.987 (strongly positively correlated)
- cash_flow_from_operations: 0.974 (strongly positively correlated)
- cashflow_op: 0.968 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
