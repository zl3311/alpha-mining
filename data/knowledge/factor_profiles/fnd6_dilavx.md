---
field: fnd6_dilavx
dataset: fundamental6
best_template: neg_rank_level
best_sharpe: 0.44
best_fitness: 0.32
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: weak
n_variations_with_pnl: 3
max_drawdown: 0.4702
ann_vol: 0.1961
hit_rate: 0.5053
rolling_sharpe_min: -2.058
rolling_sharpe_max: 2.487
redundancy_cluster: 94
negated_best_sharpe: 0.44
negated_best_template: neg_rank_level
negated_best_fitness: 0.32
n_negated_sims: 10
direction_gap: -0.1
---
# fnd6_dilavx (fundamental6)

*Dilution Available - Excluding Extraordinary Items*

## Signal Profile
- `rank(fnd6_dilavx)`: S=0.01, F=0.00, T=1.0%, INFERIOR (TOP3000)
- `rank(fnd6_dilavx / close)`: S=0.13, F=0.04, T=1.4%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_dilavx, 5))`: S=0.54, F=0.30, T=33.4%, INFERIOR (TOP200)
- `-rank(fnd6_dilavx)`: S=0.04, F=0.01, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_dilavx, 5))`: S=-0.29, F=-0.12, T=33.2%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_dilavx, 22)`: S=-0.25, F=-0.11, T=28.1%, INFERIOR (TOP3000)
- `ts_mean(fnd6_dilavx, 10)`: S=0.10, F=0.03, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_dilavx, 22))`: S=-0.33, F=-0.15, T=14.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_dilavx)`: S=0.44, F=0.32, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_dilavx / close)`: S=0.39, F=0.26, T=2.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 11F/21P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/6P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.54, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=1.68 (strong), ret=+24.4%
  - 2020: S=0.00 (negative), ret=+0.0%
  - 2021: S=-0.40 (negative), ret=-9.2%
  - 2022: S=1.71 (strong), ret=+41.1%
  - 2023: S=-0.34 (negative), ret=-4.7%

## Risk & Drawdown
- Max drawdown: 47.02% over 791 days (recovered)
- Annualized: return +10.5%, volatility 19.6% (fraction of booksize)
- Hit rate: 50.5% positive days
- Tail shape: skew -0.33, excess kurtosis +9.68

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.06, max 2.49, latest -0.24

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2021
Best month: +20.83%; worst month: -10.07%
Positive months: 52%

## Regime Profile
Regime profile: **weak**
- Bull: S=0.31
- Sideways: S=1.31
- Bear: S=0.12

## Negated Direction
Best negated: `rank(-1 * fnd6_dilavx)` S=0.44, F=0.32, INFERIOR
Direction gap: -0.10 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_dilavx)`: S=0.44, F=0.32, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_dilavx / close)`: S=0.39, F=0.26, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_dilavx, 5))`: S=-0.29, F=-0.12, T=33.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_dilavx, 5))` | TOP200 | 0.54 | 0.30 | 47.0% | 60% | weak |
| `rank(fnd6_dilavx / close)` | TOP3000 | 0.12 | 0.04 | 35.2% | 60% | bull-only |
| `rank(fnd6_dilavx / close)` | TOP1000 | 0.05 | 0.02 | 36.5% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_newa1v1300_ibadj: 0.968 (strongly positively correlated)
- fnd6_niadj: 0.965 (strongly positively correlated)
- fnd6_newa1v1300_ibcom: 0.916 (strongly positively correlated)
- fnd6_newa2v1300_ni: 0.907 (strongly positively correlated)
- fnd6_newa1v1300_ib: 0.907 (strongly positively correlated)

Redundancy cluster #94: 4 similar fields, mean |rho| 0.883 (representative: fnd6_newa1v1300_ibadj). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
