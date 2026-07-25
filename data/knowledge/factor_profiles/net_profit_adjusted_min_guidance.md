---
field: net_profit_adjusted_min_guidance
dataset: analyst4
best_template: rank_delta
best_sharpe: 0.91
best_fitness: 0.44
best_universe: TOP200
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 5
max_drawdown: 0.1219
ann_vol: 0.0856
hit_rate: 0.5287
rolling_sharpe_min: -1.105
rolling_sharpe_max: 3.225
top_merge_partner: fnd6_dn
redundancy_cluster: 40
negated_best_sharpe: 0.18
negated_best_template: neg_rank_level
negated_best_fitness: 0.08
n_negated_sims: 10
direction_gap: -0.73
---
# net_profit_adjusted_min_guidance (analyst4)

*The minimum guidance value for adjusted net profit on an annual basis.*

## Signal Profile
- `rank(net_profit_adjusted_min_guidance)`: S=0.53, F=0.24, T=1.0%, INFERIOR (TOP3000)
- `rank(net_profit_adjusted_min_guidance / close)`: S=0.13, F=0.05, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_delta(net_profit_adjusted_min_guidance, 5))`: S=0.91, F=0.44, T=33.7%, INFERIOR (TOP200)
- `-rank(net_profit_adjusted_min_guidance)`: S=-0.18, F=-0.05, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(net_profit_adjusted_min_guidance, 5))`: S=-0.91, F=-0.44, T=33.7%, INFERIOR (TOP3000)
- `-ts_zscore(net_profit_adjusted_min_guidance, 63)`: S=0.54, F=0.21, T=20.4%, INFERIOR (TOP3000)
- `ts_mean(net_profit_adjusted_min_guidance, 10)`: S=0.24, F=0.08, T=1.8%, INFERIOR (TOP3000)
- `rank(ts_rank(net_profit_adjusted_min_guidance, 22))`: S=-0.03, F=0.00, T=12.7%, INFERIOR (TOP3000)
- `rank(-1 * net_profit_adjusted_min_guidance)`: S=0.18, F=0.08, T=2.6%, INFERIOR (TOP3000)
- `rank(-1 * net_profit_adjusted_min_guidance / close)`: S=0.16, F=0.06, T=2.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 9F/23P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 12F/8P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.94, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.81 (moderate), ret=+5.8%
  - 2020: S=3.09 (strong), ret=+24.0%
  - 2021: S=-0.49 (negative), ret=-4.8%
  - 2022: S=0.35 (weak), ret=+3.1%
  - 2023: S=1.43 (moderate), ret=+11.4%

## Risk & Drawdown
- Max drawdown: 12.19% over 717 days (recovered)
- Annualized: return +8.1%, volatility 8.6% (fraction of booksize)
- Hit rate: 52.9% positive days
- Tail shape: skew +0.35, excess kurtosis +3.84

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.10, max 3.23, latest 1.54

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2021
Best month: +5.84%; worst month: -5.46%
Positive months: 61%

## Regime Profile
Regime profile: **mixed**
- Bull: S=-0.39
- Sideways: S=0.37
- Bear: S=3.21

## Negated Direction
Best negated: `rank(-1 * net_profit_adjusted_min_guidance)` S=0.18, F=0.08, INFERIOR
Direction gap: -0.73 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * net_profit_adjusted_min_guidance)`: S=0.18, F=0.08, T=2.6%, INFERIOR (TOP3000)
- `rank(-1 * net_profit_adjusted_min_guidance / close)`: S=0.16, F=0.06, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(net_profit_adjusted_min_guidance, 5))`: S=-0.91, F=-0.44, T=33.7%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(net_profit_adjusted_min_guidance, 5))` | TOP200 | 0.94 | 0.44 | 12.2% | 80% | mixed |
| `rank(net_profit_adjusted_min_guidance)` | TOP3000 | 0.54 | 0.24 | 8.5% | 60% | bull-only |
| `rank(net_profit_adjusted_min_guidance / close)` | TOP3000 | 0.13 | 0.05 | 48.1% | 60% | bull-only |
| `rank(net_profit_adjusted_min_guidance)` | TOP1000 | 0.19 | 0.05 | 14.6% | 40% | bull-only |
| `rank(ts_delta(net_profit_adjusted_min_guidance, 5))` | TOP3000 | 0.19 | 0.03 | 13.9% | 40% | bear-only |

## Correlation Notes
Top correlates:
- min_net_profit_guidance: 0.969 (strongly positively correlated)
- max_adjusted_net_profit_guidance: 0.932 (strongly positively correlated)
- max_net_profit_guidance: 0.911 (strongly positively correlated)
- max_reported_pretax_income_guidance_2: 0.823 (strongly positively correlated)
- min_tangible_book_value_per_share_guidance_2: 0.820 (strongly positively correlated)

Redundancy cluster #40: 20 similar fields, mean |rho| 0.904 (representative). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| fnd6_dn | fundamental6 | -0.36 | 1.62 | +0.67 | -0.92 | yes |
| fnd6_xrent | fundamental6 | -0.32 | 1.61 | +0.67 | -0.92 | yes |
| implied_volatility_mean_skew_180 | option8 | -0.32 | 1.71 | +0.65 | -0.77 | yes |
| fnd6_mrc2 | fundamental6 | -0.31 | 1.57 | +0.63 | -0.90 | yes |
| implied_volatility_mean_skew_270 | option8 | -0.32 | 1.67 | +0.64 | -0.76 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
