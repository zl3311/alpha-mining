---
field: max_reported_eps_guidance
dataset: analyst4
best_template: neg_rank_level
best_sharpe: 0.73
best_fitness: 0.48
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 5
max_drawdown: 0.0617
ann_vol: 0.0495
hit_rate: 0.5077
rolling_sharpe_min: -1.653
rolling_sharpe_max: 2.951
top_merge_partner: news_open_vol
redundancy_cluster: 13
negated_best_sharpe: 0.73
negated_best_template: neg_rank_level
negated_best_fitness: 0.48
n_negated_sims: 10
direction_gap: -0.08
---
# max_reported_eps_guidance (analyst4)

*Reported Earnings Per Share - Maximum guidance value*

## Signal Profile
- `rank(max_reported_eps_guidance)`: S=0.81, F=0.46, T=0.7%, INFERIOR (TOP3000)
- `rank(max_reported_eps_guidance / close)`: S=0.30, F=0.16, T=1.5%, INFERIOR (TOP3000)
- `rank(ts_delta(max_reported_eps_guidance, 5))`: S=0.34, F=0.11, T=33.2%, INFERIOR (TOP200)
- `-rank(max_reported_eps_guidance)`: S=-0.32, F=-0.12, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(max_reported_eps_guidance, 5))`: S=-0.34, F=-0.11, T=33.2%, INFERIOR (TOP3000)
- `-ts_zscore(max_reported_eps_guidance, 63)`: S=-0.17, F=-0.04, T=21.1%, INFERIOR (TOP3000)
- `ts_mean(max_reported_eps_guidance, 10)`: S=0.35, F=0.14, T=1.3%, INFERIOR (TOP3000)
- `rank(ts_rank(max_reported_eps_guidance, 22))`: S=-0.10, F=-0.02, T=12.4%, INFERIOR (TOP3000)
- `rank(-1 * max_reported_eps_guidance)`: S=0.73, F=0.48, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * max_reported_eps_guidance / close)`: S=0.53, F=0.36, T=2.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 5F/27P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 17F/3P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.80, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.82 (moderate), ret=+2.0%
  - 2020: S=-1.30 (negative), ret=-3.7%
  - 2021: S=2.19 (strong), ret=+13.2%
  - 2022: S=1.63 (strong), ret=+11.8%
  - 2023: S=-0.99 (negative), ret=-3.9%

## Risk & Drawdown
- Max drawdown: 6.17% over 511 days (recovered)
- Annualized: return +4.0%, volatility 5.0% (fraction of booksize)
- Hit rate: 50.8% positive days
- Tail shape: skew +0.21, excess kurtosis +2.43

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.65, max 2.95, latest -1.12

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2020
Best month: +3.76%; worst month: -2.95%
Positive months: 61%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.58
- Sideways: S=0.40
- Bear: S=-1.32

## Negated Direction
Best negated: `rank(-1 * max_reported_eps_guidance)` S=0.73, F=0.48, INFERIOR
Direction gap: -0.08 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * max_reported_eps_guidance)`: S=0.73, F=0.48, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * max_reported_eps_guidance / close)`: S=0.53, F=0.36, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(max_reported_eps_guidance, 5))`: S=-0.34, F=-0.11, T=33.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(max_reported_eps_guidance)` | TOP3000 | 0.80 | 0.46 | 6.2% | 60% | bull-only |
| `rank(max_reported_eps_guidance / close)` | TOP3000 | 0.29 | 0.16 | 38.5% | 60% | bull-only |
| `rank(max_reported_eps_guidance)` | TOP1000 | 0.31 | 0.12 | 9.2% | 40% | bull-only |
| `rank(ts_delta(max_reported_eps_guidance, 5))` | TOP200 | 0.35 | 0.11 | 30.4% | 60% | bear-only |
| `rank(max_reported_eps_guidance / close)` | TOP1000 | 0.11 | 0.04 | 30.6% | 60% | bull-only |

## Correlation Notes
Top correlates:
- eps_reported_min_guidance_qtr: 1.000 (strongly positively correlated)
- eps_min_guidance_quarterly: 0.925 (strongly positively correlated)
- eps_max_guidance_quarterly: 0.924 (strongly positively correlated)
- min_reported_eps_guidance: 0.899 (strongly positively correlated)
- earnings_per_share_max_guidance: 0.899 (strongly positively correlated)

Redundancy cluster #13: 127 similar fields, mean |rho| 0.82 (representative: anl4_bvps_flag). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| news_open_vol | news12 | -0.43 | 1.57 | +0.65 | -0.45 | yes |
| rank(scl12_buzz * (-1 * returns)) | socialmedia12 | -0.35 | 2.16 | +0.54 | -0.88 | yes |
| rank(fnd6_acdo) + rank(open/close - 1) | unknown | -0.36 | 2.56 | +0.54 | -0.68 | yes |
| fn_def_tax_assets_liab_net_a | fundamental2 | -0.37 | 1.46 | +0.55 | -0.43 | yes |
| fn_comp_options_forfeitures_and_expirations_a | fundamental2 | -0.29 | 1.67 | +0.50 | -0.87 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
