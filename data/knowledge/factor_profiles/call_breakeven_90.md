---
field: call_breakeven_90
dataset: option9
best_template: rank_neg_delta
best_sharpe: 1.11
best_fitness: 0.51
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 21
regime_profile: bull-only
n_variations_with_pnl: 1
max_drawdown: 0.4904
ann_vol: 0.1199
hit_rate: 0.532
rolling_sharpe_min: -3.222
rolling_sharpe_max: 2.463
negated_best_sharpe: 1.11
negated_best_template: rank_neg_delta
negated_best_fitness: 0.51
n_negated_sims: 4
direction_gap: 0.52
---
# call_breakeven_90 (option9)

*Price at which a stock's call options with expiration 90 days in the future break even based on its recent bid/ask mean*

## Signal Profile
- `rank(call_breakeven_90)`: S=0.10, F=0.03, T=2.9%, INFERIOR (TOP3000)
- `rank(call_breakeven_90 / close)`: S=0.28, F=0.18, T=10.4%, INFERIOR (TOP3000)
- `rank(ts_delta(call_breakeven_90, 5))`: S=-0.84, F=-0.38, T=34.4%, INFERIOR (TOP500)
- `-rank(call_breakeven_90)`: S=0.04, F=0.01, T=2.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(call_breakeven_90, 5))`: S=1.11, F=0.51, T=37.3%, INFERIOR (TOP3000)
- `-ts_zscore(call_breakeven_90, 63)`: S=0.59, F=0.39, T=13.8%, INFERIOR (TOP3000)
- `ts_mean(call_breakeven_90, 10)`: S=0.33, F=0.17, T=1.4%, INFERIOR (TOP3000)
- `rank(ts_rank(call_breakeven_90, 22))`: S=-0.77, F=-0.41, T=23.4%, INFERIOR (TOP3000)
- `rank(-1 * call_breakeven_90)`: S=-0.10, F=-0.03, T=2.9%, INFERIOR (TOP3000)
- `rank(-1 * call_breakeven_90 / close)`: S=-0.23, F=-0.13, T=11.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 20F/1P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 21F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/6P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.10, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.59 (moderate), ret=+4.4%
  - 2020: S=-1.75 (negative), ret=-20.8%
  - 2021: S=0.42 (weak), ret=+5.3%
  - 2022: S=1.29 (moderate), ret=+18.1%
  - 2023: S=-0.07 (negative), ret=-0.8%

## Risk & Drawdown
- Max drawdown: 49.04% over 1507 days (recovered)
- Annualized: return +1.2%, volatility 12.0% (fraction of booksize)
- Hit rate: 53.2% positive days
- Tail shape: skew -0.27, excess kurtosis +0.53

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -3.22, max 2.46, latest -0.29

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +8.20%; worst month: -10.14%
Positive months: 51%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=1.54
- Sideways: S=1.07
- Bear: S=-2.37

## Negated Direction
Best negated: `rank(-1 * ts_delta(call_breakeven_90, 5))` S=1.11, F=0.51, INFERIOR
Direction gap: +0.52 (negated - positive best Sharpe). NEGATION DOMINANT — field is significantly stronger when reversed.

Negated template variants:
- `rank(-1 * call_breakeven_90)`: S=-0.10, F=-0.03, T=2.9%, INFERIOR (TOP3000)
- `rank(-1 * call_breakeven_90 / close)`: S=-0.23, F=-0.13, T=11.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(call_breakeven_90, 5))`: S=1.11, F=0.51, T=37.3%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(call_breakeven_90)` | TOP3000 | 0.10 | 0.03 | 49.0% | 60% | bull-only |

## Correlation Notes
Top correlates:
- call_breakeven_120: 1.000 (strongly positively correlated)
- call_breakeven_60: 1.000 (strongly positively correlated)
- call_breakeven_150: 1.000 (strongly positively correlated)
- call_breakeven_180: 0.999 (strongly positively correlated)
- option_breakeven_90: 0.999 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
