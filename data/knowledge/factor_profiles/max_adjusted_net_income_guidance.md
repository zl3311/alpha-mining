---
field: max_adjusted_net_income_guidance
dataset: analyst4
best_template: rank_level
best_sharpe: 1.49
best_fitness: 1.1
best_universe: TOP3000
grade: AVERAGE
submittability: blocked_LOW_TURNOVER
n_sims: 32
regime_profile: all-weather
n_variations_with_pnl: 6
max_drawdown: 0.0394
ann_vol: 0.0457
hit_rate: 0.5182
rolling_sharpe_min: -0.996
rolling_sharpe_max: 4.058
top_merge_partner: rank(scl12_buzz * (-1 * returns))
redundancy_cluster: 7
negated_best_sharpe: 0.43
negated_best_template: neg_rank_level
negated_best_fitness: 0.3
n_negated_sims: 10
direction_gap: -1.06
---
# max_adjusted_net_income_guidance (analyst4)

*The maximum guidance value for Adjusted net income.*

## Signal Profile
- `rank(max_adjusted_net_income_guidance)`: S=1.49, F=1.10, T=1.0%, AVERAGE (TOP3000)
- `rank(max_adjusted_net_income_guidance / close)`: S=0.21, F=0.09, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_delta(max_adjusted_net_income_guidance, 5))`: S=0.70, F=0.30, T=33.8%, INFERIOR (TOP200)
- `-rank(max_adjusted_net_income_guidance)`: S=-0.93, F=-0.62, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(max_adjusted_net_income_guidance, 5))`: S=-0.70, F=-0.30, T=33.8%, INFERIOR (TOP3000)
- `ts_zscore(max_adjusted_net_income_guidance, 22)`: S=0.11, F=0.02, T=44.1%, INFERIOR (TOP3000)
- `ts_mean(max_adjusted_net_income_guidance, 10)`: S=0.90, F=0.60, T=1.8%, INFERIOR (TOP3000)
- `rank(ts_rank(max_adjusted_net_income_guidance, 22))`: S=-0.11, F=-0.02, T=12.6%, INFERIOR (TOP3000)
- `rank(-1 * max_adjusted_net_income_guidance)`: S=0.43, F=0.30, T=2.8%, INFERIOR (TOP3000)
- `rank(-1 * max_adjusted_net_income_guidance / close)`: S=0.28, F=0.14, T=2.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 9F/23P
- LOW_FITNESS: 31F/1P
- LOW_SHARPE: 31F/1P
- LOW_SUB_UNIVERSE_SHARPE: 14F/6P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 1.49, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.03 (weak), ret=+0.1%
  - 2020: S=1.64 (strong), ret=+7.1%
  - 2021: S=2.98 (strong), ret=+16.5%
  - 2022: S=1.87 (strong), ret=+9.5%
  - 2023: S=0.05 (weak), ret=+0.2%

## Risk & Drawdown
- Max drawdown: 3.94% over 478 days (recovered)
- Annualized: return +6.8%, volatility 4.6% (fraction of booksize)
- Hit rate: 51.8% positive days
- Tail shape: skew +0.51, excess kurtosis +3.77

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.00, max 4.06, latest 0.04

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2019
Best month: +3.93%; worst month: -2.21%
Positive months: 66%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=2.17
- Sideways: S=0.80
- Bear: S=1.42

## Negated Direction
Best negated: `rank(-1 * max_adjusted_net_income_guidance)` S=0.43, F=0.30, INFERIOR
Direction gap: -1.06 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * max_adjusted_net_income_guidance)`: S=0.43, F=0.30, T=2.8%, INFERIOR (TOP3000)
- `rank(-1 * max_adjusted_net_income_guidance / close)`: S=0.28, F=0.14, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(max_adjusted_net_income_guidance, 5))`: S=-0.70, F=-0.30, T=33.8%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(max_adjusted_net_income_guidance)` | TOP3000 | 1.49 | 1.10 | 3.9% | 100% | all-weather |
| `rank(max_adjusted_net_income_guidance)` | TOP1000 | 0.94 | 0.62 | 4.8% | 80% | mixed |
| `rank(ts_delta(max_adjusted_net_income_guidance, 5))` | TOP200 | 0.71 | 0.30 | 12.4% | 60% | bear-only |
| `rank(max_adjusted_net_income_guidance)` | TOP500 | 0.30 | 0.12 | 16.8% | 60% | mixed |
| `rank(max_adjusted_net_income_guidance / close)` | TOP3000 | 0.21 | 0.09 | 44.9% | 60% | bull-only |
| `rank(max_adjusted_net_income_guidance / close)` | TOP1000 | 0.15 | 0.05 | 33.5% | 60% | bull-only |

## Correlation Notes
Top correlates:
- max_net_income_guidance: 0.794 (strongly positively correlated)
- min_net_income_guidance: 0.792 (strongly positively correlated)
- eps_min_guidance_quarterly: 0.532 (moderately positively correlated)
- eps_max_guidance_quarterly: 0.532 (moderately positively correlated)
- max_reported_eps_guidance: 0.502 (moderately positively correlated)

Redundancy cluster #7: 3 similar fields, mean |rho| 0.862 (representative). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| rank(scl12_buzz * (-1 * returns)) | socialmedia12 | -0.21 | 2.33 | +0.70 | -0.29 | yes |
| implied_volatility_call_360 | option8 | -0.04 | 2.20 | +0.63 | +0.87 | yes |
| implied_volatility_call_180 | option8 | -0.02 | 2.12 | +0.63 | +0.80 | yes |
| implied_volatility_mean_720 | option8 | -0.02 | 2.13 | +0.63 | +0.90 | yes |
| implied_volatility_call_720 | option8 | -0.04 | 2.21 | +0.63 | +0.97 | yes |

## Actionability
Cataloged as active factor but not yet in submitted book.
Blocked by LOW_TURNOVER. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
