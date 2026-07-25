---
field: anl4_fcfps_flag
dataset: analyst4
best_template: rank_level
best_sharpe: 0.82
best_fitness: 0.56
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 7
max_drawdown: 0.1181
ann_vol: 0.0701
hit_rate: 0.5061
rolling_sharpe_min: -1.043
rolling_sharpe_max: 3.056
top_merge_partner: rank(scl12_buzz * (-1 * returns))
redundancy_cluster: 18
negated_best_sharpe: 0.53
negated_best_template: rank_neg_delta
negated_best_fitness: 0.38
n_negated_sims: 10
direction_gap: -0.29
---
# anl4_fcfps_flag (analyst4)

*Free cash flow per share - forecast type (revision/new/...)*

## Signal Profile
- `rank(anl4_fcfps_flag)`: S=0.82, F=0.56, T=2.2%, INFERIOR (TOP3000)
- `rank(anl4_fcfps_flag / close)`: S=0.28, F=0.14, T=3.2%, INFERIOR (TOP200)
- `rank(ts_delta(anl4_fcfps_flag, 5))`: S=0.33, F=0.26, T=21.2%, INFERIOR (TOP1000)
- `-rank(anl4_fcfps_flag)`: S=-0.39, F=-0.23, T=3.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_fcfps_flag, 5))`: S=0.53, F=0.38, T=31.4%, INFERIOR (TOP3000)
- `-ts_zscore(anl4_fcfps_flag, 63)`: S=-0.14, F=-0.11, T=6.4%, INFERIOR (TOP3000)
- `ts_mean(anl4_fcfps_flag, 10)`: S=0.39, F=0.23, T=3.0%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_fcfps_flag, 22))`: S=-0.26, F=-0.21, T=16.4%, INFERIOR (TOP3000)
- `rank(-1 * anl4_fcfps_flag)`: S=-0.82, F=-0.56, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * anl4_fcfps_flag / close)`: S=0.06, F=0.01, T=2.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 13F/19P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 18F/11P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.81, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.97 (moderate), ret=+3.6%
  - 2020: S=0.18 (weak), ret=+0.9%
  - 2021: S=1.59 (strong), ret=+16.1%
  - 2022: S=1.25 (moderate), ret=+10.6%
  - 2023: S=-0.67 (negative), ret=-3.4%

## Risk & Drawdown
- Max drawdown: 11.81% over 210 days (recovered)
- Annualized: return +5.7%, volatility 7.0% (fraction of booksize)
- Hit rate: 50.6% positive days
- Tail shape: skew -0.06, excess kurtosis +4.46

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.04, max 3.06, latest -0.70

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2023
Best month: +6.71%; worst month: -2.53%
Positive months: 59%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=1.85
- Sideways: S=0.68
- Bear: S=-0.57

## Negated Direction
Best negated: `rank(-1 * ts_delta(anl4_fcfps_flag, 5))` S=0.53, F=0.38, INFERIOR
Direction gap: -0.29 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * anl4_fcfps_flag)`: S=-0.82, F=-0.56, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * anl4_fcfps_flag / close)`: S=0.06, F=0.01, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_fcfps_flag, 5))`: S=0.53, F=0.38, T=31.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_fcfps_flag)` | TOP3000 | 0.81 | 0.56 | 11.8% | 80% | bull-only |
| `rank(ts_delta(anl4_fcfps_flag, 5))` | TOP1000 | 0.33 | 0.26 | 99.6% | 60% | mixed |
| `rank(anl4_fcfps_flag)` | TOP1000 | 0.39 | 0.23 | 14.5% | 60% | bull-only |
| `rank(ts_delta(anl4_fcfps_flag, 5))` | TOP200 | 0.25 | 0.19 | 48.0% | 60% | bull-only |
| `rank(anl4_fcfps_flag / close)` | TOP200 | 0.28 | 0.14 | 27.3% | 40% | mixed |
| `rank(ts_delta(anl4_fcfps_flag, 5))` | TOP500 | 0.15 | 0.08 | 52.5% | 80% | weak |
| `rank(anl4_fcfps_flag)` | TOP500 | 0.15 | 0.08 | 35.1% | 40% | bull-only |

## Correlation Notes
Top correlates:
- anl4_tot_gw_ft: 0.862 (strongly positively correlated)
- anl4_fcf_flag: 0.841 (strongly positively correlated)
- anl4_totassets_flag: 0.809 (strongly positively correlated)
- anl4_ptpr_flag: 0.806 (strongly positively correlated)
- anl4_cff_flag: 0.798 (strongly positively correlated)

Redundancy cluster #18: 7 similar fields, mean |rho| 0.818 (representative: anl4_totassets_flag). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| rank(scl12_buzz * (-1 * returns)) | socialmedia12 | -0.30 | 2.11 | +0.48 | -0.91 | yes |
| anl4_afv4_dts_spe | analyst4 | -0.40 | 1.62 | +0.63 | -0.73 | no |
| rank(fnd6_acdo) + rank(open/close - 1) | unknown | -0.30 | 2.50 | +0.47 | -0.72 | yes |
| rank(fnd6_acdo) * rank(-1 * returns) | unknown | -0.27 | 2.32 | +0.45 | -0.72 | yes |
| fnd2_a_sbcpnargmpmtwopsffesip | fundamental2 | -0.19 | 1.30 | +0.44 | -0.65 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
