---
field: fn_comp_options_out_weighted_avg_a
dataset: fundamental2
best_template: rank_value_norm
best_sharpe: 0.64
best_fitness: 0.41
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: all-weather
n_variations_with_pnl: 7
max_drawdown: 0.1122
ann_vol: 0.0802
hit_rate: 0.4583
rolling_sharpe_min: -1.18
rolling_sharpe_max: 2.317
redundancy_cluster: 33
negated_best_sharpe: 0.58
negated_best_template: rank_neg_delta
negated_best_fitness: 0.38
n_negated_sims: 10
direction_gap: -0.06
---
# fn_comp_options_out_weighted_avg_a (fundamental2)

*Weighted average price at which grantees can acquire the shares reserved for issuance under the stock option plan.*

## Signal Profile
- `rank(fn_comp_options_out_weighted_avg_a)`: S=0.26, F=0.11, T=0.8%, INFERIOR (TOP3000)
- `rank(fn_comp_options_out_weighted_avg_a / close)`: S=0.64, F=0.41, T=1.7%, INFERIOR (TOP3000)
- `rank(ts_delta(fn_comp_options_out_weighted_avg_a, 5))`: S=0.21, F=0.06, T=34.5%, INFERIOR (TOP3000)
- `-rank(fn_comp_options_out_weighted_avg_a)`: S=0.09, F=0.02, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_comp_options_out_weighted_avg_a, 5))`: S=0.58, F=0.38, T=28.5%, INFERIOR (TOP3000)
- `-ts_zscore(fn_comp_options_out_weighted_avg_a, 63)`: S=0.19, F=0.09, T=17.2%, INFERIOR (TOP3000)
- `ts_mean(fn_comp_options_out_weighted_avg_a, 10)`: S=0.05, F=0.02, T=3.1%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_comp_options_out_weighted_avg_a, 22))`: S=-0.23, F=-0.09, T=14.8%, INFERIOR (TOP3000)
- `rank(-1 * fn_comp_options_out_weighted_avg_a)`: S=-0.09, F=-0.03, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * fn_comp_options_out_weighted_avg_a / close)`: S=-0.43, F=-0.28, T=2.7%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 13F/19P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 11F/9P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.62, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.03 (weak), ret=+0.2%
  - 2020: S=1.12 (moderate), ret=+12.0%
  - 2021: S=1.05 (moderate), ret=+7.2%
  - 2022: S=0.20 (weak), ret=+1.3%
  - 2023: S=0.47 (weak), ret=+3.8%

## Risk & Drawdown
- Max drawdown: 11.22% over 500 days (not yet recovered, ongoing at window end)
- Annualized: return +5.0%, volatility 8.0% (fraction of booksize)
- Hit rate: 45.8% positive days
- Tail shape: skew +0.84, excess kurtosis +3.34

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.18, max 2.32, latest 0.67

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2019
Best month: +5.81%; worst month: -4.08%
Positive months: 54%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=1.14
- Sideways: S=-0.99
- Bear: S=1.52

## Negated Direction
Best negated: `rank(-1 * ts_delta(fn_comp_options_out_weighted_avg_a, 5))` S=0.58, F=0.38, INFERIOR
Direction gap: -0.06 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fn_comp_options_out_weighted_avg_a)`: S=-0.09, F=-0.03, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * fn_comp_options_out_weighted_avg_a / close)`: S=-0.43, F=-0.28, T=2.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_comp_options_out_weighted_avg_a, 5))`: S=0.58, F=0.38, T=28.5%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fn_comp_options_out_weighted_avg_a / close)` | TOP3000 | 0.62 | 0.41 | 11.2% | 100% | all-weather |
| `rank(fn_comp_options_out_weighted_avg_a / close)` | TOP200 | 0.44 | 0.28 | 28.4% | 60% | bull-only |
| `rank(fn_comp_options_out_weighted_avg_a / close)` | TOP1000 | 0.37 | 0.20 | 14.6% | 60% | bull-only |
| `rank(fn_comp_options_out_weighted_avg_a / close)` | TOP500 | 0.28 | 0.14 | 18.9% | 60% | bull-only |
| `rank(fn_comp_options_out_weighted_avg_a)` | TOP3000 | 0.25 | 0.11 | 28.5% | 80% | bull-only |
| `rank(ts_delta(fn_comp_options_out_weighted_avg_a, 5))` | TOP3000 | 0.22 | 0.06 | 36.3% | 60% | mixed |
| `rank(fn_comp_options_out_weighted_avg_a)` | TOP200 | 0.09 | 0.03 | 31.9% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_optprcey: 0.966 (strongly positively correlated)
- fn_comp_options_exercisable_weighted_avg_a: 0.960 (strongly positively correlated)
- fnd6_optprcca: 0.944 (strongly positively correlated)
- fnd6_optprcby: 0.925 (strongly positively correlated)
- fnd6_optprcwa: 0.921 (strongly positively correlated)

Redundancy cluster #33: 12 similar fields, mean |rho| 0.787 (representative: anl4_afv4_eps_high). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
