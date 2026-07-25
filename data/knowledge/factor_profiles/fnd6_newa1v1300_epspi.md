---
field: fnd6_newa1v1300_epspi
dataset: fundamental6
best_template: rank_neg_delta
best_sharpe: 0.47
best_fitness: 0.22
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: weak
n_variations_with_pnl: 5
max_drawdown: 0.4424
ann_vol: 0.207
hit_rate: 0.4988
rolling_sharpe_min: -1.845
rolling_sharpe_max: 2.436
negated_best_sharpe: 0.47
negated_best_template: rank_neg_delta
negated_best_fitness: 0.22
n_negated_sims: 10
direction_gap: 0.11
---
# fnd6_newa1v1300_epspi (fundamental6)

*Earnings Per Share (Basic) - Including Extraordinary Items*

## Signal Profile
- `rank(fnd6_newa1v1300_epspi)`: S=0.10, F=0.03, T=1.1%, INFERIOR (TOP3000)
- `rank(fnd6_newa1v1300_epspi / close)`: S=0.30, F=0.15, T=1.9%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_newa1v1300_epspi, 5))`: S=0.36, F=0.17, T=33.4%, INFERIOR (TOP200)
- `-rank(fnd6_newa1v1300_epspi)`: S=-0.09, F=-0.03, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa1v1300_epspi, 5))`: S=0.47, F=0.22, T=34.0%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_newa1v1300_epspi, 63)`: S=-0.07, F=-0.01, T=18.9%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newa1v1300_epspi, 10)`: S=-0.05, F=-0.01, T=1.4%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newa1v1300_epspi, 22))`: S=-0.78, F=-0.49, T=14.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_epspi)`: S=0.11, F=0.04, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_epspi / close)`: S=0.18, F=0.07, T=2.7%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 20F/9P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.35, Consistency 40% positive years (2/5)
Yearly breakdown:
  - 2019: S=0.97 (moderate), ret=+13.8%
  - 2020: S=-0.73 (negative), ret=-13.1%
  - 2021: S=-0.25 (negative), ret=-5.9%
  - 2022: S=1.66 (strong), ret=+46.3%
  - 2023: S=-0.37 (negative), ret=-5.3%

## Risk & Drawdown
- Max drawdown: 44.24% over 766 days (recovered)
- Annualized: return +7.3%, volatility 20.7% (fraction of booksize)
- Hit rate: 49.9% positive days
- Tail shape: skew -1.41, excess kurtosis +20.06

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.84, max 2.44, latest -0.28

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +22.66%; worst month: -10.75%
Positive months: 48%

## Regime Profile
Regime profile: **weak**
- Bull: S=0.24
- Sideways: S=0.96
- Bear: S=-0.05

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_newa1v1300_epspi, 5))` S=0.47, F=0.22, INFERIOR
Direction gap: +0.11 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fnd6_newa1v1300_epspi)`: S=0.11, F=0.04, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_epspi / close)`: S=0.18, F=0.07, T=2.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa1v1300_epspi, 5))`: S=0.47, F=0.22, T=34.0%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_newa1v1300_epspi, 5))` | TOP200 | 0.35 | 0.17 | 44.2% | 40% | weak |
| `rank(fnd6_newa1v1300_epspi / close)` | TOP3000 | 0.29 | 0.15 | 28.9% | 60% | bull-only |
| `rank(fnd6_newa1v1300_epspi / close)` | TOP1000 | 0.15 | 0.07 | 30.6% | 40% | bull-only |
| `rank(fnd6_newa1v1300_epspi)` | TOP3000 | 0.09 | 0.03 | 41.1% | 60% | bull-only |
| `rank(fnd6_newa1v1300_epspi)` | TOP1000 | 0.08 | 0.03 | 37.6% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_newa1v1300_epspx: 0.999 (strongly positively correlated)
- fnd6_newa1v1300_epsfi: 0.990 (strongly positively correlated)
- fnd6_newa1v1300_epsfx: 0.989 (strongly positively correlated)
- fnd6_newa1v1300_ibcom: 0.858 (strongly positively correlated)
- fnd6_newa2v1300_ni: 0.851 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
