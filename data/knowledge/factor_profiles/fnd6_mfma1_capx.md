---
field: fnd6_mfma1_capx
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 0.83
best_fitness: 0.57
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 7
max_drawdown: 0.082
ann_vol: 0.0725
hit_rate: 0.4842
rolling_sharpe_min: -1.271
rolling_sharpe_max: 2.686
top_merge_partner: rp_ess_revenue
redundancy_cluster: 1
negated_best_sharpe: 0.47
negated_best_template: rank_neg_delta
negated_best_fitness: 0.23
n_negated_sims: 10
direction_gap: -0.36
---
# fnd6_mfma1_capx (fundamental6)

*Capital Expenditures*

## Signal Profile
- `rank(fnd6_mfma1_capx)`: S=0.62, F=0.43, T=1.2%, INFERIOR (TOP3000)
- `rank(fnd6_mfma1_capx / close)`: S=0.83, F=0.57, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_mfma1_capx, 5))`: S=0.19, F=0.07, T=32.2%, INFERIOR (TOP200)
- `-rank(fnd6_mfma1_capx)`: S=-0.30, F=-0.16, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_mfma1_capx, 5))`: S=0.47, F=0.23, T=33.7%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_mfma1_capx, 63)`: S=0.44, F=0.24, T=19.0%, INFERIOR (TOP3000)
- `ts_mean(fnd6_mfma1_capx, 10)`: S=0.19, F=0.08, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_mfma1_capx, 22))`: S=-0.14, F=-0.04, T=15.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_mfma1_capx)`: S=-0.16, F=-0.06, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_mfma1_capx / close)`: S=-0.41, F=-0.23, T=2.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 17F/12P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.83, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=-0.47 (negative), ret=-2.1%
  - 2020: S=0.76 (moderate), ret=+5.8%
  - 2021: S=1.73 (strong), ret=+16.6%
  - 2022: S=0.68 (moderate), ret=+4.6%
  - 2023: S=0.78 (moderate), ret=+4.5%

## Risk & Drawdown
- Max drawdown: 8.20% over 406 days (recovered)
- Annualized: return +6.0%, volatility 7.2% (fraction of booksize)
- Hit rate: 48.4% positive days
- Tail shape: skew +0.56, excess kurtosis +2.34

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.27, max 2.69, latest 0.87

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2019
Best month: +7.46%; worst month: -3.33%
Positive months: 54%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.59
- Sideways: S=0.23
- Bear: S=-0.75

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_mfma1_capx, 5))` S=0.47, F=0.23, INFERIOR
Direction gap: -0.36 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_mfma1_capx)`: S=-0.16, F=-0.06, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_mfma1_capx / close)`: S=-0.41, F=-0.23, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_mfma1_capx, 5))`: S=0.47, F=0.23, T=33.7%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_mfma1_capx / close)` | TOP3000 | 0.83 | 0.57 | 8.2% | 80% | bull-only |
| `rank(fnd6_mfma1_capx)` | TOP3000 | 0.61 | 0.43 | 24.0% | 80% | bull-only |
| `rank(fnd6_mfma1_capx / close)` | TOP1000 | 0.43 | 0.24 | 9.8% | 60% | bull-only |
| `rank(fnd6_mfma1_capx / close)` | TOP500 | 0.41 | 0.23 | 16.1% | 60% | bull-only |
| `rank(fnd6_mfma1_capx)` | TOP1000 | 0.30 | 0.16 | 27.5% | 60% | bull-only |
| `rank(ts_delta(fnd6_mfma1_capx, 5))` | TOP200 | 0.18 | 0.07 | 43.0% | 60% | mixed |
| `rank(fnd6_mfma1_capx)` | TOP500 | 0.15 | 0.06 | 36.7% | 40% | bull-only |

## Correlation Notes
Top correlates:
- capex: 1.000 (strongly positively correlated)
- fnd6_newa1v1300_capx: 1.000 (strongly positively correlated)
- fnd6_capxv: 0.997 (strongly positively correlated)
- ppent: 0.970 (strongly positively correlated)
- fnd6_newqv1300_ppentq: 0.970 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| rp_ess_revenue | news18 | -0.31 | 1.44 | +0.55 | -0.48 | yes |
| anl4_epsr_flag | analyst4 | -0.31 | 1.72 | +0.54 | -0.45 | yes |
| max_gross_income_guidance_2 | analyst4 | -0.24 | 1.29 | +0.46 | -0.97 | yes |
| min_gross_income_guidance | analyst4 | -0.16 | 1.28 | +0.42 | -0.48 | yes |
| max_gross_income_guidance | analyst4 | -0.16 | 1.30 | +0.41 | -0.48 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
