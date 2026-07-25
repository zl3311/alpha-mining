---
field: option_breakeven_720
dataset: option9
best_template: rank_neg_delta
best_sharpe: 1.04
best_fitness: 0.39
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 21
regime_profile: bull-only
n_variations_with_pnl: 1
max_drawdown: 0.4836
ann_vol: 0.1193
hit_rate: 0.5328
rolling_sharpe_min: -3.178
rolling_sharpe_max: 2.482
negated_best_sharpe: 1.04
negated_best_template: rank_neg_delta
negated_best_fitness: 0.39
n_negated_sims: 4
direction_gap: 0.72
---
# option_breakeven_720 (option9)

*Price at which a stock's options with expiration 720 days in the future break even based on its recent bid/ask mean*

## Signal Profile
- `rank(option_breakeven_720)`: S=0.13, F=0.04, T=3.4%, INFERIOR (TOP3000)
- `rank(option_breakeven_720 / close)`: S=0.20, F=0.08, T=9.1%, INFERIOR (TOP3000)
- `rank(ts_delta(option_breakeven_720, 5))`: S=-0.40, F=-0.13, T=36.7%, INFERIOR (TOP200)
- `-rank(option_breakeven_720)`: S=0.01, F=0.00, T=3.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(option_breakeven_720, 5))`: S=1.04, F=0.39, T=39.6%, INFERIOR (TOP3000)
- `-ts_zscore(option_breakeven_720, 63)`: S=0.13, F=0.03, T=15.3%, INFERIOR (TOP3000)
- `ts_mean(option_breakeven_720, 10)`: S=0.32, F=0.16, T=1.7%, INFERIOR (TOP3000)
- `rank(ts_rank(option_breakeven_720, 22))`: S=-0.42, F=-0.15, T=24.0%, INFERIOR (TOP3000)
- `rank(-1 * option_breakeven_720)`: S=-0.13, F=-0.04, T=3.4%, INFERIOR (TOP3000)
- `rank(-1 * option_breakeven_720 / close)`: S=-0.09, F=-0.03, T=10.5%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 20F/1P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 21F/0P
- LOW_SUB_UNIVERSE_SHARPE: 12F/7P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.13, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.56 (moderate), ret=+4.2%
  - 2020: S=-1.69 (negative), ret=-20.0%
  - 2021: S=0.42 (weak), ret=+5.4%
  - 2022: S=1.36 (moderate), ret=+18.3%
  - 2023: S=-0.04 (negative), ret=-0.5%

## Risk & Drawdown
- Max drawdown: 48.36% over 1498 days (recovered)
- Annualized: return +1.5%, volatility 11.9% (fraction of booksize)
- Hit rate: 53.3% positive days
- Tail shape: skew -0.27, excess kurtosis +0.47

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -3.18, max 2.48, latest -0.26

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +8.23%; worst month: -10.08%
Positive months: 51%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=1.59
- Sideways: S=1.08
- Bear: S=-2.38

## Negated Direction
Best negated: `rank(-1 * ts_delta(option_breakeven_720, 5))` S=1.04, F=0.39, INFERIOR
Direction gap: +0.72 (negated - positive best Sharpe). NEGATION DOMINANT — field is significantly stronger when reversed.

Negated template variants:
- `rank(-1 * option_breakeven_720)`: S=-0.13, F=-0.04, T=3.4%, INFERIOR (TOP3000)
- `rank(-1 * option_breakeven_720 / close)`: S=-0.09, F=-0.03, T=10.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(option_breakeven_720, 5))`: S=1.04, F=0.39, T=39.6%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(option_breakeven_720)` | TOP3000 | 0.13 | 0.04 | 48.4% | 60% | bull-only |

## Correlation Notes
Top correlates:
- option_breakeven_1080: 1.000 (strongly positively correlated)
- option_breakeven_360: 0.999 (strongly positively correlated)
- option_breakeven_270: 0.999 (strongly positively correlated)
- call_breakeven_1080: 0.999 (strongly positively correlated)
- call_breakeven_720: 0.999 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
