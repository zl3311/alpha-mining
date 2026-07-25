---
field: pretax_income_total
dataset: analyst4
best_template: neg_rank_level
best_sharpe: 0.3
best_fitness: 0.19
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 2
max_drawdown: 0.3266
ann_vol: 0.1179
hit_rate: 0.5045
rolling_sharpe_min: -3.861
rolling_sharpe_max: 2.211
negated_best_sharpe: 0.3
negated_best_template: neg_rank_level
negated_best_fitness: 0.19
n_negated_sims: 10
direction_gap: 0.01
---
# pretax_income_total (analyst4)

*Pretax Profit - Value for the annual period*

## Signal Profile
- `rank(pretax_income_total)`: S=0.13, F=0.05, T=1.0%, INFERIOR (TOP3000)
- `rank(pretax_income_total / close)`: S=0.29, F=0.15, T=1.4%, INFERIOR (TOP3000)
- `rank(ts_delta(pretax_income_total, 5))`: S=-0.16, F=-0.02, T=36.3%, INFERIOR (TOP1000)
- `-rank(pretax_income_total)`: S=0.07, F=0.02, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(pretax_income_total, 5))`: S=0.44, F=0.14, T=34.8%, INFERIOR (TOP3000)
- `ts_zscore(pretax_income_total, 22)`: S=0.26, F=0.06, T=39.8%, INFERIOR (TOP3000)
- `ts_mean(pretax_income_total, 10)`: S=-0.13, F=-0.04, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_rank(pretax_income_total, 22))`: S=-0.06, F=-0.01, T=13.4%, INFERIOR (TOP3000)
- `rank(-1 * pretax_income_total)`: S=0.30, F=0.19, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * pretax_income_total / close)`: S=0.21, F=0.11, T=2.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 5F/27P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 17F/3P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.28, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.03 (negative), ret=-0.2%
  - 2020: S=-2.70 (negative), ret=-18.4%
  - 2021: S=0.89 (moderate), ret=+12.3%
  - 2022: S=1.30 (moderate), ret=+22.4%
  - 2023: S=0.01 (weak), ret=+0.1%

## Risk & Drawdown
- Max drawdown: 32.66% over 821 days (recovered)
- Annualized: return +3.3%, volatility 11.8% (fraction of booksize)
- Hit rate: 50.4% positive days
- Tail shape: skew -0.02, excess kurtosis +1.57

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -3.86, max 2.21, latest -0.19

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +8.29%; worst month: -6.74%
Positive months: 48%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.83
- Sideways: S=0.69
- Bear: S=-3.70

## Negated Direction
Best negated: `rank(-1 * pretax_income_total)` S=0.30, F=0.19, INFERIOR
Direction gap: +0.01 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * pretax_income_total)`: S=0.30, F=0.19, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * pretax_income_total / close)`: S=0.21, F=0.11, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(pretax_income_total, 5))`: S=0.44, F=0.14, T=34.8%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(pretax_income_total / close)` | TOP3000 | 0.28 | 0.15 | 32.7% | 60% | bull-only |
| `rank(pretax_income_total)` | TOP3000 | 0.12 | 0.05 | 45.8% | 60% | bull-only |

## Correlation Notes
Top correlates:
- net_income_total_2: 0.995 (strongly positively correlated)
- net_income_adjusted: 0.989 (strongly positively correlated)
- operating_profit_before_interest_tax: 0.987 (strongly positively correlated)
- fnd6_ci: 0.972 (strongly positively correlated)
- cash_flow_from_operations: 0.967 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
