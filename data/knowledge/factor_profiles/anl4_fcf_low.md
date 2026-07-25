---
field: anl4_fcf_low
dataset: analyst4
best_template: rank_value_norm
best_sharpe: 0.85
best_fitness: 0.64
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 4
max_drawdown: 0.135
ann_vol: 0.0828
hit_rate: 0.5109
rolling_sharpe_min: -2.05
rolling_sharpe_max: 3.023
top_merge_partner: anl4_rd_exp_flag
redundancy_cluster: 13
negated_best_sharpe: 0.47
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.31
n_negated_sims: 10
direction_gap: -0.38
---
# anl4_fcf_low (analyst4)

*Free Cash Flow - The lowest estimation*

## Signal Profile
- `rank(anl4_fcf_low)`: S=0.42, F=0.25, T=1.8%, INFERIOR (TOP3000)
- `rank(anl4_fcf_low / close)`: S=0.85, F=0.64, T=2.1%, INFERIOR (TOP3000)
- `rank(ts_delta(anl4_fcf_low, 5))`: S=-0.04, F=0.00, T=37.0%, INFERIOR (TOP500)
- `-rank(anl4_fcf_low)`: S=-0.23, F=-0.10, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_fcf_low, 5))`: S=0.44, F=0.16, T=34.8%, INFERIOR (TOP3000)
- `-ts_zscore(anl4_fcf_low, 63)`: S=0.15, F=0.03, T=17.0%, INFERIOR (TOP3000)
- `ts_mean(anl4_fcf_low, 10)`: S=-0.06, F=-0.02, T=1.8%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_fcf_low, 22))`: S=-0.08, F=-0.01, T=13.9%, INFERIOR (TOP3000)
- `rank(-1 * anl4_fcf_low)`: S=0.25, F=0.13, T=3.2%, INFERIOR (TOP3000)
- `rank(-1 * anl4_fcf_low / close)`: S=0.47, F=0.31, T=3.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 5F/27P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 15F/5P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.83, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.66 (moderate), ret=+2.5%
  - 2020: S=-1.71 (negative), ret=-9.9%
  - 2021: S=1.98 (strong), ret=+19.2%
  - 2022: S=1.67 (strong), ret=+19.9%
  - 2023: S=0.32 (weak), ret=+2.2%

## Risk & Drawdown
- Max drawdown: 13.50% over 539 days (recovered)
- Annualized: return +6.9%, volatility 8.3% (fraction of booksize)
- Hit rate: 51.1% positive days
- Tail shape: skew +0.04, excess kurtosis +1.75

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.05, max 3.02, latest 0.09

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2020
Best month: +7.60%; worst month: -2.72%
Positive months: 51%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.30
- Sideways: S=0.55
- Bear: S=-2.23

## Negated Direction
Best negated: `rank(-1 * anl4_fcf_low / close)` S=0.47, F=0.31, INFERIOR
Direction gap: -0.38 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * anl4_fcf_low)`: S=0.25, F=0.13, T=3.2%, INFERIOR (TOP3000)
- `rank(-1 * anl4_fcf_low / close)`: S=0.47, F=0.31, T=3.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_fcf_low, 5))`: S=0.44, F=0.16, T=34.8%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_fcf_low / close)` | TOP3000 | 0.83 | 0.64 | 13.5% | 80% | bull-only |
| `rank(anl4_fcf_low)` | TOP3000 | 0.41 | 0.25 | 31.4% | 60% | bull-only |
| `rank(anl4_fcf_low / close)` | TOP1000 | 0.31 | 0.16 | 20.4% | 40% | bull-only |
| `rank(anl4_fcf_low)` | TOP1000 | 0.22 | 0.10 | 32.0% | 60% | bull-only |

## Correlation Notes
Top correlates:
- anl4_fcf_median: 0.991 (strongly positively correlated)
- anl4_fcf_mean: 0.991 (strongly positively correlated)
- anl4_fcf_high: 0.972 (strongly positively correlated)
- est_fcf: 0.972 (strongly positively correlated)
- anl4_cfo_low: 0.944 (strongly positively correlated)

Redundancy cluster #13: 127 similar fields, mean |rho| 0.82 (representative: anl4_bvps_flag). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_rd_exp_flag | analyst4 | -0.47 | 1.80 | +0.78 | -0.86 | no |
| fnd6_txtubadjust | fundamental6 | -0.37 | 1.50 | +0.65 | -0.62 | yes |
| news_open_vol | news12 | -0.37 | 1.55 | +0.62 | -0.46 | yes |
| rp_ess_revenue | news18 | -0.29 | 1.44 | +0.55 | -0.92 | yes |
| rank(fnd6_acdo) * rank(-1 * returns) | unknown | -0.34 | 2.43 | +0.56 | -0.58 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
