---
field: parkinson_volatility_20
dataset: option8
best_template: rank_ts_rank
best_sharpe: 0.53
best_fitness: 0.18
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 27
regime_profile: mixed
n_variations_with_pnl: 5
max_drawdown: 0.1478
ann_vol: 0.0649
hit_rate: 0.5004
rolling_sharpe_min: -2.369
rolling_sharpe_max: 2.502
negated_best_sharpe: 0.07
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.02
n_negated_sims: 10
direction_gap: -0.46
---
# parkinson_volatility_20 (option8)

*Historical volatility using the Parkinson high–low estimator over approximately the past 20 calendar days*

## Signal Profile
- `rank(parkinson_volatility_20)`: S=0.18, F=0.10, T=9.7%, INFERIOR (TOP200)
- `rank(parkinson_volatility_20 / close)`: S=0.04, F=0.01, T=4.5%, INFERIOR (TOP3000)
- `rank(ts_delta(parkinson_volatility_20, 5))`: S=0.48, F=0.15, T=32.1%, INFERIOR (TOP3000)
- `-rank(parkinson_volatility_20)`: S=-0.05, F=-0.01, T=8.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(parkinson_volatility_20, 5))`: S=-0.48, F=-0.15, T=32.1%, INFERIOR (TOP3000)
- `ts_zscore(parkinson_volatility_20, 22)`: S=0.43, F=0.14, T=24.3%, INFERIOR (TOP3000)
- `ts_mean(parkinson_volatility_20, 10)`: S=-0.18, F=-0.11, T=6.2%, INFERIOR (TOP3000)
- `rank(ts_rank(parkinson_volatility_20, 22))`: S=0.53, F=0.18, T=26.4%, INFERIOR (TOP3000)
- `rank(-1 * parkinson_volatility_20)`: S=0.07, F=0.02, T=7.6%, INFERIOR (TOP3000)
- `rank(-1 * parkinson_volatility_20 / close)`: S=0.07, F=0.02, T=3.8%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 26F/1P
- LOW_FITNESS: 27F/0P
- LOW_SHARPE: 27F/0P
- LOW_SUB_UNIVERSE_SHARPE: 15F/10P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.47, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-1.09 (negative), ret=-3.2%
  - 2020: S=-0.68 (negative), ret=-4.1%
  - 2021: S=1.42 (moderate), ret=+9.3%
  - 2022: S=0.98 (moderate), ret=+9.5%
  - 2023: S=0.78 (moderate), ret=+3.6%

## Risk & Drawdown
- Max drawdown: 14.78% over 861 days (recovered)
- Annualized: return +3.1%, volatility 6.5% (fraction of booksize)
- Hit rate: 50.0% positive days
- Tail shape: skew +0.70, excess kurtosis +10.78

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.37, max 2.50, latest 0.76

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2019
Best month: +4.22%; worst month: -5.16%
Positive months: 59%

## Regime Profile
Regime profile: **mixed**
- Bull: S=1.14
- Sideways: S=0.17
- Bear: S=-0.07

## Negated Direction
Best negated: `rank(-1 * parkinson_volatility_20 / close)` S=0.07, F=0.02, INFERIOR
Direction gap: -0.46 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * parkinson_volatility_20)`: S=0.07, F=0.02, T=7.6%, INFERIOR (TOP3000)
- `rank(-1 * parkinson_volatility_20 / close)`: S=0.07, F=0.02, T=3.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(parkinson_volatility_20, 5))`: S=-0.48, F=-0.15, T=32.1%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(parkinson_volatility_20, 5))` | TOP3000 | 0.47 | 0.15 | 14.8% | 60% | mixed |
| `rank(parkinson_volatility_20)` | TOP200 | 0.18 | 0.10 | 74.5% | 60% | bear-only |
| `rank(ts_delta(parkinson_volatility_20, 5))` | TOP1000 | 0.25 | 0.06 | 14.1% | 60% | mixed |
| `rank(parkinson_volatility_20)` | TOP500 | 0.14 | 0.06 | 74.3% | 60% | bear-only |
| `rank(ts_delta(parkinson_volatility_20, 5))` | TOP200 | 0.20 | 0.06 | 21.5% | 60% | bull-only |

## Correlation Notes
Top correlates:
- historical_volatility_20: 0.788 (strongly positively correlated)
- parkinson_volatility_10: 0.552 (moderately positively correlated)
- historical_volatility_30: 0.479 (moderately positively correlated)
- parkinson_volatility_30: 0.458 (moderately positively correlated)
- historical_volatility_10 - historical_volatility_180: 0.423 (moderately positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
