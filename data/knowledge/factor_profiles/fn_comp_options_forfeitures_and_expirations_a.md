---
field: fn_comp_options_forfeitures_and_expirations_a
dataset: fundamental2
best_template: rank_level
best_sharpe: 1.13
best_fitness: 0.85
best_universe: TOP200
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: all-weather
n_variations_with_pnl: 7
max_drawdown: 0.0732
ann_vol: 0.0629
hit_rate: 0.5296
rolling_sharpe_min: -0.761
rolling_sharpe_max: 3.056
top_merge_partner: anl4_ptpr_flag
negated_best_sharpe: 0.39
negated_best_template: rank_neg_delta
negated_best_fitness: 0.18
n_negated_sims: 10
direction_gap: -0.74
---
# fn_comp_options_forfeitures_and_expirations_a (fundamental2)

*For presentations that combine terminations, the number of shares under options that were canceled during the reporting period as a result of occurrence of a terminating event specified in contractual agreements pertaining to the stock option plan or that expired.*

## Signal Profile
- `rank(fn_comp_options_forfeitures_and_expirations_a)`: S=1.13, F=0.85, T=1.7%, INFERIOR (TOP200)
- `rank(fn_comp_options_forfeitures_and_expirations_a / close)`: S=0.87, F=0.61, T=1.9%, INFERIOR (TOP200)
- `rank(ts_delta(fn_comp_options_forfeitures_and_expirations_a, 5))`: S=0.47, F=0.22, T=34.2%, INFERIOR (TOP3000)
- `-rank(fn_comp_options_forfeitures_and_expirations_a)`: S=-0.50, F=-0.21, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_comp_options_forfeitures_and_expirations_a, 5))`: S=0.39, F=0.18, T=34.1%, INFERIOR (TOP3000)
- `ts_zscore(fn_comp_options_forfeitures_and_expirations_a, 22)`: S=0.41, F=0.28, T=19.1%, INFERIOR (TOP3000)
- `ts_mean(fn_comp_options_forfeitures_and_expirations_a, 10)`: S=-0.98, F=-1.23, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_comp_options_forfeitures_and_expirations_a, 22))`: S=0.21, F=0.09, T=15.0%, INFERIOR (TOP3000)
- `rank(-1 * fn_comp_options_forfeitures_and_expirations_a)`: S=-0.50, F=-0.21, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * fn_comp_options_forfeitures_and_expirations_a / close)`: S=-0.40, F=-0.18, T=1.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 13F/19P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/16P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 1.17, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=-0.07 (negative), ret=-0.3%
  - 2020: S=2.42 (strong), ret=+17.4%
  - 2021: S=0.26 (weak), ret=+1.5%
  - 2022: S=0.78 (moderate), ret=+5.3%
  - 2023: S=1.96 (strong), ret=+12.0%

## Risk & Drawdown
- Max drawdown: 7.32% over 352 days (recovered)
- Annualized: return +7.3%, volatility 6.3% (fraction of booksize)
- Hit rate: 53.0% positive days
- Tail shape: skew +0.14, excess kurtosis +1.65

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.76, max 3.06, latest 1.92

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2019
Best month: +4.63%; worst month: -3.63%
Positive months: 63%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=1.23
- Sideways: S=-0.09
- Bear: S=2.33

## Negated Direction
Best negated: `rank(-1 * ts_delta(fn_comp_options_forfeitures_and_expirations_a, 5))` S=0.39, F=0.18, INFERIOR
Direction gap: -0.74 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fn_comp_options_forfeitures_and_expirations_a)`: S=-0.50, F=-0.21, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * fn_comp_options_forfeitures_and_expirations_a / close)`: S=-0.40, F=-0.18, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_comp_options_forfeitures_and_expirations_a, 5))`: S=0.39, F=0.18, T=34.1%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fn_comp_options_forfeitures_and_expirations_a)` | TOP200 | 1.17 | 0.85 | 7.3% | 80% | all-weather |
| `rank(fn_comp_options_forfeitures_and_expirations_a / close)` | TOP200 | 0.90 | 0.61 | 9.1% | 100% | all-weather |
| `rank(fn_comp_options_forfeitures_and_expirations_a)` | TOP500 | 0.60 | 0.28 | 8.9% | 80% | mixed |
| `rank(fn_comp_options_forfeitures_and_expirations_a / close)` | TOP500 | 0.51 | 0.24 | 10.6% | 80% | mixed |
| `rank(ts_delta(fn_comp_options_forfeitures_and_expirations_a, 5))` | TOP3000 | 0.48 | 0.22 | 37.2% | 80% | mixed |
| `rank(fn_comp_options_forfeitures_and_expirations_a)` | TOP1000 | 0.51 | 0.21 | 10.8% | 60% | bear-only |
| `rank(fn_comp_options_forfeitures_and_expirations_a / close)` | TOP1000 | 0.40 | 0.18 | 17.8% | 60% | bear-only |

## Correlation Notes
Top correlates:
- fnd2_a_sbcpnargmpmtwopsffesip: 0.653 (moderately positively correlated)
- fn_antidilutive_securities_excl_from_eps_a: 0.516 (moderately positively correlated)
- fnd6_cshtrq: 0.510 (moderately positively correlated)
- fnd6_optex: 0.488 (moderately positively correlated)
- fn_comp_options_out_number_q: 0.483 (moderately positively correlated)

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_ptpr_flag | analyst_revision | -0.26 | 2.01 | +0.73 | -0.89 | yes |
| rel_num_all | pv13 | -0.23 | 1.92 | +0.70 | -0.91 | yes |
| anl4_bvps_flag | analyst_revision | -0.25 | 2.00 | +0.70 | -0.86 | yes |
| anl4_netdebt_flag | analyst_revision | -0.24 | 1.98 | +0.71 | -0.69 | yes |
| anl4_tbve_ft | analyst_estimate | -0.24 | 1.96 | +0.71 | -0.68 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
