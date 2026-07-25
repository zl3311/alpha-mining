---
field: historical_volatility_30
dataset: option8
best_template: ts_zscore
best_sharpe: 0.53
best_fitness: 0.19
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 27
regime_profile: mixed
n_variations_with_pnl: 4
max_drawdown: 0.1029
ann_vol: 0.0725
hit_rate: 0.4964
rolling_sharpe_min: -1.14
rolling_sharpe_max: 1.451
negated_best_sharpe: 0.06
negated_best_template: neg_rank_level
negated_best_fitness: 0.02
n_negated_sims: 10
direction_gap: -0.47
---
# historical_volatility_30 (option8)

*Historical close-to-close volatility for approximately 30 calendar days*

## Signal Profile
- `rank(historical_volatility_30)`: S=0.11, F=0.05, T=10.5%, INFERIOR (TOP200)
- `rank(historical_volatility_30 / close)`: S=0.04, F=0.01, T=5.0%, INFERIOR (TOP3000)
- `rank(ts_delta(historical_volatility_30, 5))`: S=0.24, F=0.06, T=36.4%, INFERIOR (TOP200)
- `-rank(historical_volatility_30)`: S=-0.02, F=0.00, T=9.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(historical_volatility_30, 5))`: S=-0.23, F=-0.05, T=34.5%, INFERIOR (TOP3000)
- `ts_zscore(historical_volatility_30, 22)`: S=0.53, F=0.19, T=23.8%, INFERIOR (TOP3000)
- `ts_mean(historical_volatility_30, 10)`: S=-0.17, F=-0.10, T=7.0%, INFERIOR (TOP3000)
- `rank(ts_rank(historical_volatility_30, 22))`: S=0.36, F=0.10, T=25.9%, INFERIOR (TOP3000)
- `rank(-1 * historical_volatility_30)`: S=0.06, F=0.02, T=8.5%, INFERIOR (TOP3000)
- `rank(-1 * historical_volatility_30 / close)`: S=0.06, F=0.02, T=4.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 26F/1P
- LOW_FITNESS: 27F/0P
- LOW_SHARPE: 27F/0P
- LOW_SUB_UNIVERSE_SHARPE: 11F/14P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.26, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.68 (moderate), ret=+2.4%
  - 2020: S=-0.71 (negative), ret=-5.0%
  - 2021: S=0.12 (weak), ret=+0.9%
  - 2022: S=0.94 (moderate), ret=+9.8%
  - 2023: S=0.21 (weak), ret=+1.0%

## Risk & Drawdown
- Max drawdown: 10.29% over 475 days (recovered)
- Annualized: return +1.9%, volatility 7.2% (fraction of booksize)
- Hit rate: 49.6% positive days
- Tail shape: skew +0.62, excess kurtosis +7.55

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.14, max 1.45, latest 0.10

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +5.26%; worst month: -4.65%
Positive months: 51%

## Regime Profile
Regime profile: **mixed**
- Bull: S=1.00
- Sideways: S=-0.20
- Bear: S=-0.31

## Negated Direction
Best negated: `rank(-1 * historical_volatility_30)` S=0.06, F=0.02, INFERIOR
Direction gap: -0.47 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * historical_volatility_30)`: S=0.06, F=0.02, T=8.5%, INFERIOR (TOP3000)
- `rank(-1 * historical_volatility_30 / close)`: S=0.06, F=0.02, T=4.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(historical_volatility_30, 5))`: S=-0.23, F=-0.05, T=34.5%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(historical_volatility_30, 5))` | TOP1000 | 0.26 | 0.06 | 10.3% | 80% | mixed |
| `rank(ts_delta(historical_volatility_30, 5))` | TOP200 | 0.23 | 0.06 | 24.0% | 40% | mixed |
| `rank(ts_delta(historical_volatility_30, 5))` | TOP3000 | 0.24 | 0.05 | 14.0% | 40% | mixed |
| `rank(historical_volatility_30)` | TOP200 | 0.12 | 0.05 | 68.5% | 60% | bear-only |

## Correlation Notes
Top correlates:
- historical_volatility_10 - historical_volatility_180: 0.593 (moderately positively correlated)
- historical_volatility_20: 0.556 (moderately positively correlated)
- parkinson_volatility_30: 0.555 (moderately positively correlated)
- historical_volatility_120: 0.541 (moderately positively correlated)
- parkinson_volatility_20: 0.479 (moderately positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
