---
field: rp_css_assets
dataset: news18
cluster: news18_balance_sheet_assets
coverage: 0.5
community_alphas: 1052
best_template: rank_neg_delta
best_sharpe: 0.63
best_fitness: 0.2
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 20
regime_profile: mixed
n_variations_with_pnl: 1
max_drawdown: 0.211
ann_vol: 0.159
hit_rate: 0.5085
rolling_sharpe_min: -0.755
rolling_sharpe_max: 2.893
negated_best_sharpe: 0.63
negated_best_template: rank_neg_delta
negated_best_fitness: 0.2
n_negated_sims: 4
direction_gap: -0.03
---
# rp_css_assets (news18)

*Composite sentiment score of assets news*

## Signal Profile
- `rank(rp_css_assets)`: S=0.58, F=0.15, T=141.8%, INFERIOR (TOP200)
- `rank(ts_delta(rp_css_assets, 5))`: S=-0.29, F=-0.07, T=142.2%, INFERIOR (TOP200)
- `-rank(rp_css_assets)`: S=0.45, F=0.09, T=158.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(rp_css_assets, 5))`: S=0.63, F=0.20, T=155.0%, INFERIOR (TOP3000)
- `-ts_zscore(rp_css_assets, 63)`: S=0.66, F=0.17, T=156.8%, INFERIOR (TOP3000)
- `ts_mean(rp_css_assets, 10)`: S=0.29, F=0.07, T=33.0%, INFERIOR (TOP3000)
- `rank(ts_rank(rp_css_assets, 22))`: S=-0.58, F=-0.12, T=159.7%, INFERIOR (TOP3000)
- `rank(-1 * rp_css_assets)`: S=0.41, F=0.07, T=167.2%, INFERIOR (TOP3000)
- `rank(-1 * rp_css_assets / close)`: S=0.24, F=0.03, T=168.5%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 19F/1P
- HIGH_TURNOVER: 19F/1P
- LOW_FITNESS: 20F/0P
- LOW_SHARPE: 20F/0P
- LOW_SUB_UNIVERSE_SHARPE: 10F/8P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.57, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=1.74 (strong), ret=+28.1%
  - 2020: S=0.81 (moderate), ret=+12.8%
  - 2021: S=0.47 (weak), ret=+6.7%
  - 2022: S=0.34 (weak), ret=+5.7%
  - 2023: S=-0.63 (negative), ret=-9.2%

## Risk & Drawdown
- Max drawdown: 21.10% over 242 days (not yet recovered, ongoing at window end)
- Annualized: return +9.0%, volatility 15.9% (fraction of booksize)
- Hit rate: 50.8% positive days
- Tail shape: skew +0.36, excess kurtosis +3.13

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.76, max 2.89, latest -0.70

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2023
Best month: +13.12%; worst month: -12.09%
Positive months: 64%

## Regime Profile
Regime profile: **mixed**
- Bull: S=-0.26
- Sideways: S=0.28
- Bear: S=1.77

## Negated Direction
Best negated: `rank(-1 * ts_delta(rp_css_assets, 5))` S=0.63, F=0.20, INFERIOR
Direction gap: -0.03 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * rp_css_assets)`: S=0.41, F=0.07, T=167.2%, INFERIOR (TOP3000)
- `rank(-1 * rp_css_assets / close)`: S=0.24, F=0.03, T=168.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(rp_css_assets, 5))`: S=0.63, F=0.20, T=155.0%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(rp_css_assets)` | TOP200 | 0.57 | 0.15 | 21.1% | 80% | mixed |

## Correlation Notes
Top correlates:
- rp_ess_assets: 0.200 (weakly positively correlated)
- rp_css_business: 0.098 (weakly positively correlated)
- fnd6_incorp: -0.097 (weakly negatively correlated)
- min_gross_income_guidance: 0.090 (weakly positively correlated)
- max_gross_income_guidance: 0.089 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, rank_value_norm, trade_when
