---
field: anl4_tbvps_number
dataset: analyst4
best_template: rank_level
best_sharpe: 0.85
best_fitness: 0.7
best_universe: TOP500
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 8
max_drawdown: 0.1126
ann_vol: 0.1008
hit_rate: 0.5206
rolling_sharpe_min: -0.775
rolling_sharpe_max: 2.551
top_merge_partner: rp_css_revenue
negated_best_sharpe: 0.74
negated_best_template: rank_neg_delta
negated_best_fitness: 0.52
n_negated_sims: 10
direction_gap: -0.11
---
# anl4_tbvps_number (analyst4)

*Tangible Book Value per Share - number of estimations*

## Signal Profile
- `rank(anl4_tbvps_number)`: S=0.85, F=0.70, T=4.4%, INFERIOR (TOP500)
- `rank(anl4_tbvps_number / close)`: S=0.47, F=0.26, T=2.4%, INFERIOR (TOP3000)
- `rank(ts_delta(anl4_tbvps_number, 5))`: S=0.11, F=0.03, T=35.7%, INFERIOR (TOP500)
- `-rank(anl4_tbvps_number)`: S=-0.50, F=-0.27, T=4.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_tbvps_number, 5))`: S=0.74, F=0.52, T=30.3%, INFERIOR (TOP3000)
- `-ts_zscore(anl4_tbvps_number, 63)`: S=-0.01, F=0.00, T=15.7%, INFERIOR (TOP3000)
- `ts_mean(anl4_tbvps_number, 10)`: S=0.63, F=0.45, T=3.8%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_tbvps_number, 22))`: S=-0.44, F=-0.25, T=14.6%, INFERIOR (TOP3000)
- `rank(-1 * anl4_tbvps_number)`: S=-0.15, F=-0.06, T=4.6%, INFERIOR (TOP3000)
- `rank(-1 * anl4_tbvps_number / close)`: S=0.27, F=0.14, T=3.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 16F/16P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 6F/14P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.86, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=1.43 (moderate), ret=+9.8%
  - 2020: S=0.62 (moderate), ret=+5.9%
  - 2021: S=0.12 (weak), ret=+1.2%
  - 2022: S=0.87 (moderate), ret=+8.5%
  - 2023: S=1.42 (moderate), ret=+17.0%

## Risk & Drawdown
- Max drawdown: 11.26% over 208 days (recovered)
- Annualized: return +8.6%, volatility 10.1% (fraction of booksize)
- Hit rate: 52.1% positive days
- Tail shape: skew +0.31, excess kurtosis +4.61

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.78, max 2.55, latest 1.43

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2021
Best month: +8.81%; worst month: -5.87%
Positive months: 59%

## Regime Profile
Regime profile: **mixed**
- Bull: S=-0.02
- Sideways: S=1.31
- Bear: S=1.27

## Negated Direction
Best negated: `rank(-1 * ts_delta(anl4_tbvps_number, 5))` S=0.74, F=0.52, INFERIOR
Direction gap: -0.11 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * anl4_tbvps_number)`: S=-0.15, F=-0.06, T=4.6%, INFERIOR (TOP3000)
- `rank(-1 * anl4_tbvps_number / close)`: S=0.27, F=0.14, T=3.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_tbvps_number, 5))`: S=0.74, F=0.52, T=30.3%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_tbvps_number)` | TOP500 | 0.86 | 0.70 | 11.3% | 100% | mixed |
| `rank(anl4_tbvps_number)` | TOP3000 | 0.96 | 0.53 | 3.9% | 100% | all-weather |
| `rank(anl4_tbvps_number)` | TOP1000 | 0.51 | 0.27 | 12.7% | 60% | mixed |
| `rank(anl4_tbvps_number / close)` | TOP3000 | 0.47 | 0.26 | 15.8% | 80% | mixed |
| `rank(anl4_tbvps_number / close)` | TOP500 | 0.30 | 0.15 | 26.3% | 80% | mixed |
| `rank(anl4_tbvps_number)` | TOP200 | 0.15 | 0.06 | 30.5% | 60% | mixed |
| `rank(anl4_tbvps_number / close)` | TOP1000 | 0.13 | 0.04 | 21.3% | 80% | mixed |
| `rank(ts_delta(anl4_tbvps_number, 5))` | TOP500 | 0.11 | 0.03 | 69.3% | 40% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_beta: 0.227 (weakly positively correlated)
- fn_comp_non_opt_vested_a: 0.217 (weakly positively correlated)
- anl4_qf_az_div_number: 0.215 (weakly positively correlated)
- anl4_qfd1_az_div_number: 0.215 (weakly positively correlated)
- anl4_tbvps_high: 0.214 (weakly positively correlated)

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| rp_css_revenue | news18 | -0.10 | 1.27 | +0.41 | -0.38 | yes |
| rp_css_ptg | news18 | -0.04 | 1.34 | +0.34 | -0.92 | yes |
| fnd6_aqc | fundamental6 | -0.04 | 1.19 | +0.33 | -0.99 | yes |
| implied_volatility_mean_skew_150 | option8 | -0.10 | 1.27 | +0.41 | +0.32 | yes |
| fnd2_a_sbcpnargmpmtwopsffesip | fundamental2 | -0.07 | 1.26 | +0.40 | +0.04 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
