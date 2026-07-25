---
field: fn_accrued_liab_q
dataset: fundamental2
best_template: rank_value_norm
best_sharpe: 1.17
best_fitness: 0.99
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 10
max_drawdown: 0.1089
ann_vol: 0.0765
hit_rate: 0.4955
rolling_sharpe_min: -1.413
rolling_sharpe_max: 2.918
top_merge_partner: anl4_epsr_flag
redundancy_cluster: 1
negated_best_sharpe: 0.43
negated_best_template: neg_rank_level
negated_best_fitness: 0.34
n_negated_sims: 10
direction_gap: -0.74
---
# fn_accrued_liab_q (fundamental2)

*Carrying value as of the balance sheet date of obligations incurred and payable, pertaining to costs that are statutory in nature, are incurred on contractual obligations, or accumulate over time and for which invoices have not yet been received or will not be rendered.*

## Signal Profile
- `rank(fn_accrued_liab_q)`: S=0.96, F=0.87, T=1.1%, INFERIOR (TOP3000)
- `rank(fn_accrued_liab_q / close)`: S=1.17, F=0.99, T=1.5%, INFERIOR (TOP3000)
- `rank(ts_delta(fn_accrued_liab_q, 5))`: S=1.11, F=0.80, T=39.1%, INFERIOR (TOP500)
- `-rank(fn_accrued_liab_q)`: S=-0.60, F=-0.47, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_accrued_liab_q, 5))`: S=-0.35, F=-0.17, T=36.4%, INFERIOR (TOP3000)
- `ts_zscore(fn_accrued_liab_q, 22)`: S=0.43, F=0.24, T=29.8%, INFERIOR (TOP3000)
- `ts_mean(fn_accrued_liab_q, 10)`: S=0.22, F=0.10, T=0.9%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_accrued_liab_q, 22))`: S=0.51, F=0.26, T=16.2%, INFERIOR (TOP3000)
- `rank(-1 * fn_accrued_liab_q)`: S=0.43, F=0.34, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * fn_accrued_liab_q / close)`: S=0.39, F=0.25, T=2.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 5F/15P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 1.16, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=-0.23 (negative), ret=-1.4%
  - 2020: S=1.06 (moderate), ret=+10.1%
  - 2021: S=2.11 (strong), ret=+18.9%
  - 2022: S=1.69 (strong), ret=+11.2%
  - 2023: S=0.85 (moderate), ret=+4.7%

## Risk & Drawdown
- Max drawdown: 10.89% over 483 days (recovered)
- Annualized: return +8.9%, volatility 7.6% (fraction of booksize)
- Hit rate: 49.5% positive days
- Tail shape: skew +0.50, excess kurtosis +2.29

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.41, max 2.92, latest 1.02

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2019
Best month: +7.78%; worst month: -4.02%
Positive months: 56%

## Regime Profile
Regime profile: **mixed**
- Bull: S=2.93
- Sideways: S=-0.07
- Bear: S=0.28

## Negated Direction
Best negated: `rank(-1 * fn_accrued_liab_q)` S=0.43, F=0.34, INFERIOR
Direction gap: -0.74 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fn_accrued_liab_q)`: S=0.43, F=0.34, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * fn_accrued_liab_q / close)`: S=0.39, F=0.25, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_accrued_liab_q, 5))`: S=-0.35, F=-0.17, T=36.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fn_accrued_liab_q / close)` | TOP3000 | 1.16 | 0.99 | 10.9% | 80% | mixed |
| `rank(fn_accrued_liab_q)` | TOP3000 | 0.95 | 0.87 | 21.6% | 60% | bull-only |
| `rank(ts_delta(fn_accrued_liab_q, 5))` | TOP500 | 1.11 | 0.80 | 18.7% | 60% | all-weather |
| `rank(fn_accrued_liab_q / close)` | TOP1000 | 0.79 | 0.63 | 9.8% | 100% | bull-only |
| `rank(fn_accrued_liab_q / close)` | TOP500 | 0.67 | 0.52 | 15.3% | 60% | bull-only |
| `rank(fn_accrued_liab_q)` | TOP1000 | 0.59 | 0.47 | 24.2% | 60% | bull-only |
| `rank(ts_delta(fn_accrued_liab_q, 5))` | TOP1000 | 0.79 | 0.43 | 21.9% | 60% | all-weather |
| `rank(fn_accrued_liab_q)` | TOP500 | 0.43 | 0.31 | 32.6% | 60% | bull-only |
| `rank(ts_delta(fn_accrued_liab_q, 5))` | TOP200 | 0.46 | 0.26 | 31.9% | 60% | mixed |
| `rank(ts_delta(fn_accrued_liab_q, 5))` | TOP3000 | 0.47 | 0.18 | 13.1% | 60% | all-weather |

## Correlation Notes
Top correlates:
- fn_accrued_liab_curr_q: 0.993 (strongly positively correlated)
- fn_accrued_liab_a: 0.952 (strongly positively correlated)
- fn_accrued_liab_curr_a: 0.950 (strongly positively correlated)
- fnd6_xaccq: 0.910 (strongly positively correlated)
- fnd6_xopr: 0.903 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_epsr_flag | analyst4 | -0.35 | 2.02 | +0.85 | -0.50 | yes |
| rp_ess_revenue | news18 | -0.32 | 1.70 | +0.54 | -0.49 | yes |
| est_rd_expense | analyst4 | -0.14 | 1.73 | +0.57 | +0.25 | yes |
| anl4_rd_exp_flag | analyst4 | -0.24 | 1.73 | +0.56 | +0.03 | yes |
| max_gross_income_guidance_2 | analyst4 | -0.30 | 1.59 | +0.43 | -0.98 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
