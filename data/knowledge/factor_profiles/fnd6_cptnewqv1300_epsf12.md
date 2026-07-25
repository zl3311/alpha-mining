---
field: fnd6_cptnewqv1300_epsf12
dataset: fundamental6
best_template: rank_neg_delta
best_sharpe: 0.72
best_fitness: 0.24
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: all-weather
n_variations_with_pnl: 4
max_drawdown: 0.1583
ann_vol: 0.139
hit_rate: 0.5198
rolling_sharpe_min: -0.884
rolling_sharpe_max: 2.949
negated_best_sharpe: 0.72
negated_best_template: rank_neg_delta
negated_best_fitness: 0.24
n_negated_sims: 10
direction_gap: 0.27
---
# fnd6_cptnewqv1300_epsf12 (fundamental6)

*Earnings Per Share (Diluted) - Excluding Extraordinary Items - 12 Months Moving*

## Signal Profile
- `rank(fnd6_cptnewqv1300_epsf12)`: S=0.12, F=0.04, T=1.3%, INFERIOR (TOP3000)
- `rank(fnd6_cptnewqv1300_epsf12 / close)`: S=0.17, F=0.07, T=2.1%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_cptnewqv1300_epsf12, 5))`: S=0.45, F=0.18, T=36.6%, INFERIOR (TOP200)
- `-rank(fnd6_cptnewqv1300_epsf12)`: S=0.00, F=0.00, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_cptnewqv1300_epsf12, 5))`: S=0.72, F=0.24, T=37.2%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_cptnewqv1300_epsf12, 22)`: S=0.20, F=0.05, T=38.2%, INFERIOR (TOP3000)
- `ts_mean(fnd6_cptnewqv1300_epsf12, 10)`: S=-0.11, F=-0.03, T=1.5%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_cptnewqv1300_epsf12, 22))`: S=-0.22, F=-0.06, T=16.3%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_cptnewqv1300_epsf12)`: S=-0.12, F=-0.04, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_cptnewqv1300_epsf12 / close)`: S=-0.17, F=-0.07, T=2.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 6F/26P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 12F/17P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.46, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.67 (negative), ret=-6.1%
  - 2020: S=0.17 (weak), ret=+2.7%
  - 2021: S=-0.08 (negative), ret=-1.2%
  - 2022: S=2.26 (strong), ret=+33.2%
  - 2023: S=0.19 (weak), ret=+2.4%

## Risk & Drawdown
- Max drawdown: 15.83% over 458 days (not yet recovered, ongoing at window end)
- Annualized: return +6.3%, volatility 13.9% (fraction of booksize)
- Hit rate: 52.0% positive days
- Tail shape: skew -0.53, excess kurtosis +10.49

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.88, max 2.95, latest 0.28

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2019
Best month: +10.52%; worst month: -12.09%
Positive months: 54%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=0.79
- Sideways: S=-0.10
- Bear: S=0.67

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_cptnewqv1300_epsf12, 5))` S=0.72, F=0.24, INFERIOR
Direction gap: +0.27 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fnd6_cptnewqv1300_epsf12)`: S=-0.12, F=-0.04, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_cptnewqv1300_epsf12 / close)`: S=-0.17, F=-0.07, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_cptnewqv1300_epsf12, 5))`: S=0.72, F=0.24, T=37.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_cptnewqv1300_epsf12, 5))` | TOP200 | 0.46 | 0.18 | 15.8% | 60% | all-weather |
| `rank(fnd6_cptnewqv1300_epsf12 / close)` | TOP3000 | 0.16 | 0.07 | 37.5% | 40% | bull-only |
| `rank(fnd6_cptnewqv1300_epsf12)` | TOP3000 | 0.11 | 0.04 | 43.2% | 60% | bull-only |
| `rank(fnd6_cptnewqv1300_epsf12 / close)` | TOP1000 | 0.05 | 0.02 | 32.0% | 40% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_cptnewqv1300_epsx12: 0.948 (strongly positively correlated)
- fnd6_newqv1300_ibadj12: 0.476 (moderately positively correlated)
- fnd6_newqv1300_reunaq: 0.352 (weakly positively correlated)
- fnd6_newa2v1300_ni: 0.213 (weakly positively correlated)
- fnd6_ibmii: 0.212 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
