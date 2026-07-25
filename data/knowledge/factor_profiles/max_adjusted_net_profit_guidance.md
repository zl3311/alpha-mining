---
field: max_adjusted_net_profit_guidance
dataset: analyst4
best_template: rank_delta
best_sharpe: 0.78
best_fitness: 0.36
best_universe: TOP200
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bear-only
n_variations_with_pnl: 4
max_drawdown: 0.1254
ann_vol: 0.0905
hit_rate: 0.5198
rolling_sharpe_min: -0.988
rolling_sharpe_max: 3.361
top_merge_partner: fnd6_txs
redundancy_cluster: 40
negated_best_sharpe: 0.19
negated_best_template: neg_rank_level
negated_best_fitness: 0.08
n_negated_sims: 10
direction_gap: -0.59
---
# max_adjusted_net_profit_guidance (analyst4)

*The maximum guidance value for adjusted net profit on an annual basis.*

## Signal Profile
- `rank(max_adjusted_net_profit_guidance)`: S=0.53, F=0.24, T=1.0%, INFERIOR (TOP3000)
- `rank(max_adjusted_net_profit_guidance / close)`: S=0.13, F=0.05, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_delta(max_adjusted_net_profit_guidance, 5))`: S=0.78, F=0.36, T=33.8%, INFERIOR (TOP200)
- `-rank(max_adjusted_net_profit_guidance)`: S=-0.18, F=-0.05, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(max_adjusted_net_profit_guidance, 5))`: S=-0.78, F=-0.36, T=33.8%, INFERIOR (TOP3000)
- `-ts_zscore(max_adjusted_net_profit_guidance, 63)`: S=0.39, F=0.13, T=21.6%, INFERIOR (TOP3000)
- `ts_mean(max_adjusted_net_profit_guidance, 10)`: S=0.19, F=0.06, T=2.0%, INFERIOR (TOP3000)
- `rank(ts_rank(max_adjusted_net_profit_guidance, 22))`: S=-0.08, F=-0.01, T=12.7%, INFERIOR (TOP3000)
- `rank(-1 * max_adjusted_net_profit_guidance)`: S=0.19, F=0.08, T=2.6%, INFERIOR (TOP3000)
- `rank(-1 * max_adjusted_net_profit_guidance / close)`: S=0.17, F=0.07, T=2.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 9F/23P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 12F/8P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.81, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.53 (moderate), ret=+3.8%
  - 2020: S=3.23 (strong), ret=+25.9%
  - 2021: S=-0.17 (negative), ret=-1.8%
  - 2022: S=0.12 (weak), ret=+1.1%
  - 2023: S=0.77 (moderate), ret=+6.8%

## Risk & Drawdown
- Max drawdown: 12.54% over 787 days (recovered)
- Annualized: return +7.3%, volatility 9.0% (fraction of booksize)
- Hit rate: 52.0% positive days
- Tail shape: skew +0.51, excess kurtosis +4.09

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.99, max 3.36, latest 0.88

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2021
Best month: +5.72%; worst month: -5.61%
Positive months: 58%

## Regime Profile
Regime profile: **bear-only**
- Bull: S=-0.59
- Sideways: S=0.53
- Bear: S=2.82

## Negated Direction
Best negated: `rank(-1 * max_adjusted_net_profit_guidance)` S=0.19, F=0.08, INFERIOR
Direction gap: -0.59 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * max_adjusted_net_profit_guidance)`: S=0.19, F=0.08, T=2.6%, INFERIOR (TOP3000)
- `rank(-1 * max_adjusted_net_profit_guidance / close)`: S=0.17, F=0.07, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(max_adjusted_net_profit_guidance, 5))`: S=-0.78, F=-0.36, T=33.8%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(max_adjusted_net_profit_guidance, 5))` | TOP200 | 0.81 | 0.36 | 12.5% | 80% | bear-only |
| `rank(max_adjusted_net_profit_guidance)` | TOP3000 | 0.54 | 0.24 | 8.6% | 60% | bull-only |
| `rank(max_adjusted_net_profit_guidance / close)` | TOP3000 | 0.13 | 0.05 | 48.4% | 60% | bull-only |
| `rank(max_adjusted_net_profit_guidance)` | TOP1000 | 0.18 | 0.05 | 14.9% | 40% | bull-only |

## Correlation Notes
Top correlates:
- max_net_profit_guidance: 0.982 (strongly positively correlated)
- net_profit_adjusted_min_guidance: 0.932 (strongly positively correlated)
- max_reported_pretax_income_guidance_2: 0.924 (strongly positively correlated)
- min_tangible_book_value_per_share_guidance_2: 0.923 (strongly positively correlated)
- tangible_book_value_per_share_max_guidance: 0.923 (strongly positively correlated)

Redundancy cluster #40: 20 similar fields, mean |rho| 0.904 (representative: net_profit_adjusted_min_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| fnd6_txs | fundamental6 | -0.39 | 1.49 | +0.65 | -0.93 | yes |
| implied_volatility_mean_skew_150 | option8 | -0.39 | 1.50 | +0.64 | -0.92 | yes |
| fnd6_dn | fundamental6 | -0.40 | 1.53 | +0.64 | -0.85 | yes |
| fnd6_xrent | fundamental6 | -0.37 | 1.55 | +0.61 | -0.97 | yes |
| fnd6_newqv1300_xoprq | fundamental6 | -0.37 | 1.45 | +0.61 | -0.97 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
