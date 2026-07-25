---
field: fnd6_newa1v1300_dpc
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 0.94
best_fitness: 0.74
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 7
max_drawdown: 0.1011
ann_vol: 0.082
hit_rate: 0.4818
rolling_sharpe_min: -1.172
rolling_sharpe_max: 2.782
top_merge_partner: anl4_epsr_flag
redundancy_cluster: 1
negated_best_sharpe: 0.36
negated_best_template: rank_neg_delta
negated_best_fitness: 0.18
n_negated_sims: 10
direction_gap: -0.58
---
# fnd6_newa1v1300_dpc (fundamental6)

*Depreciation and Amortization (Cash Flow)*

## Signal Profile
- `rank(fnd6_newa1v1300_dpc)`: S=0.67, F=0.52, T=1.3%, INFERIOR (TOP3000)
- `rank(fnd6_newa1v1300_dpc / close)`: S=0.94, F=0.74, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_newa1v1300_dpc, 5))`: S=0.16, F=0.04, T=34.7%, INFERIOR (TOP1000)
- `-rank(fnd6_newa1v1300_dpc)`: S=-0.32, F=-0.19, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa1v1300_dpc, 5))`: S=0.36, F=0.18, T=32.3%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_newa1v1300_dpc, 22)`: S=0.44, F=0.27, T=26.8%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newa1v1300_dpc, 10)`: S=-0.09, F=-0.02, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newa1v1300_dpc, 22))`: S=-0.04, F=-0.01, T=15.6%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_dpc)`: S=0.20, F=0.10, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_dpc / close)`: S=0.07, F=0.02, T=2.5%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 10F/10P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.94, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=-0.18 (negative), ret=-0.9%
  - 2020: S=0.43 (weak), ret=+4.1%
  - 2021: S=1.77 (strong), ret=+18.7%
  - 2022: S=1.46 (moderate), ret=+11.8%
  - 2023: S=0.74 (moderate), ret=+3.9%

## Risk & Drawdown
- Max drawdown: 10.11% over 439 days (recovered)
- Annualized: return +7.7%, volatility 8.2% (fraction of booksize)
- Hit rate: 48.2% positive days
- Tail shape: skew +0.59, excess kurtosis +3.60

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.17, max 2.78, latest 0.79

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2019
Best month: +9.47%; worst month: -3.80%
Positive months: 56%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.00
- Sideways: S=0.20
- Bear: S=-0.94

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_newa1v1300_dpc, 5))` S=0.36, F=0.18, INFERIOR
Direction gap: -0.58 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_newa1v1300_dpc)`: S=0.20, F=0.10, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_dpc / close)`: S=0.07, F=0.02, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa1v1300_dpc, 5))`: S=0.36, F=0.18, T=32.3%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newa1v1300_dpc / close)` | TOP3000 | 0.94 | 0.74 | 10.1% | 80% | bull-only |
| `rank(fnd6_newa1v1300_dpc)` | TOP3000 | 0.67 | 0.52 | 27.7% | 80% | bull-only |
| `rank(fnd6_newa1v1300_dpc / close)` | TOP1000 | 0.50 | 0.33 | 13.1% | 40% | bull-only |
| `rank(fnd6_newa1v1300_dpc)` | TOP1000 | 0.31 | 0.19 | 32.8% | 60% | bull-only |
| `rank(fnd6_newa1v1300_dpc / close)` | TOP500 | 0.29 | 0.15 | 25.0% | 40% | bull-only |
| `rank(ts_delta(fnd6_newa1v1300_dpc, 5))` | TOP1000 | 0.17 | 0.04 | 48.5% | 60% | weak |
| `rank(fnd6_newa1v1300_dpc)` | TOP500 | 0.09 | 0.03 | 44.5% | 40% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_mfma1_dpc: 1.000 (strongly positively correlated)
- fnd6_newa1v1300_dp: 0.991 (strongly positively correlated)
- fnd6_mfma1_dp: 0.991 (strongly positively correlated)
- fnd6_newa1v1300_lt: 0.981 (strongly positively correlated)
- fnd6_cptmfmq_dpq: 0.980 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_epsr_flag | analyst4 | -0.35 | 1.86 | +0.69 | -0.60 | yes |
| rp_ess_revenue | news18 | -0.37 | 1.60 | +0.67 | -0.67 | yes |
| anl4_rd_exp_flag | analyst4 | -0.30 | 1.64 | +0.62 | -0.23 | yes |
| net_profit_adjusted_min_guidance | analyst4 | -0.21 | 1.50 | +0.56 | -0.59 | yes |
| max_gross_income_guidance_2 | analyst4 | -0.31 | 1.45 | +0.52 | -0.95 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
