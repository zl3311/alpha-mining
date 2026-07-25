---
field: fn_taxes_payable_q
dataset: fundamental2
best_template: rank_value_norm
best_sharpe: 1.15
best_fitness: 0.78
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 8
max_drawdown: 0.0596
ann_vol: 0.0499
hit_rate: 0.5198
rolling_sharpe_min: -0.48
rolling_sharpe_max: 2.902
top_merge_partner: anl4_epsr_flag
redundancy_cluster: 1
negated_best_sharpe: 0.51
negated_best_template: rank_neg_delta
negated_best_fitness: 0.19
n_negated_sims: 10
direction_gap: -0.64
---
# fn_taxes_payable_q (fundamental2)

*Carrying value as of the balance sheet date of obligations incurred and payable for statutory income, sales, use, payroll, excise, real, property and other taxes. For classified balance sheets, used to reflect the current portion of the liabilities (due within 1 year or within the normal operating cycle if longer); for unclassified balance sheets, used to reflect the total liabilities (regardless of due date).*

## Signal Profile
- `rank(fn_taxes_payable_q)`: S=0.69, F=0.45, T=1.1%, INFERIOR (TOP3000)
- `rank(fn_taxes_payable_q / close)`: S=1.15, F=0.78, T=1.4%, INFERIOR (TOP3000)
- `rank(ts_delta(fn_taxes_payable_q, 5))`: S=0.24, F=0.08, T=36.8%, INFERIOR (TOP200)
- `-rank(fn_taxes_payable_q)`: S=-0.48, F=-0.27, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_taxes_payable_q, 5))`: S=0.51, F=0.19, T=35.9%, INFERIOR (TOP3000)
- `-ts_zscore(fn_taxes_payable_q, 63)`: S=0.34, F=0.13, T=16.8%, INFERIOR (TOP3000)
- `ts_mean(fn_taxes_payable_q, 10)`: S=0.21, F=0.09, T=0.9%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_taxes_payable_q, 22))`: S=-0.48, F=-0.23, T=15.9%, INFERIOR (TOP3000)
- `rank(-1 * fn_taxes_payable_q)`: S=-0.69, F=-0.45, T=1.1%, INFERIOR (TOP3000)
- `rank(-1 * fn_taxes_payable_q / close)`: S=-1.15, F=-0.78, T=1.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 11F/21P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 10F/19P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 1.14, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=1.49 (moderate), ret=+5.0%
  - 2020: S=0.63 (moderate), ret=+3.2%
  - 2021: S=1.93 (strong), ret=+12.1%
  - 2022: S=1.07 (moderate), ret=+5.9%
  - 2023: S=0.51 (moderate), ret=+1.8%

## Risk & Drawdown
- Max drawdown: 5.96% over 264 days (recovered)
- Annualized: return +5.7%, volatility 5.0% (fraction of booksize)
- Hit rate: 52.0% positive days
- Tail shape: skew +0.20, excess kurtosis +1.51

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.48, max 2.90, latest 0.51

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2023
Best month: +4.90%; worst month: -2.39%
Positive months: 64%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.28
- Sideways: S=1.06
- Bear: S=-1.31

## Negated Direction
Best negated: `rank(-1 * ts_delta(fn_taxes_payable_q, 5))` S=0.51, F=0.19, INFERIOR
Direction gap: -0.64 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fn_taxes_payable_q)`: S=-0.69, F=-0.45, T=1.1%, INFERIOR (TOP3000)
- `rank(-1 * fn_taxes_payable_q / close)`: S=-1.15, F=-0.78, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_taxes_payable_q, 5))`: S=0.51, F=0.19, T=35.9%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fn_taxes_payable_q / close)` | TOP3000 | 1.14 | 0.78 | 6.0% | 100% | bull-only |
| `rank(fn_taxes_payable_q)` | TOP3000 | 0.68 | 0.45 | 16.0% | 60% | bull-only |
| `rank(fn_taxes_payable_q / close)` | TOP1000 | 0.60 | 0.34 | 11.0% | 80% | bull-only |
| `rank(fn_taxes_payable_q)` | TOP1000 | 0.48 | 0.27 | 17.7% | 60% | bull-only |
| `rank(fn_taxes_payable_q / close)` | TOP500 | 0.43 | 0.22 | 13.2% | 80% | bull-only |
| `rank(fn_taxes_payable_q)` | TOP500 | 0.40 | 0.21 | 22.8% | 80% | bull-only |
| `rank(ts_delta(fn_taxes_payable_q, 5))` | TOP500 | 0.25 | 0.08 | 22.2% | 60% | weak |
| `rank(ts_delta(fn_taxes_payable_q, 5))` | TOP200 | 0.24 | 0.08 | 24.7% | 60% | weak |

## Correlation Notes
Top correlates:
- fn_taxes_payable_a: 0.840 (strongly positively correlated)
- fnd6_newa1v1300_ao: 0.815 (strongly positively correlated)
- fnd6_aox: 0.814 (strongly positively correlated)
- fnd6_aodo: 0.814 (strongly positively correlated)
- sales: 0.811 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_epsr_flag | analyst4 | -0.28 | 1.78 | +0.60 | -0.95 | yes |
| pv13_ompetitorgraphrank_hub_rank | pv13 | -0.20 | 1.78 | +0.62 | -0.19 | yes |
| rank(scl12_buzz * (-1 * returns)) | socialmedia12 | -0.20 | 2.17 | +0.54 | -0.92 | yes |
| rank(scl12_sentiment * (-1 * returns)) | socialmedia12 | -0.06 | 1.64 | +0.50 | -0.93 | yes |
| rank(fnd6_acdo) + rank(open/close - 1) | unknown | -0.18 | 2.51 | +0.49 | -0.77 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
