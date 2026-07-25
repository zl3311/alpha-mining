---
field: fnd6_cipen
dataset: fundamental6
best_template: rank_delta
best_sharpe: 0.66
best_fitness: 0.32
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 7
max_drawdown: 0.2337
ann_vol: 0.1431
hit_rate: 0.5182
rolling_sharpe_min: -0.704
rolling_sharpe_max: 2.379
negated_best_sharpe: 0.49
negated_best_template: rank_neg_delta
negated_best_fitness: 0.28
n_negated_sims: 10
direction_gap: -0.17
---
# fnd6_cipen (fundamental6)

*Comprehensive Income - Minimum Pension Adjustment*

## Signal Profile
- `rank(fnd6_cipen)`: S=0.29, F=0.09, T=1.8%, INFERIOR (TOP3000)
- `rank(fnd6_cipen / close)`: S=0.23, F=0.07, T=2.9%, INFERIOR (TOP500)
- `rank(ts_delta(fnd6_cipen, 5))`: S=0.66, F=0.32, T=38.9%, INFERIOR (TOP3000)
- `-rank(fnd6_cipen)`: S=0.01, F=0.00, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_cipen, 5))`: S=0.49, F=0.28, T=21.8%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_cipen, 63)`: S=0.06, F=0.02, T=18.3%, INFERIOR (TOP3000)
- `ts_mean(fnd6_cipen, 10)`: S=0.10, F=0.02, T=1.9%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_cipen, 22))`: S=-0.01, F=0.00, T=20.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_cipen)`: S=-0.13, F=-0.04, T=3.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_cipen / close)`: S=-0.16, F=-0.05, T=3.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 5F/15P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.67, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.14 (negative), ret=-1.8%
  - 2020: S=0.89 (moderate), ret=+13.9%
  - 2021: S=1.32 (moderate), ret=+19.2%
  - 2022: S=1.14 (moderate), ret=+16.1%
  - 2023: S=-0.05 (negative), ret=-0.6%

## Risk & Drawdown
- Max drawdown: 23.37% over 436 days (recovered)
- Annualized: return +9.5%, volatility 14.3% (fraction of booksize)
- Hit rate: 51.8% positive days
- Tail shape: skew +0.46, excess kurtosis +4.62

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.70, max 2.38, latest -0.02

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2019
Best month: +13.53%; worst month: -12.99%
Positive months: 66%

## Regime Profile
Regime profile: **mixed**
- Bull: S=-0.17
- Sideways: S=1.24
- Bear: S=1.07

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_cipen, 5))` S=0.49, F=0.28, INFERIOR
Direction gap: -0.17 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_cipen)`: S=-0.13, F=-0.04, T=3.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_cipen / close)`: S=-0.16, F=-0.05, T=3.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_cipen, 5))`: S=0.49, F=0.28, T=21.8%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_cipen, 5))` | TOP3000 | 0.67 | 0.32 | 23.4% | 60% | mixed |
| `rank(fnd6_cipen)` | TOP3000 | 0.28 | 0.09 | 11.9% | 60% | weak |
| `rank(fnd6_cipen)` | TOP500 | 0.22 | 0.07 | 12.7% | 60% | weak |
| `rank(fnd6_cipen / close)` | TOP500 | 0.22 | 0.07 | 12.7% | 60% | mixed |
| `rank(fnd6_cipen / close)` | TOP3000 | 0.21 | 0.06 | 11.6% | 60% | weak |
| `rank(fnd6_cipen / close)` | TOP200 | 0.15 | 0.05 | 22.7% | 60% | mixed |
| `rank(fnd6_cipen)` | TOP200 | 0.12 | 0.04 | 23.2% | 60% | weak |

## Correlation Notes
Top correlates:
- fnd6_ciother: -0.160 (weakly negatively correlated)
- parkinson_volatility_120: -0.139 (weakly negatively correlated)
- fnd6_newqv1300_aocipenq: 0.133 (weakly positively correlated)
- historical_volatility_120: -0.129 (weakly negatively correlated)
- fnd6_cld2: 0.118 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
