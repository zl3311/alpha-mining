---
field: option_breakeven_180
dataset: option9
best_template: rank_neg_delta
best_sharpe: 0.91
best_fitness: 0.34
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 21
regime_profile: bull-only
n_variations_with_pnl: 1
max_drawdown: 0.5014
ann_vol: 0.1245
hit_rate: 0.5296
rolling_sharpe_min: -3.211
rolling_sharpe_max: 2.428
negated_best_sharpe: 0.91
negated_best_template: rank_neg_delta
negated_best_fitness: 0.34
n_negated_sims: 4
direction_gap: 0.63
---
# option_breakeven_180 (option9)

*Weighted mean break-even price for combined call and put options expiring in 180 days, based on recent bid/ask prices*

## Signal Profile
- `rank(option_breakeven_180)`: S=0.11, F=0.04, T=3.1%, INFERIOR (TOP3000)
- `rank(option_breakeven_180 / close)`: S=0.11, F=0.03, T=11.0%, INFERIOR (TOP3000)
- `rank(ts_delta(option_breakeven_180, 5))`: S=-0.49, F=-0.16, T=33.6%, INFERIOR (TOP500)
- `-rank(option_breakeven_180)`: S=0.04, F=0.01, T=3.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(option_breakeven_180, 5))`: S=0.91, F=0.34, T=36.2%, INFERIOR (TOP3000)
- `-ts_zscore(option_breakeven_180, 63)`: S=0.17, F=0.05, T=14.1%, INFERIOR (TOP3000)
- `ts_mean(option_breakeven_180, 10)`: S=0.28, F=0.13, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_rank(option_breakeven_180, 22))`: S=-0.18, F=-0.04, T=22.1%, INFERIOR (TOP3000)
- `rank(-1 * option_breakeven_180)`: S=-0.11, F=-0.04, T=3.1%, INFERIOR (TOP3000)
- `rank(-1 * option_breakeven_180 / close)`: S=-0.16, F=-0.06, T=11.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 20F/1P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 21F/0P
- LOW_SUB_UNIVERSE_SHARPE: 8F/11P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.11, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.55 (moderate), ret=+4.2%
  - 2020: S=-1.78 (negative), ret=-21.6%
  - 2021: S=0.45 (weak), ret=+5.9%
  - 2022: S=1.33 (moderate), ret=+19.6%
  - 2023: S=-0.12 (negative), ret=-1.4%

## Risk & Drawdown
- Max drawdown: 50.14% over 1500 days (recovered)
- Annualized: return +1.4%, volatility 12.4% (fraction of booksize)
- Hit rate: 53.0% positive days
- Tail shape: skew -0.29, excess kurtosis +0.57

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -3.21, max 2.43, latest -0.33

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +8.36%; worst month: -10.47%
Positive months: 51%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=1.53
- Sideways: S=1.05
- Bear: S=-2.38

## Negated Direction
Best negated: `rank(-1 * ts_delta(option_breakeven_180, 5))` S=0.91, F=0.34, INFERIOR
Direction gap: +0.63 (negated - positive best Sharpe). NEGATION DOMINANT — field is significantly stronger when reversed.

Negated template variants:
- `rank(-1 * option_breakeven_180)`: S=-0.11, F=-0.04, T=3.1%, INFERIOR (TOP3000)
- `rank(-1 * option_breakeven_180 / close)`: S=-0.16, F=-0.06, T=11.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(option_breakeven_180, 5))`: S=0.91, F=0.34, T=36.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(option_breakeven_180)` | TOP3000 | 0.11 | 0.04 | 50.1% | 60% | bull-only |

## Correlation Notes
Top correlates:
- option_breakeven_150: 1.000 (strongly positively correlated)
- option_breakeven_120: 0.999 (strongly positively correlated)
- option_breakeven_90: 0.999 (strongly positively correlated)
- option_breakeven_60: 0.999 (strongly positively correlated)
- call_breakeven_30: 0.999 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
