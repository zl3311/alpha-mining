---
field: call_breakeven_360
dataset: option9
best_template: rank_neg_delta
best_sharpe: 1.11
best_fitness: 0.47
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 21
regime_profile: bull-only
n_variations_with_pnl: 1
max_drawdown: 0.4735
ann_vol: 0.1143
hit_rate: 0.532
rolling_sharpe_min: -3.196
rolling_sharpe_max: 2.577
negated_best_sharpe: 1.11
negated_best_template: rank_neg_delta
negated_best_fitness: 0.47
n_negated_sims: 4
direction_gap: 0.74
---
# call_breakeven_360 (option9)

*Weighted mean break-even price of call options expiring in 360 days, based on recent bid/ask prices*

## Signal Profile
- `rank(call_breakeven_360)`: S=0.14, F=0.05, T=3.1%, INFERIOR (TOP3000)
- `rank(call_breakeven_360 / close)`: S=0.26, F=0.15, T=8.9%, INFERIOR (TOP3000)
- `rank(ts_delta(call_breakeven_360, 5))`: S=-0.41, F=-0.12, T=36.3%, INFERIOR (TOP1000)
- `-rank(call_breakeven_360)`: S=0.01, F=0.00, T=2.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(call_breakeven_360, 5))`: S=1.11, F=0.47, T=38.4%, INFERIOR (TOP3000)
- `-ts_zscore(call_breakeven_360, 63)`: S=0.21, F=0.08, T=14.4%, INFERIOR (TOP3000)
- `ts_mean(call_breakeven_360, 10)`: S=0.37, F=0.20, T=1.4%, INFERIOR (TOP3000)
- `rank(ts_rank(call_breakeven_360, 22))`: S=-0.35, F=-0.12, T=23.5%, INFERIOR (TOP3000)
- `rank(-1 * call_breakeven_360)`: S=-0.14, F=-0.05, T=3.1%, INFERIOR (TOP3000)
- `rank(-1 * call_breakeven_360 / close)`: S=-0.24, F=-0.13, T=10.6%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 20F/1P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 21F/0P
- LOW_SUB_UNIVERSE_SHARPE: 12F/7P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.14, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.66 (moderate), ret=+4.8%
  - 2020: S=-1.69 (negative), ret=-19.8%
  - 2021: S=0.40 (weak), ret=+5.0%
  - 2022: S=1.37 (moderate), ret=+17.3%
  - 2023: S=0.04 (weak), ret=+0.5%

## Risk & Drawdown
- Max drawdown: 47.35% over 1498 days (recovered)
- Annualized: return +1.6%, volatility 11.4% (fraction of booksize)
- Hit rate: 53.2% positive days
- Tail shape: skew -0.27, excess kurtosis +0.49

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -3.20, max 2.58, latest -0.17

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +8.07%; worst month: -9.95%
Positive months: 51%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=1.58
- Sideways: S=1.14
- Bear: S=-2.35

## Negated Direction
Best negated: `rank(-1 * ts_delta(call_breakeven_360, 5))` S=1.11, F=0.47, INFERIOR
Direction gap: +0.74 (negated - positive best Sharpe). NEGATION DOMINANT — field is significantly stronger when reversed.

Negated template variants:
- `rank(-1 * call_breakeven_360)`: S=-0.14, F=-0.05, T=3.1%, INFERIOR (TOP3000)
- `rank(-1 * call_breakeven_360 / close)`: S=-0.24, F=-0.13, T=10.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(call_breakeven_360, 5))`: S=1.11, F=0.47, T=38.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(call_breakeven_360)` | TOP3000 | 0.14 | 0.05 | 47.3% | 80% | bull-only |

## Correlation Notes
Top correlates:
- call_breakeven_270: 0.999 (strongly positively correlated)
- call_breakeven_720: 0.999 (strongly positively correlated)
- call_breakeven_1080: 0.999 (strongly positively correlated)
- option_breakeven_360: 0.999 (strongly positively correlated)
- call_breakeven_120: 0.998 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
