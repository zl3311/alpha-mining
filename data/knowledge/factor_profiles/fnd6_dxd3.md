---
field: fnd6_dxd3
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 1.02
best_fitness: 0.69
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 6
max_drawdown: 0.0532
ann_vol: 0.0573
hit_rate: 0.5239
rolling_sharpe_min: -0.484
rolling_sharpe_max: 2.94
top_merge_partner: anl4_rd_exp_flag
redundancy_cluster: 1
negated_best_sharpe: 0.28
negated_best_template: rank_neg_delta
negated_best_fitness: 0.1
n_negated_sims: 10
direction_gap: -0.74
---
# fnd6_dxd3 (fundamental6)

*Debt (excl Capitalized Leases) - Due in 3rd Year*

## Signal Profile
- `rank(fnd6_dxd3)`: S=0.74, F=0.45, T=1.9%, INFERIOR (TOP3000)
- `rank(fnd6_dxd3 / close)`: S=1.02, F=0.69, T=2.1%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_dxd3, 5))`: S=0.20, F=0.06, T=41.6%, INFERIOR (TOP3000)
- `-rank(fnd6_dxd3)`: S=-0.25, F=-0.10, T=2.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_dxd3, 5))`: S=0.28, F=0.10, T=37.0%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_dxd3, 63)`: S=0.50, F=0.36, T=16.2%, INFERIOR (TOP3000)
- `ts_mean(fnd6_dxd3, 10)`: S=0.28, F=0.12, T=2.0%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_dxd3, 22))`: S=-0.48, F=-0.26, T=20.7%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_dxd3)`: S=-0.25, F=-0.10, T=2.6%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_dxd3 / close)`: S=-0.39, F=-0.19, T=2.8%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 15F/14P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 1.01, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.85 (moderate), ret=+2.6%
  - 2020: S=0.20 (weak), ret=+1.1%
  - 2021: S=1.38 (moderate), ret=+9.9%
  - 2022: S=1.84 (strong), ret=+13.1%
  - 2023: S=0.47 (weak), ret=+1.7%

## Risk & Drawdown
- Max drawdown: 5.32% over 104 days (recovered)
- Annualized: return +5.8%, volatility 5.7% (fraction of booksize)
- Hit rate: 52.4% positive days
- Tail shape: skew -0.04, excess kurtosis +2.11

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.48, max 2.94, latest 0.41

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +5.51%; worst month: -1.99%
Positive months: 66%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.69
- Sideways: S=1.53
- Bear: S=-1.43

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_dxd3, 5))` S=0.28, F=0.10, INFERIOR
Direction gap: -0.74 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_dxd3)`: S=-0.25, F=-0.10, T=2.6%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_dxd3 / close)`: S=-0.39, F=-0.19, T=2.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_dxd3, 5))`: S=0.28, F=0.10, T=37.0%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_dxd3 / close)` | TOP3000 | 1.01 | 0.69 | 5.3% | 100% | bull-only |
| `rank(fnd6_dxd3)` | TOP3000 | 0.73 | 0.45 | 11.6% | 80% | bull-only |
| `rank(fnd6_dxd3 / close)` | TOP1000 | 0.38 | 0.19 | 9.4% | 40% | bull-only |
| `rank(fnd6_dxd3)` | TOP1000 | 0.24 | 0.10 | 16.3% | 40% | bull-only |
| `rank(ts_delta(fnd6_dxd3, 5))` | TOP3000 | 0.20 | 0.06 | 36.5% | 40% | mixed |
| `rank(fnd6_dxd3 / close)` | TOP500 | 0.14 | 0.04 | 14.6% | 40% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_dd3: 0.983 (strongly positively correlated)
- fnd6_dd2: 0.920 (strongly positively correlated)
- fnd6_dxd2: 0.917 (strongly positively correlated)
- fnd6_dxd4: 0.912 (strongly positively correlated)
- fnd6_dd4: 0.910 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_rd_exp_flag | analyst4 | -0.45 | 1.76 | +0.74 | -0.77 | yes |
| net_profit_adjusted_min_guidance | analyst4 | -0.30 | 1.59 | +0.57 | -0.83 | yes |
| fn_def_tax_assets_liab_net_a | fundamental2 | -0.34 | 1.60 | +0.58 | -0.49 | yes |
| anl4_epsr_flag | analyst4 | -0.26 | 1.73 | +0.55 | -0.68 | yes |
| rank(scl12_buzz * (-1 * returns)) | socialmedia12 | -0.24 | 2.17 | +0.54 | -0.67 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
