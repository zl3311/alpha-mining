---
field: fnd6_rectr
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 0.97
best_fitness: 0.8
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 6
max_drawdown: 0.0947
ann_vol: 0.0869
hit_rate: 0.5012
rolling_sharpe_min: -1.206
rolling_sharpe_max: 2.869
top_merge_partner: anl4_rd_exp_flag
redundancy_cluster: 1
negated_best_sharpe: 0.87
negated_best_template: rank_neg_delta
negated_best_fitness: 0.42
n_negated_sims: 10
direction_gap: -0.1
---
# fnd6_rectr (fundamental6)

*Receivables - Trade*

## Signal Profile
- `rank(fnd6_rectr)`: S=0.65, F=0.52, T=1.0%, INFERIOR (TOP3000)
- `rank(fnd6_rectr / close)`: S=0.97, F=0.80, T=1.4%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_rectr, 5))`: S=-0.03, F=0.00, T=33.7%, INFERIOR (TOP500)
- `-rank(fnd6_rectr)`: S=-0.37, F=-0.24, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_rectr, 5))`: S=0.87, F=0.42, T=35.7%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_rectr, 22)`: S=0.41, F=0.22, T=26.9%, INFERIOR (TOP3000)
- `ts_mean(fnd6_rectr, 10)`: S=0.58, F=0.40, T=1.3%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_rectr, 22))`: S=0.47, F=0.23, T=14.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_rectr)`: S=-0.65, F=-0.52, T=1.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_rectr / close)`: S=-0.97, F=-0.80, T=1.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 19F/10P
- LOW_TURNOVER: 4F/28P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.97, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.16 (weak), ret=+0.8%
  - 2020: S=-0.20 (negative), ret=-1.9%
  - 2021: S=1.76 (strong), ret=+20.6%
  - 2022: S=1.90 (strong), ret=+18.2%
  - 2023: S=0.78 (moderate), ret=+3.5%

## Risk & Drawdown
- Max drawdown: 9.47% over 377 days (recovered)
- Annualized: return +8.4%, volatility 8.7% (fraction of booksize)
- Hit rate: 50.1% positive days
- Tail shape: skew +0.42, excess kurtosis +2.92

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.21, max 2.87, latest 0.74

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +10.35%; worst month: -3.28%
Positive months: 54%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.57
- Sideways: S=0.21
- Bear: S=-1.73

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_rectr, 5))` S=0.87, F=0.42, INFERIOR
Direction gap: -0.10 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_rectr)`: S=-0.65, F=-0.52, T=1.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_rectr / close)`: S=-0.97, F=-0.80, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_rectr, 5))`: S=0.87, F=0.42, T=35.7%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_rectr / close)` | TOP3000 | 0.97 | 0.80 | 9.5% | 80% | bull-only |
| `rank(fnd6_rectr)` | TOP3000 | 0.65 | 0.52 | 34.1% | 80% | bull-only |
| `rank(fnd6_rectr / close)` | TOP1000 | 0.66 | 0.51 | 14.7% | 60% | bull-only |
| `rank(fnd6_rectr / close)` | TOP500 | 0.38 | 0.24 | 28.3% | 60% | bull-only |
| `rank(fnd6_rectr)` | TOP1000 | 0.36 | 0.24 | 37.0% | 60% | bull-only |
| `rank(fnd6_rectr)` | TOP500 | 0.13 | 0.05 | 51.5% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_newa2v1300_rect: 0.989 (strongly positively correlated)
- fnd6_newqv1300_rectrq: 0.989 (strongly positively correlated)
- receivable: 0.984 (strongly positively correlated)
- fnd6_cptnewqv1300_rectq: 0.984 (strongly positively correlated)
- fnd6_mfma2_revt: 0.979 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_rd_exp_flag | analyst4 | -0.38 | 1.78 | +0.75 | -0.63 | yes |
| rp_ess_revenue | news18 | -0.37 | 1.64 | +0.67 | -0.80 | yes |
| anl4_epsr_flag | analyst4 | -0.32 | 1.84 | +0.66 | -0.64 | yes |
| net_profit_adjusted_min_guidance | analyst4 | -0.27 | 1.58 | +0.61 | -0.82 | yes |
| max_gross_income_guidance_2 | analyst4 | -0.32 | 1.50 | +0.54 | -0.72 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
