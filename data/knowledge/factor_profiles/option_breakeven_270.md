---
field: option_breakeven_270
dataset: option9
best_template: rank_neg_delta
best_sharpe: 1.18
best_fitness: 0.46
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 21
regime_profile: bull-only
n_variations_with_pnl: 1
max_drawdown: 0.485
ann_vol: 0.1211
hit_rate: 0.5336
rolling_sharpe_min: -3.175
rolling_sharpe_max: 2.512
negated_best_sharpe: 1.18
negated_best_template: rank_neg_delta
negated_best_fitness: 0.46
n_negated_sims: 4
direction_gap: 0.86
---
# option_breakeven_270 (option9)

*The weighted mean price at which buyers of call and put options combined break even at 270 days to expiry based on recent bid/ask prices*

## Signal Profile
- `rank(option_breakeven_270)`: S=0.14, F=0.05, T=3.4%, INFERIOR (TOP3000)
- `rank(option_breakeven_270 / close)`: S=0.32, F=0.17, T=11.2%, INFERIOR (TOP3000)
- `rank(ts_delta(option_breakeven_270, 5))`: S=-0.98, F=-0.39, T=37.5%, INFERIOR (TOP1000)
- `-rank(option_breakeven_270)`: S=-0.01, F=0.00, T=3.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(option_breakeven_270, 5))`: S=1.18, F=0.46, T=39.0%, INFERIOR (TOP3000)
- `-ts_zscore(option_breakeven_270, 63)`: S=0.18, F=0.05, T=16.2%, INFERIOR (TOP3000)
- `ts_mean(option_breakeven_270, 10)`: S=0.31, F=0.16, T=1.7%, INFERIOR (TOP3000)
- `rank(ts_rank(option_breakeven_270, 22))`: S=-0.92, F=-0.45, T=23.9%, INFERIOR (TOP3000)
- `rank(-1 * option_breakeven_270)`: S=-0.14, F=-0.05, T=3.4%, INFERIOR (TOP3000)
- `rank(-1 * option_breakeven_270 / close)`: S=-0.24, F=-0.11, T=11.5%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 20F/1P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 21F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/6P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.15, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.56 (moderate), ret=+4.3%
  - 2020: S=-1.72 (negative), ret=-20.5%
  - 2021: S=0.49 (weak), ret=+6.4%
  - 2022: S=1.34 (moderate), ret=+18.7%
  - 2023: S=-0.02 (negative), ret=-0.3%

## Risk & Drawdown
- Max drawdown: 48.50% over 1337 days (recovered)
- Annualized: return +1.8%, volatility 12.1% (fraction of booksize)
- Hit rate: 53.4% positive days
- Tail shape: skew -0.28, excess kurtosis +0.49

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -3.17, max 2.51, latest -0.24

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +8.43%; worst month: -10.27%
Positive months: 51%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=1.60
- Sideways: S=1.11
- Bear: S=-2.36

## Negated Direction
Best negated: `rank(-1 * ts_delta(option_breakeven_270, 5))` S=1.18, F=0.46, INFERIOR
Direction gap: +0.86 (negated - positive best Sharpe). NEGATION DOMINANT — field is significantly stronger when reversed.

Negated template variants:
- `rank(-1 * option_breakeven_270)`: S=-0.14, F=-0.05, T=3.4%, INFERIOR (TOP3000)
- `rank(-1 * option_breakeven_270 / close)`: S=-0.24, F=-0.11, T=11.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(option_breakeven_270, 5))`: S=1.18, F=0.46, T=39.0%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(option_breakeven_270)` | TOP3000 | 0.15 | 0.05 | 48.5% | 60% | bull-only |

## Correlation Notes
Top correlates:
- option_breakeven_360: 0.999 (strongly positively correlated)
- option_breakeven_720: 0.999 (strongly positively correlated)
- option_breakeven_1080: 0.999 (strongly positively correlated)
- call_breakeven_60: 0.999 (strongly positively correlated)
- call_breakeven_270: 0.999 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
