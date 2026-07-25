---
field: actual_dividend_value_quarterly
dataset: analyst4
best_template: ts_zscore
best_sharpe: 0.73
best_fitness: 0.31
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 1
max_drawdown: 0.1696
ann_vol: 0.0796
hit_rate: 0.4923
rolling_sharpe_min: -2.456
rolling_sharpe_max: 1.909
negated_best_sharpe: 0.62
negated_best_template: rank_neg_delta
negated_best_fitness: 0.15
n_negated_sims: 10
direction_gap: -0.11
---
# actual_dividend_value_quarterly (analyst4)

*Dividend - Actual value for the quarter*

## Signal Profile
- `rank(actual_dividend_value_quarterly)`: S=-0.16, F=-0.05, T=1.8%, INFERIOR (TOP3000)
- `rank(actual_dividend_value_quarterly / close)`: S=0.16, F=0.05, T=2.5%, INFERIOR (TOP3000)
- `rank(ts_delta(actual_dividend_value_quarterly, 5))`: S=-0.22, F=-0.04, T=37.2%, INFERIOR (TOP1000)
- `-rank(actual_dividend_value_quarterly)`: S=0.17, F=0.06, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(actual_dividend_value_quarterly, 5))`: S=0.62, F=0.15, T=35.7%, INFERIOR (TOP3000)
- `-ts_zscore(actual_dividend_value_quarterly, 63)`: S=0.73, F=0.31, T=19.6%, INFERIOR (TOP3000)
- `ts_mean(actual_dividend_value_quarterly, 10)`: S=-0.08, F=-0.02, T=1.9%, INFERIOR (TOP3000)
- `rank(ts_rank(actual_dividend_value_quarterly, 22))`: S=-0.03, F=0.00, T=14.0%, INFERIOR (TOP3000)
- `rank(-1 * actual_dividend_value_quarterly)`: S=0.16, F=0.05, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * actual_dividend_value_quarterly / close)`: S=-0.16, F=-0.05, T=2.5%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 2F/30P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 18F/11P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.14, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.37 (weak), ret=+1.4%
  - 2020: S=-1.68 (negative), ret=-9.2%
  - 2021: S=0.76 (moderate), ret=+6.4%
  - 2022: S=1.12 (moderate), ret=+13.3%
  - 2023: S=-0.96 (negative), ret=-6.6%

## Risk & Drawdown
- Max drawdown: 16.96% over 793 days (recovered)
- Annualized: return +1.1%, volatility 8.0% (fraction of booksize)
- Hit rate: 49.2% positive days
- Tail shape: skew +0.02, excess kurtosis +2.04

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.46, max 1.91, latest -1.11

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +5.96%; worst month: -4.43%
Positive months: 51%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.37
- Sideways: S=0.38
- Bear: S=-3.12

## Negated Direction
Best negated: `rank(-1 * ts_delta(actual_dividend_value_quarterly, 5))` S=0.62, F=0.15, INFERIOR
Direction gap: -0.11 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * actual_dividend_value_quarterly)`: S=0.16, F=0.05, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * actual_dividend_value_quarterly / close)`: S=-0.16, F=-0.05, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(actual_dividend_value_quarterly, 5))`: S=0.62, F=0.15, T=35.7%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(actual_dividend_value_quarterly / close)` | TOP3000 | 0.14 | 0.05 | 17.0% | 60% | bull-only |

## Correlation Notes
Top correlates:
- cashflow_dividends: 0.893 (strongly positively correlated)
- fnd6_newa1v1300_dv: 0.893 (strongly positively correlated)
- anl4_af_div_value: 0.890 (strongly positively correlated)
- anl4_afv4_div_mean: 0.874 (strongly positively correlated)
- anl4_afv4_div_median: 0.870 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
