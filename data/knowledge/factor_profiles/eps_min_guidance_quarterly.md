---
field: eps_min_guidance_quarterly
dataset: analyst4
best_template: rank_level
best_sharpe: 0.85
best_fitness: 0.52
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 8
max_drawdown: 0.092
ann_vol: 0.0547
hit_rate: 0.5053
rolling_sharpe_min: -2.043
rolling_sharpe_max: 2.907
top_merge_partner: news_open_vol
redundancy_cluster: 13
negated_best_sharpe: 0.36
negated_best_template: rank_neg_delta
negated_best_fitness: 0.09
n_negated_sims: 10
direction_gap: -0.49
---
# eps_min_guidance_quarterly (analyst4)

*Minimum guidance value for Earnings per Share*

## Signal Profile
- `rank(eps_min_guidance_quarterly)`: S=0.85, F=0.52, T=0.7%, INFERIOR (TOP3000)
- `rank(eps_min_guidance_quarterly / close)`: S=0.50, F=0.31, T=1.5%, INFERIOR (TOP3000)
- `rank(ts_delta(eps_min_guidance_quarterly, 5))`: S=0.44, F=0.15, T=33.1%, INFERIOR (TOP200)
- `-rank(eps_min_guidance_quarterly)`: S=-0.43, F=-0.20, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(eps_min_guidance_quarterly, 5))`: S=0.36, F=0.09, T=36.3%, INFERIOR (TOP3000)
- `ts_zscore(eps_min_guidance_quarterly, 22)`: S=0.31, F=0.09, T=36.4%, INFERIOR (TOP3000)
- `ts_mean(eps_min_guidance_quarterly, 10)`: S=0.45, F=0.21, T=1.3%, INFERIOR (TOP3000)
- `rank(ts_rank(eps_min_guidance_quarterly, 22))`: S=0.06, F=0.01, T=12.4%, INFERIOR (TOP3000)
- `rank(-1 * eps_min_guidance_quarterly)`: S=-0.24, F=-0.09, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * eps_min_guidance_quarterly / close)`: S=-0.13, F=-0.04, T=2.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 2F/30P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 18F/11P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.83, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=1.39 (moderate), ret=+3.1%
  - 2020: S=-1.66 (negative), ret=-5.3%
  - 2021: S=2.21 (strong), ret=+15.8%
  - 2022: S=1.64 (strong), ret=+12.8%
  - 2023: S=-1.00 (negative), ret=-4.1%

## Risk & Drawdown
- Max drawdown: 9.20% over 539 days (recovered)
- Annualized: return +4.6%, volatility 5.5% (fraction of booksize)
- Hit rate: 50.5% positive days
- Tail shape: skew +0.08, excess kurtosis +2.74

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.04, max 2.91, latest -1.14

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2020
Best month: +4.17%; worst month: -2.79%
Positive months: 63%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.60
- Sideways: S=0.80
- Bear: S=-1.59

## Negated Direction
Best negated: `rank(-1 * ts_delta(eps_min_guidance_quarterly, 5))` S=0.36, F=0.09, INFERIOR
Direction gap: -0.49 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * eps_min_guidance_quarterly)`: S=-0.24, F=-0.09, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * eps_min_guidance_quarterly / close)`: S=-0.13, F=-0.04, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(eps_min_guidance_quarterly, 5))`: S=0.36, F=0.09, T=36.3%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(eps_min_guidance_quarterly)` | TOP3000 | 0.83 | 0.52 | 9.2% | 60% | bull-only |
| `rank(eps_min_guidance_quarterly / close)` | TOP3000 | 0.50 | 0.31 | 29.4% | 60% | bull-only |
| `rank(eps_min_guidance_quarterly)` | TOP1000 | 0.43 | 0.20 | 10.9% | 60% | bull-only |
| `rank(eps_min_guidance_quarterly / close)` | TOP1000 | 0.35 | 0.17 | 14.9% | 40% | bull-only |
| `rank(ts_delta(eps_min_guidance_quarterly, 5))` | TOP200 | 0.46 | 0.15 | 19.1% | 80% | mixed |
| `rank(eps_min_guidance_quarterly)` | TOP500 | 0.24 | 0.09 | 13.0% | 40% | bull-only |
| `rank(ts_delta(eps_min_guidance_quarterly, 5))` | TOP1000 | 0.32 | 0.06 | 8.6% | 60% | weak |
| `rank(eps_min_guidance_quarterly / close)` | TOP500 | 0.13 | 0.04 | 19.1% | 40% | bull-only |

## Correlation Notes
Top correlates:
- eps_max_guidance_quarterly: 0.999 (strongly positively correlated)
- earnings_per_share_max_guidance: 0.949 (strongly positively correlated)
- earnings_per_share_min_guidance: 0.949 (strongly positively correlated)
- max_reported_eps_guidance: 0.925 (strongly positively correlated)
- eps_reported_min_guidance_qtr: 0.925 (strongly positively correlated)

Redundancy cluster #13: 127 similar fields, mean |rho| 0.82 (representative: anl4_bvps_flag). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| news_open_vol | news12 | -0.42 | 1.61 | +0.69 | -0.32 | yes |
| rank(scl12_buzz * (-1 * returns)) | socialmedia12 | -0.35 | 2.20 | +0.58 | -0.92 | yes |
| rank(fnd6_acdo) + rank(open/close - 1) | unknown | -0.36 | 2.60 | +0.58 | -0.78 | yes |
| rank(fnd6_acdo) * rank(-1 * returns) | unknown | -0.34 | 2.40 | +0.53 | -0.82 | yes |
| fn_comp_options_forfeitures_and_expirations_a | fundamental2 | -0.28 | 1.68 | +0.51 | -0.94 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
