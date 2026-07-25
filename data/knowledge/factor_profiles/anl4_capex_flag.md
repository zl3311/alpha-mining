---
field: anl4_capex_flag
dataset: analyst4
best_template: decay_linear
best_sharpe: 1.08
best_fitness: 0.7
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 35
regime_profile: all-weather
n_variations_with_pnl: 9
max_drawdown: 0.0759
ann_vol: 0.0487
hit_rate: 0.5385
rolling_sharpe_min: -0.882
rolling_sharpe_max: 2.557
top_merge_partner: fn_line_of_credit_facility_max_borrowing_capacity_a
redundancy_cluster: 18
negated_best_sharpe: 0.34
negated_best_template: rank_neg_delta
negated_best_fitness: 0.13
n_negated_sims: 10
direction_gap: -0.74
---
# anl4_capex_flag (analyst4)

*Capital Expenditures - forecast type (revision/new/...)*

## Signal Profile
- `rank(anl4_capex_flag)`: S=1.07, F=0.69, T=2.7%, INFERIOR (TOP3000)
- `rank(anl4_capex_flag / close)`: S=0.24, F=0.11, T=3.0%, INFERIOR (TOP200)
- `rank(ts_delta(anl4_capex_flag, 5))`: S=0.53, F=0.29, T=35.0%, INFERIOR (TOP500)
- `ts_decay_linear(rank(anl4_capex_flag), 5)`: S=1.08, F=0.70, T=2.6%, INFERIOR (TOP3000)
- `-rank(anl4_capex_flag)`: S=-0.29, F=-0.10, T=3.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_capex_flag, 5))`: S=0.34, F=0.13, T=36.3%, INFERIOR (TOP3000)
- `ts_zscore(anl4_capex_flag, 22)`: S=0.14, F=0.05, T=28.4%, INFERIOR (TOP3000)
- `ts_mean(anl4_capex_flag, 10)`: S=0.70, F=0.61, T=3.6%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_capex_flag, 22))`: S=0.53, F=0.31, T=17.2%, INFERIOR (TOP3000)
- `rank(-1 * anl4_capex_flag)`: S=-1.07, F=-0.69, T=2.7%, INFERIOR (TOP3000)
- `rank(-1 * anl4_capex_flag / close)`: S=-0.02, F=0.00, T=2.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 13F/22P
- LOW_FITNESS: 35F/0P
- LOW_SHARPE: 35F/0P
- LOW_SUB_UNIVERSE_SHARPE: 12F/20P

## Temporal Behavior
Headline (decay_linear): Overall Sharpe 1.09, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.96 (moderate), ret=+3.0%
  - 2020: S=0.75 (moderate), ret=+3.0%
  - 2021: S=0.96 (moderate), ret=+6.4%
  - 2022: S=0.80 (moderate), ret=+4.3%
  - 2023: S=2.30 (strong), ret=+9.3%

## Risk & Drawdown
- Max drawdown: 7.59% over 264 days (recovered)
- Annualized: return +5.3%, volatility 4.9% (fraction of booksize)
- Hit rate: 53.8% positive days
- Tail shape: skew -0.30, excess kurtosis +4.71

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.88, max 2.56, latest 2.43

## Yearly & Monthly Returns
Best year (by Sharpe): 2023; worst year: 2020
Best month: +4.07%; worst month: -2.09%
Positive months: 64%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=0.98
- Sideways: S=1.34
- Bear: S=1.08

## Negated Direction
Best negated: `rank(-1 * ts_delta(anl4_capex_flag, 5))` S=0.34, F=0.13, INFERIOR
Direction gap: -0.74 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * anl4_capex_flag)`: S=-1.07, F=-0.69, T=2.7%, INFERIOR (TOP3000)
- `rank(-1 * anl4_capex_flag / close)`: S=-0.02, F=0.00, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_capex_flag, 5))`: S=0.34, F=0.13, T=36.3%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `ts_decay_linear(rank(anl4_capex_flag), 5)` | TOP3000 | 1.09 | 0.70 | 7.6% | 100% | all-weather |
| `rank(anl4_capex_flag)` | TOP3000 | 1.08 | 0.69 | 7.6% | 100% | all-weather |
| `rank(ts_delta(anl4_capex_flag, 5))` | TOP500 | 0.52 | 0.29 | 42.5% | 60% | all-weather |
| `rank(anl4_capex_flag)` | TOP500 | 0.51 | 0.24 | 9.1% | 80% | bear-only |
| `rank(anl4_capex_flag)` | TOP200 | 0.33 | 0.16 | 20.7% | 80% | mixed |
| `rank(anl4_capex_flag / close)` | TOP200 | 0.25 | 0.11 | 20.5% | 60% | mixed |
| `rank(ts_delta(anl4_capex_flag, 5))` | TOP200 | 0.26 | 0.11 | 39.3% | 60% | mixed |
| `rank(anl4_capex_flag)` | TOP1000 | 0.29 | 0.10 | 13.7% | 80% | bear-only |
| `rank(ts_delta(anl4_capex_flag, 5))` | TOP1000 | 0.16 | 0.05 | 37.2% | 80% | weak |

## Correlation Notes
Top correlates:
- anl4_cfo_flag: 0.839 (strongly positively correlated)
- anl4_cff_flag: 0.802 (strongly positively correlated)
- anl4_cfi_flag: 0.800 (strongly positively correlated)
- anl4_totassets_flag: 0.772 (strongly positively correlated)
- anl4_fcf_flag: 0.744 (strongly positively correlated)

Redundancy cluster #18: 7 similar fields, mean |rho| 0.818 (representative: anl4_totassets_flag). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| fn_line_of_credit_facility_max_borrowing_capacity_a | fundamental2 | -0.09 | 1.60 | +0.51 | -0.65 | yes |
| fn_repayments_of_lt_debt_q | fundamental2 | -0.13 | 1.62 | +0.53 | -0.28 | yes |
| fn_repayments_of_debt_q | fundamental2 | -0.08 | 1.56 | +0.47 | -0.72 | yes |
| fnd6_rank | fundamental6 | -0.17 | 1.70 | +0.53 | +0.87 | yes |
| fn_comp_options_forfeitures_and_expirations_a | fundamental2 | -0.10 | 1.67 | +0.50 | +0.34 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: trade_when
