---
field: fnd2_dfdfritxexp
dataset: fundamental2
best_template: rank_ts_rank
best_sharpe: 0.74
best_fitness: 0.5
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: weak
n_variations_with_pnl: 2
max_drawdown: 0.2902
ann_vol: 0.1507
hit_rate: 0.4923
rolling_sharpe_min: -2.203
rolling_sharpe_max: 1.671
negated_best_sharpe: 0.78
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.38
n_negated_sims: 10
direction_gap: 0.04
---
# fnd2_dfdfritxexp (fundamental2)

*Income Tax Expense, Deferred - Foreign*

## Signal Profile
- `rank(fnd2_dfdfritxexp)`: S=-0.02, F=0.00, T=1.6%, INFERIOR (TOP500)
- `rank(fnd2_dfdfritxexp / close)`: S=-0.15, F=-0.04, T=2.3%, INFERIOR (TOP200)
- `rank(ts_delta(fnd2_dfdfritxexp, 5))`: S=0.33, F=0.13, T=33.7%, INFERIOR (TOP500)
- `-rank(fnd2_dfdfritxexp)`: S=0.50, F=0.19, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_dfdfritxexp, 5))`: S=-0.08, F=-0.01, T=34.1%, INFERIOR (TOP3000)
- `ts_zscore(fnd2_dfdfritxexp, 22)`: S=-0.25, F=-0.12, T=20.9%, INFERIOR (TOP3000)
- `ts_mean(fnd2_dfdfritxexp, 10)`: S=0.24, F=0.09, T=1.3%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd2_dfdfritxexp, 22))`: S=0.74, F=0.50, T=15.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_dfdfritxexp)`: S=0.50, F=0.19, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_dfdfritxexp / close)`: S=0.78, F=0.38, T=1.5%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 9F/20P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.32, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.23 (negative), ret=-2.8%
  - 2020: S=0.02 (weak), ret=+0.3%
  - 2021: S=0.81 (moderate), ret=+12.3%
  - 2022: S=-0.45 (negative), ret=-7.6%
  - 2023: S=1.43 (moderate), ret=+21.3%

## Risk & Drawdown
- Max drawdown: 29.02% over 489 days (recovered)
- Annualized: return +4.8%, volatility 15.1% (fraction of booksize)
- Hit rate: 49.2% positive days
- Tail shape: skew +0.38, excess kurtosis +3.93

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.20, max 1.67, latest 1.42

## Yearly & Monthly Returns
Best year (by Sharpe): 2023; worst year: 2022
Best month: +13.47%; worst month: -7.59%
Positive months: 58%

## Regime Profile
Regime profile: **weak**
- Bull: S=0.04
- Sideways: S=0.65
- Bear: S=0.32

## Negated Direction
Best negated: `rank(-1 * fnd2_dfdfritxexp / close)` S=0.78, F=0.38, INFERIOR
Direction gap: +0.04 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fnd2_dfdfritxexp)`: S=0.50, F=0.19, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_dfdfritxexp / close)`: S=0.78, F=0.38, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_dfdfritxexp, 5))`: S=-0.08, F=-0.01, T=34.1%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd2_dfdfritxexp, 5))` | TOP500 | 0.32 | 0.13 | 29.0% | 60% | weak |
| `rank(ts_delta(fnd2_dfdfritxexp, 5))` | TOP200 | 0.15 | 0.05 | 26.5% | 40% | mixed |

## Correlation Notes
Top correlates:
- fnd6_txdfo: 0.385 (weakly positively correlated)
- fn_def_income_tax_expense_a: 0.208 (weakly positively correlated)
- cashflow_invst: 0.174 (weakly positively correlated)
- fnd6_newa1v1300_ivncf: 0.173 (weakly positively correlated)
- fnd6_optca: 0.147 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
