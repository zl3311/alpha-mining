---
field: operating_profit_before_depr_amort_min_guidance_qtr
dataset: analyst4
best_template: rank_level
best_sharpe: 0.97
best_fitness: 0.6
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 6
max_drawdown: 0.1295
ann_vol: 0.05
hit_rate: 0.5069
rolling_sharpe_min: -1.533
rolling_sharpe_max: 3.902
top_merge_partner: fnd6_newqv1300_tstknq
redundancy_cluster: 38
negated_best_sharpe: 0.2
negated_best_template: rank_neg_delta
negated_best_fitness: 0.04
n_negated_sims: 10
direction_gap: -0.77
---
# operating_profit_before_depr_amort_min_guidance_qtr (analyst4)

*Minimum guidance value for Earnings before interest, taxes, depreciation and amortization*

## Signal Profile
- `rank(operating_profit_before_depr_amort_min_guidance_qtr)`: S=0.97, F=0.60, T=0.9%, INFERIOR (TOP3000)
- `rank(operating_profit_before_depr_amort_min_guidance_qtr / close)`: S=0.36, F=0.18, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_delta(operating_profit_before_depr_amort_min_guidance_qtr, 5))`: S=0.46, F=0.16, T=33.8%, INFERIOR (TOP200)
- `-rank(operating_profit_before_depr_amort_min_guidance_qtr)`: S=-0.31, F=-0.13, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(operating_profit_before_depr_amort_min_guidance_qtr, 5))`: S=0.20, F=0.04, T=36.2%, INFERIOR (TOP3000)
- `-ts_zscore(operating_profit_before_depr_amort_min_guidance_qtr, 63)`: S=0.61, F=0.27, T=20.8%, INFERIOR (TOP3000)
- `ts_mean(operating_profit_before_depr_amort_min_guidance_qtr, 10)`: S=0.33, F=0.15, T=1.9%, INFERIOR (TOP3000)
- `rank(ts_rank(operating_profit_before_depr_amort_min_guidance_qtr, 22))`: S=-0.10, F=-0.02, T=12.7%, INFERIOR (TOP3000)
- `rank(-1 * operating_profit_before_depr_amort_min_guidance_qtr)`: S=-0.38, F=-0.22, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * operating_profit_before_depr_amort_min_guidance_qtr / close)`: S=-0.10, F=-0.03, T=2.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 3F/29P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/15P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.96, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=1.31 (moderate), ret=+4.8%
  - 2020: S=3.84 (strong), ret=+20.0%
  - 2021: S=1.39 (moderate), ret=+6.4%
  - 2022: S=-1.27 (negative), ret=-6.8%
  - 2023: S=-0.15 (negative), ret=-0.8%

## Risk & Drawdown
- Max drawdown: 12.95% over 885 days (not yet recovered, ongoing at window end)
- Annualized: return +4.8%, volatility 5.0% (fraction of booksize)
- Hit rate: 50.7% positive days
- Tail shape: skew +0.38, excess kurtosis +1.62

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.53, max 3.90, latest 0.03

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2022
Best month: +4.13%; worst month: -2.66%
Positive months: 64%

## Regime Profile
Regime profile: **mixed**
- Bull: S=-0.42
- Sideways: S=0.48
- Bear: S=2.79

## Negated Direction
Best negated: `rank(-1 * ts_delta(operating_profit_before_depr_amort_min_guidance_qtr, 5))` S=0.20, F=0.04, INFERIOR
Direction gap: -0.77 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * operating_profit_before_depr_amort_min_guidance_qtr)`: S=-0.38, F=-0.22, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * operating_profit_before_depr_amort_min_guidance_qtr / close)`: S=-0.10, F=-0.03, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(operating_profit_before_depr_amort_min_guidance_qtr, 5))`: S=0.20, F=0.04, T=36.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(operating_profit_before_depr_amort_min_guidance_qtr)` | TOP3000 | 0.96 | 0.60 | 13.0% | 60% | mixed |
| `rank(operating_profit_before_depr_amort_min_guidance_qtr)` | TOP500 | 0.40 | 0.22 | 35.0% | 80% | bear-only |
| `rank(operating_profit_before_depr_amort_min_guidance_qtr / close)` | TOP3000 | 0.35 | 0.18 | 29.8% | 60% | bull-only |
| `rank(ts_delta(operating_profit_before_depr_amort_min_guidance_qtr, 5))` | TOP200 | 0.47 | 0.16 | 17.3% | 60% | bear-only |
| `rank(operating_profit_before_depr_amort_min_guidance_qtr)` | TOP1000 | 0.32 | 0.13 | 32.1% | 60% | bear-only |
| `rank(operating_profit_before_depr_amort_min_guidance_qtr / close)` | TOP500 | 0.11 | 0.03 | 17.4% | 60% | mixed |

## Correlation Notes
Top correlates:
- operating_profit_before_depr_amort_max_guidance_qtr: 0.999 (strongly positively correlated)
- anl4_qf_az_div_number: 0.560 (moderately positively correlated)
- anl4_qfd1_az_div_number: 0.560 (moderately positively correlated)
- fn_oth_comp_grants_weighted_avg_grant_date_fair_value_a: 0.544 (moderately positively correlated)
- systematic_risk_last_90_days: 0.544 (moderately positively correlated)

Redundancy cluster #38: 2 similar fields, mean |rho| 0.999 (representative). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| fnd6_newqv1300_tstknq | fundamental6 | -0.23 | 1.51 | +0.55 | -0.68 | yes |
| fnd6_newqv1300_tstkq | fundamental6 | -0.28 | 1.50 | +0.54 | -0.67 | yes |
| fnd6_newa2v1300_tstkn | fundamental6 | -0.26 | 1.49 | +0.52 | -0.71 | yes |
| fnd6_xrent | fundamental6 | -0.26 | 1.46 | +0.49 | -0.87 | yes |
| rel_num_part | pv13 | -0.19 | 1.77 | +0.50 | -0.78 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
