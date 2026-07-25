---
field: fnd6_newa1v1300_capx
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
max_drawdown: 0.0815
ann_vol: 0.0726
hit_rate: 0.4842
rolling_sharpe_min: -1.262
rolling_sharpe_max: 2.685
top_merge_partner: rp_ess_revenue
redundancy_cluster: 1
negated_best_sharpe: 0.37
negated_best_template: rank_neg_delta
negated_best_fitness: 0.16
n_negated_sims: 10
direction_gap: -0.46
---
# fnd6_newa1v1300_capx (fundamental6)

*Capital Expenditures*

## Signal Profile
- `rank(fnd6_newa1v1300_capx)`: S=0.63, F=0.44, T=1.3%, INFERIOR (TOP3000)
- `rank(fnd6_newa1v1300_capx / close)`: S=0.83, F=0.58, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_newa1v1300_capx, 5))`: S=0.21, F=0.08, T=32.4%, INFERIOR (TOP200)
- `-rank(fnd6_newa1v1300_capx)`: S=-0.32, F=-0.17, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa1v1300_capx, 5))`: S=0.37, F=0.16, T=34.0%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_newa1v1300_capx, 63)`: S=0.45, F=0.25, T=19.0%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newa1v1300_capx, 10)`: S=0.22, F=0.09, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newa1v1300_capx, 22))`: S=-0.12, F=-0.03, T=15.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_capx)`: S=-0.16, F=-0.06, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_capx / close)`: S=-0.42, F=-0.24, T=2.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/15P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.83, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=-0.48 (negative), ret=-2.2%
  - 2020: S=0.78 (moderate), ret=+6.0%
  - 2021: S=1.73 (strong), ret=+16.7%
  - 2022: S=0.67 (moderate), ret=+4.6%
  - 2023: S=0.77 (moderate), ret=+4.5%

## Risk & Drawdown
- Max drawdown: 8.15% over 406 days (recovered)
- Annualized: return +6.0%, volatility 7.3% (fraction of booksize)
- Hit rate: 48.4% positive days
- Tail shape: skew +0.55, excess kurtosis +2.32

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.26, max 2.69, latest 0.85

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2019
Best month: +7.41%; worst month: -3.47%
Positive months: 56%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.58
- Sideways: S=0.23
- Bear: S=-0.73

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_newa1v1300_capx, 5))` S=0.37, F=0.16, INFERIOR
Direction gap: -0.46 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_newa1v1300_capx)`: S=-0.16, F=-0.06, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_capx / close)`: S=-0.42, F=-0.24, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa1v1300_capx, 5))`: S=0.37, F=0.16, T=34.0%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newa1v1300_capx / close)` | TOP3000 | 0.83 | 0.58 | 8.2% | 80% | bull-only |
| `rank(fnd6_newa1v1300_capx)` | TOP3000 | 0.62 | 0.44 | 23.7% | 80% | bull-only |
| `rank(fnd6_newa1v1300_capx / close)` | TOP1000 | 0.44 | 0.25 | 9.9% | 60% | bull-only |
| `rank(fnd6_newa1v1300_capx / close)` | TOP500 | 0.41 | 0.24 | 16.2% | 60% | bull-only |
| `rank(fnd6_newa1v1300_capx)` | TOP1000 | 0.31 | 0.17 | 27.2% | 60% | bull-only |
| `rank(ts_delta(fnd6_newa1v1300_capx, 5))` | TOP200 | 0.20 | 0.08 | 43.0% | 60% | mixed |
| `rank(fnd6_newa1v1300_capx)` | TOP500 | 0.15 | 0.06 | 36.8% | 40% | bull-only |

## Correlation Notes
Top correlates:
- capex: 1.000 (strongly positively correlated)
- fnd6_mfma1_capx: 1.000 (strongly positively correlated)
- fnd6_capxv: 0.997 (strongly positively correlated)
- ppent: 0.970 (strongly positively correlated)
- fnd6_newqv1300_ppentq: 0.970 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| rp_ess_revenue | news18 | -0.31 | 1.44 | +0.55 | -0.47 | yes |
| anl4_epsr_flag | analyst4 | -0.31 | 1.72 | +0.54 | -0.44 | yes |
| max_gross_income_guidance_2 | analyst4 | -0.24 | 1.29 | +0.46 | -0.97 | yes |
| min_gross_income_guidance | analyst4 | -0.16 | 1.28 | +0.41 | -0.47 | yes |
| max_gross_income_guidance | analyst4 | -0.15 | 1.30 | +0.41 | -0.47 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
