---
field: fnd6_newa1v1300_dp
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 0.85
best_fitness: 0.65
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 8
max_drawdown: 0.1109
ann_vol: 0.0852
hit_rate: 0.4761
rolling_sharpe_min: -1.166
rolling_sharpe_max: 2.629
top_merge_partner: rp_ess_revenue
redundancy_cluster: 1
negated_best_sharpe: 0.15
negated_best_template: neg_rank_level
negated_best_fitness: 0.07
n_negated_sims: 10
direction_gap: -0.7
---
# fnd6_newa1v1300_dp (fundamental6)

*Depreciation and Amortization*

## Signal Profile
- `rank(fnd6_newa1v1300_dp)`: S=0.61, F=0.47, T=1.1%, INFERIOR (TOP3000)
- `rank(fnd6_newa1v1300_dp / close)`: S=0.85, F=0.65, T=1.5%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_newa1v1300_dp, 5))`: S=0.60, F=0.28, T=34.2%, INFERIOR (TOP1000)
- `-rank(fnd6_newa1v1300_dp)`: S=-0.28, F=-0.16, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa1v1300_dp, 5))`: S=0.21, F=0.07, T=34.0%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_newa1v1300_dp, 63)`: S=0.26, F=0.11, T=18.8%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newa1v1300_dp, 10)`: S=0.02, F=0.00, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newa1v1300_dp, 22))`: S=0.09, F=0.02, T=15.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_dp)`: S=0.15, F=0.07, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_dp / close)`: S=0.06, F=0.02, T=2.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 15F/5P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.84, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=-0.24 (negative), ret=-1.2%
  - 2020: S=0.18 (weak), ret=+1.7%
  - 2021: S=1.62 (strong), ret=+18.5%
  - 2022: S=1.32 (moderate), ret=+11.7%
  - 2023: S=0.90 (moderate), ret=+4.6%

## Risk & Drawdown
- Max drawdown: 11.09% over 441 days (recovered)
- Annualized: return +7.2%, volatility 8.5% (fraction of booksize)
- Hit rate: 47.6% positive days
- Tail shape: skew +0.47, excess kurtosis +3.18

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.17, max 2.63, latest 0.95

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2019
Best month: +9.72%; worst month: -4.11%
Positive months: 51%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.02
- Sideways: S=0.11
- Bear: S=-1.26

## Negated Direction
Best negated: `rank(-1 * fnd6_newa1v1300_dp)` S=0.15, F=0.07, INFERIOR
Direction gap: -0.70 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_newa1v1300_dp)`: S=0.15, F=0.07, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_dp / close)`: S=0.06, F=0.02, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa1v1300_dp, 5))`: S=0.21, F=0.07, T=34.0%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newa1v1300_dp / close)` | TOP3000 | 0.84 | 0.65 | 11.1% | 80% | bull-only |
| `rank(fnd6_newa1v1300_dp)` | TOP3000 | 0.61 | 0.47 | 31.0% | 80% | bull-only |
| `rank(ts_delta(fnd6_newa1v1300_dp, 5))` | TOP1000 | 0.60 | 0.28 | 12.1% | 100% | all-weather |
| `rank(fnd6_newa1v1300_dp / close)` | TOP1000 | 0.43 | 0.27 | 15.0% | 40% | bull-only |
| `rank(fnd6_newa1v1300_dp / close)` | TOP500 | 0.31 | 0.17 | 26.4% | 80% | bull-only |
| `rank(fnd6_newa1v1300_dp)` | TOP1000 | 0.28 | 0.16 | 35.7% | 60% | bull-only |
| `rank(ts_delta(fnd6_newa1v1300_dp, 5))` | TOP500 | 0.17 | 0.05 | 44.8% | 60% | mixed |
| `rank(fnd6_newa1v1300_dp)` | TOP500 | 0.08 | 0.03 | 46.5% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_mfma1_dp: 1.000 (strongly positively correlated)
- fnd6_newa1v1300_dpc: 0.991 (strongly positively correlated)
- fnd6_mfma1_dpc: 0.991 (strongly positively correlated)
- fnd6_newa2v1300_ppegt: 0.982 (strongly positively correlated)
- fnd6_ppeveb: 0.982 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| rp_ess_revenue | news18 | -0.37 | 1.54 | +0.65 | -0.70 | yes |
| max_gross_income_guidance_2 | analyst4 | -0.32 | 1.40 | +0.56 | -0.92 | yes |
| anl4_epsr_flag | analyst4 | -0.34 | 1.77 | +0.59 | -0.54 | yes |
| anl4_rd_exp_flag | analyst4 | -0.33 | 1.61 | +0.58 | -0.30 | yes |
| min_gross_income_guidance | analyst4 | -0.24 | 1.38 | +0.51 | -0.74 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
