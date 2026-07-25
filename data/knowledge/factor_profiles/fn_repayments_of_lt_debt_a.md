---
field: fn_repayments_of_lt_debt_a
dataset: fundamental2
best_template: rank_value_norm
best_sharpe: 1.15
best_fitness: 0.71
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 7
max_drawdown: 0.052
ann_vol: 0.0415
hit_rate: 0.5134
rolling_sharpe_min: -0.727
rolling_sharpe_max: 2.784
top_merge_partner: pv13_ompetitorgraphrank_hub_rank
redundancy_cluster: 1
negated_best_sharpe: 0.31
negated_best_template: rank_neg_delta
negated_best_fitness: 0.14
n_negated_sims: 10
direction_gap: -0.84
---
# fn_repayments_of_lt_debt_a (fundamental2)

*The cash outflow for debt initially having maturity due after 1 year or beyond the normal operating cycle, if longer.*

## Signal Profile
- `rank(fn_repayments_of_lt_debt_a)`: S=0.67, F=0.34, T=0.8%, INFERIOR (TOP3000)
- `rank(fn_repayments_of_lt_debt_a / close)`: S=1.15, F=0.71, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_delta(fn_repayments_of_lt_debt_a, 5))`: S=0.48, F=0.24, T=33.2%, INFERIOR (TOP1000)
- `-rank(fn_repayments_of_lt_debt_a)`: S=-0.63, F=-0.32, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_repayments_of_lt_debt_a, 5))`: S=0.31, F=0.14, T=25.3%, INFERIOR (TOP3000)
- `ts_zscore(fn_repayments_of_lt_debt_a, 22)`: S=-0.22, F=-0.10, T=16.4%, INFERIOR (TOP3000)
- `ts_mean(fn_repayments_of_lt_debt_a, 10)`: S=-0.08, F=-0.01, T=0.9%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_repayments_of_lt_debt_a, 22))`: S=-0.15, F=-0.05, T=15.8%, INFERIOR (TOP3000)
- `rank(-1 * fn_repayments_of_lt_debt_a)`: S=0.00, F=0.00, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * fn_repayments_of_lt_debt_a / close)`: S=-0.05, F=-0.01, T=2.0%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/6P
- LOW_TURNOVER: 2F/30P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 1.14, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.66 (moderate), ret=+2.2%
  - 2020: S=1.24 (moderate), ret=+6.9%
  - 2021: S=2.04 (strong), ret=+8.1%
  - 2022: S=0.47 (weak), ret=+1.9%
  - 2023: S=1.43 (moderate), ret=+4.0%

## Risk & Drawdown
- Max drawdown: 5.20% over 246 days (recovered)
- Annualized: return +4.7%, volatility 4.2% (fraction of booksize)
- Hit rate: 51.3% positive days
- Tail shape: skew +0.55, excess kurtosis +2.85

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.73, max 2.78, latest 1.51

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2022
Best month: +3.49%; worst month: -3.01%
Positive months: 61%

## Regime Profile
Regime profile: **mixed**
- Bull: S=2.46
- Sideways: S=0.59
- Bear: S=0.25

## Negated Direction
Best negated: `rank(-1 * ts_delta(fn_repayments_of_lt_debt_a, 5))` S=0.31, F=0.14, INFERIOR
Direction gap: -0.84 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fn_repayments_of_lt_debt_a)`: S=0.00, F=0.00, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * fn_repayments_of_lt_debt_a / close)`: S=-0.05, F=-0.01, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_repayments_of_lt_debt_a, 5))`: S=0.31, F=0.14, T=25.3%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fn_repayments_of_lt_debt_a / close)` | TOP3000 | 1.14 | 0.71 | 5.2% | 100% | mixed |
| `rank(fn_repayments_of_lt_debt_a / close)` | TOP1000 | 0.86 | 0.53 | 6.0% | 100% | mixed |
| `rank(fn_repayments_of_lt_debt_a)` | TOP3000 | 0.66 | 0.34 | 9.3% | 80% | bull-only |
| `rank(fn_repayments_of_lt_debt_a)` | TOP1000 | 0.62 | 0.32 | 7.9% | 80% | bull-only |
| `rank(ts_delta(fn_repayments_of_lt_debt_a, 5))` | TOP1000 | 0.45 | 0.24 | 45.3% | 60% | mixed |
| `rank(fn_repayments_of_lt_debt_a / close)` | TOP500 | 0.42 | 0.19 | 12.3% | 80% | bull-only |
| `rank(fn_repayments_of_lt_debt_a)` | TOP500 | 0.10 | 0.03 | 18.5% | 80% | bull-only |

## Correlation Notes
Top correlates:
- fn_repayments_of_debt_a: 0.851 (strongly positively correlated)
- fn_interest_paid_net_a: 0.839 (strongly positively correlated)
- fn_op_lease_rent_exp_a: 0.825 (strongly positively correlated)
- fnd6_intpn: 0.820 (strongly positively correlated)
- fn_debt_instrument_carrying_amount_a: 0.817 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| pv13_ompetitorgraphrank_hub_rank | pv13 | -0.16 | 1.76 | +0.60 | +0.81 | yes |
| anl4_epsr_flag | analyst4 | -0.31 | 1.73 | +0.55 | -0.39 | yes |
| anl4_epsr_number | analyst4 | -0.13 | 1.69 | +0.50 | -0.76 | yes |
| anl4_netprofit_number | analyst4 | -0.12 | 1.68 | +0.50 | -0.16 | yes |
| est_rd_expense | analyst4 | -0.10 | 1.62 | +0.48 | +0.19 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
