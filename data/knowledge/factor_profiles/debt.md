---
field: debt
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 1.08
best_fitness: 0.92
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 37
regime_profile: bull-only
n_variations_with_pnl: 9
max_drawdown: 0.0791
ann_vol: 0.0845
hit_rate: 0.4996
rolling_sharpe_min: -0.703
rolling_sharpe_max: 2.658
top_merge_partner: anl4_epsr_flag
redundancy_cluster: 1
negated_best_sharpe: 0.7
negated_best_template: rank_neg_delta
negated_best_fitness: 0.31
n_negated_sims: 10
direction_gap: -0.38
---
# debt (fundamental6)

*Debt*

## Signal Profile
- `rank(debt)`: S=0.81, F=0.68, T=2.4%, INFERIOR (TOP3000)
- `rank(debt / close)`: S=1.08, F=0.92, T=2.6%, INFERIOR (TOP3000)
- `rank(ts_delta(debt, 5))`: S=-0.14, F=-0.02, T=38.9%, INFERIOR (TOP1000)
- `ts_decay_linear(rank(debt), 5)`: S=0.81, F=0.68, T=2.4%, INFERIOR (TOP3000)
- `trade_when(ts_std_dev(returns,20)>0.02, rank(debt), ts_std_dev(returns,20)<0.01)`: S=0.75, F=0.60, T=2.9%, INFERIOR (TOP3000)
- `-rank(debt)`: S=-0.36, F=-0.22, T=3.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(debt, 5))`: S=0.70, F=0.31, T=38.7%, INFERIOR (TOP3000)
- `-ts_zscore(debt, 63)`: S=0.41, F=0.12, T=19.3%, INFERIOR (TOP3000)
- `ts_mean(debt, 10)`: S=0.18, F=0.07, T=2.1%, INFERIOR (TOP3000)
- `rank(ts_rank(debt, 22))`: S=-0.11, F=-0.02, T=17.5%, INFERIOR (TOP3000)
- `rank(-1 * debt)`: S=-0.21, F=-0.10, T=3.6%, INFERIOR (TOP3000)
- `rank(-1 * debt / close)`: S=-0.46, F=-0.29, T=3.7%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 9F/28P
- LOW_FITNESS: 37F/0P
- LOW_SHARPE: 37F/0P
- LOW_SUB_UNIVERSE_SHARPE: 21F/13P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 1.08, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=1.07 (moderate), ret=+5.1%
  - 2020: S=0.48 (weak), ret=+4.6%
  - 2021: S=1.64 (strong), ret=+19.1%
  - 2022: S=1.62 (strong), ret=+13.1%
  - 2023: S=0.54 (moderate), ret=+2.8%

## Risk & Drawdown
- Max drawdown: 7.91% over 215 days (recovered)
- Annualized: return +9.1%, volatility 8.5% (fraction of booksize)
- Hit rate: 50.0% positive days
- Tail shape: skew +0.41, excess kurtosis +2.92

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.70, max 2.66, latest 0.61

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2020
Best month: +9.49%; worst month: -3.10%
Positive months: 61%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.94
- Sideways: S=0.67
- Bear: S=-0.81

## Negated Direction
Best negated: `rank(-1 * ts_delta(debt, 5))` S=0.70, F=0.31, INFERIOR
Direction gap: -0.38 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * debt)`: S=-0.21, F=-0.10, T=3.6%, INFERIOR (TOP3000)
- `rank(-1 * debt / close)`: S=-0.46, F=-0.29, T=3.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(debt, 5))`: S=0.70, F=0.31, T=38.7%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(debt / close)` | TOP3000 | 1.08 | 0.92 | 7.9% | 100% | bull-only |
| `ts_decay_linear(rank(debt), 5)` | TOP3000 | 0.80 | 0.68 | 24.3% | 80% | bull-only |
| `rank(debt)` | TOP3000 | 0.80 | 0.68 | 24.3% | 80% | bull-only |
| `trade_when(ts_std_dev(returns,20)>0.02, rank(debt), ts_std_dev(returns,20)<0.01)` | TOP3000 | 0.74 | 0.60 | 24.2% | 80% | bull-only |
| `rank(debt / close)` | TOP1000 | 0.60 | 0.43 | 13.2% | 60% | bull-only |
| `rank(debt / close)` | TOP500 | 0.45 | 0.29 | 20.5% | 60% | bull-only |
| `rank(debt)` | TOP1000 | 0.35 | 0.22 | 31.6% | 60% | bull-only |
| `rank(debt)` | TOP500 | 0.20 | 0.10 | 45.6% | 60% | bull-only |
| `rank(debt / close)` | TOP200 | 0.12 | 0.04 | 30.4% | 60% | bull-only |

## Correlation Notes
Top correlates:
- debt_lt: 0.991 (strongly positively correlated)
- fnd6_cptnewqv1300_dlttq: 0.991 (strongly positively correlated)
- fnd6_cptmfmq_dlttq: 0.991 (strongly positively correlated)
- fnd6_newqv1300_lltq: 0.983 (strongly positively correlated)
- fnd6_newa1v1300_dltt: 0.980 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_epsr_flag | analyst4 | -0.35 | 1.97 | +0.79 | -0.85 | yes |
| anl4_rd_exp_flag | analyst4 | -0.31 | 1.77 | +0.69 | -0.69 | yes |
| rp_ess_revenue | news18 | -0.35 | 1.71 | +0.63 | -0.81 | yes |
| net_profit_adjusted_min_guidance | analyst4 | -0.24 | 1.64 | +0.56 | -0.89 | yes |
| sharesout | pv1 | -0.12 | 1.56 | +0.49 | -0.80 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
