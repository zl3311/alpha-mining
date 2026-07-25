---
field: fnd6_newa2v1300_rdipeps
dataset: fundamental6
best_template: ts_mean
best_sharpe: 0.63
best_fitness: 0.65
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 6
max_drawdown: 0.3404
ann_vol: 0.2116
hit_rate: 0.4874
rolling_sharpe_min: -1.879
rolling_sharpe_max: 1.63
negated_best_sharpe: 0.01
negated_best_template: rank_neg_delta
negated_best_fitness: 0.0
n_negated_sims: 10
direction_gap: -0.62
---
# fnd6_newa2v1300_rdipeps (fundamental6)

*In Process R&D Expense Basic EPS Effect*

## Signal Profile
- `rank(fnd6_newa2v1300_rdipeps)`: S=0.24, F=0.15, T=2.6%, INFERIOR (TOP200)
- `rank(fnd6_newa2v1300_rdipeps / close)`: S=0.25, F=0.16, T=2.6%, INFERIOR (TOP200)
- `rank(ts_delta(fnd6_newa2v1300_rdipeps, 5))`: S=0.06, F=0.01, T=15.3%, INFERIOR (TOP1000)
- `-rank(fnd6_newa2v1300_rdipeps)`: S=-0.23, F=-0.11, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa2v1300_rdipeps, 5))`: S=0.01, F=0.00, T=10.1%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_newa2v1300_rdipeps, 63)`: S=0.12, F=0.07, T=8.3%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newa2v1300_rdipeps, 10)`: S=0.63, F=0.65, T=2.2%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newa2v1300_rdipeps, 22))`: S=-0.70, F=-0.79, T=11.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa2v1300_rdipeps)`: S=-0.24, F=-0.15, T=2.6%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa2v1300_rdipeps / close)`: S=-0.25, F=-0.16, T=2.6%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 21F/11P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 11F/9P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.24, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.03 (negative), ret=-0.5%
  - 2020: S=0.30 (weak), ret=+7.7%
  - 2021: S=0.44 (weak), ret=+11.5%
  - 2022: S=0.88 (moderate), ret=+15.7%
  - 2023: S=-0.56 (negative), ret=-9.1%

## Risk & Drawdown
- Max drawdown: 34.04% over 563 days (recovered)
- Annualized: return +5.2%, volatility 21.2% (fraction of booksize)
- Hit rate: 48.7% positive days
- Tail shape: skew +0.32, excess kurtosis +3.39

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.88, max 1.63, latest -0.50

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2023
Best month: +13.00%; worst month: -10.96%
Positive months: 48%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.22
- Sideways: S=-1.18
- Bear: S=1.60

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_newa2v1300_rdipeps, 5))` S=0.01, F=0.00, INFERIOR
Direction gap: -0.62 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_newa2v1300_rdipeps)`: S=-0.24, F=-0.15, T=2.6%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa2v1300_rdipeps / close)`: S=-0.25, F=-0.16, T=2.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa2v1300_rdipeps, 5))`: S=0.01, F=0.00, T=10.1%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newa2v1300_rdipeps / close)` | TOP200 | 0.24 | 0.16 | 34.0% | 60% | mixed |
| `rank(fnd6_newa2v1300_rdipeps)` | TOP200 | 0.23 | 0.15 | 34.7% | 60% | mixed |
| `rank(fnd6_newa2v1300_rdipeps / close)` | TOP3000 | 0.27 | 0.14 | 26.2% | 60% | bear-only |
| `rank(fnd6_newa2v1300_rdipeps)` | TOP3000 | 0.26 | 0.13 | 26.2% | 60% | bear-only |
| `rank(fnd6_newa2v1300_rdipeps / close)` | TOP1000 | 0.24 | 0.11 | 25.3% | 60% | bear-only |
| `rank(fnd6_newa2v1300_rdipeps)` | TOP1000 | 0.24 | 0.11 | 25.3% | 60% | bear-only |

## Correlation Notes
Top correlates:
- fnd6_newa2v1300_rdipd: 0.997 (strongly positively correlated)
- fnd6_itcb: -0.395 (weakly negatively correlated)
- min_stock_option_expense_guidance: -0.367 (weakly negatively correlated)
- stock_option_expense_max_guidance_qtr: -0.367 (weakly negatively correlated)
- historical_volatility_150: 0.361 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
