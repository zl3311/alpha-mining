---
field: fnd2_a_flintasacmamtzcsrld
dataset: fundamental2
best_template: rank_value_norm
best_sharpe: 0.98
best_fitness: 0.72
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 8
max_drawdown: 0.0683
ann_vol: 0.07
hit_rate: 0.5109
rolling_sharpe_min: -0.484
rolling_sharpe_max: 2.151
top_merge_partner: anl4_rd_exp_flag
redundancy_cluster: 1
negated_best_sharpe: 0.59
negated_best_template: rank_neg_delta
negated_best_fitness: 0.31
n_negated_sims: 10
direction_gap: -0.39
---
# fnd2_a_flintasacmamtzcsrld (fundamental2)

*Finite Lived Intangible Assets Accumulated Amortization, Customer Related*

## Signal Profile
- `rank(fnd2_a_flintasacmamtzcsrld)`: S=0.48, F=0.27, T=0.7%, INFERIOR (TOP3000)
- `rank(fnd2_a_flintasacmamtzcsrld / close)`: S=0.98, F=0.72, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd2_a_flintasacmamtzcsrld, 5))`: S=0.20, F=0.06, T=31.3%, INFERIOR (TOP500)
- `-rank(fnd2_a_flintasacmamtzcsrld)`: S=-0.24, F=-0.11, T=1.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_a_flintasacmamtzcsrld, 5))`: S=0.59, F=0.31, T=32.6%, INFERIOR (TOP3000)
- `-ts_zscore(fnd2_a_flintasacmamtzcsrld, 63)`: S=0.35, F=0.20, T=17.7%, INFERIOR (TOP3000)
- `ts_mean(fnd2_a_flintasacmamtzcsrld, 10)`: S=0.21, F=0.08, T=0.8%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd2_a_flintasacmamtzcsrld, 22))`: S=-0.90, F=-0.69, T=15.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_a_flintasacmamtzcsrld)`: S=-0.24, F=-0.11, T=1.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_a_flintasacmamtzcsrld / close)`: S=-0.36, F=-0.19, T=1.5%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/15P
- LOW_TURNOVER: 2F/30P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.97, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.72 (moderate), ret=+3.5%
  - 2020: S=0.68 (moderate), ret=+6.3%
  - 2021: S=0.92 (moderate), ret=+7.0%
  - 2022: S=1.84 (strong), ret=+13.2%
  - 2023: S=0.86 (moderate), ret=+3.3%

## Risk & Drawdown
- Max drawdown: 6.83% over 237 days (recovered)
- Annualized: return +6.8%, volatility 7.0% (fraction of booksize)
- Hit rate: 51.1% positive days
- Tail shape: skew +0.65, excess kurtosis +3.67

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.48, max 2.15, latest 0.94

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +5.55%; worst month: -2.95%
Positive months: 61%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.22
- Sideways: S=0.22
- Bear: S=-0.91

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd2_a_flintasacmamtzcsrld, 5))` S=0.59, F=0.31, INFERIOR
Direction gap: -0.39 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd2_a_flintasacmamtzcsrld)`: S=-0.24, F=-0.11, T=1.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_a_flintasacmamtzcsrld / close)`: S=-0.36, F=-0.19, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_a_flintasacmamtzcsrld, 5))`: S=0.59, F=0.31, T=32.6%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd2_a_flintasacmamtzcsrld / close)` | TOP3000 | 0.97 | 0.72 | 6.8% | 100% | bull-only |
| `rank(fnd2_a_flintasacmamtzcsrld / close)` | TOP200 | 0.42 | 0.27 | 17.8% | 60% | bull-only |
| `rank(fnd2_a_flintasacmamtzcsrld)` | TOP3000 | 0.47 | 0.27 | 18.1% | 80% | bull-only |
| `rank(fnd2_a_flintasacmamtzcsrld / close)` | TOP1000 | 0.35 | 0.19 | 11.5% | 60% | bull-only |
| `rank(fnd2_a_flintasacmamtzcsrld)` | TOP1000 | 0.23 | 0.11 | 19.2% | 60% | bull-only |
| `rank(fnd2_a_flintasacmamtzcsrld)` | TOP200 | 0.20 | 0.10 | 22.5% | 60% | bull-only |
| `rank(ts_delta(fnd2_a_flintasacmamtzcsrld, 5))` | TOP500 | 0.20 | 0.06 | 40.4% | 80% | bull-only |
| `rank(fnd2_a_flintasacmamtzcsrld / close)` | TOP500 | 0.06 | 0.02 | 22.5% | 20% | bull-only |

## Correlation Notes
Top correlates:
- fnd2_a_flintasgcsrld: 0.960 (strongly positively correlated)
- fn_intangible_assets_accum_amort_a: 0.934 (strongly positively correlated)
- fn_finite_lived_intangible_assets_gross_a: 0.901 (strongly positively correlated)
- fn_intangible_assets_accum_amort_q: 0.898 (strongly positively correlated)
- fn_interest_paid_net_a: 0.887 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_rd_exp_flag | analyst4 | -0.39 | 1.75 | +0.72 | -0.59 | yes |
| anl4_epsr_flag | analyst4 | -0.34 | 1.84 | +0.66 | -0.17 | yes |
| rp_ess_revenue | news18 | -0.38 | 1.60 | +0.63 | -0.26 | yes |
| fnd6_txtubadjust | fundamental6 | -0.30 | 1.53 | +0.56 | -0.87 | yes |
| max_gross_income_guidance | analyst4 | -0.30 | 1.50 | +0.53 | -0.85 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
