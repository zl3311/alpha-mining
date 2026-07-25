---
field: fnd6_dd1
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 1.02
best_fitness: 0.74
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 6
max_drawdown: 0.0774
ann_vol: 0.0648
hit_rate: 0.4939
rolling_sharpe_min: -1.274
rolling_sharpe_max: 2.691
top_merge_partner: anl4_epsr_flag
redundancy_cluster: 1
negated_best_sharpe: 0.21
negated_best_template: neg_rank_level
negated_best_fitness: 0.1
n_negated_sims: 10
direction_gap: -0.81
---
# fnd6_dd1 (fundamental6)

*Long-Term Debt Due in 1 Year*

## Signal Profile
- `rank(fnd6_dd1)`: S=0.74, F=0.54, T=1.4%, INFERIOR (TOP3000)
- `rank(fnd6_dd1 / close)`: S=1.02, F=0.74, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_dd1, 5))`: S=0.11, F=0.03, T=34.2%, INFERIOR (TOP500)
- `-rank(fnd6_dd1)`: S=-0.28, F=-0.14, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_dd1, 5))`: S=-0.01, F=0.00, T=36.4%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_dd1, 63)`: S=0.31, F=0.15, T=18.6%, INFERIOR (TOP3000)
- `ts_mean(fnd6_dd1, 10)`: S=0.19, F=0.07, T=1.7%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_dd1, 22))`: S=0.67, F=0.40, T=15.6%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_dd1)`: S=0.21, F=0.10, T=2.7%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_dd1 / close)`: S=0.13, F=0.05, T=2.8%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 12F/8P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 1.02, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.83 (moderate), ret=+2.1%
  - 2020: S=0.48 (weak), ret=+3.6%
  - 2021: S=1.75 (strong), ret=+14.6%
  - 2022: S=1.45 (moderate), ret=+10.0%
  - 2023: S=0.45 (weak), ret=+2.0%

## Risk & Drawdown
- Max drawdown: 7.74% over 597 days (not yet recovered, ongoing at window end)
- Annualized: return +6.6%, volatility 6.5% (fraction of booksize)
- Hit rate: 49.4% positive days
- Tail shape: skew +0.55, excess kurtosis +3.08

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.27, max 2.69, latest 0.47

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2023
Best month: +7.67%; worst month: -2.82%
Positive months: 58%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.90
- Sideways: S=0.64
- Bear: S=-0.90

## Negated Direction
Best negated: `rank(-1 * fnd6_dd1)` S=0.21, F=0.10, INFERIOR
Direction gap: -0.81 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_dd1)`: S=0.21, F=0.10, T=2.7%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_dd1 / close)`: S=0.13, F=0.05, T=2.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_dd1, 5))`: S=-0.01, F=0.00, T=36.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_dd1 / close)` | TOP3000 | 1.02 | 0.74 | 7.7% | 100% | bull-only |
| `rank(fnd6_dd1)` | TOP3000 | 0.73 | 0.54 | 19.1% | 80% | bull-only |
| `rank(fnd6_dd1 / close)` | TOP1000 | 0.50 | 0.30 | 12.6% | 60% | bull-only |
| `rank(fnd6_dd1)` | TOP1000 | 0.27 | 0.14 | 24.1% | 60% | bull-only |
| `rank(fnd6_dd1 / close)` | TOP500 | 0.12 | 0.04 | 19.6% | 40% | bull-only |
| `rank(ts_delta(fnd6_dd1, 5))` | TOP500 | 0.12 | 0.03 | 50.5% | 60% | mixed |

## Correlation Notes
Top correlates:
- fnd6_newa1v1300_dlc: 0.970 (strongly positively correlated)
- fnd6_newa1v1300_lt: 0.953 (strongly positively correlated)
- fnd6_mfma1_dpc: 0.951 (strongly positively correlated)
- fnd6_newa1v1300_dpc: 0.951 (strongly positively correlated)
- fnd6_dd1q: 0.950 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_epsr_flag | analyst4 | -0.35 | 1.88 | +0.70 | -0.91 | yes |
| anl4_rd_exp_flag | analyst4 | -0.29 | 1.64 | +0.61 | -0.54 | yes |
| rp_ess_revenue | news18 | -0.36 | 1.59 | +0.57 | -0.84 | yes |
| net_profit_adjusted_min_guidance | analyst4 | -0.19 | 1.51 | +0.50 | -0.86 | yes |
| fn_def_tax_assets_liab_net_a | fundamental2 | -0.25 | 1.49 | +0.47 | -0.27 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
