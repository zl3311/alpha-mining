---
field: fnd6_newqv1300_lcoq
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 1.11
best_fitness: 0.82
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 8
max_drawdown: 0.0774
ann_vol: 0.0623
hit_rate: 0.5012
rolling_sharpe_min: -0.925
rolling_sharpe_max: 2.845
top_merge_partner: anl4_epsr_flag
redundancy_cluster: 1
negated_best_sharpe: 0.31
negated_best_template: rank_neg_delta
negated_best_fitness: 0.07
n_negated_sims: 10
direction_gap: -0.8
---
# fnd6_newqv1300_lcoq (fundamental6)

*Current Liabilities - Other - Total*

## Signal Profile
- `rank(fnd6_newqv1300_lcoq)`: S=0.88, F=0.70, T=2.5%, INFERIOR (TOP3000)
- `rank(fnd6_newqv1300_lcoq / close)`: S=1.11, F=0.82, T=2.7%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_newqv1300_lcoq, 5))`: S=0.21, F=0.05, T=39.0%, INFERIOR (TOP500)
- `-rank(fnd6_newqv1300_lcoq)`: S=-0.47, F=-0.29, T=3.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_lcoq, 5))`: S=0.31, F=0.07, T=39.2%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_newqv1300_lcoq, 22)`: S=0.62, F=0.24, T=38.5%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newqv1300_lcoq, 10)`: S=0.24, F=0.10, T=1.7%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newqv1300_lcoq, 22))`: S=0.24, F=0.06, T=17.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_lcoq)`: S=-0.47, F=-0.29, T=3.3%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_lcoq / close)`: S=-0.73, F=-0.50, T=3.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 9F/23P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 11F/18P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 1.10, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=-0.01 (negative), ret=-0.0%
  - 2020: S=1.00 (moderate), ret=+6.7%
  - 2021: S=1.98 (strong), ret=+15.3%
  - 2022: S=1.29 (moderate), ret=+7.8%
  - 2023: S=0.78 (moderate), ret=+3.9%

## Risk & Drawdown
- Max drawdown: 7.74% over 482 days (recovered)
- Annualized: return +6.9%, volatility 6.2% (fraction of booksize)
- Hit rate: 50.1% positive days
- Tail shape: skew +0.50, excess kurtosis +2.03

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.93, max 2.85, latest 0.91

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2019
Best month: +7.48%; worst month: -3.35%
Positive months: 56%

## Regime Profile
Regime profile: **mixed**
- Bull: S=2.82
- Sideways: S=0.13
- Bear: S=-0.15

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_newqv1300_lcoq, 5))` S=0.31, F=0.07, INFERIOR
Direction gap: -0.80 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_newqv1300_lcoq)`: S=-0.47, F=-0.29, T=3.3%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_lcoq / close)`: S=-0.73, F=-0.50, T=3.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_lcoq, 5))`: S=0.31, F=0.07, T=39.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newqv1300_lcoq / close)` | TOP3000 | 1.10 | 0.82 | 7.7% | 80% | mixed |
| `rank(fnd6_newqv1300_lcoq)` | TOP3000 | 0.88 | 0.70 | 20.0% | 80% | bull-only |
| `rank(fnd6_newqv1300_lcoq / close)` | TOP1000 | 0.73 | 0.50 | 9.0% | 80% | bull-only |
| `rank(fnd6_newqv1300_lcoq)` | TOP1000 | 0.46 | 0.29 | 26.3% | 80% | bull-only |
| `rank(fnd6_newqv1300_lcoq / close)` | TOP500 | 0.47 | 0.28 | 19.6% | 60% | bull-only |
| `rank(fnd6_newqv1300_lcoq)` | TOP500 | 0.19 | 0.09 | 41.9% | 60% | bull-only |
| `rank(ts_delta(fnd6_newqv1300_lcoq, 5))` | TOP500 | 0.20 | 0.05 | 12.0% | 40% | weak |
| `rank(ts_delta(fnd6_newqv1300_lcoq, 5))` | TOP200 | 0.15 | 0.03 | 24.3% | 20% | mixed |

## Correlation Notes
Top correlates:
- fnd6_newa1v1300_lco: 0.978 (strongly positively correlated)
- fnd6_cptnewqv1300_lctq: 0.969 (strongly positively correlated)
- liabilities_curr: 0.969 (strongly positively correlated)
- fnd6_cptmfmq_lctq: 0.968 (strongly positively correlated)
- fnd6_newa1v1300_lct: 0.953 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_epsr_flag | analyst4 | -0.32 | 1.87 | +0.70 | -0.58 | yes |
| anl4_cfo_flag | analyst4 | -0.04 | 1.60 | +0.48 | -0.85 | yes |
| pv13_ompetitorgraphrank_hub_rank | pv13 | -0.22 | 1.70 | +0.55 | +0.68 | yes |
| est_rd_expense | analyst4 | -0.10 | 1.65 | +0.54 | +0.34 | yes |
| rp_ess_revenue | news18 | -0.31 | 1.57 | +0.47 | -0.55 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
