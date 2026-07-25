---
field: anl4_afv4_dts_spe
dataset: analyst4
best_template: rank_value_norm
best_sharpe: 1.0
best_fitness: 0.87
best_universe: TOP500
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: all-weather
n_variations_with_pnl: 10
max_drawdown: 0.197
ann_vol: 0.0953
hit_rate: 0.5036
rolling_sharpe_min: -1.254
rolling_sharpe_max: 2.456
top_merge_partner: anl4_bvps_flag
negated_best_sharpe: 0.39
negated_best_template: rank_neg_delta
negated_best_fitness: 0.13
n_negated_sims: 10
direction_gap: -0.61
---
# anl4_afv4_dts_spe (analyst4)

*Earnings per share - standard deviation of estimations*

## Signal Profile
- `rank(anl4_afv4_dts_spe)`: S=0.92, F=0.62, T=4.9%, INFERIOR (TOP500)
- `rank(anl4_afv4_dts_spe / close)`: S=1.00, F=0.87, T=5.4%, INFERIOR (TOP500)
- `rank(ts_delta(anl4_afv4_dts_spe, 5))`: S=0.42, F=0.11, T=37.8%, INFERIOR (TOP500)
- `-rank(anl4_afv4_dts_spe)`: S=-0.60, F=-0.30, T=4.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_afv4_dts_spe, 5))`: S=0.39, F=0.13, T=37.0%, INFERIOR (TOP3000)
- `ts_zscore(anl4_afv4_dts_spe, 22)`: S=0.43, F=0.12, T=31.9%, INFERIOR (TOP3000)
- `ts_mean(anl4_afv4_dts_spe, 10)`: S=-0.01, F=0.00, T=3.2%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_afv4_dts_spe, 22))`: S=0.09, F=0.01, T=16.5%, INFERIOR (TOP3000)
- `rank(-1 * anl4_afv4_dts_spe)`: S=-0.45, F=-0.25, T=4.9%, INFERIOR (TOP3000)
- `rank(-1 * anl4_afv4_dts_spe / close)`: S=-0.70, F=-0.57, T=5.9%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 1F/31P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 4F/16P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 1.00, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=2.03 (strong), ret=+13.0%
  - 2020: S=1.28 (moderate), ret=+11.0%
  - 2021: S=-0.50 (negative), ret=-5.8%
  - 2022: S=0.92 (moderate), ret=+10.0%
  - 2023: S=2.21 (strong), ret=+18.4%

## Risk & Drawdown
- Max drawdown: 19.70% over 692 days (recovered)
- Annualized: return +9.5%, volatility 9.5% (fraction of booksize)
- Hit rate: 50.4% positive days
- Tail shape: skew +0.35, excess kurtosis +1.62

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.25, max 2.46, latest 2.25

## Yearly & Monthly Returns
Best year (by Sharpe): 2023; worst year: 2021
Best month: +7.98%; worst month: -4.66%
Positive months: 58%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=0.77
- Sideways: S=0.03
- Bear: S=2.19

## Negated Direction
Best negated: `rank(-1 * ts_delta(anl4_afv4_dts_spe, 5))` S=0.39, F=0.13, INFERIOR
Direction gap: -0.61 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * anl4_afv4_dts_spe)`: S=-0.45, F=-0.25, T=4.9%, INFERIOR (TOP3000)
- `rank(-1 * anl4_afv4_dts_spe / close)`: S=-0.70, F=-0.57, T=5.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_afv4_dts_spe, 5))`: S=0.39, F=0.13, T=37.0%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_afv4_dts_spe / close)` | TOP500 | 1.00 | 0.87 | 19.7% | 80% | all-weather |
| `rank(anl4_afv4_dts_spe)` | TOP500 | 0.91 | 0.62 | 10.3% | 80% | bull-only |
| `rank(anl4_afv4_dts_spe / close)` | TOP200 | 0.70 | 0.57 | 20.1% | 80% | all-weather |
| `rank(anl4_afv4_dts_spe)` | TOP1000 | 0.60 | 0.30 | 16.7% | 60% | bull-only |
| `rank(anl4_afv4_dts_spe)` | TOP200 | 0.44 | 0.25 | 17.1% | 40% | bull-only |
| `rank(anl4_afv4_dts_spe)` | TOP3000 | 0.51 | 0.21 | 18.5% | 60% | mixed |
| `rank(anl4_afv4_dts_spe / close)` | TOP1000 | 0.34 | 0.17 | 21.5% | 60% | mixed |
| `rank(ts_delta(anl4_afv4_dts_spe, 5))` | TOP500 | 0.40 | 0.11 | 12.9% | 60% | mixed |
| `rank(ts_delta(anl4_afv4_dts_spe, 5))` | TOP1000 | 0.44 | 0.10 | 8.4% | 60% | mixed |
| `rank(anl4_afv4_dts_spe / close)` | TOP3000 | 0.20 | 0.08 | 28.3% | 60% | bear-only |

## Correlation Notes
Top correlates:
- anl4_afv4_cfps_number: 0.718 (strongly positively correlated)
- anl4_afv4_div_number: 0.684 (moderately positively correlated)
- put_breakeven_1080: -0.682 (moderately negatively correlated)
- put_breakeven_720: -0.681 (moderately negatively correlated)
- put_breakeven_360: -0.680 (moderately negatively correlated)

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_bvps_flag | analyst_revision | -0.48 | 2.21 | +0.90 | -0.27 | yes |
| implied_volatility_mean_skew_180 | option8 | -0.47 | 1.98 | +0.92 | -0.01 | yes |
| rel_num_all | pv13 | -0.46 | 2.06 | +0.84 | -0.34 | yes |
| anl4_netdebt_flag | analyst_revision | -0.46 | 2.11 | +0.83 | -0.33 | yes |
| rel_num_comp | pv13 | -0.46 | 1.93 | +0.82 | -0.50 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
