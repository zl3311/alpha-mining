---
field: fn_taxes_payable_a
dataset: fundamental2
best_template: rank_value_norm
best_sharpe: 0.81
best_fitness: 0.47
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 8
max_drawdown: 0.0714
ann_vol: 0.0514
hit_rate: 0.5134
rolling_sharpe_min: -1.049
rolling_sharpe_max: 2.371
top_merge_partner: rp_ess_revenue
redundancy_cluster: 1
negated_best_sharpe: 0.47
negated_best_template: rank_neg_delta
negated_best_fitness: 0.2
n_negated_sims: 10
direction_gap: -0.34
---
# fn_taxes_payable_a (fundamental2)

*Carrying value as of the balance sheet date of obligations incurred and payable for statutory income, sales, use, payroll, excise, real, property, and other taxes. For classified balance sheets, used to reflect the current portion of the liabilities (due within 1 year or within the normal operating cycle if longer); for unclassified balance sheets, used to reflect the total liabilities (regardless of due date).*

## Signal Profile
- `rank(fn_taxes_payable_a)`: S=0.53, F=0.30, T=0.8%, INFERIOR (TOP3000)
- `rank(fn_taxes_payable_a / close)`: S=0.81, F=0.47, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_delta(fn_taxes_payable_a, 5))`: S=-0.06, F=-0.01, T=29.0%, INFERIOR (TOP200)
- `-rank(fn_taxes_payable_a)`: S=-0.22, F=-0.08, T=1.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_taxes_payable_a, 5))`: S=0.47, F=0.20, T=34.9%, INFERIOR (TOP3000)
- `-ts_zscore(fn_taxes_payable_a, 63)`: S=0.30, F=0.16, T=16.8%, INFERIOR (TOP3000)
- `ts_mean(fn_taxes_payable_a, 10)`: S=0.28, F=0.14, T=0.7%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_taxes_payable_a, 22))`: S=-0.65, F=-0.43, T=14.3%, INFERIOR (TOP3000)
- `rank(-1 * fn_taxes_payable_a)`: S=-0.53, F=-0.30, T=0.8%, INFERIOR (TOP3000)
- `rank(-1 * fn_taxes_payable_a / close)`: S=-0.81, F=-0.47, T=1.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 11F/18P
- LOW_TURNOVER: 5F/27P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.81, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=1.09 (moderate), ret=+3.8%
  - 2020: S=0.43 (weak), ret=+2.2%
  - 2021: S=1.17 (moderate), ret=+7.5%
  - 2022: S=0.77 (moderate), ret=+4.3%
  - 2023: S=0.65 (moderate), ret=+2.5%

## Risk & Drawdown
- Max drawdown: 7.14% over 551 days (recovered)
- Annualized: return +4.2%, volatility 5.1% (fraction of booksize)
- Hit rate: 51.3% positive days
- Tail shape: skew +0.25, excess kurtosis +1.17

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.05, max 2.37, latest 0.64

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2020
Best month: +5.02%; worst month: -2.88%
Positive months: 61%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.99
- Sideways: S=0.94
- Bear: S=-1.88

## Negated Direction
Best negated: `rank(-1 * ts_delta(fn_taxes_payable_a, 5))` S=0.47, F=0.20, INFERIOR
Direction gap: -0.34 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fn_taxes_payable_a)`: S=-0.53, F=-0.30, T=0.8%, INFERIOR (TOP3000)
- `rank(-1 * fn_taxes_payable_a / close)`: S=-0.81, F=-0.47, T=1.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_taxes_payable_a, 5))`: S=0.47, F=0.20, T=34.9%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fn_taxes_payable_a / close)` | TOP3000 | 0.81 | 0.47 | 7.1% | 100% | bull-only |
| `rank(fn_taxes_payable_a)` | TOP3000 | 0.52 | 0.30 | 18.5% | 80% | bull-only |
| `rank(fn_taxes_payable_a / close)` | TOP1000 | 0.33 | 0.14 | 12.7% | 60% | bull-only |
| `rank(fn_taxes_payable_a / close)` | TOP200 | 0.22 | 0.09 | 20.4% | 40% | bull-only |
| `rank(fn_taxes_payable_a)` | TOP1000 | 0.21 | 0.08 | 23.8% | 60% | bull-only |
| `rank(fn_taxes_payable_a / close)` | TOP500 | 0.20 | 0.07 | 16.9% | 60% | bull-only |
| `rank(fn_taxes_payable_a)` | TOP200 | 0.13 | 0.04 | 27.4% | 40% | bull-only |
| `rank(fn_taxes_payable_a)` | TOP500 | 0.09 | 0.03 | 26.6% | 80% | bull-only |

## Correlation Notes
Top correlates:
- fn_taxes_payable_q: 0.840 (strongly positively correlated)
- actual_sales_value_quarterly: 0.838 (strongly positively correlated)
- actual_sales_value_annual: 0.837 (strongly positively correlated)
- fnd6_lcox: 0.836 (strongly positively correlated)
- est_grossincome: 0.831 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| rp_ess_revenue | news18 | -0.27 | 1.31 | +0.42 | -0.84 | yes |
| anl4_epsr_flag | analyst4 | -0.26 | 1.60 | +0.42 | -0.85 | yes |
| max_adjusted_net_profit_guidance | analyst4 | -0.15 | 1.18 | +0.37 | -0.79 | yes |
| net_profit_adjusted_min_guidance | analyst4 | -0.14 | 1.31 | +0.36 | -0.86 | yes |
| snt_value_fast_d1 | socialmedia12 | -0.09 | 1.24 | +0.36 | -0.78 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
