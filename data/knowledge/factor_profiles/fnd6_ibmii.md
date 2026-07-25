---
field: fnd6_ibmii
dataset: fundamental6
best_template: neg_rank_level
best_sharpe: 0.44
best_fitness: 0.31
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: weak
n_variations_with_pnl: 2
max_drawdown: 0.459
ann_vol: 0.2087
hit_rate: 0.4923
rolling_sharpe_min: -1.929
rolling_sharpe_max: 2.243
negated_best_sharpe: 0.44
negated_best_template: neg_rank_level
negated_best_fitness: 0.31
n_negated_sims: 10
direction_gap: 0.24
---
# fnd6_ibmii (fundamental6)

*Income before Extraordinary Items and Noncontrolling Interests*

## Signal Profile
- `rank(fnd6_ibmii)`: S=0.01, F=0.00, T=1.0%, INFERIOR (TOP3000)
- `rank(fnd6_ibmii / close)`: S=0.11, F=0.04, T=1.4%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_ibmii, 5))`: S=0.20, F=0.07, T=33.1%, INFERIOR (TOP200)
- `-rank(fnd6_ibmii)`: S=0.02, F=0.00, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_ibmii, 5))`: S=-0.22, F=-0.08, T=33.3%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_ibmii, 22)`: S=-0.26, F=-0.12, T=28.1%, INFERIOR (TOP3000)
- `ts_mean(fnd6_ibmii, 10)`: S=0.12, F=0.04, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_ibmii, 22))`: S=-0.45, F=-0.23, T=14.6%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_ibmii)`: S=0.44, F=0.31, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_ibmii / close)`: S=0.42, F=0.29, T=2.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/6P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.19, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.56 (moderate), ret=+7.8%
  - 2020: S=-0.76 (negative), ret=-12.8%
  - 2021: S=0.31 (weak), ret=+7.7%
  - 2022: S=0.73 (moderate), ret=+20.8%
  - 2023: S=-0.26 (negative), ret=-3.7%

## Risk & Drawdown
- Max drawdown: 45.90% over 933 days (recovered)
- Annualized: return +4.0%, volatility 20.9% (fraction of booksize)
- Hit rate: 49.2% positive days
- Tail shape: skew -1.49, excess kurtosis +19.85

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.93, max 2.24, latest -0.17

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +24.23%; worst month: -20.91%
Positive months: 48%

## Regime Profile
Regime profile: **weak**
- Bull: S=-0.17
- Sideways: S=0.74
- Bear: S=0.18

## Negated Direction
Best negated: `rank(-1 * fnd6_ibmii)` S=0.44, F=0.31, INFERIOR
Direction gap: +0.24 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fnd6_ibmii)`: S=0.44, F=0.31, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_ibmii / close)`: S=0.42, F=0.29, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_ibmii, 5))`: S=-0.22, F=-0.08, T=33.3%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_ibmii, 5))` | TOP200 | 0.19 | 0.07 | 45.9% | 60% | weak |
| `rank(fnd6_ibmii / close)` | TOP3000 | 0.10 | 0.04 | 35.8% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_newa2v1300_ni: 0.921 (strongly positively correlated)
- fnd6_newa1v1300_ib: 0.918 (strongly positively correlated)
- fnd6_newa2v1300_pi: 0.915 (strongly positively correlated)
- fnd6_newa1v1300_ibcom: 0.901 (strongly positively correlated)
- fnd6_newa1v1300_ibc: 0.883 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
