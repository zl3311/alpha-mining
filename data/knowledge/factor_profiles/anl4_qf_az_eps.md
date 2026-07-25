---
field: anl4_qf_az_eps
dataset: analyst4
best_template: rank_value_norm
best_sharpe: 0.9
best_fitness: 0.74
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 8
max_drawdown: 0.113
ann_vol: 0.0933
hit_rate: 0.5045
rolling_sharpe_min: -1.115
rolling_sharpe_max: 2.998
top_merge_partner: rp_ess_revenue
redundancy_cluster: 1
negated_best_sharpe: 0.16
negated_best_template: rank_neg_delta
negated_best_fitness: 0.03
n_negated_sims: 10
direction_gap: -0.74
---
# anl4_qf_az_eps (analyst4)

*EPS - aggregation on estimations, 50th percentile*

## Signal Profile
- `rank(anl4_qf_az_eps)`: S=0.40, F=0.25, T=1.2%, INFERIOR (TOP3000)
- `rank(anl4_qf_az_eps / close)`: S=0.90, F=0.74, T=2.2%, INFERIOR (TOP3000)
- `rank(ts_delta(anl4_qf_az_eps, 5))`: S=0.41, F=0.09, T=36.7%, INFERIOR (TOP1000)
- `-rank(anl4_qf_az_eps)`: S=-0.16, F=-0.06, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_qf_az_eps, 5))`: S=0.16, F=0.03, T=36.9%, INFERIOR (TOP3000)
- `ts_zscore(anl4_qf_az_eps, 22)`: S=0.24, F=0.05, T=33.7%, INFERIOR (TOP3000)
- `ts_mean(anl4_qf_az_eps, 10)`: S=-0.10, F=-0.03, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_qf_az_eps, 22))`: S=0.08, F=0.01, T=14.3%, INFERIOR (TOP3000)
- `rank(-1 * anl4_qf_az_eps)`: S=-0.08, F=-0.02, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * anl4_qf_az_eps / close)`: S=-0.14, F=-0.05, T=3.0%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 2F/30P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 19F/10P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.89, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.41 (weak), ret=+1.9%
  - 2020: S=-0.71 (negative), ret=-6.3%
  - 2021: S=1.92 (strong), ret=+20.7%
  - 2022: S=2.23 (strong), ret=+27.5%
  - 2023: S=-0.46 (negative), ret=-3.2%

## Risk & Drawdown
- Max drawdown: 11.30% over 487 days (recovered)
- Annualized: return +8.3%, volatility 9.3% (fraction of booksize)
- Hit rate: 50.4% positive days
- Tail shape: skew +0.15, excess kurtosis +1.44

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.11, max 3.00, latest -0.60

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +8.80%; worst month: -4.34%
Positive months: 59%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.75
- Sideways: S=0.34
- Bear: S=-2.02

## Negated Direction
Best negated: `rank(-1 * ts_delta(anl4_qf_az_eps, 5))` S=0.16, F=0.03, INFERIOR
Direction gap: -0.74 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * anl4_qf_az_eps)`: S=-0.08, F=-0.02, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * anl4_qf_az_eps / close)`: S=-0.14, F=-0.05, T=3.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_qf_az_eps, 5))`: S=0.16, F=0.03, T=36.9%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_qf_az_eps / close)` | TOP3000 | 0.89 | 0.74 | 11.3% | 60% | bull-only |
| `rank(anl4_qf_az_eps)` | TOP3000 | 0.39 | 0.25 | 37.5% | 60% | bull-only |
| `rank(anl4_qf_az_eps / close)` | TOP1000 | 0.35 | 0.21 | 22.6% | 60% | bull-only |
| `rank(ts_delta(anl4_qf_az_eps, 5))` | TOP1000 | 0.42 | 0.09 | 7.7% | 60% | mixed |
| `rank(anl4_qf_az_eps)` | TOP1000 | 0.15 | 0.06 | 38.1% | 60% | bull-only |
| `rank(anl4_qf_az_eps / close)` | TOP500 | 0.12 | 0.05 | 30.7% | 60% | bull-only |
| `rank(ts_delta(anl4_qf_az_eps, 5))` | TOP3000 | 0.24 | 0.03 | 8.7% | 80% | bull-only |
| `rank(anl4_qf_az_eps)` | TOP500 | 0.08 | 0.02 | 36.0% | 60% | bull-only |

## Correlation Notes
Top correlates:
- anl4_qfd1_azeps: 1.000 (strongly positively correlated)
- earnings_per_share_average: 1.000 (strongly positively correlated)
- anl4_qf_az_eps_mean: 1.000 (strongly positively correlated)
- anl4_qfd1_az_wol_spe: 0.987 (strongly positively correlated)
- anl4_qf_az_wol_spe: 0.987 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| rp_ess_revenue | news18 | -0.34 | 1.54 | +0.65 | -0.77 | yes |
| anl4_rd_exp_flag | analyst4 | -0.45 | 1.82 | +0.80 | -0.69 | no |
| news_open_vol | news12 | -0.36 | 1.56 | +0.64 | -0.52 | yes |
| fnd6_txtubadjust | fundamental6 | -0.33 | 1.50 | +0.61 | -0.59 | yes |
| sharesout | pv1 | -0.20 | 1.52 | +0.48 | -0.86 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
