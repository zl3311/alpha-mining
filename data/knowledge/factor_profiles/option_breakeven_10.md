---
field: option_breakeven_10
dataset: option9
best_template: rank_neg_delta
best_sharpe: 0.84
best_fitness: 0.32
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 21
regime_profile: bull-only
n_variations_with_pnl: 1
max_drawdown: 0.5296
ann_vol: 0.1302
hit_rate: 0.5352
rolling_sharpe_min: -3.286
rolling_sharpe_max: 2.383
negated_best_sharpe: 0.84
negated_best_template: rank_neg_delta
negated_best_fitness: 0.32
n_negated_sims: 4
direction_gap: 0.34
---
# option_breakeven_10 (option9)

*Open-interest-weighted mean breakeven price at which buyers of calls and puts combined break even for options expiring in 10 days*

## Signal Profile
- `rank(option_breakeven_10)`: S=0.06, F=0.02, T=3.0%, INFERIOR (TOP3000)
- `rank(option_breakeven_10 / close)`: S=-0.03, F=0.00, T=22.7%, INFERIOR (TOP3000)
- `rank(ts_delta(option_breakeven_10, 5))`: S=-0.69, F=-0.25, T=38.4%, INFERIOR (TOP1000)
- `-rank(option_breakeven_10)`: S=0.07, F=0.02, T=3.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(option_breakeven_10, 5))`: S=0.84, F=0.32, T=39.4%, INFERIOR (TOP3000)
- `-ts_zscore(option_breakeven_10, 63)`: S=0.50, F=0.29, T=16.1%, INFERIOR (TOP3000)
- `ts_mean(option_breakeven_10, 10)`: S=0.26, F=0.12, T=1.5%, INFERIOR (TOP3000)
- `rank(ts_rank(option_breakeven_10, 22))`: S=-0.63, F=-0.28, T=26.6%, INFERIOR (TOP3000)
- `rank(-1 * option_breakeven_10)`: S=-0.06, F=-0.02, T=3.0%, INFERIOR (TOP3000)
- `rank(-1 * option_breakeven_10 / close)`: S=0.03, F=0.00, T=23.9%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 20F/1P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 21F/0P
- LOW_SUB_UNIVERSE_SHARPE: 12F/7P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.06, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.51 (moderate), ret=+4.0%
  - 2020: S=-1.86 (negative), ret=-23.5%
  - 2021: S=0.41 (weak), ret=+5.6%
  - 2022: S=1.25 (moderate), ret=+19.8%
  - 2023: S=-0.15 (negative), ret=-1.9%

## Risk & Drawdown
- Max drawdown: 52.96% over 1518 days (recovered)
- Annualized: return +0.8%, volatility 13.0% (fraction of booksize)
- Hit rate: 53.5% positive days
- Tail shape: skew -0.29, excess kurtosis +0.59

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -3.29, max 2.38, latest -0.36

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +8.73%; worst month: -10.69%
Positive months: 51%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=1.53
- Sideways: S=1.02
- Bear: S=-2.48

## Negated Direction
Best negated: `rank(-1 * ts_delta(option_breakeven_10, 5))` S=0.84, F=0.32, INFERIOR
Direction gap: +0.34 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * option_breakeven_10)`: S=-0.06, F=-0.02, T=3.0%, INFERIOR (TOP3000)
- `rank(-1 * option_breakeven_10 / close)`: S=0.03, F=0.00, T=23.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(option_breakeven_10, 5))`: S=0.84, F=0.32, T=39.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(option_breakeven_10)` | TOP3000 | 0.06 | 0.02 | 53.0% | 60% | bull-only |

## Correlation Notes
Top correlates:
- option_breakeven_20: 1.000 (strongly positively correlated)
- option_breakeven_30: 1.000 (strongly positively correlated)
- option_breakeven_60: 1.000 (strongly positively correlated)
- call_breakeven_10: 1.000 (strongly positively correlated)
- call_breakeven_20: 1.000 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
