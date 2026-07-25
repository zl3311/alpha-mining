---
field: fnd6_newqv1300_txpq
dataset: fundamental6
best_template: rank_neg_delta
best_sharpe: 0.74
best_fitness: 0.42
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 5
max_drawdown: 0.2467
ann_vol: 0.0795
hit_rate: 0.5036
rolling_sharpe_min: -2.797
rolling_sharpe_max: 4.146
negated_best_sharpe: 0.74
negated_best_template: rank_neg_delta
negated_best_fitness: 0.42
n_negated_sims: 10
direction_gap: -0.03
---
# fnd6_newqv1300_txpq (fundamental6)

*Income Taxes Payable*

## Signal Profile
- `rank(fnd6_newqv1300_txpq)`: S=0.13, F=0.04, T=3.0%, INFERIOR (TOP3000)
- `rank(fnd6_newqv1300_txpq / close)`: S=0.14, F=0.04, T=3.0%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_newqv1300_txpq, 5))`: S=0.47, F=0.14, T=40.0%, INFERIOR (TOP3000)
- `-rank(fnd6_newqv1300_txpq)`: S=-0.07, F=-0.02, T=4.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_txpq, 5))`: S=0.74, F=0.42, T=44.4%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_newqv1300_txpq, 63)`: S=0.77, F=0.35, T=19.8%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newqv1300_txpq, 10)`: S=-0.04, F=-0.01, T=3.1%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newqv1300_txpq, 22))`: S=-0.73, F=-0.37, T=18.3%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_txpq)`: S=0.31, F=0.16, T=6.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_txpq / close)`: S=0.29, F=0.14, T=6.0%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 11F/21P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/6P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.48, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=1.33 (moderate), ret=+9.0%
  - 2020: S=-2.46 (negative), ret=-17.4%
  - 2021: S=-0.64 (negative), ret=-5.5%
  - 2022: S=3.83 (strong), ret=+31.0%
  - 2023: S=0.18 (weak), ret=+1.5%

## Risk & Drawdown
- Max drawdown: 24.67% over 1034 days (recovered)
- Annualized: return +3.8%, volatility 8.0% (fraction of booksize)
- Hit rate: 50.4% positive days
- Tail shape: skew -0.07, excess kurtosis +4.48

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.80, max 4.15, latest 0.10

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +11.41%; worst month: -6.88%
Positive months: 51%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=1.71
- Sideways: S=0.03
- Bear: S=-0.72

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_newqv1300_txpq, 5))` S=0.74, F=0.42, INFERIOR
Direction gap: -0.03 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_newqv1300_txpq)`: S=0.31, F=0.16, T=6.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_txpq / close)`: S=0.29, F=0.14, T=6.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_txpq, 5))`: S=0.74, F=0.42, T=44.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_newqv1300_txpq, 5))` | TOP3000 | 0.48 | 0.14 | 24.7% | 60% | bull-only |
| `rank(fnd6_newqv1300_txpq)` | TOP3000 | 0.12 | 0.04 | 21.3% | 40% | bull-only |
| `rank(fnd6_newqv1300_txpq / close)` | TOP3000 | 0.14 | 0.04 | 17.1% | 60% | bull-only |
| `rank(fnd6_newqv1300_txpq / close)` | TOP1000 | 0.11 | 0.03 | 14.8% | 40% | bull-only |
| `rank(fnd6_newqv1300_txpq)` | TOP1000 | 0.06 | 0.02 | 21.4% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_newqv1300_aocipenq: -0.123 (weakly negatively correlated)
- fnd6_newqv1300_rcpq: -0.112 (weakly negatively correlated)
- fnd6_esopct: -0.102 (weakly negatively correlated)
- implied_volatility_mean_skew_20: 0.099 (weakly positively correlated)
- pcr_vol_30: 0.096 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
