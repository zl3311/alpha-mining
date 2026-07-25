---
field: fn_comp_options_out_number_a
dataset: fundamental2
best_template: rank_ts_rank
best_sharpe: 1.12
best_fitness: 1.0
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 7
max_drawdown: 0.1582
ann_vol: 0.0621
hit_rate: 0.5036
rolling_sharpe_min: -2.077
rolling_sharpe_max: 2.959
redundancy_cluster: 57
negated_best_sharpe: 0.47
negated_best_template: rank_neg_delta
negated_best_fitness: 0.29
n_negated_sims: 10
direction_gap: -0.65
---
# fn_comp_options_out_number_a (fundamental2)

*Number of options outstanding, including both vested and non-vested options.*

## Signal Profile
- `rank(fn_comp_options_out_number_a)`: S=0.67, F=0.34, T=1.4%, INFERIOR (TOP500)
- `rank(fn_comp_options_out_number_a / close)`: S=0.68, F=0.39, T=1.6%, INFERIOR (TOP500)
- `rank(ts_delta(fn_comp_options_out_number_a, 5))`: S=0.13, F=0.03, T=34.6%, INFERIOR (TOP1000)
- `-rank(fn_comp_options_out_number_a)`: S=-0.31, F=-0.10, T=1.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_comp_options_out_number_a, 5))`: S=0.47, F=0.29, T=29.2%, INFERIOR (TOP3000)
- `ts_zscore(fn_comp_options_out_number_a, 22)`: S=0.00, F=0.00, T=22.9%, INFERIOR (TOP3000)
- `ts_mean(fn_comp_options_out_number_a, 10)`: S=-0.29, F=-0.20, T=1.8%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_comp_options_out_number_a, 22))`: S=1.12, F=1.00, T=14.5%, INFERIOR (TOP3000)
- `rank(-1 * fn_comp_options_out_number_a)`: S=-0.35, F=-0.16, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * fn_comp_options_out_number_a / close)`: S=-0.37, F=-0.18, T=2.0%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 13F/19P
- LOW_FITNESS: 31F/1P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 7F/13P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.69, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=1.80 (strong), ret=+6.4%
  - 2020: S=2.64 (strong), ret=+16.2%
  - 2021: S=-1.13 (negative), ret=-8.3%
  - 2022: S=1.14 (moderate), ret=+8.4%
  - 2023: S=-0.34 (negative), ret=-1.7%

## Risk & Drawdown
- Max drawdown: 15.82% over 1019 days (not yet recovered, ongoing at window end)
- Annualized: return +4.2%, volatility 6.2% (fraction of booksize)
- Hit rate: 50.4% positive days
- Tail shape: skew +0.40, excess kurtosis +1.47

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.08, max 2.96, latest -0.29

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2021
Best month: +6.27%; worst month: -3.01%
Positive months: 59%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.27
- Sideways: S=-0.07
- Bear: S=1.93

## Negated Direction
Best negated: `rank(-1 * ts_delta(fn_comp_options_out_number_a, 5))` S=0.47, F=0.29, INFERIOR
Direction gap: -0.65 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fn_comp_options_out_number_a)`: S=-0.35, F=-0.16, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * fn_comp_options_out_number_a / close)`: S=-0.37, F=-0.18, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_comp_options_out_number_a, 5))`: S=0.47, F=0.29, T=29.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fn_comp_options_out_number_a / close)` | TOP500 | 0.69 | 0.39 | 15.8% | 60% | mixed |
| `rank(fn_comp_options_out_number_a)` | TOP500 | 0.67 | 0.34 | 13.4% | 60% | all-weather |
| `rank(fn_comp_options_out_number_a / close)` | TOP200 | 0.38 | 0.18 | 16.7% | 60% | mixed |
| `rank(fn_comp_options_out_number_a / close)` | TOP1000 | 0.38 | 0.16 | 20.0% | 60% | bear-only |
| `rank(fn_comp_options_out_number_a)` | TOP200 | 0.37 | 0.16 | 16.8% | 60% | all-weather |
| `rank(fn_comp_options_out_number_a)` | TOP1000 | 0.33 | 0.10 | 13.6% | 40% | mixed |
| `rank(ts_delta(fn_comp_options_out_number_a, 5))` | TOP1000 | 0.13 | 0.03 | 41.8% | 60% | mixed |

## Correlation Notes
Top correlates:
- fnd6_optosey: 0.846 (strongly positively correlated)
- fnd6_sstk: 0.680 (moderately positively correlated)
- anl4_fcf_number: 0.678 (moderately positively correlated)
- fn_antidilutive_securities_excl_from_eps_a: 0.665 (moderately positively correlated)
- anl4_afv4_cfps_number: 0.658 (moderately positively correlated)

Redundancy cluster #57: 2 similar fields, mean |rho| 0.846 (representative: fnd6_optosey). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
