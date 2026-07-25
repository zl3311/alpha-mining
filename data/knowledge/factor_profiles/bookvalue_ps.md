---
field: bookvalue_ps
dataset: fundamental6
best_template: rank_delta
best_sharpe: 0.72
best_fitness: 0.4
best_universe: TOP1000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 36
regime_profile: all-weather
n_variations_with_pnl: 5
max_drawdown: 0.187
ann_vol: 0.1669
hit_rate: 0.5134
rolling_sharpe_min: -0.445
rolling_sharpe_max: 3.26
negated_best_sharpe: 0.3
negated_best_template: rank_neg_delta
negated_best_fitness: 0.14
n_negated_sims: 10
direction_gap: -0.42
---
# bookvalue_ps (fundamental6)

*Book Value Per Share*

## Signal Profile
- `rank(bookvalue_ps)`: S=0.30, F=0.14, T=1.7%, INFERIOR (TOP3000)
- `rank(bookvalue_ps / close)`: S=0.49, F=0.29, T=2.6%, INFERIOR (TOP3000)
- `rank(ts_delta(bookvalue_ps, 5))`: S=0.72, F=0.40, T=38.7%, INFERIOR (TOP1000)
- `ts_decay_linear(rank(bookvalue_ps), 5)`: S=0.30, F=0.14, T=1.7%, INFERIOR (TOP3000)
- `-rank(bookvalue_ps)`: S=-0.01, F=0.00, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(bookvalue_ps, 5))`: S=0.30, F=0.14, T=32.5%, INFERIOR (TOP3000)
- `-ts_zscore(bookvalue_ps, 63)`: S=0.18, F=0.06, T=21.1%, INFERIOR (TOP3000)
- `ts_mean(bookvalue_ps, 10)`: S=-0.32, F=-0.14, T=1.9%, INFERIOR (TOP3000)
- `rank(ts_rank(bookvalue_ps, 22))`: S=0.25, F=0.09, T=17.8%, INFERIOR (TOP3000)
- `rank(-1 * bookvalue_ps)`: S=0.17, F=0.07, T=3.1%, INFERIOR (TOP3000)
- `rank(-1 * bookvalue_ps / close)`: S=0.26, F=0.13, T=3.7%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 13F/23P
- LOW_FITNESS: 36F/0P
- LOW_SHARPE: 36F/0P
- LOW_SUB_UNIVERSE_SHARPE: 17F/7P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.72, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.40 (weak), ret=+4.9%
  - 2020: S=-0.16 (negative), ret=-2.8%
  - 2021: S=1.29 (moderate), ret=+22.8%
  - 2022: S=2.36 (strong), ret=+37.9%
  - 2023: S=-0.20 (negative), ret=-3.5%

## Risk & Drawdown
- Max drawdown: 18.70% over 441 days (recovered)
- Annualized: return +12.1%, volatility 16.7% (fraction of booksize)
- Hit rate: 51.3% positive days
- Tail shape: skew +0.39, excess kurtosis +8.98

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.45, max 3.26, latest -0.23

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2023
Best month: +16.85%; worst month: -9.50%
Positive months: 54%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=0.63
- Sideways: S=0.60
- Bear: S=0.94

## Negated Direction
Best negated: `rank(-1 * ts_delta(bookvalue_ps, 5))` S=0.30, F=0.14, INFERIOR
Direction gap: -0.42 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * bookvalue_ps)`: S=0.17, F=0.07, T=3.1%, INFERIOR (TOP3000)
- `rank(-1 * bookvalue_ps / close)`: S=0.26, F=0.13, T=3.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(bookvalue_ps, 5))`: S=0.30, F=0.14, T=32.5%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(bookvalue_ps, 5))` | TOP1000 | 0.72 | 0.40 | 18.7% | 60% | all-weather |
| `rank(bookvalue_ps / close)` | TOP3000 | 0.48 | 0.29 | 13.8% | 80% | all-weather |
| `ts_decay_linear(rank(bookvalue_ps), 5)` | TOP3000 | 0.29 | 0.14 | 35.1% | 40% | bull-only |
| `rank(bookvalue_ps)` | TOP3000 | 0.28 | 0.14 | 35.1% | 40% | bull-only |
| `rank(bookvalue_ps / close)` | TOP1000 | 0.24 | 0.11 | 13.6% | 60% | bull-only |

## Correlation Notes
Top correlates:
- parkinson_volatility_20: -0.121 (weakly negatively correlated)
- min_share_count_guidance: 0.114 (weakly positively correlated)
- shares_outstanding_max_guidance: 0.114 (weakly positively correlated)
- min_basic_shares_guidance: 0.114 (weakly positively correlated)
- basic_shares_max_guidance_qtr: 0.114 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: trade_when
