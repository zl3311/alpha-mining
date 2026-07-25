---
field: pv13_revere_company_total
dataset: pv13
best_template: rank_delta
best_sharpe: 1.04
best_fitness: 0.91
best_universe: TOP500
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 24
regime_profile: mixed
n_variations_with_pnl: 5
max_drawdown: 0.2953
ann_vol: 0.2091
hit_rate: 0.5215
rolling_sharpe_min: -1.887
rolling_sharpe_max: 2.53
top_merge_partner: fnd6_cisecgl
negated_best_sharpe: 0.98
negated_best_template: rank_neg_delta
negated_best_fitness: 0.7
n_negated_sims: 10
direction_gap: -0.06
---
# pv13_revere_company_total (pv13)

*Total number of companies in the sector*

## Signal Profile
- `rank(pv13_revere_company_total)`: S=0.90, F=0.56, T=1.6%, INFERIOR (TOP1000)
- `rank(ts_delta(pv13_revere_company_total, 5))`: S=1.04, F=0.91, T=28.5%, INFERIOR (TOP500)
- `-rank(pv13_revere_company_total)`: S=-0.90, F=-0.56, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(pv13_revere_company_total, 5))`: S=0.98, F=0.70, T=28.0%, INFERIOR (TOP3000)
- `ts_zscore(pv13_revere_company_total, 22)`: S=0.32, F=0.15, T=9.6%, INFERIOR (TOP3000)
- `ts_mean(pv13_revere_company_total, 10)`: S=0.57, F=0.36, T=1.5%, INFERIOR (TOP3000)
- `rank(ts_rank(pv13_revere_company_total, 22))`: S=-0.54, F=-0.41, T=12.1%, INFERIOR (TOP3000)
- `rank(-1 * pv13_revere_company_total)`: S=0.35, F=0.11, T=1.1%, INFERIOR (TOP3000)
- `rank(-1 * pv13_revere_company_total / close)`: S=0.13, F=0.04, T=1.6%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 11F/13P
- LOW_FITNESS: 24F/0P
- LOW_SHARPE: 24F/0P
- LOW_SUB_UNIVERSE_SHARPE: 11F/11P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 1.05, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.16 (weak), ret=+1.2%
  - 2020: S=2.18 (strong), ret=+52.0%
  - 2021: S=0.65 (moderate), ret=+18.3%
  - 2022: S=-0.64 (negative), ret=-10.2%
  - 2023: S=2.34 (strong), ret=+46.7%

## Risk & Drawdown
- Max drawdown: 29.53% over 283 days (recovered)
- Annualized: return +22.1%, volatility 20.9% (fraction of booksize)
- Hit rate: 52.1% positive days
- Tail shape: skew +1.35, excess kurtosis +14.46

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.89, max 2.53, latest 2.33

## Yearly & Monthly Returns
Best year (by Sharpe): 2023; worst year: 2022
Best month: +19.21%; worst month: -9.79%
Positive months: 63%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.31
- Sideways: S=1.18
- Bear: S=1.72

## Negated Direction
Best negated: `rank(-1 * ts_delta(pv13_revere_company_total, 5))` S=0.98, F=0.70, INFERIOR
Direction gap: -0.06 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * pv13_revere_company_total)`: S=0.35, F=0.11, T=1.1%, INFERIOR (TOP3000)
- `rank(-1 * pv13_revere_company_total / close)`: S=0.13, F=0.04, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(pv13_revere_company_total, 5))`: S=0.98, F=0.70, T=28.0%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(pv13_revere_company_total, 5))` | TOP500 | 1.05 | 0.91 | 29.5% | 80% | mixed |
| `rank(pv13_revere_company_total)` | TOP1000 | 0.89 | 0.56 | 6.3% | 80% | all-weather |
| `rank(pv13_revere_company_total)` | TOP500 | 0.34 | 0.16 | 13.5% | 60% | mixed |
| `rank(ts_delta(pv13_revere_company_total, 5))` | TOP200 | 0.27 | 0.13 | 36.4% | 60% | bull-only |
| `rank(pv13_revere_company_total)` | TOP200 | 0.09 | 0.03 | 23.2% | 40% | all-weather |

## Correlation Notes
Top correlates:
- pcr_vol_20: 0.131 (weakly positively correlated)
- implied_volatility_mean_skew_180: 0.127 (weakly positively correlated)
- fnd6_newqv1300_msaq: 0.125 (weakly positively correlated)
- implied_volatility_mean_skew_270: 0.125 (weakly positively correlated)
- min_investing_cashflow_guidance_2: 0.125 (weakly positively correlated)

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| fnd6_cisecgl | fundamental6 | -0.06 | 1.49 | +0.43 | -0.51 | yes |
| fnd6_optosby | fundamental6 | +0.01 | 1.47 | +0.41 | -0.61 | yes |
| fn_payments_to_acquire_businesses_net_of_cash_acquired_a | fundamental2 | -0.03 | 1.62 | +0.40 | -0.69 | yes |
| fnd6_mrc1 | fundamental6 | -0.04 | 1.68 | +0.41 | -0.61 | yes |
| fnd6_currencya_curcd | fundamental6 | +0.04 | 1.45 | +0.39 | -0.67 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, rank_value_norm, trade_when
