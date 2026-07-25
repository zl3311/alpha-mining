---
field: option_breakeven_20
dataset: option9
best_template: rank_neg_delta
best_sharpe: 0.87
best_fitness: 0.33
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 21
regime_profile: bull-only
n_variations_with_pnl: 1
max_drawdown: 0.5269
ann_vol: 0.1299
hit_rate: 0.5328
rolling_sharpe_min: -3.277
rolling_sharpe_max: 2.39
negated_best_sharpe: 0.87
negated_best_template: rank_neg_delta
negated_best_fitness: 0.33
n_negated_sims: 4
direction_gap: 0.43
---
# option_breakeven_20 (option9)

*Price at which a stock's options with expiration 20 days in the future break even based on its recent bid/ask mean*

## Signal Profile
- `rank(option_breakeven_20)`: S=0.07, F=0.02, T=2.9%, INFERIOR (TOP3000)
- `rank(option_breakeven_20 / close)`: S=0.21, F=0.07, T=21.0%, INFERIOR (TOP3000)
- `rank(ts_delta(option_breakeven_20, 5))`: S=-0.12, F=-0.02, T=38.6%, INFERIOR (TOP200)
- `-rank(option_breakeven_20)`: S=0.05, F=0.01, T=3.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(option_breakeven_20, 5))`: S=0.87, F=0.33, T=38.4%, INFERIOR (TOP3000)
- `-ts_zscore(option_breakeven_20, 63)`: S=0.44, F=0.24, T=16.1%, INFERIOR (TOP3000)
- `ts_mean(option_breakeven_20, 10)`: S=0.26, F=0.12, T=1.5%, INFERIOR (TOP3000)
- `rank(ts_rank(option_breakeven_20, 22))`: S=-0.37, F=-0.13, T=26.3%, INFERIOR (TOP3000)
- `rank(-1 * option_breakeven_20)`: S=-0.07, F=-0.02, T=2.9%, INFERIOR (TOP3000)
- `rank(-1 * option_breakeven_20 / close)`: S=-0.14, F=-0.03, T=21.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 20F/1P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 21F/0P
- LOW_SUB_UNIVERSE_SHARPE: 12F/7P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.07, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.52 (moderate), ret=+4.1%
  - 2020: S=-1.85 (negative), ret=-23.3%
  - 2021: S=0.41 (weak), ret=+5.6%
  - 2022: S=1.25 (moderate), ret=+19.7%
  - 2023: S=-0.15 (negative), ret=-1.9%

## Risk & Drawdown
- Max drawdown: 52.69% over 1518 days (recovered)
- Annualized: return +0.9%, volatility 13.0% (fraction of booksize)
- Hit rate: 53.3% positive days
- Tail shape: skew -0.29, excess kurtosis +0.59

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -3.28, max 2.39, latest -0.37

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +8.72%; worst month: -10.71%
Positive months: 51%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=1.53
- Sideways: S=1.02
- Bear: S=-2.47

## Negated Direction
Best negated: `rank(-1 * ts_delta(option_breakeven_20, 5))` S=0.87, F=0.33, INFERIOR
Direction gap: +0.43 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * option_breakeven_20)`: S=-0.07, F=-0.02, T=2.9%, INFERIOR (TOP3000)
- `rank(-1 * option_breakeven_20 / close)`: S=-0.14, F=-0.03, T=21.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(option_breakeven_20, 5))`: S=0.87, F=0.33, T=38.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(option_breakeven_20)` | TOP3000 | 0.07 | 0.02 | 52.7% | 60% | bull-only |

## Correlation Notes
Top correlates:
- option_breakeven_10: 1.000 (strongly positively correlated)
- option_breakeven_30: 1.000 (strongly positively correlated)
- option_breakeven_60: 1.000 (strongly positively correlated)
- call_breakeven_10: 1.000 (strongly positively correlated)
- call_breakeven_20: 1.000 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
