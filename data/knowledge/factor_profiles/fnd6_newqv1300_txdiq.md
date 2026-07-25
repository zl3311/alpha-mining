---
field: fnd6_newqv1300_txdiq
dataset: fundamental6
best_template: rank_delta
best_sharpe: 0.62
best_fitness: 0.71
best_universe: TOP200
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: all-weather
n_variations_with_pnl: 3
max_drawdown: 0.7443
ann_vol: 0.3303
hit_rate: 0.2032
rolling_sharpe_min: -1.897
rolling_sharpe_max: 2.258
negated_best_sharpe: 0.91
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.61
n_negated_sims: 10
direction_gap: 0.29
---
# fnd6_newqv1300_txdiq (fundamental6)

*Income Taxes - Deferred*

## Signal Profile
- `rank(fnd6_newqv1300_txdiq)`: S=-0.07, F=-0.03, T=13.0%, INFERIOR (TOP200)
- `rank(fnd6_newqv1300_txdiq / close)`: S=-0.08, F=-0.04, T=12.9%, INFERIOR (TOP200)
- `rank(ts_delta(fnd6_newqv1300_txdiq, 5))`: S=0.62, F=0.71, T=16.2%, INFERIOR (TOP200)
- `-rank(fnd6_newqv1300_txdiq)`: S=0.48, F=0.31, T=11.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_txdiq, 5))`: S=-0.50, F=-0.25, T=39.6%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_newqv1300_txdiq, 63)`: S=0.40, F=0.25, T=15.5%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newqv1300_txdiq, 10)`: S=-0.46, F=-0.39, T=10.5%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newqv1300_txdiq, 22))`: S=-0.65, F=-0.50, T=20.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_txdiq)`: S=0.91, F=0.60, T=8.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_txdiq / close)`: S=0.91, F=0.61, T=8.6%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 17F/15P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 8F/21P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.61, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.94 (moderate), ret=+17.8%
  - 2020: S=1.62 (strong), ret=+20.7%
  - 2021: S=0.13 (weak), ret=+7.3%
  - 2022: S=1.36 (moderate), ret=+50.8%
  - 2023: S=0.13 (weak), ret=+2.7%

## Risk & Drawdown
- Max drawdown: 74.43% over 404 days (recovered)
- Annualized: return +20.2%, volatility 33.0% (fraction of booksize)
- Hit rate: 20.3% positive days
- Tail shape: skew +3.34, excess kurtosis +49.35

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.90, max 2.26, latest 0.12

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2023
Best month: +64.15%; worst month: -27.38%
Positive months: 58%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=0.95
- Sideways: S=-1.10
- Bear: S=1.74

## Negated Direction
Best negated: `rank(-1 * fnd6_newqv1300_txdiq / close)` S=0.91, F=0.61, INFERIOR
Direction gap: +0.29 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fnd6_newqv1300_txdiq)`: S=0.91, F=0.60, T=8.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_txdiq / close)`: S=0.91, F=0.61, T=8.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_txdiq, 5))`: S=-0.50, F=-0.25, T=39.6%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_newqv1300_txdiq, 5))` | TOP200 | 0.61 | 0.71 | 74.4% | 100% | all-weather |
| `rank(ts_delta(fnd6_newqv1300_txdiq, 5))` | TOP3000 | 0.49 | 0.24 | 31.3% | 60% | all-weather |
| `rank(ts_delta(fnd6_newqv1300_txdiq, 5))` | TOP500 | 0.31 | 0.18 | 69.3% | 80% | mixed |

## Correlation Notes
Top correlates:
- fnd6_dc: -0.165 (weakly negatively correlated)
- fnd6_txr: 0.157 (weakly positively correlated)
- snt_buzz_ret_fast_d1: -0.155 (weakly negatively correlated)
- rp_ess_price: -0.153 (weakly negatively correlated)
- fnd6_txpd: 0.149 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
