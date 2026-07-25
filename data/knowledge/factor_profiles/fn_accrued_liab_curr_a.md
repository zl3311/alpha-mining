---
field: fn_accrued_liab_curr_a
dataset: fundamental2
best_template: rank_value_norm
best_sharpe: 1.0
best_fitness: 0.79
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 9
max_drawdown: 0.0845
ann_vol: 0.0777
hit_rate: 0.498
rolling_sharpe_min: -0.535
rolling_sharpe_max: 2.287
top_merge_partner: anl4_epsr_flag
redundancy_cluster: 1
negated_best_sharpe: 0.66
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.59
n_negated_sims: 10
direction_gap: -0.34
---
# fn_accrued_liab_curr_a (fundamental2)

*Carrying value as of the balance sheet date of obligations incurred and payable, pertaining to costs that are statutory in nature, are incurred on contractual obligations, or accumulate over time and for which invoices have not yet been received or will not be rendered.*

## Signal Profile
- `rank(fn_accrued_liab_curr_a)`: S=0.79, F=0.66, T=1.0%, INFERIOR (TOP3000)
- `rank(fn_accrued_liab_curr_a / close)`: S=1.00, F=0.79, T=1.4%, INFERIOR (TOP3000)
- `rank(ts_delta(fn_accrued_liab_curr_a, 5))`: S=0.70, F=0.46, T=33.4%, INFERIOR (TOP1000)
- `-rank(fn_accrued_liab_curr_a)`: S=-0.32, F=-0.19, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_accrued_liab_curr_a, 5))`: S=-0.89, F=-0.86, T=23.7%, INFERIOR (TOP3000)
- `ts_zscore(fn_accrued_liab_curr_a, 22)`: S=0.31, F=0.22, T=15.6%, INFERIOR (TOP3000)
- `ts_mean(fn_accrued_liab_curr_a, 10)`: S=-0.02, F=0.00, T=0.9%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_accrued_liab_curr_a, 22))`: S=0.33, F=0.18, T=16.4%, INFERIOR (TOP3000)
- `rank(-1 * fn_accrued_liab_curr_a)`: S=0.57, F=0.55, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * fn_accrued_liab_curr_a / close)`: S=0.66, F=0.59, T=2.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 9F/11P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.98, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.59 (moderate), ret=+3.2%
  - 2020: S=0.72 (moderate), ret=+6.8%
  - 2021: S=1.27 (moderate), ret=+11.6%
  - 2022: S=1.49 (moderate), ret=+10.6%
  - 2023: S=0.88 (moderate), ret=+5.2%

## Risk & Drawdown
- Max drawdown: 8.45% over 239 days (recovered)
- Annualized: return +7.6%, volatility 7.8% (fraction of booksize)
- Hit rate: 49.8% positive days
- Tail shape: skew +0.35, excess kurtosis +1.96

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.54, max 2.29, latest 1.03

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2019
Best month: +7.63%; worst month: -3.50%
Positive months: 61%

## Regime Profile
Regime profile: **mixed**
- Bull: S=2.56
- Sideways: S=0.33
- Bear: S=-0.22

## Negated Direction
Best negated: `rank(-1 * fn_accrued_liab_curr_a / close)` S=0.66, F=0.59, INFERIOR
Direction gap: -0.34 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fn_accrued_liab_curr_a)`: S=0.57, F=0.55, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * fn_accrued_liab_curr_a / close)`: S=0.66, F=0.59, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_accrued_liab_curr_a, 5))`: S=-0.89, F=-0.86, T=23.7%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fn_accrued_liab_curr_a / close)` | TOP3000 | 0.98 | 0.79 | 8.5% | 100% | mixed |
| `rank(fn_accrued_liab_curr_a)` | TOP3000 | 0.79 | 0.66 | 25.3% | 80% | bull-only |
| `rank(ts_delta(fn_accrued_liab_curr_a, 5))` | TOP1000 | 0.69 | 0.46 | 30.9% | 80% | all-weather |
| `rank(ts_delta(fn_accrued_liab_curr_a, 5))` | TOP500 | 0.59 | 0.39 | 35.4% | 80% | all-weather |
| `rank(ts_delta(fn_accrued_liab_curr_a, 5))` | TOP200 | 0.41 | 0.28 | 43.7% | 60% | mixed |
| `rank(fn_accrued_liab_curr_a / close)` | TOP1000 | 0.36 | 0.21 | 16.6% | 60% | bull-only |
| `rank(fn_accrued_liab_curr_a)` | TOP1000 | 0.31 | 0.19 | 36.3% | 60% | bull-only |
| `rank(fn_accrued_liab_curr_a / close)` | TOP500 | 0.25 | 0.13 | 26.6% | 60% | bull-only |
| `rank(fn_accrued_liab_curr_a)` | TOP500 | 0.15 | 0.07 | 50.0% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fn_accrued_liab_a: 0.993 (strongly positively correlated)
- fn_accrued_liab_curr_q: 0.954 (strongly positively correlated)
- fn_accrued_liab_q: 0.950 (strongly positively correlated)
- fnd6_xacc: 0.925 (strongly positively correlated)
- fnd6_xopr: 0.925 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_epsr_flag | analyst4 | -0.36 | 1.91 | +0.73 | -0.51 | yes |
| rp_ess_revenue | news18 | -0.32 | 1.58 | +0.59 | -0.60 | yes |
| anl4_rd_exp_flag | analyst4 | -0.21 | 1.57 | +0.55 | -0.46 | yes |
| max_gross_income_guidance | analyst4 | -0.23 | 1.47 | +0.48 | -0.85 | yes |
| net_profit_adjusted_min_guidance | analyst4 | -0.16 | 1.49 | +0.50 | -0.63 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
