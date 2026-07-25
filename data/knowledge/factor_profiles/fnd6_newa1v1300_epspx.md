---
field: fnd6_newa1v1300_epspx
dataset: fundamental6
best_template: rank_neg_delta
best_sharpe: 0.5
best_fitness: 0.24
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: weak
n_variations_with_pnl: 4
max_drawdown: 0.4361
ann_vol: 0.2066
hit_rate: 0.4988
rolling_sharpe_min: -1.822
rolling_sharpe_max: 2.436
negated_best_sharpe: 0.5
negated_best_template: rank_neg_delta
negated_best_fitness: 0.24
n_negated_sims: 10
direction_gap: 0.14
---
# fnd6_newa1v1300_epspx (fundamental6)

*Earnings Per Share (Basic) - Excluding Extraordinary Items*

## Signal Profile
- `rank(fnd6_newa1v1300_epspx)`: S=0.09, F=0.03, T=1.1%, INFERIOR (TOP3000)
- `rank(fnd6_newa1v1300_epspx / close)`: S=0.30, F=0.15, T=1.9%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_newa1v1300_epspx, 5))`: S=0.36, F=0.17, T=33.3%, INFERIOR (TOP200)
- `-rank(fnd6_newa1v1300_epspx)`: S=-0.06, F=-0.01, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa1v1300_epspx, 5))`: S=0.50, F=0.24, T=34.0%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_newa1v1300_epspx, 22)`: S=0.06, F=0.01, T=28.7%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newa1v1300_epspx, 10)`: S=-0.07, F=-0.02, T=1.4%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newa1v1300_epspx, 22))`: S=-0.74, F=-0.45, T=14.7%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_epspx)`: S=0.10, F=0.03, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_epspx / close)`: S=0.15, F=0.06, T=2.7%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 20F/9P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.36, Consistency 40% positive years (2/5)
Yearly breakdown:
  - 2019: S=0.97 (moderate), ret=+13.8%
  - 2020: S=-0.72 (negative), ret=-13.0%
  - 2021: S=-0.22 (negative), ret=-5.2%
  - 2022: S=1.64 (strong), ret=+45.8%
  - 2023: S=-0.37 (negative), ret=-5.3%

## Risk & Drawdown
- Max drawdown: 43.61% over 766 days (recovered)
- Annualized: return +7.4%, volatility 20.7% (fraction of booksize)
- Hit rate: 49.9% positive days
- Tail shape: skew -1.42, excess kurtosis +20.21

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.82, max 2.44, latest -0.28

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +22.65%; worst month: -9.94%
Positive months: 48%

## Regime Profile
Regime profile: **weak**
- Bull: S=0.27
- Sideways: S=0.92
- Bear: S=-0.05

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_newa1v1300_epspx, 5))` S=0.50, F=0.24, INFERIOR
Direction gap: +0.14 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fnd6_newa1v1300_epspx)`: S=0.10, F=0.03, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_epspx / close)`: S=0.15, F=0.06, T=2.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa1v1300_epspx, 5))`: S=0.50, F=0.24, T=34.0%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_newa1v1300_epspx, 5))` | TOP200 | 0.36 | 0.17 | 43.6% | 40% | weak |
| `rank(fnd6_newa1v1300_epspx / close)` | TOP3000 | 0.29 | 0.15 | 29.2% | 60% | bull-only |
| `rank(fnd6_newa1v1300_epspx / close)` | TOP1000 | 0.13 | 0.05 | 31.3% | 40% | bull-only |
| `rank(fnd6_newa1v1300_epspx)` | TOP3000 | 0.08 | 0.03 | 41.7% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_newa1v1300_epspi: 0.999 (strongly positively correlated)
- fnd6_newa1v1300_epsfx: 0.990 (strongly positively correlated)
- fnd6_newa1v1300_epsfi: 0.989 (strongly positively correlated)
- fnd6_newa1v1300_ibcom: 0.859 (strongly positively correlated)
- fnd6_newa2v1300_ni: 0.850 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
