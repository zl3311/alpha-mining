---
field: historical_volatility_20
dataset: option8
best_template: rank_delta
best_sharpe: 0.73
best_fitness: 0.25
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 27
regime_profile: all-weather
n_variations_with_pnl: 6
max_drawdown: 0.1125
ann_vol: 0.0562
hit_rate: 0.5198
rolling_sharpe_min: -2.248
rolling_sharpe_max: 2.875
negated_best_sharpe: 0.06
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.02
n_negated_sims: 10
direction_gap: -0.67
---
# historical_volatility_20 (option8)

*Historical close-to-close volatility for approximately 20 calendar days*

## Signal Profile
- `rank(historical_volatility_20)`: S=0.15, F=0.07, T=13.4%, INFERIOR (TOP200)
- `rank(historical_volatility_20 / close)`: S=0.05, F=0.01, T=6.0%, INFERIOR (TOP3000)
- `rank(ts_delta(historical_volatility_20, 5))`: S=0.73, F=0.25, T=35.0%, INFERIOR (TOP3000)
- `-rank(historical_volatility_20)`: S=-0.04, F=-0.01, T=12.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(historical_volatility_20, 5))`: S=-0.73, F=-0.25, T=35.0%, INFERIOR (TOP3000)
- `ts_zscore(historical_volatility_20, 22)`: S=0.60, F=0.22, T=24.9%, INFERIOR (TOP3000)
- `ts_mean(historical_volatility_20, 10)`: S=-0.17, F=-0.10, T=9.1%, INFERIOR (TOP3000)
- `rank(ts_rank(historical_volatility_20, 22))`: S=0.53, F=0.17, T=26.9%, INFERIOR (TOP3000)
- `rank(-1 * historical_volatility_20)`: S=0.05, F=0.01, T=11.2%, INFERIOR (TOP3000)
- `rank(-1 * historical_volatility_20 / close)`: S=0.06, F=0.02, T=5.0%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 26F/1P
- LOW_FITNESS: 27F/0P
- LOW_SHARPE: 27F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/11P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.74, Consistency 40% positive years (2/5)
Yearly breakdown:
  - 2019: S=-0.48 (negative), ret=-1.4%
  - 2020: S=-0.06 (negative), ret=-0.3%
  - 2021: S=1.39 (moderate), ret=+6.8%
  - 2022: S=1.87 (strong), ret=+15.7%
  - 2023: S=-0.08 (negative), ret=-0.3%

## Risk & Drawdown
- Max drawdown: 11.25% over 861 days (recovered)
- Annualized: return +4.2%, volatility 5.6% (fraction of booksize)
- Hit rate: 52.0% positive days
- Tail shape: skew +0.59, excess kurtosis +8.97

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.25, max 2.88, latest -0.13

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2019
Best month: +6.33%; worst month: -4.98%
Positive months: 54%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=1.37
- Sideways: S=-0.11
- Bear: S=0.74

## Negated Direction
Best negated: `rank(-1 * historical_volatility_20 / close)` S=0.06, F=0.02, INFERIOR
Direction gap: -0.67 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * historical_volatility_20)`: S=0.05, F=0.01, T=11.2%, INFERIOR (TOP3000)
- `rank(-1 * historical_volatility_20 / close)`: S=0.06, F=0.02, T=5.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(historical_volatility_20, 5))`: S=-0.73, F=-0.25, T=35.0%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(historical_volatility_20, 5))` | TOP3000 | 0.74 | 0.25 | 11.2% | 40% | all-weather |
| `rank(ts_delta(historical_volatility_20, 5))` | TOP200 | 0.41 | 0.15 | 20.6% | 40% | mixed |
| `rank(ts_delta(historical_volatility_20, 5))` | TOP1000 | 0.49 | 0.15 | 10.5% | 80% | mixed |
| `rank(ts_delta(historical_volatility_20, 5))` | TOP500 | 0.41 | 0.12 | 16.4% | 40% | mixed |
| `rank(historical_volatility_20)` | TOP200 | 0.16 | 0.07 | 65.0% | 60% | bear-only |
| `rank(historical_volatility_20)` | TOP500 | 0.08 | 0.02 | 70.1% | 60% | bear-only |

## Correlation Notes
Top correlates:
- parkinson_volatility_20: 0.788 (strongly positively correlated)
- historical_volatility_30: 0.556 (moderately positively correlated)
- historical_volatility_10 - historical_volatility_180: 0.534 (moderately positively correlated)
- historical_volatility_10: 0.527 (moderately positively correlated)
- parkinson_volatility_10: 0.427 (moderately positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
