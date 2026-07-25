---
field: fnd6_newqv1300_epspiq
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
max_drawdown: 0.3735
ann_vol: 0.1082
hit_rate: 0.4996
rolling_sharpe_min: -4.509
rolling_sharpe_max: 2.846
negated_best_sharpe: 0.75
negated_best_template: rank_neg_delta
negated_best_fitness: 0.24
n_negated_sims: 10
direction_gap: 0.47
---
# fnd6_newqv1300_epspiq (fundamental6)

*Earnings Per Share (Basic) - Including Extraordinary Items*

## Signal Profile
- `rank(fnd6_newqv1300_epspiq)`: S=0.22, F=0.10, T=2.2%, INFERIOR (TOP3000)
- `rank(fnd6_newqv1300_epspiq / close)`: S=0.28, F=0.14, T=3.1%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_newqv1300_epspiq, 5))`: S=0.14, F=0.03, T=36.9%, INFERIOR (TOP200)
- `-rank(fnd6_newqv1300_epspiq)`: S=-0.16, F=-0.06, T=2.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_epspiq, 5))`: S=0.75, F=0.24, T=37.3%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_newqv1300_epspiq, 22)`: S=0.37, F=0.11, T=37.4%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newqv1300_epspiq, 10)`: S=0.09, F=0.02, T=2.6%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newqv1300_epspiq, 22))`: S=0.34, F=0.10, T=16.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_epspiq)`: S=-0.22, F=-0.10, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_epspiq / close)`: S=-0.28, F=-0.14, T=3.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 6F/26P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 15F/14P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.28, Consistency 40% positive years (2/5)
Yearly breakdown:
  - 2019: S=-0.18 (negative), ret=-0.8%
  - 2020: S=-3.85 (negative), ret=-25.8%
  - 2021: S=1.67 (strong), ret=+18.9%
  - 2022: S=1.58 (strong), ret=+25.2%
  - 2023: S=-0.27 (negative), ret=-2.9%

## Risk & Drawdown
- Max drawdown: 37.35% over 801 days (recovered)
- Annualized: return +3.0%, volatility 10.8% (fraction of booksize)
- Hit rate: 50.0% positive days
- Tail shape: skew -0.17, excess kurtosis +1.46

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -4.51, max 2.85, latest -0.45

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2020
Best month: +7.47%; worst month: -9.34%
Positive months: 56%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.84
- Sideways: S=0.42
- Bear: S=-3.30

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_newqv1300_epspiq, 5))` S=0.75, F=0.24, INFERIOR
Direction gap: +0.47 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fnd6_newqv1300_epspiq)`: S=-0.22, F=-0.10, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_epspiq / close)`: S=-0.28, F=-0.14, T=3.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_epspiq, 5))`: S=0.75, F=0.24, T=37.3%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newqv1300_epspiq / close)` | TOP3000 | 0.28 | 0.14 | 37.4% | 40% | bull-only |
| `rank(fnd6_newqv1300_epspiq)` | TOP3000 | 0.22 | 0.10 | 41.5% | 60% | bull-only |
| `rank(fnd6_newqv1300_epspiq)` | TOP1000 | 0.15 | 0.06 | 39.1% | 60% | bull-only |
| `rank(fnd6_newqv1300_epspiq / close)` | TOP1000 | 0.12 | 0.05 | 33.5% | 40% | bull-only |
| `rank(ts_delta(fnd6_newqv1300_epspiq, 5))` | TOP200 | 0.13 | 0.03 | 29.9% | 60% | weak |

## Correlation Notes
Top correlates:
- eps: 1.000 (strongly positively correlated)
- fnd6_newqv1300_epsfiq: 1.000 (strongly positively correlated)
- fnd6_newqv1300_epspxq: 0.999 (strongly positively correlated)
- fnd6_cptnewqv1300_epsfxq: 0.999 (strongly positively correlated)
- earnings_per_share_reported_value: 0.991 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
