---
field: low
dataset: pv1
best_template: rank_neg_delta
best_sharpe: 1.37
best_fitness: 0.77
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_FITNESS
n_sims: 21
regime_profile: bull-only
n_variations_with_pnl: 1
max_drawdown: 0.5331
ann_vol: 0.1307
hit_rate: 0.5336
rolling_sharpe_min: -3.419
rolling_sharpe_max: 2.395
negated_best_sharpe: 1.37
negated_best_template: rank_neg_delta
negated_best_fitness: 0.77
n_negated_sims: 4
direction_gap: 0.7
---
# low (pv1)

*Daily low price*

## Signal Profile
- `rank(low)`: S=0.08, F=0.02, T=1.6%, INFERIOR (TOP3000)
- `rank(low / close)`: S=0.53, F=0.23, T=46.9%, INFERIOR (TOP3000)
- `rank(ts_delta(low, 5))`: S=-1.06, F=-0.55, T=35.3%, INFERIOR (TOP1000)
- `-rank(low)`: S=0.05, F=0.01, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(low, 5))`: S=1.37, F=0.77, T=34.8%, INFERIOR (TOP3000)
- `-ts_zscore(low, 63)`: S=0.67, F=0.52, T=13.1%, INFERIOR (TOP3000)
- `ts_mean(low, 10)`: S=-0.06, F=-0.01, T=1.0%, INFERIOR (TOP3000)
- `rank(ts_rank(low, 22))`: S=-0.83, F=-0.49, T=24.3%, INFERIOR (TOP3000)
- `rank(-1 * low)`: S=-0.08, F=-0.02, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * low / close)`: S=-0.66, F=-0.32, T=45.6%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 1F/20P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 20F/1P
- LOW_SUB_UNIVERSE_SHARPE: 13F/6P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.08, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.61 (moderate), ret=+4.6%
  - 2020: S=-2.05 (negative), ret=-24.6%
  - 2021: S=0.49 (weak), ret=+6.9%
  - 2022: S=1.20 (moderate), ret=+19.4%
  - 2023: S=-0.08 (negative), ret=-1.0%

## Risk & Drawdown
- Max drawdown: 53.31% over 1507 days (recovered)
- Annualized: return +1.1%, volatility 13.1% (fraction of booksize)
- Hit rate: 53.4% positive days
- Tail shape: skew -0.25, excess kurtosis +0.60

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -3.42, max 2.40, latest -0.30

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +9.48%; worst month: -10.95%
Positive months: 51%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=1.60
- Sideways: S=0.97
- Bear: S=-2.54

## Negated Direction
Best negated: `rank(-1 * ts_delta(low, 5))` S=1.37, F=0.77, INFERIOR
Direction gap: +0.70 (negated - positive best Sharpe). NEGATION DOMINANT — field is significantly stronger when reversed.

Negated template variants:
- `rank(-1 * low)`: S=-0.08, F=-0.02, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * low / close)`: S=-0.66, F=-0.32, T=45.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(low, 5))`: S=1.37, F=0.77, T=34.8%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(low)` | TOP3000 | 0.08 | 0.02 | 53.3% | 60% | bull-only |

## Correlation Notes
Top correlates:
- close: 1.000 (strongly positively correlated)
- open: 1.000 (strongly positively correlated)
- vwap: 1.000 (strongly positively correlated)
- high: 1.000 (strongly positively correlated)
- put_breakeven_10: 0.996 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_FITNESS. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
