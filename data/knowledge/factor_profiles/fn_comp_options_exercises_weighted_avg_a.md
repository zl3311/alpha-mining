---
field: fn_comp_options_exercises_weighted_avg_a
dataset: fundamental2
best_template: rank_value_norm
best_sharpe: 0.8
best_fitness: 0.53
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 7
max_drawdown: 0.0821
ann_vol: 0.0685
hit_rate: 0.481
rolling_sharpe_min: -0.754
rolling_sharpe_max: 2.462
redundancy_cluster: 1
negated_best_sharpe: 0.67
negated_best_template: rank_neg_delta
negated_best_fitness: 0.4
n_negated_sims: 10
direction_gap: -0.13
---
# fn_comp_options_exercises_weighted_avg_a (fundamental2)

*Share-Based Compensation, Options Assumed, Weighted Average Exercise Price*

## Signal Profile
- `rank(fn_comp_options_exercises_weighted_avg_a)`: S=0.17, F=0.06, T=0.8%, INFERIOR (TOP3000)
- `rank(fn_comp_options_exercises_weighted_avg_a / close)`: S=0.80, F=0.53, T=1.7%, INFERIOR (TOP3000)
- `rank(ts_delta(fn_comp_options_exercises_weighted_avg_a, 5))`: S=0.21, F=0.06, T=34.5%, INFERIOR (TOP3000)
- `-rank(fn_comp_options_exercises_weighted_avg_a)`: S=0.08, F=0.02, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_comp_options_exercises_weighted_avg_a, 5))`: S=0.67, F=0.40, T=33.0%, INFERIOR (TOP3000)
- `-ts_zscore(fn_comp_options_exercises_weighted_avg_a, 63)`: S=0.52, F=0.41, T=17.0%, INFERIOR (TOP3000)
- `ts_mean(fn_comp_options_exercises_weighted_avg_a, 10)`: S=0.17, F=0.08, T=2.4%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_comp_options_exercises_weighted_avg_a, 22))`: S=0.05, F=0.01, T=14.9%, INFERIOR (TOP3000)
- `rank(-1 * fn_comp_options_exercises_weighted_avg_a)`: S=0.08, F=0.02, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * fn_comp_options_exercises_weighted_avg_a / close)`: S=-0.25, F=-0.12, T=2.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 13F/19P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 17F/12P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.78, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.12 (weak), ret=+0.5%
  - 2020: S=0.43 (weak), ret=+3.9%
  - 2021: S=0.82 (moderate), ret=+6.3%
  - 2022: S=2.05 (strong), ret=+12.1%
  - 2023: S=0.65 (moderate), ret=+3.2%

## Risk & Drawdown
- Max drawdown: 8.21% over 262 days (recovered)
- Annualized: return +5.3%, volatility 6.9% (fraction of booksize)
- Hit rate: 48.1% positive days
- Tail shape: skew +0.75, excess kurtosis +4.42

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.75, max 2.46, latest 0.81

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2019
Best month: +6.20%; worst month: -3.18%
Positive months: 56%

## Regime Profile
Regime profile: **mixed**
- Bull: S=2.45
- Sideways: S=-0.76
- Bear: S=0.21

## Negated Direction
Best negated: `rank(-1 * ts_delta(fn_comp_options_exercises_weighted_avg_a, 5))` S=0.67, F=0.40, INFERIOR
Direction gap: -0.13 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fn_comp_options_exercises_weighted_avg_a)`: S=0.08, F=0.02, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * fn_comp_options_exercises_weighted_avg_a / close)`: S=-0.25, F=-0.12, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_comp_options_exercises_weighted_avg_a, 5))`: S=0.67, F=0.40, T=33.0%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fn_comp_options_exercises_weighted_avg_a / close)` | TOP3000 | 0.78 | 0.53 | 8.2% | 100% | mixed |
| `rank(fn_comp_options_exercises_weighted_avg_a / close)` | TOP1000 | 0.43 | 0.26 | 15.3% | 60% | bull-only |
| `rank(fn_comp_options_exercises_weighted_avg_a / close)` | TOP500 | 0.24 | 0.12 | 23.4% | 60% | bull-only |
| `rank(fn_comp_options_exercises_weighted_avg_a)` | TOP3000 | 0.16 | 0.06 | 37.2% | 80% | bull-only |
| `rank(ts_delta(fn_comp_options_exercises_weighted_avg_a, 5))` | TOP3000 | 0.20 | 0.06 | 26.6% | 60% | bear-only |
| `rank(ts_delta(fn_comp_options_exercises_weighted_avg_a, 5))` | TOP200 | 0.10 | 0.03 | 33.4% | 60% | bull-only |
| `rank(fn_comp_options_exercises_weighted_avg_a / close)` | TOP200 | 0.09 | 0.03 | 37.7% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_optprcex: 0.955 (strongly positively correlated)
- fnd6_optprcwa: 0.878 (strongly positively correlated)
- fn_comp_options_exercisable_weighted_avg_a: 0.874 (strongly positively correlated)
- fnd6_optprcby: 0.871 (strongly positively correlated)
- fnd6_optprcey: 0.851 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
