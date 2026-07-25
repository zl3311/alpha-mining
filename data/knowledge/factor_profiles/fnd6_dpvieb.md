---
field: fnd6_dpvieb
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 1.05
best_fitness: 0.93
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 8
max_drawdown: 0.1032
ann_vol: 0.0949
hit_rate: 0.5028
rolling_sharpe_min: -1.18
rolling_sharpe_max: 2.876
top_merge_partner: anl4_rd_exp_flag
redundancy_cluster: 1
negated_best_sharpe: 0.51
negated_best_template: rank_neg_delta
negated_best_fitness: 0.23
n_negated_sims: 10
direction_gap: -0.54
---
# fnd6_dpvieb (fundamental6)

*Depreciation (Accumulated) - Ending Balance (Schedule VI)*

## Signal Profile
- `rank(fnd6_dpvieb)`: S=0.71, F=0.62, T=1.8%, INFERIOR (TOP3000)
- `rank(fnd6_dpvieb / close)`: S=1.05, F=0.93, T=2.1%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_dpvieb, 5))`: S=0.99, F=0.64, T=40.7%, INFERIOR (TOP1000)
- `-rank(fnd6_dpvieb)`: S=-0.32, F=-0.20, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_dpvieb, 5))`: S=0.51, F=0.23, T=40.0%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_dpvieb, 22)`: S=0.22, F=0.09, T=25.9%, INFERIOR (TOP3000)
- `ts_mean(fnd6_dpvieb, 10)`: S=-0.18, F=-0.07, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_dpvieb, 22))`: S=0.81, F=0.56, T=19.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_dpvieb)`: S=-0.71, F=-0.62, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_dpvieb / close)`: S=-1.05, F=-0.93, T=2.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 18F/11P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 1.04, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.15 (weak), ret=+0.8%
  - 2020: S=-0.08 (negative), ret=-0.8%
  - 2021: S=1.86 (strong), ret=+24.0%
  - 2022: S=1.95 (strong), ret=+21.7%
  - 2023: S=0.55 (moderate), ret=+2.5%

## Risk & Drawdown
- Max drawdown: 10.32% over 238 days (recovered)
- Annualized: return +9.8%, volatility 9.5% (fraction of booksize)
- Hit rate: 50.3% positive days
- Tail shape: skew +0.38, excess kurtosis +3.09

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.18, max 2.88, latest 0.54

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +11.04%; worst month: -3.90%
Positive months: 61%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.36
- Sideways: S=0.33
- Bear: S=-1.40

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_dpvieb, 5))` S=0.51, F=0.23, INFERIOR
Direction gap: -0.54 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_dpvieb)`: S=-0.71, F=-0.62, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_dpvieb / close)`: S=-1.05, F=-0.93, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_dpvieb, 5))`: S=0.51, F=0.23, T=40.0%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_dpvieb / close)` | TOP3000 | 1.04 | 0.93 | 10.3% | 80% | bull-only |
| `rank(ts_delta(fnd6_dpvieb, 5))` | TOP1000 | 0.99 | 0.64 | 32.1% | 80% | all-weather |
| `rank(fnd6_dpvieb)` | TOP3000 | 0.70 | 0.62 | 35.0% | 80% | bull-only |
| `rank(fnd6_dpvieb / close)` | TOP1000 | 0.45 | 0.30 | 18.2% | 40% | bull-only |
| `rank(ts_delta(fnd6_dpvieb, 5))` | TOP500 | 0.48 | 0.26 | 54.7% | 60% | weak |
| `rank(fnd6_dpvieb)` | TOP1000 | 0.31 | 0.20 | 39.3% | 40% | bull-only |
| `rank(fnd6_dpvieb / close)` | TOP500 | 0.20 | 0.09 | 35.0% | 40% | bull-only |
| `rank(fnd6_dpvieb)` | TOP500 | 0.05 | 0.02 | 54.2% | 40% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_newa1v1300_dpact: 0.999 (strongly positively correlated)
- fn_accum_depr_depletion_and_amortization_ppne_a: 0.972 (strongly positively correlated)
- fnd6_newa2v1300_ppegt: 0.969 (strongly positively correlated)
- fnd6_ppeveb: 0.969 (strongly positively correlated)
- fn_mne_a: 0.963 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_rd_exp_flag | analyst4 | -0.41 | 1.90 | +0.86 | -0.58 | yes |
| anl4_epsr_flag | analyst4 | -0.31 | 1.88 | +0.71 | -0.70 | yes |
| rp_ess_revenue | news18 | -0.38 | 1.73 | +0.69 | -0.79 | yes |
| net_profit_adjusted_min_guidance | analyst4 | -0.28 | 1.65 | +0.61 | -0.81 | yes |
| max_gross_income_guidance_2 | analyst4 | -0.35 | 1.61 | +0.57 | -0.74 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
