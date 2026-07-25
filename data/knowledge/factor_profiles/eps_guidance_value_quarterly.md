---
field: eps_guidance_value_quarterly
dataset: analyst4
best_template: rank_value_norm
best_sharpe: 0.86
best_fitness: 0.48
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 8
max_drawdown: 0.0834
ann_vol: 0.0457
hit_rate: 0.532
rolling_sharpe_min: -1.251
rolling_sharpe_max: 2.826
top_merge_partner: fn_def_tax_assets_liab_net_a
negated_best_sharpe: 0.49
negated_best_template: rank_neg_delta
negated_best_fitness: 0.21
n_negated_sims: 10
direction_gap: -0.37
---
# eps_guidance_value_quarterly (analyst4)

*Earnings Per Share - Basic value*

## Signal Profile
- `rank(eps_guidance_value_quarterly)`: S=0.58, F=0.34, T=2.4%, INFERIOR (TOP200)
- `rank(eps_guidance_value_quarterly / close)`: S=0.86, F=0.48, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_delta(eps_guidance_value_quarterly, 5))`: S=0.47, F=0.17, T=33.6%, INFERIOR (TOP500)
- `-rank(eps_guidance_value_quarterly)`: S=-0.09, F=-0.02, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(eps_guidance_value_quarterly, 5))`: S=0.49, F=0.21, T=34.2%, INFERIOR (TOP3000)
- `-ts_zscore(eps_guidance_value_quarterly, 63)`: S=0.46, F=0.27, T=15.7%, INFERIOR (TOP3000)
- `ts_mean(eps_guidance_value_quarterly, 10)`: S=-0.52, F=-0.37, T=1.9%, INFERIOR (TOP3000)
- `rank(ts_rank(eps_guidance_value_quarterly, 22))`: S=-0.19, F=-0.06, T=12.5%, INFERIOR (TOP3000)
- `rank(-1 * eps_guidance_value_quarterly)`: S=-0.58, F=-0.34, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * eps_guidance_value_quarterly / close)`: S=-0.55, F=-0.35, T=2.9%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 8F/12P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.85, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=1.44 (moderate), ret=+5.5%
  - 2020: S=-0.37 (negative), ret=-1.8%
  - 2021: S=0.62 (moderate), ret=+3.1%
  - 2022: S=2.08 (strong), ret=+9.9%
  - 2023: S=0.58 (moderate), ret=+2.2%

## Risk & Drawdown
- Max drawdown: 8.34% over 660 days (recovered)
- Annualized: return +3.9%, volatility 4.6% (fraction of booksize)
- Hit rate: 53.2% positive days
- Tail shape: skew -0.01, excess kurtosis +0.54

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.25, max 2.83, latest 0.51

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +2.96%; worst month: -2.63%
Positive months: 59%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.16
- Sideways: S=2.08
- Bear: S=-1.48

## Negated Direction
Best negated: `rank(-1 * ts_delta(eps_guidance_value_quarterly, 5))` S=0.49, F=0.21, INFERIOR
Direction gap: -0.37 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * eps_guidance_value_quarterly)`: S=-0.58, F=-0.34, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * eps_guidance_value_quarterly / close)`: S=-0.55, F=-0.35, T=2.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(eps_guidance_value_quarterly, 5))`: S=0.49, F=0.21, T=34.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(eps_guidance_value_quarterly / close)` | TOP3000 | 0.85 | 0.48 | 8.3% | 80% | bull-only |
| `rank(eps_guidance_value_quarterly / close)` | TOP200 | 0.53 | 0.35 | 15.2% | 80% | weak |
| `rank(eps_guidance_value_quarterly)` | TOP200 | 0.56 | 0.34 | 9.3% | 80% | weak |
| `rank(eps_guidance_value_quarterly)` | TOP3000 | 0.59 | 0.29 | 11.4% | 80% | bull-only |
| `rank(ts_delta(eps_guidance_value_quarterly, 5))` | TOP500 | 0.48 | 0.17 | 11.5% | 80% | bull-only |
| `rank(eps_guidance_value_quarterly / close)` | TOP1000 | 0.29 | 0.12 | 13.6% | 80% | bull-only |
| `rank(eps_guidance_value_quarterly / close)` | TOP500 | 0.26 | 0.11 | 18.6% | 80% | bull-only |
| `rank(eps_guidance_value_quarterly)` | TOP500 | 0.13 | 0.04 | 18.6% | 80% | bull-only |

## Correlation Notes
Top correlates:
- fnd2_itxreexftfedstyitxrt: 0.662 (moderately positively correlated)
- cap: 0.656 (moderately positively correlated)
- shareholders_equity_reported_value: 0.650 (moderately positively correlated)
- shareholders_equity_actual_value: 0.650 (moderately positively correlated)
- fnd6_cptnewqv1300_ceqq: 0.649 (moderately positively correlated)

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| fn_def_tax_assets_liab_net_a | fundamental2 | -0.27 | 1.43 | +0.52 | -0.71 | yes |
| operating_profit_before_depr_amort_max_guidance_qtr | analyst4 | -0.36 | 1.59 | +0.65 | -0.82 | no |
| operating_profit_before_depr_amort_min_guidance_qtr | analyst4 | -0.36 | 1.60 | +0.64 | -0.82 | no |
| snt_value_fast_d1 | socialmedia12 | -0.19 | 1.36 | +0.47 | -0.61 | yes |
| fnd6_rank | fundamental6 | -0.32 | 1.65 | +0.49 | -0.25 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
