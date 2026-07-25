---
field: option_breakeven_90
dataset: option9
best_template: rank_neg_delta
best_sharpe: 1.11
best_fitness: 0.47
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 21
regime_profile: bull-only
n_variations_with_pnl: 1
max_drawdown: 0.5061
ann_vol: 0.1257
hit_rate: 0.532
rolling_sharpe_min: -3.233
rolling_sharpe_max: 2.443
negated_best_sharpe: 1.11
negated_best_template: rank_neg_delta
negated_best_fitness: 0.47
n_negated_sims: 4
direction_gap: 0.52
---
# option_breakeven_90 (option9)

*Open-interest-weighted mean breakeven price at which buyers of calls and puts combined break even for options expiring in 90 days*

## Signal Profile
- `rank(option_breakeven_90)`: S=0.10, F=0.03, T=2.9%, INFERIOR (TOP3000)
- `rank(option_breakeven_90 / close)`: S=0.19, F=0.08, T=11.8%, INFERIOR (TOP3000)
- `rank(ts_delta(option_breakeven_90, 5))`: S=-0.56, F=-0.20, T=35.9%, INFERIOR (TOP500)
- `-rank(option_breakeven_90)`: S=0.05, F=0.01, T=3.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(option_breakeven_90, 5))`: S=1.11, F=0.47, T=38.2%, INFERIOR (TOP3000)
- `-ts_zscore(option_breakeven_90, 63)`: S=0.59, F=0.36, T=14.9%, INFERIOR (TOP3000)
- `ts_mean(option_breakeven_90, 10)`: S=0.26, F=0.12, T=1.5%, INFERIOR (TOP3000)
- `rank(ts_rank(option_breakeven_90, 22))`: S=-0.50, F=-0.20, T=23.9%, INFERIOR (TOP3000)
- `rank(-1 * option_breakeven_90)`: S=-0.10, F=-0.03, T=2.9%, INFERIOR (TOP3000)
- `rank(-1 * option_breakeven_90 / close)`: S=-0.19, F=-0.08, T=12.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 20F/1P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 21F/0P
- LOW_SUB_UNIVERSE_SHARPE: 12F/7P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.10, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.58 (moderate), ret=+4.5%
  - 2020: S=-1.81 (negative), ret=-22.2%
  - 2021: S=0.48 (weak), ret=+6.3%
  - 2022: S=1.27 (moderate), ret=+19.0%
  - 2023: S=-0.13 (negative), ret=-1.6%

## Risk & Drawdown
- Max drawdown: 50.61% over 1504 days (recovered)
- Annualized: return +1.2%, volatility 12.6% (fraction of booksize)
- Hit rate: 53.2% positive days
- Tail shape: skew -0.28, excess kurtosis +0.56

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -3.23, max 2.44, latest -0.34

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +8.65%; worst month: -10.58%
Positive months: 51%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=1.56
- Sideways: S=1.06
- Bear: S=-2.41

## Negated Direction
Best negated: `rank(-1 * ts_delta(option_breakeven_90, 5))` S=1.11, F=0.47, INFERIOR
Direction gap: +0.52 (negated - positive best Sharpe). NEGATION DOMINANT — field is significantly stronger when reversed.

Negated template variants:
- `rank(-1 * option_breakeven_90)`: S=-0.10, F=-0.03, T=2.9%, INFERIOR (TOP3000)
- `rank(-1 * option_breakeven_90 / close)`: S=-0.19, F=-0.08, T=12.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(option_breakeven_90, 5))`: S=1.11, F=0.47, T=38.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(option_breakeven_90)` | TOP3000 | 0.10 | 0.03 | 50.6% | 60% | bull-only |

## Correlation Notes
Top correlates:
- option_breakeven_120: 1.000 (strongly positively correlated)
- option_breakeven_60: 1.000 (strongly positively correlated)
- option_breakeven_150: 1.000 (strongly positively correlated)
- call_breakeven_30: 0.999 (strongly positively correlated)
- call_breakeven_60: 0.999 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
