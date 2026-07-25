---
field: fnd2_dfdtxastxdfdexpcompbnf
dataset: fundamental2
best_template: rank_value_norm
best_sharpe: 0.91
best_fitness: 0.62
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: all-weather
n_variations_with_pnl: 6
max_drawdown: 0.0721
ann_vol: 0.0646
hit_rate: 0.502
rolling_sharpe_min: -1.08
rolling_sharpe_max: 2.609
top_merge_partner: anl4_epsr_flag
redundancy_cluster: 33
negated_best_sharpe: 0.84
negated_best_template: rank_neg_delta
negated_best_fitness: 0.51
n_negated_sims: 10
direction_gap: -0.07
---
# fnd2_dfdtxastxdfdexpcompbnf (fundamental2)

*Amount before allocation of valuation allowances of deferred tax asset attributable to deductible temporary differences from compensation and benefits costs.*

## Signal Profile
- `rank(fnd2_dfdtxastxdfdexpcompbnf)`: S=0.76, F=0.52, T=0.9%, INFERIOR (TOP3000)
- `rank(fnd2_dfdtxastxdfdexpcompbnf / close)`: S=0.91, F=0.62, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd2_dfdtxastxdfdexpcompbnf, 5))`: S=-0.32, F=-0.12, T=34.6%, INFERIOR (TOP1000)
- `-rank(fnd2_dfdtxastxdfdexpcompbnf)`: S=-0.25, F=-0.11, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_dfdtxastxdfdexpcompbnf, 5))`: S=0.84, F=0.51, T=33.7%, INFERIOR (TOP3000)
- `-ts_zscore(fnd2_dfdtxastxdfdexpcompbnf, 63)`: S=0.31, F=0.16, T=17.1%, INFERIOR (TOP3000)
- `ts_mean(fnd2_dfdtxastxdfdexpcompbnf, 10)`: S=-0.15, F=-0.05, T=0.9%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd2_dfdtxastxdfdexpcompbnf, 22))`: S=-0.24, F=-0.09, T=15.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_dfdtxastxdfdexpcompbnf)`: S=-0.11, F=-0.03, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_dfdtxastxdfdexpcompbnf / close)`: S=-0.43, F=-0.22, T=1.8%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 12F/17P
- LOW_TURNOVER: 2F/30P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.91, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.34 (weak), ret=+1.5%
  - 2020: S=1.15 (moderate), ret=+8.8%
  - 2021: S=1.68 (strong), ret=+10.5%
  - 2022: S=0.73 (moderate), ret=+4.7%
  - 2023: S=0.49 (weak), ret=+3.2%

## Risk & Drawdown
- Max drawdown: 7.21% over 591 days (not yet recovered, ongoing at window end)
- Annualized: return +5.9%, volatility 6.5% (fraction of booksize)
- Hit rate: 50.2% positive days
- Tail shape: skew +0.68, excess kurtosis +2.64

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.08, max 2.61, latest 0.67

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2019
Best month: +6.49%; worst month: -3.51%
Positive months: 54%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=1.81
- Sideways: S=-0.27
- Bear: S=1.00

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd2_dfdtxastxdfdexpcompbnf, 5))` S=0.84, F=0.51, INFERIOR
Direction gap: -0.07 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd2_dfdtxastxdfdexpcompbnf)`: S=-0.11, F=-0.03, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_dfdtxastxdfdexpcompbnf / close)`: S=-0.43, F=-0.22, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_dfdtxastxdfdexpcompbnf, 5))`: S=0.84, F=0.51, T=33.7%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd2_dfdtxastxdfdexpcompbnf / close)` | TOP3000 | 0.91 | 0.62 | 7.2% | 100% | all-weather |
| `rank(fnd2_dfdtxastxdfdexpcompbnf)` | TOP3000 | 0.76 | 0.52 | 18.6% | 80% | bull-only |
| `rank(fnd2_dfdtxastxdfdexpcompbnf / close)` | TOP1000 | 0.54 | 0.31 | 10.1% | 40% | bull-only |
| `rank(fnd2_dfdtxastxdfdexpcompbnf / close)` | TOP500 | 0.42 | 0.22 | 15.7% | 80% | bull-only |
| `rank(fnd2_dfdtxastxdfdexpcompbnf)` | TOP1000 | 0.24 | 0.11 | 28.0% | 60% | bull-only |
| `rank(fnd2_dfdtxastxdfdexpcompbnf)` | TOP500 | 0.10 | 0.03 | 34.5% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd2_oprlsfmpdcurr: 0.930 (strongly positively correlated)
- fn_op_lease_min_pay_due_a: 0.918 (strongly positively correlated)
- fn_op_lease_min_pay_due_in_5y_a: 0.901 (strongly positively correlated)
- fn_op_lease_rent_exp_a: 0.888 (strongly positively correlated)
- selling_general_admin_expense_actual_value: 0.886 (strongly positively correlated)

Redundancy cluster #33: 12 similar fields, mean |rho| 0.787 (representative: anl4_afv4_eps_high). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_epsr_flag | analyst4 | -0.35 | 1.80 | +0.62 | -0.61 | yes |
| rp_ess_revenue | news18 | -0.26 | 1.42 | +0.51 | -0.41 | yes |
| anl4_capex_high | analyst4 | -0.19 | 1.43 | +0.50 | -0.03 | yes |
| rp_css_revenue | news18 | -0.23 | 1.39 | +0.48 | +0.26 | yes |
| max_gross_income_guidance_2 | analyst4 | -0.21 | 1.30 | +0.39 | -0.80 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
