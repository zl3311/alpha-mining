---
field: fnd6_optdrq
dataset: fundamental6
best_template: neg_rank_level
best_sharpe: 0.56
best_fitness: 0.54
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 4
max_drawdown: 0.4498
ann_vol: 0.2141
hit_rate: 0.498
rolling_sharpe_min: -1.672
rolling_sharpe_max: 3.211
negated_best_sharpe: 0.56
negated_best_template: neg_rank_level
negated_best_fitness: 0.54
n_negated_sims: 10
direction_gap: 0.0
---
# fnd6_optdrq (fundamental6)

*Dividend Rate - Assumption (%)*

## Signal Profile
- `rank(fnd6_optdrq)`: S=0.20, F=0.10, T=9.2%, INFERIOR (TOP3000)
- `rank(fnd6_optdrq / close)`: S=0.20, F=0.10, T=9.1%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_optdrq, 5))`: S=0.56, F=0.29, T=45.5%, INFERIOR (TOP3000)
- `-rank(fnd6_optdrq)`: S=-0.01, F=0.00, T=10.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_optdrq, 5))`: S=0.11, F=0.03, T=34.9%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_optdrq, 22)`: S=0.41, F=0.26, T=7.2%, INFERIOR (TOP3000)
- `ts_mean(fnd6_optdrq, 10)`: S=0.09, F=0.03, T=6.7%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_optdrq, 22))`: S=-0.11, F=-0.03, T=28.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_optdrq)`: S=0.56, F=0.54, T=12.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_optdrq / close)`: S=0.54, F=0.51, T=12.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 22F/10P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/16P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.55, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.99 (moderate), ret=+20.9%
  - 2020: S=0.99 (moderate), ret=+26.5%
  - 2021: S=2.75 (strong), ret=+44.2%
  - 2022: S=-1.05 (negative), ret=-23.3%
  - 2023: S=-0.65 (negative), ret=-10.5%

## Risk & Drawdown
- Max drawdown: 44.98% over 640 days (not yet recovered, ongoing at window end)
- Annualized: return +11.8%, volatility 21.4% (fraction of booksize)
- Hit rate: 49.8% positive days
- Tail shape: skew +0.32, excess kurtosis +8.22

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.67, max 3.21, latest -0.74

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2022
Best month: +25.11%; worst month: -19.43%
Positive months: 56%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.11
- Sideways: S=-0.43
- Bear: S=1.93

## Negated Direction
Best negated: `rank(-1 * fnd6_optdrq)` S=0.56, F=0.54, INFERIOR
Direction gap: +0.00 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_optdrq)`: S=0.56, F=0.54, T=12.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_optdrq / close)`: S=0.54, F=0.51, T=12.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_optdrq, 5))`: S=0.11, F=0.03, T=34.9%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_optdrq, 5))` | TOP3000 | 0.55 | 0.29 | 45.0% | 60% | mixed |
| `rank(ts_delta(fnd6_optdrq, 5))` | TOP1000 | 0.53 | 0.28 | 31.5% | 60% | mixed |
| `rank(fnd6_optdrq)` | TOP3000 | 0.20 | 0.10 | 51.5% | 60% | bull-only |
| `rank(fnd6_optdrq / close)` | TOP3000 | 0.20 | 0.10 | 49.1% | 60% | bull-only |

## Correlation Notes
Top correlates:
- implied_volatility_call_10: -0.100 (weakly negatively correlated)
- fnd6_txr: -0.099 (weakly negatively correlated)
- fnd6_txpd: -0.093 (weakly negatively correlated)
- fnd6_newqv1300_aul3q: 0.092 (weakly positively correlated)
- implied_volatility_mean_10: -0.091 (weakly negatively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
