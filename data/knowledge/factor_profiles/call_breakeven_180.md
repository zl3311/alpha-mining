---
field: call_breakeven_180
dataset: option9
best_template: rank_neg_delta
best_sharpe: 0.81
best_fitness: 0.31
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 21
regime_profile: bull-only
n_variations_with_pnl: 1
max_drawdown: 0.4871
ann_vol: 0.119
hit_rate: 0.5304
rolling_sharpe_min: -3.216
rolling_sharpe_max: 2.437
negated_best_sharpe: 0.81
negated_best_template: rank_neg_delta
negated_best_fitness: 0.31
n_negated_sims: 4
direction_gap: 0.46
---
# call_breakeven_180 (option9)

*Open-interest-weighted mean breakeven price at which buyers of call options break even for options expiring in 180 days*

## Signal Profile
- `rank(call_breakeven_180)`: S=0.12, F=0.04, T=3.0%, INFERIOR (TOP3000)
- `rank(call_breakeven_180 / close)`: S=0.23, F=0.13, T=10.0%, INFERIOR (TOP3000)
- `rank(ts_delta(call_breakeven_180, 5))`: S=-0.39, F=-0.12, T=33.1%, INFERIOR (TOP1000)
- `-rank(call_breakeven_180)`: S=0.01, F=0.00, T=2.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(call_breakeven_180, 5))`: S=0.81, F=0.31, T=35.7%, INFERIOR (TOP3000)
- `-ts_zscore(call_breakeven_180, 63)`: S=0.24, F=0.10, T=13.2%, INFERIOR (TOP3000)
- `ts_mean(call_breakeven_180, 10)`: S=0.35, F=0.19, T=1.4%, INFERIOR (TOP3000)
- `rank(ts_rank(call_breakeven_180, 22))`: S=-0.24, F=-0.07, T=22.1%, INFERIOR (TOP3000)
- `rank(-1 * call_breakeven_180)`: S=-0.12, F=-0.04, T=3.0%, INFERIOR (TOP3000)
- `rank(-1 * call_breakeven_180 / close)`: S=-0.24, F=-0.14, T=10.9%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 20F/1P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 21F/0P
- LOW_SUB_UNIVERSE_SHARPE: 12F/7P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.12, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.61 (moderate), ret=+4.5%
  - 2020: S=-1.75 (negative), ret=-20.7%
  - 2021: S=0.40 (weak), ret=+5.0%
  - 2022: S=1.37 (moderate), ret=+18.9%
  - 2023: S=-0.04 (negative), ret=-0.4%

## Risk & Drawdown
- Max drawdown: 48.71% over 1498 days (recovered)
- Annualized: return +1.5%, volatility 11.9% (fraction of booksize)
- Hit rate: 53.0% positive days
- Tail shape: skew -0.27, excess kurtosis +0.55

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -3.22, max 2.44, latest -0.26

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +7.95%; worst month: -10.20%
Positive months: 51%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=1.51
- Sideways: S=1.08
- Bear: S=-2.32

## Negated Direction
Best negated: `rank(-1 * ts_delta(call_breakeven_180, 5))` S=0.81, F=0.31, INFERIOR
Direction gap: +0.46 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * call_breakeven_180)`: S=-0.12, F=-0.04, T=3.0%, INFERIOR (TOP3000)
- `rank(-1 * call_breakeven_180 / close)`: S=-0.24, F=-0.14, T=10.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(call_breakeven_180, 5))`: S=0.81, F=0.31, T=35.7%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(call_breakeven_180)` | TOP3000 | 0.12 | 0.04 | 48.7% | 60% | bull-only |

## Correlation Notes
Top correlates:
- call_breakeven_150: 1.000 (strongly positively correlated)
- call_breakeven_120: 0.999 (strongly positively correlated)
- call_breakeven_90: 0.999 (strongly positively correlated)
- call_breakeven_60: 0.999 (strongly positively correlated)
- call_breakeven_1080: 0.999 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
