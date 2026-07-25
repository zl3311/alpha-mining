---
field: call_breakeven_270
dataset: option9
best_template: rank_neg_delta
best_sharpe: 1.16
best_fitness: 0.49
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 21
regime_profile: bull-only
n_variations_with_pnl: 1
max_drawdown: 0.476
ann_vol: 0.1161
hit_rate: 0.5296
rolling_sharpe_min: -3.198
rolling_sharpe_max: 2.533
negated_best_sharpe: 1.16
negated_best_template: rank_neg_delta
negated_best_fitness: 0.49
n_negated_sims: 4
direction_gap: 0.79
---
# call_breakeven_270 (option9)

*Price at which a stock's call options with expiration 270 days in the future break even based on its recent bid/ask mean*

## Signal Profile
- `rank(call_breakeven_270)`: S=0.14, F=0.05, T=3.1%, INFERIOR (TOP3000)
- `rank(call_breakeven_270 / close)`: S=0.26, F=0.16, T=10.0%, INFERIOR (TOP3000)
- `rank(ts_delta(call_breakeven_270, 5))`: S=-0.61, F=-0.21, T=35.9%, INFERIOR (TOP1000)
- `-rank(call_breakeven_270)`: S=-0.01, F=0.00, T=3.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(call_breakeven_270, 5))`: S=1.16, F=0.49, T=38.0%, INFERIOR (TOP3000)
- `-ts_zscore(call_breakeven_270, 63)`: S=0.27, F=0.11, T=14.6%, INFERIOR (TOP3000)
- `ts_mean(call_breakeven_270, 10)`: S=0.37, F=0.20, T=1.4%, INFERIOR (TOP3000)
- `rank(ts_rank(call_breakeven_270, 22))`: S=-0.55, F=-0.23, T=23.3%, INFERIOR (TOP3000)
- `rank(-1 * call_breakeven_270)`: S=-0.14, F=-0.05, T=3.1%, INFERIOR (TOP3000)
- `rank(-1 * call_breakeven_270 / close)`: S=-0.25, F=-0.14, T=11.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 20F/1P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 21F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/6P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.14, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.62 (moderate), ret=+4.6%
  - 2020: S=-1.71 (negative), ret=-20.0%
  - 2021: S=0.44 (weak), ret=+5.5%
  - 2022: S=1.35 (moderate), ret=+17.7%
  - 2023: S=0.04 (weak), ret=+0.5%

## Risk & Drawdown
- Max drawdown: 47.60% over 1491 days (recovered)
- Annualized: return +1.7%, volatility 11.6% (fraction of booksize)
- Hit rate: 53.0% positive days
- Tail shape: skew -0.27, excess kurtosis +0.49

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -3.20, max 2.53, latest -0.18

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +8.08%; worst month: -10.08%
Positive months: 51%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=1.57
- Sideways: S=1.14
- Bear: S=-2.33

## Negated Direction
Best negated: `rank(-1 * ts_delta(call_breakeven_270, 5))` S=1.16, F=0.49, INFERIOR
Direction gap: +0.79 (negated - positive best Sharpe). NEGATION DOMINANT — field is significantly stronger when reversed.

Negated template variants:
- `rank(-1 * call_breakeven_270)`: S=-0.14, F=-0.05, T=3.1%, INFERIOR (TOP3000)
- `rank(-1 * call_breakeven_270 / close)`: S=-0.25, F=-0.14, T=11.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(call_breakeven_270, 5))`: S=1.16, F=0.49, T=38.0%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(call_breakeven_270)` | TOP3000 | 0.14 | 0.05 | 47.6% | 80% | bull-only |

## Correlation Notes
Top correlates:
- call_breakeven_1080: 0.999 (strongly positively correlated)
- call_breakeven_720: 0.999 (strongly positively correlated)
- call_breakeven_360: 0.999 (strongly positively correlated)
- option_breakeven_360: 0.999 (strongly positively correlated)
- option_breakeven_270: 0.999 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
