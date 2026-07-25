---
field: option_breakeven_60
dataset: option9
best_template: rank_neg_delta
best_sharpe: 1.17
best_fitness: 0.47
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 21
regime_profile: bull-only
n_variations_with_pnl: 1
max_drawdown: 0.5172
ann_vol: 0.1275
hit_rate: 0.5328
rolling_sharpe_min: -3.253
rolling_sharpe_max: 2.401
negated_best_sharpe: 1.17
negated_best_template: rank_neg_delta
negated_best_fitness: 0.47
n_negated_sims: 4
direction_gap: 0.59
---
# option_breakeven_60 (option9)

*The weighted mean price at which buyers of call and put options combined break even at 60 days to expiry based on recent bid/ask prices*

## Signal Profile
- `rank(option_breakeven_60)`: S=0.08, F=0.02, T=3.1%, INFERIOR (TOP3000)
- `rank(option_breakeven_60 / close)`: S=0.27, F=0.11, T=17.6%, INFERIOR (TOP3000)
- `rank(ts_delta(option_breakeven_60, 5))`: S=-0.51, F=-0.15, T=39.2%, INFERIOR (TOP500)
- `-rank(option_breakeven_60)`: S=0.05, F=0.01, T=3.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(option_breakeven_60, 5))`: S=1.17, F=0.47, T=39.8%, INFERIOR (TOP3000)
- `-ts_zscore(option_breakeven_60, 63)`: S=0.58, F=0.33, T=17.6%, INFERIOR (TOP3000)
- `ts_mean(option_breakeven_60, 10)`: S=0.26, F=0.12, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_rank(option_breakeven_60, 22))`: S=-0.62, F=-0.25, T=26.2%, INFERIOR (TOP3000)
- `rank(-1 * option_breakeven_60)`: S=-0.08, F=-0.02, T=3.1%, INFERIOR (TOP3000)
- `rank(-1 * option_breakeven_60 / close)`: S=-0.21, F=-0.08, T=17.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 20F/1P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 21F/0P
- LOW_SUB_UNIVERSE_SHARPE: 10F/9P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.08, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.54 (moderate), ret=+4.2%
  - 2020: S=-1.82 (negative), ret=-22.6%
  - 2021: S=0.43 (weak), ret=+5.7%
  - 2022: S=1.25 (moderate), ret=+19.1%
  - 2023: S=-0.12 (negative), ret=-1.6%

## Risk & Drawdown
- Max drawdown: 51.72% over 1508 days (recovered)
- Annualized: return +1.0%, volatility 12.8% (fraction of booksize)
- Hit rate: 53.3% positive days
- Tail shape: skew -0.29, excess kurtosis +0.56

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -3.25, max 2.40, latest -0.34

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +8.72%; worst month: -10.60%
Positive months: 51%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=1.53
- Sideways: S=1.03
- Bear: S=-2.44

## Negated Direction
Best negated: `rank(-1 * ts_delta(option_breakeven_60, 5))` S=1.17, F=0.47, INFERIOR
Direction gap: +0.59 (negated - positive best Sharpe). NEGATION DOMINANT — field is significantly stronger when reversed.

Negated template variants:
- `rank(-1 * option_breakeven_60)`: S=-0.08, F=-0.02, T=3.1%, INFERIOR (TOP3000)
- `rank(-1 * option_breakeven_60 / close)`: S=-0.21, F=-0.08, T=17.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(option_breakeven_60, 5))`: S=1.17, F=0.47, T=39.8%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(option_breakeven_60)` | TOP3000 | 0.08 | 0.02 | 51.7% | 60% | bull-only |

## Correlation Notes
Top correlates:
- option_breakeven_90: 1.000 (strongly positively correlated)
- option_breakeven_30: 1.000 (strongly positively correlated)
- option_breakeven_20: 1.000 (strongly positively correlated)
- option_breakeven_10: 1.000 (strongly positively correlated)
- option_breakeven_120: 1.000 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
