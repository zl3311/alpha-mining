---
field: put_breakeven_30
dataset: option9
best_template: rank_neg_delta
best_sharpe: 1.24
best_fitness: 0.56
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 21
regime_profile: bull-only
n_variations_with_pnl: 1
max_drawdown: 0.5395
ann_vol: 0.1362
hit_rate: 0.5377
rolling_sharpe_min: -3.258
rolling_sharpe_max: 2.416
negated_best_sharpe: 1.24
negated_best_template: rank_neg_delta
negated_best_fitness: 0.56
n_negated_sims: 4
direction_gap: 0.68
---
# put_breakeven_30 (option9)

*The weighted mean break-even price of put options expiring in 30 days based on recent bid/ask prices*

## Signal Profile
- `rank(put_breakeven_30)`: S=0.09, F=0.03, T=3.3%, INFERIOR (TOP3000)
- `rank(put_breakeven_30 / close)`: S=0.56, F=0.33, T=18.9%, INFERIOR (TOP3000)
- `rank(ts_delta(put_breakeven_30, 5))`: S=-0.80, F=-0.35, T=38.6%, INFERIOR (TOP200)
- `-rank(put_breakeven_30)`: S=0.04, F=0.01, T=3.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(put_breakeven_30, 5))`: S=1.24, F=0.56, T=38.2%, INFERIOR (TOP3000)
- `-ts_zscore(put_breakeven_30, 63)`: S=0.49, F=0.28, T=15.9%, INFERIOR (TOP3000)
- `ts_mean(put_breakeven_30, 10)`: S=0.27, F=0.13, T=1.5%, INFERIOR (TOP3000)
- `rank(ts_rank(put_breakeven_30, 22))`: S=-0.65, F=-0.30, T=25.7%, INFERIOR (TOP3000)
- `rank(-1 * put_breakeven_30)`: S=-0.09, F=-0.03, T=3.3%, INFERIOR (TOP3000)
- `rank(-1 * put_breakeven_30 / close)`: S=-0.80, F=-0.47, T=19.0%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 20F/1P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 21F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/6P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.09, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.53 (moderate), ret=+4.3%
  - 2020: S=-1.91 (negative), ret=-24.6%
  - 2021: S=0.50 (moderate), ret=+7.3%
  - 2022: S=1.25 (moderate), ret=+20.9%
  - 2023: S=-0.17 (negative), ret=-2.1%

## Risk & Drawdown
- Max drawdown: 53.95% over 1504 days (recovered)
- Annualized: return +1.2%, volatility 13.6% (fraction of booksize)
- Hit rate: 53.8% positive days
- Tail shape: skew -0.26, excess kurtosis +0.54

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -3.26, max 2.42, latest -0.38

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +9.29%; worst month: -11.28%
Positive months: 51%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=1.59
- Sideways: S=1.04
- Bear: S=-2.52

## Negated Direction
Best negated: `rank(-1 * ts_delta(put_breakeven_30, 5))` S=1.24, F=0.56, INFERIOR
Direction gap: +0.68 (negated - positive best Sharpe). NEGATION DOMINANT — field is significantly stronger when reversed.

Negated template variants:
- `rank(-1 * put_breakeven_30)`: S=-0.09, F=-0.03, T=3.3%, INFERIOR (TOP3000)
- `rank(-1 * put_breakeven_30 / close)`: S=-0.80, F=-0.47, T=19.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(put_breakeven_30, 5))`: S=1.24, F=0.56, T=38.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(put_breakeven_30)` | TOP3000 | 0.09 | 0.03 | 53.9% | 60% | bull-only |

## Correlation Notes
Top correlates:
- put_breakeven_20: 1.000 (strongly positively correlated)
- put_breakeven_10: 1.000 (strongly positively correlated)
- put_breakeven_60: 1.000 (strongly positively correlated)
- put_breakeven_90: 1.000 (strongly positively correlated)
- put_breakeven_120: 1.000 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
