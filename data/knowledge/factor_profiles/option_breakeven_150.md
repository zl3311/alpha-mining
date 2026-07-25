---
field: option_breakeven_150
dataset: option9
best_template: rank_neg_delta
best_sharpe: 1.23
best_fitness: 0.56
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 21
regime_profile: bull-only
n_variations_with_pnl: 1
max_drawdown: 0.5038
ann_vol: 0.1247
hit_rate: 0.532
rolling_sharpe_min: -3.225
rolling_sharpe_max: 2.443
negated_best_sharpe: 1.23
negated_best_template: rank_neg_delta
negated_best_fitness: 0.56
n_negated_sims: 4
direction_gap: 0.76
---
# option_breakeven_150 (option9)

*Price at which a stock's options with expiration 150 days in the future break even based on its recent bid/ask mean*

## Signal Profile
- `rank(option_breakeven_150)`: S=0.09, F=0.03, T=2.9%, INFERIOR (TOP3000)
- `rank(option_breakeven_150 / close)`: S=0.03, F=0.00, T=10.1%, INFERIOR (TOP3000)
- `rank(ts_delta(option_breakeven_150, 5))`: S=-1.09, F=-0.51, T=33.6%, INFERIOR (TOP1000)
- `-rank(option_breakeven_150)`: S=0.06, F=0.01, T=3.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(option_breakeven_150, 5))`: S=1.23, F=0.56, T=35.7%, INFERIOR (TOP3000)
- `-ts_zscore(option_breakeven_150, 63)`: S=0.47, F=0.26, T=13.3%, INFERIOR (TOP3000)
- `ts_mean(option_breakeven_150, 10)`: S=0.28, F=0.14, T=1.5%, INFERIOR (TOP3000)
- `rank(ts_rank(option_breakeven_150, 22))`: S=-0.53, F=-0.23, T=21.7%, INFERIOR (TOP3000)
- `rank(-1 * option_breakeven_150)`: S=-0.09, F=-0.03, T=2.9%, INFERIOR (TOP3000)
- `rank(-1 * option_breakeven_150 / close)`: S=-0.12, F=-0.04, T=10.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 20F/1P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 21F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/6P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.09, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.56 (moderate), ret=+4.3%
  - 2020: S=-1.80 (negative), ret=-22.0%
  - 2021: S=0.47 (weak), ret=+6.1%
  - 2022: S=1.27 (moderate), ret=+18.9%
  - 2023: S=-0.14 (negative), ret=-1.7%

## Risk & Drawdown
- Max drawdown: 50.38% over 1507 days (recovered)
- Annualized: return +1.1%, volatility 12.5% (fraction of booksize)
- Hit rate: 53.2% positive days
- Tail shape: skew -0.29, excess kurtosis +0.58

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -3.23, max 2.44, latest -0.36

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +8.51%; worst month: -10.52%
Positive months: 51%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=1.52
- Sideways: S=1.04
- Bear: S=-2.41

## Negated Direction
Best negated: `rank(-1 * ts_delta(option_breakeven_150, 5))` S=1.23, F=0.56, INFERIOR
Direction gap: +0.76 (negated - positive best Sharpe). NEGATION DOMINANT — field is significantly stronger when reversed.

Negated template variants:
- `rank(-1 * option_breakeven_150)`: S=-0.09, F=-0.03, T=2.9%, INFERIOR (TOP3000)
- `rank(-1 * option_breakeven_150 / close)`: S=-0.12, F=-0.04, T=10.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(option_breakeven_150, 5))`: S=1.23, F=0.56, T=35.7%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(option_breakeven_150)` | TOP3000 | 0.09 | 0.03 | 50.4% | 60% | bull-only |

## Correlation Notes
Top correlates:
- option_breakeven_120: 1.000 (strongly positively correlated)
- option_breakeven_180: 1.000 (strongly positively correlated)
- option_breakeven_90: 1.000 (strongly positively correlated)
- option_breakeven_60: 0.999 (strongly positively correlated)
- call_breakeven_30: 0.999 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
