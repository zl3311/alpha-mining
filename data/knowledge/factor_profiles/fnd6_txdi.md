---
field: fnd6_txdi
dataset: fundamental6
best_template: neg_rank
best_sharpe: 0.63
best_fitness: 0.28
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 1
max_drawdown: 0.1971
ann_vol: 0.1829
hit_rate: 0.4858
rolling_sharpe_min: -0.971
rolling_sharpe_max: 1.586
negated_best_sharpe: 0.63
negated_best_template: neg_rank
negated_best_fitness: 0.28
n_negated_sims: 10
direction_gap: 0.2
---
# fnd6_txdi (fundamental6)

*Income Taxes - Deferred*

## Signal Profile
- `rank(fnd6_txdi)`: S=-0.34, F=-0.15, T=3.2%, INFERIOR (TOP200)
- `rank(fnd6_txdi / close)`: S=-0.46, F=-0.14, T=2.0%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_txdi, 5))`: S=0.43, F=0.21, T=34.5%, INFERIOR (TOP500)
- `-rank(fnd6_txdi)`: S=0.63, F=0.28, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_txdi, 5))`: S=0.58, F=0.28, T=41.0%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_txdi, 63)`: S=-0.19, F=-0.07, T=19.6%, INFERIOR (TOP3000)
- `ts_mean(fnd6_txdi, 10)`: S=-0.58, F=-0.30, T=1.9%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_txdi, 22))`: S=-0.31, F=-0.12, T=19.6%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_txdi)`: S=0.63, F=0.28, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_txdi / close)`: S=0.54, F=0.21, T=2.6%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 18F/11P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.44, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.14 (weak), ret=+1.8%
  - 2020: S=-0.06 (negative), ret=-1.1%
  - 2021: S=0.18 (weak), ret=+3.4%
  - 2022: S=1.05 (moderate), ret=+23.7%
  - 2023: S=0.68 (moderate), ret=+11.3%

## Risk & Drawdown
- Max drawdown: 19.71% over 782 days (recovered)
- Annualized: return +8.0%, volatility 18.3% (fraction of booksize)
- Hit rate: 48.6% positive days
- Tail shape: skew +0.65, excess kurtosis +8.52

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.97, max 1.59, latest 0.68

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +12.67%; worst month: -8.07%
Positive months: 58%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.58
- Sideways: S=0.36
- Bear: S=0.36

## Negated Direction
Best negated: `-rank(fnd6_txdi)` S=0.63, F=0.28, INFERIOR
Direction gap: +0.20 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fnd6_txdi)`: S=0.63, F=0.28, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_txdi / close)`: S=0.54, F=0.21, T=2.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_txdi, 5))`: S=0.58, F=0.28, T=41.0%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_txdi, 5))` | TOP500 | 0.44 | 0.21 | 19.7% | 80% | mixed |

## Correlation Notes
Top correlates:
- fnd6_txdfed: 0.477 (moderately positively correlated)
- fnd6_newa1v1300_fca: 0.260 (weakly positively correlated)
- fnd6_txdfo: 0.222 (weakly positively correlated)
- fnd6_newa1v1300_dcom: 0.188 (weakly positively correlated)
- fn_def_income_tax_expense_a: 0.167 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
