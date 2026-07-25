---
field: fn_accum_depr_depletion_and_amortization_ppne_a
dataset: fundamental2
best_template: rank_value_norm
best_sharpe: 0.87
best_fitness: 0.67
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 5
max_drawdown: 0.0912
ann_vol: 0.0865
hit_rate: 0.4907
rolling_sharpe_min: -0.683
rolling_sharpe_max: 2.448
top_merge_partner: anl4_rd_exp_flag
redundancy_cluster: 1
negated_best_sharpe: 0.9
negated_best_template: rank_neg_delta
negated_best_fitness: 0.57
n_negated_sims: 10
direction_gap: 0.03
---
# fn_accum_depr_depletion_and_amortization_ppne_a (fundamental2)

*Amount of accumulated depreciation, depletion and amortization for physical assets used in the normal conduct of business to produce goods and services.*

## Signal Profile
- `rank(fn_accum_depr_depletion_and_amortization_ppne_a)`: S=0.52, F=0.37, T=0.9%, INFERIOR (TOP3000)
- `rank(fn_accum_depr_depletion_and_amortization_ppne_a / close)`: S=0.87, F=0.67, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_delta(fn_accum_depr_depletion_and_amortization_ppne_a, 5))`: S=-0.43, F=-0.22, T=32.8%, INFERIOR (TOP200)
- `-rank(fn_accum_depr_depletion_and_amortization_ppne_a)`: S=-0.27, F=-0.15, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_accum_depr_depletion_and_amortization_ppne_a, 5))`: S=0.90, F=0.57, T=35.0%, INFERIOR (TOP3000)
- `-ts_zscore(fn_accum_depr_depletion_and_amortization_ppne_a, 63)`: S=0.65, F=0.50, T=19.2%, INFERIOR (TOP3000)
- `ts_mean(fn_accum_depr_depletion_and_amortization_ppne_a, 10)`: S=-0.02, F=0.00, T=0.8%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_accum_depr_depletion_and_amortization_ppne_a, 22))`: S=-0.04, F=-0.01, T=14.6%, INFERIOR (TOP3000)
- `rank(-1 * fn_accum_depr_depletion_and_amortization_ppne_a)`: S=-0.27, F=-0.15, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * fn_accum_depr_depletion_and_amortization_ppne_a / close)`: S=-0.41, F=-0.26, T=1.6%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 16F/13P
- LOW_TURNOVER: 2F/30P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.85, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.45 (weak), ret=+2.1%
  - 2020: S=-0.02 (negative), ret=-0.2%
  - 2021: S=1.32 (moderate), ret=+14.8%
  - 2022: S=1.93 (strong), ret=+18.8%
  - 2023: S=0.10 (weak), ret=+0.4%

## Risk & Drawdown
- Max drawdown: 9.12% over 238 days (recovered)
- Annualized: return +7.3%, volatility 8.6% (fraction of booksize)
- Hit rate: 49.1% positive days
- Tail shape: skew +0.49, excess kurtosis +3.11

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.68, max 2.45, latest 0.10

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +8.89%; worst month: -3.62%
Positive months: 58%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.07
- Sideways: S=0.29
- Bear: S=-1.48

## Negated Direction
Best negated: `rank(-1 * ts_delta(fn_accum_depr_depletion_and_amortization_ppne_a, 5))` S=0.90, F=0.57, INFERIOR
Direction gap: +0.03 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fn_accum_depr_depletion_and_amortization_ppne_a)`: S=-0.27, F=-0.15, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * fn_accum_depr_depletion_and_amortization_ppne_a / close)`: S=-0.41, F=-0.26, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_accum_depr_depletion_and_amortization_ppne_a, 5))`: S=0.90, F=0.57, T=35.0%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fn_accum_depr_depletion_and_amortization_ppne_a / close)` | TOP3000 | 0.85 | 0.67 | 9.1% | 80% | bull-only |
| `rank(fn_accum_depr_depletion_and_amortization_ppne_a)` | TOP3000 | 0.51 | 0.37 | 33.7% | 80% | bull-only |
| `rank(fn_accum_depr_depletion_and_amortization_ppne_a / close)` | TOP1000 | 0.40 | 0.26 | 17.0% | 40% | bull-only |
| `rank(fn_accum_depr_depletion_and_amortization_ppne_a)` | TOP1000 | 0.26 | 0.15 | 35.5% | 40% | bull-only |
| `rank(fn_accum_depr_depletion_and_amortization_ppne_a / close)` | TOP500 | 0.11 | 0.04 | 34.2% | 40% | bull-only |

## Correlation Notes
Top correlates:
- fn_mne_a: 0.983 (strongly positively correlated)
- fnd6_dpvieb: 0.972 (strongly positively correlated)
- fnd6_newa1v1300_dpact: 0.972 (strongly positively correlated)
- fn_ppne_gross_a: 0.970 (strongly positively correlated)
- fn_accum_depr_depletion_and_amortization_ppne_q: 0.959 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_rd_exp_flag | analyst4 | -0.41 | 1.73 | +0.70 | -0.67 | yes |
| rp_ess_revenue | news18 | -0.39 | 1.57 | +0.68 | -0.65 | yes |
| anl4_epsr_flag | analyst4 | -0.34 | 1.78 | +0.60 | -0.66 | yes |
| max_gross_income_guidance_2 | analyst4 | -0.37 | 1.46 | +0.61 | -0.52 | yes |
| fnd6_txtubadjust | fundamental6 | -0.31 | 1.44 | +0.59 | -0.69 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
