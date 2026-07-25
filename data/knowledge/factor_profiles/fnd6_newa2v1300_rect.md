---
field: fnd6_newa2v1300_rect
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 0.92
best_fitness: 0.73
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 6
max_drawdown: 0.0919
ann_vol: 0.0853
hit_rate: 0.4931
rolling_sharpe_min: -1.235
rolling_sharpe_max: 2.756
top_merge_partner: rp_ess_revenue
redundancy_cluster: 1
negated_best_sharpe: 1.05
negated_best_template: rank_neg_delta
negated_best_fitness: 0.63
n_negated_sims: 10
direction_gap: 0.13
---
# fnd6_newa2v1300_rect (fundamental6)

*Receivables - Total*

## Signal Profile
- `rank(fnd6_newa2v1300_rect)`: S=0.63, F=0.49, T=0.9%, INFERIOR (TOP3000)
- `rank(fnd6_newa2v1300_rect / close)`: S=0.92, F=0.73, T=1.3%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_newa2v1300_rect, 5))`: S=-0.39, F=-0.19, T=34.0%, INFERIOR (TOP200)
- `-rank(fnd6_newa2v1300_rect)`: S=-0.42, F=-0.29, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa2v1300_rect, 5))`: S=1.05, F=0.63, T=34.4%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_newa2v1300_rect, 63)`: S=0.00, F=0.00, T=19.6%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newa2v1300_rect, 10)`: S=0.17, F=0.06, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newa2v1300_rect, 22))`: S=0.09, F=0.02, T=14.3%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa2v1300_rect)`: S=-0.42, F=-0.29, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa2v1300_rect / close)`: S=-0.66, F=-0.50, T=1.8%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/15P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.92, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.16 (negative), ret=-0.8%
  - 2020: S=-0.16 (negative), ret=-1.6%
  - 2021: S=1.67 (strong), ret=+18.5%
  - 2022: S=1.90 (strong), ret=+17.6%
  - 2023: S=1.00 (moderate), ret=+4.5%

## Risk & Drawdown
- Max drawdown: 9.19% over 214 days (recovered)
- Annualized: return +7.8%, volatility 8.5% (fraction of booksize)
- Hit rate: 49.3% positive days
- Tail shape: skew +0.48, excess kurtosis +3.08

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.24, max 2.76, latest 0.97

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2019
Best month: +10.31%; worst month: -3.50%
Positive months: 54%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.44
- Sideways: S=0.20
- Bear: S=-1.64

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_newa2v1300_rect, 5))` S=1.05, F=0.63, INFERIOR
Direction gap: +0.13 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fnd6_newa2v1300_rect)`: S=-0.42, F=-0.29, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa2v1300_rect / close)`: S=-0.66, F=-0.50, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa2v1300_rect, 5))`: S=1.05, F=0.63, T=34.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newa2v1300_rect / close)` | TOP3000 | 0.92 | 0.73 | 9.2% | 60% | bull-only |
| `rank(fnd6_newa2v1300_rect / close)` | TOP1000 | 0.65 | 0.50 | 13.6% | 60% | bull-only |
| `rank(fnd6_newa2v1300_rect)` | TOP3000 | 0.62 | 0.49 | 33.9% | 80% | bull-only |
| `rank(fnd6_newa2v1300_rect)` | TOP1000 | 0.41 | 0.29 | 34.2% | 60% | bull-only |
| `rank(fnd6_newa2v1300_rect / close)` | TOP500 | 0.38 | 0.23 | 24.9% | 80% | bull-only |
| `rank(fnd6_newa2v1300_rect)` | TOP500 | 0.15 | 0.07 | 47.5% | 60% | bull-only |

## Correlation Notes
Top correlates:
- receivable: 0.990 (strongly positively correlated)
- fnd6_cptnewqv1300_rectq: 0.990 (strongly positively correlated)
- fnd6_rectr: 0.989 (strongly positively correlated)
- fnd6_newa2v1300_sale: 0.986 (strongly positively correlated)
- fnd6_newa2v1300_revt: 0.986 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| rp_ess_revenue | news18 | -0.37 | 1.60 | +0.68 | -0.71 | yes |
| anl4_rd_exp_flag | analyst4 | -0.34 | 1.69 | +0.66 | -0.53 | yes |
| anl4_epsr_flag | analyst4 | -0.33 | 1.82 | +0.64 | -0.51 | yes |
| net_profit_adjusted_min_guidance | analyst4 | -0.24 | 1.51 | +0.57 | -0.71 | yes |
| max_gross_income_guidance_2 | analyst4 | -0.32 | 1.46 | +0.54 | -0.78 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
