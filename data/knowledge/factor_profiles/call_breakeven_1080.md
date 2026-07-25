---
field: call_breakeven_1080
dataset: option9
best_template: rank_neg_delta
best_sharpe: 1.1
best_fitness: 0.46
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 21
regime_profile: bull-only
n_variations_with_pnl: 1
max_drawdown: 0.4747
ann_vol: 0.1159
hit_rate: 0.532
rolling_sharpe_min: -3.184
rolling_sharpe_max: 2.493
negated_best_sharpe: 1.1
negated_best_template: rank_neg_delta
negated_best_fitness: 0.46
n_negated_sims: 4
direction_gap: 0.76
---
# call_breakeven_1080 (option9)

*Price at which a stock's call options with expiration 1080 days in the future break even based on its recent bid/ask mean.*

## Signal Profile
- `rank(call_breakeven_1080)`: S=0.14, F=0.05, T=3.1%, INFERIOR (TOP3000)
- `rank(call_breakeven_1080 / close)`: S=0.22, F=0.12, T=8.7%, INFERIOR (TOP3000)
- `rank(ts_delta(call_breakeven_1080, 5))`: S=-0.39, F=-0.11, T=36.7%, INFERIOR (TOP1000)
- `-rank(call_breakeven_1080)`: S=0.01, F=0.00, T=3.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(call_breakeven_1080, 5))`: S=1.10, F=0.46, T=38.8%, INFERIOR (TOP3000)
- `-ts_zscore(call_breakeven_1080, 63)`: S=0.20, F=0.07, T=14.5%, INFERIOR (TOP3000)
- `ts_mean(call_breakeven_1080, 10)`: S=0.34, F=0.18, T=1.4%, INFERIOR (TOP3000)
- `rank(ts_rank(call_breakeven_1080, 22))`: S=-0.38, F=-0.14, T=23.8%, INFERIOR (TOP3000)
- `rank(-1 * call_breakeven_1080)`: S=-0.14, F=-0.05, T=3.1%, INFERIOR (TOP3000)
- `rank(-1 * call_breakeven_1080 / close)`: S=-0.26, F=-0.15, T=10.5%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 20F/1P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 21F/0P
- LOW_SUB_UNIVERSE_SHARPE: 9F/10P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.14, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.65 (moderate), ret=+4.8%
  - 2020: S=-1.69 (negative), ret=-19.8%
  - 2021: S=0.39 (weak), ret=+4.9%
  - 2022: S=1.40 (moderate), ret=+18.1%
  - 2023: S=0.03 (weak), ret=+0.3%

## Risk & Drawdown
- Max drawdown: 47.47% over 1491 days (recovered)
- Annualized: return +1.7%, volatility 11.6% (fraction of booksize)
- Hit rate: 53.2% positive days
- Tail shape: skew -0.27, excess kurtosis +0.51

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -3.18, max 2.49, latest -0.19

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +7.92%; worst month: -10.04%
Positive months: 51%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=1.57
- Sideways: S=1.12
- Bear: S=-2.33

## Negated Direction
Best negated: `rank(-1 * ts_delta(call_breakeven_1080, 5))` S=1.10, F=0.46, INFERIOR
Direction gap: +0.76 (negated - positive best Sharpe). NEGATION DOMINANT — field is significantly stronger when reversed.

Negated template variants:
- `rank(-1 * call_breakeven_1080)`: S=-0.14, F=-0.05, T=3.1%, INFERIOR (TOP3000)
- `rank(-1 * call_breakeven_1080 / close)`: S=-0.26, F=-0.15, T=10.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(call_breakeven_1080, 5))`: S=1.10, F=0.46, T=38.8%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(call_breakeven_1080)` | TOP3000 | 0.14 | 0.05 | 47.5% | 80% | bull-only |

## Correlation Notes
Top correlates:
- call_breakeven_720: 1.000 (strongly positively correlated)
- call_breakeven_270: 0.999 (strongly positively correlated)
- call_breakeven_180: 0.999 (strongly positively correlated)
- call_breakeven_360: 0.999 (strongly positively correlated)
- call_breakeven_150: 0.999 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
