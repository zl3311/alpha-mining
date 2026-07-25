---
field: put_breakeven_180
dataset: option9
best_template: rank_neg_delta
best_sharpe: 1.2
best_fitness: 0.53
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 21
regime_profile: bull-only
n_variations_with_pnl: 1
max_drawdown: 0.5427
ann_vol: 0.1382
hit_rate: 0.5344
rolling_sharpe_min: -3.264
rolling_sharpe_max: 2.435
negated_best_sharpe: 1.2
negated_best_template: rank_neg_delta
negated_best_fitness: 0.53
n_negated_sims: 4
direction_gap: 0.68
---
# put_breakeven_180 (option9)

*Weighted mean breakeven price of put options expiring in 180 days derived from open interest or volume, indicating the price at which put buyers break even*

## Signal Profile
- `rank(put_breakeven_180)`: S=0.09, F=0.03, T=3.4%, INFERIOR (TOP3000)
- `rank(put_breakeven_180 / close)`: S=0.37, F=0.21, T=11.0%, INFERIOR (TOP3000)
- `rank(ts_delta(put_breakeven_180, 5))`: S=-0.82, F=-0.40, T=32.7%, INFERIOR (TOP200)
- `-rank(put_breakeven_180)`: S=0.05, F=0.01, T=3.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(put_breakeven_180, 5))`: S=1.20, F=0.53, T=37.7%, INFERIOR (TOP3000)
- `-ts_zscore(put_breakeven_180, 63)`: S=0.52, F=0.31, T=14.0%, INFERIOR (TOP3000)
- `ts_mean(put_breakeven_180, 10)`: S=0.24, F=0.11, T=1.5%, INFERIOR (TOP3000)
- `rank(ts_rank(put_breakeven_180, 22))`: S=-0.64, F=-0.30, T=22.5%, INFERIOR (TOP3000)
- `rank(-1 * put_breakeven_180)`: S=-0.09, F=-0.03, T=3.4%, INFERIOR (TOP3000)
- `rank(-1 * put_breakeven_180 / close)`: S=-0.50, F=-0.29, T=12.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 20F/1P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 21F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/6P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.09, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.52 (moderate), ret=+4.2%
  - 2020: S=-1.95 (negative), ret=-25.0%
  - 2021: S=0.51 (moderate), ret=+7.7%
  - 2022: S=1.29 (moderate), ret=+21.8%
  - 2023: S=-0.17 (negative), ret=-2.2%

## Risk & Drawdown
- Max drawdown: 54.27% over 1498 days (recovered)
- Annualized: return +1.3%, volatility 13.8% (fraction of booksize)
- Hit rate: 53.4% positive days
- Tail shape: skew -0.24, excess kurtosis +0.49

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -3.26, max 2.44, latest -0.38

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +9.38%; worst month: -11.36%
Positive months: 51%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=1.64
- Sideways: S=1.02
- Bear: S=-2.56

## Negated Direction
Best negated: `rank(-1 * ts_delta(put_breakeven_180, 5))` S=1.20, F=0.53, INFERIOR
Direction gap: +0.68 (negated - positive best Sharpe). NEGATION DOMINANT — field is significantly stronger when reversed.

Negated template variants:
- `rank(-1 * put_breakeven_180)`: S=-0.09, F=-0.03, T=3.4%, INFERIOR (TOP3000)
- `rank(-1 * put_breakeven_180 / close)`: S=-0.50, F=-0.29, T=12.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(put_breakeven_180, 5))`: S=1.20, F=0.53, T=37.7%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(put_breakeven_180)` | TOP3000 | 0.09 | 0.03 | 54.3% | 60% | bull-only |

## Correlation Notes
Top correlates:
- put_breakeven_150: 1.000 (strongly positively correlated)
- put_breakeven_120: 1.000 (strongly positively correlated)
- put_breakeven_270: 1.000 (strongly positively correlated)
- put_breakeven_90: 1.000 (strongly positively correlated)
- put_breakeven_60: 1.000 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
