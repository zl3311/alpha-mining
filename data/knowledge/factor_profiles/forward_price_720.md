---
field: forward_price_720
dataset: option9
best_template: rank_neg_delta
best_sharpe: 1.3
best_fitness: 0.6
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_FITNESS
n_sims: 21
regime_profile: bull-only
n_variations_with_pnl: 1
max_drawdown: 0.5448
ann_vol: 0.1333
hit_rate: 0.5409
rolling_sharpe_min: -3.331
rolling_sharpe_max: 2.437
negated_best_sharpe: 1.3
negated_best_template: rank_neg_delta
negated_best_fitness: 0.6
n_negated_sims: 4
direction_gap: 0.68
---
# forward_price_720 (option9)

*Synthetic forward price at 720 days derived from at-the-money call and put options reflecting the market's forward expectation of the underlying security*

## Signal Profile
- `rank(forward_price_720)`: S=0.08, F=0.02, T=7.4%, INFERIOR (TOP3000)
- `rank(forward_price_720 / close)`: S=0.32, F=0.15, T=15.1%, INFERIOR (TOP3000)
- `rank(ts_delta(forward_price_720, 5))`: S=-0.98, F=-0.44, T=41.2%, INFERIOR (TOP1000)
- `-rank(forward_price_720)`: S=0.07, F=0.02, T=5.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(forward_price_720, 5))`: S=1.30, F=0.60, T=45.1%, INFERIOR (TOP3000)
- `-ts_zscore(forward_price_720, 63)`: S=0.62, F=0.39, T=17.8%, INFERIOR (TOP3000)
- `ts_mean(forward_price_720, 10)`: S=0.27, F=0.13, T=1.5%, INFERIOR (TOP3000)
- `rank(ts_rank(forward_price_720, 22))`: S=-0.80, F=-0.41, T=29.2%, INFERIOR (TOP3000)
- `rank(-1 * forward_price_720)`: S=-0.08, F=-0.02, T=7.4%, INFERIOR (TOP3000)
- `rank(-1 * forward_price_720 / close)`: S=-0.26, F=-0.09, T=19.0%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 20F/1P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 20F/1P
- LOW_SUB_UNIVERSE_SHARPE: 12F/7P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.08, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.53 (moderate), ret=+4.2%
  - 2020: S=-1.92 (negative), ret=-24.5%
  - 2021: S=0.51 (moderate), ret=+7.2%
  - 2022: S=1.22 (moderate), ret=+19.7%
  - 2023: S=-0.13 (negative), ret=-1.6%

## Risk & Drawdown
- Max drawdown: 54.48% over 1508 days (recovered)
- Annualized: return +1.0%, volatility 13.3% (fraction of booksize)
- Hit rate: 54.1% positive days
- Tail shape: skew -0.28, excess kurtosis +0.57

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -3.33, max 2.44, latest -0.34

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +9.10%; worst month: -10.96%
Positive months: 49%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=1.51
- Sideways: S=1.02
- Bear: S=-2.44

## Negated Direction
Best negated: `rank(-1 * ts_delta(forward_price_720, 5))` S=1.30, F=0.60, INFERIOR
Direction gap: +0.68 (negated - positive best Sharpe). NEGATION DOMINANT — field is significantly stronger when reversed.

Negated template variants:
- `rank(-1 * forward_price_720)`: S=-0.08, F=-0.02, T=7.4%, INFERIOR (TOP3000)
- `rank(-1 * forward_price_720 / close)`: S=-0.26, F=-0.09, T=19.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(forward_price_720, 5))`: S=1.30, F=0.60, T=45.1%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(forward_price_720)` | TOP3000 | 0.08 | 0.02 | 54.5% | 60% | bull-only |

## Correlation Notes
Top correlates:
- forward_price_1080: 1.000 (strongly positively correlated)
- forward_price_360: 1.000 (strongly positively correlated)
- forward_price_270: 1.000 (strongly positively correlated)
- forward_price_180: 1.000 (strongly positively correlated)
- forward_price_150: 1.000 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_FITNESS. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
