---
field: fnd2_a_rvndm
dataset: fundamental2
best_template: rank_value_norm
best_sharpe: 0.91
best_fitness: 0.7
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 8
max_drawdown: 0.1022
ann_vol: 0.0822
hit_rate: 0.4931
rolling_sharpe_min: -1.067
rolling_sharpe_max: 2.611
top_merge_partner: anl4_rd_exp_flag
redundancy_cluster: 1
negated_best_sharpe: 0.03
negated_best_template: neg_rank_level
negated_best_fitness: 0.01
n_negated_sims: 10
direction_gap: -0.88
---
# fnd2_a_rvndm (fundamental2)

*Revenue, Domestic*

## Signal Profile
- `rank(fnd2_a_rvndm)`: S=0.42, F=0.26, T=0.8%, INFERIOR (TOP3000)
- `rank(fnd2_a_rvndm / close)`: S=0.91, F=0.70, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd2_a_rvndm, 5))`: S=0.66, F=0.34, T=33.6%, INFERIOR (TOP3000)
- `-rank(fnd2_a_rvndm)`: S=-0.13, F=-0.05, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_a_rvndm, 5))`: S=-0.40, F=-0.18, T=32.8%, INFERIOR (TOP3000)
- `ts_zscore(fnd2_a_rvndm, 22)`: S=0.08, F=0.02, T=20.3%, INFERIOR (TOP3000)
- `ts_mean(fnd2_a_rvndm, 10)`: S=0.02, F=0.00, T=0.8%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd2_a_rvndm, 22))`: S=0.10, F=0.02, T=15.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_a_rvndm)`: S=0.03, F=0.01, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_a_rvndm / close)`: S=-0.13, F=-0.04, T=2.0%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 15F/14P
- LOW_TURNOVER: 2F/30P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.90, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=-0.09 (negative), ret=-0.4%
  - 2020: S=0.34 (weak), ret=+3.1%
  - 2021: S=1.28 (moderate), ret=+13.6%
  - 2022: S=1.59 (strong), ret=+14.4%
  - 2023: S=1.23 (moderate), ret=+5.5%

## Risk & Drawdown
- Max drawdown: 10.22% over 400 days (recovered)
- Annualized: return +7.4%, volatility 8.2% (fraction of booksize)
- Hit rate: 49.3% positive days
- Tail shape: skew +0.40, excess kurtosis +2.52

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.07, max 2.61, latest 1.25

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2019
Best month: +7.75%; worst month: -3.80%
Positive months: 58%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.89
- Sideways: S=0.28
- Bear: S=-1.07

## Negated Direction
Best negated: `rank(-1 * fnd2_a_rvndm)` S=0.03, F=0.01, INFERIOR
Direction gap: -0.88 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd2_a_rvndm)`: S=0.03, F=0.01, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_a_rvndm / close)`: S=-0.13, F=-0.04, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_a_rvndm, 5))`: S=-0.40, F=-0.18, T=32.8%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd2_a_rvndm / close)` | TOP3000 | 0.90 | 0.70 | 10.2% | 80% | bull-only |
| `rank(ts_delta(fnd2_a_rvndm, 5))` | TOP3000 | 0.68 | 0.34 | 16.7% | 100% | mixed |
| `rank(fnd2_a_rvndm)` | TOP3000 | 0.41 | 0.26 | 31.3% | 80% | bull-only |
| `rank(fnd2_a_rvndm / close)` | TOP1000 | 0.38 | 0.22 | 13.5% | 60% | bull-only |
| `rank(ts_delta(fnd2_a_rvndm, 5))` | TOP1000 | 0.39 | 0.17 | 22.9% | 80% | weak |
| `rank(ts_delta(fnd2_a_rvndm, 5))` | TOP500 | 0.34 | 0.15 | 27.7% | 60% | weak |
| `rank(fnd2_a_rvndm)` | TOP1000 | 0.12 | 0.05 | 35.0% | 60% | bull-only |
| `rank(fnd2_a_rvndm / close)` | TOP500 | 0.12 | 0.04 | 29.4% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fn_accum_depr_depletion_and_amortization_ppne_a: 0.930 (strongly positively correlated)
- fnd2_asdm: 0.924 (strongly positively correlated)
- fn_intangible_assets_accum_amort_a: 0.923 (strongly positively correlated)
- fnd6_mfma2_revt: 0.920 (strongly positively correlated)
- fnd6_newa2v1300_sale: 0.920 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_rd_exp_flag | analyst4 | -0.41 | 1.76 | +0.74 | -0.34 | yes |
| rp_ess_revenue | news18 | -0.36 | 1.57 | +0.67 | -0.51 | yes |
| max_gross_income_guidance | analyst4 | -0.28 | 1.47 | +0.57 | -0.90 | yes |
| max_gross_income_guidance_2 | analyst4 | -0.35 | 1.47 | +0.57 | -0.81 | yes |
| min_gross_income_guidance | analyst4 | -0.28 | 1.45 | +0.56 | -0.89 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
