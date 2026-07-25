---
field: rd_expense
dataset: fundamental6
best_template: rank_delta
best_sharpe: 0.76
best_fitness: 0.51
best_universe: TOP200
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 4
max_drawdown: 0.3071
ann_vol: 0.2117
hit_rate: 0.5004
rolling_sharpe_min: -1.118
rolling_sharpe_max: 2.228
negated_best_sharpe: 0.38
negated_best_template: neg_rank_level
negated_best_fitness: 0.1
n_negated_sims: 10
direction_gap: -0.38
---
# rd_expense (fundamental6)

*Research And Development (Quarterly)*

## Signal Profile
- `rank(rd_expense)`: S=0.01, F=0.00, T=5.7%, INFERIOR (TOP500)
- `rank(rd_expense / close)`: S=0.05, F=0.01, T=5.8%, INFERIOR (TOP500)
- `rank(ts_delta(rd_expense, 5))`: S=0.76, F=0.51, T=36.2%, INFERIOR (TOP200)
- `-rank(rd_expense)`: S=0.05, F=0.01, T=5.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(rd_expense, 5))`: S=-0.13, F=-0.02, T=38.7%, INFERIOR (TOP3000)
- `ts_zscore(rd_expense, 22)`: S=0.44, F=0.19, T=37.0%, INFERIOR (TOP3000)
- `ts_mean(rd_expense, 10)`: S=-0.33, F=-0.28, T=11.1%, INFERIOR (TOP3000)
- `rank(ts_rank(rd_expense, 22))`: S=0.03, F=0.00, T=16.8%, INFERIOR (TOP3000)
- `rank(-1 * rd_expense)`: S=0.38, F=0.10, T=4.5%, INFERIOR (TOP3000)
- `rank(-1 * rd_expense / close)`: S=0.24, F=0.05, T=4.6%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 7F/25P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 15F/14P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.76, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.50 (moderate), ret=+7.5%
  - 2020: S=1.30 (moderate), ret=+26.8%
  - 2021: S=-0.97 (negative), ret=-20.0%
  - 2022: S=1.48 (moderate), ret=+42.4%
  - 2023: S=1.37 (moderate), ret=+21.9%

## Risk & Drawdown
- Max drawdown: 30.71% over 337 days (recovered)
- Annualized: return +16.0%, volatility 21.2% (fraction of booksize)
- Hit rate: 50.0% positive days
- Tail shape: skew -0.49, excess kurtosis +22.04

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.12, max 2.23, latest 1.34

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2021
Best month: +27.72%; worst month: -15.79%
Positive months: 59%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.40
- Sideways: S=0.22
- Bear: S=1.71

## Negated Direction
Best negated: `rank(-1 * rd_expense)` S=0.38, F=0.10, INFERIOR
Direction gap: -0.38 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * rd_expense)`: S=0.38, F=0.10, T=4.5%, INFERIOR (TOP3000)
- `rank(-1 * rd_expense / close)`: S=0.24, F=0.05, T=4.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(rd_expense, 5))`: S=-0.13, F=-0.02, T=38.7%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(rd_expense, 5))` | TOP200 | 0.76 | 0.51 | 30.7% | 80% | mixed |
| `rank(ts_delta(rd_expense, 5))` | TOP500 | 0.52 | 0.21 | 17.2% | 80% | weak |
| `rank(ts_delta(rd_expense, 5))` | TOP1000 | 0.23 | 0.05 | 14.0% | 60% | weak |
| `rank(ts_delta(rd_expense, 5))` | TOP3000 | 0.14 | 0.02 | 13.1% | 40% | bull-only |

## Correlation Notes
Top correlates:
- fnd2_q_flintasamt1expythree: -0.127 (weakly negatively correlated)
- fnd6_newa2v1300_re: 0.110 (weakly positively correlated)
- fnd6_newa2v1300_rdipeps: -0.110 (weakly negatively correlated)
- actual_dividend_value_quarterly: 0.109 (weakly positively correlated)
- fnd6_newa2v1300_rdipd: -0.109 (weakly negatively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
