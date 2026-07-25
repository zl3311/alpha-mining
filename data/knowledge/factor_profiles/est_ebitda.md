---
field: est_ebitda
dataset: analyst4
best_template: rank_value_norm
best_sharpe: 0.91
best_fitness: 0.73
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 9
max_drawdown: 0.158
ann_vol: 0.0883
hit_rate: 0.5012
rolling_sharpe_min: -1.587
rolling_sharpe_max: 2.916
top_merge_partner: rp_ess_revenue
redundancy_cluster: 1
negated_best_sharpe: 0.27
negated_best_template: rank_neg_delta
negated_best_fitness: 0.07
n_negated_sims: 10
direction_gap: -0.64
---
# est_ebitda (analyst4)

*Earnings before interest, taxes, depreciation, and amortization - mean of estimations*

## Signal Profile
- `rank(est_ebitda)`: S=0.49, F=0.34, T=1.0%, INFERIOR (TOP3000)
- `rank(est_ebitda / close)`: S=0.91, F=0.73, T=1.4%, INFERIOR (TOP3000)
- `rank(ts_delta(est_ebitda, 5))`: S=0.25, F=0.04, T=36.0%, INFERIOR (TOP3000)
- `-rank(est_ebitda)`: S=-0.22, F=-0.11, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(est_ebitda, 5))`: S=0.27, F=0.07, T=36.1%, INFERIOR (TOP3000)
- `ts_zscore(est_ebitda, 22)`: S=-0.08, F=-0.01, T=33.9%, INFERIOR (TOP3000)
- `ts_mean(est_ebitda, 10)`: S=0.14, F=0.05, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_rank(est_ebitda, 22))`: S=-0.02, F=0.00, T=14.2%, INFERIOR (TOP3000)
- `rank(-1 * est_ebitda)`: S=-0.07, F=-0.02, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * est_ebitda / close)`: S=-0.13, F=-0.05, T=2.2%, INFERIOR (TOP3000)

## Check Summary
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 15F/5P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.91, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.04 (weak), ret=+0.2%
  - 2020: S=-0.86 (negative), ret=-6.9%
  - 2021: S=1.62 (strong), ret=+19.1%
  - 2022: S=1.94 (strong), ret=+21.3%
  - 2023: S=1.08 (moderate), ret=+5.6%

## Risk & Drawdown
- Max drawdown: 15.80% over 544 days (recovered)
- Annualized: return +8.0%, volatility 8.8% (fraction of booksize)
- Hit rate: 50.1% positive days
- Tail shape: skew +0.20, excess kurtosis +2.23

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.59, max 2.92, latest 0.90

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +9.90%; worst month: -3.35%
Positive months: 58%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.60
- Sideways: S=0.92
- Bear: S=-2.52

## Negated Direction
Best negated: `rank(-1 * ts_delta(est_ebitda, 5))` S=0.27, F=0.07, INFERIOR
Direction gap: -0.64 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * est_ebitda)`: S=-0.07, F=-0.02, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * est_ebitda / close)`: S=-0.13, F=-0.05, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(est_ebitda, 5))`: S=0.27, F=0.07, T=36.1%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(est_ebitda / close)` | TOP3000 | 0.91 | 0.73 | 15.8% | 80% | bull-only |
| `rank(est_ebitda)` | TOP3000 | 0.49 | 0.34 | 38.5% | 80% | bull-only |
| `rank(est_ebitda / close)` | TOP1000 | 0.45 | 0.28 | 21.6% | 60% | bull-only |
| `rank(est_ebitda / close)` | TOP500 | 0.27 | 0.14 | 35.3% | 60% | bull-only |
| `rank(est_ebitda)` | TOP1000 | 0.21 | 0.11 | 41.9% | 60% | bull-only |
| `rank(est_ebitda)` | TOP500 | 0.16 | 0.07 | 47.9% | 60% | bull-only |
| `rank(est_ebitda / close)` | TOP200 | 0.12 | 0.05 | 33.0% | 60% | bull-only |
| `rank(ts_delta(est_ebitda, 5))` | TOP3000 | 0.28 | 0.04 | 7.0% | 60% | bull-only |
| `rank(est_ebitda)` | TOP200 | 0.06 | 0.02 | 43.5% | 60% | bull-only |

## Correlation Notes
Top correlates:
- anl4_ebitda_mean: 0.994 (strongly positively correlated)
- anl4_medianepsbfam: 0.994 (strongly positively correlated)
- anl4_ebitda_low: 0.991 (strongly positively correlated)
- anl4_ebitda_high: 0.989 (strongly positively correlated)
- anl4_ebit_high: 0.961 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| rp_ess_revenue | news18 | -0.34 | 1.56 | +0.65 | -0.78 | yes |
| anl4_rd_exp_flag | analyst4 | -0.42 | 1.79 | +0.76 | -0.73 | no |
| fnd6_txtubadjust | fundamental6 | -0.29 | 1.48 | +0.57 | -0.88 | yes |
| news_open_vol | news12 | -0.20 | 1.44 | +0.51 | -0.57 | yes |
| sharesout | pv1 | -0.20 | 1.53 | +0.49 | -0.69 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
