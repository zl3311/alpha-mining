---
field: parkinson_volatility_60
dataset: option8
best_template: rank_ts_rank
best_sharpe: 0.43
best_fitness: 0.14
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 27
regime_profile: mixed
n_variations_with_pnl: 3
max_drawdown: 0.1356
ann_vol: 0.0718
hit_rate: 0.5004
rolling_sharpe_min: -1.219
rolling_sharpe_max: 2.731
negated_best_sharpe: 0.18
negated_best_template: rank_neg_delta
negated_best_fitness: 0.05
n_negated_sims: 10
direction_gap: -0.25
---
# parkinson_volatility_60 (option8)

*Historical volatility using the Parkinson high–low estimator over approximately the past 60 calendar days*

## Signal Profile
- `rank(parkinson_volatility_60)`: S=0.14, F=0.07, T=6.0%, INFERIOR (TOP200)
- `rank(parkinson_volatility_60 / close)`: S=0.02, F=0.00, T=3.7%, INFERIOR (TOP3000)
- `rank(ts_delta(parkinson_volatility_60, 5))`: S=0.42, F=0.13, T=30.3%, INFERIOR (TOP3000)
- `-rank(parkinson_volatility_60)`: S=-0.02, F=0.00, T=5.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(parkinson_volatility_60, 5))`: S=0.18, F=0.05, T=32.3%, INFERIOR (TOP3000)
- `ts_zscore(parkinson_volatility_60, 22)`: S=0.35, F=0.12, T=22.4%, INFERIOR (TOP3000)
- `ts_mean(parkinson_volatility_60, 10)`: S=-0.22, F=-0.16, T=3.6%, INFERIOR (TOP3000)
- `rank(ts_rank(parkinson_volatility_60, 22))`: S=0.43, F=0.14, T=25.0%, INFERIOR (TOP3000)
- `rank(-1 * parkinson_volatility_60)`: S=-0.14, F=-0.07, T=6.0%, INFERIOR (TOP3000)
- `rank(-1 * parkinson_volatility_60 / close)`: S=-0.07, F=-0.02, T=4.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 26F/1P
- LOW_FITNESS: 27F/0P
- LOW_SHARPE: 27F/0P
- LOW_SUB_UNIVERSE_SHARPE: 8F/8P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.41, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.16 (negative), ret=-0.6%
  - 2020: S=-0.31 (negative), ret=-2.7%
  - 2021: S=1.52 (strong), ret=+12.0%
  - 2022: S=0.67 (moderate), ret=+5.7%
  - 2023: S=0.04 (weak), ret=+0.2%

## Risk & Drawdown
- Max drawdown: 13.56% over 370 days (recovered)
- Annualized: return +3.0%, volatility 7.2% (fraction of booksize)
- Hit rate: 50.0% positive days
- Tail shape: skew +0.87, excess kurtosis +7.57

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.22, max 2.73, latest 0.21

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2020
Best month: +5.00%; worst month: -5.73%
Positive months: 52%

## Regime Profile
Regime profile: **mixed**
- Bull: S=1.67
- Sideways: S=-0.26
- Bear: S=-0.40

## Negated Direction
Best negated: `rank(-1 * ts_delta(parkinson_volatility_60, 5))` S=0.18, F=0.05, INFERIOR
Direction gap: -0.25 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * parkinson_volatility_60)`: S=-0.14, F=-0.07, T=6.0%, INFERIOR (TOP3000)
- `rank(-1 * parkinson_volatility_60 / close)`: S=-0.07, F=-0.02, T=4.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(parkinson_volatility_60, 5))`: S=0.18, F=0.05, T=32.3%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(parkinson_volatility_60, 5))` | TOP3000 | 0.41 | 0.13 | 13.6% | 60% | mixed |
| `rank(parkinson_volatility_60)` | TOP200 | 0.15 | 0.07 | 69.4% | 60% | bear-only |
| `rank(parkinson_volatility_60)` | TOP500 | 0.13 | 0.05 | 69.2% | 40% | bear-only |

## Correlation Notes
Top correlates:
- historical_volatility_60: 0.862 (strongly positively correlated)
- parkinson_volatility_90: 0.624 (moderately positively correlated)
- parkinson_volatility_120: 0.580 (moderately positively correlated)
- historical_volatility_10 - historical_volatility_180: 0.553 (moderately positively correlated)
- historical_volatility_90: 0.541 (moderately positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
