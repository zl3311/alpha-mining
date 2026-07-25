---
field: historical_volatility_10 - historical_volatility_180
dataset: option8
best_template: rank_level
best_sharpe: 0.4
best_fitness: 0.13
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 3
regime_profile: bull-only
n_variations_with_pnl: 1
max_drawdown: 0.1453
ann_vol: 0.064
hit_rate: 0.5045
rolling_sharpe_min: -1.763
rolling_sharpe_max: 1.862
negated_best_sharpe: -0.04
negated_best_template: neg_rank_level
negated_best_fitness: -0.01
n_negated_sims: 2
direction_gap: -0.44
---
# historical_volatility_10 - historical_volatility_180 (option8)


## Signal Profile
- `rank(historical_volatility_10 - historical_volatility_180)`: S=0.40, F=0.13, T=22.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(historical_volatility_10 - historical_volatility_180, 5))`: S=-0.39, F=-0.09, T=41.4%, INFERIOR (TOP3000)
- `rank(-1 * historical_volatility_10 - historical_volatility_180)`: S=-0.04, F=-0.01, T=11.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 3F/0P
- LOW_FITNESS: 3F/0P
- LOW_SHARPE: 3F/0P
- LOW_SUB_UNIVERSE_SHARPE: 2F/1P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.40, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.72 (moderate), ret=+2.3%
  - 2020: S=-0.79 (negative), ret=-5.3%
  - 2021: S=0.20 (weak), ret=+1.4%
  - 2022: S=1.42 (moderate), ret=+11.7%
  - 2023: S=0.50 (weak), ret=+2.4%

## Risk & Drawdown
- Max drawdown: 14.53% over 1134 days (recovered)
- Annualized: return +2.5%, volatility 6.4% (fraction of booksize)
- Hit rate: 50.4% positive days
- Tail shape: skew +0.43, excess kurtosis +4.28

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.76, max 1.86, latest 0.37

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +3.35%; worst month: -3.22%
Positive months: 54%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.10
- Sideways: S=-0.66
- Bear: S=-0.72

## Negated Direction
Best negated: `rank(-1 * historical_volatility_10 - historical_volatility_180)` S=-0.04, F=-0.01, INFERIOR
Direction gap: -0.44 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * historical_volatility_10 - historical_volatility_180)`: S=-0.04, F=-0.01, T=11.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(historical_volatility_10 - historical_volatility_180, 5))`: S=-0.39, F=-0.09, T=41.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(historical_volatility_10 - historical_volatility_180)` | TOP3000 | 0.40 | 0.13 | 14.5% | 80% | bull-only |

## Correlation Notes
Top correlates:
- historical_volatility_60: 0.617 (moderately positively correlated)
- historical_volatility_90: 0.614 (moderately positively correlated)
- historical_volatility_30: 0.593 (moderately positively correlated)
- parkinson_volatility_60: 0.553 (moderately positively correlated)
- historical_volatility_120: 0.552 (moderately positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, rank_delta, rank_value_norm, trade_when
