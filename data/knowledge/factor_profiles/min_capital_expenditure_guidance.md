---
field: min_capital_expenditure_guidance
dataset: analyst4
best_template: rank_level
best_sharpe: 0.93
best_fitness: 0.57
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 6
max_drawdown: 0.1012
ann_vol: 0.0514
hit_rate: 0.5166
rolling_sharpe_min: -2.276
rolling_sharpe_max: 2.892
top_merge_partner: news_open_vol
redundancy_cluster: 13
negated_best_sharpe: 0.65
negated_best_template: rank_neg_delta
negated_best_fitness: 0.25
n_negated_sims: 10
direction_gap: -0.28
---
# min_capital_expenditure_guidance (analyst4)

*Minimum guidance value for Capital Expenditures*

## Signal Profile
- `rank(min_capital_expenditure_guidance)`: S=0.93, F=0.57, T=1.1%, INFERIOR (TOP3000)
- `rank(min_capital_expenditure_guidance / close)`: S=0.55, F=0.34, T=1.7%, INFERIOR (TOP3000)
- `rank(ts_delta(min_capital_expenditure_guidance, 5))`: S=0.09, F=0.01, T=36.5%, INFERIOR (TOP1000)
- `-rank(min_capital_expenditure_guidance)`: S=-0.81, F=-0.46, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(min_capital_expenditure_guidance, 5))`: S=0.65, F=0.25, T=33.3%, INFERIOR (TOP3000)
- `-ts_zscore(min_capital_expenditure_guidance, 63)`: S=0.14, F=0.03, T=18.9%, INFERIOR (TOP3000)
- `ts_mean(min_capital_expenditure_guidance, 10)`: S=0.82, F=0.46, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_rank(min_capital_expenditure_guidance, 22))`: S=-0.22, F=-0.05, T=12.5%, INFERIOR (TOP3000)
- `rank(-1 * min_capital_expenditure_guidance)`: S=-0.05, F=-0.01, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * min_capital_expenditure_guidance / close)`: S=0.11, F=0.03, T=2.7%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 5F/27P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 12F/8P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.92, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=1.11 (moderate), ret=+2.5%
  - 2020: S=-1.51 (negative), ret=-5.2%
  - 2021: S=1.95 (strong), ret=+13.5%
  - 2022: S=1.58 (strong), ret=+11.2%
  - 2023: S=0.34 (weak), ret=+1.2%

## Risk & Drawdown
- Max drawdown: 10.12% over 551 days (recovered)
- Annualized: return +4.7%, volatility 5.1% (fraction of booksize)
- Hit rate: 51.7% positive days
- Tail shape: skew +0.13, excess kurtosis +2.43

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.28, max 2.89, latest 0.20

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2020
Best month: +3.99%; worst month: -2.59%
Positive months: 61%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.89
- Sideways: S=0.97
- Bear: S=-1.94

## Negated Direction
Best negated: `rank(-1 * ts_delta(min_capital_expenditure_guidance, 5))` S=0.65, F=0.25, INFERIOR
Direction gap: -0.28 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * min_capital_expenditure_guidance)`: S=-0.05, F=-0.01, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * min_capital_expenditure_guidance / close)`: S=0.11, F=0.03, T=2.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(min_capital_expenditure_guidance, 5))`: S=0.65, F=0.25, T=33.3%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(min_capital_expenditure_guidance)` | TOP3000 | 0.92 | 0.57 | 10.1% | 80% | bull-only |
| `rank(min_capital_expenditure_guidance)` | TOP1000 | 0.81 | 0.46 | 6.9% | 80% | bull-only |
| `rank(min_capital_expenditure_guidance / close)` | TOP3000 | 0.55 | 0.34 | 24.1% | 80% | bull-only |
| `rank(min_capital_expenditure_guidance / close)` | TOP1000 | 0.56 | 0.31 | 11.1% | 60% | bull-only |
| `rank(min_capital_expenditure_guidance)` | TOP500 | 0.43 | 0.19 | 13.9% | 60% | bull-only |
| `rank(min_capital_expenditure_guidance / close)` | TOP500 | 0.30 | 0.13 | 17.9% | 40% | bull-only |

## Correlation Notes
Top correlates:
- max_capital_expenditure_guidance: 0.996 (strongly positively correlated)
- earnings_per_share_max_guidance: 0.873 (strongly positively correlated)
- earnings_per_share_min_guidance: 0.872 (strongly positively correlated)
- fnd6_fatp: 0.865 (strongly positively correlated)
- eps_min_guidance_quarterly: 0.857 (strongly positively correlated)

Redundancy cluster #13: 127 similar fields, mean |rho| 0.82 (representative: anl4_bvps_flag). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| news_open_vol | news12 | -0.42 | 1.66 | +0.74 | -0.37 | yes |
| fn_def_tax_assets_liab_net_a | fundamental2 | -0.37 | 1.57 | +0.65 | -0.28 | yes |
| rank(scl12_buzz * (-1 * returns)) | socialmedia12 | -0.34 | 2.22 | +0.59 | -0.75 | yes |
| rank(fnd6_acdo) + rank(open/close - 1) | unknown | -0.35 | 2.63 | +0.61 | -0.61 | yes |
| rank(fnd6_acdo) * rank(-1 * returns) | unknown | -0.34 | 2.42 | +0.55 | -0.69 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
