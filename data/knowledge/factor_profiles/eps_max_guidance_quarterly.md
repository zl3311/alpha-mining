---
field: eps_max_guidance_quarterly
dataset: analyst4
best_template: rank_level
best_sharpe: 0.86
best_fitness: 0.53
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 7
max_drawdown: 0.0915
ann_vol: 0.0547
hit_rate: 0.5061
rolling_sharpe_min: -1.967
rolling_sharpe_max: 2.913
top_merge_partner: news_open_vol
redundancy_cluster: 13
negated_best_sharpe: 0.48
negated_best_template: rank_neg_delta
negated_best_fitness: 0.15
n_negated_sims: 10
direction_gap: -0.38
---
# eps_max_guidance_quarterly (analyst4)

*The maximum guidance value for Earnings Per Share.*

## Signal Profile
- `rank(eps_max_guidance_quarterly)`: S=0.86, F=0.53, T=0.7%, INFERIOR (TOP3000)
- `rank(eps_max_guidance_quarterly / close)`: S=0.44, F=0.27, T=1.4%, INFERIOR (TOP3000)
- `rank(ts_delta(eps_max_guidance_quarterly, 5))`: S=0.46, F=0.19, T=32.6%, INFERIOR (TOP200)
- `-rank(eps_max_guidance_quarterly)`: S=-0.47, F=-0.23, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(eps_max_guidance_quarterly, 5))`: S=0.48, F=0.15, T=34.8%, INFERIOR (TOP3000)
- `-ts_zscore(eps_max_guidance_quarterly, 63)`: S=0.26, F=0.08, T=20.9%, INFERIOR (TOP3000)
- `ts_mean(eps_max_guidance_quarterly, 10)`: S=0.53, F=0.27, T=1.4%, INFERIOR (TOP3000)
- `rank(ts_rank(eps_max_guidance_quarterly, 22))`: S=-0.17, F=-0.04, T=12.4%, INFERIOR (TOP3000)
- `rank(-1 * eps_max_guidance_quarterly)`: S=-0.29, F=-0.11, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * eps_max_guidance_quarterly / close)`: S=-0.12, F=-0.04, T=2.0%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 6F/26P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 18F/11P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.85, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=1.39 (moderate), ret=+3.1%
  - 2020: S=-1.57 (negative), ret=-5.1%
  - 2021: S=2.20 (strong), ret=+15.7%
  - 2022: S=1.63 (strong), ret=+12.8%
  - 2023: S=-0.89 (negative), ret=-3.6%

## Risk & Drawdown
- Max drawdown: 9.15% over 539 days (recovered)
- Annualized: return +4.7%, volatility 5.5% (fraction of booksize)
- Hit rate: 50.6% positive days
- Tail shape: skew +0.09, excess kurtosis +2.78

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.97, max 2.91, latest -1.04

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2020
Best month: +4.14%; worst month: -2.77%
Positive months: 63%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.63
- Sideways: S=0.83
- Bear: S=-1.59

## Negated Direction
Best negated: `rank(-1 * ts_delta(eps_max_guidance_quarterly, 5))` S=0.48, F=0.15, INFERIOR
Direction gap: -0.38 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * eps_max_guidance_quarterly)`: S=-0.29, F=-0.11, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * eps_max_guidance_quarterly / close)`: S=-0.12, F=-0.04, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(eps_max_guidance_quarterly, 5))`: S=0.48, F=0.15, T=34.8%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(eps_max_guidance_quarterly)` | TOP3000 | 0.85 | 0.53 | 9.2% | 60% | bull-only |
| `rank(eps_max_guidance_quarterly / close)` | TOP3000 | 0.43 | 0.27 | 32.9% | 60% | bull-only |
| `rank(eps_max_guidance_quarterly)` | TOP1000 | 0.47 | 0.23 | 9.4% | 60% | bull-only |
| `rank(ts_delta(eps_max_guidance_quarterly, 5))` | TOP200 | 0.48 | 0.19 | 25.1% | 60% | mixed |
| `rank(eps_max_guidance_quarterly / close)` | TOP1000 | 0.28 | 0.13 | 20.8% | 60% | bull-only |
| `rank(eps_max_guidance_quarterly)` | TOP500 | 0.28 | 0.11 | 13.4% | 40% | bull-only |
| `rank(eps_max_guidance_quarterly / close)` | TOP500 | 0.11 | 0.04 | 24.5% | 40% | bull-only |

## Correlation Notes
Top correlates:
- eps_min_guidance_quarterly: 0.999 (strongly positively correlated)
- earnings_per_share_max_guidance: 0.948 (strongly positively correlated)
- earnings_per_share_min_guidance: 0.947 (strongly positively correlated)
- max_reported_eps_guidance: 0.924 (strongly positively correlated)
- eps_reported_min_guidance_qtr: 0.924 (strongly positively correlated)

Redundancy cluster #13: 127 similar fields, mean |rho| 0.82 (representative: anl4_bvps_flag). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| news_open_vol | news12 | -0.42 | 1.63 | +0.70 | -0.32 | yes |
| rank(scl12_buzz * (-1 * returns)) | socialmedia12 | -0.35 | 2.21 | +0.58 | -0.92 | yes |
| rank(fnd6_acdo) + rank(open/close - 1) | unknown | -0.36 | 2.61 | +0.58 | -0.77 | yes |
| fn_comp_options_forfeitures_and_expirations_a | fundamental2 | -0.28 | 1.69 | +0.52 | -0.94 | yes |
| rank(fnd6_acdo) * rank(-1 * returns) | unknown | -0.34 | 2.40 | +0.53 | -0.82 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
