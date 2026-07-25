---
field: fnd6_newqv1300_xintq
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 1.09
best_fitness: 0.86
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 7
max_drawdown: 0.0834
ann_vol: 0.0728
hit_rate: 0.502
rolling_sharpe_min: -1.107
rolling_sharpe_max: 2.82
top_merge_partner: anl4_epsr_flag
redundancy_cluster: 1
negated_best_sharpe: 0.78
negated_best_template: rank_neg_delta
negated_best_fitness: 0.36
n_negated_sims: 10
direction_gap: -0.31
---
# fnd6_newqv1300_xintq (fundamental6)

*Interest and Related Expense - Total*

## Signal Profile
- `rank(fnd6_newqv1300_xintq)`: S=0.80, F=0.62, T=2.0%, INFERIOR (TOP3000)
- `rank(fnd6_newqv1300_xintq / close)`: S=1.09, F=0.86, T=2.3%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_newqv1300_xintq, 5))`: S=-0.17, F=-0.03, T=38.8%, INFERIOR (TOP3000)
- `-rank(fnd6_newqv1300_xintq)`: S=-0.46, F=-0.29, T=3.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_xintq, 5))`: S=0.78, F=0.36, T=39.2%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_newqv1300_xintq, 63)`: S=0.13, F=0.02, T=18.8%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newqv1300_xintq, 10)`: S=0.22, F=0.08, T=2.0%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newqv1300_xintq, 22))`: S=0.03, F=0.00, T=17.6%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_xintq)`: S=-0.25, F=-0.13, T=3.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_xintq / close)`: S=-0.57, F=-0.39, T=3.8%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 10F/22P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 16F/13P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 1.08, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.54 (moderate), ret=+2.6%
  - 2020: S=0.96 (moderate), ret=+9.1%
  - 2021: S=1.80 (strong), ret=+15.0%
  - 2022: S=1.31 (moderate), ret=+8.9%
  - 2023: S=0.64 (moderate), ret=+3.0%

## Risk & Drawdown
- Max drawdown: 8.34% over 597 days (not yet recovered, ongoing at window end)
- Annualized: return +7.9%, volatility 7.3% (fraction of booksize)
- Hit rate: 50.2% positive days
- Tail shape: skew +0.49, excess kurtosis +2.68

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.11, max 2.82, latest 0.74

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2019
Best month: +7.90%; worst month: -3.60%
Positive months: 61%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.86
- Sideways: S=0.66
- Bear: S=-0.50

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_newqv1300_xintq, 5))` S=0.78, F=0.36, INFERIOR
Direction gap: -0.31 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_newqv1300_xintq)`: S=-0.25, F=-0.13, T=3.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_xintq / close)`: S=-0.57, F=-0.39, T=3.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_xintq, 5))`: S=0.78, F=0.36, T=39.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newqv1300_xintq / close)` | TOP3000 | 1.08 | 0.86 | 8.3% | 100% | bull-only |
| `rank(fnd6_newqv1300_xintq)` | TOP3000 | 0.80 | 0.62 | 17.7% | 80% | bull-only |
| `rank(fnd6_newqv1300_xintq / close)` | TOP1000 | 0.75 | 0.56 | 12.0% | 100% | bull-only |
| `rank(fnd6_newqv1300_xintq / close)` | TOP500 | 0.57 | 0.39 | 15.3% | 80% | bull-only |
| `rank(fnd6_newqv1300_xintq)` | TOP1000 | 0.45 | 0.29 | 25.0% | 80% | bull-only |
| `rank(fnd6_newqv1300_xintq)` | TOP500 | 0.24 | 0.13 | 41.4% | 60% | bull-only |
| `rank(fnd6_newqv1300_xintq / close)` | TOP200 | 0.17 | 0.07 | 27.1% | 60% | bull-only |

## Correlation Notes
Top correlates:
- interest_expense: 1.000 (strongly positively correlated)
- fnd6_newa2v1300_xint: 0.980 (strongly positively correlated)
- debt_lt: 0.954 (strongly positively correlated)
- fnd6_cptnewqv1300_dlttq: 0.954 (strongly positively correlated)
- fnd6_cptmfmq_dlttq: 0.954 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_epsr_flag | analyst4 | -0.37 | 1.98 | +0.80 | -0.78 | yes |
| anl4_rd_exp_flag | analyst4 | -0.29 | 1.72 | +0.63 | -0.07 | yes |
| rp_ess_revenue | news18 | -0.34 | 1.66 | +0.57 | -0.66 | yes |
| net_profit_adjusted_min_guidance | analyst4 | -0.20 | 1.59 | +0.51 | -0.56 | yes |
| est_rd_expense | analyst4 | -0.10 | 1.63 | +0.52 | +0.58 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
