---
field: anl4_epsr_high
dataset: analyst4
best_template: rank_value_norm
best_sharpe: 0.84
best_fitness: 0.67
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 6
max_drawdown: 0.1557
ann_vol: 0.0947
hit_rate: 0.5101
rolling_sharpe_min: -1.445
rolling_sharpe_max: 3.045
top_merge_partner: fnd6_txtubadjust
redundancy_cluster: 13
negated_best_sharpe: 0.53
negated_best_template: rank_neg_delta
negated_best_fitness: 0.16
n_negated_sims: 10
direction_gap: -0.31
---
# anl4_epsr_high (analyst4)

*GAAP Earnings per share - The highest estimation*

## Signal Profile
- `rank(anl4_epsr_high)`: S=0.40, F=0.25, T=1.2%, INFERIOR (TOP3000)
- `rank(anl4_epsr_high / close)`: S=0.84, F=0.67, T=2.3%, INFERIOR (TOP3000)
- `rank(ts_delta(anl4_epsr_high, 5))`: S=-0.03, F=0.00, T=37.0%, INFERIOR (TOP1000)
- `-rank(anl4_epsr_high)`: S=-0.23, F=-0.11, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_epsr_high, 5))`: S=0.53, F=0.16, T=37.2%, INFERIOR (TOP3000)
- `ts_zscore(anl4_epsr_high, 22)`: S=0.27, F=0.06, T=35.0%, INFERIOR (TOP3000)
- `ts_mean(anl4_epsr_high, 10)`: S=0.02, F=0.00, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_epsr_high, 22))`: S=0.11, F=0.02, T=13.9%, INFERIOR (TOP3000)
- `rank(-1 * anl4_epsr_high)`: S=-0.14, F=-0.05, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * anl4_epsr_high / close)`: S=-0.16, F=-0.06, T=3.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 2F/30P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 19F/10P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.82, Consistency 40% positive years (2/5)
Yearly breakdown:
  - 2019: S=-0.18 (negative), ret=-0.8%
  - 2020: S=-1.09 (negative), ret=-8.3%
  - 2021: S=1.97 (strong), ret=+21.4%
  - 2022: S=2.22 (strong), ret=+28.3%
  - 2023: S=-0.31 (negative), ret=-2.6%

## Risk & Drawdown
- Max drawdown: 15.57% over 748 days (recovered)
- Annualized: return +7.8%, volatility 9.5% (fraction of booksize)
- Hit rate: 51.0% positive days
- Tail shape: skew +0.07, excess kurtosis +1.11

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.45, max 3.04, latest -0.48

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +8.26%; worst month: -4.91%
Positive months: 56%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.64
- Sideways: S=0.18
- Bear: S=-2.04

## Negated Direction
Best negated: `rank(-1 * ts_delta(anl4_epsr_high, 5))` S=0.53, F=0.16, INFERIOR
Direction gap: -0.31 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * anl4_epsr_high)`: S=-0.14, F=-0.05, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * anl4_epsr_high / close)`: S=-0.16, F=-0.06, T=3.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_epsr_high, 5))`: S=0.53, F=0.16, T=37.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_epsr_high / close)` | TOP3000 | 0.82 | 0.67 | 15.6% | 40% | bull-only |
| `rank(anl4_epsr_high)` | TOP3000 | 0.39 | 0.25 | 38.3% | 60% | bull-only |
| `rank(anl4_epsr_high / close)` | TOP1000 | 0.29 | 0.17 | 24.7% | 60% | bull-only |
| `rank(anl4_epsr_high)` | TOP1000 | 0.22 | 0.11 | 36.5% | 60% | bull-only |
| `rank(anl4_epsr_high / close)` | TOP500 | 0.14 | 0.06 | 30.5% | 60% | bull-only |
| `rank(anl4_epsr_high)` | TOP500 | 0.13 | 0.05 | 35.3% | 60% | bull-only |

## Correlation Notes
Top correlates:
- anl4_median_epsreported: 0.992 (strongly positively correlated)
- anl4_epsr_mean: 0.992 (strongly positively correlated)
- est_epsr: 0.988 (strongly positively correlated)
- anl4_epsr_low: 0.969 (strongly positively correlated)
- anl4_qfd1_az_wol_spe: 0.966 (strongly positively correlated)

Redundancy cluster #13: 127 similar fields, mean |rho| 0.82 (representative: anl4_bvps_flag). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| fnd6_txtubadjust | fundamental6 | -0.36 | 1.46 | +0.61 | -0.70 | yes |
| news_open_vol | news12 | -0.39 | 1.53 | +0.61 | -0.62 | yes |
| anl4_rd_exp_flag | analyst4 | -0.44 | 1.75 | +0.72 | -0.67 | no |
| rp_ess_revenue | news18 | -0.30 | 1.45 | +0.56 | -0.80 | yes |
| max_adjusted_net_profit_guidance | analyst4 | -0.34 | 1.42 | +0.60 | -0.78 | no |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
