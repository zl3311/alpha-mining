---
field: fnd6_newqv1300_epspxq
dataset: fundamental6
best_template: rank_neg_delta
best_sharpe: 0.75
best_fitness: 0.24
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 5
max_drawdown: 0.3681
ann_vol: 0.1084
hit_rate: 0.4972
rolling_sharpe_min: -4.454
rolling_sharpe_max: 2.83
negated_best_sharpe: 0.75
negated_best_template: rank_neg_delta
negated_best_fitness: 0.24
n_negated_sims: 10
direction_gap: 0.44
---
# fnd6_newqv1300_epspxq (fundamental6)

*Earnings Per Share (Basic) - Excluding Extraordinary Items*

## Signal Profile
- `rank(fnd6_newqv1300_epspxq)`: S=0.24, F=0.11, T=2.2%, INFERIOR (TOP3000)
- `rank(fnd6_newqv1300_epspxq / close)`: S=0.31, F=0.16, T=3.1%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_newqv1300_epspxq, 5))`: S=0.09, F=0.02, T=36.9%, INFERIOR (TOP200)
- `-rank(fnd6_newqv1300_epspxq)`: S=-0.16, F=-0.06, T=2.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_epspxq, 5))`: S=0.75, F=0.24, T=37.3%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_newqv1300_epspxq, 22)`: S=0.33, F=0.10, T=37.4%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newqv1300_epspxq, 10)`: S=0.12, F=0.04, T=2.6%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newqv1300_epspxq, 22))`: S=0.28, F=0.08, T=16.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_epspxq)`: S=-0.24, F=-0.11, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_epspxq / close)`: S=-0.31, F=-0.16, T=3.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 6F/26P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/16P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.30, Consistency 40% positive years (2/5)
Yearly breakdown:
  - 2019: S=-0.04 (negative), ret=-0.1%
  - 2020: S=-3.78 (negative), ret=-25.2%
  - 2021: S=1.65 (strong), ret=+18.7%
  - 2022: S=1.60 (strong), ret=+25.7%
  - 2023: S=-0.26 (negative), ret=-2.8%

## Risk & Drawdown
- Max drawdown: 36.81% over 801 days (recovered)
- Annualized: return +3.3%, volatility 10.8% (fraction of booksize)
- Hit rate: 49.7% positive days
- Tail shape: skew -0.17, excess kurtosis +1.43

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -4.45, max 2.83, latest -0.44

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2020
Best month: +7.42%; worst month: -9.21%
Positive months: 56%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.84
- Sideways: S=0.48
- Bear: S=-3.26

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_newqv1300_epspxq, 5))` S=0.75, F=0.24, INFERIOR
Direction gap: +0.44 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fnd6_newqv1300_epspxq)`: S=-0.24, F=-0.11, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_epspxq / close)`: S=-0.31, F=-0.16, T=3.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_epspxq, 5))`: S=0.75, F=0.24, T=37.3%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newqv1300_epspxq / close)` | TOP3000 | 0.30 | 0.16 | 36.8% | 40% | bull-only |
| `rank(fnd6_newqv1300_epspxq)` | TOP3000 | 0.23 | 0.11 | 41.4% | 60% | bull-only |
| `rank(fnd6_newqv1300_epspxq)` | TOP1000 | 0.15 | 0.06 | 38.7% | 60% | bull-only |
| `rank(fnd6_newqv1300_epspxq / close)` | TOP1000 | 0.11 | 0.04 | 33.4% | 60% | bull-only |
| `rank(ts_delta(fnd6_newqv1300_epspxq, 5))` | TOP200 | 0.08 | 0.02 | 31.3% | 60% | weak |

## Correlation Notes
Top correlates:
- fnd6_cptnewqv1300_epsfxq: 1.000 (strongly positively correlated)
- fnd6_newqv1300_epspiq: 0.999 (strongly positively correlated)
- eps: 0.999 (strongly positively correlated)
- fnd6_newqv1300_epsfiq: 0.999 (strongly positively correlated)
- earnings_per_share_reported_value: 0.991 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
