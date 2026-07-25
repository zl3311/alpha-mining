---
field: fnd6_newa2v1300_xint
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 0.96
best_fitness: 0.71
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 6
max_drawdown: 0.0935
ann_vol: 0.071
hit_rate: 0.4972
rolling_sharpe_min: -1.444
rolling_sharpe_max: 2.808
top_merge_partner: anl4_epsr_flag
redundancy_cluster: 1
negated_best_sharpe: 0.78
negated_best_template: rank_neg_delta
negated_best_fitness: 0.36
n_negated_sims: 10
direction_gap: -0.18
---
# fnd6_newa2v1300_xint (fundamental6)

*Interest and Related Expense - Total*

## Signal Profile
- `rank(fnd6_newa2v1300_xint)`: S=0.68, F=0.48, T=1.0%, INFERIOR (TOP3000)
- `rank(fnd6_newa2v1300_xint / close)`: S=0.96, F=0.71, T=1.4%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_newa2v1300_xint, 5))`: S=-0.24, F=-0.09, T=35.0%, INFERIOR (TOP200)
- `-rank(fnd6_newa2v1300_xint)`: S=-0.43, F=-0.26, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa2v1300_xint, 5))`: S=0.78, F=0.36, T=35.9%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_newa2v1300_xint, 63)`: S=0.14, F=0.05, T=19.0%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newa2v1300_xint, 10)`: S=0.40, F=0.19, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newa2v1300_xint, 22))`: S=-0.32, F=-0.13, T=15.3%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa2v1300_xint)`: S=-0.68, F=-0.48, T=1.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa2v1300_xint / close)`: S=-0.96, F=-0.71, T=1.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 19F/10P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.96, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.23 (weak), ret=+1.1%
  - 2020: S=0.86 (moderate), ret=+8.1%
  - 2021: S=1.78 (strong), ret=+14.1%
  - 2022: S=1.17 (moderate), ret=+7.8%
  - 2023: S=0.52 (moderate), ret=+2.4%

## Risk & Drawdown
- Max drawdown: 9.35% over 597 days (not yet recovered, ongoing at window end)
- Annualized: return +6.8%, volatility 7.1% (fraction of booksize)
- Hit rate: 49.7% positive days
- Tail shape: skew +0.52, excess kurtosis +2.79

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.44, max 2.81, latest 0.62

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2019
Best month: +7.13%; worst month: -4.18%
Positive months: 59%

## Regime Profile
Regime profile: **mixed**
- Bull: S=2.82
- Sideways: S=0.30
- Bear: S=-0.50

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_newa2v1300_xint, 5))` S=0.78, F=0.36, INFERIOR
Direction gap: -0.18 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_newa2v1300_xint)`: S=-0.68, F=-0.48, T=1.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa2v1300_xint / close)`: S=-0.96, F=-0.71, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa2v1300_xint, 5))`: S=0.78, F=0.36, T=35.9%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newa2v1300_xint / close)` | TOP3000 | 0.96 | 0.71 | 9.3% | 100% | mixed |
| `rank(fnd6_newa2v1300_xint / close)` | TOP1000 | 0.73 | 0.52 | 11.5% | 80% | bull-only |
| `rank(fnd6_newa2v1300_xint)` | TOP3000 | 0.67 | 0.48 | 18.0% | 80% | bull-only |
| `rank(fnd6_newa2v1300_xint / close)` | TOP500 | 0.44 | 0.27 | 17.2% | 60% | bull-only |
| `rank(fnd6_newa2v1300_xint)` | TOP1000 | 0.42 | 0.26 | 23.5% | 60% | bull-only |
| `rank(fnd6_newa2v1300_xint)` | TOP500 | 0.23 | 0.12 | 37.4% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_newqv1300_xintq: 0.980 (strongly positively correlated)
- interest_expense: 0.980 (strongly positively correlated)
- fnd6_intpn: 0.960 (strongly positively correlated)
- fn_interest_paid_net_a: 0.950 (strongly positively correlated)
- fnd6_newa1v1300_lt: 0.950 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_epsr_flag | analyst4 | -0.37 | 1.88 | +0.70 | -0.72 | yes |
| rp_ess_revenue | news18 | -0.35 | 1.56 | +0.60 | -0.62 | yes |
| anl4_rd_exp_flag | analyst4 | -0.28 | 1.62 | +0.59 | +0.00 | yes |
| net_profit_adjusted_min_guidance | analyst4 | -0.19 | 1.49 | +0.53 | -0.50 | yes |
| max_gross_income_guidance_2 | analyst4 | -0.29 | 1.42 | +0.46 | -0.93 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
