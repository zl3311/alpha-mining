---
field: fnd6_dxd4
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 0.92
best_fitness: 0.59
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 11
max_drawdown: 0.0549
ann_vol: 0.0567
hit_rate: 0.5109
rolling_sharpe_min: -0.661
rolling_sharpe_max: 2.644
top_merge_partner: anl4_rd_exp_flag
redundancy_cluster: 1
negated_best_sharpe: 0.25
negated_best_template: rank_neg_delta
negated_best_fitness: 0.08
n_negated_sims: 10
direction_gap: -0.67
---
# fnd6_dxd4 (fundamental6)

*Debt (excl Capitalized Leases) - Due in 4th Year*

## Signal Profile
- `rank(fnd6_dxd4)`: S=0.71, F=0.42, T=1.9%, INFERIOR (TOP3000)
- `rank(fnd6_dxd4 / close)`: S=0.92, F=0.59, T=2.1%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_dxd4, 5))`: S=0.39, F=0.23, T=21.8%, INFERIOR (TOP200)
- `-rank(fnd6_dxd4)`: S=-0.10, F=-0.03, T=2.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_dxd4, 5))`: S=0.25, F=0.08, T=41.9%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_dxd4, 22)`: S=0.36, F=0.23, T=15.6%, INFERIOR (TOP3000)
- `ts_mean(fnd6_dxd4, 10)`: S=0.11, F=0.03, T=2.0%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_dxd4, 22))`: S=-0.53, F=-0.30, T=20.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_dxd4)`: S=-0.71, F=-0.42, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_dxd4 / close)`: S=-0.92, F=-0.59, T=2.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 11F/18P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.92, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=1.22 (moderate), ret=+4.0%
  - 2020: S=0.17 (weak), ret=+1.1%
  - 2021: S=1.43 (moderate), ret=+10.0%
  - 2022: S=1.54 (strong), ret=+9.7%
  - 2023: S=0.27 (weak), ret=+0.9%

## Risk & Drawdown
- Max drawdown: 5.49% over 211 days (recovered)
- Annualized: return +5.2%, volatility 5.7% (fraction of booksize)
- Hit rate: 51.1% positive days
- Tail shape: skew +0.16, excess kurtosis +2.18

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.66, max 2.64, latest 0.17

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +4.98%; worst month: -2.27%
Positive months: 63%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.63
- Sideways: S=1.11
- Bear: S=-1.12

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_dxd4, 5))` S=0.25, F=0.08, INFERIOR
Direction gap: -0.67 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_dxd4)`: S=-0.71, F=-0.42, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_dxd4 / close)`: S=-0.92, F=-0.59, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_dxd4, 5))`: S=0.25, F=0.08, T=41.9%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_dxd4 / close)` | TOP3000 | 0.92 | 0.59 | 5.5% | 100% | bull-only |
| `rank(fnd6_dxd4)` | TOP3000 | 0.70 | 0.42 | 10.2% | 80% | bull-only |
| `rank(fnd6_dxd4 / close)` | TOP500 | 0.52 | 0.30 | 10.0% | 60% | bull-only |
| `rank(ts_delta(fnd6_dxd4, 5))` | TOP200 | 0.39 | 0.23 | 28.1% | 40% | weak |
| `rank(fnd6_dxd4 / close)` | TOP200 | 0.28 | 0.14 | 18.7% | 60% | bull-only |
| `rank(ts_delta(fnd6_dxd4, 5))` | TOP1000 | 0.34 | 0.13 | 23.4% | 60% | mixed |
| `rank(fnd6_dxd4)` | TOP500 | 0.26 | 0.11 | 14.0% | 40% | bull-only |
| `rank(fnd6_dxd4 / close)` | TOP1000 | 0.23 | 0.09 | 11.7% | 80% | bull-only |
| `rank(fnd6_dxd4)` | TOP200 | 0.14 | 0.05 | 21.1% | 60% | bull-only |
| `rank(ts_delta(fnd6_dxd4, 5))` | TOP500 | 0.16 | 0.05 | 22.8% | 60% | weak |
| `rank(fnd6_dxd4)` | TOP1000 | 0.10 | 0.03 | 13.3% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_dd4: 0.982 (strongly positively correlated)
- fnd6_dxd3: 0.912 (strongly positively correlated)
- fnd6_dd3: 0.910 (strongly positively correlated)
- fnd6_dd2: 0.899 (strongly positively correlated)
- fnd6_dltr: 0.893 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_rd_exp_flag | analyst4 | -0.43 | 1.68 | +0.66 | -0.79 | yes |
| net_profit_adjusted_min_guidance | analyst4 | -0.31 | 1.53 | +0.59 | -0.87 | yes |
| fn_def_tax_assets_liab_net_a | fundamental2 | -0.31 | 1.49 | +0.56 | -0.61 | yes |
| anl4_epsr_flag | analyst4 | -0.29 | 1.71 | +0.53 | -0.80 | yes |
| rp_ess_revenue | news18 | -0.32 | 1.44 | +0.52 | -0.74 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
