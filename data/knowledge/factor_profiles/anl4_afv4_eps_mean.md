---
field: anl4_afv4_eps_mean
dataset: analyst4
best_template: rank_value_norm
best_sharpe: 1.01
best_fitness: 0.8
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 10
max_drawdown: 0.0988
ann_vol: 0.0772
hit_rate: 0.5198
rolling_sharpe_min: -1.259
rolling_sharpe_max: 3.401
top_merge_partner: rp_ess_revenue
redundancy_cluster: 1
negated_best_sharpe: 0.42
negated_best_template: rank_neg_delta
negated_best_fitness: 0.13
n_negated_sims: 10
direction_gap: -0.59
---
# anl4_afv4_eps_mean (analyst4)

*Earnings per share - mean of estimations for annual frequency*

## Signal Profile
- `rank(anl4_afv4_eps_mean)`: S=0.44, F=0.28, T=1.2%, INFERIOR (TOP3000)
- `rank(anl4_afv4_eps_mean / close)`: S=1.01, F=0.80, T=2.4%, INFERIOR (TOP3000)
- `rank(ts_delta(anl4_afv4_eps_mean, 5))`: S=0.42, F=0.09, T=35.4%, INFERIOR (TOP3000)
- `-rank(anl4_afv4_eps_mean)`: S=-0.26, F=-0.13, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_afv4_eps_mean, 5))`: S=0.42, F=0.13, T=35.9%, INFERIOR (TOP3000)
- `ts_zscore(anl4_afv4_eps_mean, 22)`: S=0.15, F=0.03, T=32.7%, INFERIOR (TOP3000)
- `ts_mean(anl4_afv4_eps_mean, 10)`: S=-0.11, F=-0.03, T=1.0%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_afv4_eps_mean, 22))`: S=-0.27, F=-0.08, T=14.4%, INFERIOR (TOP3000)
- `rank(-1 * anl4_afv4_eps_mean)`: S=-0.23, F=-0.11, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * anl4_afv4_eps_mean / close)`: S=-0.29, F=-0.17, T=3.5%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 1F/31P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 10F/10P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 1.00, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.29 (weak), ret=+1.7%
  - 2020: S=-0.21 (negative), ret=-1.9%
  - 2021: S=0.76 (moderate), ret=+6.4%
  - 2022: S=3.33 (strong), ret=+26.4%
  - 2023: S=1.02 (moderate), ret=+5.4%

## Risk & Drawdown
- Max drawdown: 9.88% over 496 days (recovered)
- Annualized: return +7.7%, volatility 7.7% (fraction of booksize)
- Hit rate: 52.0% positive days
- Tail shape: skew +0.36, excess kurtosis +1.79

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.26, max 3.40, latest 1.07

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +8.89%; worst month: -4.39%
Positive months: 59%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.72
- Sideways: S=-0.09
- Bear: S=-0.87

## Negated Direction
Best negated: `rank(-1 * ts_delta(anl4_afv4_eps_mean, 5))` S=0.42, F=0.13, INFERIOR
Direction gap: -0.59 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * anl4_afv4_eps_mean)`: S=-0.23, F=-0.11, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * anl4_afv4_eps_mean / close)`: S=-0.29, F=-0.17, T=3.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_afv4_eps_mean, 5))`: S=0.42, F=0.13, T=35.9%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_afv4_eps_mean / close)` | TOP3000 | 1.00 | 0.80 | 9.9% | 80% | bull-only |
| `rank(anl4_afv4_eps_mean / close)` | TOP1000 | 0.59 | 0.45 | 17.4% | 80% | bull-only |
| `rank(anl4_afv4_eps_mean / close)` | TOP500 | 0.50 | 0.36 | 20.4% | 80% | bull-only |
| `rank(anl4_afv4_eps_mean)` | TOP3000 | 0.44 | 0.28 | 37.5% | 60% | bull-only |
| `rank(anl4_afv4_eps_mean / close)` | TOP200 | 0.28 | 0.17 | 34.6% | 60% | bull-only |
| `rank(anl4_afv4_eps_mean)` | TOP1000 | 0.25 | 0.13 | 39.5% | 60% | bull-only |
| `rank(anl4_afv4_eps_mean)` | TOP200 | 0.22 | 0.11 | 33.4% | 60% | bull-only |
| `rank(ts_delta(anl4_afv4_eps_mean, 5))` | TOP3000 | 0.42 | 0.09 | 6.0% | 40% | weak |
| `rank(ts_delta(anl4_afv4_eps_mean, 5))` | TOP1000 | 0.30 | 0.06 | 12.2% | 60% | weak |
| `rank(anl4_afv4_eps_mean)` | TOP500 | 0.16 | 0.06 | 37.4% | 60% | bull-only |

## Correlation Notes
Top correlates:
- anl4_afv4_median_eps: 0.997 (strongly positively correlated)
- anl4_afv4_eps_high: 0.948 (strongly positively correlated)
- anl4_afv4_eps_low: 0.939 (strongly positively correlated)
- anl4_qf_az_hgih_spe: 0.873 (strongly positively correlated)
- anl4_qfd1_az_hgih_spe: 0.873 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| rp_ess_revenue | news18 | -0.35 | 1.62 | +0.62 | -0.31 | yes |
| fnd6_txtubadjust | fundamental6 | -0.26 | 1.51 | +0.51 | -0.94 | yes |
| anl4_rd_exp_flag | analyst4 | -0.29 | 1.68 | +0.65 | -0.68 | no |
| sharesout | pv1 | -0.11 | 1.50 | +0.46 | -0.91 | yes |
| systematic_risk_last_360_days | model51 | -0.13 | 1.51 | +0.49 | -0.28 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
