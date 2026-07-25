---
field: fnd6_dxd2
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 0.86
best_fitness: 0.54
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 8
max_drawdown: 0.0694
ann_vol: 0.057
hit_rate: 0.5101
rolling_sharpe_min: -0.576
rolling_sharpe_max: 2.897
top_merge_partner: anl4_rd_exp_flag
redundancy_cluster: 1
negated_best_sharpe: 0.36
negated_best_template: rank_neg_delta
negated_best_fitness: 0.18
n_negated_sims: 10
direction_gap: -0.5
---
# fnd6_dxd2 (fundamental6)

*Debt (excl Capitalized Leases) - Due in 2nd Year*

## Signal Profile
- `rank(fnd6_dxd2)`: S=0.66, F=0.38, T=1.9%, INFERIOR (TOP3000)
- `rank(fnd6_dxd2 / close)`: S=0.86, F=0.54, T=2.0%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_dxd2, 5))`: S=0.44, F=0.19, T=40.9%, INFERIOR (TOP3000)
- `-rank(fnd6_dxd2)`: S=-0.32, F=-0.15, T=2.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_dxd2, 5))`: S=0.36, F=0.18, T=28.5%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_dxd2, 22)`: S=-0.09, F=-0.04, T=16.0%, INFERIOR (TOP3000)
- `ts_mean(fnd6_dxd2, 10)`: S=0.24, F=0.10, T=1.9%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_dxd2, 22))`: S=-0.11, F=-0.03, T=20.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_dxd2)`: S=-0.09, F=-0.02, T=2.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_dxd2 / close)`: S=-0.19, F=-0.07, T=3.0%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 17F/12P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.85, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.75 (moderate), ret=+2.2%
  - 2020: S=-0.12 (negative), ret=-0.7%
  - 2021: S=1.88 (strong), ret=+11.9%
  - 2022: S=1.34 (moderate), ret=+10.2%
  - 2023: S=0.00 (weak), ret=+0.0%

## Risk & Drawdown
- Max drawdown: 6.94% over 597 days (not yet recovered, ongoing at window end)
- Annualized: return +4.8%, volatility 5.7% (fraction of booksize)
- Hit rate: 51.0% positive days
- Tail shape: skew +0.12, excess kurtosis +1.60

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.58, max 2.90, latest -0.07

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2020
Best month: +5.72%; worst month: -2.33%
Positive months: 59%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.87
- Sideways: S=0.96
- Bear: S=-1.63

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_dxd2, 5))` S=0.36, F=0.18, INFERIOR
Direction gap: -0.50 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_dxd2)`: S=-0.09, F=-0.02, T=2.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_dxd2 / close)`: S=-0.19, F=-0.07, T=3.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_dxd2, 5))`: S=0.36, F=0.18, T=28.5%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_dxd2 / close)` | TOP3000 | 0.85 | 0.54 | 6.9% | 80% | bull-only |
| `rank(fnd6_dxd2)` | TOP3000 | 0.65 | 0.38 | 10.3% | 60% | bull-only |
| `rank(fnd6_dxd2 / close)` | TOP1000 | 0.45 | 0.24 | 9.1% | 60% | bull-only |
| `rank(ts_delta(fnd6_dxd2, 5))` | TOP200 | 0.34 | 0.19 | 21.9% | 80% | mixed |
| `rank(ts_delta(fnd6_dxd2, 5))` | TOP3000 | 0.44 | 0.19 | 37.3% | 60% | mixed |
| `rank(fnd6_dxd2)` | TOP1000 | 0.32 | 0.15 | 16.7% | 40% | bull-only |
| `rank(fnd6_dxd2 / close)` | TOP500 | 0.18 | 0.07 | 22.8% | 40% | bull-only |
| `rank(fnd6_dxd2)` | TOP500 | 0.08 | 0.02 | 28.6% | 40% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_dd2: 0.979 (strongly positively correlated)
- fnd6_dxd3: 0.917 (strongly positively correlated)
- fnd6_dd3: 0.914 (strongly positively correlated)
- net_debt_amount: 0.893 (strongly positively correlated)
- fnd6_dxd4: 0.892 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_rd_exp_flag | analyst4 | -0.48 | 1.70 | +0.67 | -0.62 | yes |
| net_profit_adjusted_min_guidance | analyst4 | -0.30 | 1.48 | +0.54 | -0.92 | yes |
| news_open_vol | news12 | -0.28 | 1.48 | +0.55 | -0.59 | yes |
| rp_ess_revenue | news18 | -0.33 | 1.41 | +0.52 | -0.89 | yes |
| max_adjusted_net_profit_guidance | analyst4 | -0.33 | 1.35 | +0.50 | -0.78 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
