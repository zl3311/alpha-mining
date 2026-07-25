---
field: fnd6_dd4
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 0.98
best_fitness: 0.68
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 10
max_drawdown: 0.0564
ann_vol: 0.0614
hit_rate: 0.5085
rolling_sharpe_min: -0.762
rolling_sharpe_max: 2.739
top_merge_partner: anl4_rd_exp_flag
redundancy_cluster: 1
negated_best_sharpe: 0.38
negated_best_template: rank_neg_delta
negated_best_fitness: 0.18
n_negated_sims: 10
direction_gap: -0.6
---
# fnd6_dd4 (fundamental6)

*Debt Due in 4th Year*

## Signal Profile
- `rank(fnd6_dd4)`: S=0.72, F=0.45, T=1.9%, INFERIOR (TOP3000)
- `rank(fnd6_dd4 / close)`: S=0.98, F=0.68, T=2.1%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_dd4, 5))`: S=0.24, F=0.10, T=24.0%, INFERIOR (TOP200)
- `-rank(fnd6_dd4)`: S=-0.21, F=-0.08, T=2.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_dd4, 5))`: S=0.38, F=0.18, T=32.1%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_dd4, 22)`: S=0.37, F=0.22, T=18.9%, INFERIOR (TOP3000)
- `ts_mean(fnd6_dd4, 10)`: S=0.31, F=0.14, T=1.8%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_dd4, 22))`: S=-0.60, F=-0.36, T=20.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_dd4)`: S=-0.28, F=-0.13, T=2.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_dd4 / close)`: S=-0.51, F=-0.31, T=3.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 12F/17P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.98, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=1.44 (moderate), ret=+4.5%
  - 2020: S=0.14 (weak), ret=+0.9%
  - 2021: S=1.56 (strong), ret=+12.2%
  - 2022: S=1.50 (strong), ret=+10.7%
  - 2023: S=0.29 (weak), ret=+1.0%

## Risk & Drawdown
- Max drawdown: 5.64% over 115 days (recovered)
- Annualized: return +6.0%, volatility 6.1% (fraction of booksize)
- Hit rate: 50.8% positive days
- Tail shape: skew +0.12, excess kurtosis +2.57

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.76, max 2.74, latest 0.18

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2020
Best month: +5.95%; worst month: -2.19%
Positive months: 64%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.67
- Sideways: S=1.08
- Bear: S=-1.07

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_dd4, 5))` S=0.38, F=0.18, INFERIOR
Direction gap: -0.60 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_dd4)`: S=-0.28, F=-0.13, T=2.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_dd4 / close)`: S=-0.51, F=-0.31, T=3.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_dd4, 5))`: S=0.38, F=0.18, T=32.1%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_dd4 / close)` | TOP3000 | 0.98 | 0.68 | 5.6% | 100% | bull-only |
| `rank(fnd6_dd4)` | TOP3000 | 0.71 | 0.45 | 12.2% | 60% | bull-only |
| `rank(fnd6_dd4 / close)` | TOP500 | 0.52 | 0.31 | 11.4% | 60% | bull-only |
| `rank(fnd6_dd4 / close)` | TOP1000 | 0.34 | 0.16 | 10.5% | 80% | bull-only |
| `rank(fnd6_dd4)` | TOP500 | 0.28 | 0.13 | 13.9% | 40% | bull-only |
| `rank(ts_delta(fnd6_dd4, 5))` | TOP200 | 0.24 | 0.10 | 31.4% | 60% | weak |
| `rank(fnd6_dd4)` | TOP1000 | 0.20 | 0.08 | 13.2% | 60% | bull-only |
| `rank(fnd6_dd4 / close)` | TOP200 | 0.16 | 0.06 | 21.8% | 60% | bull-only |
| `rank(ts_delta(fnd6_dd4, 5))` | TOP3000 | 0.13 | 0.03 | 32.8% | 60% | weak |
| `rank(ts_delta(fnd6_dd4, 5))` | TOP1000 | 0.12 | 0.02 | 32.9% | 60% | mixed |

## Correlation Notes
Top correlates:
- fnd6_dxd4: 0.982 (strongly positively correlated)
- fnd6_dd3: 0.933 (strongly positively correlated)
- fnd6_dd2: 0.919 (strongly positively correlated)
- fnd6_dd5: 0.911 (strongly positively correlated)
- fnd6_dxd3: 0.910 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_rd_exp_flag | analyst4 | -0.44 | 1.76 | +0.74 | -0.79 | yes |
| net_profit_adjusted_min_guidance | analyst4 | -0.31 | 1.60 | +0.62 | -0.88 | yes |
| anl4_epsr_flag | analyst4 | -0.28 | 1.75 | +0.57 | -0.82 | yes |
| fn_def_tax_assets_liab_net_a | fundamental2 | -0.32 | 1.52 | +0.54 | -0.60 | yes |
| rp_ess_revenue | news18 | -0.32 | 1.50 | +0.52 | -0.76 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
