---
field: fnd6_newa1v1300_epsfx
dataset: fundamental6
best_template: rank_delta
best_sharpe: 0.52
best_fitness: 0.3
best_universe: TOP200
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: weak
n_variations_with_pnl: 5
max_drawdown: 0.4335
ann_vol: 0.2084
hit_rate: 0.5069
rolling_sharpe_min: -1.797
rolling_sharpe_max: 2.269
redundancy_cluster: 94
negated_best_sharpe: 0.54
negated_best_template: rank_neg_delta
negated_best_fitness: 0.27
n_negated_sims: 10
direction_gap: 0.02
---
# fnd6_newa1v1300_epsfx (fundamental6)

*Earnings Per Share (Diluted) - Excluding Extraordinary Items*

## Signal Profile
- `rank(fnd6_newa1v1300_epsfx)`: S=0.10, F=0.03, T=1.1%, INFERIOR (TOP3000)
- `rank(fnd6_newa1v1300_epsfx / close)`: S=0.31, F=0.16, T=1.9%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_newa1v1300_epsfx, 5))`: S=0.52, F=0.30, T=33.2%, INFERIOR (TOP200)
- `-rank(fnd6_newa1v1300_epsfx)`: S=-0.07, F=-0.02, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa1v1300_epsfx, 5))`: S=0.54, F=0.27, T=33.9%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_newa1v1300_epsfx, 22)`: S=-0.05, F=-0.01, T=28.2%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newa1v1300_epsfx, 10)`: S=-0.06, F=-0.01, T=1.4%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newa1v1300_epsfx, 22))`: S=-0.80, F=-0.52, T=14.7%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_epsfx)`: S=0.10, F=0.03, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_epsfx / close)`: S=0.14, F=0.05, T=2.7%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 11F/21P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 20F/9P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.52, Consistency 40% positive years (2/5)
Yearly breakdown:
  - 2019: S=1.61 (strong), ret=+22.9%
  - 2020: S=-0.47 (negative), ret=-8.6%
  - 2021: S=-0.04 (negative), ret=-1.0%
  - 2022: S=1.56 (strong), ret=+43.5%
  - 2023: S=-0.25 (negative), ret=-3.7%

## Risk & Drawdown
- Max drawdown: 43.35% over 715 days (recovered)
- Annualized: return +10.8%, volatility 20.8% (fraction of booksize)
- Hit rate: 50.7% positive days
- Tail shape: skew -1.38, excess kurtosis +19.49

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.80, max 2.27, latest -0.17

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2020
Best month: +22.63%; worst month: -10.02%
Positive months: 52%

## Regime Profile
Regime profile: **weak**
- Bull: S=0.36
- Sideways: S=1.21
- Bear: S=0.10

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_newa1v1300_epsfx, 5))` S=0.54, F=0.27, INFERIOR
Direction gap: +0.02 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fnd6_newa1v1300_epsfx)`: S=0.10, F=0.03, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_epsfx / close)`: S=0.14, F=0.05, T=2.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa1v1300_epsfx, 5))`: S=0.54, F=0.27, T=33.9%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_newa1v1300_epsfx, 5))` | TOP200 | 0.52 | 0.30 | 43.4% | 40% | weak |
| `rank(fnd6_newa1v1300_epsfx / close)` | TOP3000 | 0.30 | 0.16 | 29.4% | 60% | bull-only |
| `rank(fnd6_newa1v1300_epsfx / close)` | TOP1000 | 0.14 | 0.06 | 31.3% | 40% | bull-only |
| `rank(fnd6_newa1v1300_epsfx)` | TOP3000 | 0.08 | 0.03 | 41.8% | 60% | bull-only |
| `rank(fnd6_newa1v1300_epsfx)` | TOP1000 | 0.06 | 0.02 | 38.6% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_newa1v1300_epsfi: 0.999 (strongly positively correlated)
- fnd6_newa1v1300_epspx: 0.990 (strongly positively correlated)
- fnd6_newa1v1300_epspi: 0.989 (strongly positively correlated)
- fnd6_newa1v1300_ibcom: 0.870 (strongly positively correlated)
- fnd6_newa2v1300_ni: 0.859 (strongly positively correlated)

Redundancy cluster #94: 4 similar fields, mean |rho| 0.883 (representative: fnd6_newa1v1300_ibadj). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
