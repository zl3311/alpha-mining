---
field: fnd6_capxv
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 0.83
best_fitness: 0.58
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 7
max_drawdown: 0.0843
ann_vol: 0.0745
hit_rate: 0.4826
rolling_sharpe_min: -1.139
rolling_sharpe_max: 2.708
top_merge_partner: rp_ess_revenue
redundancy_cluster: 1
negated_best_sharpe: 0.35
negated_best_template: rank_neg_delta
negated_best_fitness: 0.15
n_negated_sims: 10
direction_gap: -0.48
---
# fnd6_capxv (fundamental6)

*Capital Expend Property, Plant and Equipment Schd V*

## Signal Profile
- `rank(fnd6_capxv)`: S=0.62, F=0.44, T=1.2%, INFERIOR (TOP3000)
- `rank(fnd6_capxv / close)`: S=0.83, F=0.58, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_capxv, 5))`: S=0.21, F=0.08, T=32.5%, INFERIOR (TOP200)
- `-rank(fnd6_capxv)`: S=-0.31, F=-0.17, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_capxv, 5))`: S=0.35, F=0.15, T=33.8%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_capxv, 63)`: S=0.56, F=0.35, T=18.9%, INFERIOR (TOP3000)
- `ts_mean(fnd6_capxv, 10)`: S=0.22, F=0.10, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_capxv, 22))`: S=-0.21, F=-0.07, T=15.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_capxv)`: S=-0.14, F=-0.05, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_capxv / close)`: S=-0.39, F=-0.22, T=2.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 18F/11P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.83, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=-0.46 (negative), ret=-2.1%
  - 2020: S=0.75 (moderate), ret=+5.8%
  - 2021: S=1.77 (strong), ret=+17.7%
  - 2022: S=0.65 (moderate), ret=+4.5%
  - 2023: S=0.75 (moderate), ret=+4.4%

## Risk & Drawdown
- Max drawdown: 8.43% over 407 days (recovered)
- Annualized: return +6.2%, volatility 7.4% (fraction of booksize)
- Hit rate: 48.3% positive days
- Tail shape: skew +0.54, excess kurtosis +2.24

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.14, max 2.71, latest 0.84

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2019
Best month: +7.68%; worst month: -3.54%
Positive months: 54%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.59
- Sideways: S=0.15
- Bear: S=-0.71

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_capxv, 5))` S=0.35, F=0.15, INFERIOR
Direction gap: -0.48 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_capxv)`: S=-0.14, F=-0.05, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_capxv / close)`: S=-0.39, F=-0.22, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_capxv, 5))`: S=0.35, F=0.15, T=33.8%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_capxv / close)` | TOP3000 | 0.83 | 0.58 | 8.4% | 80% | bull-only |
| `rank(fnd6_capxv)` | TOP3000 | 0.62 | 0.44 | 25.6% | 80% | bull-only |
| `rank(fnd6_capxv / close)` | TOP1000 | 0.42 | 0.24 | 10.3% | 60% | bull-only |
| `rank(fnd6_capxv / close)` | TOP500 | 0.39 | 0.22 | 19.4% | 60% | bull-only |
| `rank(fnd6_capxv)` | TOP1000 | 0.30 | 0.17 | 28.7% | 60% | bull-only |
| `rank(ts_delta(fnd6_capxv, 5))` | TOP200 | 0.21 | 0.08 | 42.9% | 60% | mixed |
| `rank(fnd6_capxv)` | TOP500 | 0.13 | 0.05 | 40.5% | 40% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_newa1v1300_capx: 0.997 (strongly positively correlated)
- capex: 0.997 (strongly positively correlated)
- fnd6_mfma1_capx: 0.997 (strongly positively correlated)
- ppent: 0.968 (strongly positively correlated)
- fnd6_newqv1300_ppentq: 0.968 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| rp_ess_revenue | news18 | -0.31 | 1.45 | +0.56 | -0.49 | yes |
| anl4_epsr_flag | analyst4 | -0.31 | 1.72 | +0.54 | -0.47 | yes |
| max_gross_income_guidance_2 | analyst4 | -0.23 | 1.29 | +0.46 | -0.96 | yes |
| min_gross_income_guidance | analyst4 | -0.15 | 1.29 | +0.42 | -0.45 | yes |
| max_gross_income_guidance | analyst4 | -0.15 | 1.30 | +0.41 | -0.45 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
