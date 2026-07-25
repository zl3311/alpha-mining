---
field: put_breakeven_270
dataset: option9
best_template: rank_neg_delta
best_sharpe: 1.13
best_fitness: 0.47
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 21
regime_profile: bull-only
n_variations_with_pnl: 1
max_drawdown: 0.5436
ann_vol: 0.1386
hit_rate: 0.5336
rolling_sharpe_min: -3.281
rolling_sharpe_max: 2.44
negated_best_sharpe: 1.13
negated_best_template: rank_neg_delta
negated_best_fitness: 0.47
n_negated_sims: 4
direction_gap: 0.63
---
# put_breakeven_270 (option9)

*Weighted mean breakeven price of put options expiring in 270 days indicating the break even price for put buyers based on recent bids and asks*

## Signal Profile
- `rank(put_breakeven_270)`: S=0.10, F=0.03, T=3.5%, INFERIOR (TOP3000)
- `rank(put_breakeven_270 / close)`: S=0.34, F=0.18, T=11.0%, INFERIOR (TOP3000)
- `rank(ts_delta(put_breakeven_270, 5))`: S=-0.88, F=-0.42, T=37.2%, INFERIOR (TOP200)
- `-rank(put_breakeven_270)`: S=0.04, F=0.01, T=3.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(put_breakeven_270, 5))`: S=1.13, F=0.47, T=40.2%, INFERIOR (TOP3000)
- `-ts_zscore(put_breakeven_270, 63)`: S=0.50, F=0.27, T=15.9%, INFERIOR (TOP3000)
- `ts_mean(put_breakeven_270, 10)`: S=0.23, F=0.10, T=1.5%, INFERIOR (TOP3000)
- `rank(ts_rank(put_breakeven_270, 22))`: S=-0.87, F=-0.46, T=24.4%, INFERIOR (TOP3000)
- `rank(-1 * put_breakeven_270)`: S=-0.10, F=-0.03, T=3.5%, INFERIOR (TOP3000)
- `rank(-1 * put_breakeven_270 / close)`: S=-0.39, F=-0.20, T=12.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 20F/1P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 21F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/5P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.10, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.50 (moderate), ret=+4.1%
  - 2020: S=-1.97 (negative), ret=-25.0%
  - 2021: S=0.52 (moderate), ret=+8.0%
  - 2022: S=1.28 (moderate), ret=+21.7%
  - 2023: S=-0.16 (negative), ret=-2.2%

## Risk & Drawdown
- Max drawdown: 54.36% over 1498 days (recovered)
- Annualized: return +1.3%, volatility 13.9% (fraction of booksize)
- Hit rate: 53.4% positive days
- Tail shape: skew -0.23, excess kurtosis +0.47

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -3.28, max 2.44, latest -0.37

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +9.52%; worst month: -11.33%
Positive months: 51%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=1.66
- Sideways: S=1.02
- Bear: S=-2.57

## Negated Direction
Best negated: `rank(-1 * ts_delta(put_breakeven_270, 5))` S=1.13, F=0.47, INFERIOR
Direction gap: +0.63 (negated - positive best Sharpe). NEGATION DOMINANT — field is significantly stronger when reversed.

Negated template variants:
- `rank(-1 * put_breakeven_270)`: S=-0.10, F=-0.03, T=3.5%, INFERIOR (TOP3000)
- `rank(-1 * put_breakeven_270 / close)`: S=-0.39, F=-0.20, T=12.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(put_breakeven_270, 5))`: S=1.13, F=0.47, T=40.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(put_breakeven_270)` | TOP3000 | 0.10 | 0.03 | 54.4% | 60% | bull-only |

## Correlation Notes
Top correlates:
- put_breakeven_360: 1.000 (strongly positively correlated)
- put_breakeven_180: 1.000 (strongly positively correlated)
- put_breakeven_150: 1.000 (strongly positively correlated)
- put_breakeven_120: 1.000 (strongly positively correlated)
- put_breakeven_720: 1.000 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
