---
field: fnd6_newa1v1300_dpact
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 1.04
best_fitness: 0.92
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 8
max_drawdown: 0.1042
ann_vol: 0.0941
hit_rate: 0.5012
rolling_sharpe_min: -1.149
rolling_sharpe_max: 2.872
top_merge_partner: anl4_rd_exp_flag
redundancy_cluster: 1
negated_best_sharpe: 0.51
negated_best_template: rank_neg_delta
negated_best_fitness: 0.22
n_negated_sims: 10
direction_gap: -0.53
---
# fnd6_newa1v1300_dpact (fundamental6)

*Depreciation, Depletion and Amortization (Accumulated)*

## Signal Profile
- `rank(fnd6_newa1v1300_dpact)`: S=0.69, F=0.59, T=1.8%, INFERIOR (TOP3000)
- `rank(fnd6_newa1v1300_dpact / close)`: S=1.04, F=0.92, T=2.1%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_newa1v1300_dpact, 5))`: S=0.96, F=0.61, T=41.0%, INFERIOR (TOP1000)
- `-rank(fnd6_newa1v1300_dpact)`: S=-0.33, F=-0.21, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa1v1300_dpact, 5))`: S=0.51, F=0.22, T=39.6%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_newa1v1300_dpact, 22)`: S=0.24, F=0.11, T=26.1%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newa1v1300_dpact, 10)`: S=-0.17, F=-0.06, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newa1v1300_dpact, 22))`: S=0.83, F=0.58, T=19.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_dpact)`: S=-0.69, F=-0.59, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_dpact / close)`: S=-1.04, F=-0.92, T=2.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 18F/11P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 1.03, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.13 (weak), ret=+0.7%
  - 2020: S=-0.09 (negative), ret=-0.9%
  - 2021: S=1.86 (strong), ret=+23.8%
  - 2022: S=1.92 (strong), ret=+21.2%
  - 2023: S=0.55 (moderate), ret=+2.5%

## Risk & Drawdown
- Max drawdown: 10.42% over 238 days (recovered)
- Annualized: return +9.7%, volatility 9.4% (fraction of booksize)
- Hit rate: 50.1% positive days
- Tail shape: skew +0.37, excess kurtosis +3.10

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.15, max 2.87, latest 0.53

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +10.98%; worst month: -3.94%
Positive months: 61%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.34
- Sideways: S=0.33
- Bear: S=-1.42

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_newa1v1300_dpact, 5))` S=0.51, F=0.22, INFERIOR
Direction gap: -0.53 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_newa1v1300_dpact)`: S=-0.69, F=-0.59, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_dpact / close)`: S=-1.04, F=-0.92, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa1v1300_dpact, 5))`: S=0.51, F=0.22, T=39.6%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newa1v1300_dpact / close)` | TOP3000 | 1.03 | 0.92 | 10.4% | 80% | bull-only |
| `rank(ts_delta(fnd6_newa1v1300_dpact, 5))` | TOP1000 | 0.97 | 0.61 | 33.0% | 80% | all-weather |
| `rank(fnd6_newa1v1300_dpact)` | TOP3000 | 0.68 | 0.59 | 34.7% | 80% | bull-only |
| `rank(fnd6_newa1v1300_dpact / close)` | TOP1000 | 0.49 | 0.34 | 16.5% | 40% | bull-only |
| `rank(ts_delta(fnd6_newa1v1300_dpact, 5))` | TOP500 | 0.46 | 0.24 | 56.1% | 60% | weak |
| `rank(fnd6_newa1v1300_dpact)` | TOP1000 | 0.32 | 0.21 | 38.0% | 60% | bull-only |
| `rank(fnd6_newa1v1300_dpact / close)` | TOP500 | 0.22 | 0.11 | 32.8% | 40% | bull-only |
| `rank(fnd6_newa1v1300_dpact)` | TOP500 | 0.07 | 0.02 | 51.5% | 40% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_dpvieb: 0.999 (strongly positively correlated)
- fn_accum_depr_depletion_and_amortization_ppne_a: 0.972 (strongly positively correlated)
- fnd6_newa2v1300_ppegt: 0.969 (strongly positively correlated)
- fnd6_ppeveb: 0.968 (strongly positively correlated)
- fn_mne_a: 0.962 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_rd_exp_flag | analyst4 | -0.41 | 1.89 | +0.86 | -0.58 | yes |
| rp_ess_revenue | news18 | -0.38 | 1.72 | +0.69 | -0.79 | yes |
| anl4_epsr_flag | analyst4 | -0.30 | 1.87 | +0.69 | -0.70 | yes |
| net_profit_adjusted_min_guidance | analyst4 | -0.28 | 1.64 | +0.61 | -0.81 | yes |
| max_gross_income_guidance_2 | analyst4 | -0.35 | 1.60 | +0.57 | -0.75 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
