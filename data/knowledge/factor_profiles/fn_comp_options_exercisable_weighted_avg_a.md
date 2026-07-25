---
field: fn_comp_options_exercisable_weighted_avg_a
dataset: fundamental2
best_template: rank_value_norm
best_sharpe: 0.59
best_fitness: 0.37
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: all-weather
n_variations_with_pnl: 5
max_drawdown: 0.1174
ann_vol: 0.0845
hit_rate: 0.4826
rolling_sharpe_min: -1.293
rolling_sharpe_max: 2.303
redundancy_cluster: 12
negated_best_sharpe: 0.55
negated_best_template: rank_neg_delta
negated_best_fitness: 0.35
n_negated_sims: 10
direction_gap: -0.04
---
# fn_comp_options_exercisable_weighted_avg_a (fundamental2)

*The weighted-average price as of the balance sheet date at which grantees can acquire the shares reserved for issuance on vested portions of options outstanding and currently exercisable under the stock option plan.*

## Signal Profile
- `rank(fn_comp_options_exercisable_weighted_avg_a)`: S=0.14, F=0.04, T=0.8%, INFERIOR (TOP3000)
- `rank(fn_comp_options_exercisable_weighted_avg_a / close)`: S=0.59, F=0.37, T=1.7%, INFERIOR (TOP3000)
- `rank(ts_delta(fn_comp_options_exercisable_weighted_avg_a, 5))`: S=-0.24, F=-0.08, T=32.9%, INFERIOR (TOP500)
- `-rank(fn_comp_options_exercisable_weighted_avg_a)`: S=0.02, F=0.00, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_comp_options_exercisable_weighted_avg_a, 5))`: S=0.55, F=0.35, T=27.0%, INFERIOR (TOP3000)
- `-ts_zscore(fn_comp_options_exercisable_weighted_avg_a, 63)`: S=0.34, F=0.23, T=17.7%, INFERIOR (TOP3000)
- `ts_mean(fn_comp_options_exercisable_weighted_avg_a, 10)`: S=0.23, F=0.11, T=2.6%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_comp_options_exercisable_weighted_avg_a, 22))`: S=-0.39, F=-0.21, T=15.0%, INFERIOR (TOP3000)
- `rank(-1 * fn_comp_options_exercisable_weighted_avg_a)`: S=0.12, F=0.04, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * fn_comp_options_exercisable_weighted_avg_a / close)`: S=-0.30, F=-0.17, T=2.7%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 13F/19P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 12F/8P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.57, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=-0.07 (negative), ret=-0.4%
  - 2020: S=0.87 (moderate), ret=+10.1%
  - 2021: S=0.92 (moderate), ret=+7.4%
  - 2022: S=0.94 (moderate), ret=+6.2%
  - 2023: S=0.06 (weak), ret=+0.5%

## Risk & Drawdown
- Max drawdown: 11.74% over 469 days (recovered)
- Annualized: return +4.8%, volatility 8.5% (fraction of booksize)
- Hit rate: 48.3% positive days
- Tail shape: skew +0.89, excess kurtosis +4.09

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.29, max 2.30, latest 0.24

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2019
Best month: +6.48%; worst month: -3.73%
Positive months: 49%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=1.47
- Sideways: S=-1.08
- Bear: S=1.06

## Negated Direction
Best negated: `rank(-1 * ts_delta(fn_comp_options_exercisable_weighted_avg_a, 5))` S=0.55, F=0.35, INFERIOR
Direction gap: -0.04 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fn_comp_options_exercisable_weighted_avg_a)`: S=0.12, F=0.04, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * fn_comp_options_exercisable_weighted_avg_a / close)`: S=-0.30, F=-0.17, T=2.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_comp_options_exercisable_weighted_avg_a, 5))`: S=0.55, F=0.35, T=27.0%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fn_comp_options_exercisable_weighted_avg_a / close)` | TOP3000 | 0.57 | 0.37 | 11.7% | 80% | all-weather |
| `rank(fn_comp_options_exercisable_weighted_avg_a / close)` | TOP1000 | 0.36 | 0.20 | 17.7% | 80% | bull-only |
| `rank(fn_comp_options_exercisable_weighted_avg_a / close)` | TOP200 | 0.30 | 0.17 | 37.4% | 80% | bull-only |
| `rank(fn_comp_options_exercisable_weighted_avg_a / close)` | TOP500 | 0.21 | 0.09 | 21.8% | 40% | bull-only |
| `rank(fn_comp_options_exercisable_weighted_avg_a)` | TOP3000 | 0.12 | 0.04 | 30.2% | 40% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_optprcwa: 0.965 (strongly positively correlated)
- fnd6_optprcby: 0.963 (strongly positively correlated)
- fn_comp_options_out_weighted_avg_a: 0.960 (strongly positively correlated)
- fnd6_optprcey: 0.954 (strongly positively correlated)
- fnd6_optprcca: 0.940 (strongly positively correlated)

Redundancy cluster #12: 12 similar fields, mean |rho| 0.749 (representative: fnd6_dlto). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
