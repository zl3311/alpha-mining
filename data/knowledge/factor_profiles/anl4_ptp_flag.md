---
field: anl4_ptp_flag
dataset: analyst4
best_template: rank_level
best_sharpe: 1.42
best_fitness: 2.31
best_universe: TOP500
grade: EXCELLENT
submittability: blocked_CONCENTRATED_WEIGHT
n_sims: 35
regime_profile: all-weather
n_variations_with_pnl: 8
max_drawdown: 0.2087
ann_vol: 0.2341
hit_rate: 0.5223
rolling_sharpe_min: -0.086
rolling_sharpe_max: 2.869
top_merge_partner: fn_assets_fair_val_a
negated_best_sharpe: 0.56
negated_best_template: rank_neg_delta
negated_best_fitness: 0.41
n_negated_sims: 10
direction_gap: -0.86
---
# anl4_ptp_flag (analyst4)

*Pretax income - forecast type (revision/new/...)*

## Signal Profile
- `rank(anl4_ptp_flag)`: S=1.42, F=2.31, T=4.9%, EXCELLENT (TOP500)
- `rank(anl4_ptp_flag / close)`: S=0.29, F=0.15, T=2.5%, INFERIOR (TOP200)
- `rank(ts_delta(anl4_ptp_flag, 5))`: S=0.01, F=0.00, T=13.3%, INFERIOR (TOP200)
- `ts_decay_linear(rank(anl4_ptp_flag), 5)`: S=1.47, F=1.46, T=3.5%, AVERAGE (TOP3000)
- `-rank(anl4_ptp_flag)`: S=-1.03, F=-1.24, T=5.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_ptp_flag, 5))`: S=0.56, F=0.41, T=32.7%, INFERIOR (TOP3000)
- `ts_zscore(anl4_ptp_flag, 22)`: S=0.44, F=0.56, T=5.6%, INFERIOR (TOP3000)
- `ts_mean(anl4_ptp_flag, 10)`: S=1.00, F=1.51, T=7.8%, GOOD (TOP3000)
- `rank(ts_rank(anl4_ptp_flag, 22))`: S=-0.03, F=-0.01, T=17.5%, INFERIOR (TOP3000)
- `rank(-1 * anl4_ptp_flag)`: S=-1.45, F=-1.43, T=3.6%, INFERIOR (TOP3000)
- `rank(-1 * anl4_ptp_flag / close)`: S=0.01, F=0.00, T=1.9%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 15F/20P
- LOW_FITNESS: 27F/8P
- LOW_SHARPE: 31F/4P
- LOW_SUB_UNIVERSE_SHARPE: 13F/19P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 1.44, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=1.09 (moderate), ret=+11.3%
  - 2020: S=2.28 (strong), ret=+40.5%
  - 2021: S=1.19 (moderate), ret=+42.5%
  - 2022: S=2.05 (strong), ret=+57.2%
  - 2023: S=1.01 (moderate), ret=+13.3%

## Risk & Drawdown
- Max drawdown: 20.87% over 204 days (recovered)
- Annualized: return +33.6%, volatility 23.4% (fraction of booksize)
- Hit rate: 52.2% positive days
- Tail shape: skew +0.63, excess kurtosis +8.07

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.09, max 2.87, latest 0.96

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2023
Best month: +41.12%; worst month: -11.78%
Positive months: 64%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=1.19
- Sideways: S=1.03
- Bear: S=2.03

## Negated Direction
Best negated: `rank(-1 * ts_delta(anl4_ptp_flag, 5))` S=0.56, F=0.41, INFERIOR
Direction gap: -0.86 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * anl4_ptp_flag)`: S=-1.45, F=-1.43, T=3.6%, INFERIOR (TOP3000)
- `rank(-1 * anl4_ptp_flag / close)`: S=0.01, F=0.00, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_ptp_flag, 5))`: S=0.56, F=0.41, T=32.7%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_ptp_flag)` | TOP500 | 1.44 | 2.31 | 20.9% | 100% | all-weather |
| `ts_decay_linear(rank(anl4_ptp_flag), 5)` | TOP3000 | 1.46 | 1.46 | 8.0% | 100% | all-weather |
| `rank(anl4_ptp_flag)` | TOP3000 | 1.43 | 1.43 | 8.1% | 100% | all-weather |
| `rank(anl4_ptp_flag)` | TOP1000 | 1.04 | 1.24 | 20.8% | 100% | mixed |
| `rank(anl4_ptp_flag)` | TOP200 | 0.38 | 0.36 | 54.0% | 80% | bull-only |
| `rank(anl4_ptp_flag / close)` | TOP200 | 0.30 | 0.15 | 21.6% | 80% | mixed |
| `rank(anl4_ptp_flag / close)` | TOP500 | 0.19 | 0.07 | 30.0% | 60% | bear-only |
| `rank(anl4_ptp_flag / close)` | TOP1000 | 0.16 | 0.06 | 35.7% | 40% | bear-only |

## Correlation Notes
Top correlates:
- anl4_netprofit_flag: 0.282 (weakly positively correlated)
- fnd6_dltis: 0.256 (weakly positively correlated)
- fnd6_cptmfmq_atq: 0.248 (weakly positively correlated)
- fn_proceeds_from_issuance_of_debt_a: 0.248 (weakly positively correlated)
- fnd6_cptnewqv1300_atq: 0.246 (weakly positively correlated)

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| fn_assets_fair_val_a | fundamental2 | -0.00 | 2.00 | +0.56 | -0.48 | yes |
| fn_line_of_credit_facility_amount_out_a | fundamental2 | -0.00 | 1.93 | +0.50 | -0.44 | yes |
| fnd6_mrc1 | fundamental6 | -0.04 | 1.96 | +0.53 | +0.07 | yes |
| fnd6_nopio | fundamental6 | -0.04 | 1.96 | +0.52 | -0.03 | yes |
| fnd6_mrct | fundamental6 | +0.04 | 2.04 | +0.51 | +0.18 | yes |

## Actionability
Cataloged as active factor but not yet in submitted book.
Blocked by CONCENTRATED_WEIGHT. Consider template changes or neutralization adjustment.
Untried templates: trade_when
