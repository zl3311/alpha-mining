---
field: high
dataset: pv1
best_template: rank_neg_delta
best_sharpe: 1.32
best_fitness: 0.72
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_FITNESS
n_sims: 21
regime_profile: bull-only
n_variations_with_pnl: 1
max_drawdown: 0.5291
ann_vol: 0.1286
hit_rate: 0.532
rolling_sharpe_min: -3.443
rolling_sharpe_max: 2.402
negated_best_sharpe: 1.32
negated_best_template: rank_neg_delta
negated_best_fitness: 0.72
n_negated_sims: 4
direction_gap: 0.7
---
# high (pv1)

*Daily high price*

## Signal Profile
- `rank(high)`: S=0.08, F=0.02, T=1.6%, INFERIOR (TOP3000)
- `rank(high / close)`: S=0.39, F=0.16, T=45.5%, INFERIOR (TOP3000)
- `rank(ts_delta(high, 5))`: S=-1.00, F=-0.52, T=35.7%, INFERIOR (TOP500)
- `-rank(high)`: S=0.05, F=0.01, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(high, 5))`: S=1.32, F=0.72, T=34.8%, INFERIOR (TOP3000)
- `-ts_zscore(high, 63)`: S=0.62, F=0.46, T=13.1%, INFERIOR (TOP3000)
- `ts_mean(high, 10)`: S=-0.07, F=-0.02, T=1.0%, INFERIOR (TOP3000)
- `rank(ts_rank(high, 22))`: S=-0.81, F=-0.47, T=24.2%, INFERIOR (TOP3000)
- `rank(-1 * high)`: S=-0.08, F=-0.02, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * high / close)`: S=-0.39, F=-0.16, T=43.5%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 1F/20P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 20F/1P
- LOW_SUB_UNIVERSE_SHARPE: 13F/6P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.08, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.61 (moderate), ret=+4.6%
  - 2020: S=-2.04 (negative), ret=-24.3%
  - 2021: S=0.48 (weak), ret=+6.7%
  - 2022: S=1.20 (moderate), ret=+19.1%
  - 2023: S=-0.09 (negative), ret=-1.1%

## Risk & Drawdown
- Max drawdown: 52.91% over 1518 days (recovered)
- Annualized: return +1.0%, volatility 12.9% (fraction of booksize)
- Hit rate: 53.2% positive days
- Tail shape: skew -0.25, excess kurtosis +0.57

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -3.44, max 2.40, latest -0.31

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +9.35%; worst month: -10.78%
Positive months: 51%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=1.59
- Sideways: S=0.97
- Bear: S=-2.53

## Negated Direction
Best negated: `rank(-1 * ts_delta(high, 5))` S=1.32, F=0.72, INFERIOR
Direction gap: +0.70 (negated - positive best Sharpe). NEGATION DOMINANT — field is significantly stronger when reversed.

Negated template variants:
- `rank(-1 * high)`: S=-0.08, F=-0.02, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * high / close)`: S=-0.39, F=-0.16, T=43.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(high, 5))`: S=1.32, F=0.72, T=34.8%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(high)` | TOP3000 | 0.08 | 0.02 | 52.9% | 60% | bull-only |

## Correlation Notes
Top correlates:
- open: 1.000 (strongly positively correlated)
- close: 1.000 (strongly positively correlated)
- vwap: 1.000 (strongly positively correlated)
- low: 1.000 (strongly positively correlated)
- put_breakeven_10: 0.995 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_FITNESS. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
