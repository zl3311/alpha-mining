---
field: sales_estimate_count_2
dataset: analyst4
best_template: rank_level
best_sharpe: 0.7
best_fitness: 0.26
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 7
max_drawdown: 0.0695
ann_vol: 0.0249
hit_rate: 0.5263
rolling_sharpe_min: -2.187
rolling_sharpe_max: 3.758
negated_best_sharpe: 0.16
negated_best_template: rank_neg_delta
negated_best_fitness: 0.02
n_negated_sims: 10
direction_gap: -0.54
---
# sales_estimate_count_2 (analyst4)

*Number of Sales estimates*

## Signal Profile
- `rank(sales_estimate_count_2)`: S=0.70, F=0.26, T=2.5%, INFERIOR (TOP3000)
- `rank(sales_estimate_count_2 / close)`: S=0.34, F=0.17, T=3.2%, INFERIOR (TOP200)
- `rank(ts_delta(sales_estimate_count_2, 5))`: S=-0.06, F=-0.01, T=35.3%, INFERIOR (TOP500)
- `-rank(sales_estimate_count_2)`: S=-0.20, F=-0.05, T=3.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(sales_estimate_count_2, 5))`: S=0.16, F=0.02, T=34.2%, INFERIOR (TOP3000)
- `-ts_zscore(sales_estimate_count_2, 63)`: S=0.38, F=0.12, T=20.9%, INFERIOR (TOP3000)
- `ts_mean(sales_estimate_count_2, 10)`: S=-0.05, F=-0.01, T=2.9%, INFERIOR (TOP3000)
- `rank(ts_rank(sales_estimate_count_2, 22))`: S=0.38, F=0.13, T=12.2%, INFERIOR (TOP3000)
- `rank(-1 * sales_estimate_count_2)`: S=-0.70, F=-0.26, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * sales_estimate_count_2 / close)`: S=-0.04, F=-0.01, T=2.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 2F/30P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 9F/20P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.70, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.82 (moderate), ret=+1.5%
  - 2020: S=-0.95 (negative), ret=-2.4%
  - 2021: S=0.12 (weak), ret=+0.4%
  - 2022: S=2.06 (strong), ret=+5.0%
  - 2023: S=1.69 (strong), ret=+3.9%

## Risk & Drawdown
- Max drawdown: 6.95% over 911 days (recovered)
- Annualized: return +1.7%, volatility 2.5% (fraction of booksize)
- Hit rate: 52.6% positive days
- Tail shape: skew -0.06, excess kurtosis +1.18

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.19, max 3.76, latest 1.58

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +2.46%; worst month: -1.93%
Positive months: 59%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.30
- Sideways: S=1.25
- Bear: S=-1.47

## Negated Direction
Best negated: `rank(-1 * ts_delta(sales_estimate_count_2, 5))` S=0.16, F=0.02, INFERIOR
Direction gap: -0.54 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * sales_estimate_count_2)`: S=-0.70, F=-0.26, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * sales_estimate_count_2 / close)`: S=-0.04, F=-0.01, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(sales_estimate_count_2, 5))`: S=0.16, F=0.02, T=34.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(sales_estimate_count_2)` | TOP3000 | 0.70 | 0.26 | 7.0% | 80% | bull-only |
| `rank(sales_estimate_count_2 / close)` | TOP200 | 0.36 | 0.17 | 16.1% | 80% | mixed |
| `rank(sales_estimate_count_2 / close)` | TOP500 | 0.24 | 0.10 | 26.2% | 60% | mixed |
| `rank(sales_estimate_count_2)` | TOP500 | 0.26 | 0.08 | 11.1% | 60% | bull-only |
| `rank(sales_estimate_count_2)` | TOP1000 | 0.21 | 0.05 | 13.7% | 60% | bull-only |
| `rank(sales_estimate_count_2 / close)` | TOP1000 | 0.13 | 0.04 | 25.1% | 40% | bear-only |
| `rank(sales_estimate_count_2)` | TOP200 | 0.14 | 0.03 | 16.9% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_newqv1300_wcapq: 0.494 (moderately positively correlated)
- working_capital: 0.494 (moderately positively correlated)
- research_development_expense_reported_value: 0.484 (moderately positively correlated)
- research_development_expense_actual_value: 0.484 (moderately positively correlated)
- fnd6_newa2v1300_wcap: 0.456 (moderately positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
