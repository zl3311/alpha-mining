---
field: put_breakeven_20
dataset: option9
best_template: rank_neg_delta
best_sharpe: 1.08
best_fitness: 0.46
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 21
regime_profile: bull-only
n_variations_with_pnl: 1
max_drawdown: 0.5381
ann_vol: 0.1358
hit_rate: 0.5368
rolling_sharpe_min: -3.255
rolling_sharpe_max: 2.408
negated_best_sharpe: 1.08
negated_best_template: rank_neg_delta
negated_best_fitness: 0.46
n_negated_sims: 4
direction_gap: 0.47
---
# put_breakeven_20 (option9)

*Price at which a stock's put options with expiration 20 days in the future break even based on its recent bid/ask mean, weighted by open interest or volume*

## Signal Profile
- `rank(put_breakeven_20)`: S=0.08, F=0.02, T=3.4%, INFERIOR (TOP3000)
- `rank(put_breakeven_20 / close)`: S=0.61, F=0.37, T=19.1%, INFERIOR (TOP3000)
- `rank(ts_delta(put_breakeven_20, 5))`: S=-0.22, F=-0.05, T=37.7%, INFERIOR (TOP200)
- `-rank(put_breakeven_20)`: S=0.05, F=0.01, T=3.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(put_breakeven_20, 5))`: S=1.08, F=0.46, T=39.4%, INFERIOR (TOP3000)
- `-ts_zscore(put_breakeven_20, 63)`: S=0.48, F=0.28, T=15.7%, INFERIOR (TOP3000)
- `ts_mean(put_breakeven_20, 10)`: S=0.26, F=0.12, T=1.5%, INFERIOR (TOP3000)
- `rank(ts_rank(put_breakeven_20, 22))`: S=-0.44, F=-0.17, T=26.0%, INFERIOR (TOP3000)
- `rank(-1 * put_breakeven_20)`: S=-0.08, F=-0.02, T=3.4%, INFERIOR (TOP3000)
- `rank(-1 * put_breakeven_20 / close)`: S=-0.93, F=-0.55, T=19.9%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 20F/1P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 21F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/6P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.08, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.53 (moderate), ret=+4.3%
  - 2020: S=-1.90 (negative), ret=-24.4%
  - 2021: S=0.49 (weak), ret=+7.1%
  - 2022: S=1.24 (moderate), ret=+20.6%
  - 2023: S=-0.17 (negative), ret=-2.2%

## Risk & Drawdown
- Max drawdown: 53.81% over 1507 days (recovered)
- Annualized: return +1.1%, volatility 13.6% (fraction of booksize)
- Hit rate: 53.7% positive days
- Tail shape: skew -0.27, excess kurtosis +0.55

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -3.25, max 2.41, latest -0.38

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +9.28%; worst month: -11.24%
Positive months: 51%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=1.58
- Sideways: S=1.04
- Bear: S=-2.52

## Negated Direction
Best negated: `rank(-1 * ts_delta(put_breakeven_20, 5))` S=1.08, F=0.46, INFERIOR
Direction gap: +0.47 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * put_breakeven_20)`: S=-0.08, F=-0.02, T=3.4%, INFERIOR (TOP3000)
- `rank(-1 * put_breakeven_20 / close)`: S=-0.93, F=-0.55, T=19.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(put_breakeven_20, 5))`: S=1.08, F=0.46, T=39.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(put_breakeven_20)` | TOP3000 | 0.08 | 0.02 | 53.8% | 60% | bull-only |

## Correlation Notes
Top correlates:
- put_breakeven_10: 1.000 (strongly positively correlated)
- put_breakeven_30: 1.000 (strongly positively correlated)
- put_breakeven_60: 1.000 (strongly positively correlated)
- put_breakeven_90: 1.000 (strongly positively correlated)
- put_breakeven_120: 0.999 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
