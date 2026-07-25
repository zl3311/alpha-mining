---
field: rp_ess_assets
dataset: news18
best_template: ts_mean
best_sharpe: 0.6
best_fitness: 0.2
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 20
regime_profile: mixed
n_variations_with_pnl: 3
max_drawdown: 0.2691
ann_vol: 0.1707
hit_rate: 0.5093
rolling_sharpe_min: -1.451
rolling_sharpe_max: 2.65
negated_best_sharpe: 0.3
negated_best_template: neg_rank_level
negated_best_fitness: 0.05
n_negated_sims: 4
direction_gap: -0.3
---
# rp_ess_assets (news18)

*Event sentiment score of assets news*

## Signal Profile
- `rank(rp_ess_assets)`: S=0.67, F=0.19, T=136.1%, INFERIOR (TOP200)
- `rank(ts_delta(rp_ess_assets, 5))`: S=0.11, F=0.02, T=141.2%, INFERIOR (TOP200)
- `-rank(rp_ess_assets)`: S=-0.18, F=-0.02, T=151.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(rp_ess_assets, 5))`: S=0.08, F=0.01, T=153.1%, INFERIOR (TOP3000)
- `-ts_zscore(rp_ess_assets, 63)`: S=0.09, F=0.01, T=151.4%, INFERIOR (TOP3000)
- `ts_mean(rp_ess_assets, 10)`: S=0.60, F=0.20, T=29.6%, INFERIOR (TOP3000)
- `rank(ts_rank(rp_ess_assets, 22))`: S=-0.21, F=-0.03, T=156.8%, INFERIOR (TOP3000)
- `rank(-1 * rp_ess_assets)`: S=0.30, F=0.05, T=159.1%, INFERIOR (TOP3000)
- `rank(-1 * rp_ess_assets / close)`: S=0.04, F=0.00, T=160.9%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 19F/1P
- HIGH_TURNOVER: 19F/1P
- LOW_FITNESS: 20F/0P
- LOW_SHARPE: 20F/0P
- LOW_SUB_UNIVERSE_SHARPE: 6F/12P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.66, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=1.06 (moderate), ret=+17.0%
  - 2020: S=2.42 (strong), ret=+43.6%
  - 2021: S=-0.76 (negative), ret=-11.8%
  - 2022: S=-0.07 (negative), ret=-1.4%
  - 2023: S=0.56 (moderate), ret=+8.1%

## Risk & Drawdown
- Max drawdown: 26.91% over 1060 days (not yet recovered, ongoing at window end)
- Annualized: return +11.3%, volatility 17.1% (fraction of booksize)
- Hit rate: 50.9% positive days
- Tail shape: skew +0.22, excess kurtosis +2.56

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.45, max 2.65, latest 0.60

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2021
Best month: +19.10%; worst month: -14.73%
Positive months: 51%

## Regime Profile
Regime profile: **mixed**
- Bull: S=-0.31
- Sideways: S=0.34
- Bear: S=1.99

## Negated Direction
Best negated: `rank(-1 * rp_ess_assets)` S=0.30, F=0.05, INFERIOR
Direction gap: -0.30 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * rp_ess_assets)`: S=0.30, F=0.05, T=159.1%, INFERIOR (TOP3000)
- `rank(-1 * rp_ess_assets / close)`: S=0.04, F=0.00, T=160.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(rp_ess_assets, 5))`: S=0.08, F=0.01, T=153.1%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(rp_ess_assets)` | TOP200 | 0.66 | 0.19 | 26.9% | 60% | mixed |
| `rank(rp_ess_assets)` | TOP500 | 0.30 | 0.05 | 31.2% | 60% | mixed |
| `rank(ts_delta(rp_ess_assets, 5))` | TOP200 | 0.11 | 0.02 | 58.0% | 40% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_incorp: -0.295 (weakly negatively correlated)
- est_cashflow_fin: 0.293 (weakly positively correlated)
- anl4_rd_exp_flag: 0.292 (weakly positively correlated)
- fnd6_newa2v1300_spi: 0.283 (weakly positively correlated)
- fn_accum_oth_income_loss_net_of_tax_a: 0.279 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, rank_value_norm, trade_when
