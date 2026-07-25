---
field: fnd6_optlife
dataset: fundamental6
best_template: rank_delta
best_sharpe: 0.71
best_fitness: 0.51
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 7
max_drawdown: 0.5394
ann_vol: 0.2703
hit_rate: 0.5053
rolling_sharpe_min: -1.323
rolling_sharpe_max: 2.257
negated_best_sharpe: 0.27
negated_best_template: rank_neg_delta
negated_best_fitness: 0.16
n_negated_sims: 10
direction_gap: -0.44
---
# fnd6_optlife (fundamental6)

*Life of Options - Assumption (# yrs)*

## Signal Profile
- `rank(fnd6_optlife)`: S=0.29, F=0.10, T=2.6%, INFERIOR (TOP1000)
- `rank(fnd6_optlife / close)`: S=0.31, F=0.16, T=3.6%, INFERIOR (TOP500)
- `rank(ts_delta(fnd6_optlife, 5))`: S=0.71, F=0.51, T=37.7%, INFERIOR (TOP3000)
- `-rank(fnd6_optlife)`: S=-0.29, F=-0.10, T=2.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_optlife, 5))`: S=0.27, F=0.16, T=14.0%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_optlife, 63)`: S=0.48, F=0.42, T=10.9%, INFERIOR (TOP3000)
- `ts_mean(fnd6_optlife, 10)`: S=0.22, F=0.07, T=2.2%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_optlife, 22))`: S=0.10, F=0.03, T=21.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_optlife)`: S=0.22, F=0.09, T=3.3%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_optlife / close)`: S=-0.14, F=-0.05, T=3.7%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 12F/8P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.70, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.54 (moderate), ret=+10.8%
  - 2020: S=1.05 (moderate), ret=+33.3%
  - 2021: S=0.03 (weak), ret=+0.9%
  - 2022: S=1.36 (moderate), ret=+36.0%
  - 2023: S=0.59 (moderate), ret=+12.3%

## Risk & Drawdown
- Max drawdown: 53.94% over 459 days (recovered)
- Annualized: return +19.0%, volatility 27.0% (fraction of booksize)
- Hit rate: 50.5% positive days
- Tail shape: skew +2.22, excess kurtosis +29.02

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.32, max 2.26, latest 0.58

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2021
Best month: +21.76%; worst month: -20.10%
Positive months: 66%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.30
- Sideways: S=0.36
- Bear: S=1.24

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_optlife, 5))` S=0.27, F=0.16, INFERIOR
Direction gap: -0.44 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_optlife)`: S=0.22, F=0.09, T=3.3%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_optlife / close)`: S=-0.14, F=-0.05, T=3.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_optlife, 5))`: S=0.27, F=0.16, T=14.0%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_optlife, 5))` | TOP3000 | 0.70 | 0.51 | 53.9% | 100% | mixed |
| `rank(ts_delta(fnd6_optlife, 5))` | TOP1000 | 0.39 | 0.21 | 65.8% | 60% | mixed |
| `rank(fnd6_optlife / close)` | TOP500 | 0.31 | 0.16 | 27.3% | 80% | mixed |
| `rank(fnd6_optlife)` | TOP1000 | 0.31 | 0.10 | 10.6% | 80% | mixed |
| `rank(fnd6_optlife / close)` | TOP1000 | 0.23 | 0.10 | 27.6% | 40% | bear-only |
| `rank(fnd6_optlife)` | TOP500 | 0.20 | 0.07 | 15.5% | 60% | bear-only |
| `rank(fnd6_optlife / close)` | TOP200 | 0.12 | 0.05 | 27.9% | 60% | bear-only |

## Correlation Notes
Top correlates:
- news_max_dn_ret: 0.202 (weakly positively correlated)
- news_close_vol: 0.169 (weakly positively correlated)
- snt_value_fast_d1: 0.137 (weakly positively correlated)
- pretax_income_actual_reported_value: -0.127 (weakly negatively correlated)
- pretax_income_reported_value: -0.127 (weakly negatively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
