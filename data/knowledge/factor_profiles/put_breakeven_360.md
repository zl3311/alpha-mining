---
field: put_breakeven_360
dataset: option9
best_template: rank_neg_delta
best_sharpe: 1.04
best_fitness: 0.42
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 21
regime_profile: bull-only
n_variations_with_pnl: 1
max_drawdown: 0.5463
ann_vol: 0.1389
hit_rate: 0.532
rolling_sharpe_min: -3.294
rolling_sharpe_max: 2.439
negated_best_sharpe: 1.04
negated_best_template: rank_neg_delta
negated_best_fitness: 0.42
n_negated_sims: 4
direction_gap: 0.65
---
# put_breakeven_360 (option9)

*Open-interest-weighted mean breakeven price at which buyers of put options break even for options expiring in 360 days*

## Signal Profile
- `rank(put_breakeven_360)`: S=0.10, F=0.03, T=3.5%, INFERIOR (TOP3000)
- `rank(put_breakeven_360 / close)`: S=0.39, F=0.22, T=9.7%, INFERIOR (TOP3000)
- `rank(ts_delta(put_breakeven_360, 5))`: S=-0.52, F=-0.20, T=37.7%, INFERIOR (TOP200)
- `-rank(put_breakeven_360)`: S=0.03, F=0.01, T=3.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(put_breakeven_360, 5))`: S=1.04, F=0.42, T=40.8%, INFERIOR (TOP3000)
- `-ts_zscore(put_breakeven_360, 63)`: S=0.40, F=0.20, T=15.6%, INFERIOR (TOP3000)
- `ts_mean(put_breakeven_360, 10)`: S=0.24, F=0.11, T=1.5%, INFERIOR (TOP3000)
- `rank(ts_rank(put_breakeven_360, 22))`: S=-0.73, F=-0.36, T=24.9%, INFERIOR (TOP3000)
- `rank(-1 * put_breakeven_360)`: S=-0.10, F=-0.03, T=3.5%, INFERIOR (TOP3000)
- `rank(-1 * put_breakeven_360 / close)`: S=-0.40, F=-0.21, T=11.6%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 20F/1P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 21F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/5P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.10, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.50 (moderate), ret=+4.1%
  - 2020: S=-1.98 (negative), ret=-25.1%
  - 2021: S=0.51 (moderate), ret=+7.8%
  - 2022: S=1.29 (moderate), ret=+21.9%
  - 2023: S=-0.17 (negative), ret=-2.2%

## Risk & Drawdown
- Max drawdown: 54.63% over 1337 days (recovered)
- Annualized: return +1.3%, volatility 13.9% (fraction of booksize)
- Hit rate: 53.2% positive days
- Tail shape: skew -0.23, excess kurtosis +0.47

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -3.29, max 2.44, latest -0.38

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +9.54%; worst month: -11.37%
Positive months: 51%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=1.68
- Sideways: S=1.01
- Bear: S=-2.58

## Negated Direction
Best negated: `rank(-1 * ts_delta(put_breakeven_360, 5))` S=1.04, F=0.42, INFERIOR
Direction gap: +0.65 (negated - positive best Sharpe). NEGATION DOMINANT — field is significantly stronger when reversed.

Negated template variants:
- `rank(-1 * put_breakeven_360)`: S=-0.10, F=-0.03, T=3.5%, INFERIOR (TOP3000)
- `rank(-1 * put_breakeven_360 / close)`: S=-0.40, F=-0.21, T=11.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(put_breakeven_360, 5))`: S=1.04, F=0.42, T=40.8%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(put_breakeven_360)` | TOP3000 | 0.10 | 0.03 | 54.6% | 60% | bull-only |

## Correlation Notes
Top correlates:
- put_breakeven_270: 1.000 (strongly positively correlated)
- put_breakeven_720: 1.000 (strongly positively correlated)
- put_breakeven_1080: 1.000 (strongly positively correlated)
- put_breakeven_180: 1.000 (strongly positively correlated)
- put_breakeven_150: 1.000 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
