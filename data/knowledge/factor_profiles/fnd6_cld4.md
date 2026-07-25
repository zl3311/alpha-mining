---
field: fnd6_cld4
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 1.13
best_fitness: 1.16
best_universe: TOP200
grade: AVERAGE
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: all-weather
n_variations_with_pnl: 8
max_drawdown: 0.1248
ann_vol: 0.118
hit_rate: 0.5344
rolling_sharpe_min: -0.145
rolling_sharpe_max: 3.2
top_merge_partner: anl4_rd_exp_flag
redundancy_cluster: 26
negated_best_sharpe: 0.47
negated_best_template: rank_neg_delta
negated_best_fitness: 0.24
n_negated_sims: 10
direction_gap: -0.66
---
# fnd6_cld4 (fundamental6)

*Capitalized Leases - Due in 4th Year*

## Signal Profile
- `rank(fnd6_cld4)`: S=1.11, F=1.14, T=3.8%, AVERAGE (TOP200)
- `rank(fnd6_cld4 / close)`: S=1.13, F=1.16, T=4.1%, AVERAGE (TOP200)
- `rank(ts_delta(fnd6_cld4, 5))`: S=0.03, F=0.00, T=30.5%, INFERIOR (TOP1000)
- `-rank(fnd6_cld4)`: S=-0.65, F=-0.40, T=2.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_cld4, 5))`: S=0.47, F=0.24, T=40.3%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_cld4, 63)`: S=0.08, F=0.03, T=12.4%, INFERIOR (TOP3000)
- `ts_mean(fnd6_cld4, 10)`: S=0.67, F=0.55, T=2.1%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_cld4, 22))`: S=0.26, F=0.14, T=21.3%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_cld4)`: S=-0.88, F=-0.61, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_cld4 / close)`: S=-1.22, F=-0.87, T=2.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 13F/19P
- LOW_FITNESS: 30F/2P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/16P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 1.12, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=1.35 (moderate), ret=+12.6%
  - 2020: S=-0.03 (negative), ret=-0.3%
  - 2021: S=2.47 (strong), ret=+35.0%
  - 2022: S=0.50 (moderate), ret=+6.7%
  - 2023: S=1.04 (moderate), ret=+10.5%

## Risk & Drawdown
- Max drawdown: 12.48% over 140 days (recovered)
- Annualized: return +13.2%, volatility 11.8% (fraction of booksize)
- Hit rate: 53.4% positive days
- Tail shape: skew +0.04, excess kurtosis +1.94

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.14, max 3.20, latest 1.12

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2020
Best month: +8.46%; worst month: -5.78%
Positive months: 63%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=1.52
- Sideways: S=0.70
- Bear: S=1.05

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_cld4, 5))` S=0.47, F=0.24, INFERIOR
Direction gap: -0.66 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_cld4)`: S=-0.88, F=-0.61, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_cld4 / close)`: S=-1.22, F=-0.87, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_cld4, 5))`: S=0.47, F=0.24, T=40.3%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_cld4 / close)` | TOP200 | 1.12 | 1.16 | 12.5% | 80% | all-weather |
| `rank(fnd6_cld4)` | TOP200 | 1.10 | 1.14 | 14.5% | 80% | all-weather |
| `rank(fnd6_cld4 / close)` | TOP500 | 1.11 | 0.95 | 10.2% | 100% | all-weather |
| `rank(fnd6_cld4 / close)` | TOP3000 | 1.22 | 0.87 | 4.4% | 100% | bull-only |
| `rank(fnd6_cld4)` | TOP500 | 0.97 | 0.79 | 10.5% | 80% | bull-only |
| `rank(fnd6_cld4)` | TOP3000 | 0.88 | 0.61 | 9.6% | 80% | bull-only |
| `rank(fnd6_cld4 / close)` | TOP1000 | 0.73 | 0.46 | 9.7% | 80% | bull-only |
| `rank(fnd6_cld4)` | TOP1000 | 0.65 | 0.40 | 12.3% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_cld5: 0.850 (strongly positively correlated)
- fnd6_loxdr: 0.413 (moderately positively correlated)
- fnd6_esopnr: 0.413 (moderately positively correlated)
- fnd6_dn: 0.412 (moderately positively correlated)
- fnd6_itcb: 0.412 (moderately positively correlated)

Redundancy cluster #26: 2 similar fields, mean |rho| 0.85 (representative). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_rd_exp_flag | analyst4 | -0.26 | 1.76 | +0.65 | -0.42 | yes |
| anl4_epsr_flag | analyst4 | -0.09 | 1.69 | +0.51 | -0.83 | yes |
| rp_ess_revenue | news18 | -0.19 | 1.58 | +0.47 | -0.90 | yes |
| anl4_afv4_dts_spe | analyst4 | -0.15 | 1.62 | +0.51 | -0.52 | yes |
| news_open_vol | news12 | -0.24 | 1.62 | +0.50 | -0.53 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
