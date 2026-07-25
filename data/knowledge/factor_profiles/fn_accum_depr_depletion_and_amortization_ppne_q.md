---
field: fn_accum_depr_depletion_and_amortization_ppne_q
dataset: fundamental2
best_template: rank_value_norm
best_sharpe: 1.01
best_fitness: 0.84
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 8
max_drawdown: 0.0775
ann_vol: 0.0858
hit_rate: 0.5069
rolling_sharpe_min: -1.169
rolling_sharpe_max: 2.906
top_merge_partner: anl4_rd_exp_flag
redundancy_cluster: 1
negated_best_sharpe: 0.68
negated_best_template: rank_neg_delta
negated_best_fitness: 0.4
n_negated_sims: 10
direction_gap: -0.33
---
# fn_accum_depr_depletion_and_amortization_ppne_q (fundamental2)

*Amount of accumulated depreciation, depletion and amortization for physical assets used in the normal conduct of business to produce goods and services.*

## Signal Profile
- `rank(fn_accum_depr_depletion_and_amortization_ppne_q)`: S=0.55, F=0.40, T=0.9%, INFERIOR (TOP3000)
- `rank(fn_accum_depr_depletion_and_amortization_ppne_q / close)`: S=1.01, F=0.84, T=1.3%, INFERIOR (TOP3000)
- `rank(ts_delta(fn_accum_depr_depletion_and_amortization_ppne_q, 5))`: S=0.50, F=0.24, T=37.3%, INFERIOR (TOP200)
- `-rank(fn_accum_depr_depletion_and_amortization_ppne_q)`: S=-0.54, F=-0.39, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_accum_depr_depletion_and_amortization_ppne_q, 5))`: S=0.68, F=0.40, T=38.2%, INFERIOR (TOP3000)
- `ts_zscore(fn_accum_depr_depletion_and_amortization_ppne_q, 22)`: S=0.52, F=0.26, T=33.3%, INFERIOR (TOP3000)
- `ts_mean(fn_accum_depr_depletion_and_amortization_ppne_q, 10)`: S=0.30, F=0.14, T=0.8%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_accum_depr_depletion_and_amortization_ppne_q, 22))`: S=-0.52, F=-0.26, T=16.7%, INFERIOR (TOP3000)
- `rank(-1 * fn_accum_depr_depletion_and_amortization_ppne_q)`: S=-0.30, F=-0.16, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * fn_accum_depr_depletion_and_amortization_ppne_q / close)`: S=-0.58, F=-0.39, T=1.9%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 17F/12P
- LOW_TURNOVER: 2F/30P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.99, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.26 (weak), ret=+1.4%
  - 2020: S=-0.06 (negative), ret=-0.5%
  - 2021: S=1.72 (strong), ret=+18.2%
  - 2022: S=1.97 (strong), ret=+20.0%
  - 2023: S=0.59 (moderate), ret=+2.7%

## Risk & Drawdown
- Max drawdown: 7.75% over 453 days (recovered)
- Annualized: return +8.5%, volatility 8.6% (fraction of booksize)
- Hit rate: 50.7% positive days
- Tail shape: skew +0.45, excess kurtosis +2.81

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.17, max 2.91, latest 0.52

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +10.18%; worst month: -3.34%
Positive months: 63%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.26
- Sideways: S=0.34
- Bear: S=-1.23

## Negated Direction
Best negated: `rank(-1 * ts_delta(fn_accum_depr_depletion_and_amortization_ppne_q, 5))` S=0.68, F=0.40, INFERIOR
Direction gap: -0.33 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fn_accum_depr_depletion_and_amortization_ppne_q)`: S=-0.30, F=-0.16, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * fn_accum_depr_depletion_and_amortization_ppne_q / close)`: S=-0.58, F=-0.39, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_accum_depr_depletion_and_amortization_ppne_q, 5))`: S=0.68, F=0.40, T=38.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fn_accum_depr_depletion_and_amortization_ppne_q / close)` | TOP3000 | 0.99 | 0.84 | 7.8% | 80% | bull-only |
| `rank(fn_accum_depr_depletion_and_amortization_ppne_q / close)` | TOP1000 | 0.81 | 0.67 | 10.9% | 60% | bull-only |
| `rank(fn_accum_depr_depletion_and_amortization_ppne_q)` | TOP3000 | 0.54 | 0.40 | 33.6% | 80% | bull-only |
| `rank(fn_accum_depr_depletion_and_amortization_ppne_q / close)` | TOP500 | 0.58 | 0.39 | 20.1% | 80% | bull-only |
| `rank(fn_accum_depr_depletion_and_amortization_ppne_q)` | TOP1000 | 0.54 | 0.39 | 25.3% | 80% | bull-only |
| `rank(ts_delta(fn_accum_depr_depletion_and_amortization_ppne_q, 5))` | TOP200 | 0.50 | 0.24 | 25.4% | 80% | mixed |
| `rank(fn_accum_depr_depletion_and_amortization_ppne_q)` | TOP500 | 0.30 | 0.16 | 34.3% | 60% | bull-only |
| `rank(fn_accum_depr_depletion_and_amortization_ppne_q / close)` | TOP200 | 0.23 | 0.11 | 22.2% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fn_accum_depr_depletion_and_amortization_ppne_a: 0.959 (strongly positively correlated)
- fnd6_newa1v1300_dpact: 0.948 (strongly positively correlated)
- fnd6_dpvieb: 0.948 (strongly positively correlated)
- fn_mne_a: 0.943 (strongly positively correlated)
- fnd6_newqv1300_dpactq: 0.939 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_rd_exp_flag | analyst4 | -0.42 | 1.86 | +0.83 | -0.63 | yes |
| rp_ess_revenue | news18 | -0.39 | 1.68 | +0.69 | -0.77 | yes |
| anl4_epsr_flag | analyst4 | -0.32 | 1.86 | +0.69 | -0.67 | yes |
| net_profit_adjusted_min_guidance | analyst4 | -0.27 | 1.60 | +0.61 | -0.81 | yes |
| max_gross_income_guidance_2 | analyst4 | -0.36 | 1.57 | +0.58 | -0.70 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
