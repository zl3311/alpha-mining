---
field: forward_price_1080
dataset: option9
best_template: rank_neg_delta
best_sharpe: 1.29
best_fitness: 0.6
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_FITNESS
n_sims: 21
regime_profile: bull-only
n_variations_with_pnl: 1
max_drawdown: 0.5444
ann_vol: 0.1332
hit_rate: 0.5401
rolling_sharpe_min: -3.329
rolling_sharpe_max: 2.439
negated_best_sharpe: 1.29
negated_best_template: rank_neg_delta
negated_best_fitness: 0.6
n_negated_sims: 4
direction_gap: 0.67
---
# forward_price_1080 (option9)

*Synthetic forward price at 1080 days derived from at-the-money call and put option prices, reflecting market consensus for the underlying at that tenor*

## Signal Profile
- `rank(forward_price_1080)`: S=0.08, F=0.02, T=7.5%, INFERIOR (TOP3000)
- `rank(forward_price_1080 / close)`: S=0.33, F=0.15, T=15.1%, INFERIOR (TOP3000)
- `rank(ts_delta(forward_price_1080, 5))`: S=-0.97, F=-0.44, T=41.3%, INFERIOR (TOP1000)
- `-rank(forward_price_1080)`: S=0.07, F=0.02, T=5.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(forward_price_1080, 5))`: S=1.29, F=0.60, T=45.2%, INFERIOR (TOP3000)
- `-ts_zscore(forward_price_1080, 63)`: S=0.62, F=0.39, T=17.9%, INFERIOR (TOP3000)
- `ts_mean(forward_price_1080, 10)`: S=0.28, F=0.14, T=1.5%, INFERIOR (TOP3000)
- `rank(ts_rank(forward_price_1080, 22))`: S=-0.79, F=-0.41, T=29.3%, INFERIOR (TOP3000)
- `rank(-1 * forward_price_1080)`: S=-0.08, F=-0.02, T=7.5%, INFERIOR (TOP3000)
- `rank(-1 * forward_price_1080 / close)`: S=-0.26, F=-0.09, T=19.0%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 20F/1P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 20F/1P
- LOW_SUB_UNIVERSE_SHARPE: 12F/7P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.08, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.53 (moderate), ret=+4.2%
  - 2020: S=-1.92 (negative), ret=-24.4%
  - 2021: S=0.51 (moderate), ret=+7.3%
  - 2022: S=1.21 (moderate), ret=+19.6%
  - 2023: S=-0.13 (negative), ret=-1.7%

## Risk & Drawdown
- Max drawdown: 54.44% over 1508 days (recovered)
- Annualized: return +1.0%, volatility 13.3% (fraction of booksize)
- Hit rate: 54.0% positive days
- Tail shape: skew -0.28, excess kurtosis +0.57

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -3.33, max 2.44, latest -0.34

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +9.10%; worst month: -10.94%
Positive months: 49%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=1.50
- Sideways: S=1.02
- Bear: S=-2.44

## Negated Direction
Best negated: `rank(-1 * ts_delta(forward_price_1080, 5))` S=1.29, F=0.60, INFERIOR
Direction gap: +0.67 (negated - positive best Sharpe). NEGATION DOMINANT — field is significantly stronger when reversed.

Negated template variants:
- `rank(-1 * forward_price_1080)`: S=-0.08, F=-0.02, T=7.5%, INFERIOR (TOP3000)
- `rank(-1 * forward_price_1080 / close)`: S=-0.26, F=-0.09, T=19.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(forward_price_1080, 5))`: S=1.29, F=0.60, T=45.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(forward_price_1080)` | TOP3000 | 0.08 | 0.02 | 54.4% | 60% | bull-only |

## Correlation Notes
Top correlates:
- forward_price_720: 1.000 (strongly positively correlated)
- forward_price_360: 1.000 (strongly positively correlated)
- forward_price_270: 1.000 (strongly positively correlated)
- forward_price_180: 1.000 (strongly positively correlated)
- forward_price_150: 1.000 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_FITNESS. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
