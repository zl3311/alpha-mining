---
field: operating_profit_before_depr_amort_max_guidance_qtr
dataset: analyst4
best_template: rank_level
best_sharpe: 0.95
best_fitness: 0.59
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bear-only
n_variations_with_pnl: 6
max_drawdown: 0.1338
ann_vol: 0.0503
hit_rate: 0.5012
rolling_sharpe_min: -1.544
rolling_sharpe_max: 3.93
top_merge_partner: fnd6_newqv1300_tstknq
redundancy_cluster: 38
negated_best_sharpe: 0.2
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.08
n_negated_sims: 10
direction_gap: -0.75
---
# operating_profit_before_depr_amort_max_guidance_qtr (analyst4)

*Max guidance value for Earnings before interest, taxes, depreciation and amortization*

## Signal Profile
- `rank(operating_profit_before_depr_amort_max_guidance_qtr)`: S=0.95, F=0.59, T=0.9%, INFERIOR (TOP3000)
- `rank(operating_profit_before_depr_amort_max_guidance_qtr / close)`: S=0.34, F=0.17, T=1.5%, INFERIOR (TOP3000)
- `rank(ts_delta(operating_profit_before_depr_amort_max_guidance_qtr, 5))`: S=0.66, F=0.28, T=33.8%, INFERIOR (TOP200)
- `-rank(operating_profit_before_depr_amort_max_guidance_qtr)`: S=-0.30, F=-0.13, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(operating_profit_before_depr_amort_max_guidance_qtr, 5))`: S=-0.66, F=-0.28, T=33.8%, INFERIOR (TOP3000)
- `ts_zscore(operating_profit_before_depr_amort_max_guidance_qtr, 22)`: S=0.12, F=0.02, T=44.0%, INFERIOR (TOP3000)
- `ts_mean(operating_profit_before_depr_amort_max_guidance_qtr, 10)`: S=0.26, F=0.11, T=2.0%, INFERIOR (TOP3000)
- `rank(ts_rank(operating_profit_before_depr_amort_max_guidance_qtr, 22))`: S=-0.11, F=-0.02, T=12.7%, INFERIOR (TOP3000)
- `rank(-1 * operating_profit_before_depr_amort_max_guidance_qtr)`: S=-0.03, F=-0.01, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * operating_profit_before_depr_amort_max_guidance_qtr / close)`: S=0.20, F=0.08, T=2.5%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 9F/23P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 8F/12P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.95, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=1.31 (moderate), ret=+4.8%
  - 2020: S=3.87 (strong), ret=+20.1%
  - 2021: S=1.34 (moderate), ret=+6.2%
  - 2022: S=-1.28 (negative), ret=-7.0%
  - 2023: S=-0.14 (negative), ret=-0.7%

## Risk & Drawdown
- Max drawdown: 13.38% over 885 days (not yet recovered, ongoing at window end)
- Annualized: return +4.8%, volatility 5.0% (fraction of booksize)
- Hit rate: 50.1% positive days
- Tail shape: skew +0.37, excess kurtosis +1.61

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.54, max 3.93, latest 0.05

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2022
Best month: +4.14%; worst month: -2.71%
Positive months: 66%

## Regime Profile
Regime profile: **bear-only**
- Bull: S=-0.52
- Sideways: S=0.51
- Bear: S=2.83

## Negated Direction
Best negated: `rank(-1 * operating_profit_before_depr_amort_max_guidance_qtr / close)` S=0.20, F=0.08, INFERIOR
Direction gap: -0.75 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * operating_profit_before_depr_amort_max_guidance_qtr)`: S=-0.03, F=-0.01, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * operating_profit_before_depr_amort_max_guidance_qtr / close)`: S=0.20, F=0.08, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(operating_profit_before_depr_amort_max_guidance_qtr, 5))`: S=-0.66, F=-0.28, T=33.8%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(operating_profit_before_depr_amort_max_guidance_qtr)` | TOP3000 | 0.95 | 0.59 | 13.4% | 60% | bear-only |
| `rank(ts_delta(operating_profit_before_depr_amort_max_guidance_qtr, 5))` | TOP200 | 0.68 | 0.28 | 17.4% | 60% | bear-only |
| `rank(operating_profit_before_depr_amort_max_guidance_qtr)` | TOP500 | 0.41 | 0.23 | 35.0% | 80% | bear-only |
| `rank(operating_profit_before_depr_amort_max_guidance_qtr / close)` | TOP3000 | 0.33 | 0.17 | 30.6% | 60% | bull-only |
| `rank(operating_profit_before_depr_amort_max_guidance_qtr)` | TOP1000 | 0.31 | 0.13 | 32.4% | 60% | bear-only |
| `rank(operating_profit_before_depr_amort_max_guidance_qtr / close)` | TOP500 | 0.11 | 0.03 | 17.7% | 60% | mixed |

## Correlation Notes
Top correlates:
- operating_profit_before_depr_amort_min_guidance_qtr: 0.999 (strongly positively correlated)
- anl4_qf_az_div_number: 0.560 (moderately positively correlated)
- anl4_qfd1_az_div_number: 0.560 (moderately positively correlated)
- systematic_risk_last_90_days: 0.554 (moderately positively correlated)
- beta_last_90_days_spy: 0.549 (moderately positively correlated)

Redundancy cluster #38: 2 similar fields, mean |rho| 0.999 (representative: operating_profit_before_depr_amort_min_guidance_qtr). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| fnd6_newqv1300_tstknq | fundamental6 | -0.25 | 1.51 | +0.57 | -0.69 | yes |
| fnd6_newqv1300_tstkq | fundamental6 | -0.29 | 1.50 | +0.56 | -0.68 | yes |
| fnd6_newa2v1300_tstkn | fundamental6 | -0.27 | 1.49 | +0.54 | -0.72 | yes |
| fnd6_xrent | fundamental6 | -0.27 | 1.46 | +0.51 | -0.88 | yes |
| fnd6_tstkc | fundamental6 | -0.29 | 1.47 | +0.52 | -0.71 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
