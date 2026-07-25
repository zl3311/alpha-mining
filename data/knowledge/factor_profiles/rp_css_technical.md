---
field: rp_css_technical
dataset: news18
best_template: rank_level
best_sharpe: 1.03
best_fitness: 0.95
best_universe: TOP500
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 20
regime_profile: all-weather
n_variations_with_pnl: 3
max_drawdown: 0.1232
ann_vol: 0.1626
hit_rate: 0.1344
rolling_sharpe_min: 0.01
rolling_sharpe_max: 2.645
top_merge_partner: news_open_gap
negated_best_sharpe: 0.34
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.12
n_negated_sims: 4
direction_gap: -0.69
---
# rp_css_technical (news18)

*Composite sentiment score based on technical analysis*

## Signal Profile
- `rank(rp_css_technical)`: S=1.03, F=0.95, T=17.7%, INFERIOR (TOP500)
- `rank(ts_delta(rp_css_technical, 5))`: S=0.00, F=0.00, T=0.0%, UNKNOWN (TOP3000)
- `-rank(rp_css_technical)`: S=-1.21, F=-0.95, T=32.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(rp_css_technical, 5))`: S=0.00, F=0.00, T=0.0%, UNKNOWN (TOP3000)
- `ts_zscore(rp_css_technical, 22)`: S=-0.49, F=-0.17, T=1.6%, INFERIOR (TOP3000)
- `ts_mean(rp_css_technical, 10)`: S=-0.09, F=-0.02, T=44.2%, INFERIOR (TOP3000)
- `rank(ts_rank(rp_css_technical, 22))`: S=0.36, F=0.23, T=11.8%, INFERIOR (TOP3000)
- `rank(-1 * rp_css_technical)`: S=0.17, F=0.04, T=61.1%, INFERIOR (TOP3000)
- `rank(-1 * rp_css_technical / close)`: S=0.34, F=0.12, T=66.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 20F/0P
- LOW_FITNESS: 13F/0P
- LOW_SHARPE: 20F/0P
- LOW_SUB_UNIVERSE_SHARPE: 6F/6P
- LOW_TURNOVER: 7F/13P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 1.19, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.81 (moderate), ret=+18.2%
  - 2020: S=1.49 (moderate), ret=+23.5%
  - 2021: S=1.15 (moderate), ret=+14.3%
  - 2022: S=2.49 (strong), ret=+39.9%
  - 2023: S=-0.13 (negative), ret=-1.4%

## Risk & Drawdown
- Max drawdown: 12.32% over 106 days (not yet recovered, ongoing at window end)
- Annualized: return +19.3%, volatility 16.3% (fraction of booksize)
- Hit rate: 13.4% positive days
- Tail shape: skew +8.30, excess kurtosis +147.35

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min 0.01, max 2.65, latest 0.01

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2023
Best month: +14.33%; worst month: -3.85%
Positive months: 64%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=2.29
- Sideways: S=0.61
- Bear: S=0.83

## Negated Direction
Best negated: `rank(-1 * rp_css_technical / close)` S=0.34, F=0.12, INFERIOR
Direction gap: -0.69 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * rp_css_technical)`: S=0.17, F=0.04, T=61.1%, INFERIOR (TOP3000)
- `rank(-1 * rp_css_technical / close)`: S=0.34, F=0.12, T=66.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(rp_css_technical, 5))`: S=0.00, F=0.00, T=0.0%, UNKNOWN (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(rp_css_technical)` | TOP1000 | 1.19 | 0.95 | 12.3% | 80% | all-weather |
| `rank(rp_css_technical)` | TOP500 | 1.01 | 0.95 | 12.8% | 100% | all-weather |
| `rank(rp_css_technical)` | TOP200 | 1.03 | 0.84 | 6.9% | 100% | all-weather |

## Correlation Notes
Top correlates:
- rp_nip_technical: -0.331 (weakly negatively correlated)
- rp_ess_technical: 0.149 (weakly positively correlated)
- fnd6_newqv1300_anoq: 0.098 (weakly positively correlated)
- fn_business_combination_assets_aquired_goodwill_q: -0.094 (weakly negatively correlated)
- implied_volatility_put_30: 0.087 (weakly positively correlated)

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| news_open_gap | news12 | -0.06 | 1.73 | +0.54 | +0.22 | yes |
| fnd6_nopio | fundamental6 | +0.01 | 1.74 | +0.46 | -0.54 | yes |
| fn_line_of_credit_facility_amount_out_a | fundamental2 | -0.06 | 1.79 | +0.51 | +0.00 | yes |
| fn_comp_options_out_weighted_avg_q | fundamental2 | -0.03 | 1.74 | +0.50 | +0.69 | yes |
| fnd6_cld4 | fundamental6 | -0.04 | 1.65 | +0.47 | -0.33 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, rank_value_norm, trade_when
