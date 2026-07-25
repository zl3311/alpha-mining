---
field: fn_repayments_of_lines_of_credit_q
dataset: fundamental2
best_template: rank_value_norm
best_sharpe: 1.11
best_fitness: 0.8
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 6
max_drawdown: 0.0692
ann_vol: 0.058
hit_rate: 0.5085
rolling_sharpe_min: -0.549
rolling_sharpe_max: 2.975
top_merge_partner: anl4_epsr_flag
redundancy_cluster: 1
negated_best_sharpe: 0.81
negated_best_template: rank_neg_delta
negated_best_fitness: 0.42
n_negated_sims: 10
direction_gap: -0.3
---
# fn_repayments_of_lines_of_credit_q (fundamental2)

*Amount of cash outflow for payment of an obligation from a lender, including but not limited to, letter of credit, standby letter of credit and revolving credit arrangements.*

## Signal Profile
- `rank(fn_repayments_of_lines_of_credit_q)`: S=0.65, F=0.45, T=1.6%, INFERIOR (TOP3000)
- `rank(fn_repayments_of_lines_of_credit_q / close)`: S=1.11, F=0.80, T=2.0%, INFERIOR (TOP3000)
- `rank(ts_delta(fn_repayments_of_lines_of_credit_q, 5))`: S=-0.03, F=0.00, T=36.2%, INFERIOR (TOP3000)
- `-rank(fn_repayments_of_lines_of_credit_q)`: S=-0.36, F=-0.20, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_repayments_of_lines_of_credit_q, 5))`: S=0.81, F=0.42, T=35.4%, INFERIOR (TOP3000)
- `-ts_zscore(fn_repayments_of_lines_of_credit_q, 63)`: S=0.54, F=0.27, T=15.2%, INFERIOR (TOP3000)
- `ts_mean(fn_repayments_of_lines_of_credit_q, 10)`: S=0.07, F=0.02, T=1.5%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_repayments_of_lines_of_credit_q, 22))`: S=0.28, F=0.10, T=17.4%, INFERIOR (TOP3000)
- `rank(-1 * fn_repayments_of_lines_of_credit_q)`: S=-0.36, F=-0.20, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * fn_repayments_of_lines_of_credit_q / close)`: S=-0.63, F=-0.40, T=2.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 10F/19P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 1.10, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.51 (moderate), ret=+2.3%
  - 2020: S=-0.03 (negative), ret=-0.2%
  - 2021: S=1.66 (strong), ret=+12.1%
  - 2022: S=2.10 (strong), ret=+12.2%
  - 2023: S=1.49 (moderate), ret=+4.8%

## Risk & Drawdown
- Max drawdown: 6.92% over 273 days (recovered)
- Annualized: return +6.4%, volatility 5.8% (fraction of booksize)
- Hit rate: 50.8% positive days
- Tail shape: skew +0.50, excess kurtosis +2.31

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.55, max 2.98, latest 1.53

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +7.29%; worst month: -2.84%
Positive months: 64%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.71
- Sideways: S=0.64
- Bear: S=-1.53

## Negated Direction
Best negated: `rank(-1 * ts_delta(fn_repayments_of_lines_of_credit_q, 5))` S=0.81, F=0.42, INFERIOR
Direction gap: -0.30 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fn_repayments_of_lines_of_credit_q)`: S=-0.36, F=-0.20, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * fn_repayments_of_lines_of_credit_q / close)`: S=-0.63, F=-0.40, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_repayments_of_lines_of_credit_q, 5))`: S=0.81, F=0.42, T=35.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fn_repayments_of_lines_of_credit_q / close)` | TOP3000 | 1.10 | 0.80 | 6.9% | 80% | bull-only |
| `rank(fn_repayments_of_lines_of_credit_q)` | TOP3000 | 0.64 | 0.45 | 28.3% | 80% | bull-only |
| `rank(fn_repayments_of_lines_of_credit_q / close)` | TOP1000 | 0.62 | 0.40 | 9.1% | 60% | bull-only |
| `rank(fn_repayments_of_lines_of_credit_q / close)` | TOP500 | 0.52 | 0.33 | 22.2% | 60% | bull-only |
| `rank(fn_repayments_of_lines_of_credit_q)` | TOP1000 | 0.35 | 0.20 | 29.9% | 60% | bull-only |
| `rank(fn_repayments_of_lines_of_credit_q)` | TOP500 | 0.18 | 0.08 | 39.2% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_newa2v1300_sale: 0.901 (strongly positively correlated)
- fnd6_newa2v1300_revt: 0.901 (strongly positively correlated)
- fnd6_mfma2_revt: 0.901 (strongly positively correlated)
- fnd6_cptnewqv1300_saleq: 0.900 (strongly positively correlated)
- sales: 0.900 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_epsr_flag | analyst4 | -0.29 | 1.82 | +0.64 | -0.43 | yes |
| anl4_rd_exp_flag | analyst4 | -0.30 | 1.66 | +0.56 | -0.71 | yes |
| pv13_ompetitorgraphrank_hub_rank | pv13 | -0.20 | 1.70 | +0.54 | -0.07 | yes |
| rp_ess_revenue | news18 | -0.34 | 1.57 | +0.47 | -0.71 | yes |
| net_profit_adjusted_min_guidance | analyst4 | -0.21 | 1.56 | +0.46 | -0.76 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
