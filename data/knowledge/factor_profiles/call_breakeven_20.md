---
field: call_breakeven_20
dataset: option9
cluster: option9_other
coverage: 0.9824
community_alphas: 1723
best_template: rank_value_norm
best_sharpe: 0.39
best_fitness: 0.25
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 21
regime_profile: bull-only
n_variations_with_pnl: 1
max_drawdown: 0.5155
ann_vol: 0.1264
hit_rate: 0.5336
rolling_sharpe_min: -3.264
rolling_sharpe_max: 2.388
negated_best_sharpe: 0.68
negated_best_template: rank_neg_delta
negated_best_fitness: 0.24
n_negated_sims: 4
direction_gap: 0.29
---
# call_breakeven_20 (option9)

*Open-interest-weighted average breakeven price of call options expiring in 20 days, representing the price at which call buyers break even*

## Signal Profile
- `rank(call_breakeven_20)`: S=0.08, F=0.02, T=3.0%, INFERIOR (TOP3000)
- `rank(call_breakeven_20 / close)`: S=0.39, F=0.25, T=17.0%, INFERIOR (TOP3000)
- `rank(ts_delta(call_breakeven_20, 5))`: S=-0.16, F=-0.03, T=35.9%, INFERIOR (TOP200)
- `-rank(call_breakeven_20)`: S=0.04, F=0.01, T=3.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(call_breakeven_20, 5))`: S=0.68, F=0.24, T=37.6%, INFERIOR (TOP3000)
- `-ts_zscore(call_breakeven_20, 63)`: S=0.40, F=0.22, T=14.4%, INFERIOR (TOP3000)
- `ts_mean(call_breakeven_20, 10)`: S=0.30, F=0.15, T=1.4%, INFERIOR (TOP3000)
- `rank(ts_rank(call_breakeven_20, 22))`: S=-0.49, F=-0.20, T=24.9%, INFERIOR (TOP3000)
- `rank(-1 * call_breakeven_20)`: S=-0.08, F=-0.02, T=3.0%, INFERIOR (TOP3000)
- `rank(-1 * call_breakeven_20 / close)`: S=-0.27, F=-0.13, T=18.6%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 20F/1P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 21F/0P
- LOW_SUB_UNIVERSE_SHARPE: 9F/10P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.08, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.54 (moderate), ret=+4.1%
  - 2020: S=-1.82 (negative), ret=-22.5%
  - 2021: S=0.39 (weak), ret=+5.2%
  - 2022: S=1.26 (moderate), ret=+19.2%
  - 2023: S=-0.10 (negative), ret=-1.3%

## Risk & Drawdown
- Max drawdown: 51.55% over 1508 days (recovered)
- Annualized: return +1.0%, volatility 12.6% (fraction of booksize)
- Hit rate: 53.4% positive days
- Tail shape: skew -0.28, excess kurtosis +0.57

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -3.26, max 2.39, latest -0.32

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +8.49%; worst month: -10.42%
Positive months: 51%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=1.52
- Sideways: S=1.03
- Bear: S=-2.42

## Negated Direction
Best negated: `rank(-1 * ts_delta(call_breakeven_20, 5))` S=0.68, F=0.24, INFERIOR
Direction gap: +0.29 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * call_breakeven_20)`: S=-0.08, F=-0.02, T=3.0%, INFERIOR (TOP3000)
- `rank(-1 * call_breakeven_20 / close)`: S=-0.27, F=-0.13, T=18.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(call_breakeven_20, 5))`: S=0.68, F=0.24, T=37.6%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(call_breakeven_20)` | TOP3000 | 0.08 | 0.02 | 51.5% | 60% | bull-only |

## Correlation Notes
Top correlates:
- call_breakeven_10: 1.000 (strongly positively correlated)
- call_breakeven_30: 1.000 (strongly positively correlated)
- option_breakeven_20: 1.000 (strongly positively correlated)
- option_breakeven_30: 1.000 (strongly positively correlated)
- option_breakeven_60: 1.000 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
