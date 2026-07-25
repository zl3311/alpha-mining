---
field: fn_comp_non_opt_grants_a
dataset: fundamental2
best_template: ts_zscore
best_sharpe: 0.68
best_fitness: 0.49
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bear-only
n_variations_with_pnl: 3
max_drawdown: 0.2641
ann_vol: 0.0834
hit_rate: 0.4794
rolling_sharpe_min: -1.897
rolling_sharpe_max: 3.834
negated_best_sharpe: 0.19
negated_best_template: neg_rank_level
negated_best_fitness: 0.07
n_negated_sims: 10
direction_gap: -0.49
---
# fn_comp_non_opt_grants_a (fundamental2)

*The number of grants made during the period on other than stock (or unit) option plans (for example, phantom stock or unit plan, stock or unit appreciation rights plan, performance target plan).*

## Signal Profile
- `rank(fn_comp_non_opt_grants_a)`: S=0.18, F=0.05, T=1.0%, INFERIOR (TOP3000)
- `rank(fn_comp_non_opt_grants_a / close)`: S=0.25, F=0.10, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_delta(fn_comp_non_opt_grants_a, 5))`: S=0.29, F=0.09, T=34.7%, INFERIOR (TOP3000)
- `-rank(fn_comp_non_opt_grants_a)`: S=-0.01, F=0.00, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_comp_non_opt_grants_a, 5))`: S=0.01, F=0.00, T=31.2%, INFERIOR (TOP3000)
- `-ts_zscore(fn_comp_non_opt_grants_a, 63)`: S=0.68, F=0.49, T=16.9%, INFERIOR (TOP3000)
- `ts_mean(fn_comp_non_opt_grants_a, 10)`: S=-0.91, F=-0.87, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_comp_non_opt_grants_a, 22))`: S=-0.55, F=-0.31, T=14.3%, INFERIOR (TOP3000)
- `rank(-1 * fn_comp_non_opt_grants_a)`: S=0.19, F=0.07, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * fn_comp_non_opt_grants_a / close)`: S=-0.04, F=-0.01, T=2.0%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 13F/19P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 10F/10P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.26, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.05 (weak), ret=+0.2%
  - 2020: S=2.29 (strong), ret=+18.1%
  - 2021: S=-0.01 (negative), ret=-0.0%
  - 2022: S=-0.90 (negative), ret=-9.7%
  - 2023: S=0.21 (weak), ret=+2.0%

## Risk & Drawdown
- Max drawdown: 26.41% over 933 days (not yet recovered, ongoing at window end)
- Annualized: return +2.2%, volatility 8.3% (fraction of booksize)
- Hit rate: 47.9% positive days
- Tail shape: skew +0.30, excess kurtosis +1.18

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.90, max 3.83, latest 0.38

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2022
Best month: +7.19%; worst month: -5.02%
Positive months: 54%

## Regime Profile
Regime profile: **bear-only**
- Bull: S=-0.76
- Sideways: S=-0.72
- Bear: S=2.32

## Negated Direction
Best negated: `rank(-1 * fn_comp_non_opt_grants_a)` S=0.19, F=0.07, INFERIOR
Direction gap: -0.49 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fn_comp_non_opt_grants_a)`: S=0.19, F=0.07, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * fn_comp_non_opt_grants_a / close)`: S=-0.04, F=-0.01, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_comp_non_opt_grants_a, 5))`: S=0.01, F=0.00, T=31.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fn_comp_non_opt_grants_a / close)` | TOP3000 | 0.26 | 0.10 | 26.4% | 60% | bear-only |
| `rank(ts_delta(fn_comp_non_opt_grants_a, 5))` | TOP3000 | 0.30 | 0.09 | 24.3% | 60% | all-weather |
| `rank(fn_comp_non_opt_grants_a)` | TOP3000 | 0.20 | 0.05 | 12.3% | 80% | mixed |

## Correlation Notes
Top correlates:
- fn_comp_non_opt_vested_a: 0.960 (strongly positively correlated)
- option_breakeven_20: -0.916 (strongly negatively correlated)
- option_breakeven_30: -0.916 (strongly negatively correlated)
- option_breakeven_10: -0.916 (strongly negatively correlated)
- call_breakeven_10: -0.916 (strongly negatively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
