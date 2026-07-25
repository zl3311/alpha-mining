---
field: fn_income_from_equity_investments_a
dataset: fundamental2
best_template: ts_zscore
best_sharpe: 0.66
best_fitness: 0.76
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 4
max_drawdown: 0.2497
ann_vol: 0.0961
hit_rate: 0.519
rolling_sharpe_min: -1.675
rolling_sharpe_max: 2.921
negated_best_sharpe: 0.63
negated_best_template: neg_rank
negated_best_fitness: 0.31
n_negated_sims: 10
direction_gap: -0.03
---
# fn_income_from_equity_investments_a (fundamental2)

*Income From Equity Method Investments*

## Signal Profile
- `rank(fn_income_from_equity_investments_a)`: S=0.44, F=0.25, T=2.3%, INFERIOR (TOP200)
- `rank(fn_income_from_equity_investments_a / close)`: S=0.51, F=0.32, T=2.5%, INFERIOR (TOP200)
- `rank(ts_delta(fn_income_from_equity_investments_a, 5))`: S=0.17, F=0.08, T=16.0%, INFERIOR (TOP200)
- `-rank(fn_income_from_equity_investments_a)`: S=0.63, F=0.31, T=1.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_income_from_equity_investments_a, 5))`: S=0.19, F=0.06, T=30.3%, INFERIOR (TOP3000)
- `-ts_zscore(fn_income_from_equity_investments_a, 63)`: S=0.66, F=0.76, T=12.8%, INFERIOR (TOP3000)
- `ts_mean(fn_income_from_equity_investments_a, 10)`: S=-0.98, F=-0.66, T=0.7%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_income_from_equity_investments_a, 22))`: S=-0.21, F=-0.09, T=15.7%, INFERIOR (TOP3000)
- `rank(-1 * fn_income_from_equity_investments_a)`: S=0.63, F=0.31, T=1.2%, INFERIOR (TOP3000)
- `rank(-1 * fn_income_from_equity_investments_a / close)`: S=0.54, F=0.24, T=1.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 16F/13P
- LOW_TURNOVER: 3F/29P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.53, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-1.00 (negative), ret=-5.4%
  - 2020: S=-1.52 (negative), ret=-17.9%
  - 2021: S=2.48 (strong), ret=+31.5%
  - 2022: S=1.96 (strong), ret=+16.5%
  - 2023: S=0.03 (weak), ret=+0.2%

## Risk & Drawdown
- Max drawdown: 24.97% over 797 days (recovered)
- Annualized: return +5.1%, volatility 9.6% (fraction of booksize)
- Hit rate: 51.9% positive days
- Tail shape: skew -0.02, excess kurtosis +3.42

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.68, max 2.92, latest 0.10

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2020
Best month: +5.84%; worst month: -5.38%
Positive months: 63%

## Regime Profile
Regime profile: **mixed**
- Bull: S=1.92
- Sideways: S=-0.62
- Bear: S=-0.04

## Negated Direction
Best negated: `-rank(fn_income_from_equity_investments_a)` S=0.63, F=0.31, INFERIOR
Direction gap: -0.03 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fn_income_from_equity_investments_a)`: S=0.63, F=0.31, T=1.2%, INFERIOR (TOP3000)
- `rank(-1 * fn_income_from_equity_investments_a / close)`: S=0.54, F=0.24, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_income_from_equity_investments_a, 5))`: S=0.19, F=0.06, T=30.3%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fn_income_from_equity_investments_a / close)` | TOP200 | 0.53 | 0.32 | 25.0% | 60% | mixed |
| `rank(fn_income_from_equity_investments_a)` | TOP200 | 0.45 | 0.25 | 25.2% | 40% | mixed |
| `rank(ts_delta(fn_income_from_equity_investments_a, 5))` | TOP200 | 0.17 | 0.08 | 29.9% | 40% | mixed |
| `rank(ts_delta(fn_income_from_equity_investments_a, 5))` | TOP500 | 0.12 | 0.04 | 37.0% | 60% | weak |

## Correlation Notes
Top correlates:
- fnd6_txndbl: 0.514 (moderately positively correlated)
- fnd6_txndba: 0.508 (moderately positively correlated)
- fnd6_loxdr: 0.504 (moderately positively correlated)
- fn_def_tax_liab_a: 0.492 (moderately positively correlated)
- fnd6_newa1v1300_dltt: 0.491 (moderately positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
