---
field: call_breakeven_10
dataset: option9
best_template: ts_zscore
best_sharpe: 0.47
best_fitness: 0.27
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 21
regime_profile: bull-only
n_variations_with_pnl: 1
max_drawdown: 0.5173
ann_vol: 0.127
hit_rate: 0.5336
rolling_sharpe_min: -3.262
rolling_sharpe_max: 2.382
negated_best_sharpe: 0.73
negated_best_template: rank_neg_delta
negated_best_fitness: 0.26
n_negated_sims: 4
direction_gap: 0.26
---
# call_breakeven_10 (option9)

*Price at which a stock's call options with expiration 10 days in the future break even based on its recent bid/ask mean, weighted by open interest or volume*

## Signal Profile
- `rank(call_breakeven_10)`: S=0.07, F=0.02, T=3.0%, INFERIOR (TOP3000)
- `rank(call_breakeven_10 / close)`: S=0.33, F=0.18, T=19.0%, INFERIOR (TOP3000)
- `rank(ts_delta(call_breakeven_10, 5))`: S=-0.59, F=-0.22, T=36.3%, INFERIOR (TOP500)
- `-rank(call_breakeven_10)`: S=0.05, F=0.01, T=3.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(call_breakeven_10, 5))`: S=0.73, F=0.26, T=38.8%, INFERIOR (TOP3000)
- `-ts_zscore(call_breakeven_10, 63)`: S=0.47, F=0.27, T=15.0%, INFERIOR (TOP3000)
- `ts_mean(call_breakeven_10, 10)`: S=0.29, F=0.14, T=1.4%, INFERIOR (TOP3000)
- `rank(ts_rank(call_breakeven_10, 22))`: S=-0.75, F=-0.38, T=25.4%, INFERIOR (TOP3000)
- `rank(-1 * call_breakeven_10)`: S=-0.07, F=-0.02, T=3.0%, INFERIOR (TOP3000)
- `rank(-1 * call_breakeven_10 / close)`: S=-0.30, F=-0.13, T=20.8%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 20F/1P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 21F/0P
- LOW_SUB_UNIVERSE_SHARPE: 9F/10P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.07, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.53 (moderate), ret=+4.1%
  - 2020: S=-1.83 (negative), ret=-22.7%
  - 2021: S=0.40 (weak), ret=+5.2%
  - 2022: S=1.26 (moderate), ret=+19.4%
  - 2023: S=-0.11 (negative), ret=-1.4%

## Risk & Drawdown
- Max drawdown: 51.73% over 1518 days (recovered)
- Annualized: return +0.9%, volatility 12.7% (fraction of booksize)
- Hit rate: 53.4% positive days
- Tail shape: skew -0.27, excess kurtosis +0.56

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -3.26, max 2.38, latest -0.33

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +8.53%; worst month: -10.47%
Positive months: 51%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=1.52
- Sideways: S=1.03
- Bear: S=-2.43

## Negated Direction
Best negated: `rank(-1 * ts_delta(call_breakeven_10, 5))` S=0.73, F=0.26, INFERIOR
Direction gap: +0.26 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * call_breakeven_10)`: S=-0.07, F=-0.02, T=3.0%, INFERIOR (TOP3000)
- `rank(-1 * call_breakeven_10 / close)`: S=-0.30, F=-0.13, T=20.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(call_breakeven_10, 5))`: S=0.73, F=0.26, T=38.8%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(call_breakeven_10)` | TOP3000 | 0.07 | 0.02 | 51.7% | 60% | bull-only |

## Correlation Notes
Top correlates:
- call_breakeven_20: 1.000 (strongly positively correlated)
- call_breakeven_30: 1.000 (strongly positively correlated)
- option_breakeven_20: 1.000 (strongly positively correlated)
- option_breakeven_10: 1.000 (strongly positively correlated)
- option_breakeven_30: 1.000 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
