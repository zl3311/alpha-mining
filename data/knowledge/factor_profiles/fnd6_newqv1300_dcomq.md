---
field: fnd6_newqv1300_dcomq
dataset: fundamental6
best_template: rank_ts_rank
best_sharpe: 0.55
best_fitness: 0.45
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 10
max_drawdown: 0.4271
ann_vol: 0.1624
hit_rate: 0.4769
rolling_sharpe_min: -1.374
rolling_sharpe_max: 3.013
negated_best_sharpe: 0.19
negated_best_template: neg_rank_level
negated_best_fitness: 0.06
n_negated_sims: 10
direction_gap: -0.36
---
# fnd6_newqv1300_dcomq (fundamental6)

*Deferred Compensation*

## Signal Profile
- `rank(fnd6_newqv1300_dcomq)`: S=0.21, F=0.12, T=10.3%, INFERIOR (TOP200)
- `rank(fnd6_newqv1300_dcomq / close)`: S=0.21, F=0.12, T=10.3%, INFERIOR (TOP200)
- `rank(ts_delta(fnd6_newqv1300_dcomq, 5))`: S=0.57, F=0.41, T=18.3%, INFERIOR (TOP500)
- `-rank(fnd6_newqv1300_dcomq)`: S=-0.15, F=-0.05, T=5.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_dcomq, 5))`: S=-0.35, F=-0.16, T=24.1%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_newqv1300_dcomq, 22)`: S=-0.05, F=-0.01, T=2.2%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newqv1300_dcomq, 10)`: S=-0.03, F=0.00, T=3.4%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newqv1300_dcomq, 22))`: S=0.55, F=0.45, T=17.3%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_dcomq)`: S=0.19, F=0.06, T=4.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_dcomq / close)`: S=0.19, F=0.06, T=4.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 17F/15P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 10F/19P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.57, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.82 (negative), ret=-8.1%
  - 2020: S=-0.41 (negative), ret=-8.0%
  - 2021: S=1.39 (moderate), ret=+34.4%
  - 2022: S=1.68 (strong), ret=+14.7%
  - 2023: S=1.36 (moderate), ret=+12.5%

## Risk & Drawdown
- Max drawdown: 42.71% over 414 days (recovered)
- Annualized: return +9.3%, volatility 16.2% (fraction of booksize)
- Hit rate: 47.7% positive days
- Tail shape: skew -2.33, excess kurtosis +67.41

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.37, max 3.01, latest 1.34

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2019
Best month: +22.47%; worst month: -15.30%
Positive months: 48%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.27
- Sideways: S=0.93
- Bear: S=-0.82

## Negated Direction
Best negated: `rank(-1 * fnd6_newqv1300_dcomq)` S=0.19, F=0.06, INFERIOR
Direction gap: -0.36 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_newqv1300_dcomq)`: S=0.19, F=0.06, T=4.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_dcomq / close)`: S=0.19, F=0.06, T=4.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_dcomq, 5))`: S=-0.35, F=-0.16, T=24.1%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_newqv1300_dcomq, 5))` | TOP500 | 0.57 | 0.41 | 42.7% | 60% | bull-only |
| `rank(ts_delta(fnd6_newqv1300_dcomq, 5))` | TOP3000 | 0.61 | 0.38 | 19.0% | 80% | mixed |
| `rank(ts_delta(fnd6_newqv1300_dcomq, 5))` | TOP200 | 0.45 | 0.31 | 27.0% | 60% | bull-only |
| `rank(fnd6_newqv1300_dcomq)` | TOP200 | 0.21 | 0.12 | 53.9% | 40% | weak |
| `rank(fnd6_newqv1300_dcomq / close)` | TOP200 | 0.21 | 0.12 | 53.9% | 40% | weak |
| `rank(fnd6_newqv1300_dcomq)` | TOP500 | 0.19 | 0.09 | 28.1% | 60% | weak |
| `rank(fnd6_newqv1300_dcomq / close)` | TOP500 | 0.19 | 0.09 | 28.1% | 60% | weak |
| `rank(fnd6_newqv1300_dcomq)` | TOP1000 | 0.14 | 0.05 | 35.5% | 60% | bull-only |
| `rank(fnd6_newqv1300_dcomq / close)` | TOP1000 | 0.14 | 0.05 | 35.5% | 60% | bull-only |
| `rank(ts_delta(fnd6_newqv1300_dcomq, 5))` | TOP1000 | 0.12 | 0.03 | 31.1% | 60% | bull-only |

## Correlation Notes
Top correlates:
- cash: 0.353 (weakly positively correlated)
- fnd6_esopnr: 0.349 (weakly positively correlated)
- min_free_cashflow_per_share_guidance: 0.349 (weakly positively correlated)
- shareholders_equity_min_guidance: 0.349 (weakly positively correlated)
- min_total_assets_guidance: 0.349 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
