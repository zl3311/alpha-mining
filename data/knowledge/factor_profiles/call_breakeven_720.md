---
field: call_breakeven_720
dataset: option9
best_template: rank_neg_delta
best_sharpe: 1.12
best_fitness: 0.48
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 21
regime_profile: bull-only
n_variations_with_pnl: 1
max_drawdown: 0.4745
ann_vol: 0.1154
hit_rate: 0.5312
rolling_sharpe_min: -3.187
rolling_sharpe_max: 2.5
negated_best_sharpe: 1.12
negated_best_template: rank_neg_delta
negated_best_fitness: 0.48
n_negated_sims: 4
direction_gap: 0.78
---
# call_breakeven_720 (option9)

*Weighted mean breakeven price of call options expiring in 720 days indicating the price at which call buyers break even*

## Signal Profile
- `rank(call_breakeven_720)`: S=0.14, F=0.05, T=3.1%, INFERIOR (TOP3000)
- `rank(call_breakeven_720 / close)`: S=0.22, F=0.12, T=8.5%, INFERIOR (TOP3000)
- `rank(ts_delta(call_breakeven_720, 5))`: S=-0.46, F=-0.14, T=36.5%, INFERIOR (TOP1000)
- `-rank(call_breakeven_720)`: S=0.01, F=0.00, T=3.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(call_breakeven_720, 5))`: S=1.12, F=0.48, T=38.7%, INFERIOR (TOP3000)
- `-ts_zscore(call_breakeven_720, 63)`: S=0.21, F=0.08, T=14.3%, INFERIOR (TOP3000)
- `ts_mean(call_breakeven_720, 10)`: S=0.34, F=0.18, T=1.4%, INFERIOR (TOP3000)
- `rank(ts_rank(call_breakeven_720, 22))`: S=-0.42, F=-0.16, T=23.7%, INFERIOR (TOP3000)
- `rank(-1 * call_breakeven_720)`: S=-0.14, F=-0.05, T=3.1%, INFERIOR (TOP3000)
- `rank(-1 * call_breakeven_720 / close)`: S=-0.26, F=-0.15, T=10.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 20F/1P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 21F/0P
- LOW_SUB_UNIVERSE_SHARPE: 12F/7P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.14, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.65 (moderate), ret=+4.7%
  - 2020: S=-1.69 (negative), ret=-19.8%
  - 2021: S=0.39 (weak), ret=+4.8%
  - 2022: S=1.39 (moderate), ret=+17.8%
  - 2023: S=0.04 (weak), ret=+0.4%

## Risk & Drawdown
- Max drawdown: 47.45% over 1498 days (recovered)
- Annualized: return +1.7%, volatility 11.5% (fraction of booksize)
- Hit rate: 53.1% positive days
- Tail shape: skew -0.27, excess kurtosis +0.50

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -3.19, max 2.50, latest -0.18

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +7.92%; worst month: -9.98%
Positive months: 51%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=1.56
- Sideways: S=1.13
- Bear: S=-2.33

## Negated Direction
Best negated: `rank(-1 * ts_delta(call_breakeven_720, 5))` S=1.12, F=0.48, INFERIOR
Direction gap: +0.78 (negated - positive best Sharpe). NEGATION DOMINANT — field is significantly stronger when reversed.

Negated template variants:
- `rank(-1 * call_breakeven_720)`: S=-0.14, F=-0.05, T=3.1%, INFERIOR (TOP3000)
- `rank(-1 * call_breakeven_720 / close)`: S=-0.26, F=-0.15, T=10.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(call_breakeven_720, 5))`: S=1.12, F=0.48, T=38.7%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(call_breakeven_720)` | TOP3000 | 0.14 | 0.05 | 47.4% | 80% | bull-only |

## Correlation Notes
Top correlates:
- call_breakeven_1080: 1.000 (strongly positively correlated)
- call_breakeven_270: 0.999 (strongly positively correlated)
- call_breakeven_360: 0.999 (strongly positively correlated)
- call_breakeven_150: 0.999 (strongly positively correlated)
- call_breakeven_180: 0.999 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
