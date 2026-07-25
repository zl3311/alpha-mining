---
field: earnings_per_share_average
dataset: analyst4
best_template: rank_value_norm
best_sharpe: 0.9
best_fitness: 0.74
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 6
max_drawdown: 0.1164
ann_vol: 0.0942
hit_rate: 0.5053
rolling_sharpe_min: -1.12
rolling_sharpe_max: 3.007
top_merge_partner: rp_ess_revenue
redundancy_cluster: 1
negated_best_sharpe: 0.4
negated_best_template: rank_neg_delta
negated_best_fitness: 0.11
n_negated_sims: 10
direction_gap: -0.5
---
# earnings_per_share_average (analyst4)

*Earnings per share - mean of estimations*

## Signal Profile
- `rank(earnings_per_share_average)`: S=0.40, F=0.25, T=1.2%, INFERIOR (TOP3000)
- `rank(earnings_per_share_average / close)`: S=0.90, F=0.74, T=2.2%, INFERIOR (TOP3000)
- `rank(ts_delta(earnings_per_share_average, 5))`: S=0.22, F=0.03, T=35.7%, INFERIOR (TOP1000)
- `-rank(earnings_per_share_average)`: S=-0.14, F=-0.05, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(earnings_per_share_average, 5))`: S=0.40, F=0.11, T=36.2%, INFERIOR (TOP3000)
- `ts_zscore(earnings_per_share_average, 22)`: S=0.09, F=0.01, T=32.5%, INFERIOR (TOP3000)
- `ts_mean(earnings_per_share_average, 10)`: S=-0.10, F=-0.03, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_rank(earnings_per_share_average, 22))`: S=0.08, F=0.01, T=15.2%, INFERIOR (TOP3000)
- `rank(-1 * earnings_per_share_average)`: S=-0.01, F=0.00, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * earnings_per_share_average / close)`: S=0.04, F=0.01, T=3.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 1F/31P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/7P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.89, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.35 (weak), ret=+1.7%
  - 2020: S=-0.74 (negative), ret=-6.5%
  - 2021: S=1.93 (strong), ret=+20.9%
  - 2022: S=2.24 (strong), ret=+27.8%
  - 2023: S=-0.43 (negative), ret=-3.1%

## Risk & Drawdown
- Max drawdown: 11.64% over 487 days (recovered)
- Annualized: return +8.3%, volatility 9.4% (fraction of booksize)
- Hit rate: 50.5% positive days
- Tail shape: skew +0.15, excess kurtosis +1.44

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.12, max 3.01, latest -0.57

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +8.88%; worst month: -4.30%
Positive months: 59%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.75
- Sideways: S=0.34
- Bear: S=-2.01

## Negated Direction
Best negated: `rank(-1 * ts_delta(earnings_per_share_average, 5))` S=0.40, F=0.11, INFERIOR
Direction gap: -0.50 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * earnings_per_share_average)`: S=-0.01, F=0.00, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * earnings_per_share_average / close)`: S=0.04, F=0.01, T=3.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(earnings_per_share_average, 5))`: S=0.40, F=0.11, T=36.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(earnings_per_share_average / close)` | TOP3000 | 0.89 | 0.74 | 11.6% | 60% | bull-only |
| `rank(earnings_per_share_average / close)` | TOP1000 | 0.31 | 0.18 | 23.2% | 60% | bull-only |
| `rank(earnings_per_share_average)` | TOP1000 | 0.13 | 0.05 | 38.6% | 60% | bull-only |
| `rank(earnings_per_share_average / close)` | TOP500 | 0.12 | 0.05 | 31.4% | 60% | bull-only |
| `rank(ts_delta(earnings_per_share_average, 5))` | TOP1000 | 0.22 | 0.03 | 11.7% | 60% | bull-only |
| `rank(earnings_per_share_average)` | TOP500 | 0.07 | 0.02 | 36.5% | 60% | bull-only |

## Correlation Notes
Top correlates:
- anl4_qf_az_eps_mean: 1.000 (strongly positively correlated)
- anl4_qfd1_azeps: 1.000 (strongly positively correlated)
- anl4_qf_az_eps: 1.000 (strongly positively correlated)
- anl4_qfd1_az_wol_spe: 0.988 (strongly positively correlated)
- anl4_qf_az_wol_spe: 0.988 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| rp_ess_revenue | news18 | -0.33 | 1.54 | +0.65 | -0.78 | yes |
| anl4_rd_exp_flag | analyst4 | -0.45 | 1.82 | +0.80 | -0.69 | no |
| news_open_vol | news12 | -0.36 | 1.56 | +0.64 | -0.53 | yes |
| fnd6_txtubadjust | fundamental6 | -0.33 | 1.49 | +0.61 | -0.61 | yes |
| sharesout | pv1 | -0.20 | 1.52 | +0.48 | -0.86 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
