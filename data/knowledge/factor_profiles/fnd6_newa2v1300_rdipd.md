---
field: fnd6_newa2v1300_rdipd
dataset: fundamental6
best_template: ts_mean
best_sharpe: 0.71
best_fitness: 0.78
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 7
max_drawdown: 0.3403
ann_vol: 0.2115
hit_rate: 0.4907
rolling_sharpe_min: -2.034
rolling_sharpe_max: 1.63
negated_best_sharpe: 0.07
negated_best_template: rank_neg_delta
negated_best_fitness: 0.02
n_negated_sims: 10
direction_gap: -0.64
---
# fnd6_newa2v1300_rdipd (fundamental6)

*In Process R&D Expense Diluted EPS Effect*

## Signal Profile
- `rank(fnd6_newa2v1300_rdipd)`: S=0.28, F=0.19, T=2.5%, INFERIOR (TOP200)
- `rank(fnd6_newa2v1300_rdipd / close)`: S=0.29, F=0.20, T=2.5%, INFERIOR (TOP200)
- `rank(ts_delta(fnd6_newa2v1300_rdipd, 5))`: S=0.08, F=0.02, T=15.0%, INFERIOR (TOP1000)
- `-rank(fnd6_newa2v1300_rdipd)`: S=-0.28, F=-0.15, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa2v1300_rdipd, 5))`: S=0.07, F=0.02, T=10.2%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_newa2v1300_rdipd, 63)`: S=-0.39, F=-0.41, T=7.7%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newa2v1300_rdipd, 10)`: S=0.71, F=0.78, T=2.2%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newa2v1300_rdipd, 22))`: S=-0.61, F=-0.64, T=11.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa2v1300_rdipd)`: S=-0.28, F=-0.19, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa2v1300_rdipd / close)`: S=-0.29, F=-0.20, T=2.5%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 21F/11P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 12F/8P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.29, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.09 (negative), ret=-1.2%
  - 2020: S=0.30 (weak), ret=+7.5%
  - 2021: S=0.39 (weak), ret=+10.2%
  - 2022: S=0.88 (moderate), ret=+15.7%
  - 2023: S=-0.14 (negative), ret=-2.4%

## Risk & Drawdown
- Max drawdown: 34.03% over 563 days (recovered)
- Annualized: return +6.1%, volatility 21.1% (fraction of booksize)
- Hit rate: 49.1% positive days
- Tail shape: skew +0.31, excess kurtosis +3.37

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.03, max 1.63, latest -0.09

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2023
Best month: +11.54%; worst month: -10.94%
Positive months: 49%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.28
- Sideways: S=-1.09
- Bear: S=1.58

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_newa2v1300_rdipd, 5))` S=0.07, F=0.02, INFERIOR
Direction gap: -0.64 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_newa2v1300_rdipd)`: S=-0.28, F=-0.19, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa2v1300_rdipd / close)`: S=-0.29, F=-0.20, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa2v1300_rdipd, 5))`: S=0.07, F=0.02, T=10.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newa2v1300_rdipd / close)` | TOP200 | 0.29 | 0.20 | 34.0% | 60% | mixed |
| `rank(fnd6_newa2v1300_rdipd)` | TOP200 | 0.28 | 0.19 | 34.7% | 60% | mixed |
| `rank(fnd6_newa2v1300_rdipd / close)` | TOP3000 | 0.31 | 0.17 | 26.2% | 60% | bear-only |
| `rank(fnd6_newa2v1300_rdipd)` | TOP3000 | 0.31 | 0.17 | 26.3% | 60% | bear-only |
| `rank(fnd6_newa2v1300_rdipd / close)` | TOP1000 | 0.29 | 0.15 | 25.1% | 60% | bear-only |
| `rank(fnd6_newa2v1300_rdipd)` | TOP1000 | 0.29 | 0.15 | 25.1% | 60% | bear-only |
| `rank(ts_delta(fnd6_newa2v1300_rdipd, 5))` | TOP1000 | 0.07 | 0.02 | 37.3% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_newa2v1300_rdipeps: 0.997 (strongly positively correlated)
- fnd6_itcb: -0.395 (weakly negatively correlated)
- min_stock_option_expense_guidance: -0.367 (weakly negatively correlated)
- stock_option_expense_max_guidance_qtr: -0.367 (weakly negatively correlated)
- historical_volatility_150: 0.361 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
