---
field: historical_volatility_10
dataset: option8
best_template: ts_zscore
best_sharpe: 0.64
best_fitness: 0.22
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 29
regime_profile: mixed
n_variations_with_pnl: 3
max_drawdown: 0.1297
ann_vol: 0.0573
hit_rate: 0.5247
rolling_sharpe_min: -2.034
rolling_sharpe_max: 3.132
redundancy_cluster: 98
negated_best_sharpe: 0.05
negated_best_template: rank_neg_delta
negated_best_fitness: 0.01
n_negated_sims: 10
direction_gap: -0.59
---
# historical_volatility_10 (option8)

*Historical close-to-close volatility for approximately 10 calendar days*

## Signal Profile
- `rank(historical_volatility_10)`: S=0.10, F=0.03, T=21.1%, INFERIOR (TOP200)
- `rank(historical_volatility_10 / close)`: S=0.06, F=0.02, T=8.9%, INFERIOR (TOP3000)
- `rank(ts_delta(historical_volatility_10, 5))`: S=0.53, F=0.14, T=41.5%, INFERIOR (TOP3000)
- `-rank(historical_volatility_10)`: S=-0.06, F=-0.01, T=19.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(historical_volatility_10, 5))`: S=0.05, F=0.01, T=43.1%, INFERIOR (TOP3000)
- `ts_zscore(historical_volatility_10, 22)`: S=0.64, F=0.22, T=32.0%, INFERIOR (TOP3000)
- `ts_mean(historical_volatility_10, 10)`: S=-0.18, F=-0.11, T=12.0%, INFERIOR (TOP3000)
- `rank(ts_rank(historical_volatility_10, 22))`: S=0.62, F=0.20, T=33.4%, INFERIOR (TOP3000)
- `rank(-1 * historical_volatility_10)`: S=-0.10, F=-0.03, T=21.1%, INFERIOR (TOP3000)
- `rank(-1 * historical_volatility_10 / close)`: S=-0.07, F=-0.02, T=10.0%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 28F/1P
- LOW_FITNESS: 29F/0P
- LOW_SHARPE: 29F/0P
- LOW_SUB_UNIVERSE_SHARPE: 7F/11P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.55, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=1.85 (strong), ret=+5.1%
  - 2020: S=-0.84 (negative), ret=-4.8%
  - 2021: S=2.10 (strong), ret=+11.2%
  - 2022: S=1.10 (moderate), ret=+9.2%
  - 2023: S=-1.20 (negative), ret=-5.4%

## Risk & Drawdown
- Max drawdown: 12.97% over 512 days (not yet recovered, ongoing at window end)
- Annualized: return +3.1%, volatility 5.7% (fraction of booksize)
- Hit rate: 52.5% positive days
- Tail shape: skew +0.36, excess kurtosis +7.73

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.03, max 3.13, latest -1.16

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2023
Best month: +5.38%; worst month: -4.85%
Positive months: 61%

## Regime Profile
Regime profile: **mixed**
- Bull: S=1.07
- Sideways: S=-0.02
- Bear: S=0.43

## Negated Direction
Best negated: `rank(-1 * ts_delta(historical_volatility_10, 5))` S=0.05, F=0.01, INFERIOR
Direction gap: -0.59 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * historical_volatility_10)`: S=-0.10, F=-0.03, T=21.1%, INFERIOR (TOP3000)
- `rank(-1 * historical_volatility_10 / close)`: S=-0.07, F=-0.02, T=10.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(historical_volatility_10, 5))`: S=0.05, F=0.01, T=43.1%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(historical_volatility_10, 5))` | TOP3000 | 0.55 | 0.14 | 13.0% | 60% | mixed |
| `rank(ts_delta(historical_volatility_10, 5))` | TOP1000 | 0.35 | 0.08 | 13.9% | 60% | all-weather |
| `rank(historical_volatility_10)` | TOP200 | 0.10 | 0.03 | 65.2% | 60% | bear-only |

## Correlation Notes
Top correlates:
- parkinson_volatility_10: 0.745 (strongly positively correlated)
- historical_volatility_20: 0.527 (moderately positively correlated)
- parkinson_volatility_20: 0.413 (moderately positively correlated)
- historical_volatility_30: 0.395 (weakly positively correlated)
- rank(fnd6_acdo) * rank(volume/adv20): 0.390 (weakly positively correlated)

Redundancy cluster #98: 2 similar fields, mean |rho| 0.745 (representative). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
