---
field: put_breakeven_720
dataset: option9
best_template: rank_neg_delta
best_sharpe: 1.03
best_fitness: 0.41
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 21
regime_profile: bull-only
n_variations_with_pnl: 1
max_drawdown: 0.5508
ann_vol: 0.1398
hit_rate: 0.5296
rolling_sharpe_min: -3.316
rolling_sharpe_max: 2.435
negated_best_sharpe: 1.03
negated_best_template: rank_neg_delta
negated_best_fitness: 0.41
n_negated_sims: 4
direction_gap: 0.64
---
# put_breakeven_720 (option9)

*Weighted mean breakeven price of put options expiring in 720 days indicating the put buyers break-even price based on recent bid/ask*

## Signal Profile
- `rank(put_breakeven_720)`: S=0.09, F=0.03, T=3.5%, INFERIOR (TOP3000)
- `rank(put_breakeven_720 / close)`: S=0.30, F=0.15, T=8.9%, INFERIOR (TOP3000)
- `rank(ts_delta(put_breakeven_720, 5))`: S=-0.76, F=-0.35, T=37.1%, INFERIOR (TOP200)
- `-rank(put_breakeven_720)`: S=0.04, F=0.01, T=3.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(put_breakeven_720, 5))`: S=1.03, F=0.41, T=41.1%, INFERIOR (TOP3000)
- `-ts_zscore(put_breakeven_720, 63)`: S=0.39, F=0.19, T=15.5%, INFERIOR (TOP3000)
- `ts_mean(put_breakeven_720, 10)`: S=0.25, F=0.12, T=1.5%, INFERIOR (TOP3000)
- `rank(ts_rank(put_breakeven_720, 22))`: S=-0.81, F=-0.42, T=25.1%, INFERIOR (TOP3000)
- `rank(-1 * put_breakeven_720)`: S=-0.09, F=-0.03, T=3.5%, INFERIOR (TOP3000)
- `rank(-1 * put_breakeven_720 / close)`: S=-0.34, F=-0.16, T=11.0%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 20F/1P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 21F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/5P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.09, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.50 (moderate), ret=+4.1%
  - 2020: S=-2.01 (negative), ret=-25.7%
  - 2021: S=0.52 (moderate), ret=+8.0%
  - 2022: S=1.30 (moderate), ret=+22.3%
  - 2023: S=-0.19 (negative), ret=-2.6%

## Risk & Drawdown
- Max drawdown: 55.08% over 1498 days (recovered)
- Annualized: return +1.2%, volatility 14.0% (fraction of booksize)
- Hit rate: 53.0% positive days
- Tail shape: skew -0.23, excess kurtosis +0.47

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -3.32, max 2.44, latest -0.40

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +9.59%; worst month: -11.51%
Positive months: 51%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=1.68
- Sideways: S=0.98
- Bear: S=-2.58

## Negated Direction
Best negated: `rank(-1 * ts_delta(put_breakeven_720, 5))` S=1.03, F=0.41, INFERIOR
Direction gap: +0.64 (negated - positive best Sharpe). NEGATION DOMINANT — field is significantly stronger when reversed.

Negated template variants:
- `rank(-1 * put_breakeven_720)`: S=-0.09, F=-0.03, T=3.5%, INFERIOR (TOP3000)
- `rank(-1 * put_breakeven_720 / close)`: S=-0.34, F=-0.16, T=11.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(put_breakeven_720, 5))`: S=1.03, F=0.41, T=41.1%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(put_breakeven_720)` | TOP3000 | 0.09 | 0.03 | 55.1% | 60% | bull-only |

## Correlation Notes
Top correlates:
- put_breakeven_1080: 1.000 (strongly positively correlated)
- put_breakeven_360: 1.000 (strongly positively correlated)
- put_breakeven_270: 1.000 (strongly positively correlated)
- put_breakeven_180: 1.000 (strongly positively correlated)
- put_breakeven_150: 0.999 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
