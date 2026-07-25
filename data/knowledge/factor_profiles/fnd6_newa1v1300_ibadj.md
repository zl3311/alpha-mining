---
field: fnd6_newa1v1300_ibadj
dataset: fundamental6
best_template: rank_delta
best_sharpe: 0.58
best_fitness: 0.34
best_universe: TOP200
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: weak
n_variations_with_pnl: 3
max_drawdown: 0.4428
ann_vol: 0.1926
hit_rate: 0.502
rolling_sharpe_min: -1.886
rolling_sharpe_max: 3.079
redundancy_cluster: 94
negated_best_sharpe: 0.42
negated_best_template: neg_rank_level
negated_best_fitness: 0.3
n_negated_sims: 10
direction_gap: -0.16
---
# fnd6_newa1v1300_ibadj (fundamental6)

*Income Before Extraordinary Items - Adjusted for Common Stock Equivalents*

## Signal Profile
- `rank(fnd6_newa1v1300_ibadj)`: S=0.01, F=0.00, T=1.0%, INFERIOR (TOP3000)
- `rank(fnd6_newa1v1300_ibadj / close)`: S=0.13, F=0.04, T=1.4%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_newa1v1300_ibadj, 5))`: S=0.58, F=0.34, T=33.2%, INFERIOR (TOP200)
- `-rank(fnd6_newa1v1300_ibadj)`: S=0.05, F=0.01, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa1v1300_ibadj, 5))`: S=-0.43, F=-0.22, T=33.0%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_newa1v1300_ibadj, 22)`: S=-0.23, F=-0.10, T=28.2%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newa1v1300_ibadj, 10)`: S=0.11, F=0.03, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newa1v1300_ibadj, 22))`: S=-0.21, F=-0.07, T=14.6%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_ibadj)`: S=0.42, F=0.30, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_ibadj / close)`: S=0.38, F=0.25, T=2.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 11F/21P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/6P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.57, Consistency 40% positive years (2/5)
Yearly breakdown:
  - 2019: S=2.30 (strong), ret=+30.5%
  - 2020: S=-0.03 (negative), ret=-0.5%
  - 2021: S=-0.38 (negative), ret=-8.8%
  - 2022: S=1.64 (strong), ret=+39.3%
  - 2023: S=-0.45 (negative), ret=-6.3%

## Risk & Drawdown
- Max drawdown: 44.28% over 791 days (recovered)
- Annualized: return +11.1%, volatility 19.3% (fraction of booksize)
- Hit rate: 50.2% positive days
- Tail shape: skew -0.27, excess kurtosis +10.28

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.89, max 3.08, latest -0.36

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2023
Best month: +20.78%; worst month: -10.13%
Positive months: 49%

## Regime Profile
Regime profile: **weak**
- Bull: S=0.15
- Sideways: S=1.66
- Bear: S=0.09

## Negated Direction
Best negated: `rank(-1 * fnd6_newa1v1300_ibadj)` S=0.42, F=0.30, INFERIOR
Direction gap: -0.16 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_newa1v1300_ibadj)`: S=0.42, F=0.30, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_ibadj / close)`: S=0.38, F=0.25, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa1v1300_ibadj, 5))`: S=-0.43, F=-0.22, T=33.0%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_newa1v1300_ibadj, 5))` | TOP200 | 0.57 | 0.34 | 44.3% | 40% | weak |
| `rank(fnd6_newa1v1300_ibadj / close)` | TOP3000 | 0.11 | 0.04 | 34.8% | 60% | bull-only |
| `rank(ts_delta(fnd6_newa1v1300_ibadj, 5))` | TOP1000 | 0.11 | 0.02 | 22.0% | 80% | weak |

## Correlation Notes
Top correlates:
- fnd6_niadj: 0.996 (strongly positively correlated)
- fnd6_dilavx: 0.968 (strongly positively correlated)
- fnd6_newa1v1300_ibcom: 0.941 (strongly positively correlated)
- fnd6_newa1v1300_ib: 0.921 (strongly positively correlated)
- fnd6_newa2v1300_ni: 0.921 (strongly positively correlated)

Redundancy cluster #94: 4 similar fields, mean |rho| 0.883 (representative). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
