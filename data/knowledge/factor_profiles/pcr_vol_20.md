---
field: pcr_vol_20
dataset: option9
best_template: rank_level
best_sharpe: 1.14
best_fitness: 0.36
best_universe: TOP1000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 20
regime_profile: mixed
n_variations_with_pnl: 7
max_drawdown: 0.0705
ann_vol: 0.0444
hit_rate: 0.5409
rolling_sharpe_min: -0.395
rolling_sharpe_max: 2.514
top_merge_partner: fnd6_rank
redundancy_cluster: 23
negated_best_sharpe: -0.14
negated_best_template: neg_rank_value_norm
negated_best_fitness: -0.02
n_negated_sims: 4
direction_gap: -1.28
---
# pcr_vol_20 (option9)

*Ratio of put option volume to call option volume for options expiring in 20 days, signaling short-term options flow sentiment*

## Signal Profile
- `rank(pcr_vol_20)`: S=1.14, F=0.36, T=51.2%, INFERIOR (TOP1000)
- `rank(ts_delta(pcr_vol_20, 5))`: S=0.72, F=0.18, T=68.4%, INFERIOR (TOP200)
- `-rank(pcr_vol_20)`: S=-1.14, F=-0.36, T=51.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(pcr_vol_20, 5))`: S=-0.35, F=-0.04, T=84.3%, INFERIOR (TOP3000)
- `ts_zscore(pcr_vol_20, 22)`: S=0.78, F=0.18, T=58.1%, INFERIOR (TOP3000)
- `ts_mean(pcr_vol_20, 10)`: S=-0.14, F=-0.03, T=18.2%, INFERIOR (TOP3000)
- `rank(ts_rank(pcr_vol_20, 22))`: S=0.56, F=0.10, T=61.9%, INFERIOR (TOP3000)
- `rank(-1 * pcr_vol_20)`: S=-0.66, F=-0.14, T=60.6%, INFERIOR (TOP3000)
- `rank(-1 * pcr_vol_20 / close)`: S=-0.14, F=-0.02, T=58.7%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 19F/1P
- HIGH_TURNOVER: 6F/14P
- LOW_FITNESS: 20F/0P
- LOW_SHARPE: 20F/0P
- LOW_SUB_UNIVERSE_SHARPE: 8F/10P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 1.13, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=1.54 (strong), ret=+3.9%
  - 2020: S=0.62 (moderate), ret=+2.5%
  - 2021: S=1.50 (moderate), ret=+10.3%
  - 2022: S=0.60 (moderate), ret=+2.5%
  - 2023: S=1.91 (strong), ret=+5.5%

## Risk & Drawdown
- Max drawdown: 7.05% over 166 days (recovered)
- Annualized: return +5.0%, volatility 4.4% (fraction of booksize)
- Hit rate: 54.1% positive days
- Tail shape: skew +0.03, excess kurtosis +4.17

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.40, max 2.51, latest 1.74

## Yearly & Monthly Returns
Best year (by Sharpe): 2023; worst year: 2022
Best month: +2.91%; worst month: -2.46%
Positive months: 64%

## Regime Profile
Regime profile: **mixed**
- Bull: S=2.51
- Sideways: S=0.78
- Bear: S=-0.11

## Negated Direction
Best negated: `rank(-1 * pcr_vol_20 / close)` S=-0.14, F=-0.02, INFERIOR
Direction gap: -1.28 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * pcr_vol_20)`: S=-0.66, F=-0.14, T=60.6%, INFERIOR (TOP3000)
- `rank(-1 * pcr_vol_20 / close)`: S=-0.14, F=-0.02, T=58.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(pcr_vol_20, 5))`: S=-0.35, F=-0.04, T=84.3%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(pcr_vol_20)` | TOP1000 | 1.13 | 0.36 | 7.0% | 100% | mixed |
| `rank(pcr_vol_20)` | TOP500 | 0.74 | 0.22 | 8.2% | 100% | mixed |
| `rank(ts_delta(pcr_vol_20, 5))` | TOP200 | 0.71 | 0.18 | 9.4% | 80% | mixed |
| `rank(pcr_vol_20)` | TOP3000 | 0.67 | 0.14 | 6.8% | 60% | mixed |
| `rank(ts_delta(pcr_vol_20, 5))` | TOP1000 | 0.58 | 0.09 | 4.1% | 80% | weak |
| `rank(pcr_vol_20)` | TOP200 | 0.22 | 0.05 | 22.3% | 40% | mixed |
| `rank(ts_delta(pcr_vol_20, 5))` | TOP3000 | 0.37 | 0.04 | 4.7% | 60% | weak |

## Correlation Notes
Top correlates:
- pcr_vol_30: 0.886 (strongly positively correlated)
- pcr_vol_all: 0.883 (strongly positively correlated)
- pcr_vol_10: 0.652 (moderately positively correlated)
- correlation_last_360_days_spy: 0.561 (moderately positively correlated)
- pcr_oi_20: 0.555 (moderately positively correlated)

Redundancy cluster #23: 3 similar fields, mean |rho| 0.877 (representative). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| fnd6_rank | fundamental6 | -0.21 | 1.79 | +0.63 | +0.71 | yes |
| fn_comp_options_forfeitures_and_expirations_a | fundamental2 | -0.15 | 1.74 | +0.57 | -0.24 | yes |
| fn_def_tax_assets_liab_net_a | fundamental2 | -0.28 | 1.70 | +0.56 | +0.50 | yes |
| news_close_vol | news12 | -0.14 | 1.74 | +0.55 | -0.12 | yes |
| anl4_tbvps_high | analyst4 | -0.10 | 1.61 | +0.48 | -0.46 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, rank_value_norm, trade_when
