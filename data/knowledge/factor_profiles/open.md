---
field: open
dataset: pv1
best_template: rank_value_norm
best_sharpe: 1.82
best_fitness: 0.99
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_FITNESS
n_sims: 21
regime_profile: bull-only
n_variations_with_pnl: 1
max_drawdown: 0.5286
ann_vol: 0.1295
hit_rate: 0.532
rolling_sharpe_min: -3.414
rolling_sharpe_max: 2.413
negated_best_sharpe: 1.24
negated_best_template: rank_neg_delta
negated_best_fitness: 0.64
n_negated_sims: 4
direction_gap: -0.58
---
# open (pv1)

*Daily open price*

## Signal Profile
- `rank(open)`: S=0.09, F=0.03, T=1.6%, INFERIOR (TOP3000)
- `rank(open / close)`: S=1.82, F=0.99, T=70.0%, INFERIOR (TOP3000)
- `rank(ts_delta(open, 5))`: S=-0.92, F=-0.43, T=36.0%, INFERIOR (TOP1000)
- `-rank(open)`: S=0.04, F=0.01, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(open, 5))`: S=1.24, F=0.64, T=35.6%, INFERIOR (TOP3000)
- `-ts_zscore(open, 63)`: S=0.61, F=0.44, T=13.3%, INFERIOR (TOP3000)
- `ts_mean(open, 10)`: S=-0.06, F=-0.01, T=1.0%, INFERIOR (TOP3000)
- `rank(ts_rank(open, 22))`: S=-0.75, F=-0.41, T=24.6%, INFERIOR (TOP3000)
- `rank(-1 * open)`: S=-0.09, F=-0.03, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * open / close)`: S=-1.87, F=-0.99, T=70.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 1F/20P
- HIGH_TURNOVER: 1F/20P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 20F/1P
- LOW_SUB_UNIVERSE_SHARPE: 14F/5P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.09, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.61 (moderate), ret=+4.6%
  - 2020: S=-2.03 (negative), ret=-24.3%
  - 2021: S=0.49 (weak), ret=+6.9%
  - 2022: S=1.21 (moderate), ret=+19.4%
  - 2023: S=-0.08 (negative), ret=-0.9%

## Risk & Drawdown
- Max drawdown: 52.86% over 1507 days (recovered)
- Annualized: return +1.1%, volatility 13.0% (fraction of booksize)
- Hit rate: 53.2% positive days
- Tail shape: skew -0.25, excess kurtosis +0.57

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -3.41, max 2.41, latest -0.30

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +9.43%; worst month: -10.84%
Positive months: 51%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=1.61
- Sideways: S=0.98
- Bear: S=-2.53

## Negated Direction
Best negated: `rank(-1 * ts_delta(open, 5))` S=1.24, F=0.64, INFERIOR
Direction gap: -0.58 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * open)`: S=-0.09, F=-0.03, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * open / close)`: S=-1.87, F=-0.99, T=70.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(open, 5))`: S=1.24, F=0.64, T=35.6%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(open)` | TOP3000 | 0.09 | 0.03 | 52.9% | 60% | bull-only |

## Correlation Notes
Top correlates:
- high: 1.000 (strongly positively correlated)
- close: 1.000 (strongly positively correlated)
- low: 1.000 (strongly positively correlated)
- vwap: 1.000 (strongly positively correlated)
- put_breakeven_10: 0.996 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_FITNESS. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
