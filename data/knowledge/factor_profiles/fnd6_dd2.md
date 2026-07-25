---
field: fnd6_dd2
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 0.9
best_fitness: 0.59
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 8
max_drawdown: 0.0736
ann_vol: 0.0605
hit_rate: 0.502
rolling_sharpe_min: -0.874
rolling_sharpe_max: 2.802
top_merge_partner: anl4_rd_exp_flag
redundancy_cluster: 1
negated_best_sharpe: 0.62
negated_best_template: rank_neg_delta
negated_best_fitness: 0.37
n_negated_sims: 10
direction_gap: -0.28
---
# fnd6_dd2 (fundamental6)

*Debt Due in 2nd Year*

## Signal Profile
- `rank(fnd6_dd2)`: S=0.67, F=0.41, T=1.9%, INFERIOR (TOP3000)
- `rank(fnd6_dd2 / close)`: S=0.90, F=0.59, T=2.0%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_dd2, 5))`: S=0.45, F=0.20, T=41.8%, INFERIOR (TOP3000)
- `-rank(fnd6_dd2)`: S=-0.30, F=-0.14, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_dd2, 5))`: S=0.62, F=0.37, T=31.4%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_dd2, 63)`: S=0.04, F=0.01, T=17.2%, INFERIOR (TOP3000)
- `ts_mean(fnd6_dd2, 10)`: S=0.34, F=0.18, T=1.7%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_dd2, 22))`: S=-0.14, F=-0.04, T=19.6%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_dd2)`: S=-0.14, F=-0.05, T=2.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_dd2 / close)`: S=-0.21, F=-0.09, T=3.0%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 16F/13P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.89, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.75 (moderate), ret=+2.2%
  - 2020: S=0.15 (weak), ret=+0.9%
  - 2021: S=1.75 (strong), ret=+12.6%
  - 2022: S=1.35 (moderate), ret=+10.6%
  - 2023: S=-0.01 (negative), ret=-0.0%

## Risk & Drawdown
- Max drawdown: 7.36% over 597 days (not yet recovered, ongoing at window end)
- Annualized: return +5.4%, volatility 6.0% (fraction of booksize)
- Hit rate: 50.2% positive days
- Tail shape: skew +0.15, excess kurtosis +2.09

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.87, max 2.80, latest -0.09

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2023
Best month: +6.61%; worst month: -2.31%
Positive months: 63%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.84
- Sideways: S=0.89
- Bear: S=-1.52

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_dd2, 5))` S=0.62, F=0.37, INFERIOR
Direction gap: -0.28 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_dd2)`: S=-0.14, F=-0.05, T=2.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_dd2 / close)`: S=-0.21, F=-0.09, T=3.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_dd2, 5))`: S=0.62, F=0.37, T=31.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_dd2 / close)` | TOP3000 | 0.89 | 0.59 | 7.4% | 80% | bull-only |
| `rank(fnd6_dd2)` | TOP3000 | 0.65 | 0.41 | 12.3% | 60% | bull-only |
| `rank(fnd6_dd2 / close)` | TOP1000 | 0.39 | 0.21 | 11.2% | 40% | bull-only |
| `rank(ts_delta(fnd6_dd2, 5))` | TOP3000 | 0.44 | 0.20 | 50.5% | 60% | mixed |
| `rank(fnd6_dd2)` | TOP1000 | 0.29 | 0.14 | 19.3% | 40% | bull-only |
| `rank(fnd6_dd2 / close)` | TOP500 | 0.20 | 0.09 | 22.0% | 40% | bull-only |
| `rank(ts_delta(fnd6_dd2, 5))` | TOP200 | 0.21 | 0.08 | 26.7% | 60% | bull-only |
| `rank(fnd6_dd2)` | TOP500 | 0.13 | 0.05 | 27.7% | 40% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_dxd2: 0.979 (strongly positively correlated)
- fnd6_dd3: 0.941 (strongly positively correlated)
- fnd6_dxd3: 0.920 (strongly positively correlated)
- fnd6_dd4: 0.919 (strongly positively correlated)
- fnd6_dltr: 0.909 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_rd_exp_flag | analyst4 | -0.48 | 1.75 | +0.72 | -0.55 | yes |
| net_profit_adjusted_min_guidance | analyst4 | -0.30 | 1.52 | +0.58 | -0.85 | yes |
| rp_ess_revenue | news18 | -0.34 | 1.46 | +0.57 | -0.83 | yes |
| news_open_vol | news12 | -0.24 | 1.47 | +0.54 | -0.59 | yes |
| anl4_epsr_flag | analyst4 | -0.27 | 1.69 | +0.51 | -0.93 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
