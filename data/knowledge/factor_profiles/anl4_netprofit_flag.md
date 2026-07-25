---
field: anl4_netprofit_flag
dataset: analyst4
best_template: rank_level
best_sharpe: 1.27
best_fitness: 1.41
best_universe: TOP500
grade: AVERAGE
submittability: blocked_CONCENTRATED_WEIGHT
n_sims: 35
regime_profile: all-weather
n_variations_with_pnl: 10
max_drawdown: 0.1373
ann_vol: 0.1222
hit_rate: 0.5198
rolling_sharpe_min: 0.064
rolling_sharpe_max: 3.045
top_merge_partner: fnd6_fatl
negated_best_sharpe: 0.53
negated_best_template: rank_neg_delta
negated_best_fitness: 0.32
n_negated_sims: 10
direction_gap: -0.74
---
# anl4_netprofit_flag (analyst4)

*Net profit - forecast type (revision/new/...)*

## Signal Profile
- `rank(anl4_netprofit_flag)`: S=1.27, F=1.41, T=6.5%, AVERAGE (TOP500)
- `rank(anl4_netprofit_flag / close)`: S=0.29, F=0.15, T=2.5%, INFERIOR (TOP200)
- `rank(ts_delta(anl4_netprofit_flag, 5))`: S=0.44, F=0.27, T=34.0%, INFERIOR (TOP200)
- `ts_decay_linear(rank(anl4_netprofit_flag), 5)`: S=0.51, F=0.26, T=4.8%, INFERIOR (TOP3000)
- `-rank(anl4_netprofit_flag)`: S=-0.26, F=-0.11, T=5.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_netprofit_flag, 5))`: S=0.53, F=0.32, T=36.7%, INFERIOR (TOP3000)
- `-ts_zscore(anl4_netprofit_flag, 63)`: S=0.02, F=0.00, T=18.2%, INFERIOR (TOP3000)
- `ts_mean(anl4_netprofit_flag, 10)`: S=1.03, F=1.36, T=7.5%, AVERAGE (TOP3000)
- `rank(ts_rank(anl4_netprofit_flag, 22))`: S=0.31, F=0.15, T=17.5%, INFERIOR (TOP3000)
- `rank(-1 * anl4_netprofit_flag)`: S=-0.26, F=-0.11, T=5.8%, INFERIOR (TOP3000)
- `rank(-1 * anl4_netprofit_flag / close)`: S=-0.09, F=-0.03, T=2.0%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 15F/20P
- LOW_FITNESS: 33F/2P
- LOW_SHARPE: 34F/1P
- LOW_SUB_UNIVERSE_SHARPE: 15F/17P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 1.27, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.62 (moderate), ret=+4.6%
  - 2020: S=1.33 (moderate), ret=+16.7%
  - 2021: S=0.58 (moderate), ret=+8.7%
  - 2022: S=2.39 (strong), ret=+30.5%
  - 2023: S=1.49 (moderate), ret=+15.9%

## Risk & Drawdown
- Max drawdown: 13.73% over 275 days (recovered)
- Annualized: return +15.6%, volatility 12.2% (fraction of booksize)
- Hit rate: 52.0% positive days
- Tail shape: skew +0.28, excess kurtosis +3.15

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min 0.06, max 3.04, latest 1.44

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2021
Best month: +10.36%; worst month: -8.86%
Positive months: 73%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=0.81
- Sideways: S=1.75
- Bear: S=1.32

## Negated Direction
Best negated: `rank(-1 * ts_delta(anl4_netprofit_flag, 5))` S=0.53, F=0.32, INFERIOR
Direction gap: -0.74 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * anl4_netprofit_flag)`: S=-0.26, F=-0.11, T=5.8%, INFERIOR (TOP3000)
- `rank(-1 * anl4_netprofit_flag / close)`: S=-0.09, F=-0.03, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_netprofit_flag, 5))`: S=0.53, F=0.32, T=36.7%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_netprofit_flag)` | TOP500 | 1.27 | 1.41 | 13.7% | 100% | all-weather |
| `rank(anl4_netprofit_flag)` | TOP200 | 0.57 | 0.52 | 24.5% | 80% | mixed |
| `rank(ts_delta(anl4_netprofit_flag, 5))` | TOP200 | 0.43 | 0.27 | 32.3% | 60% | bull-only |
| `ts_decay_linear(rank(anl4_netprofit_flag), 5)` | TOP3000 | 0.52 | 0.26 | 18.1% | 80% | mixed |
| `rank(anl4_netprofit_flag)` | TOP3000 | 0.44 | 0.20 | 18.2% | 80% | weak |
| `rank(anl4_netprofit_flag / close)` | TOP200 | 0.30 | 0.15 | 21.6% | 80% | mixed |
| `rank(anl4_netprofit_flag)` | TOP1000 | 0.26 | 0.11 | 11.5% | 80% | weak |
| `rank(anl4_netprofit_flag / close)` | TOP500 | 0.14 | 0.04 | 31.3% | 60% | bear-only |
| `rank(anl4_netprofit_flag / close)` | TOP1000 | 0.09 | 0.03 | 37.6% | 40% | bear-only |
| `rank(ts_delta(anl4_netprofit_flag, 5))` | TOP3000 | 0.11 | 0.02 | 46.1% | 60% | weak |

## Correlation Notes
Top correlates:
- anl4_epsr_flag: 0.320 (weakly positively correlated)
- anl4_adjusted_netincome_ft: 0.288 (weakly positively correlated)
- anl4_ptp_flag: 0.282 (weakly positively correlated)
- anl4_flag_erbfintax: 0.268 (weakly positively correlated)
- fnd6_mkvalt: -0.171 (weakly negatively correlated)

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| fnd6_fatl | fundamental_capital_intensity | -0.05 | 1.78 | +0.50 | -0.69 | yes |
| news_mins_3_pct_dn | news12 | -0.02 | 1.89 | +0.52 | -0.33 | yes |
| pcr_vol_10 | option9 | -0.15 | 1.79 | +0.51 | -0.36 | yes |
| anl4_ffo_flag | analyst_revision_momentum | -0.04 | 1.88 | +0.54 | +0.83 | yes |
| fn_oth_income_loss_derivatives_qualifying_as_hedges_of_tax_q | fundamental2 | -0.05 | 1.75 | +0.48 | -0.54 | yes |

## Actionability
Blocked by CONCENTRATED_WEIGHT. Consider template changes or neutralization adjustment.
Untried templates: trade_when
