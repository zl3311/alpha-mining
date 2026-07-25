---
field: vwap
dataset: pv1
best_template: rank_neg_delta
best_sharpe: 1.36
best_fitness: 0.77
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_FITNESS
n_sims: 21
regime_profile: bull-only
n_variations_with_pnl: 1
max_drawdown: 0.5342
ann_vol: 0.13
hit_rate: 0.5336
rolling_sharpe_min: -3.443
rolling_sharpe_max: 2.388
negated_best_sharpe: 1.36
negated_best_template: rank_neg_delta
negated_best_fitness: 0.77
n_negated_sims: 4
direction_gap: -0.08
---
# vwap (pv1)

*Daily volume weighted average price*

## Signal Profile
- `rank(vwap)`: S=0.08, F=0.02, T=1.6%, INFERIOR (TOP3000)
- `rank(vwap / close)`: S=1.44, F=0.61, T=70.2%, INFERIOR (TOP3000)
- `rank(ts_delta(vwap, 5))`: S=-1.06, F=-0.55, T=35.0%, INFERIOR (TOP1000)
- `-rank(vwap)`: S=0.07, F=0.02, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(vwap, 5))`: S=1.36, F=0.77, T=34.5%, INFERIOR (TOP3000)
- `-ts_zscore(vwap, 63)`: S=0.66, F=0.51, T=13.0%, INFERIOR (TOP3000)
- `ts_mean(vwap, 10)`: S=-0.07, F=-0.02, T=1.0%, INFERIOR (TOP3000)
- `rank(ts_rank(vwap, 22))`: S=-0.84, F=-0.50, T=24.1%, INFERIOR (TOP3000)
- `rank(-1 * vwap)`: S=-0.08, F=-0.02, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * vwap / close)`: S=-1.77, F=-0.78, T=69.9%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 1F/20P
- HIGH_TURNOVER: 1F/20P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 19F/2P
- LOW_SUB_UNIVERSE_SHARPE: 13F/6P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.08, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.61 (moderate), ret=+4.5%
  - 2020: S=-2.06 (negative), ret=-24.7%
  - 2021: S=0.48 (weak), ret=+6.7%
  - 2022: S=1.21 (moderate), ret=+19.4%
  - 2023: S=-0.09 (negative), ret=-1.1%

## Risk & Drawdown
- Max drawdown: 53.42% over 1518 days (recovered)
- Annualized: return +1.0%, volatility 13.0% (fraction of booksize)
- Hit rate: 53.4% positive days
- Tail shape: skew -0.26, excess kurtosis +0.60

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -3.44, max 2.39, latest -0.31

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +9.40%; worst month: -10.88%
Positive months: 51%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=1.57
- Sideways: S=0.96
- Bear: S=-2.52

## Negated Direction
Best negated: `rank(-1 * ts_delta(vwap, 5))` S=1.36, F=0.77, INFERIOR
Direction gap: -0.08 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * vwap)`: S=-0.08, F=-0.02, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * vwap / close)`: S=-1.77, F=-0.78, T=69.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(vwap, 5))`: S=1.36, F=0.77, T=34.5%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(vwap)` | TOP3000 | 0.08 | 0.02 | 53.4% | 60% | bull-only |

## Correlation Notes
Top correlates:
- close: 1.000 (strongly positively correlated)
- open: 1.000 (strongly positively correlated)
- low: 1.000 (strongly positively correlated)
- high: 1.000 (strongly positively correlated)
- put_breakeven_10: 0.996 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_FITNESS. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
