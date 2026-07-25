---
field: pcr_vol_30
dataset: option9
best_template: rank_level
best_sharpe: 1.14
best_fitness: 0.35
best_universe: TOP1000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 21
regime_profile: mixed
n_variations_with_pnl: 7
max_drawdown: 0.0744
ann_vol: 0.0443
hit_rate: 0.549
rolling_sharpe_min: -0.429
rolling_sharpe_max: 2.754
top_merge_partner: fnd6_rank
redundancy_cluster: 23
negated_best_sharpe: -0.17
negated_best_template: neg_rank_value_norm
negated_best_fitness: -0.03
n_negated_sims: 4
direction_gap: -1.31
---
# pcr_vol_30 (option9)

*Ratio of put volume to call volume on a stock's options with expiration 30 days in the future*

## Signal Profile
- `rank(pcr_vol_30)`: S=1.14, F=0.35, T=52.3%, INFERIOR (TOP1000)
- `rank(pcr_vol_30 / close)`: S=0.33, F=0.09, T=42.3%, INFERIOR (TOP3000)
- `rank(ts_delta(pcr_vol_30, 5))`: S=1.05, F=0.22, T=74.1%, INFERIOR (TOP1000)
- `-rank(pcr_vol_30)`: S=-1.14, F=-0.35, T=52.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(pcr_vol_30, 5))`: S=-0.66, F=-0.10, T=84.8%, INFERIOR (TOP3000)
- `ts_zscore(pcr_vol_30, 22)`: S=0.64, F=0.13, T=58.8%, INFERIOR (TOP3000)
- `ts_mean(pcr_vol_30, 10)`: S=0.29, F=0.09, T=18.4%, INFERIOR (TOP3000)
- `rank(ts_rank(pcr_vol_30, 22))`: S=0.74, F=0.15, T=62.7%, INFERIOR (TOP3000)
- `rank(-1 * pcr_vol_30)`: S=-0.67, F=-0.14, T=60.9%, INFERIOR (TOP3000)
- `rank(-1 * pcr_vol_30 / close)`: S=-0.17, F=-0.03, T=59.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 20F/1P
- HIGH_TURNOVER: 6F/15P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 21F/0P
- LOW_SUB_UNIVERSE_SHARPE: 7F/12P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 1.13, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=1.20 (moderate), ret=+3.1%
  - 2020: S=0.69 (moderate), ret=+3.0%
  - 2021: S=1.63 (strong), ret=+10.9%
  - 2022: S=0.29 (weak), ret=+1.2%
  - 2023: S=2.23 (strong), ret=+6.5%

## Risk & Drawdown
- Max drawdown: 7.44% over 184 days (recovered)
- Annualized: return +5.0%, volatility 4.4% (fraction of booksize)
- Hit rate: 54.9% positive days
- Tail shape: skew -0.12, excess kurtosis +4.04

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.43, max 2.75, latest 2.18

## Yearly & Monthly Returns
Best year (by Sharpe): 2023; worst year: 2022
Best month: +3.46%; worst month: -2.36%
Positive months: 63%

## Regime Profile
Regime profile: **mixed**
- Bull: S=2.62
- Sideways: S=0.89
- Bear: S=-0.34

## Negated Direction
Best negated: `rank(-1 * pcr_vol_30 / close)` S=-0.17, F=-0.03, INFERIOR
Direction gap: -1.31 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * pcr_vol_30)`: S=-0.67, F=-0.14, T=60.9%, INFERIOR (TOP3000)
- `rank(-1 * pcr_vol_30 / close)`: S=-0.17, F=-0.03, T=59.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(pcr_vol_30, 5))`: S=-0.66, F=-0.10, T=84.8%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(pcr_vol_30)` | TOP1000 | 1.13 | 0.35 | 7.4% | 100% | mixed |
| `rank(pcr_vol_30)` | TOP500 | 0.89 | 0.28 | 8.8% | 80% | mixed |
| `rank(ts_delta(pcr_vol_30, 5))` | TOP1000 | 1.08 | 0.22 | 3.9% | 80% | all-weather |
| `rank(pcr_vol_30)` | TOP3000 | 0.67 | 0.14 | 6.3% | 60% | mixed |
| `rank(ts_delta(pcr_vol_30, 5))` | TOP3000 | 0.69 | 0.10 | 4.1% | 60% | mixed |
| `rank(ts_delta(pcr_vol_30, 5))` | TOP500 | 0.32 | 0.04 | 6.5% | 60% | mixed |
| `rank(pcr_vol_30)` | TOP200 | 0.15 | 0.03 | 16.6% | 40% | weak |

## Correlation Notes
Top correlates:
- pcr_vol_20: 0.886 (strongly positively correlated)
- pcr_vol_all: 0.862 (strongly positively correlated)
- pcr_vol_10: 0.597 (moderately positively correlated)
- correlation_last_360_days_spy: 0.578 (moderately positively correlated)
- pcr_oi_30: 0.537 (moderately positively correlated)

Redundancy cluster #23: 3 similar fields, mean |rho| 0.877 (representative: pcr_vol_20). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| fnd6_rank | fundamental6 | -0.21 | 1.79 | +0.63 | +0.86 | yes |
| fn_comp_options_forfeitures_and_expirations_a | fundamental2 | -0.14 | 1.72 | +0.55 | +0.04 | yes |
| fn_def_tax_assets_liab_net_a | fundamental2 | -0.26 | 1.69 | +0.55 | +0.76 | yes |
| news_close_vol | news12 | -0.13 | 1.72 | +0.53 | -0.07 | yes |
| anl4_tbvps_high | analyst4 | -0.11 | 1.61 | +0.48 | -0.28 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
