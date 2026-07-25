---
field: max_net_income_guidance
dataset: analyst4
best_template: rank_level
best_sharpe: 1.32
best_fitness: 0.76
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_FITNESS
n_sims: 32
regime_profile: all-weather
n_variations_with_pnl: 6
max_drawdown: 0.0364
ann_vol: 0.0317
hit_rate: 0.5134
rolling_sharpe_min: -1.033
rolling_sharpe_max: 3.906
top_merge_partner: fnd6_newqv1300_drltq
redundancy_cluster: 7
negated_best_sharpe: 0.34
negated_best_template: neg_rank_level
negated_best_fitness: 0.18
n_negated_sims: 10
direction_gap: -0.98
---
# max_net_income_guidance (analyst4)

*The maximum guidance value for net profit.*

## Signal Profile
- `rank(max_net_income_guidance)`: S=1.32, F=0.76, T=0.9%, INFERIOR (TOP3000)
- `rank(max_net_income_guidance / close)`: S=0.24, F=0.11, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_delta(max_net_income_guidance, 5))`: S=0.66, F=0.29, T=33.5%, INFERIOR (TOP200)
- `-rank(max_net_income_guidance)`: S=-1.00, F=-0.61, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(max_net_income_guidance, 5))`: S=-0.66, F=-0.29, T=33.5%, INFERIOR (TOP3000)
- `ts_zscore(max_net_income_guidance, 22)`: S=0.08, F=0.01, T=43.3%, INFERIOR (TOP3000)
- `ts_mean(max_net_income_guidance, 10)`: S=0.98, F=0.59, T=1.7%, INFERIOR (TOP3000)
- `rank(ts_rank(max_net_income_guidance, 22))`: S=-0.05, F=-0.01, T=12.5%, INFERIOR (TOP3000)
- `rank(-1 * max_net_income_guidance)`: S=0.34, F=0.18, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * max_net_income_guidance / close)`: S=0.29, F=0.14, T=2.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 5F/27P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 31F/1P
- LOW_SUB_UNIVERSE_SHARPE: 12F/8P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 1.31, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.54 (moderate), ret=+1.4%
  - 2020: S=1.22 (moderate), ret=+4.0%
  - 2021: S=3.08 (strong), ret=+11.1%
  - 2022: S=1.30 (moderate), ret=+4.3%
  - 2023: S=-0.18 (negative), ret=-0.4%

## Risk & Drawdown
- Max drawdown: 3.64% over 559 days (recovered)
- Annualized: return +4.2%, volatility 3.2% (fraction of booksize)
- Hit rate: 51.3% positive days
- Tail shape: skew +0.25, excess kurtosis +1.69

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.03, max 3.91, latest -0.18

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2023
Best month: +3.06%; worst month: -1.76%
Positive months: 66%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=1.86
- Sideways: S=0.45
- Bear: S=1.59

## Negated Direction
Best negated: `rank(-1 * max_net_income_guidance)` S=0.34, F=0.18, INFERIOR
Direction gap: -0.98 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * max_net_income_guidance)`: S=0.34, F=0.18, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * max_net_income_guidance / close)`: S=0.29, F=0.14, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(max_net_income_guidance, 5))`: S=-0.66, F=-0.29, T=33.5%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(max_net_income_guidance)` | TOP3000 | 1.31 | 0.76 | 3.6% | 80% | all-weather |
| `rank(max_net_income_guidance)` | TOP1000 | 1.01 | 0.61 | 3.8% | 80% | mixed |
| `rank(ts_delta(max_net_income_guidance, 5))` | TOP200 | 0.68 | 0.29 | 12.4% | 100% | bear-only |
| `rank(max_net_income_guidance)` | TOP500 | 0.41 | 0.19 | 16.9% | 80% | bull-only |
| `rank(max_net_income_guidance / close)` | TOP3000 | 0.23 | 0.11 | 39.6% | 60% | bull-only |
| `rank(max_net_income_guidance / close)` | TOP1000 | 0.21 | 0.08 | 29.3% | 60% | bull-only |

## Correlation Notes
Top correlates:
- min_net_income_guidance: 1.000 (strongly positively correlated)
- max_adjusted_net_income_guidance: 0.794 (strongly positively correlated)
- operating_profit_before_depr_amort_min_guidance_qtr: 0.399 (weakly positively correlated)
- eps_max_guidance_quarterly: 0.395 (weakly positively correlated)
- eps_min_guidance_quarterly: 0.393 (weakly positively correlated)

Redundancy cluster #7: 3 similar fields, mean |rho| 0.862 (representative: max_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| fnd6_newqv1300_drltq | fundamental6 | +0.01 | 1.93 | +0.50 | +0.85 | yes |
| rank(scl12_sentiment * (-1 * returns)) | socialmedia12 | -0.03 | 1.75 | +0.44 | -0.57 | yes |
| unsystematic_risk_last_360_days | model51 | +0.00 | 1.81 | +0.49 | +0.69 | yes |
| fn_assets_fair_val_l2_q | fundamental2 | +0.05 | 1.73 | +0.42 | -0.73 | yes |
| implied_volatility_put_1080 | option8 | +0.02 | 1.88 | +0.49 | +0.65 | yes |

## Actionability
Blocked by LOW_FITNESS. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
