---
field: option_breakeven_120
dataset: option9
best_template: rank_neg_delta
best_sharpe: 1.29
best_fitness: 0.61
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_FITNESS
n_sims: 21
regime_profile: bull-only
n_variations_with_pnl: 1
max_drawdown: 0.5053
ann_vol: 0.1249
hit_rate: 0.5304
rolling_sharpe_min: -3.24
rolling_sharpe_max: 2.453
negated_best_sharpe: 1.29
negated_best_template: rank_neg_delta
negated_best_fitness: 0.61
n_negated_sims: 4
direction_gap: 0.63
---
# option_breakeven_120 (option9)

*Weighted mean breakeven price for combined call and put options with expiration 120 days in the future, based on recent bid/ask mid-prices and weighted by open interest or volume*

## Signal Profile
- `rank(option_breakeven_120)`: S=0.09, F=0.03, T=2.9%, INFERIOR (TOP3000)
- `rank(option_breakeven_120 / close)`: S=0.10, F=0.03, T=10.2%, INFERIOR (TOP3000)
- `rank(ts_delta(option_breakeven_120, 5))`: S=-0.74, F=-0.35, T=33.4%, INFERIOR (TOP200)
- `-rank(option_breakeven_120)`: S=0.06, F=0.01, T=3.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(option_breakeven_120, 5))`: S=1.29, F=0.61, T=36.7%, INFERIOR (TOP3000)
- `-ts_zscore(option_breakeven_120, 63)`: S=0.66, F=0.44, T=13.6%, INFERIOR (TOP3000)
- `ts_mean(option_breakeven_120, 10)`: S=0.28, F=0.14, T=1.5%, INFERIOR (TOP3000)
- `rank(ts_rank(option_breakeven_120, 22))`: S=-0.68, F=-0.33, T=22.3%, INFERIOR (TOP3000)
- `rank(-1 * option_breakeven_120)`: S=-0.09, F=-0.03, T=2.9%, INFERIOR (TOP3000)
- `rank(-1 * option_breakeven_120 / close)`: S=-0.14, F=-0.05, T=10.6%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 20F/1P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 20F/1P
- LOW_SUB_UNIVERSE_SHARPE: 11F/8P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.09, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.58 (moderate), ret=+4.4%
  - 2020: S=-1.82 (negative), ret=-22.2%
  - 2021: S=0.48 (weak), ret=+6.4%
  - 2022: S=1.27 (moderate), ret=+18.8%
  - 2023: S=-0.15 (negative), ret=-1.8%

## Risk & Drawdown
- Max drawdown: 50.53% over 1507 days (recovered)
- Annualized: return +1.1%, volatility 12.5% (fraction of booksize)
- Hit rate: 53.0% positive days
- Tail shape: skew -0.28, excess kurtosis +0.57

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -3.24, max 2.45, latest -0.36

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +8.62%; worst month: -10.57%
Positive months: 51%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=1.53
- Sideways: S=1.06
- Bear: S=-2.41

## Negated Direction
Best negated: `rank(-1 * ts_delta(option_breakeven_120, 5))` S=1.29, F=0.61, INFERIOR
Direction gap: +0.63 (negated - positive best Sharpe). NEGATION DOMINANT — field is significantly stronger when reversed.

Negated template variants:
- `rank(-1 * option_breakeven_120)`: S=-0.09, F=-0.03, T=2.9%, INFERIOR (TOP3000)
- `rank(-1 * option_breakeven_120 / close)`: S=-0.14, F=-0.05, T=10.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(option_breakeven_120, 5))`: S=1.29, F=0.61, T=36.7%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(option_breakeven_120)` | TOP3000 | 0.09 | 0.03 | 50.5% | 60% | bull-only |

## Correlation Notes
Top correlates:
- option_breakeven_90: 1.000 (strongly positively correlated)
- option_breakeven_150: 1.000 (strongly positively correlated)
- option_breakeven_60: 1.000 (strongly positively correlated)
- option_breakeven_180: 0.999 (strongly positively correlated)
- call_breakeven_30: 0.999 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_FITNESS. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
