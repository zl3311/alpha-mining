---
field: anl4_qf_az_hgih_spe
dataset: analyst4
best_template: rank_value_norm
best_sharpe: 1.01
best_fitness: 0.85
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 6
max_drawdown: 0.0975
ann_vol: 0.0877
hit_rate: 0.515
rolling_sharpe_min: -1.256
rolling_sharpe_max: 3.146
top_merge_partner: anl4_rd_exp_flag
redundancy_cluster: 1
negated_best_sharpe: 0.58
negated_best_template: rank_neg_delta
negated_best_fitness: 0.18
n_negated_sims: 10
direction_gap: -0.43
---
# anl4_qf_az_hgih_spe (analyst4)

*Earnings per share - The highest estimation*

## Signal Profile
- `rank(anl4_qf_az_hgih_spe)`: S=0.44, F=0.28, T=1.2%, INFERIOR (TOP3000)
- `rank(anl4_qf_az_hgih_spe / close)`: S=1.01, F=0.85, T=2.3%, INFERIOR (TOP3000)
- `rank(ts_delta(anl4_qf_az_hgih_spe, 5))`: S=0.39, F=0.09, T=36.9%, INFERIOR (TOP1000)
- `-rank(anl4_qf_az_hgih_spe)`: S=-0.18, F=-0.07, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_qf_az_hgih_spe, 5))`: S=0.58, F=0.18, T=37.1%, INFERIOR (TOP3000)
- `ts_zscore(anl4_qf_az_hgih_spe, 22)`: S=0.43, F=0.12, T=35.0%, INFERIOR (TOP3000)
- `ts_mean(anl4_qf_az_hgih_spe, 10)`: S=-0.09, F=-0.02, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_qf_az_hgih_spe, 22))`: S=0.55, F=0.21, T=13.9%, INFERIOR (TOP3000)
- `rank(-1 * anl4_qf_az_hgih_spe)`: S=-0.06, F=-0.01, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * anl4_qf_az_hgih_spe / close)`: S=-0.16, F=-0.06, T=3.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 2F/30P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 20F/9P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 1.00, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.26 (weak), ret=+1.3%
  - 2020: S=-0.54 (negative), ret=-4.9%
  - 2021: S=2.11 (strong), ret=+21.4%
  - 2022: S=2.52 (strong), ret=+27.1%
  - 2023: S=-0.31 (negative), ret=-1.9%

## Risk & Drawdown
- Max drawdown: 9.75% over 765 days (recovered)
- Annualized: return +8.8%, volatility 8.8% (fraction of booksize)
- Hit rate: 51.5% positive days
- Tail shape: skew +0.24, excess kurtosis +1.34

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.26, max 3.15, latest -0.44

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +8.46%; worst month: -3.98%
Positive months: 58%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.88
- Sideways: S=0.17
- Bear: S=-1.63

## Negated Direction
Best negated: `rank(-1 * ts_delta(anl4_qf_az_hgih_spe, 5))` S=0.58, F=0.18, INFERIOR
Direction gap: -0.43 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * anl4_qf_az_hgih_spe)`: S=-0.06, F=-0.01, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * anl4_qf_az_hgih_spe / close)`: S=-0.16, F=-0.06, T=3.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_qf_az_hgih_spe, 5))`: S=0.58, F=0.18, T=37.1%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_qf_az_hgih_spe / close)` | TOP3000 | 1.00 | 0.85 | 9.8% | 60% | bull-only |
| `rank(anl4_qf_az_hgih_spe / close)` | TOP1000 | 0.39 | 0.24 | 22.7% | 60% | bull-only |
| `rank(ts_delta(anl4_qf_az_hgih_spe, 5))` | TOP1000 | 0.40 | 0.09 | 6.9% | 60% | mixed |
| `rank(anl4_qf_az_hgih_spe)` | TOP1000 | 0.17 | 0.07 | 38.1% | 60% | bull-only |
| `rank(anl4_qf_az_hgih_spe / close)` | TOP500 | 0.14 | 0.06 | 30.4% | 60% | bull-only |
| `rank(ts_delta(anl4_qf_az_hgih_spe, 5))` | TOP3000 | 0.23 | 0.03 | 8.3% | 60% | mixed |

## Correlation Notes
Top correlates:
- anl4_qfd1_az_hgih_spe: 1.000 (strongly positively correlated)
- anl4_qfd1_azeps: 0.987 (strongly positively correlated)
- anl4_qf_az_eps: 0.987 (strongly positively correlated)
- earnings_per_share_average: 0.986 (strongly positively correlated)
- anl4_qf_az_eps_mean: 0.986 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_rd_exp_flag | analyst4 | -0.42 | 1.87 | +0.84 | -0.64 | no |
| rp_ess_revenue | news18 | -0.35 | 1.64 | +0.64 | -0.75 | yes |
| news_open_vol | news12 | -0.30 | 1.61 | +0.61 | -0.57 | yes |
| fnd6_txtubadjust | fundamental6 | -0.31 | 1.57 | +0.57 | -0.64 | yes |
| sharesout | pv1 | -0.17 | 1.56 | +0.53 | -0.87 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
