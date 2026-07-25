---
field: fn_comp_options_grants_fair_value_a
dataset: fundamental2
best_template: ts_zscore
best_sharpe: 1.06
best_fitness: 1.6
best_universe: TOP3000
grade: GOOD
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: weak
n_variations_with_pnl: 6
max_drawdown: 0.3293
ann_vol: 0.1664
hit_rate: 0.5036
rolling_sharpe_min: -1.749
rolling_sharpe_max: 1.867
negated_best_sharpe: 0.74
negated_best_template: rank_neg_delta
negated_best_fitness: 0.46
n_negated_sims: 10
direction_gap: -0.32
---
# fn_comp_options_grants_fair_value_a (fundamental2)

*Annual Share-Based Compensation Arrangement by Share-Based Payment Award Options Grants in Period Weighted Average Grant Date Fair Value*

## Signal Profile
- `rank(fn_comp_options_grants_fair_value_a)`: S=0.22, F=0.07, T=0.9%, INFERIOR (TOP3000)
- `rank(fn_comp_options_grants_fair_value_a / close)`: S=0.31, F=0.14, T=2.1%, INFERIOR (TOP1000)
- `rank(ts_delta(fn_comp_options_grants_fair_value_a, 5))`: S=0.34, F=0.14, T=33.2%, INFERIOR (TOP3000)
- `-rank(fn_comp_options_grants_fair_value_a)`: S=0.25, F=0.09, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_comp_options_grants_fair_value_a, 5))`: S=0.74, F=0.46, T=32.9%, INFERIOR (TOP3000)
- `-ts_zscore(fn_comp_options_grants_fair_value_a, 63)`: S=1.06, F=1.60, T=15.7%, GOOD (TOP3000)
- `ts_mean(fn_comp_options_grants_fair_value_a, 10)`: S=0.19, F=0.10, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_comp_options_grants_fair_value_a, 22))`: S=0.18, F=0.07, T=15.3%, INFERIOR (TOP3000)
- `rank(-1 * fn_comp_options_grants_fair_value_a)`: S=0.25, F=0.09, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * fn_comp_options_grants_fair_value_a / close)`: S=-0.31, F=-0.14, T=2.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 13F/19P
- LOW_FITNESS: 31F/1P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 16F/13P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.34, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=1.95 (strong), ret=+33.8%
  - 2020: S=0.54 (moderate), ret=+9.0%
  - 2021: S=-1.39 (negative), ret=-22.0%
  - 2022: S=0.91 (moderate), ret=+14.9%
  - 2023: S=-0.52 (negative), ret=-7.8%

## Risk & Drawdown
- Max drawdown: 32.93% over 1113 days (not yet recovered, ongoing at window end)
- Annualized: return +5.7%, volatility 16.6% (fraction of booksize)
- Hit rate: 50.4% positive days
- Tail shape: skew +0.23, excess kurtosis +6.21

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.75, max 1.87, latest -0.58

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2021
Best month: +11.41%; worst month: -9.91%
Positive months: 56%

## Regime Profile
Regime profile: **weak**
- Bull: S=-0.11
- Sideways: S=1.02
- Bear: S=0.17

## Negated Direction
Best negated: `rank(-1 * ts_delta(fn_comp_options_grants_fair_value_a, 5))` S=0.74, F=0.46, INFERIOR
Direction gap: -0.32 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fn_comp_options_grants_fair_value_a)`: S=0.25, F=0.09, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * fn_comp_options_grants_fair_value_a / close)`: S=-0.31, F=-0.14, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_comp_options_grants_fair_value_a, 5))`: S=0.74, F=0.46, T=32.9%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fn_comp_options_grants_fair_value_a, 5))` | TOP3000 | 0.34 | 0.14 | 32.9% | 60% | weak |
| `rank(fn_comp_options_grants_fair_value_a / close)` | TOP1000 | 0.31 | 0.14 | 10.7% | 80% | mixed |
| `rank(fn_comp_options_grants_fair_value_a / close)` | TOP200 | 0.26 | 0.11 | 17.6% | 80% | weak |
| `rank(fn_comp_options_grants_fair_value_a / close)` | TOP500 | 0.24 | 0.09 | 10.9% | 60% | all-weather |
| `rank(fn_comp_options_grants_fair_value_a)` | TOP3000 | 0.23 | 0.07 | 23.6% | 80% | bull-only |
| `rank(fn_comp_options_grants_fair_value_a / close)` | TOP3000 | 0.17 | 0.07 | 21.9% | 60% | bear-only |

## Correlation Notes
Top correlates:
- fn_incremental_shares_attributable_to_share_based_payment_a: -0.129 (weakly negatively correlated)
- inventory_turnover: 0.129 (weakly positively correlated)
- fnd6_msa: 0.129 (weakly positively correlated)
- fn_comp_non_opt_grants_a: -0.122 (weakly negatively correlated)
- news_open_vol: -0.122 (weakly negatively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
