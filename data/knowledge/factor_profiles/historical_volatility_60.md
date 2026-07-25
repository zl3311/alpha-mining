---
field: historical_volatility_60
dataset: option8
best_template: rank_delta
best_sharpe: 0.32
best_fitness: 0.08
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 27
regime_profile: mixed
n_variations_with_pnl: 2
max_drawdown: 0.1159
ann_vol: 0.0625
hit_rate: 0.4955
rolling_sharpe_min: -1.606
rolling_sharpe_max: 2.569
negated_best_sharpe: 0.06
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.02
n_negated_sims: 10
direction_gap: -0.26
---
# historical_volatility_60 (option8)

*Historical close-to-close volatility for approximately 60 calendar days*

## Signal Profile
- `rank(historical_volatility_60)`: S=0.09, F=0.03, T=7.0%, INFERIOR (TOP500)
- `rank(historical_volatility_60 / close)`: S=0.02, F=0.00, T=4.1%, INFERIOR (TOP3000)
- `rank(ts_delta(historical_volatility_60, 5))`: S=0.32, F=0.08, T=33.7%, INFERIOR (TOP3000)
- `-rank(historical_volatility_60)`: S=-0.02, F=0.00, T=6.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(historical_volatility_60, 5))`: S=-0.32, F=-0.08, T=33.7%, INFERIOR (TOP3000)
- `ts_zscore(historical_volatility_60, 22)`: S=0.25, F=0.07, T=23.0%, INFERIOR (TOP3000)
- `ts_mean(historical_volatility_60, 10)`: S=-0.19, F=-0.12, T=4.8%, INFERIOR (TOP3000)
- `rank(ts_rank(historical_volatility_60, 22))`: S=0.24, F=0.06, T=25.4%, INFERIOR (TOP3000)
- `rank(-1 * historical_volatility_60)`: S=0.04, F=0.01, T=5.8%, INFERIOR (TOP3000)
- `rank(-1 * historical_volatility_60 / close)`: S=0.06, F=0.02, T=3.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 26F/1P
- LOW_FITNESS: 27F/0P
- LOW_SHARPE: 27F/0P
- LOW_SUB_UNIVERSE_SHARPE: 15F/10P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.31, Consistency 40% positive years (2/5)
Yearly breakdown:
  - 2019: S=-0.01 (negative), ret=-0.0%
  - 2020: S=-0.41 (negative), ret=-3.0%
  - 2021: S=1.79 (strong), ret=+11.1%
  - 2022: S=0.91 (moderate), ret=+6.8%
  - 2023: S=-1.05 (negative), ret=-5.2%

## Risk & Drawdown
- Max drawdown: 11.59% over 654 days (recovered)
- Annualized: return +2.0%, volatility 6.2% (fraction of booksize)
- Hit rate: 49.5% positive days
- Tail shape: skew +0.93, excess kurtosis +9.24

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.61, max 2.57, latest -0.98

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2023
Best month: +4.20%; worst month: -6.20%
Positive months: 52%

## Regime Profile
Regime profile: **mixed**
- Bull: S=1.88
- Sideways: S=-1.15
- Bear: S=-0.06

## Negated Direction
Best negated: `rank(-1 * historical_volatility_60 / close)` S=0.06, F=0.02, INFERIOR
Direction gap: -0.26 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * historical_volatility_60)`: S=0.04, F=0.01, T=5.8%, INFERIOR (TOP3000)
- `rank(-1 * historical_volatility_60 / close)`: S=0.06, F=0.02, T=3.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(historical_volatility_60, 5))`: S=-0.32, F=-0.08, T=33.7%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(historical_volatility_60, 5))` | TOP3000 | 0.31 | 0.08 | 11.6% | 40% | mixed |
| `rank(historical_volatility_60)` | TOP500 | 0.09 | 0.03 | 66.3% | 60% | bear-only |

## Correlation Notes
Top correlates:
- parkinson_volatility_60: 0.862 (strongly positively correlated)
- historical_volatility_10 - historical_volatility_180: 0.617 (moderately positively correlated)
- historical_volatility_90: 0.594 (moderately positively correlated)
- parkinson_volatility_90: 0.551 (moderately positively correlated)
- parkinson_volatility_120: 0.521 (moderately positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
