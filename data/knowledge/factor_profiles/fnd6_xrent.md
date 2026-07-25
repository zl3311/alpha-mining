---
field: fnd6_xrent
dataset: fundamental6
best_template: rank_level
best_sharpe: 0.94
best_fitness: 0.77
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 9
max_drawdown: 0.1814
ann_vol: 0.09
hit_rate: 0.5174
rolling_sharpe_min: -2.32
rolling_sharpe_max: 2.543
top_merge_partner: anl4_rd_exp_flag
redundancy_cluster: 13
negated_best_sharpe: 0.21
negated_best_template: neg_rank_level
negated_best_fitness: 0.11
n_negated_sims: 10
direction_gap: -0.73
---
# fnd6_xrent (fundamental6)

*Rental Expense*

## Signal Profile
- `rank(fnd6_xrent)`: S=0.94, F=0.77, T=1.9%, INFERIOR (TOP3000)
- `rank(fnd6_xrent / close)`: S=1.00, F=0.76, T=2.2%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_xrent, 5))`: S=0.35, F=0.16, T=35.4%, INFERIOR (TOP500)
- `-rank(fnd6_xrent)`: S=-0.40, F=-0.23, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_xrent, 5))`: S=-0.27, F=-0.12, T=28.7%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_xrent, 63)`: S=0.56, F=0.37, T=19.7%, INFERIOR (TOP3000)
- `ts_mean(fnd6_xrent, 10)`: S=0.17, F=0.05, T=1.7%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_xrent, 22))`: S=0.29, F=0.11, T=20.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_xrent)`: S=0.21, F=0.11, T=3.6%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_xrent / close)`: S=0.03, F=0.00, T=3.7%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/6P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.94, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.74 (moderate), ret=+3.6%
  - 2020: S=-0.98 (negative), ret=-5.6%
  - 2021: S=1.41 (moderate), ret=+18.2%
  - 2022: S=1.69 (strong), ret=+18.9%
  - 2023: S=0.92 (moderate), ret=+6.1%

## Risk & Drawdown
- Max drawdown: 18.14% over 539 days (recovered)
- Annualized: return +8.4%, volatility 9.0% (fraction of booksize)
- Hit rate: 51.7% positive days
- Tail shape: skew +0.05, excess kurtosis +2.45

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.32, max 2.54, latest 0.73

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +6.53%; worst month: -3.18%
Positive months: 58%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.96
- Sideways: S=1.44
- Bear: S=-2.22

## Negated Direction
Best negated: `rank(-1 * fnd6_xrent)` S=0.21, F=0.11, INFERIOR
Direction gap: -0.73 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_xrent)`: S=0.21, F=0.11, T=3.6%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_xrent / close)`: S=0.03, F=0.00, T=3.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_xrent, 5))`: S=-0.27, F=-0.12, T=28.7%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_xrent)` | TOP3000 | 0.94 | 0.77 | 18.1% | 80% | bull-only |
| `rank(fnd6_xrent / close)` | TOP3000 | 0.99 | 0.76 | 7.7% | 100% | all-weather |
| `rank(fnd6_xrent / close)` | TOP1000 | 0.50 | 0.30 | 9.0% | 60% | bull-only |
| `rank(fnd6_xrent)` | TOP1000 | 0.40 | 0.23 | 25.6% | 60% | bull-only |
| `rank(ts_delta(fnd6_xrent, 5))` | TOP500 | 0.35 | 0.16 | 41.6% | 40% | mixed |
| `rank(ts_delta(fnd6_xrent, 5))` | TOP200 | 0.30 | 0.15 | 41.0% | 60% | mixed |
| `rank(ts_delta(fnd6_xrent, 5))` | TOP1000 | 0.39 | 0.15 | 32.1% | 80% | mixed |
| `rank(ts_delta(fnd6_xrent, 5))` | TOP3000 | 0.21 | 0.06 | 30.0% | 60% | weak |
| `rank(fnd6_xrent / close)` | TOP500 | 0.14 | 0.05 | 20.2% | 40% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_mrc2: 0.984 (strongly positively correlated)
- fnd6_mrc3: 0.976 (strongly positively correlated)
- fn_op_lease_min_pay_due_in_2y_a: 0.970 (strongly positively correlated)
- operating_expense: 0.968 (strongly positively correlated)
- fnd6_newqv1300_xoprq: 0.968 (strongly positively correlated)

Redundancy cluster #13: 127 similar fields, mean |rho| 0.82 (representative: anl4_bvps_flag). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_rd_exp_flag | analyst4 | -0.41 | 1.80 | +0.77 | -0.91 | yes |
| anl4_afv4_dts_spe | analyst4 | -0.42 | 1.79 | +0.79 | -0.30 | yes |
| net_profit_adjusted_min_guidance | analyst4 | -0.32 | 1.61 | +0.67 | -0.92 | yes |
| max_adjusted_net_profit_guidance | analyst4 | -0.37 | 1.55 | +0.61 | -0.97 | yes |
| rank(fnd6_acdo) + rank(open/close - 1) | unknown | -0.36 | 2.65 | +0.63 | -0.39 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
