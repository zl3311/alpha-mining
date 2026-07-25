---
field: put_breakeven_120
dataset: option9
best_template: rank_neg_delta
best_sharpe: 1.25
best_fitness: 0.59
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_FITNESS
n_sims: 21
regime_profile: bull-only
n_variations_with_pnl: 1
max_drawdown: 0.5388
ann_vol: 0.1371
hit_rate: 0.536
rolling_sharpe_min: -3.276
rolling_sharpe_max: 2.44
negated_best_sharpe: 1.25
negated_best_template: rank_neg_delta
negated_best_fitness: 0.59
n_negated_sims: 4
direction_gap: 0.57
---
# put_breakeven_120 (option9)

*Price at which a stock's put options with expiration 120 days in the future break even based on its recent bid/ask mean*

## Signal Profile
- `rank(put_breakeven_120)`: S=0.10, F=0.03, T=3.2%, INFERIOR (TOP3000)
- `rank(put_breakeven_120 / close)`: S=0.32, F=0.16, T=10.5%, INFERIOR (TOP3000)
- `rank(ts_delta(put_breakeven_120, 5))`: S=-0.81, F=-0.40, T=33.2%, INFERIOR (TOP200)
- `-rank(put_breakeven_120)`: S=0.06, F=0.01, T=3.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(put_breakeven_120, 5))`: S=1.25, F=0.59, T=38.1%, INFERIOR (TOP3000)
- `-ts_zscore(put_breakeven_120, 63)`: S=0.68, F=0.49, T=13.9%, INFERIOR (TOP3000)
- `ts_mean(put_breakeven_120, 10)`: S=0.25, F=0.12, T=1.4%, INFERIOR (TOP3000)
- `rank(ts_rank(put_breakeven_120, 22))`: S=-0.92, F=-0.54, T=23.0%, INFERIOR (TOP3000)
- `rank(-1 * put_breakeven_120)`: S=-0.10, F=-0.03, T=3.2%, INFERIOR (TOP3000)
- `rank(-1 * put_breakeven_120 / close)`: S=-0.56, F=-0.34, T=12.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 20F/1P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 20F/1P
- LOW_SUB_UNIVERSE_SHARPE: 15F/4P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.10, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.56 (moderate), ret=+4.5%
  - 2020: S=-1.95 (negative), ret=-24.8%
  - 2021: S=0.52 (moderate), ret=+7.7%
  - 2022: S=1.28 (moderate), ret=+21.5%
  - 2023: S=-0.17 (negative), ret=-2.2%

## Risk & Drawdown
- Max drawdown: 53.88% over 1498 days (recovered)
- Annualized: return +1.4%, volatility 13.7% (fraction of booksize)
- Hit rate: 53.6% positive days
- Tail shape: skew -0.24, excess kurtosis +0.49

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -3.28, max 2.44, latest -0.38

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +9.37%; worst month: -11.41%
Positive months: 51%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=1.65
- Sideways: S=1.04
- Bear: S=-2.55

## Negated Direction
Best negated: `rank(-1 * ts_delta(put_breakeven_120, 5))` S=1.25, F=0.59, INFERIOR
Direction gap: +0.57 (negated - positive best Sharpe). NEGATION DOMINANT — field is significantly stronger when reversed.

Negated template variants:
- `rank(-1 * put_breakeven_120)`: S=-0.10, F=-0.03, T=3.2%, INFERIOR (TOP3000)
- `rank(-1 * put_breakeven_120 / close)`: S=-0.56, F=-0.34, T=12.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(put_breakeven_120, 5))`: S=1.25, F=0.59, T=38.1%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(put_breakeven_120)` | TOP3000 | 0.10 | 0.03 | 53.9% | 60% | bull-only |

## Correlation Notes
Top correlates:
- put_breakeven_150: 1.000 (strongly positively correlated)
- put_breakeven_90: 1.000 (strongly positively correlated)
- put_breakeven_180: 1.000 (strongly positively correlated)
- put_breakeven_60: 1.000 (strongly positively correlated)
- put_breakeven_270: 1.000 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_FITNESS. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
