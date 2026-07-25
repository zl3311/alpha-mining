---
field: put_breakeven_60
dataset: option9
best_template: rank_neg_delta
best_sharpe: 1.3
best_fitness: 0.57
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_FITNESS
n_sims: 21
regime_profile: bull-only
n_variations_with_pnl: 1
max_drawdown: 0.5396
ann_vol: 0.1365
hit_rate: 0.536
rolling_sharpe_min: -3.268
rolling_sharpe_max: 2.426
negated_best_sharpe: 1.3
negated_best_template: rank_neg_delta
negated_best_fitness: 0.57
n_negated_sims: 4
direction_gap: 0.77
---
# put_breakeven_60 (option9)

*Price at which a stock's put options with expiration 60 days in the future break even based on its recent bid/ask mean, weighted by open interest or volume*

## Signal Profile
- `rank(put_breakeven_60)`: S=0.09, F=0.03, T=3.4%, INFERIOR (TOP3000)
- `rank(put_breakeven_60 / close)`: S=0.47, F=0.26, T=15.8%, INFERIOR (TOP3000)
- `rank(ts_delta(put_breakeven_60, 5))`: S=-0.53, F=-0.19, T=36.9%, INFERIOR (TOP200)
- `-rank(put_breakeven_60)`: S=0.04, F=0.01, T=3.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(put_breakeven_60, 5))`: S=1.30, F=0.57, T=39.2%, INFERIOR (TOP3000)
- `-ts_zscore(put_breakeven_60, 63)`: S=0.53, F=0.30, T=16.5%, INFERIOR (TOP3000)
- `ts_mean(put_breakeven_60, 10)`: S=0.26, F=0.12, T=1.5%, INFERIOR (TOP3000)
- `rank(ts_rank(put_breakeven_60, 22))`: S=-0.73, F=-0.34, T=25.4%, INFERIOR (TOP3000)
- `rank(-1 * put_breakeven_60)`: S=-0.09, F=-0.03, T=3.4%, INFERIOR (TOP3000)
- `rank(-1 * put_breakeven_60 / close)`: S=-0.63, F=-0.35, T=16.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 20F/1P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 20F/1P
- LOW_SUB_UNIVERSE_SHARPE: 15F/4P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.09, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.54 (moderate), ret=+4.3%
  - 2020: S=-1.94 (negative), ret=-24.8%
  - 2021: S=0.52 (moderate), ret=+7.6%
  - 2022: S=1.26 (moderate), ret=+21.1%
  - 2023: S=-0.17 (negative), ret=-2.2%

## Risk & Drawdown
- Max drawdown: 53.96% over 1504 days (recovered)
- Annualized: return +1.2%, volatility 13.7% (fraction of booksize)
- Hit rate: 53.6% positive days
- Tail shape: skew -0.25, excess kurtosis +0.52

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -3.27, max 2.43, latest -0.38

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +9.31%; worst month: -11.36%
Positive months: 51%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=1.61
- Sideways: S=1.03
- Bear: S=-2.53

## Negated Direction
Best negated: `rank(-1 * ts_delta(put_breakeven_60, 5))` S=1.30, F=0.57, INFERIOR
Direction gap: +0.77 (negated - positive best Sharpe). NEGATION DOMINANT — field is significantly stronger when reversed.

Negated template variants:
- `rank(-1 * put_breakeven_60)`: S=-0.09, F=-0.03, T=3.4%, INFERIOR (TOP3000)
- `rank(-1 * put_breakeven_60 / close)`: S=-0.63, F=-0.35, T=16.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(put_breakeven_60, 5))`: S=1.30, F=0.57, T=39.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(put_breakeven_60)` | TOP3000 | 0.09 | 0.03 | 54.0% | 60% | bull-only |

## Correlation Notes
Top correlates:
- put_breakeven_90: 1.000 (strongly positively correlated)
- put_breakeven_30: 1.000 (strongly positively correlated)
- put_breakeven_120: 1.000 (strongly positively correlated)
- put_breakeven_20: 1.000 (strongly positively correlated)
- put_breakeven_150: 1.000 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_FITNESS. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
