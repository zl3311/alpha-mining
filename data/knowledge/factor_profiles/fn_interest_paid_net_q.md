---
field: fn_interest_paid_net_q
dataset: fundamental2
best_template: rank_value_norm
best_sharpe: 1.0
best_fitness: 0.75
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 7
max_drawdown: 0.0755
ann_vol: 0.0711
hit_rate: 0.5028
rolling_sharpe_min: -0.983
rolling_sharpe_max: 2.762
top_merge_partner: anl4_epsr_flag
redundancy_cluster: 1
negated_best_sharpe: 0.51
negated_best_template: rank_neg_delta
negated_best_fitness: 0.27
n_negated_sims: 10
direction_gap: -0.49
---
# fn_interest_paid_net_q (fundamental2)

*Net interest*

## Signal Profile
- `rank(fn_interest_paid_net_q)`: S=0.78, F=0.54, T=1.7%, INFERIOR (TOP3000)
- `rank(fn_interest_paid_net_q / close)`: S=1.00, F=0.75, T=1.9%, INFERIOR (TOP3000)
- `rank(ts_delta(fn_interest_paid_net_q, 5))`: S=0.23, F=0.07, T=36.1%, INFERIOR (TOP500)
- `-rank(fn_interest_paid_net_q)`: S=-0.39, F=-0.21, T=2.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_interest_paid_net_q, 5))`: S=0.51, F=0.27, T=35.7%, INFERIOR (TOP3000)
- `-ts_zscore(fn_interest_paid_net_q, 63)`: S=0.66, F=0.30, T=16.6%, INFERIOR (TOP3000)
- `ts_mean(fn_interest_paid_net_q, 10)`: S=0.25, F=0.09, T=1.7%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_interest_paid_net_q, 22))`: S=-1.11, F=-0.80, T=17.0%, INFERIOR (TOP3000)
- `rank(-1 * fn_interest_paid_net_q)`: S=0.20, F=0.10, T=3.8%, INFERIOR (TOP3000)
- `rank(-1 * fn_interest_paid_net_q / close)`: S=0.33, F=0.20, T=3.9%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/6P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 1.00, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.17 (weak), ret=+0.8%
  - 2020: S=1.06 (moderate), ret=+10.4%
  - 2021: S=1.94 (strong), ret=+13.6%
  - 2022: S=1.45 (moderate), ret=+8.9%
  - 2023: S=0.18 (weak), ret=+1.0%

## Risk & Drawdown
- Max drawdown: 7.55% over 473 days (not yet recovered, ongoing at window end)
- Annualized: return +7.1%, volatility 7.1% (fraction of booksize)
- Hit rate: 50.3% positive days
- Tail shape: skew +0.67, excess kurtosis +3.37

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.98, max 2.76, latest 0.23

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2019
Best month: +5.59%; worst month: -3.24%
Positive months: 59%

## Regime Profile
Regime profile: **mixed**
- Bull: S=2.18
- Sideways: S=0.52
- Bear: S=0.23

## Negated Direction
Best negated: `rank(-1 * ts_delta(fn_interest_paid_net_q, 5))` S=0.51, F=0.27, INFERIOR
Direction gap: -0.49 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fn_interest_paid_net_q)`: S=0.20, F=0.10, T=3.8%, INFERIOR (TOP3000)
- `rank(-1 * fn_interest_paid_net_q / close)`: S=0.33, F=0.20, T=3.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_interest_paid_net_q, 5))`: S=0.51, F=0.27, T=35.7%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fn_interest_paid_net_q / close)` | TOP3000 | 1.00 | 0.75 | 7.5% | 100% | mixed |
| `rank(fn_interest_paid_net_q)` | TOP3000 | 0.77 | 0.54 | 12.4% | 60% | bull-only |
| `rank(fn_interest_paid_net_q / close)` | TOP1000 | 0.63 | 0.41 | 12.2% | 80% | bull-only |
| `rank(fn_interest_paid_net_q)` | TOP1000 | 0.38 | 0.21 | 21.6% | 60% | bull-only |
| `rank(fn_interest_paid_net_q / close)` | TOP500 | 0.32 | 0.17 | 15.2% | 60% | bull-only |
| `rank(ts_delta(fn_interest_paid_net_q, 5))` | TOP500 | 0.23 | 0.07 | 32.7% | 60% | bull-only |
| `rank(ts_delta(fn_interest_paid_net_q, 5))` | TOP3000 | 0.12 | 0.02 | 18.2% | 40% | weak |

## Correlation Notes
Top correlates:
- fn_interest_paid_net_a: 0.941 (strongly positively correlated)
- fnd6_intpn: 0.912 (strongly positively correlated)
- fnd6_newqv1300_xintq: 0.902 (strongly positively correlated)
- interest_expense: 0.902 (strongly positively correlated)
- fnd6_newa2v1300_xint: 0.901 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_epsr_flag | analyst4 | -0.38 | 1.93 | +0.75 | -0.68 | yes |
| rp_ess_revenue | news18 | -0.32 | 1.56 | +0.56 | -0.50 | yes |
| anl4_rd_exp_flag | analyst4 | -0.27 | 1.63 | +0.60 | +0.03 | yes |
| max_gross_income_guidance_2 | analyst4 | -0.30 | 1.46 | +0.46 | -0.84 | yes |
| max_gross_income_guidance | analyst4 | -0.27 | 1.50 | +0.50 | -0.47 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
