---
field: fn_accrued_liab_curr_q
dataset: fundamental2
best_template: rank_value_norm
best_sharpe: 1.11
best_fitness: 0.94
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 10
max_drawdown: 0.1193
ann_vol: 0.0814
hit_rate: 0.498
rolling_sharpe_min: -1.495
rolling_sharpe_max: 2.988
top_merge_partner: anl4_epsr_flag
redundancy_cluster: 1
negated_best_sharpe: 0.42
negated_best_template: neg_rank_level
negated_best_fitness: 0.34
n_negated_sims: 10
direction_gap: -0.69
---
# fn_accrued_liab_curr_q (fundamental2)

*Carrying value as of the balance sheet date of obligations incurred and payable, pertaining to costs that are statutory in nature, are incurred on contractual obligations, or accumulate over time and for which invoices have not yet been received or will not be rendered.*

## Signal Profile
- `rank(fn_accrued_liab_curr_q)`: S=0.93, F=0.87, T=1.1%, INFERIOR (TOP3000)
- `rank(fn_accrued_liab_curr_q / close)`: S=1.11, F=0.94, T=1.5%, INFERIOR (TOP3000)
- `rank(ts_delta(fn_accrued_liab_curr_q, 5))`: S=1.09, F=0.78, T=39.2%, INFERIOR (TOP500)
- `-rank(fn_accrued_liab_curr_q)`: S=-0.58, F=-0.46, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_accrued_liab_curr_q, 5))`: S=-0.50, F=-0.28, T=35.9%, INFERIOR (TOP3000)
- `ts_zscore(fn_accrued_liab_curr_q, 22)`: S=0.35, F=0.18, T=29.7%, INFERIOR (TOP3000)
- `ts_mean(fn_accrued_liab_curr_q, 10)`: S=0.18, F=0.08, T=0.9%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_accrued_liab_curr_q, 22))`: S=0.53, F=0.28, T=16.3%, INFERIOR (TOP3000)
- `rank(-1 * fn_accrued_liab_curr_q)`: S=0.42, F=0.34, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * fn_accrued_liab_curr_q / close)`: S=0.36, F=0.23, T=2.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 5F/15P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 1.09, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=-0.27 (negative), ret=-1.7%
  - 2020: S=0.85 (moderate), ret=+8.2%
  - 2021: S=2.16 (strong), ret=+20.8%
  - 2022: S=1.59 (strong), ret=+11.5%
  - 2023: S=0.77 (moderate), ret=+4.7%

## Risk & Drawdown
- Max drawdown: 11.93% over 484 days (recovered)
- Annualized: return +8.9%, volatility 8.1% (fraction of booksize)
- Hit rate: 49.8% positive days
- Tail shape: skew +0.43, excess kurtosis +2.04

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.50, max 2.99, latest 0.95

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2019
Best month: +8.67%; worst month: -4.50%
Positive months: 56%

## Regime Profile
Regime profile: **mixed**
- Bull: S=2.94
- Sideways: S=-0.08
- Bear: S=0.05

## Negated Direction
Best negated: `rank(-1 * fn_accrued_liab_curr_q)` S=0.42, F=0.34, INFERIOR
Direction gap: -0.69 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fn_accrued_liab_curr_q)`: S=0.42, F=0.34, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * fn_accrued_liab_curr_q / close)`: S=0.36, F=0.23, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_accrued_liab_curr_q, 5))`: S=-0.50, F=-0.28, T=35.9%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fn_accrued_liab_curr_q / close)` | TOP3000 | 1.09 | 0.94 | 11.9% | 80% | mixed |
| `rank(fn_accrued_liab_curr_q)` | TOP3000 | 0.92 | 0.87 | 25.2% | 60% | bull-only |
| `rank(ts_delta(fn_accrued_liab_curr_q, 5))` | TOP500 | 1.09 | 0.78 | 18.9% | 60% | all-weather |
| `rank(fn_accrued_liab_curr_q / close)` | TOP1000 | 0.71 | 0.55 | 10.2% | 80% | bull-only |
| `rank(fn_accrued_liab_curr_q / close)` | TOP500 | 0.61 | 0.47 | 16.0% | 80% | bull-only |
| `rank(fn_accrued_liab_curr_q)` | TOP1000 | 0.57 | 0.46 | 27.7% | 80% | bull-only |
| `rank(ts_delta(fn_accrued_liab_curr_q, 5))` | TOP1000 | 0.68 | 0.36 | 25.0% | 60% | all-weather |
| `rank(fn_accrued_liab_curr_q)` | TOP500 | 0.44 | 0.34 | 36.5% | 80% | bull-only |
| `rank(ts_delta(fn_accrued_liab_curr_q, 5))` | TOP200 | 0.48 | 0.26 | 35.4% | 60% | mixed |
| `rank(ts_delta(fn_accrued_liab_curr_q, 5))` | TOP3000 | 0.33 | 0.11 | 14.6% | 60% | mixed |

## Correlation Notes
Top correlates:
- fn_accrued_liab_q: 0.993 (strongly positively correlated)
- fn_accrued_liab_curr_a: 0.954 (strongly positively correlated)
- fn_accrued_liab_a: 0.946 (strongly positively correlated)
- fnd6_xaccq: 0.911 (strongly positively correlated)
- fnd6_xacc: 0.904 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_epsr_flag | analyst4 | -0.35 | 1.98 | +0.80 | -0.57 | yes |
| rp_ess_revenue | news18 | -0.32 | 1.66 | +0.57 | -0.58 | yes |
| anl4_rd_exp_flag | analyst4 | -0.25 | 1.70 | +0.61 | -0.04 | yes |
| max_gross_income_guidance_2 | analyst4 | -0.30 | 1.56 | +0.47 | -0.98 | yes |
| est_rd_expense | analyst4 | -0.13 | 1.66 | +0.55 | +0.27 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
