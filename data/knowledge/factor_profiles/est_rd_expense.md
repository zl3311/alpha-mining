---
field: est_rd_expense
dataset: analyst4
best_template: ts_zscore
best_sharpe: 0.95
best_fitness: 0.54
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: all-weather
n_variations_with_pnl: 8
max_drawdown: 0.0633
ann_vol: 0.0669
hit_rate: 0.5117
rolling_sharpe_min: -0.506
rolling_sharpe_max: 2.989
top_merge_partner: fnd6_fopo
negated_best_sharpe: 0.26
negated_best_template: rank_neg_delta
negated_best_fitness: 0.08
n_negated_sims: 10
direction_gap: -0.69
---
# est_rd_expense (analyst4)

*Research and Development Expense - mean of estimations*

## Signal Profile
- `rank(est_rd_expense)`: S=0.67, F=0.49, T=1.2%, INFERIOR (TOP3000)
- `rank(est_rd_expense / close)`: S=0.41, F=0.22, T=1.9%, INFERIOR (TOP1000)
- `rank(ts_delta(est_rd_expense, 5))`: S=1.14, F=0.52, T=36.4%, INFERIOR (TOP3000)
- `-rank(est_rd_expense)`: S=-0.39, F=-0.24, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(est_rd_expense, 5))`: S=0.26, F=0.08, T=34.5%, INFERIOR (TOP3000)
- `ts_zscore(est_rd_expense, 22)`: S=0.95, F=0.54, T=33.6%, INFERIOR (TOP3000)
- `ts_mean(est_rd_expense, 10)`: S=0.15, F=0.07, T=1.0%, INFERIOR (TOP3000)
- `rank(ts_rank(est_rd_expense, 22))`: S=0.82, F=0.48, T=14.0%, INFERIOR (TOP3000)
- `rank(-1 * est_rd_expense)`: S=0.12, F=0.05, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * est_rd_expense / close)`: S=-0.03, F=-0.01, T=2.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 4F/28P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/6P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 1.11, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=1.41 (moderate), ret=+8.4%
  - 2020: S=1.34 (moderate), ret=+9.0%
  - 2021: S=1.99 (strong), ret=+14.0%
  - 2022: S=0.96 (moderate), ret=+6.4%
  - 2023: S=-0.21 (negative), ret=-1.3%

## Risk & Drawdown
- Max drawdown: 6.33% over 147 days (recovered)
- Annualized: return +7.4%, volatility 6.7% (fraction of booksize)
- Hit rate: 51.2% positive days
- Tail shape: skew +0.22, excess kurtosis +2.69

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.51, max 2.99, latest -0.38

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2023
Best month: +5.08%; worst month: -3.68%
Positive months: 64%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=1.34
- Sideways: S=0.77
- Bear: S=1.23

## Negated Direction
Best negated: `rank(-1 * ts_delta(est_rd_expense, 5))` S=0.26, F=0.08, INFERIOR
Direction gap: -0.69 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * est_rd_expense)`: S=0.12, F=0.05, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * est_rd_expense / close)`: S=-0.03, F=-0.01, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(est_rd_expense, 5))`: S=0.26, F=0.08, T=34.5%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(est_rd_expense, 5))` | TOP3000 | 1.11 | 0.52 | 6.3% | 80% | all-weather |
| `rank(est_rd_expense)` | TOP3000 | 0.68 | 0.49 | 30.3% | 80% | bull-only |
| `rank(ts_delta(est_rd_expense, 5))` | TOP1000 | 0.72 | 0.30 | 10.9% | 60% | all-weather |
| `rank(est_rd_expense)` | TOP1000 | 0.39 | 0.24 | 36.8% | 80% | bull-only |
| `rank(est_rd_expense / close)` | TOP1000 | 0.41 | 0.22 | 14.1% | 80% | bull-only |
| `rank(est_rd_expense / close)` | TOP3000 | 0.40 | 0.21 | 16.8% | 80% | mixed |
| `rank(est_rd_expense / close)` | TOP500 | 0.37 | 0.19 | 25.2% | 60% | bull-only |
| `rank(est_rd_expense)` | TOP500 | 0.13 | 0.04 | 51.9% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fn_comp_options_out_weighted_avg_a: -0.208 (weakly negatively correlated)
- fnd2_a_sbcpnargtbysbpmtwpwrr: -0.208 (weakly negatively correlated)
- fn_oth_comp_forfeitures_fair_value_a: -0.202 (weakly negatively correlated)
- fn_oth_comp_grants_weighted_avg_grant_date_fair_value_a: -0.192 (weakly negatively correlated)
- fn_comp_options_exercisable_weighted_avg_a: -0.191 (weakly negatively correlated)

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| fnd6_fopo | fundamental6 | -0.11 | 1.64 | +0.53 | -0.61 | yes |
| fnd2_a_bnsacqproformarvn | fundamental2 | -0.13 | 1.69 | +0.57 | -0.12 | yes |
| fnd6_fatl | fundamental_capital_intensity | -0.15 | 1.81 | +0.57 | +0.94 | yes |
| fn_accrued_liab_q | fundamental2 | -0.14 | 1.73 | +0.57 | +0.25 | yes |
| fn_proceeds_from_issuance_of_debt_a | fundamental2 | -0.15 | 1.76 | +0.56 | +0.18 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
