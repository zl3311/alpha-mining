---
field: call_breakeven_150
dataset: option9
best_template: rank_neg_delta
best_sharpe: 0.99
best_fitness: 0.44
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 21
regime_profile: bull-only
n_variations_with_pnl: 1
max_drawdown: 0.4877
ann_vol: 0.119
hit_rate: 0.5336
rolling_sharpe_min: -3.217
rolling_sharpe_max: 2.451
negated_best_sharpe: 0.99
negated_best_template: rank_neg_delta
negated_best_fitness: 0.44
n_negated_sims: 4
direction_gap: 0.48
---
# call_breakeven_150 (option9)

*Price at which a stock's call options with expiration 150 days in the future break even based on its recent bid/ask mean, weighted by open interest or volume*

## Signal Profile
- `rank(call_breakeven_150)`: S=0.10, F=0.03, T=2.9%, INFERIOR (TOP3000)
- `rank(call_breakeven_150 / close)`: S=0.24, F=0.14, T=9.6%, INFERIOR (TOP3000)
- `rank(ts_delta(call_breakeven_150, 5))`: S=-0.77, F=-0.34, T=33.1%, INFERIOR (TOP1000)
- `-rank(call_breakeven_150)`: S=0.04, F=0.01, T=2.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(call_breakeven_150, 5))`: S=0.99, F=0.44, T=35.7%, INFERIOR (TOP3000)
- `-ts_zscore(call_breakeven_150, 63)`: S=0.51, F=0.32, T=12.8%, INFERIOR (TOP3000)
- `ts_mean(call_breakeven_150, 10)`: S=0.34, F=0.18, T=1.3%, INFERIOR (TOP3000)
- `rank(ts_rank(call_breakeven_150, 22))`: S=-0.52, F=-0.24, T=22.1%, INFERIOR (TOP3000)
- `rank(-1 * call_breakeven_150)`: S=-0.10, F=-0.03, T=2.9%, INFERIOR (TOP3000)
- `rank(-1 * call_breakeven_150 / close)`: S=-0.22, F=-0.12, T=10.5%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 20F/1P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 21F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/6P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.10, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.60 (moderate), ret=+4.4%
  - 2020: S=-1.75 (negative), ret=-20.7%
  - 2021: S=0.41 (weak), ret=+5.1%
  - 2022: S=1.30 (moderate), ret=+18.0%
  - 2023: S=-0.07 (negative), ret=-0.8%

## Risk & Drawdown
- Max drawdown: 48.77% over 1507 days (recovered)
- Annualized: return +1.2%, volatility 11.9% (fraction of booksize)
- Hit rate: 53.4% positive days
- Tail shape: skew -0.27, excess kurtosis +0.55

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -3.22, max 2.45, latest -0.28

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +8.05%; worst month: -10.20%
Positive months: 51%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=1.51
- Sideways: S=1.07
- Bear: S=-2.36

## Negated Direction
Best negated: `rank(-1 * ts_delta(call_breakeven_150, 5))` S=0.99, F=0.44, INFERIOR
Direction gap: +0.48 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * call_breakeven_150)`: S=-0.10, F=-0.03, T=2.9%, INFERIOR (TOP3000)
- `rank(-1 * call_breakeven_150 / close)`: S=-0.22, F=-0.12, T=10.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(call_breakeven_150, 5))`: S=0.99, F=0.44, T=35.7%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(call_breakeven_150)` | TOP3000 | 0.10 | 0.03 | 48.8% | 60% | bull-only |

## Correlation Notes
Top correlates:
- call_breakeven_120: 1.000 (strongly positively correlated)
- call_breakeven_180: 1.000 (strongly positively correlated)
- call_breakeven_90: 1.000 (strongly positively correlated)
- call_breakeven_60: 0.999 (strongly positively correlated)
- call_breakeven_1080: 0.999 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
