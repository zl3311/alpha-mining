---
field: fnd6_newa2v1300_pi
dataset: fundamental6
best_template: neg_rank_level
best_sharpe: 0.42
best_fitness: 0.3
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 2
max_drawdown: 0.4259
ann_vol: 0.209
hit_rate: 0.5061
rolling_sharpe_min: -1.815
rolling_sharpe_max: 2.201
negated_best_sharpe: 0.42
negated_best_template: neg_rank_level
negated_best_fitness: 0.3
n_negated_sims: 10
direction_gap: 0.07
---
# fnd6_newa2v1300_pi (fundamental6)

*Pretax Income*

## Signal Profile
- `rank(fnd6_newa2v1300_pi)`: S=0.01, F=0.00, T=1.0%, INFERIOR (TOP3000)
- `rank(fnd6_newa2v1300_pi / close)`: S=0.13, F=0.04, T=1.4%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_newa2v1300_pi, 5))`: S=0.35, F=0.16, T=33.4%, INFERIOR (TOP200)
- `-rank(fnd6_newa2v1300_pi)`: S=0.04, F=0.01, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa2v1300_pi, 5))`: S=-0.24, F=-0.09, T=33.3%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_newa2v1300_pi, 63)`: S=-0.21, F=-0.08, T=18.7%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newa2v1300_pi, 10)`: S=0.11, F=0.03, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newa2v1300_pi, 22))`: S=-0.33, F=-0.14, T=14.6%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa2v1300_pi)`: S=0.42, F=0.30, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa2v1300_pi / close)`: S=0.35, F=0.22, T=2.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 11F/21P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/6P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.34, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.88 (moderate), ret=+12.0%
  - 2020: S=-0.30 (negative), ret=-5.1%
  - 2021: S=0.49 (weak), ret=+12.3%
  - 2022: S=0.80 (moderate), ret=+22.4%
  - 2023: S=-0.42 (negative), ret=-6.4%

## Risk & Drawdown
- Max drawdown: 42.59% over 900 days (recovered)
- Annualized: return +7.2%, volatility 20.9% (fraction of booksize)
- Hit rate: 50.6% positive days
- Tail shape: skew -1.46, excess kurtosis +19.89

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.81, max 2.20, latest -0.34

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2023
Best month: +24.25%; worst month: -20.92%
Positive months: 52%

## Regime Profile
Regime profile: **mixed**
- Bull: S=-0.19
- Sideways: S=0.80
- Bear: S=0.63

## Negated Direction
Best negated: `rank(-1 * fnd6_newa2v1300_pi)` S=0.42, F=0.30, INFERIOR
Direction gap: +0.07 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fnd6_newa2v1300_pi)`: S=0.42, F=0.30, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa2v1300_pi / close)`: S=0.35, F=0.22, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa2v1300_pi, 5))`: S=-0.24, F=-0.09, T=33.3%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_newa2v1300_pi, 5))` | TOP200 | 0.34 | 0.16 | 42.6% | 60% | mixed |
| `rank(fnd6_newa2v1300_pi / close)` | TOP3000 | 0.12 | 0.04 | 34.4% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_ibmii: 0.915 (strongly positively correlated)
- fnd6_newa2v1300_ni: 0.833 (strongly positively correlated)
- fnd6_newa1v1300_ib: 0.832 (strongly positively correlated)
- fnd6_newa1v1300_ibcom: 0.816 (strongly positively correlated)
- fnd6_newa1v1300_ibc: 0.804 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
