---
field: anl4_afv4_median_eps
dataset: analyst4
best_template: rank_value_norm
best_sharpe: 1.03
best_fitness: 0.82
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 9
max_drawdown: 0.0952
ann_vol: 0.0765
hit_rate: 0.515
rolling_sharpe_min: -1.29
rolling_sharpe_max: 3.374
top_merge_partner: rp_ess_revenue
redundancy_cluster: 1
negated_best_sharpe: 0.26
negated_best_template: rank_neg_delta
negated_best_fitness: 0.05
n_negated_sims: 10
direction_gap: -0.77
---
# anl4_afv4_median_eps (analyst4)

*Earnings per share - median of estimations*

## Signal Profile
- `rank(anl4_afv4_median_eps)`: S=0.46, F=0.29, T=1.2%, INFERIOR (TOP3000)
- `rank(anl4_afv4_median_eps / close)`: S=1.03, F=0.82, T=2.4%, INFERIOR (TOP3000)
- `rank(ts_delta(anl4_afv4_median_eps, 5))`: S=0.49, F=0.11, T=36.1%, INFERIOR (TOP3000)
- `-rank(anl4_afv4_median_eps)`: S=-0.28, F=-0.14, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_afv4_median_eps, 5))`: S=0.26, F=0.05, T=36.8%, INFERIOR (TOP3000)
- `ts_zscore(anl4_afv4_median_eps, 22)`: S=0.09, F=0.01, T=34.0%, INFERIOR (TOP3000)
- `ts_mean(anl4_afv4_median_eps, 10)`: S=-0.11, F=-0.03, T=1.0%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_afv4_median_eps, 22))`: S=-0.13, F=-0.03, T=14.1%, INFERIOR (TOP3000)
- `rank(-1 * anl4_afv4_median_eps)`: S=-0.18, F=-0.07, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * anl4_afv4_median_eps / close)`: S=-0.56, F=-0.41, T=3.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 2F/30P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 18F/11P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 1.03, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.35 (weak), ret=+2.0%
  - 2020: S=-0.24 (negative), ret=-2.3%
  - 2021: S=0.83 (moderate), ret=+7.0%
  - 2022: S=3.31 (strong), ret=+25.8%
  - 2023: S=1.19 (moderate), ret=+6.0%

## Risk & Drawdown
- Max drawdown: 9.52% over 488 days (recovered)
- Annualized: return +7.9%, volatility 7.6% (fraction of booksize)
- Hit rate: 51.5% positive days
- Tail shape: skew +0.37, excess kurtosis +1.75

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.29, max 3.37, latest 1.24

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +8.56%; worst month: -4.37%
Positive months: 61%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.74
- Sideways: S=-0.08
- Bear: S=-0.82

## Negated Direction
Best negated: `rank(-1 * ts_delta(anl4_afv4_median_eps, 5))` S=0.26, F=0.05, INFERIOR
Direction gap: -0.77 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * anl4_afv4_median_eps)`: S=-0.18, F=-0.07, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * anl4_afv4_median_eps / close)`: S=-0.56, F=-0.41, T=3.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_afv4_median_eps, 5))`: S=0.26, F=0.05, T=36.8%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_afv4_median_eps / close)` | TOP3000 | 1.03 | 0.82 | 9.5% | 80% | bull-only |
| `rank(anl4_afv4_median_eps / close)` | TOP1000 | 0.63 | 0.48 | 17.3% | 80% | bull-only |
| `rank(anl4_afv4_median_eps / close)` | TOP500 | 0.54 | 0.41 | 19.2% | 80% | bull-only |
| `rank(anl4_afv4_median_eps)` | TOP3000 | 0.46 | 0.29 | 37.3% | 60% | bull-only |
| `rank(anl4_afv4_median_eps / close)` | TOP200 | 0.40 | 0.29 | 31.0% | 60% | bull-only |
| `rank(anl4_afv4_median_eps)` | TOP200 | 0.28 | 0.16 | 31.5% | 60% | bull-only |
| `rank(anl4_afv4_median_eps)` | TOP1000 | 0.27 | 0.14 | 39.1% | 60% | bull-only |
| `rank(ts_delta(anl4_afv4_median_eps, 5))` | TOP3000 | 0.49 | 0.11 | 4.6% | 80% | weak |
| `rank(anl4_afv4_median_eps)` | TOP500 | 0.18 | 0.07 | 36.7% | 60% | bull-only |

## Correlation Notes
Top correlates:
- anl4_afv4_eps_mean: 0.997 (strongly positively correlated)
- anl4_afv4_eps_high: 0.955 (strongly positively correlated)
- anl4_afv4_eps_low: 0.931 (strongly positively correlated)
- anl4_qf_az_hgih_spe: 0.867 (strongly positively correlated)
- anl4_qfd1_az_hgih_spe: 0.867 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| rp_ess_revenue | news18 | -0.35 | 1.64 | +0.61 | -0.34 | yes |
| fnd6_txtubadjust | fundamental6 | -0.25 | 1.53 | +0.50 | -0.95 | yes |
| anl4_rd_exp_flag | analyst4 | -0.29 | 1.69 | +0.66 | -0.70 | no |
| sharesout | pv1 | -0.11 | 1.50 | +0.47 | -0.90 | yes |
| anl4_epsr_flag | analyst4 | -0.29 | 1.84 | +0.66 | -0.14 | no |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
