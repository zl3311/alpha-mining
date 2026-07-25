---
field: fnd6_newqv1300_citotalq
dataset: fundamental6
best_template: rank_neg_delta
best_sharpe: 0.76
best_fitness: 0.27
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 5
max_drawdown: 0.18
ann_vol: 0.1578
hit_rate: 0.5053
rolling_sharpe_min: -0.95
rolling_sharpe_max: 1.534
negated_best_sharpe: 0.76
negated_best_template: rank_neg_delta
negated_best_fitness: 0.27
n_negated_sims: 10
direction_gap: 0.39
---
# fnd6_newqv1300_citotalq (fundamental6)

*Comprehensive Income - Parent*

## Signal Profile
- `rank(fnd6_newqv1300_citotalq)`: S=0.18, F=0.07, T=6.0%, INFERIOR (TOP3000)
- `rank(fnd6_newqv1300_citotalq / close)`: S=0.12, F=0.04, T=6.0%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_newqv1300_citotalq, 5))`: S=0.37, F=0.12, T=56.4%, INFERIOR (TOP500)
- `-rank(fnd6_newqv1300_citotalq)`: S=-0.11, F=-0.04, T=7.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_citotalq, 5))`: S=0.76, F=0.27, T=46.4%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_newqv1300_citotalq, 22)`: S=-0.01, F=0.00, T=42.0%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newqv1300_citotalq, 10)`: S=0.25, F=0.11, T=4.2%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newqv1300_citotalq, 22))`: S=0.35, F=0.11, T=21.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_citotalq)`: S=-0.18, F=-0.07, T=6.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_citotalq / close)`: S=-0.12, F=-0.04, T=6.0%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 10F/22P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 19F/10P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.37, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=-0.08 (negative), ret=-0.9%
  - 2020: S=0.89 (moderate), ret=+15.4%
  - 2021: S=0.07 (weak), ret=+1.3%
  - 2022: S=0.62 (moderate), ret=+11.2%
  - 2023: S=0.13 (weak), ret=+1.6%

## Risk & Drawdown
- Max drawdown: 18.00% over 452 days (not yet recovered, ongoing at window end)
- Annualized: return +5.8%, volatility 15.8% (fraction of booksize)
- Hit rate: 50.5% positive days
- Tail shape: skew +0.41, excess kurtosis +5.84

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.95, max 1.53, latest 0.19

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2019
Best month: +13.68%; worst month: -8.31%
Positive months: 48%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.66
- Sideways: S=0.27
- Bear: S=0.21

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_newqv1300_citotalq, 5))` S=0.76, F=0.27, INFERIOR
Direction gap: +0.39 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fnd6_newqv1300_citotalq)`: S=-0.18, F=-0.07, T=6.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_citotalq / close)`: S=-0.12, F=-0.04, T=6.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_citotalq, 5))`: S=0.76, F=0.27, T=46.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_newqv1300_citotalq, 5))` | TOP500 | 0.37 | 0.12 | 18.0% | 80% | mixed |
| `rank(ts_delta(fnd6_newqv1300_citotalq, 5))` | TOP1000 | 0.30 | 0.08 | 25.9% | 60% | all-weather |
| `rank(fnd6_newqv1300_citotalq)` | TOP3000 | 0.17 | 0.07 | 39.0% | 60% | bull-only |
| `rank(fnd6_newqv1300_citotalq / close)` | TOP3000 | 0.11 | 0.04 | 38.2% | 60% | bull-only |
| `rank(fnd6_newqv1300_citotalq)` | TOP1000 | 0.10 | 0.04 | 41.4% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_newqv1300_ciq: 0.987 (strongly positively correlated)
- fnd6_cptnewqv1300_nopiq: 0.180 (weakly positively correlated)
- historical_volatility_90: -0.115 (weakly negatively correlated)
- fnd6_mrcta: 0.112 (weakly positively correlated)
- anl4_qfd1_az_cfps_number: -0.108 (weakly negatively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
