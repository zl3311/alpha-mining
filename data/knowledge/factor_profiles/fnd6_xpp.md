---
field: fnd6_xpp
dataset: fundamental6
best_template: neg_rank_level
best_sharpe: 0.91
best_fitness: 0.65
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 4
max_drawdown: 0.2545
ann_vol: 0.263
hit_rate: 0.4939
rolling_sharpe_min: -1.106
rolling_sharpe_max: 2.217
negated_best_sharpe: 0.91
negated_best_template: neg_rank_level
negated_best_fitness: 0.65
n_negated_sims: 10
direction_gap: 0.15
---
# fnd6_xpp (fundamental6)

*Prepaid Expenses*

## Signal Profile
- `rank(fnd6_xpp)`: S=0.41, F=0.13, T=1.2%, INFERIOR (TOP3000)
- `rank(fnd6_xpp / close)`: S=0.12, F=0.03, T=2.0%, INFERIOR (TOP1000)
- `rank(ts_delta(fnd6_xpp, 5))`: S=0.76, F=0.57, T=35.0%, INFERIOR (TOP3000)
- `-rank(fnd6_xpp)`: S=-0.18, F=-0.05, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_xpp, 5))`: S=0.56, F=0.42, T=21.4%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_xpp, 63)`: S=-0.02, F=0.00, T=13.8%, INFERIOR (TOP3000)
- `ts_mean(fnd6_xpp, 10)`: S=-0.38, F=-0.20, T=1.5%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_xpp, 22))`: S=-0.08, F=-0.02, T=18.3%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_xpp)`: S=0.91, F=0.65, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_xpp / close)`: S=0.72, F=0.51, T=2.5%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 18F/11P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.75, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=1.11 (moderate), ret=+19.8%
  - 2020: S=1.18 (moderate), ret=+46.5%
  - 2021: S=-0.08 (negative), ret=-1.8%
  - 2022: S=1.88 (strong), ret=+46.3%
  - 2023: S=-0.83 (negative), ret=-14.1%

## Risk & Drawdown
- Max drawdown: 25.45% over 367 days (not yet recovered, ongoing at window end)
- Annualized: return +19.7%, volatility 26.3% (fraction of booksize)
- Hit rate: 49.4% positive days
- Tail shape: skew +6.68, excess kurtosis +126.23

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.11, max 2.22, latest -0.97

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2023
Best month: +38.75%; worst month: -10.94%
Positive months: 52%

## Regime Profile
Regime profile: **mixed**
- Bull: S=-0.01
- Sideways: S=0.12
- Bear: S=1.64

## Negated Direction
Best negated: `rank(-1 * fnd6_xpp)` S=0.91, F=0.65, INFERIOR
Direction gap: +0.15 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fnd6_xpp)`: S=0.91, F=0.65, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_xpp / close)`: S=0.72, F=0.51, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_xpp, 5))`: S=0.56, F=0.42, T=21.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_xpp, 5))` | TOP3000 | 0.75 | 0.57 | 25.4% | 60% | mixed |
| `rank(fnd6_xpp)` | TOP3000 | 0.43 | 0.13 | 4.2% | 80% | mixed |
| `rank(fnd6_xpp)` | TOP1000 | 0.19 | 0.05 | 7.8% | 80% | bull-only |
| `rank(fnd6_xpp / close)` | TOP1000 | 0.13 | 0.03 | 14.8% | 60% | mixed |

## Correlation Notes
Top correlates:
- fn_business_combination_purchase_price_q: 0.142 (weakly positively correlated)
- fnd6_invrm: 0.114 (weakly positively correlated)
- fnd6_mfma1_aoloch: 0.095 (weakly positively correlated)
- fnd6_newa1v1300_aoloch: 0.095 (weakly positively correlated)
- fnd6_newqv1300_stkcpaq: 0.093 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
