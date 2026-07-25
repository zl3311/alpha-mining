---
field: fnd6_cptnewqv1300_ltq
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 1.05
best_fitness: 0.86
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 8
max_drawdown: 0.0834
ann_vol: 0.0814
hit_rate: 0.4939
rolling_sharpe_min: -0.728
rolling_sharpe_max: 2.715
top_merge_partner: anl4_epsr_flag
redundancy_cluster: 1
negated_best_sharpe: 0.07
negated_best_template: rank_neg_delta
negated_best_fitness: 0.01
n_negated_sims: 10
direction_gap: -0.98
---
# fnd6_cptnewqv1300_ltq (fundamental6)

*Liabilities - Total*

## Signal Profile
- `rank(fnd6_cptnewqv1300_ltq)`: S=0.82, F=0.70, T=1.4%, INFERIOR (TOP3000)
- `rank(fnd6_cptnewqv1300_ltq / close)`: S=1.05, F=0.86, T=1.7%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_cptnewqv1300_ltq, 5))`: S=0.26, F=0.06, T=37.3%, INFERIOR (TOP1000)
- `-rank(fnd6_cptnewqv1300_ltq)`: S=-0.40, F=-0.26, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_cptnewqv1300_ltq, 5))`: S=0.07, F=0.01, T=37.4%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_cptnewqv1300_ltq, 63)`: S=0.57, F=0.22, T=18.9%, INFERIOR (TOP3000)
- `ts_mean(fnd6_cptnewqv1300_ltq, 10)`: S=0.28, F=0.12, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_cptnewqv1300_ltq, 22))`: S=-0.33, F=-0.10, T=16.7%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_cptnewqv1300_ltq)`: S=-0.82, F=-0.70, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_cptnewqv1300_ltq / close)`: S=-1.05, F=-0.86, T=1.7%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 6F/26P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 17F/12P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 1.04, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.25 (weak), ret=+1.2%
  - 2020: S=0.56 (moderate), ret=+5.5%
  - 2021: S=1.73 (strong), ret=+18.3%
  - 2022: S=1.64 (strong), ret=+12.0%
  - 2023: S=0.80 (moderate), ret=+4.4%

## Risk & Drawdown
- Max drawdown: 8.34% over 236 days (recovered)
- Annualized: return +8.5%, volatility 8.1% (fraction of booksize)
- Hit rate: 49.4% positive days
- Tail shape: skew +0.61, excess kurtosis +3.44

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.73, max 2.71, latest 0.88

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2019
Best month: +8.97%; worst month: -3.48%
Positive months: 59%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.99
- Sideways: S=0.40
- Bear: S=-0.75

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_cptnewqv1300_ltq, 5))` S=0.07, F=0.01, INFERIOR
Direction gap: -0.98 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_cptnewqv1300_ltq)`: S=-0.82, F=-0.70, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_cptnewqv1300_ltq / close)`: S=-1.05, F=-0.86, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_cptnewqv1300_ltq, 5))`: S=0.07, F=0.01, T=37.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_cptnewqv1300_ltq / close)` | TOP3000 | 1.04 | 0.86 | 8.3% | 100% | bull-only |
| `rank(fnd6_cptnewqv1300_ltq)` | TOP3000 | 0.81 | 0.70 | 25.8% | 80% | bull-only |
| `rank(fnd6_cptnewqv1300_ltq / close)` | TOP1000 | 0.62 | 0.45 | 14.7% | 60% | bull-only |
| `rank(fnd6_cptnewqv1300_ltq / close)` | TOP500 | 0.45 | 0.29 | 21.5% | 60% | bull-only |
| `rank(fnd6_cptnewqv1300_ltq)` | TOP1000 | 0.39 | 0.26 | 32.6% | 60% | bull-only |
| `rank(fnd6_cptnewqv1300_ltq)` | TOP500 | 0.19 | 0.10 | 47.4% | 60% | bull-only |
| `rank(ts_delta(fnd6_cptnewqv1300_ltq, 5))` | TOP1000 | 0.27 | 0.06 | 13.5% | 80% | weak |
| `rank(fnd6_cptnewqv1300_ltq / close)` | TOP200 | 0.13 | 0.05 | 31.8% | 60% | bull-only |

## Correlation Notes
Top correlates:
- liabilities: 1.000 (strongly positively correlated)
- fnd6_newqv1300_ltmibq: 1.000 (strongly positively correlated)
- fnd6_newa1v1300_lt: 0.993 (strongly positively correlated)
- fnd6_mfma1_at: 0.978 (strongly positively correlated)
- fnd6_newa1v1300_at: 0.977 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_epsr_flag | analyst4 | -0.36 | 1.95 | +0.77 | -0.64 | yes |
| rp_ess_revenue | news18 | -0.34 | 1.65 | +0.61 | -0.70 | yes |
| anl4_rd_exp_flag | analyst4 | -0.24 | 1.66 | +0.62 | -0.35 | yes |
| net_profit_adjusted_min_guidance | analyst4 | -0.19 | 1.55 | +0.51 | -0.67 | yes |
| max_gross_income_guidance_2 | analyst4 | -0.28 | 1.50 | +0.46 | -0.89 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
