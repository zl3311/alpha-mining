---
field: call_breakeven_30
dataset: option9
best_template: rank_neg_delta
best_sharpe: 0.97
best_fitness: 0.41
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 21
regime_profile: bull-only
n_variations_with_pnl: 1
max_drawdown: 0.5135
ann_vol: 0.1257
hit_rate: 0.5336
rolling_sharpe_min: -3.264
rolling_sharpe_max: 2.393
negated_best_sharpe: 0.97
negated_best_template: rank_neg_delta
negated_best_fitness: 0.41
n_negated_sims: 4
direction_gap: 0.4
---
# call_breakeven_30 (option9)

*Open-interest-weighted average breakeven price of call options expiring in 30 days, representing the price at which call buyers break even*

## Signal Profile
- `rank(call_breakeven_30)`: S=0.07, F=0.02, T=3.0%, INFERIOR (TOP3000)
- `rank(call_breakeven_30 / close)`: S=0.34, F=0.21, T=16.7%, INFERIOR (TOP3000)
- `rank(ts_delta(call_breakeven_30, 5))`: S=-0.72, F=-0.30, T=35.7%, INFERIOR (TOP500)
- `-rank(call_breakeven_30)`: S=0.06, F=0.01, T=3.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(call_breakeven_30, 5))`: S=0.97, F=0.41, T=36.6%, INFERIOR (TOP3000)
- `-ts_zscore(call_breakeven_30, 63)`: S=0.57, F=0.37, T=14.5%, INFERIOR (TOP3000)
- `ts_mean(call_breakeven_30, 10)`: S=0.30, F=0.15, T=1.4%, INFERIOR (TOP3000)
- `rank(ts_rank(call_breakeven_30, 22))`: S=-0.80, F=-0.42, T=24.6%, INFERIOR (TOP3000)
- `rank(-1 * call_breakeven_30)`: S=-0.07, F=-0.02, T=3.0%, INFERIOR (TOP3000)
- `rank(-1 * call_breakeven_30 / close)`: S=-0.27, F=-0.13, T=17.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 20F/1P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 21F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/6P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.07, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.54 (moderate), ret=+4.1%
  - 2020: S=-1.81 (negative), ret=-22.3%
  - 2021: S=0.39 (weak), ret=+5.1%
  - 2022: S=1.25 (moderate), ret=+18.9%
  - 2023: S=-0.11 (negative), ret=-1.3%

## Risk & Drawdown
- Max drawdown: 51.35% over 1518 days (recovered)
- Annualized: return +0.9%, volatility 12.6% (fraction of booksize)
- Hit rate: 53.4% positive days
- Tail shape: skew -0.28, excess kurtosis +0.57

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -3.26, max 2.39, latest -0.33

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +8.49%; worst month: -10.34%
Positive months: 51%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=1.50
- Sideways: S=1.04
- Bear: S=-2.42

## Negated Direction
Best negated: `rank(-1 * ts_delta(call_breakeven_30, 5))` S=0.97, F=0.41, INFERIOR
Direction gap: +0.40 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * call_breakeven_30)`: S=-0.07, F=-0.02, T=3.0%, INFERIOR (TOP3000)
- `rank(-1 * call_breakeven_30 / close)`: S=-0.27, F=-0.13, T=17.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(call_breakeven_30, 5))`: S=0.97, F=0.41, T=36.6%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(call_breakeven_30)` | TOP3000 | 0.07 | 0.02 | 51.3% | 60% | bull-only |

## Correlation Notes
Top correlates:
- call_breakeven_20: 1.000 (strongly positively correlated)
- call_breakeven_10: 1.000 (strongly positively correlated)
- call_breakeven_60: 1.000 (strongly positively correlated)
- option_breakeven_60: 1.000 (strongly positively correlated)
- option_breakeven_30: 1.000 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
