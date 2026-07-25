---
field: rp_ess_insider
dataset: news18
best_template: ts_mean
best_sharpe: 0.61
best_fitness: 0.28
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 20
regime_profile: all-weather
n_variations_with_pnl: 2
max_drawdown: 0.2057
ann_vol: 0.2003
hit_rate: 0.519
rolling_sharpe_min: -1.159
rolling_sharpe_max: 2.371
top_merge_partner: fnd2_propplteqflublgland
negated_best_sharpe: 0.39
negated_best_template: neg_rank_level
negated_best_fitness: 0.05
n_negated_sims: 4
direction_gap: -0.22
---
# rp_ess_insider (news18)

*Event sentiment score of insider trading news*

## Signal Profile
- `rank(rp_ess_insider)`: S=0.03, F=0.00, T=130.3%, INFERIOR (TOP200)
- `rank(ts_delta(rp_ess_insider, 5))`: S=0.82, F=0.27, T=150.0%, INFERIOR (TOP200)
- `-rank(rp_ess_insider)`: S=0.04, F=0.00, T=145.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(rp_ess_insider, 5))`: S=0.17, F=0.02, T=172.8%, INFERIOR (TOP3000)
- `-ts_zscore(rp_ess_insider, 63)`: S=0.10, F=0.01, T=147.3%, INFERIOR (TOP3000)
- `ts_mean(rp_ess_insider, 10)`: S=0.61, F=0.28, T=18.2%, INFERIOR (TOP3000)
- `rank(ts_rank(rp_ess_insider, 22))`: S=-0.29, F=-0.03, T=146.0%, INFERIOR (TOP3000)
- `rank(-1 * rp_ess_insider)`: S=0.39, F=0.05, T=154.9%, INFERIOR (TOP3000)
- `rank(-1 * rp_ess_insider / close)`: S=-0.74, F=-0.14, T=146.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 15F/5P
- HIGH_TURNOVER: 19F/1P
- LOW_FITNESS: 20F/0P
- LOW_SHARPE: 20F/0P
- LOW_SUB_UNIVERSE_SHARPE: 6F/12P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.83, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.03 (negative), ret=-0.5%
  - 2020: S=0.71 (moderate), ret=+18.1%
  - 2021: S=1.55 (strong), ret=+34.5%
  - 2022: S=1.80 (strong), ret=+39.1%
  - 2023: S=-1.01 (negative), ret=-9.5%

## Risk & Drawdown
- Max drawdown: 20.57% over 273 days (recovered)
- Annualized: return +16.7%, volatility 20.0% (fraction of booksize)
- Hit rate: 51.9% positive days
- Tail shape: skew +1.80, excess kurtosis +18.59

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.16, max 2.37, latest -0.94

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2023
Best month: +24.79%; worst month: -14.93%
Positive months: 49%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=1.07
- Sideways: S=-0.08
- Bear: S=1.37

## Negated Direction
Best negated: `rank(-1 * rp_ess_insider)` S=0.39, F=0.05, INFERIOR
Direction gap: -0.22 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * rp_ess_insider)`: S=0.39, F=0.05, T=154.9%, INFERIOR (TOP3000)
- `rank(-1 * rp_ess_insider / close)`: S=-0.74, F=-0.14, T=146.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(rp_ess_insider, 5))`: S=0.17, F=0.02, T=172.8%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(rp_ess_insider, 5))` | TOP200 | 0.83 | 0.27 | 20.6% | 60% | all-weather |
| `rank(ts_delta(rp_ess_insider, 5))` | TOP500 | 0.43 | 0.08 | 33.3% | 80% | all-weather |

## Correlation Notes
Top correlates:
- sales_growth: 0.136 (weakly positively correlated)
- fnd6_optca: -0.132 (weakly negatively correlated)
- fnd6_txds: 0.131 (weakly positively correlated)
- parkinson_volatility_20: 0.120 (weakly positively correlated)
- rp_nip_ptg: 0.115 (weakly positively correlated)

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| fnd2_propplteqflublgland | fundamental2 | -0.07 | 1.21 | +0.38 | -0.55 | yes |
| fn_comp_options_exercisable_number_a | fundamental2 | +0.02 | 1.20 | +0.31 | -0.93 | yes |
| reporting_currency_code_9 | analyst4 | -0.06 | 1.18 | +0.35 | -0.49 | yes |
| fnd2_ebitfr | fundamental2 | -0.11 | 1.28 | +0.40 | +0.22 | yes |
| fnd6_cimii | fundamental6 | +0.00 | 1.16 | +0.33 | -0.62 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, rank_value_norm, trade_when
