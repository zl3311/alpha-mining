---
field: fnd6_cptnewqv1300_rectq
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 0.96
best_fitness: 0.78
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 7
max_drawdown: 0.1052
ann_vol: 0.0861
hit_rate: 0.4955
rolling_sharpe_min: -1.449
rolling_sharpe_max: 2.788
top_merge_partner: anl4_rd_exp_flag
redundancy_cluster: 1
negated_best_sharpe: 1.15
negated_best_template: rank_neg_delta
negated_best_fitness: 0.52
n_negated_sims: 10
direction_gap: 0.19
---
# fnd6_cptnewqv1300_rectq (fundamental6)

*Receivables - Total*

## Signal Profile
- `rank(fnd6_cptnewqv1300_rectq)`: S=0.73, F=0.61, T=2.1%, INFERIOR (TOP3000)
- `rank(fnd6_cptnewqv1300_rectq / close)`: S=0.96, F=0.78, T=2.3%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_cptnewqv1300_rectq, 5))`: S=-0.48, F=-0.12, T=38.1%, INFERIOR (TOP3000)
- `-rank(fnd6_cptnewqv1300_rectq)`: S=-0.46, F=-0.33, T=2.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_cptnewqv1300_rectq, 5))`: S=1.15, F=0.52, T=38.6%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_cptnewqv1300_rectq, 63)`: S=-0.03, F=0.00, T=19.0%, INFERIOR (TOP3000)
- `ts_mean(fnd6_cptnewqv1300_rectq, 10)`: S=-0.04, F=-0.01, T=2.2%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_cptnewqv1300_rectq, 22))`: S=-0.42, F=-0.14, T=17.3%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_cptnewqv1300_rectq)`: S=-0.46, F=-0.33, T=2.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_cptnewqv1300_rectq / close)`: S=-0.68, F=-0.52, T=3.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 9F/23P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 11F/18P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.96, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.14 (negative), ret=-0.7%
  - 2020: S=-0.23 (negative), ret=-2.3%
  - 2021: S=1.86 (strong), ret=+21.4%
  - 2022: S=1.95 (strong), ret=+17.5%
  - 2023: S=1.01 (moderate), ret=+4.5%

## Risk & Drawdown
- Max drawdown: 10.52% over 764 days (recovered)
- Annualized: return +8.2%, volatility 8.6% (fraction of booksize)
- Hit rate: 49.5% positive days
- Tail shape: skew +0.44, excess kurtosis +3.11

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.45, max 2.79, latest 1.00

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +9.84%; worst month: -3.57%
Positive months: 56%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.51
- Sideways: S=0.24
- Bear: S=-1.62

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_cptnewqv1300_rectq, 5))` S=1.15, F=0.52, INFERIOR
Direction gap: +0.19 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fnd6_cptnewqv1300_rectq)`: S=-0.46, F=-0.33, T=2.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_cptnewqv1300_rectq / close)`: S=-0.68, F=-0.52, T=3.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_cptnewqv1300_rectq, 5))`: S=1.15, F=0.52, T=38.6%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_cptnewqv1300_rectq / close)` | TOP3000 | 0.96 | 0.78 | 10.5% | 60% | bull-only |
| `rank(fnd6_cptnewqv1300_rectq)` | TOP3000 | 0.72 | 0.61 | 32.7% | 80% | bull-only |
| `rank(fnd6_cptnewqv1300_rectq / close)` | TOP1000 | 0.67 | 0.52 | 14.1% | 80% | bull-only |
| `rank(fnd6_cptnewqv1300_rectq / close)` | TOP500 | 0.51 | 0.36 | 23.5% | 80% | bull-only |
| `rank(fnd6_cptnewqv1300_rectq)` | TOP1000 | 0.45 | 0.33 | 35.5% | 60% | bull-only |
| `rank(fnd6_cptnewqv1300_rectq)` | TOP500 | 0.27 | 0.16 | 46.0% | 80% | bull-only |
| `rank(fnd6_cptnewqv1300_rectq / close)` | TOP200 | 0.10 | 0.03 | 36.3% | 60% | bull-only |

## Correlation Notes
Top correlates:
- receivable: 1.000 (strongly positively correlated)
- fnd6_newa2v1300_rect: 0.990 (strongly positively correlated)
- fnd6_newqv1300_rectrq: 0.987 (strongly positively correlated)
- fnd6_rectr: 0.984 (strongly positively correlated)
- fnd6_mfma2_revt: 0.980 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_rd_exp_flag | analyst4 | -0.36 | 1.74 | +0.71 | -0.55 | yes |
| rp_ess_revenue | news18 | -0.36 | 1.62 | +0.66 | -0.76 | yes |
| anl4_epsr_flag | analyst4 | -0.33 | 1.84 | +0.67 | -0.57 | yes |
| net_profit_adjusted_min_guidance | analyst4 | -0.25 | 1.55 | +0.60 | -0.75 | yes |
| max_gross_income_guidance_2 | analyst4 | -0.33 | 1.50 | +0.54 | -0.78 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
