---
field: fnd6_idit
dataset: fundamental6
best_template: rank_delta
best_sharpe: 1.1
best_fitness: 0.79
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: all-weather
n_variations_with_pnl: 6
max_drawdown: 0.2029
ann_vol: 0.1661
hit_rate: 0.5182
rolling_sharpe_min: -0.848
rolling_sharpe_max: 3.189
top_merge_partner: fn_payments_to_acquire_businesses_net_of_cash_acquired_a
negated_best_sharpe: 0.26
negated_best_template: neg_rank_level
negated_best_fitness: 0.15
n_negated_sims: 10
direction_gap: -0.84
---
# fnd6_idit (fundamental6)

*Interest and Related Income - Total*

## Signal Profile
- `rank(fnd6_idit)`: S=0.40, F=0.20, T=1.6%, INFERIOR (TOP3000)
- `rank(fnd6_idit / close)`: S=0.63, F=0.34, T=1.9%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_idit, 5))`: S=1.10, F=0.79, T=35.6%, INFERIOR (TOP3000)
- `-rank(fnd6_idit)`: S=0.02, F=0.00, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_idit, 5))`: S=0.25, F=0.12, T=24.8%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_idit, 22)`: S=0.42, F=0.31, T=18.6%, INFERIOR (TOP3000)
- `ts_mean(fnd6_idit, 10)`: S=-0.14, F=-0.05, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_idit, 22))`: S=0.34, F=0.17, T=17.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_idit)`: S=0.26, F=0.15, T=3.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_idit / close)`: S=0.02, F=0.00, T=3.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 12F/8P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 1.07, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.39 (weak), ret=+5.5%
  - 2020: S=1.36 (moderate), ret=+24.1%
  - 2021: S=1.93 (strong), ret=+31.2%
  - 2022: S=1.01 (moderate), ret=+17.0%
  - 2023: S=0.57 (moderate), ret=+9.1%

## Risk & Drawdown
- Max drawdown: 20.29% over 437 days (recovered)
- Annualized: return +17.7%, volatility 16.6% (fraction of booksize)
- Hit rate: 51.8% positive days
- Tail shape: skew +0.27, excess kurtosis +4.12

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.85, max 3.19, latest 0.65

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2019
Best month: +13.76%; worst month: -9.73%
Positive months: 58%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=1.15
- Sideways: S=0.80
- Bear: S=1.23

## Negated Direction
Best negated: `rank(-1 * fnd6_idit)` S=0.26, F=0.15, INFERIOR
Direction gap: -0.84 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_idit)`: S=0.26, F=0.15, T=3.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_idit / close)`: S=0.02, F=0.00, T=3.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_idit, 5))`: S=0.25, F=0.12, T=24.8%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_idit, 5))` | TOP3000 | 1.07 | 0.79 | 20.3% | 100% | all-weather |
| `rank(fnd6_idit / close)` | TOP3000 | 0.63 | 0.34 | 7.5% | 100% | bull-only |
| `rank(ts_delta(fnd6_idit, 5))` | TOP200 | 0.40 | 0.25 | 44.6% | 80% | bull-only |
| `rank(fnd6_idit)` | TOP3000 | 0.40 | 0.20 | 28.2% | 80% | bull-only |
| `rank(ts_delta(fnd6_idit, 5))` | TOP500 | 0.35 | 0.17 | 39.3% | 60% | mixed |
| `rank(ts_delta(fnd6_idit, 5))` | TOP1000 | 0.33 | 0.14 | 42.4% | 40% | mixed |

## Correlation Notes
Top correlates:
- anl4_tot_gw_ft: -0.141 (weakly negatively correlated)
- anl4_cff_flag: -0.129 (weakly negatively correlated)
- anl4_fcfps_flag: -0.129 (weakly negatively correlated)
- anl4_cfi_flag: -0.126 (weakly negatively correlated)
- anl4_bvps_flag: -0.125 (weakly negatively correlated)

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| fn_payments_to_acquire_businesses_net_of_cash_acquired_a | fundamental2 | -0.06 | 1.68 | +0.45 | -0.73 | yes |
| news_open_gap | news12 | -0.07 | 1.65 | +0.47 | -0.37 | yes |
| anl4_cff_flag | analyst4 | -0.13 | 1.54 | +0.42 | -0.64 | yes |
| anl4_cfi_flag | analyst_revision | -0.13 | 1.57 | +0.40 | -0.69 | yes |
| sales_ps | fundamental_value | -0.07 | 1.53 | +0.46 | +0.54 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
