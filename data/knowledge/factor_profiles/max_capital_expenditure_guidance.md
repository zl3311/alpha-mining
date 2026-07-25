---
field: max_capital_expenditure_guidance
dataset: analyst4
best_template: rank_level
best_sharpe: 0.89
best_fitness: 0.54
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 6
max_drawdown: 0.1078
ann_vol: 0.0523
hit_rate: 0.5239
rolling_sharpe_min: -2.408
rolling_sharpe_max: 2.866
top_merge_partner: news_open_vol
redundancy_cluster: 13
negated_best_sharpe: 0.47
negated_best_template: rank_neg_delta
negated_best_fitness: 0.14
n_negated_sims: 10
direction_gap: -0.42
---
# max_capital_expenditure_guidance (analyst4)

*The maximum guidance value for Capital Expenditures on an annual basis.*

## Signal Profile
- `rank(max_capital_expenditure_guidance)`: S=0.89, F=0.54, T=1.1%, INFERIOR (TOP3000)
- `rank(max_capital_expenditure_guidance / close)`: S=0.45, F=0.26, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_delta(max_capital_expenditure_guidance, 5))`: S=0.03, F=0.00, T=32.4%, INFERIOR (TOP200)
- `-rank(max_capital_expenditure_guidance)`: S=-0.77, F=-0.43, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(max_capital_expenditure_guidance, 5))`: S=0.47, F=0.14, T=35.7%, INFERIOR (TOP3000)
- `-ts_zscore(max_capital_expenditure_guidance, 63)`: S=0.34, F=0.12, T=20.4%, INFERIOR (TOP3000)
- `ts_mean(max_capital_expenditure_guidance, 10)`: S=0.73, F=0.40, T=1.7%, INFERIOR (TOP3000)
- `rank(ts_rank(max_capital_expenditure_guidance, 22))`: S=-0.22, F=-0.06, T=12.2%, INFERIOR (TOP3000)
- `rank(-1 * max_capital_expenditure_guidance)`: S=-0.39, F=-0.17, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * max_capital_expenditure_guidance / close)`: S=-0.23, F=-0.09, T=2.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 2F/30P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 16F/13P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.89, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=1.19 (moderate), ret=+2.6%
  - 2020: S=-1.59 (negative), ret=-5.6%
  - 2021: S=1.85 (strong), ret=+13.0%
  - 2022: S=1.73 (strong), ret=+12.6%
  - 2023: S=0.02 (weak), ret=+0.1%

## Risk & Drawdown
- Max drawdown: 10.78% over 554 days (recovered)
- Annualized: return +4.6%, volatility 5.2% (fraction of booksize)
- Hit rate: 52.4% positive days
- Tail shape: skew +0.12, excess kurtosis +2.59

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.41, max 2.87, latest -0.13

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2020
Best month: +4.04%; worst month: -2.52%
Positive months: 61%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.84
- Sideways: S=0.92
- Bear: S=-1.97

## Negated Direction
Best negated: `rank(-1 * ts_delta(max_capital_expenditure_guidance, 5))` S=0.47, F=0.14, INFERIOR
Direction gap: -0.42 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * max_capital_expenditure_guidance)`: S=-0.39, F=-0.17, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * max_capital_expenditure_guidance / close)`: S=-0.23, F=-0.09, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(max_capital_expenditure_guidance, 5))`: S=0.47, F=0.14, T=35.7%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(max_capital_expenditure_guidance)` | TOP3000 | 0.89 | 0.54 | 10.8% | 80% | bull-only |
| `rank(max_capital_expenditure_guidance)` | TOP1000 | 0.77 | 0.43 | 7.1% | 60% | bull-only |
| `rank(max_capital_expenditure_guidance / close)` | TOP3000 | 0.45 | 0.26 | 30.3% | 60% | bull-only |
| `rank(max_capital_expenditure_guidance / close)` | TOP1000 | 0.43 | 0.22 | 18.3% | 60% | bull-only |
| `rank(max_capital_expenditure_guidance)` | TOP500 | 0.39 | 0.17 | 13.5% | 60% | bull-only |
| `rank(max_capital_expenditure_guidance / close)` | TOP500 | 0.23 | 0.09 | 19.9% | 60% | bull-only |

## Correlation Notes
Top correlates:
- min_capital_expenditure_guidance: 0.996 (strongly positively correlated)
- earnings_per_share_max_guidance: 0.880 (strongly positively correlated)
- earnings_per_share_min_guidance: 0.879 (strongly positively correlated)
- fnd6_fatp: 0.869 (strongly positively correlated)
- eps_min_guidance_quarterly: 0.862 (strongly positively correlated)

Redundancy cluster #13: 127 similar fields, mean |rho| 0.82 (representative: anl4_bvps_flag). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| news_open_vol | news12 | -0.42 | 1.65 | +0.72 | -0.32 | yes |
| rank(fnd6_acdo) + rank(open/close - 1) | unknown | -0.36 | 2.62 | +0.60 | -0.67 | yes |
| fn_def_tax_assets_liab_net_a | fundamental2 | -0.38 | 1.53 | +0.62 | -0.39 | yes |
| rank(scl12_buzz * (-1 * returns)) | socialmedia12 | -0.34 | 2.20 | +0.58 | -0.80 | yes |
| rank(fnd6_acdo) * rank(-1 * returns) | unknown | -0.34 | 2.41 | +0.54 | -0.73 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
