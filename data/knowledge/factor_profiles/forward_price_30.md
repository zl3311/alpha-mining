---
field: forward_price_30
dataset: option9
cluster: option9_analyst_forecast
coverage: 0.9796
community_alphas: 584
best_template: rank_neg_delta
best_sharpe: 1.34
best_fitness: 0.65
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_FITNESS
n_sims: 21
regime_profile: bull-only
n_variations_with_pnl: 1
max_drawdown: 0.5489
ann_vol: 0.1342
hit_rate: 0.5393
rolling_sharpe_min: -3.346
rolling_sharpe_max: 2.409
negated_best_sharpe: 1.34
negated_best_template: rank_neg_delta
negated_best_fitness: 0.65
n_negated_sims: 4
direction_gap: 0.73
---
# forward_price_30 (option9)

*Synthetic forward price at 30 days expiry, derived from at-the-money call and put options, reflecting market consensus forward expectation*

## Signal Profile
- `rank(forward_price_30)`: S=0.07, F=0.02, T=7.3%, INFERIOR (TOP3000)
- `rank(forward_price_30 / close)`: S=0.31, F=0.09, T=24.1%, INFERIOR (TOP3000)
- `rank(ts_delta(forward_price_30, 5))`: S=-1.02, F=-0.48, T=39.9%, INFERIOR (TOP1000)
- `-rank(forward_price_30)`: S=0.07, F=0.02, T=5.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(forward_price_30, 5))`: S=1.34, F=0.65, T=43.5%, INFERIOR (TOP3000)
- `-ts_zscore(forward_price_30, 63)`: S=0.61, F=0.40, T=16.8%, INFERIOR (TOP3000)
- `ts_mean(forward_price_30, 10)`: S=0.27, F=0.13, T=1.5%, INFERIOR (TOP3000)
- `rank(ts_rank(forward_price_30, 22))`: S=-0.80, F=-0.43, T=28.1%, INFERIOR (TOP3000)
- `rank(-1 * forward_price_30)`: S=-0.07, F=-0.02, T=7.3%, INFERIOR (TOP3000)
- `rank(-1 * forward_price_30 / close)`: S=-0.12, F=-0.02, T=20.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 20F/1P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 20F/1P
- LOW_SUB_UNIVERSE_SHARPE: 12F/7P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.07, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.51 (moderate), ret=+4.0%
  - 2020: S=-1.94 (negative), ret=-24.7%
  - 2021: S=0.50 (moderate), ret=+7.2%
  - 2022: S=1.20 (moderate), ret=+19.8%
  - 2023: S=-0.14 (negative), ret=-1.7%

## Risk & Drawdown
- Max drawdown: 54.89% over 1518 days (recovered)
- Annualized: return +0.9%, volatility 13.4% (fraction of booksize)
- Hit rate: 53.9% positive days
- Tail shape: skew -0.28, excess kurtosis +0.59

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -3.35, max 2.41, latest -0.35

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +9.08%; worst month: -11.00%
Positive months: 49%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=1.51
- Sideways: S=1.02
- Bear: S=-2.47

## Negated Direction
Best negated: `rank(-1 * ts_delta(forward_price_30, 5))` S=1.34, F=0.65, INFERIOR
Direction gap: +0.73 (negated - positive best Sharpe). NEGATION DOMINANT — field is significantly stronger when reversed.

Negated template variants:
- `rank(-1 * forward_price_30)`: S=-0.07, F=-0.02, T=7.3%, INFERIOR (TOP3000)
- `rank(-1 * forward_price_30 / close)`: S=-0.12, F=-0.02, T=20.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(forward_price_30, 5))`: S=1.34, F=0.65, T=43.5%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(forward_price_30)` | TOP3000 | 0.07 | 0.02 | 54.9% | 60% | bull-only |

## Correlation Notes
Top correlates:
- forward_price_20: 1.000 (strongly positively correlated)
- forward_price_10: 1.000 (strongly positively correlated)
- forward_price_60: 1.000 (strongly positively correlated)
- forward_price_90: 1.000 (strongly positively correlated)
- forward_price_120: 1.000 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_FITNESS. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
