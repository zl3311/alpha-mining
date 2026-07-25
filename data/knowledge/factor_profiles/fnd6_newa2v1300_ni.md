---
field: fnd6_newa2v1300_ni
dataset: fundamental6
best_template: rank_delta
best_sharpe: 0.37
best_fitness: 0.17
best_universe: TOP200
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: weak
n_variations_with_pnl: 3
max_drawdown: 0.3946
ann_vol: 0.193
hit_rate: 0.5004
rolling_sharpe_min: -1.641
rolling_sharpe_max: 2.201
negated_best_sharpe: 0.4
negated_best_template: rank_neg_delta
negated_best_fitness: 0.15
n_negated_sims: 10
direction_gap: 0.03
---
# fnd6_newa2v1300_ni (fundamental6)

*Net Income (Loss)*

## Signal Profile
- `rank(fnd6_newa2v1300_ni)`: S=0.00, F=0.00, T=1.0%, INFERIOR (TOP3000)
- `rank(fnd6_newa2v1300_ni / close)`: S=0.11, F=0.03, T=1.4%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_newa2v1300_ni, 5))`: S=0.37, F=0.17, T=33.3%, INFERIOR (TOP200)
- `-rank(fnd6_newa2v1300_ni)`: S=0.03, F=0.01, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa2v1300_ni, 5))`: S=0.40, F=0.15, T=34.7%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_newa2v1300_ni, 63)`: S=-0.23, F=-0.09, T=18.8%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newa2v1300_ni, 10)`: S=0.13, F=0.04, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newa2v1300_ni, 22))`: S=-0.46, F=-0.24, T=14.6%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa2v1300_ni)`: S=0.03, F=0.01, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa2v1300_ni / close)`: S=-0.07, F=-0.02, T=1.8%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 11F/21P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 17F/12P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.36, Consistency 40% positive years (2/5)
Yearly breakdown:
  - 2019: S=0.69 (moderate), ret=+9.7%
  - 2020: S=-0.32 (negative), ret=-5.5%
  - 2021: S=-0.16 (negative), ret=-3.9%
  - 2022: S=1.56 (strong), ret=+36.2%
  - 2023: S=-0.15 (negative), ret=-2.1%

## Risk & Drawdown
- Max drawdown: 39.46% over 759 days (recovered)
- Annualized: return +7.0%, volatility 19.3% (fraction of booksize)
- Hit rate: 50.0% positive days
- Tail shape: skew -0.58, excess kurtosis +8.65

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.64, max 2.20, latest -0.06

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +22.74%; worst month: -11.14%
Positive months: 51%

## Regime Profile
Regime profile: **weak**
- Bull: S=0.09
- Sideways: S=0.85
- Bear: S=0.22

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_newa2v1300_ni, 5))` S=0.40, F=0.15, INFERIOR
Direction gap: +0.03 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fnd6_newa2v1300_ni)`: S=0.03, F=0.01, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa2v1300_ni / close)`: S=-0.07, F=-0.02, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa2v1300_ni, 5))`: S=0.40, F=0.15, T=34.7%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_newa2v1300_ni, 5))` | TOP200 | 0.36 | 0.17 | 39.5% | 40% | weak |
| `rank(fnd6_newa2v1300_ni / close)` | TOP3000 | 0.10 | 0.03 | 34.6% | 60% | bull-only |
| `rank(fnd6_newa2v1300_ni / close)` | TOP1000 | 0.05 | 0.02 | 35.6% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_newa1v1300_ib: 0.996 (strongly positively correlated)
- fnd6_newa1v1300_ibcom: 0.977 (strongly positively correlated)
- fnd6_niadj: 0.923 (strongly positively correlated)
- fnd6_newa1v1300_ibadj: 0.921 (strongly positively correlated)
- fnd6_ibmii: 0.921 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
