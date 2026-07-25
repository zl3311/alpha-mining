---
field: fnd6_newa1v1300_ibcom
dataset: fundamental6
best_template: neg_rank_level
best_sharpe: 0.43
best_fitness: 0.3
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: weak
n_variations_with_pnl: 2
max_drawdown: 0.4344
ann_vol: 0.1933
hit_rate: 0.4988
rolling_sharpe_min: -1.815
rolling_sharpe_max: 2.216
negated_best_sharpe: 0.43
negated_best_template: neg_rank_level
negated_best_fitness: 0.3
n_negated_sims: 10
direction_gap: 0.08
---
# fnd6_newa1v1300_ibcom (fundamental6)

*Income Before Extraordinary Items - Available for Common*

## Signal Profile
- `rank(fnd6_newa1v1300_ibcom)`: S=0.01, F=0.00, T=1.0%, INFERIOR (TOP3000)
- `rank(fnd6_newa1v1300_ibcom / close)`: S=0.13, F=0.04, T=1.4%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_newa1v1300_ibcom, 5))`: S=0.35, F=0.16, T=33.4%, INFERIOR (TOP200)
- `-rank(fnd6_newa1v1300_ibcom)`: S=0.05, F=0.01, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa1v1300_ibcom, 5))`: S=-0.25, F=-0.10, T=33.2%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_newa1v1300_ibcom, 22)`: S=-0.24, F=-0.11, T=28.1%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newa1v1300_ibcom, 10)`: S=0.11, F=0.03, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newa1v1300_ibcom, 22))`: S=-0.27, F=-0.11, T=14.6%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_ibcom)`: S=0.43, F=0.30, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_ibcom / close)`: S=0.38, F=0.25, T=2.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 11F/21P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/6P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.34, Consistency 40% positive years (2/5)
Yearly breakdown:
  - 2019: S=0.88 (moderate), ret=+12.8%
  - 2020: S=-0.23 (negative), ret=-4.0%
  - 2021: S=-0.23 (negative), ret=-5.4%
  - 2022: S=1.40 (moderate), ret=+32.2%
  - 2023: S=-0.22 (negative), ret=-3.1%

## Risk & Drawdown
- Max drawdown: 43.44% over 933 days (recovered)
- Annualized: return +6.6%, volatility 19.3% (fraction of booksize)
- Hit rate: 49.9% positive days
- Tail shape: skew -0.54, excess kurtosis +8.66

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.81, max 2.22, latest -0.13

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +22.71%; worst month: -9.86%
Positive months: 48%

## Regime Profile
Regime profile: **weak**
- Bull: S=-0.02
- Sideways: S=1.03
- Bear: S=0.11

## Negated Direction
Best negated: `rank(-1 * fnd6_newa1v1300_ibcom)` S=0.43, F=0.30, INFERIOR
Direction gap: +0.08 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fnd6_newa1v1300_ibcom)`: S=0.43, F=0.30, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_ibcom / close)`: S=0.38, F=0.25, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa1v1300_ibcom, 5))`: S=-0.25, F=-0.10, T=33.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_newa1v1300_ibcom, 5))` | TOP200 | 0.34 | 0.16 | 43.4% | 40% | weak |
| `rank(fnd6_newa1v1300_ibcom / close)` | TOP3000 | 0.12 | 0.04 | 34.5% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_newa1v1300_ib: 0.979 (strongly positively correlated)
- fnd6_newa2v1300_ni: 0.977 (strongly positively correlated)
- fnd6_newa1v1300_ibadj: 0.941 (strongly positively correlated)
- fnd6_niadj: 0.938 (strongly positively correlated)
- fnd6_dilavx: 0.916 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
