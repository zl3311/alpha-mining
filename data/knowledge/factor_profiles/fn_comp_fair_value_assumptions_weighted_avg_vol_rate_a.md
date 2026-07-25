---
field: fn_comp_fair_value_assumptions_weighted_avg_vol_rate_a
dataset: fundamental2
best_template: rank_level
best_sharpe: 0.52
best_fitness: 0.4
best_universe: TOP200
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bear-only
n_variations_with_pnl: 8
max_drawdown: 0.4107
ann_vol: 0.1437
hit_rate: 0.5239
rolling_sharpe_min: -1.728
rolling_sharpe_max: 3.788
negated_best_sharpe: 0.49
negated_best_template: rank_neg_delta
negated_best_fitness: 0.24
n_negated_sims: 10
direction_gap: -0.03
---
# fn_comp_fair_value_assumptions_weighted_avg_vol_rate_a (fundamental2)

*Weighted average expected volatility rate of share-based compensation awards.*

## Signal Profile
- `rank(fn_comp_fair_value_assumptions_weighted_avg_vol_rate_a)`: S=0.52, F=0.40, T=2.1%, INFERIOR (TOP200)
- `rank(fn_comp_fair_value_assumptions_weighted_avg_vol_rate_a / close)`: S=0.54, F=0.38, T=2.4%, INFERIOR (TOP200)
- `rank(ts_delta(fn_comp_fair_value_assumptions_weighted_avg_vol_rate_a, 5))`: S=0.68, F=0.38, T=33.9%, INFERIOR (TOP3000)
- `-rank(fn_comp_fair_value_assumptions_weighted_avg_vol_rate_a)`: S=-0.09, F=-0.03, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_comp_fair_value_assumptions_weighted_avg_vol_rate_a, 5))`: S=0.49, F=0.24, T=33.8%, INFERIOR (TOP3000)
- `-ts_zscore(fn_comp_fair_value_assumptions_weighted_avg_vol_rate_a, 63)`: S=-0.20, F=-0.10, T=16.6%, INFERIOR (TOP3000)
- `ts_mean(fn_comp_fair_value_assumptions_weighted_avg_vol_rate_a, 10)`: S=0.07, F=0.02, T=1.7%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_comp_fair_value_assumptions_weighted_avg_vol_rate_a, 22))`: S=-0.23, F=-0.10, T=14.9%, INFERIOR (TOP3000)
- `rank(-1 * fn_comp_fair_value_assumptions_weighted_avg_vol_rate_a)`: S=-0.09, F=-0.03, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * fn_comp_fair_value_assumptions_weighted_avg_vol_rate_a / close)`: S=-0.26, F=-0.13, T=1.8%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 13F/19P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/16P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.53, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.73 (moderate), ret=+4.7%
  - 2020: S=3.39 (strong), ret=+38.6%
  - 2021: S=-0.16 (negative), ret=-3.3%
  - 2022: S=-1.29 (negative), ret=-23.3%
  - 2023: S=2.36 (strong), ret=+20.5%

## Risk & Drawdown
- Max drawdown: 41.07% over 1043 days (not yet recovered, ongoing at window end)
- Annualized: return +7.6%, volatility 14.4% (fraction of booksize)
- Hit rate: 52.4% positive days
- Tail shape: skew +0.14, excess kurtosis +2.96

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.73, max 3.79, latest 2.38

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2022
Best month: +12.76%; worst month: -9.14%
Positive months: 59%

## Regime Profile
Regime profile: **bear-only**
- Bull: S=-1.43
- Sideways: S=0.73
- Bear: S=3.39

## Negated Direction
Best negated: `rank(-1 * ts_delta(fn_comp_fair_value_assumptions_weighted_avg_vol_rate_a, 5))` S=0.49, F=0.24, INFERIOR
Direction gap: -0.03 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fn_comp_fair_value_assumptions_weighted_avg_vol_rate_a)`: S=-0.09, F=-0.03, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * fn_comp_fair_value_assumptions_weighted_avg_vol_rate_a / close)`: S=-0.26, F=-0.13, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_comp_fair_value_assumptions_weighted_avg_vol_rate_a, 5))`: S=0.49, F=0.24, T=33.8%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fn_comp_fair_value_assumptions_weighted_avg_vol_rate_a)` | TOP200 | 0.53 | 0.40 | 41.1% | 60% | bear-only |
| `rank(fn_comp_fair_value_assumptions_weighted_avg_vol_rate_a / close)` | TOP200 | 0.55 | 0.38 | 22.4% | 80% | bear-only |
| `rank(ts_delta(fn_comp_fair_value_assumptions_weighted_avg_vol_rate_a, 5))` | TOP3000 | 0.67 | 0.38 | 16.5% | 80% | mixed |
| `rank(fn_comp_fair_value_assumptions_weighted_avg_vol_rate_a / close)` | TOP500 | 0.48 | 0.31 | 23.9% | 60% | bear-only |
| `rank(fn_comp_fair_value_assumptions_weighted_avg_vol_rate_a)` | TOP500 | 0.37 | 0.21 | 39.9% | 40% | bear-only |
| `rank(fn_comp_fair_value_assumptions_weighted_avg_vol_rate_a / close)` | TOP1000 | 0.26 | 0.13 | 31.2% | 40% | bear-only |
| `rank(fn_comp_fair_value_assumptions_weighted_avg_vol_rate_a)` | TOP3000 | 0.10 | 0.03 | 37.8% | 40% | bear-only |
| `rank(fn_comp_fair_value_assumptions_weighted_avg_vol_rate_a)` | TOP1000 | 0.10 | 0.03 | 40.7% | 40% | bear-only |

## Correlation Notes
Top correlates:
- parkinson_volatility_150: 0.872 (strongly positively correlated)
- parkinson_volatility_180: 0.867 (strongly positively correlated)
- historical_volatility_150: 0.861 (strongly positively correlated)
- historical_volatility_180: 0.856 (strongly positively correlated)
- fnd6_optvol: 0.849 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
