---
field: fn_op_lease_min_pay_due_in_3y_a
dataset: fundamental2
best_template: rank_level
best_sharpe: 0.81
best_fitness: 0.57
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 7
max_drawdown: 0.151
ann_vol: 0.0765
hit_rate: 0.5223
rolling_sharpe_min: -1.705
rolling_sharpe_max: 2.317
top_merge_partner: max_adjusted_net_profit_guidance
redundancy_cluster: 13
negated_best_sharpe: 0.92
negated_best_template: rank_neg_delta
negated_best_fitness: 0.57
n_negated_sims: 10
direction_gap: 0.11
---
# fn_op_lease_min_pay_due_in_3y_a (fundamental2)

*Amount of required minimum rental payments for operating leases having an initial or remaining non-cancelable lease term in excess of one year due in the 3rd fiscal year following the latest fiscal year. Excludes interim and annual periods when interim periods are reported on a rolling approach, from latest balance sheet date.*

## Signal Profile
- `rank(fn_op_lease_min_pay_due_in_3y_a)`: S=0.81, F=0.57, T=0.9%, INFERIOR (TOP3000)
- `rank(fn_op_lease_min_pay_due_in_3y_a / close)`: S=0.81, F=0.55, T=1.3%, INFERIOR (TOP3000)
- `rank(ts_delta(fn_op_lease_min_pay_due_in_3y_a, 5))`: S=0.20, F=0.07, T=31.3%, INFERIOR (TOP200)
- `-rank(fn_op_lease_min_pay_due_in_3y_a)`: S=-0.50, F=-0.30, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_op_lease_min_pay_due_in_3y_a, 5))`: S=0.92, F=0.57, T=34.5%, INFERIOR (TOP3000)
- `-ts_zscore(fn_op_lease_min_pay_due_in_3y_a, 63)`: S=0.72, F=0.57, T=16.8%, INFERIOR (TOP3000)
- `ts_mean(fn_op_lease_min_pay_due_in_3y_a, 10)`: S=0.58, F=0.39, T=0.8%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_op_lease_min_pay_due_in_3y_a, 22))`: S=-0.48, F=-0.27, T=14.6%, INFERIOR (TOP3000)
- `rank(-1 * fn_op_lease_min_pay_due_in_3y_a)`: S=-0.50, F=-0.30, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * fn_op_lease_min_pay_due_in_3y_a / close)`: S=-0.53, F=-0.30, T=1.6%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 13F/19P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 12F/17P
- LOW_TURNOVER: 2F/30P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.80, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=1.18 (moderate), ret=+4.6%
  - 2020: S=0.05 (weak), ret=+0.3%
  - 2021: S=0.98 (moderate), ret=+11.2%
  - 2022: S=1.19 (moderate), ret=+10.5%
  - 2023: S=0.64 (moderate), ret=+3.5%

## Risk & Drawdown
- Max drawdown: 15.10% over 185 days (recovered)
- Annualized: return +6.2%, volatility 7.6% (fraction of booksize)
- Hit rate: 52.2% positive days
- Tail shape: skew +0.00, excess kurtosis +2.01

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.71, max 2.32, latest 0.45

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +5.26%; worst month: -4.38%
Positive months: 63%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.74
- Sideways: S=1.52
- Bear: S=-2.26

## Negated Direction
Best negated: `rank(-1 * ts_delta(fn_op_lease_min_pay_due_in_3y_a, 5))` S=0.92, F=0.57, INFERIOR
Direction gap: +0.11 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fn_op_lease_min_pay_due_in_3y_a)`: S=-0.50, F=-0.30, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * fn_op_lease_min_pay_due_in_3y_a / close)`: S=-0.53, F=-0.30, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_op_lease_min_pay_due_in_3y_a, 5))`: S=0.92, F=0.57, T=34.5%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fn_op_lease_min_pay_due_in_3y_a)` | TOP3000 | 0.80 | 0.57 | 15.1% | 100% | bull-only |
| `rank(fn_op_lease_min_pay_due_in_3y_a / close)` | TOP3000 | 0.80 | 0.55 | 10.2% | 80% | all-weather |
| `rank(fn_op_lease_min_pay_due_in_3y_a)` | TOP1000 | 0.49 | 0.30 | 21.1% | 80% | bull-only |
| `rank(fn_op_lease_min_pay_due_in_3y_a / close)` | TOP1000 | 0.53 | 0.30 | 7.9% | 80% | bull-only |
| `rank(fn_op_lease_min_pay_due_in_3y_a / close)` | TOP500 | 0.24 | 0.09 | 15.6% | 60% | bull-only |
| `rank(ts_delta(fn_op_lease_min_pay_due_in_3y_a, 5))` | TOP200 | 0.20 | 0.07 | 28.9% | 80% | bull-only |
| `rank(fn_op_lease_min_pay_due_in_3y_a)` | TOP500 | 0.10 | 0.03 | 32.6% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fn_op_lease_min_pay_due_in_2y_a: 0.996 (strongly positively correlated)
- fn_op_lease_min_pay_due_in_4y_a: 0.994 (strongly positively correlated)
- fnd6_mrc3: 0.980 (strongly positively correlated)
- fnd6_mrc2: 0.979 (strongly positively correlated)
- fnd6_mrc4: 0.976 (strongly positively correlated)

Redundancy cluster #13: 127 similar fields, mean |rho| 0.82 (representative: anl4_bvps_flag). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| max_adjusted_net_profit_guidance | analyst4 | -0.34 | 1.39 | +0.58 | -0.91 | yes |
| anl4_rd_exp_flag | analyst4 | -0.35 | 1.60 | +0.57 | -0.97 | yes |
| anl4_afv4_dts_spe | analyst4 | -0.40 | 1.64 | +0.64 | -0.15 | yes |
| net_profit_adjusted_min_guidance | analyst4 | -0.29 | 1.47 | +0.53 | -0.87 | yes |
| rank(fnd6_acdo) + rank(open/close - 1) | unknown | -0.31 | 2.50 | +0.48 | -0.77 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
