---
field: parkinson_volatility_30
dataset: option8
best_template: rank_delta
best_sharpe: 0.52
best_fitness: 0.22
best_universe: TOP200
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 27
regime_profile: mixed
n_variations_with_pnl: 6
max_drawdown: 0.1693
ann_vol: 0.1203
hit_rate: 0.5182
rolling_sharpe_min: -1.021
rolling_sharpe_max: 2.093
negated_best_sharpe: 0.07
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.02
n_negated_sims: 10
direction_gap: -0.45
---
# parkinson_volatility_30 (option8)

*Historical volatility using the Parkinson high–low estimator over approximately the past 30 calendar days*

## Signal Profile
- `rank(parkinson_volatility_30)`: S=0.23, F=0.15, T=7.9%, INFERIOR (TOP200)
- `rank(parkinson_volatility_30 / close)`: S=0.04, F=0.01, T=4.1%, INFERIOR (TOP3000)
- `rank(ts_delta(parkinson_volatility_30, 5))`: S=0.52, F=0.22, T=33.7%, INFERIOR (TOP200)
- `-rank(parkinson_volatility_30)`: S=-0.05, F=-0.01, T=6.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(parkinson_volatility_30, 5))`: S=-0.37, F=-0.10, T=31.4%, INFERIOR (TOP3000)
- `ts_zscore(parkinson_volatility_30, 22)`: S=0.25, F=0.07, T=23.3%, INFERIOR (TOP3000)
- `ts_mean(parkinson_volatility_30, 10)`: S=-0.18, F=-0.11, T=4.9%, INFERIOR (TOP3000)
- `rank(ts_rank(parkinson_volatility_30, 22))`: S=0.46, F=0.15, T=25.7%, INFERIOR (TOP3000)
- `rank(-1 * parkinson_volatility_30)`: S=0.05, F=0.01, T=6.0%, INFERIOR (TOP3000)
- `rank(-1 * parkinson_volatility_30 / close)`: S=0.07, F=0.02, T=3.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 26F/1P
- LOW_FITNESS: 27F/0P
- LOW_SHARPE: 27F/0P
- LOW_SUB_UNIVERSE_SHARPE: 11F/14P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.50, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=1.52 (strong), ret=+9.0%
  - 2020: S=0.35 (weak), ret=+3.7%
  - 2021: S=-0.41 (negative), ret=-5.6%
  - 2022: S=1.58 (strong), ret=+28.0%
  - 2023: S=-0.80 (negative), ret=-5.4%

## Risk & Drawdown
- Max drawdown: 16.93% over 163 days (recovered)
- Annualized: return +6.1%, volatility 12.0% (fraction of booksize)
- Hit rate: 51.8% positive days
- Tail shape: skew +0.81, excess kurtosis +8.05

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.02, max 2.09, latest -0.77

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2023
Best month: +10.18%; worst month: -7.47%
Positive months: 54%

## Regime Profile
Regime profile: **mixed**
- Bull: S=1.19
- Sideways: S=0.53
- Bear: S=-0.44

## Negated Direction
Best negated: `rank(-1 * parkinson_volatility_30 / close)` S=0.07, F=0.02, INFERIOR
Direction gap: -0.45 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * parkinson_volatility_30)`: S=0.05, F=0.01, T=6.0%, INFERIOR (TOP3000)
- `rank(-1 * parkinson_volatility_30 / close)`: S=0.07, F=0.02, T=3.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(parkinson_volatility_30, 5))`: S=-0.37, F=-0.10, T=31.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(parkinson_volatility_30, 5))` | TOP200 | 0.50 | 0.22 | 16.9% | 60% | mixed |
| `rank(ts_delta(parkinson_volatility_30, 5))` | TOP1000 | 0.55 | 0.21 | 8.2% | 100% | bull-only |
| `rank(parkinson_volatility_30)` | TOP200 | 0.23 | 0.15 | 73.4% | 60% | bear-only |
| `rank(ts_delta(parkinson_volatility_30, 5))` | TOP500 | 0.43 | 0.14 | 16.4% | 80% | bull-only |
| `rank(ts_delta(parkinson_volatility_30, 5))` | TOP3000 | 0.36 | 0.10 | 15.5% | 40% | bull-only |
| `rank(parkinson_volatility_30)` | TOP500 | 0.12 | 0.05 | 75.8% | 60% | bear-only |

## Correlation Notes
Top correlates:
- historical_volatility_30: 0.555 (moderately positively correlated)
- parkinson_volatility_20: 0.458 (moderately positively correlated)
- historical_volatility_20: 0.370 (weakly positively correlated)
- historical_volatility_120: 0.362 (weakly positively correlated)
- parkinson_volatility_120: 0.334 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
