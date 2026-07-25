---
field: call_breakeven_60
dataset: option9
best_template: rank_neg_delta
best_sharpe: 1.05
best_fitness: 0.44
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 21
regime_profile: bull-only
n_variations_with_pnl: 1
max_drawdown: 0.4995
ann_vol: 0.1223
hit_rate: 0.5328
rolling_sharpe_min: -3.229
rolling_sharpe_max: 2.413
negated_best_sharpe: 1.05
negated_best_template: rank_neg_delta
negated_best_fitness: 0.44
n_negated_sims: 4
direction_gap: 0.54
---
# call_breakeven_60 (option9)

*Open interest-weighted mean breakeven price for call options expiring in 60 days, showing average price at which call buyers break even*

## Signal Profile
- `rank(call_breakeven_60)`: S=0.09, F=0.03, T=3.0%, INFERIOR (TOP3000)
- `rank(call_breakeven_60 / close)`: S=0.34, F=0.23, T=13.6%, INFERIOR (TOP3000)
- `rank(ts_delta(call_breakeven_60, 5))`: S=-0.95, F=-0.41, T=36.0%, INFERIOR (TOP1000)
- `-rank(call_breakeven_60)`: S=0.04, F=0.01, T=3.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(call_breakeven_60, 5))`: S=1.05, F=0.44, T=37.8%, INFERIOR (TOP3000)
- `-ts_zscore(call_breakeven_60, 63)`: S=0.51, F=0.30, T=14.9%, INFERIOR (TOP3000)
- `ts_mean(call_breakeven_60, 10)`: S=0.32, F=0.16, T=1.4%, INFERIOR (TOP3000)
- `rank(ts_rank(call_breakeven_60, 22))`: S=-0.75, F=-0.36, T=24.6%, INFERIOR (TOP3000)
- `rank(-1 * call_breakeven_60)`: S=-0.09, F=-0.03, T=3.0%, INFERIOR (TOP3000)
- `rank(-1 * call_breakeven_60 / close)`: S=-0.25, F=-0.14, T=14.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 20F/1P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 21F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/6P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.09, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.57 (moderate), ret=+4.3%
  - 2020: S=-1.76 (negative), ret=-21.3%
  - 2021: S=0.39 (weak), ret=+5.0%
  - 2022: S=1.27 (moderate), ret=+18.4%
  - 2023: S=-0.07 (negative), ret=-0.9%

## Risk & Drawdown
- Max drawdown: 49.95% over 1507 days (recovered)
- Annualized: return +1.1%, volatility 12.2% (fraction of booksize)
- Hit rate: 53.3% positive days
- Tail shape: skew -0.27, excess kurtosis +0.54

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -3.23, max 2.41, latest -0.29

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +8.36%; worst month: -10.12%
Positive months: 51%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=1.52
- Sideways: S=1.06
- Bear: S=-2.38

## Negated Direction
Best negated: `rank(-1 * ts_delta(call_breakeven_60, 5))` S=1.05, F=0.44, INFERIOR
Direction gap: +0.54 (negated - positive best Sharpe). NEGATION DOMINANT — field is significantly stronger when reversed.

Negated template variants:
- `rank(-1 * call_breakeven_60)`: S=-0.09, F=-0.03, T=3.0%, INFERIOR (TOP3000)
- `rank(-1 * call_breakeven_60 / close)`: S=-0.25, F=-0.14, T=14.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(call_breakeven_60, 5))`: S=1.05, F=0.44, T=37.8%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(call_breakeven_60)` | TOP3000 | 0.09 | 0.03 | 50.0% | 60% | bull-only |

## Correlation Notes
Top correlates:
- call_breakeven_90: 1.000 (strongly positively correlated)
- call_breakeven_30: 1.000 (strongly positively correlated)
- call_breakeven_20: 0.999 (strongly positively correlated)
- call_breakeven_120: 0.999 (strongly positively correlated)
- option_breakeven_90: 0.999 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
