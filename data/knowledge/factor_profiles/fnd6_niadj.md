---
field: fnd6_niadj
dataset: fundamental6
best_template: neg_rank_level
best_sharpe: 0.4
best_fitness: 0.28
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: weak
n_variations_with_pnl: 3
max_drawdown: 0.4607
ann_vol: 0.1922
hit_rate: 0.5004
rolling_sharpe_min: -1.971
rolling_sharpe_max: 2.709
negated_best_sharpe: 0.4
negated_best_template: neg_rank_level
negated_best_fitness: 0.28
n_negated_sims: 10
direction_gap: -0.1
---
# fnd6_niadj (fundamental6)

*Net Income Adjusted for Common/Ordinary Stock (Capital) Equivalents*

## Signal Profile
- `rank(fnd6_niadj)`: S=0.00, F=0.00, T=1.0%, INFERIOR (TOP3000)
- `rank(fnd6_niadj / close)`: S=0.11, F=0.03, T=1.4%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_niadj, 5))`: S=0.50, F=0.27, T=33.1%, INFERIOR (TOP200)
- `-rank(fnd6_niadj)`: S=0.04, F=0.01, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_niadj, 5))`: S=-0.42, F=-0.21, T=33.1%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_niadj, 63)`: S=-0.21, F=-0.08, T=18.8%, INFERIOR (TOP3000)
- `ts_mean(fnd6_niadj, 10)`: S=0.13, F=0.04, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_niadj, 22))`: S=-0.31, F=-0.13, T=14.6%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_niadj)`: S=0.40, F=0.28, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_niadj / close)`: S=0.35, F=0.22, T=2.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 11F/21P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/6P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.50, Consistency 40% positive years (2/5)
Yearly breakdown:
  - 2019: S=2.34 (strong), ret=+31.0%
  - 2020: S=-0.49 (negative), ret=-8.3%
  - 2021: S=-0.42 (negative), ret=-9.7%
  - 2022: S=1.67 (strong), ret=+40.3%
  - 2023: S=-0.44 (negative), ret=-6.2%

## Risk & Drawdown
- Max drawdown: 46.07% over 876 days (recovered)
- Annualized: return +9.6%, volatility 19.2% (fraction of booksize)
- Hit rate: 50.0% positive days
- Tail shape: skew -0.28, excess kurtosis +10.20

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.97, max 2.71, latest -0.35

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2020
Best month: +20.74%; worst month: -10.80%
Positive months: 49%

## Regime Profile
Regime profile: **weak**
- Bull: S=0.11
- Sideways: S=1.63
- Bear: S=-0.07

## Negated Direction
Best negated: `rank(-1 * fnd6_niadj)` S=0.40, F=0.28, INFERIOR
Direction gap: -0.10 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_niadj)`: S=0.40, F=0.28, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_niadj / close)`: S=0.35, F=0.22, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_niadj, 5))`: S=-0.42, F=-0.21, T=33.1%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_niadj, 5))` | TOP200 | 0.50 | 0.27 | 46.1% | 40% | weak |
| `rank(fnd6_niadj / close)` | TOP3000 | 0.10 | 0.03 | 34.8% | 60% | bull-only |
| `rank(fnd6_niadj / close)` | TOP1000 | 0.05 | 0.02 | 35.6% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_newa1v1300_ibadj: 0.996 (strongly positively correlated)
- fnd6_dilavx: 0.965 (strongly positively correlated)
- fnd6_newa1v1300_ibcom: 0.938 (strongly positively correlated)
- fnd6_newa2v1300_ni: 0.923 (strongly positively correlated)
- fnd6_newa1v1300_ib: 0.918 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
