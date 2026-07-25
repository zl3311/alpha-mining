---
field: anl4_qf_az_wol_spe
dataset: analyst4
best_template: rank_value_norm
best_sharpe: 0.81
best_fitness: 0.64
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 7
max_drawdown: 0.1416
ann_vol: 0.0957
hit_rate: 0.5012
rolling_sharpe_min: -1.335
rolling_sharpe_max: 2.915
top_merge_partner: anl4_rd_exp_flag
redundancy_cluster: 13
negated_best_sharpe: 0.13
negated_best_template: rank_neg_delta
negated_best_fitness: 0.02
n_negated_sims: 10
direction_gap: -0.68
---
# anl4_qf_az_wol_spe (analyst4)

*Earnings per share - The lowest estimation*

## Signal Profile
- `rank(anl4_qf_az_wol_spe)`: S=0.38, F=0.23, T=1.3%, INFERIOR (TOP3000)
- `rank(anl4_qf_az_wol_spe / close)`: S=0.81, F=0.64, T=2.3%, INFERIOR (TOP3000)
- `rank(ts_delta(anl4_qf_az_wol_spe, 5))`: S=0.49, F=0.17, T=35.9%, INFERIOR (TOP200)
- `-rank(anl4_qf_az_wol_spe)`: S=-0.16, F=-0.06, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_qf_az_wol_spe, 5))`: S=0.13, F=0.02, T=37.2%, INFERIOR (TOP3000)
- `ts_zscore(anl4_qf_az_wol_spe, 22)`: S=0.25, F=0.05, T=34.8%, INFERIOR (TOP3000)
- `ts_mean(anl4_qf_az_wol_spe, 10)`: S=-0.11, F=-0.03, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_qf_az_wol_spe, 22))`: S=-0.11, F=-0.02, T=14.0%, INFERIOR (TOP3000)
- `rank(-1 * anl4_qf_az_wol_spe)`: S=-0.06, F=-0.01, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * anl4_qf_az_wol_spe / close)`: S=-0.03, F=-0.01, T=3.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 2F/30P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 19F/10P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.80, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.33 (weak), ret=+1.4%
  - 2020: S=-0.94 (negative), ret=-7.5%
  - 2021: S=1.76 (strong), ret=+19.6%
  - 2022: S=2.13 (strong), ret=+28.1%
  - 2023: S=-0.51 (negative), ret=-3.9%

## Risk & Drawdown
- Max drawdown: 14.16% over 529 days (recovered)
- Annualized: return +7.7%, volatility 9.6% (fraction of booksize)
- Hit rate: 50.1% positive days
- Tail shape: skew +0.08, excess kurtosis +1.57

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.33, max 2.92, latest -0.67

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +9.00%; worst month: -3.68%
Positive months: 56%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.55
- Sideways: S=0.51
- Bear: S=-2.30

## Negated Direction
Best negated: `rank(-1 * ts_delta(anl4_qf_az_wol_spe, 5))` S=0.13, F=0.02, INFERIOR
Direction gap: -0.68 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * anl4_qf_az_wol_spe)`: S=-0.06, F=-0.01, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * anl4_qf_az_wol_spe / close)`: S=-0.03, F=-0.01, T=3.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_qf_az_wol_spe, 5))`: S=0.13, F=0.02, T=37.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_qf_az_wol_spe / close)` | TOP3000 | 0.80 | 0.64 | 14.2% | 60% | bull-only |
| `rank(anl4_qf_az_wol_spe)` | TOP3000 | 0.37 | 0.23 | 37.8% | 60% | bull-only |
| `rank(ts_delta(anl4_qf_az_wol_spe, 5))` | TOP200 | 0.48 | 0.17 | 19.9% | 60% | mixed |
| `rank(anl4_qf_az_wol_spe / close)` | TOP1000 | 0.20 | 0.10 | 25.2% | 60% | bull-only |
| `rank(anl4_qf_az_wol_spe)` | TOP1000 | 0.15 | 0.06 | 38.1% | 60% | bull-only |
| `rank(ts_delta(anl4_qf_az_wol_spe, 5))` | TOP1000 | 0.23 | 0.04 | 9.4% | 60% | weak |
| `rank(ts_delta(anl4_qf_az_wol_spe, 5))` | TOP3000 | 0.24 | 0.04 | 6.7% | 60% | weak |

## Correlation Notes
Top correlates:
- anl4_qfd1_az_wol_spe: 1.000 (strongly positively correlated)
- earnings_per_share_average: 0.988 (strongly positively correlated)
- anl4_qf_az_eps_mean: 0.988 (strongly positively correlated)
- anl4_qfd1_azeps: 0.987 (strongly positively correlated)
- anl4_qf_az_eps: 0.987 (strongly positively correlated)

Redundancy cluster #13: 127 similar fields, mean |rho| 0.82 (representative: anl4_bvps_flag). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_rd_exp_flag | analyst4 | -0.47 | 1.79 | +0.76 | -0.73 | no |
| news_open_vol | news12 | -0.41 | 1.53 | +0.60 | -0.49 | yes |
| fnd6_txtubadjust | fundamental6 | -0.36 | 1.44 | +0.59 | -0.61 | yes |
| rp_ess_revenue | news18 | -0.32 | 1.45 | +0.56 | -0.78 | yes |
| max_adjusted_net_profit_guidance | analyst4 | -0.35 | 1.42 | +0.61 | -0.79 | no |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
