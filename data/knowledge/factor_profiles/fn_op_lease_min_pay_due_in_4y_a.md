---
field: fn_op_lease_min_pay_due_in_4y_a
dataset: fundamental2
best_template: rank_level
best_sharpe: 0.88
best_fitness: 0.62
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 5
max_drawdown: 0.1357
ann_vol: 0.0703
hit_rate: 0.5304
rolling_sharpe_min: -1.544
rolling_sharpe_max: 2.398
top_merge_partner: anl4_afv4_dts_spe
redundancy_cluster: 13
negated_best_sharpe: 0.35
negated_best_template: rank_neg_delta
negated_best_fitness: 0.15
n_negated_sims: 10
direction_gap: -0.53
---
# fn_op_lease_min_pay_due_in_4y_a (fundamental2)

*Amount of required minimum rental payments for operating leases having an initial or remaining non-cancelable lease term in excess of 1 year due in the 4th fiscal year following the latest fiscal year. Excludes interim and annual periods when interim periods are reported on a rolling approach, from latest balance sheet date.*

## Signal Profile
- `rank(fn_op_lease_min_pay_due_in_4y_a)`: S=0.88, F=0.62, T=0.9%, INFERIOR (TOP3000)
- `rank(fn_op_lease_min_pay_due_in_4y_a / close)`: S=0.87, F=0.60, T=1.3%, INFERIOR (TOP3000)
- `rank(ts_delta(fn_op_lease_min_pay_due_in_4y_a, 5))`: S=-0.16, F=-0.05, T=31.4%, INFERIOR (TOP200)
- `-rank(fn_op_lease_min_pay_due_in_4y_a)`: S=-0.48, F=-0.27, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_op_lease_min_pay_due_in_4y_a, 5))`: S=0.35, F=0.15, T=34.2%, INFERIOR (TOP3000)
- `-ts_zscore(fn_op_lease_min_pay_due_in_4y_a, 63)`: S=0.26, F=0.12, T=16.6%, INFERIOR (TOP3000)
- `ts_mean(fn_op_lease_min_pay_due_in_4y_a, 10)`: S=0.56, F=0.37, T=0.8%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_op_lease_min_pay_due_in_4y_a, 22))`: S=-0.23, F=-0.09, T=14.8%, INFERIOR (TOP3000)
- `rank(-1 * fn_op_lease_min_pay_due_in_4y_a)`: S=-0.02, F=0.00, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * fn_op_lease_min_pay_due_in_4y_a / close)`: S=-0.12, F=-0.03, T=1.9%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 13F/19P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 21F/8P
- LOW_TURNOVER: 2F/30P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.87, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=1.43 (moderate), ret=+5.5%
  - 2020: S=0.10 (weak), ret=+0.5%
  - 2021: S=1.06 (moderate), ret=+11.0%
  - 2022: S=1.23 (moderate), ret=+9.9%
  - 2023: S=0.61 (moderate), ret=+3.2%

## Risk & Drawdown
- Max drawdown: 13.57% over 185 days (recovered)
- Annualized: return +6.1%, volatility 7.0% (fraction of booksize)
- Hit rate: 53.0% positive days
- Tail shape: skew -0.05, excess kurtosis +1.84

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.54, max 2.40, latest 0.42

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2020
Best month: +4.70%; worst month: -3.95%
Positive months: 63%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.80
- Sideways: S=1.55
- Bear: S=-2.12

## Negated Direction
Best negated: `rank(-1 * ts_delta(fn_op_lease_min_pay_due_in_4y_a, 5))` S=0.35, F=0.15, INFERIOR
Direction gap: -0.53 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fn_op_lease_min_pay_due_in_4y_a)`: S=-0.02, F=0.00, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * fn_op_lease_min_pay_due_in_4y_a / close)`: S=-0.12, F=-0.03, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_op_lease_min_pay_due_in_4y_a, 5))`: S=0.35, F=0.15, T=34.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fn_op_lease_min_pay_due_in_4y_a)` | TOP3000 | 0.87 | 0.62 | 13.6% | 100% | bull-only |
| `rank(fn_op_lease_min_pay_due_in_4y_a / close)` | TOP3000 | 0.86 | 0.60 | 9.4% | 80% | all-weather |
| `rank(fn_op_lease_min_pay_due_in_4y_a / close)` | TOP1000 | 0.53 | 0.30 | 7.0% | 80% | mixed |
| `rank(fn_op_lease_min_pay_due_in_4y_a)` | TOP1000 | 0.48 | 0.27 | 19.2% | 80% | bull-only |
| `rank(fn_op_lease_min_pay_due_in_4y_a / close)` | TOP500 | 0.12 | 0.03 | 14.4% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fn_op_lease_min_pay_due_in_3y_a: 0.994 (strongly positively correlated)
- fn_op_lease_min_pay_due_in_2y_a: 0.989 (strongly positively correlated)
- fnd6_mrc3: 0.973 (strongly positively correlated)
- fnd6_mrc4: 0.972 (strongly positively correlated)
- fnd6_mrc2: 0.970 (strongly positively correlated)

Redundancy cluster #13: 127 similar fields, mean |rho| 0.82 (representative: anl4_bvps_flag). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_afv4_dts_spe | analyst4 | -0.39 | 1.67 | +0.67 | -0.12 | yes |
| anl4_rd_exp_flag | analyst4 | -0.34 | 1.62 | +0.59 | -0.93 | yes |
| net_profit_adjusted_min_guidance | analyst4 | -0.28 | 1.50 | +0.56 | -0.82 | yes |
| max_adjusted_net_profit_guidance | analyst4 | -0.33 | 1.42 | +0.54 | -0.85 | yes |
| rank(fnd6_acdo) + rank(open/close - 1) | unknown | -0.30 | 2.55 | +0.53 | -0.86 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
