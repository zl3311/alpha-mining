---
field: fnd6_mfma1_dpc
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 0.95
best_fitness: 0.75
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 7
max_drawdown: 0.1022
ann_vol: 0.0819
hit_rate: 0.481
rolling_sharpe_min: -1.129
rolling_sharpe_max: 2.797
top_merge_partner: anl4_epsr_flag
redundancy_cluster: 1
negated_best_sharpe: 0.36
negated_best_template: rank_neg_delta
negated_best_fitness: 0.18
n_negated_sims: 10
direction_gap: -0.59
---
# fnd6_mfma1_dpc (fundamental6)

*Depreciation and Amortization (Cash Flow)*

## Signal Profile
- `rank(fnd6_mfma1_dpc)`: S=0.67, F=0.52, T=1.3%, INFERIOR (TOP3000)
- `rank(fnd6_mfma1_dpc / close)`: S=0.95, F=0.75, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_mfma1_dpc, 5))`: S=0.17, F=0.05, T=34.6%, INFERIOR (TOP1000)
- `-rank(fnd6_mfma1_dpc)`: S=-0.32, F=-0.18, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_mfma1_dpc, 5))`: S=0.36, F=0.18, T=32.2%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_mfma1_dpc, 22)`: S=0.43, F=0.26, T=26.8%, INFERIOR (TOP3000)
- `ts_mean(fnd6_mfma1_dpc, 10)`: S=-0.13, F=-0.04, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_mfma1_dpc, 22))`: S=-0.03, F=0.00, T=15.6%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_mfma1_dpc)`: S=0.19, F=0.10, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_mfma1_dpc / close)`: S=0.06, F=0.02, T=2.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 11F/9P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.95, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=-0.16 (negative), ret=-0.8%
  - 2020: S=0.45 (weak), ret=+4.4%
  - 2021: S=1.79 (strong), ret=+18.8%
  - 2022: S=1.45 (moderate), ret=+11.7%
  - 2023: S=0.75 (moderate), ret=+3.9%

## Risk & Drawdown
- Max drawdown: 10.22% over 439 days (recovered)
- Annualized: return +7.8%, volatility 8.2% (fraction of booksize)
- Hit rate: 48.1% positive days
- Tail shape: skew +0.59, excess kurtosis +3.60

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.13, max 2.80, latest 0.80

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2019
Best month: +9.47%; worst month: -3.79%
Positive months: 56%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.00
- Sideways: S=0.21
- Bear: S=-0.91

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_mfma1_dpc, 5))` S=0.36, F=0.18, INFERIOR
Direction gap: -0.59 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_mfma1_dpc)`: S=0.19, F=0.10, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_mfma1_dpc / close)`: S=0.06, F=0.02, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_mfma1_dpc, 5))`: S=0.36, F=0.18, T=32.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_mfma1_dpc / close)` | TOP3000 | 0.95 | 0.75 | 10.2% | 80% | bull-only |
| `rank(fnd6_mfma1_dpc)` | TOP3000 | 0.67 | 0.52 | 27.2% | 80% | bull-only |
| `rank(fnd6_mfma1_dpc / close)` | TOP1000 | 0.50 | 0.32 | 13.1% | 40% | bull-only |
| `rank(fnd6_mfma1_dpc)` | TOP1000 | 0.31 | 0.18 | 32.6% | 60% | bull-only |
| `rank(fnd6_mfma1_dpc / close)` | TOP500 | 0.29 | 0.15 | 24.6% | 40% | bull-only |
| `rank(ts_delta(fnd6_mfma1_dpc, 5))` | TOP1000 | 0.18 | 0.05 | 47.2% | 60% | weak |
| `rank(fnd6_mfma1_dpc)` | TOP500 | 0.09 | 0.03 | 44.3% | 40% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_newa1v1300_dpc: 1.000 (strongly positively correlated)
- fnd6_mfma1_dp: 0.991 (strongly positively correlated)
- fnd6_newa1v1300_dp: 0.991 (strongly positively correlated)
- fnd6_newa1v1300_lt: 0.981 (strongly positively correlated)
- fnd6_cptmfmq_dpq: 0.980 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_epsr_flag | analyst4 | -0.35 | 1.87 | +0.69 | -0.60 | yes |
| rp_ess_revenue | news18 | -0.37 | 1.61 | +0.67 | -0.67 | yes |
| anl4_rd_exp_flag | analyst4 | -0.30 | 1.65 | +0.63 | -0.21 | yes |
| net_profit_adjusted_min_guidance | analyst4 | -0.22 | 1.51 | +0.56 | -0.59 | yes |
| max_gross_income_guidance_2 | analyst4 | -0.31 | 1.46 | +0.52 | -0.95 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
