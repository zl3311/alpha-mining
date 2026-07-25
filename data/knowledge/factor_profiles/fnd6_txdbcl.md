---
field: fnd6_txdbcl
dataset: fundamental6
best_template: neg_rank_level
best_sharpe: 0.52
best_fitness: 0.6
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 6
max_drawdown: 0.1513
ann_vol: 0.0862
hit_rate: 0.468
rolling_sharpe_min: -1.554
rolling_sharpe_max: 2.664
negated_best_sharpe: 0.52
negated_best_template: neg_rank_level
negated_best_fitness: 0.6
n_negated_sims: 10
direction_gap: 0.09
---
# fnd6_txdbcl (fundamental6)

*Deferred Tax Liability - Current*

## Signal Profile
- `rank(fnd6_txdbcl)`: S=0.25, F=0.12, T=2.1%, INFERIOR (TOP200)
- `rank(fnd6_txdbcl / close)`: S=0.25, F=0.12, T=2.1%, INFERIOR (TOP200)
- `rank(ts_delta(fnd6_txdbcl, 5))`: S=0.43, F=0.23, T=5.6%, INFERIOR (TOP3000)
- `-rank(fnd6_txdbcl)`: S=0.50, F=0.43, T=3.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_txdbcl, 5))`: S=0.68, F=0.48, T=5.6%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_txdbcl, 63)`: S=0.00, F=0.00, T=0.0%, UNKNOWN (TOP3000)
- `ts_mean(fnd6_txdbcl, 10)`: S=-0.19, F=-0.11, T=1.3%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_txdbcl, 22))`: S=0.25, F=0.12, T=4.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_txdbcl)`: S=0.52, F=0.60, T=2.7%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_txdbcl / close)`: S=0.52, F=0.60, T=2.7%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 32F/0P
- LOW_FITNESS: 30F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 9F/18P
- LOW_TURNOVER: 2F/30P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.42, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.59 (negative), ret=-5.6%
  - 2020: S=-0.45 (negative), ret=-2.2%
  - 2021: S=1.43 (moderate), ret=+18.5%
  - 2022: S=0.34 (weak), ret=+2.8%
  - 2023: S=1.30 (moderate), ret=+4.1%

## Risk & Drawdown
- Max drawdown: 15.13% over 736 days (recovered)
- Annualized: return +3.6%, volatility 8.6% (fraction of booksize)
- Hit rate: 46.8% positive days
- Tail shape: skew +1.04, excess kurtosis +31.64

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.55, max 2.66, latest 0.76

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2019
Best month: +16.57%; worst month: -9.52%
Positive months: 66%

## Regime Profile
Regime profile: **mixed**
- Bull: S=1.58
- Sideways: S=-0.64
- Bear: S=-0.36

## Negated Direction
Best negated: `rank(-1 * fnd6_txdbcl)` S=0.52, F=0.60, INFERIOR
Direction gap: +0.09 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fnd6_txdbcl)`: S=0.52, F=0.60, T=2.7%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_txdbcl / close)`: S=0.52, F=0.60, T=2.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_txdbcl, 5))`: S=0.68, F=0.48, T=5.6%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_txdbcl, 5))` | TOP3000 | 0.42 | 0.23 | 15.1% | 60% | mixed |
| `rank(fnd6_txdbcl)` | TOP200 | 0.24 | 0.12 | 26.9% | 60% | bull-only |
| `rank(fnd6_txdbcl / close)` | TOP200 | 0.24 | 0.12 | 26.9% | 60% | bull-only |
| `rank(ts_delta(fnd6_txdbcl, 5))` | TOP500 | 0.18 | 0.06 | 21.1% | 80% | bull-only |
| `rank(fnd6_txdbcl)` | TOP500 | 0.07 | 0.02 | 49.1% | 60% | mixed |
| `rank(fnd6_txdbcl / close)` | TOP500 | 0.07 | 0.02 | 49.1% | 60% | mixed |

## Correlation Notes
Top correlates:
- fnd6_txdbclq: 0.516 (moderately positively correlated)
- max_adjusted_funds_from_operations_adj_guidance: 0.322 (weakly positively correlated)
- max_custom_eps_guidance: 0.322 (weakly positively correlated)
- goodwill_min_guidance_qtr: 0.322 (weakly positively correlated)
- min_adjusted_funds_from_operations_guidance_2: 0.322 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
