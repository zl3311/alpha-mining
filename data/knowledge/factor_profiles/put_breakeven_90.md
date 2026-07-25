---
field: put_breakeven_90
dataset: option9
best_template: rank_neg_delta
best_sharpe: 1.25
best_fitness: 0.58
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_FITNESS
n_sims: 21
regime_profile: bull-only
n_variations_with_pnl: 1
max_drawdown: 0.5385
ann_vol: 0.1367
hit_rate: 0.536
rolling_sharpe_min: -3.282
rolling_sharpe_max: 2.427
negated_best_sharpe: 1.25
negated_best_template: rank_neg_delta
negated_best_fitness: 0.58
n_negated_sims: 4
direction_gap: 0.61
---
# put_breakeven_90 (option9)

*Open-interest-weighted mean breakeven price at which buyers of put options break even for options expiring in 90 days*

## Signal Profile
- `rank(put_breakeven_90)`: S=0.09, F=0.03, T=3.3%, INFERIOR (TOP3000)
- `rank(put_breakeven_90 / close)`: S=0.46, F=0.28, T=11.7%, INFERIOR (TOP3000)
- `rank(ts_delta(put_breakeven_90, 5))`: S=-0.82, F=-0.39, T=33.9%, INFERIOR (TOP200)
- `-rank(put_breakeven_90)`: S=0.05, F=0.01, T=3.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(put_breakeven_90, 5))`: S=1.25, F=0.58, T=38.8%, INFERIOR (TOP3000)
- `-ts_zscore(put_breakeven_90, 63)`: S=0.64, F=0.43, T=14.9%, INFERIOR (TOP3000)
- `ts_mean(put_breakeven_90, 10)`: S=0.25, F=0.12, T=1.4%, INFERIOR (TOP3000)
- `rank(ts_rank(put_breakeven_90, 22))`: S=-0.81, F=-0.43, T=24.0%, INFERIOR (TOP3000)
- `rank(-1 * put_breakeven_90)`: S=-0.09, F=-0.03, T=3.3%, INFERIOR (TOP3000)
- `rank(-1 * put_breakeven_90 / close)`: S=-0.58, F=-0.35, T=13.0%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 20F/1P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 20F/1P
- LOW_SUB_UNIVERSE_SHARPE: 15F/4P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.10, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.56 (moderate), ret=+4.5%
  - 2020: S=-1.95 (negative), ret=-24.9%
  - 2021: S=0.51 (moderate), ret=+7.5%
  - 2022: S=1.28 (moderate), ret=+21.4%
  - 2023: S=-0.17 (negative), ret=-2.2%

## Risk & Drawdown
- Max drawdown: 53.85% over 1498 days (recovered)
- Annualized: return +1.3%, volatility 13.7% (fraction of booksize)
- Hit rate: 53.6% positive days
- Tail shape: skew -0.24, excess kurtosis +0.50

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -3.28, max 2.43, latest -0.38

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +9.33%; worst month: -11.42%
Positive months: 51%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=1.64
- Sideways: S=1.04
- Bear: S=-2.55

## Negated Direction
Best negated: `rank(-1 * ts_delta(put_breakeven_90, 5))` S=1.25, F=0.58, INFERIOR
Direction gap: +0.61 (negated - positive best Sharpe). NEGATION DOMINANT — field is significantly stronger when reversed.

Negated template variants:
- `rank(-1 * put_breakeven_90)`: S=-0.09, F=-0.03, T=3.3%, INFERIOR (TOP3000)
- `rank(-1 * put_breakeven_90 / close)`: S=-0.58, F=-0.35, T=13.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(put_breakeven_90, 5))`: S=1.25, F=0.58, T=38.8%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(put_breakeven_90)` | TOP3000 | 0.10 | 0.03 | 53.8% | 60% | bull-only |

## Correlation Notes
Top correlates:
- put_breakeven_120: 1.000 (strongly positively correlated)
- put_breakeven_60: 1.000 (strongly positively correlated)
- put_breakeven_150: 1.000 (strongly positively correlated)
- put_breakeven_180: 1.000 (strongly positively correlated)
- put_breakeven_270: 1.000 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_FITNESS. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
