---
field: fnd6_newqv1300_optfvgrq
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 0.79
best_fitness: 0.89
best_universe: TOP200
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: all-weather
n_variations_with_pnl: 6
max_drawdown: 0.4528
ann_vol: 0.2384
hit_rate: 0.5061
rolling_sharpe_min: -0.578
rolling_sharpe_max: 1.949
negated_best_sharpe: -0.03
negated_best_template: neg_rank
negated_best_fitness: -0.01
n_negated_sims: 10
direction_gap: -0.82
---
# fnd6_newqv1300_optfvgrq (fundamental6)

*Options - Fair Value of Options Granted*

## Signal Profile
- `rank(fnd6_newqv1300_optfvgrq)`: S=0.37, F=0.23, T=7.0%, INFERIOR (TOP3000)
- `rank(fnd6_newqv1300_optfvgrq / close)`: S=0.79, F=0.89, T=14.8%, INFERIOR (TOP200)
- `rank(ts_delta(fnd6_newqv1300_optfvgrq, 5))`: S=-0.08, F=-0.02, T=29.6%, INFERIOR (TOP200)
- `-rank(fnd6_newqv1300_optfvgrq)`: S=-0.03, F=-0.01, T=9.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_optfvgrq, 5))`: S=-0.33, F=-0.16, T=55.0%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_newqv1300_optfvgrq, 22)`: S=0.12, F=0.04, T=26.1%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newqv1300_optfvgrq, 10)`: S=-0.10, F=-0.03, T=6.1%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newqv1300_optfvgrq, 22))`: S=0.34, F=0.18, T=26.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_optfvgrq)`: S=-0.34, F=-0.22, T=11.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_optfvgrq / close)`: S=-0.34, F=-0.24, T=13.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 14F/18P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 11F/18P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.80, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.98 (moderate), ret=+16.4%
  - 2020: S=-0.04 (negative), ret=-1.0%
  - 2021: S=1.39 (moderate), ret=+40.0%
  - 2022: S=0.76 (moderate), ret=+17.6%
  - 2023: S=1.12 (moderate), ret=+20.0%

## Risk & Drawdown
- Max drawdown: 45.28% over 396 days (recovered)
- Annualized: return +19.0%, volatility 23.8% (fraction of booksize)
- Hit rate: 50.6% positive days
- Tail shape: skew +1.00, excess kurtosis +6.42

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.58, max 1.95, latest 1.16

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2020
Best month: +18.66%; worst month: -16.18%
Positive months: 64%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=0.85
- Sideways: S=-0.57
- Bear: S=1.93

## Negated Direction
Best negated: `-rank(fnd6_newqv1300_optfvgrq)` S=-0.03, F=-0.01, INFERIOR
Direction gap: -0.82 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_newqv1300_optfvgrq)`: S=-0.34, F=-0.22, T=11.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_optfvgrq / close)`: S=-0.34, F=-0.24, T=13.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_optfvgrq, 5))`: S=-0.33, F=-0.16, T=55.0%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newqv1300_optfvgrq / close)` | TOP200 | 0.80 | 0.89 | 45.3% | 80% | all-weather |
| `rank(fnd6_newqv1300_optfvgrq / close)` | TOP500 | 0.34 | 0.24 | 30.8% | 60% | mixed |
| `rank(fnd6_newqv1300_optfvgrq)` | TOP3000 | 0.37 | 0.23 | 42.3% | 60% | bull-only |
| `rank(fnd6_newqv1300_optfvgrq)` | TOP500 | 0.35 | 0.22 | 28.3% | 60% | mixed |
| `rank(fnd6_newqv1300_optfvgrq)` | TOP200 | 0.10 | 0.03 | 42.4% | 60% | weak |
| `rank(fnd6_newqv1300_optfvgrq / close)` | TOP1000 | 0.10 | 0.03 | 36.7% | 40% | bear-only |

## Correlation Notes
Top correlates:
- fnd6_optfvgr: 0.287 (weakly positively correlated)
- fnd6_prch: 0.259 (weakly positively correlated)
- fnd6_prchq: 0.259 (weakly positively correlated)
- systematic_risk_last_90_days: 0.249 (weakly positively correlated)
- beta_last_90_days_spy: 0.249 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
