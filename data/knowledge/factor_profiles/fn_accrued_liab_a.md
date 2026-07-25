---
field: fn_accrued_liab_a
dataset: fundamental2
best_template: rank_value_norm
best_sharpe: 1.02
best_fitness: 0.79
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 9
max_drawdown: 0.0762
ann_vol: 0.0734
hit_rate: 0.4988
rolling_sharpe_min: -0.53
rolling_sharpe_max: 2.303
top_merge_partner: anl4_epsr_flag
redundancy_cluster: 1
negated_best_sharpe: 0.55
negated_best_template: neg_rank_level
negated_best_fitness: 0.51
n_negated_sims: 10
direction_gap: -0.47
---
# fn_accrued_liab_a (fundamental2)

*Carrying value as of the balance sheet date of obligations incurred and payable, pertaining to costs that are statutory in nature, are incurred on contractual obligations, or accumulate over time and for which invoices have not yet been received or will not be rendered.*

## Signal Profile
- `rank(fn_accrued_liab_a)`: S=0.78, F=0.62, T=1.0%, INFERIOR (TOP3000)
- `rank(fn_accrued_liab_a / close)`: S=1.02, F=0.79, T=1.4%, INFERIOR (TOP3000)
- `rank(ts_delta(fn_accrued_liab_a, 5))`: S=0.50, F=0.28, T=34.1%, INFERIOR (TOP1000)
- `-rank(fn_accrued_liab_a)`: S=-0.31, F=-0.18, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_accrued_liab_a, 5))`: S=-0.74, F=-0.66, T=23.6%, INFERIOR (TOP3000)
- `ts_zscore(fn_accrued_liab_a, 22)`: S=0.32, F=0.23, T=17.3%, INFERIOR (TOP3000)
- `ts_mean(fn_accrued_liab_a, 10)`: S=-0.02, F=0.00, T=0.9%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_accrued_liab_a, 22))`: S=0.05, F=0.01, T=15.7%, INFERIOR (TOP3000)
- `rank(-1 * fn_accrued_liab_a)`: S=0.55, F=0.51, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * fn_accrued_liab_a / close)`: S=0.61, F=0.51, T=2.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 10F/10P
- LOW_TURNOVER: 2F/30P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 1.01, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.62 (moderate), ret=+3.2%
  - 2020: S=0.84 (moderate), ret=+7.7%
  - 2021: S=1.19 (moderate), ret=+10.1%
  - 2022: S=1.55 (strong), ret=+10.2%
  - 2023: S=0.93 (moderate), ret=+5.3%

## Risk & Drawdown
- Max drawdown: 7.62% over 239 days (recovered)
- Annualized: return +7.4%, volatility 7.3% (fraction of booksize)
- Hit rate: 49.9% positive days
- Tail shape: skew +0.39, excess kurtosis +2.07

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.53, max 2.30, latest 1.08

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2019
Best month: +7.10%; worst month: -3.44%
Positive months: 59%

## Regime Profile
Regime profile: **mixed**
- Bull: S=2.47
- Sideways: S=0.32
- Bear: S=-0.01

## Negated Direction
Best negated: `rank(-1 * fn_accrued_liab_a)` S=0.55, F=0.51, INFERIOR
Direction gap: -0.47 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fn_accrued_liab_a)`: S=0.55, F=0.51, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * fn_accrued_liab_a / close)`: S=0.61, F=0.51, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_accrued_liab_a, 5))`: S=-0.74, F=-0.66, T=23.6%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fn_accrued_liab_a / close)` | TOP3000 | 1.01 | 0.79 | 7.6% | 100% | mixed |
| `rank(fn_accrued_liab_a)` | TOP3000 | 0.78 | 0.62 | 22.8% | 80% | bull-only |
| `rank(ts_delta(fn_accrued_liab_a, 5))` | TOP1000 | 0.49 | 0.28 | 31.6% | 60% | all-weather |
| `rank(ts_delta(fn_accrued_liab_a, 5))` | TOP500 | 0.46 | 0.27 | 35.7% | 60% | all-weather |
| `rank(ts_delta(fn_accrued_liab_a, 5))` | TOP200 | 0.39 | 0.25 | 40.1% | 60% | bull-only |
| `rank(fn_accrued_liab_a / close)` | TOP1000 | 0.41 | 0.24 | 13.2% | 60% | bull-only |
| `rank(fn_accrued_liab_a)` | TOP1000 | 0.31 | 0.18 | 34.1% | 60% | bull-only |
| `rank(fn_accrued_liab_a / close)` | TOP500 | 0.24 | 0.12 | 24.3% | 80% | bull-only |
| `rank(fn_accrued_liab_a)` | TOP500 | 0.12 | 0.05 | 48.2% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fn_accrued_liab_curr_a: 0.993 (strongly positively correlated)
- fn_accrued_liab_q: 0.952 (strongly positively correlated)
- fn_accrued_liab_curr_q: 0.946 (strongly positively correlated)
- fnd6_xopr: 0.929 (strongly positively correlated)
- fnd6_xacc: 0.924 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_epsr_flag | analyst4 | -0.36 | 1.92 | +0.74 | -0.35 | yes |
| rp_ess_revenue | news18 | -0.32 | 1.58 | +0.57 | -0.43 | yes |
| anl4_rd_exp_flag | analyst4 | -0.19 | 1.57 | +0.55 | -0.39 | yes |
| max_gross_income_guidance | analyst4 | -0.22 | 1.46 | +0.45 | -0.92 | yes |
| min_gross_income_guidance | analyst4 | -0.22 | 1.45 | +0.44 | -0.93 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
