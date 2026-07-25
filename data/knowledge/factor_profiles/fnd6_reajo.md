---
field: fnd6_reajo
dataset: fundamental6
best_template: rank_delta
best_sharpe: 0.98
best_fitness: 0.69
best_universe: TOP500
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 6
max_drawdown: 0.2272
ann_vol: 0.1752
hit_rate: 0.5174
rolling_sharpe_min: -0.481
rolling_sharpe_max: 2.761
top_merge_partner: min_net_debt_guidance
negated_best_sharpe: 0.74
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.41
n_negated_sims: 10
direction_gap: -0.24
---
# fnd6_reajo (fundamental6)

*Retained Earnings - Other Adjustments*

## Signal Profile
- `rank(fnd6_reajo)`: S=0.26, F=0.13, T=3.2%, INFERIOR (TOP200)
- `rank(fnd6_reajo / close)`: S=0.24, F=0.11, T=3.3%, INFERIOR (TOP200)
- `rank(ts_delta(fnd6_reajo, 5))`: S=0.98, F=0.69, T=34.6%, INFERIOR (TOP500)
- `-rank(fnd6_reajo)`: S=0.10, F=0.02, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_reajo, 5))`: S=-0.16, F=-0.04, T=38.9%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_reajo, 22)`: S=0.46, F=0.28, T=23.9%, INFERIOR (TOP3000)
- `ts_mean(fnd6_reajo, 10)`: S=-0.36, F=-0.18, T=1.5%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_reajo, 22))`: S=0.89, F=0.61, T=19.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_reajo)`: S=0.59, F=0.30, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_reajo / close)`: S=0.74, F=0.41, T=1.7%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 10F/19P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.99, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=1.01 (moderate), ret=+18.2%
  - 2020: S=1.33 (moderate), ret=+26.5%
  - 2021: S=0.09 (weak), ret=+1.7%
  - 2022: S=0.28 (weak), ret=+3.0%
  - 2023: S=2.14 (strong), ret=+35.3%

## Risk & Drawdown
- Max drawdown: 22.72% over 313 days (recovered)
- Annualized: return +17.3%, volatility 17.5% (fraction of booksize)
- Hit rate: 51.7% positive days
- Tail shape: skew +0.89, excess kurtosis +13.20

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.48, max 2.76, latest 2.15

## Yearly & Monthly Returns
Best year (by Sharpe): 2023; worst year: 2021
Best month: +30.60%; worst month: -8.33%
Positive months: 56%

## Regime Profile
Regime profile: **mixed**
- Bull: S=1.59
- Sideways: S=1.36
- Bear: S=-0.16

## Negated Direction
Best negated: `rank(-1 * fnd6_reajo / close)` S=0.74, F=0.41, INFERIOR
Direction gap: -0.24 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_reajo)`: S=0.59, F=0.30, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_reajo / close)`: S=0.74, F=0.41, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_reajo, 5))`: S=-0.16, F=-0.04, T=38.9%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_reajo, 5))` | TOP500 | 0.99 | 0.69 | 22.7% | 100% | mixed |
| `rank(ts_delta(fnd6_reajo, 5))` | TOP200 | 0.51 | 0.30 | 24.9% | 80% | all-weather |
| `rank(ts_delta(fnd6_reajo, 5))` | TOP1000 | 0.53 | 0.25 | 29.8% | 80% | bull-only |
| `rank(fnd6_reajo)` | TOP200 | 0.27 | 0.13 | 34.8% | 60% | bear-only |
| `rank(fnd6_reajo / close)` | TOP200 | 0.26 | 0.11 | 33.6% | 60% | bear-only |
| `rank(ts_delta(fnd6_reajo, 5))` | TOP3000 | 0.18 | 0.04 | 26.8% | 60% | weak |

## Correlation Notes
Top correlates:
- fnd6_newa1v1300_aocipen: 0.446 (moderately positively correlated)
- fnd6_cidergl: 0.315 (weakly positively correlated)
- fnd6_newa1v1300_aociother: 0.167 (weakly positively correlated)
- rp_ess_credit_ratings: 0.150 (weakly positively correlated)
- fnd6_dd: 0.141 (weakly positively correlated)

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| min_net_debt_guidance | company_guidance | +0.00 | 1.42 | +0.39 | -0.78 | yes |
| max_net_debt_guidance | company_guidance | +0.00 | 1.42 | +0.39 | -0.78 | yes |
| fn_incremental_shares_attributable_to_share_based_payment_q | fundamental2 | -0.03 | 1.51 | +0.39 | -0.44 | yes |
| systematic_risk_last_360_days | model51 | -0.01 | 1.37 | +0.36 | -0.66 | yes |
| sales_ps | fundamental_value | -0.05 | 1.44 | +0.38 | -0.49 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
