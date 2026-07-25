---
field: rp_ess_dividends
dataset: news18
best_template: rank_delta
best_sharpe: 1.38
best_fitness: 0.35
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_FITNESS
n_sims: 20
regime_profile: all-weather
n_variations_with_pnl: 4
max_drawdown: 0.0818
ann_vol: 0.0795
hit_rate: 0.5287
rolling_sharpe_min: 0.151
rolling_sharpe_max: 3.134
top_merge_partner: fnd6_acdo
negated_best_sharpe: 0.16
negated_best_template: neg_rank
negated_best_fitness: 0.01
n_negated_sims: 4
direction_gap: -1.22
---
# rp_ess_dividends (news18)

*Event sentiment score of dividends news*

## Signal Profile
- `rank(rp_ess_dividends)`: S=0.32, F=0.03, T=148.6%, INFERIOR (TOP3000)
- `rank(ts_delta(rp_ess_dividends, 5))`: S=1.38, F=0.35, T=168.9%, INFERIOR (TOP3000)
- `-rank(rp_ess_dividends)`: S=0.16, F=0.01, T=137.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(rp_ess_dividends, 5))`: S=-1.38, F=-0.35, T=168.9%, INFERIOR (TOP3000)
- `ts_zscore(rp_ess_dividends, 22)`: S=0.57, F=0.09, T=144.8%, INFERIOR (TOP3000)
- `ts_mean(rp_ess_dividends, 10)`: S=-0.41, F=-0.13, T=21.5%, INFERIOR (TOP3000)
- `rank(ts_rank(rp_ess_dividends, 22))`: S=0.28, F=0.03, T=145.2%, INFERIOR (TOP3000)
- `rank(-1 * rp_ess_dividends)`: S=-0.32, F=-0.03, T=148.6%, INFERIOR (TOP3000)
- `rank(-1 * rp_ess_dividends / close)`: S=-0.53, F=-0.07, T=149.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 19F/1P
- HIGH_TURNOVER: 19F/1P
- LOW_FITNESS: 20F/0P
- LOW_SHARPE: 19F/1P
- LOW_SUB_UNIVERSE_SHARPE: 11F/7P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 1.40, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=2.64 (strong), ret=+29.0%
  - 2020: S=1.45 (moderate), ret=+12.3%
  - 2021: S=0.67 (moderate), ret=+5.5%
  - 2022: S=0.97 (moderate), ret=+5.6%
  - 2023: S=0.70 (moderate), ret=+2.1%

## Risk & Drawdown
- Max drawdown: 8.18% over 66 days (recovered)
- Annualized: return +11.1%, volatility 8.0% (fraction of booksize)
- Hit rate: 52.9% positive days
- Tail shape: skew +0.26, excess kurtosis +9.79

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min 0.15, max 3.13, latest 0.77

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2021
Best month: +7.64%; worst month: -5.69%
Positive months: 61%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=0.64
- Sideways: S=2.22
- Bear: S=1.20

## Negated Direction
Best negated: `-rank(rp_ess_dividends)` S=0.16, F=0.01, INFERIOR
Direction gap: -1.22 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * rp_ess_dividends)`: S=-0.32, F=-0.03, T=148.6%, INFERIOR (TOP3000)
- `rank(-1 * rp_ess_dividends / close)`: S=-0.53, F=-0.07, T=149.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(rp_ess_dividends, 5))`: S=-1.38, F=-0.35, T=168.9%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(rp_ess_dividends, 5))` | TOP3000 | 1.40 | 0.35 | 8.2% | 100% | all-weather |
| `rank(ts_delta(rp_ess_dividends, 5))` | TOP1000 | 1.21 | 0.32 | 14.7% | 80% | all-weather |
| `rank(ts_delta(rp_ess_dividends, 5))` | TOP200 | 0.60 | 0.15 | 20.6% | 80% | all-weather |
| `rank(rp_ess_dividends)` | TOP3000 | 0.34 | 0.03 | 6.9% | 80% | weak |

## Correlation Notes
Top correlates:
- fnd6_txtubposdec: 0.123 (weakly positively correlated)
- news_pe_ratio: -0.105 (weakly negatively correlated)
- fnd6_newa2v1300_prsho: -0.086 (weakly negatively correlated)
- rp_css_partner: 0.086 (weakly positively correlated)
- fnd6_optlife: 0.079 (weakly positively correlated)

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| fnd6_acdo | fundamental_discontinued_ops | -0.01 | 1.99 | +0.59 | -0.80 | yes |
| unsystematic_risk_last_90_days | model51 | -0.02 | 1.93 | +0.53 | -0.81 | yes |
| rank(scl12_buzz * (-1 * returns)) | socialmedia12 | -0.04 | 2.19 | +0.56 | -0.40 | yes |
| fnd6_dlto | fundamental_debt | +0.03 | 1.91 | +0.51 | -0.87 | yes |
| unsystematic_risk_last_360_days | model51 | -0.03 | 1.91 | +0.51 | -0.73 | yes |

## Actionability
Blocked by LOW_FITNESS. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, rank_value_norm, trade_when
