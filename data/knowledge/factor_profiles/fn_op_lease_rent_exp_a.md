---
field: fn_op_lease_rent_exp_a
dataset: fundamental2
cluster: fundamental2_income_expense
coverage: 0.6377
community_alphas: 2400
best_template: rank_value_norm
best_sharpe: 1.05
best_fitness: 0.78
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 4
max_drawdown: 0.0716
ann_vol: 0.0667
hit_rate: 0.4939
rolling_sharpe_min: -1.186
rolling_sharpe_max: 2.993
top_merge_partner: anl4_epsr_flag
redundancy_cluster: 1
negated_best_sharpe: 0.18
negated_best_template: rank_neg_delta
negated_best_fitness: 0.07
n_negated_sims: 10
direction_gap: -0.87
---
# fn_op_lease_rent_exp_a (fundamental2)

*Rental expense for the reporting period incurred under operating leases, including minimum and any contingent rent expense, net of related sublease income.*

## Signal Profile
- `rank(fn_op_lease_rent_exp_a)`: S=0.77, F=0.55, T=0.7%, INFERIOR (TOP3000)
- `rank(fn_op_lease_rent_exp_a / close)`: S=1.05, F=0.78, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_delta(fn_op_lease_rent_exp_a, 5))`: S=0.00, F=0.00, T=23.3%, INFERIOR (TOP3000)
- `-rank(fn_op_lease_rent_exp_a)`: S=-0.27, F=-0.12, T=1.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_op_lease_rent_exp_a, 5))`: S=0.18, F=0.07, T=17.0%, INFERIOR (TOP3000)
- `-ts_zscore(fn_op_lease_rent_exp_a, 63)`: S=-0.13, F=-0.05, T=11.8%, INFERIOR (TOP3000)
- `ts_mean(fn_op_lease_rent_exp_a, 10)`: S=0.43, F=0.21, T=0.7%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_op_lease_rent_exp_a, 22))`: S=-1.20, F=-1.55, T=10.1%, INFERIOR (TOP3000)
- `rank(-1 * fn_op_lease_rent_exp_a)`: S=-0.27, F=-0.12, T=1.2%, INFERIOR (TOP3000)
- `rank(-1 * fn_op_lease_rent_exp_a / close)`: S=-0.46, F=-0.26, T=1.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 18F/11P
- LOW_TURNOVER: 2F/30P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 1.03, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.57 (moderate), ret=+2.9%
  - 2020: S=1.39 (moderate), ret=+12.8%
  - 2021: S=1.75 (strong), ret=+12.0%
  - 2022: S=0.94 (moderate), ret=+5.2%
  - 2023: S=0.18 (weak), ret=+0.8%

## Risk & Drawdown
- Max drawdown: 7.16% over 590 days (not yet recovered, ongoing at window end)
- Annualized: return +6.9%, volatility 6.7% (fraction of booksize)
- Hit rate: 49.4% positive days
- Tail shape: skew +0.95, excess kurtosis +5.03

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.19, max 2.99, latest 0.32

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2023
Best month: +6.05%; worst month: -3.38%
Positive months: 64%

## Regime Profile
Regime profile: **mixed**
- Bull: S=2.46
- Sideways: S=0.33
- Bear: S=0.13

## Negated Direction
Best negated: `rank(-1 * ts_delta(fn_op_lease_rent_exp_a, 5))` S=0.18, F=0.07, INFERIOR
Direction gap: -0.87 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fn_op_lease_rent_exp_a)`: S=-0.27, F=-0.12, T=1.2%, INFERIOR (TOP3000)
- `rank(-1 * fn_op_lease_rent_exp_a / close)`: S=-0.46, F=-0.26, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_op_lease_rent_exp_a, 5))`: S=0.18, F=0.07, T=17.0%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fn_op_lease_rent_exp_a / close)` | TOP3000 | 1.03 | 0.78 | 7.2% | 100% | mixed |
| `rank(fn_op_lease_rent_exp_a)` | TOP3000 | 0.76 | 0.55 | 17.5% | 80% | bull-only |
| `rank(fn_op_lease_rent_exp_a / close)` | TOP1000 | 0.45 | 0.26 | 10.7% | 60% | bull-only |
| `rank(fn_op_lease_rent_exp_a)` | TOP1000 | 0.26 | 0.12 | 26.8% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd2_oprlsfmpdcurr: 0.941 (strongly positively correlated)
- fnd6_xopr: 0.918 (strongly positively correlated)
- fnd2_dfdtxastxdfdexprssaccrs: 0.917 (strongly positively correlated)
- fn_op_lease_min_pay_due_a: 0.911 (strongly positively correlated)
- fn_interest_paid_net_a: 0.902 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_epsr_flag | analyst4 | -0.39 | 1.94 | +0.76 | -0.62 | yes |
| rp_ess_revenue | news18 | -0.33 | 1.57 | +0.55 | -0.29 | yes |
| anl4_rd_exp_flag | analyst4 | -0.19 | 1.56 | +0.53 | +0.35 | yes |
| est_rd_expense | analyst4 | -0.15 | 1.64 | +0.53 | +0.83 | yes |
| anl4_capex_high | analyst4 | -0.19 | 1.53 | +0.50 | +0.09 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
