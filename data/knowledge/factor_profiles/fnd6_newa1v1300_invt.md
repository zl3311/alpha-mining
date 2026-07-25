---
field: fnd6_newa1v1300_invt
dataset: fundamental6
best_template: ts_zscore
best_sharpe: 0.9
best_fitness: 0.76
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 9
max_drawdown: 0.0841
ann_vol: 0.0668
hit_rate: 0.5061
rolling_sharpe_min: -0.986
rolling_sharpe_max: 2.705
top_merge_partner: rp_ess_revenue
redundancy_cluster: 1
negated_best_sharpe: 0.29
negated_best_template: neg_rank_level
negated_best_fitness: 0.15
n_negated_sims: 10
direction_gap: -0.61
---
# fnd6_newa1v1300_invt (fundamental6)

*Inventories - Total*

## Signal Profile
- `rank(fnd6_newa1v1300_invt)`: S=0.63, F=0.42, T=0.9%, INFERIOR (TOP3000)
- `rank(fnd6_newa1v1300_invt / close)`: S=0.91, F=0.63, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_newa1v1300_invt, 5))`: S=0.36, F=0.12, T=35.0%, INFERIOR (TOP3000)
- `-rank(fnd6_newa1v1300_invt)`: S=-0.34, F=-0.18, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa1v1300_invt, 5))`: S=-0.24, F=-0.10, T=32.1%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_newa1v1300_invt, 22)`: S=0.90, F=0.76, T=25.7%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newa1v1300_invt, 10)`: S=0.30, F=0.14, T=0.9%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newa1v1300_invt, 22))`: S=0.68, F=0.43, T=14.6%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_invt)`: S=0.29, F=0.15, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_invt / close)`: S=0.31, F=0.15, T=2.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 5F/15P
- LOW_TURNOVER: 2F/30P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.90, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=-0.24 (negative), ret=-1.0%
  - 2020: S=0.30 (weak), ret=+2.0%
  - 2021: S=1.82 (strong), ret=+15.7%
  - 2022: S=1.21 (moderate), ret=+9.6%
  - 2023: S=0.75 (moderate), ret=+3.3%

## Risk & Drawdown
- Max drawdown: 8.41% over 530 days (recovered)
- Annualized: return +6.0%, volatility 6.7% (fraction of booksize)
- Hit rate: 50.6% positive days
- Tail shape: skew +0.08, excess kurtosis +1.66

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.99, max 2.71, latest 0.65

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2019
Best month: +7.38%; worst month: -3.72%
Positive months: 59%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.60
- Sideways: S=0.09
- Bear: S=-1.71

## Negated Direction
Best negated: `rank(-1 * fnd6_newa1v1300_invt)` S=0.29, F=0.15, INFERIOR
Direction gap: -0.61 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_newa1v1300_invt)`: S=0.29, F=0.15, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_invt / close)`: S=0.31, F=0.15, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa1v1300_invt, 5))`: S=-0.24, F=-0.10, T=32.1%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newa1v1300_invt / close)` | TOP3000 | 0.90 | 0.63 | 8.4% | 80% | bull-only |
| `rank(fnd6_newa1v1300_invt)` | TOP3000 | 0.62 | 0.42 | 19.6% | 80% | bull-only |
| `rank(fnd6_newa1v1300_invt / close)` | TOP1000 | 0.49 | 0.29 | 11.1% | 60% | bull-only |
| `rank(fnd6_newa1v1300_invt / close)` | TOP500 | 0.42 | 0.23 | 12.2% | 60% | bull-only |
| `rank(fnd6_newa1v1300_invt)` | TOP1000 | 0.33 | 0.18 | 22.5% | 60% | bull-only |
| `rank(fnd6_newa1v1300_invt)` | TOP500 | 0.29 | 0.15 | 26.1% | 80% | bull-only |
| `rank(ts_delta(fnd6_newa1v1300_invt, 5))` | TOP3000 | 0.36 | 0.12 | 14.2% | 80% | weak |
| `rank(ts_delta(fnd6_newa1v1300_invt, 5))` | TOP500 | 0.21 | 0.08 | 34.8% | 60% | mixed |
| `rank(ts_delta(fnd6_newa1v1300_invt, 5))` | TOP200 | 0.13 | 0.04 | 47.8% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_newqv1300_invtq: 0.987 (strongly positively correlated)
- inventory: 0.987 (strongly positively correlated)
- fnd6_invfg: 0.937 (strongly positively correlated)
- fnd6_newa1v1300_gp: 0.923 (strongly positively correlated)
- fnd6_rectr: 0.923 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| rp_ess_revenue | news18 | -0.31 | 1.47 | +0.57 | -0.73 | yes |
| anl4_rd_exp_flag | analyst4 | -0.35 | 1.64 | +0.61 | -0.20 | yes |
| net_profit_adjusted_min_guidance | analyst4 | -0.24 | 1.49 | +0.54 | -0.62 | yes |
| max_gross_income_guidance_2 | analyst4 | -0.30 | 1.38 | +0.47 | -0.95 | yes |
| anl4_epsr_flag | analyst4 | -0.24 | 1.68 | +0.50 | -0.63 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
