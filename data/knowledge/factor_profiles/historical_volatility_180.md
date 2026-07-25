---
field: historical_volatility_180
dataset: option8
cluster: option8_volatility_historical
coverage: 0.9796
community_alphas: 4458
best_template: ts_zscore
best_sharpe: 0.61
best_fitness: 0.25
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 29
regime_profile: bear-only
n_variations_with_pnl: 6
max_drawdown: 0.5806
ann_vol: 0.2078
hit_rate: 0.5012
rolling_sharpe_min: -1.775
rolling_sharpe_max: 3.306
negated_best_sharpe: 0.21
negated_best_template: rank_neg_delta
negated_best_fitness: 0.05
n_negated_sims: 10
direction_gap: -0.4
---
# historical_volatility_180 (option8)

*Historical close-to-close volatility for approximately 180 calendar days*

## Signal Profile
- `rank(historical_volatility_180)`: S=0.30, F=0.21, T=5.0%, INFERIOR (TOP200)
- `rank(historical_volatility_180 / close)`: S=0.09, F=0.03, T=3.6%, INFERIOR (TOP3000)
- `rank(ts_delta(historical_volatility_180, 5))`: S=0.40, F=0.12, T=32.4%, INFERIOR (TOP3000)
- `-rank(historical_volatility_180)`: S=-0.13, F=-0.06, T=4.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(historical_volatility_180, 5))`: S=0.21, F=0.05, T=34.2%, INFERIOR (TOP3000)
- `ts_zscore(historical_volatility_180, 22)`: S=0.61, F=0.25, T=23.7%, INFERIOR (TOP3000)
- `ts_mean(historical_volatility_180, 10)`: S=-0.03, F=-0.01, T=3.0%, INFERIOR (TOP3000)
- `rank(ts_rank(historical_volatility_180, 22))`: S=0.36, F=0.10, T=26.1%, INFERIOR (TOP3000)
- `rank(-1 * historical_volatility_180)`: S=-0.29, F=-0.19, T=4.6%, INFERIOR (TOP3000)
- `rank(-1 * historical_volatility_180 / close)`: S=-0.21, F=-0.10, T=3.9%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 28F/1P
- LOW_FITNESS: 29F/0P
- LOW_SHARPE: 29F/0P
- LOW_SUB_UNIVERSE_SHARPE: 15F/12P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.31, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=1.38 (moderate), ret=+14.7%
  - 2020: S=2.69 (strong), ret=+42.6%
  - 2021: S=-0.53 (negative), ret=-13.2%
  - 2022: S=-0.88 (negative), ret=-25.8%
  - 2023: S=0.87 (moderate), ret=+13.0%

## Risk & Drawdown
- Max drawdown: 58.06% over 1043 days (not yet recovered, ongoing at window end)
- Annualized: return +6.4%, volatility 20.8% (fraction of booksize)
- Hit rate: 50.1% positive days
- Tail shape: skew +0.41, excess kurtosis +2.43

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.77, max 3.31, latest 0.96

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2022
Best month: +12.54%; worst month: -12.75%
Positive months: 56%

## Regime Profile
Regime profile: **bear-only**
- Bull: S=-1.53
- Sideways: S=0.26
- Bear: S=2.99

## Negated Direction
Best negated: `rank(-1 * ts_delta(historical_volatility_180, 5))` S=0.21, F=0.05, INFERIOR
Direction gap: -0.40 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * historical_volatility_180)`: S=-0.29, F=-0.19, T=4.6%, INFERIOR (TOP3000)
- `rank(-1 * historical_volatility_180 / close)`: S=-0.21, F=-0.10, T=3.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(historical_volatility_180, 5))`: S=0.21, F=0.05, T=34.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(historical_volatility_180)` | TOP200 | 0.31 | 0.21 | 58.1% | 60% | bear-only |
| `rank(historical_volatility_180)` | TOP500 | 0.30 | 0.19 | 58.5% | 60% | bear-only |
| `rank(ts_delta(historical_volatility_180, 5))` | TOP3000 | 0.39 | 0.12 | 7.1% | 100% | mixed |
| `rank(ts_delta(historical_volatility_180, 5))` | TOP1000 | 0.27 | 0.07 | 17.3% | 60% | mixed |
| `rank(historical_volatility_180)` | TOP1000 | 0.13 | 0.06 | 58.9% | 60% | bear-only |
| `rank(historical_volatility_180)` | TOP3000 | 0.09 | 0.03 | 67.0% | 60% | bear-only |

## Correlation Notes
Top correlates:
- historical_volatility_150: 0.994 (strongly positively correlated)
- parkinson_volatility_180: 0.992 (strongly positively correlated)
- parkinson_volatility_150: 0.986 (strongly positively correlated)
- fn_comp_fair_value_assumptions_weighted_avg_vol_rate_a: 0.856 (strongly positively correlated)
- unsystematic_risk_last_30_days: 0.842 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
