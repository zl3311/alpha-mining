---
field: call_breakeven_120
dataset: option9
best_template: rank_neg_delta
best_sharpe: 1.18
best_fitness: 0.57
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 21
regime_profile: bull-only
n_variations_with_pnl: 1
max_drawdown: 0.4884
ann_vol: 0.1191
hit_rate: 0.5304
rolling_sharpe_min: -3.223
rolling_sharpe_max: 2.47
negated_best_sharpe: 1.18
negated_best_template: rank_neg_delta
negated_best_fitness: 0.57
n_negated_sims: 4
direction_gap: 0.54
---
# call_breakeven_120 (option9)

*Price at which a stock's call options with expiration 120 days in the future break even based on its recent bid/ask mean, weighted by open interest or volume*

## Signal Profile
- `rank(call_breakeven_120)`: S=0.10, F=0.03, T=2.9%, INFERIOR (TOP3000)
- `rank(call_breakeven_120 / close)`: S=0.25, F=0.15, T=9.6%, INFERIOR (TOP3000)
- `rank(ts_delta(call_breakeven_120, 5))`: S=-0.86, F=-0.41, T=33.4%, INFERIOR (TOP500)
- `-rank(call_breakeven_120)`: S=0.05, F=0.01, T=2.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(call_breakeven_120, 5))`: S=1.18, F=0.57, T=36.5%, INFERIOR (TOP3000)
- `-ts_zscore(call_breakeven_120, 63)`: S=0.64, F=0.45, T=13.1%, INFERIOR (TOP3000)
- `ts_mean(call_breakeven_120, 10)`: S=0.34, F=0.18, T=1.3%, INFERIOR (TOP3000)
- `rank(ts_rank(call_breakeven_120, 22))`: S=-0.73, F=-0.39, T=22.5%, INFERIOR (TOP3000)
- `rank(-1 * call_breakeven_120)`: S=-0.10, F=-0.03, T=2.9%, INFERIOR (TOP3000)
- `rank(-1 * call_breakeven_120 / close)`: S=-0.22, F=-0.12, T=10.6%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 20F/1P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 21F/0P
- LOW_SUB_UNIVERSE_SHARPE: 11F/8P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.10, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.59 (moderate), ret=+4.3%
  - 2020: S=-1.75 (negative), ret=-20.8%
  - 2021: S=0.42 (weak), ret=+5.3%
  - 2022: S=1.29 (moderate), ret=+17.8%
  - 2023: S=-0.08 (negative), ret=-0.9%

## Risk & Drawdown
- Max drawdown: 48.84% over 1507 days (recovered)
- Annualized: return +1.2%, volatility 11.9% (fraction of booksize)
- Hit rate: 53.0% positive days
- Tail shape: skew -0.27, excess kurtosis +0.54

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -3.22, max 2.47, latest -0.30

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +8.12%; worst month: -10.19%
Positive months: 51%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=1.51
- Sideways: S=1.07
- Bear: S=-2.36

## Negated Direction
Best negated: `rank(-1 * ts_delta(call_breakeven_120, 5))` S=1.18, F=0.57, INFERIOR
Direction gap: +0.54 (negated - positive best Sharpe). NEGATION DOMINANT — field is significantly stronger when reversed.

Negated template variants:
- `rank(-1 * call_breakeven_120)`: S=-0.10, F=-0.03, T=2.9%, INFERIOR (TOP3000)
- `rank(-1 * call_breakeven_120 / close)`: S=-0.22, F=-0.12, T=10.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(call_breakeven_120, 5))`: S=1.18, F=0.57, T=36.5%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(call_breakeven_120)` | TOP3000 | 0.10 | 0.03 | 48.8% | 60% | bull-only |

## Correlation Notes
Top correlates:
- call_breakeven_90: 1.000 (strongly positively correlated)
- call_breakeven_150: 1.000 (strongly positively correlated)
- call_breakeven_60: 0.999 (strongly positively correlated)
- call_breakeven_180: 0.999 (strongly positively correlated)
- option_breakeven_120: 0.999 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
