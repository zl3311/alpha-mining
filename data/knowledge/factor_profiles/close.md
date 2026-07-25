---
field: close
dataset: pv1
cluster: pv1_other
coverage: 1.0
community_alphas: 546513
best_template: rank_neg_delta
best_sharpe: 1.36
best_fitness: 0.77
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_FITNESS
n_sims: 21
regime_profile: bull-only
n_variations_with_pnl: 1
max_drawdown: 0.5345
ann_vol: 0.1297
hit_rate: 0.5336
rolling_sharpe_min: -3.452
rolling_sharpe_max: 2.386
negated_best_sharpe: 1.36
negated_best_template: rank_neg_delta
negated_best_fitness: 0.77
n_negated_sims: 4
direction_gap: 0.67
---
# close (pv1)

*Daily close price*

## Signal Profile
- `rank(close)`: S=0.07, F=0.02, T=1.6%, INFERIOR (TOP3000)
- `rank(close / close)`: S=0.04, F=0.01, T=2.9%, INFERIOR (TOP3000)
- `rank(ts_delta(close, 5))`: S=-1.06, F=-0.55, T=35.7%, INFERIOR (TOP1000)
- `-rank(close)`: S=0.06, F=0.01, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(close, 5))`: S=1.36, F=0.77, T=35.2%, INFERIOR (TOP3000)
- `-ts_zscore(close, 63)`: S=0.69, F=0.54, T=13.2%, INFERIOR (TOP3000)
- `ts_mean(close, 10)`: S=-0.06, F=-0.01, T=1.0%, INFERIOR (TOP3000)
- `rank(ts_rank(close, 22))`: S=-0.90, F=-0.55, T=24.4%, INFERIOR (TOP3000)
- `rank(-1 * close)`: S=-0.07, F=-0.02, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * close / close)`: S=0.51, F=0.35, T=2.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 3F/18P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 20F/1P
- LOW_SUB_UNIVERSE_SHARPE: 12F/7P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.07, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.61 (moderate), ret=+4.5%
  - 2020: S=-2.06 (negative), ret=-24.7%
  - 2021: S=0.47 (weak), ret=+6.7%
  - 2022: S=1.19 (moderate), ret=+19.1%
  - 2023: S=-0.09 (negative), ret=-1.1%

## Risk & Drawdown
- Max drawdown: 53.45% over 1518 days (recovered)
- Annualized: return +0.9%, volatility 13.0% (fraction of booksize)
- Hit rate: 53.4% positive days
- Tail shape: skew -0.26, excess kurtosis +0.59

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -3.45, max 2.39, latest -0.31

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +9.41%; worst month: -10.89%
Positive months: 51%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=1.58
- Sideways: S=0.96
- Bear: S=-2.54

## Negated Direction
Best negated: `rank(-1 * ts_delta(close, 5))` S=1.36, F=0.77, INFERIOR
Direction gap: +0.67 (negated - positive best Sharpe). NEGATION DOMINANT — field is significantly stronger when reversed.

Negated template variants:
- `rank(-1 * close)`: S=-0.07, F=-0.02, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * close / close)`: S=0.51, F=0.35, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(close, 5))`: S=1.36, F=0.77, T=35.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(close)` | TOP3000 | 0.07 | 0.02 | 53.4% | 60% | bull-only |

## Correlation Notes
Top correlates:
- low: 1.000 (strongly positively correlated)
- open: 1.000 (strongly positively correlated)
- high: 1.000 (strongly positively correlated)
- vwap: 1.000 (strongly positively correlated)
- put_breakeven_10: 0.995 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_FITNESS. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
