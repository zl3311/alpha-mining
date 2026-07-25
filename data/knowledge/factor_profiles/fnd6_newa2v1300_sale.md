---
field: fnd6_newa2v1300_sale
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 1.03
best_fitness: 0.88
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 10
max_drawdown: 0.0992
ann_vol: 0.0885
hit_rate: 0.5045
rolling_sharpe_min: -1.174
rolling_sharpe_max: 2.659
top_merge_partner: anl4_rd_exp_flag
redundancy_cluster: 1
negated_best_sharpe: 0.16
negated_best_template: neg_rank_level
negated_best_fitness: 0.08
n_negated_sims: 10
direction_gap: -0.87
---
# fnd6_newa2v1300_sale (fundamental6)

*Sales/Turnover (Net)*

## Signal Profile
- `rank(fnd6_newa2v1300_sale)`: S=0.66, F=0.53, T=0.9%, INFERIOR (TOP3000)
- `rank(fnd6_newa2v1300_sale / close)`: S=1.03, F=0.88, T=1.4%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_newa2v1300_sale, 5))`: S=0.45, F=0.24, T=33.8%, INFERIOR (TOP200)
- `-rank(fnd6_newa2v1300_sale)`: S=-0.35, F=-0.22, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa2v1300_sale, 5))`: S=-0.36, F=-0.17, T=33.6%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_newa2v1300_sale, 63)`: S=0.05, F=0.01, T=20.6%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newa2v1300_sale, 10)`: S=0.15, F=0.05, T=1.0%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newa2v1300_sale, 22))`: S=0.08, F=0.02, T=14.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa2v1300_sale)`: S=0.16, F=0.08, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa2v1300_sale / close)`: S=0.01, F=0.00, T=2.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 11F/9P
- LOW_TURNOVER: 2F/30P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 1.02, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=-0.19 (negative), ret=-1.0%
  - 2020: S=0.13 (weak), ret=+1.3%
  - 2021: S=1.59 (strong), ret=+18.7%
  - 2022: S=1.93 (strong), ret=+18.1%
  - 2023: S=1.52 (strong), ret=+7.2%

## Risk & Drawdown
- Max drawdown: 9.92% over 238 days (recovered)
- Annualized: return +9.0%, volatility 8.8% (fraction of booksize)
- Hit rate: 50.4% positive days
- Tail shape: skew +0.45, excess kurtosis +3.04

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.17, max 2.66, latest 1.50

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2019
Best month: +10.07%; worst month: -3.55%
Positive months: 63%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.43
- Sideways: S=0.41
- Bear: S=-1.44

## Negated Direction
Best negated: `rank(-1 * fnd6_newa2v1300_sale)` S=0.16, F=0.08, INFERIOR
Direction gap: -0.87 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_newa2v1300_sale)`: S=0.16, F=0.08, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa2v1300_sale / close)`: S=0.01, F=0.00, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa2v1300_sale, 5))`: S=-0.36, F=-0.17, T=33.6%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newa2v1300_sale / close)` | TOP3000 | 1.02 | 0.88 | 9.9% | 80% | bull-only |
| `rank(fnd6_newa2v1300_sale)` | TOP3000 | 0.66 | 0.53 | 32.4% | 80% | bull-only |
| `rank(fnd6_newa2v1300_sale / close)` | TOP1000 | 0.62 | 0.47 | 14.5% | 60% | bull-only |
| `rank(ts_delta(fnd6_newa2v1300_sale, 5))` | TOP200 | 0.45 | 0.24 | 40.1% | 80% | mixed |
| `rank(fnd6_newa2v1300_sale)` | TOP1000 | 0.34 | 0.22 | 37.0% | 60% | bull-only |
| `rank(fnd6_newa2v1300_sale / close)` | TOP500 | 0.36 | 0.21 | 26.2% | 60% | bull-only |
| `rank(ts_delta(fnd6_newa2v1300_sale, 5))` | TOP500 | 0.24 | 0.09 | 62.2% | 40% | mixed |
| `rank(ts_delta(fnd6_newa2v1300_sale, 5))` | TOP1000 | 0.26 | 0.08 | 40.2% | 80% | mixed |
| `rank(ts_delta(fnd6_newa2v1300_sale, 5))` | TOP3000 | 0.23 | 0.06 | 16.0% | 80% | weak |
| `rank(fnd6_newa2v1300_sale)` | TOP500 | 0.11 | 0.05 | 48.6% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_newa2v1300_revt: 1.000 (strongly positively correlated)
- fnd6_mfma2_revt: 1.000 (strongly positively correlated)
- fnd6_cptmfmq_saleq: 0.989 (strongly positively correlated)
- sales: 0.989 (strongly positively correlated)
- fnd6_cptnewqv1300_saleq: 0.989 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_rd_exp_flag | analyst4 | -0.35 | 1.78 | +0.75 | -0.42 | yes |
| anl4_epsr_flag | analyst4 | -0.33 | 1.90 | +0.73 | -0.31 | yes |
| rp_ess_revenue | news18 | -0.37 | 1.69 | +0.67 | -0.57 | yes |
| net_profit_adjusted_min_guidance | analyst4 | -0.24 | 1.59 | +0.57 | -0.56 | yes |
| max_gross_income_guidance_2 | analyst4 | -0.32 | 1.55 | +0.53 | -0.78 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
