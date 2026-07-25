---
field: fnd6_mfma1_dp
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 0.86
best_fitness: 0.66
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 9
max_drawdown: 0.1116
ann_vol: 0.0849
hit_rate: 0.4761
rolling_sharpe_min: -1.136
rolling_sharpe_max: 2.644
top_merge_partner: rp_ess_revenue
redundancy_cluster: 1
negated_best_sharpe: 0.21
negated_best_template: rank_neg_delta
negated_best_fitness: 0.07
n_negated_sims: 10
direction_gap: -0.65
---
# fnd6_mfma1_dp (fundamental6)

*Depreciation and Amortization*

## Signal Profile
- `rank(fnd6_mfma1_dp)`: S=0.62, F=0.48, T=1.1%, INFERIOR (TOP3000)
- `rank(fnd6_mfma1_dp / close)`: S=0.86, F=0.66, T=1.5%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_mfma1_dp, 5))`: S=0.60, F=0.28, T=34.2%, INFERIOR (TOP1000)
- `-rank(fnd6_mfma1_dp)`: S=-0.28, F=-0.16, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_mfma1_dp, 5))`: S=0.21, F=0.07, T=34.1%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_mfma1_dp, 63)`: S=0.25, F=0.10, T=18.9%, INFERIOR (TOP3000)
- `ts_mean(fnd6_mfma1_dp, 10)`: S=-0.02, F=0.00, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_mfma1_dp, 22))`: S=0.10, F=0.02, T=15.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_mfma1_dp)`: S=0.14, F=0.06, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_mfma1_dp / close)`: S=0.04, F=0.01, T=2.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/6P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.86, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=-0.23 (negative), ret=-1.2%
  - 2020: S=0.21 (weak), ret=+1.9%
  - 2021: S=1.63 (strong), ret=+18.6%
  - 2022: S=1.32 (moderate), ret=+11.6%
  - 2023: S=0.92 (moderate), ret=+4.8%

## Risk & Drawdown
- Max drawdown: 11.16% over 441 days (recovered)
- Annualized: return +7.3%, volatility 8.5% (fraction of booksize)
- Hit rate: 47.6% positive days
- Tail shape: skew +0.47, excess kurtosis +3.18

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.14, max 2.64, latest 0.97

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2019
Best month: +9.69%; worst month: -4.08%
Positive months: 49%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.03
- Sideways: S=0.12
- Bear: S=-1.23

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_mfma1_dp, 5))` S=0.21, F=0.07, INFERIOR
Direction gap: -0.65 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_mfma1_dp)`: S=0.14, F=0.06, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_mfma1_dp / close)`: S=0.04, F=0.01, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_mfma1_dp, 5))`: S=0.21, F=0.07, T=34.1%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_mfma1_dp / close)` | TOP3000 | 0.86 | 0.66 | 11.2% | 80% | bull-only |
| `rank(fnd6_mfma1_dp)` | TOP3000 | 0.61 | 0.48 | 30.6% | 80% | bull-only |
| `rank(ts_delta(fnd6_mfma1_dp, 5))` | TOP1000 | 0.61 | 0.28 | 12.2% | 100% | all-weather |
| `rank(fnd6_mfma1_dp / close)` | TOP1000 | 0.43 | 0.27 | 14.9% | 40% | bull-only |
| `rank(fnd6_mfma1_dp / close)` | TOP500 | 0.31 | 0.17 | 26.0% | 80% | bull-only |
| `rank(fnd6_mfma1_dp)` | TOP1000 | 0.27 | 0.16 | 35.5% | 60% | bull-only |
| `rank(ts_delta(fnd6_mfma1_dp, 5))` | TOP500 | 0.19 | 0.06 | 43.3% | 60% | mixed |
| `rank(fnd6_mfma1_dp)` | TOP500 | 0.08 | 0.03 | 46.4% | 60% | bull-only |
| `rank(ts_delta(fnd6_mfma1_dp, 5))` | TOP3000 | 0.13 | 0.02 | 21.0% | 80% | mixed |

## Correlation Notes
Top correlates:
- fnd6_newa1v1300_dp: 1.000 (strongly positively correlated)
- fnd6_mfma1_dpc: 0.991 (strongly positively correlated)
- fnd6_newa1v1300_dpc: 0.991 (strongly positively correlated)
- fnd6_newa2v1300_ppegt: 0.982 (strongly positively correlated)
- fnd6_ppeveb: 0.981 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| rp_ess_revenue | news18 | -0.37 | 1.55 | +0.66 | -0.70 | yes |
| anl4_epsr_flag | analyst4 | -0.34 | 1.78 | +0.60 | -0.54 | yes |
| max_gross_income_guidance_2 | analyst4 | -0.32 | 1.41 | +0.56 | -0.92 | yes |
| anl4_rd_exp_flag | analyst4 | -0.33 | 1.62 | +0.60 | -0.29 | yes |
| min_gross_income_guidance | analyst4 | -0.24 | 1.39 | +0.52 | -0.74 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
