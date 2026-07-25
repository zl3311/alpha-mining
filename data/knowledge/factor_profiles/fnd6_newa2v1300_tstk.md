---
field: fnd6_newa2v1300_tstk
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 0.82
best_fitness: 0.51
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 8
max_drawdown: 0.1073
ann_vol: 0.0586
hit_rate: 0.5093
rolling_sharpe_min: -2.093
rolling_sharpe_max: 2.651
top_merge_partner: anl4_rd_exp_flag
redundancy_cluster: 13
negated_best_sharpe: 0.64
negated_best_template: rank_neg_delta
negated_best_fitness: 0.34
n_negated_sims: 10
direction_gap: -0.18
---
# fnd6_newa2v1300_tstk (fundamental6)

*Treasury Stock - Total (All Capital)*

## Signal Profile
- `rank(fnd6_newa2v1300_tstk)`: S=0.68, F=0.40, T=0.9%, INFERIOR (TOP3000)
- `rank(fnd6_newa2v1300_tstk / close)`: S=0.82, F=0.51, T=0.9%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_newa2v1300_tstk, 5))`: S=0.40, F=0.23, T=22.5%, INFERIOR (TOP200)
- `-rank(fnd6_newa2v1300_tstk)`: S=-0.31, F=-0.13, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa2v1300_tstk, 5))`: S=0.64, F=0.34, T=34.4%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_newa2v1300_tstk, 22)`: S=0.20, F=0.10, T=17.7%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newa2v1300_tstk, 10)`: S=-0.05, F=-0.01, T=0.9%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newa2v1300_tstk, 22))`: S=-0.04, F=-0.01, T=16.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa2v1300_tstk)`: S=-0.31, F=-0.13, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa2v1300_tstk / close)`: S=-0.41, F=-0.20, T=1.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 11F/18P
- LOW_TURNOVER: 3F/29P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.81, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=1.27 (moderate), ret=+3.1%
  - 2020: S=-1.58 (negative), ret=-6.5%
  - 2021: S=1.68 (strong), ret=+11.2%
  - 2022: S=1.86 (strong), ret=+16.1%
  - 2023: S=-0.17 (negative), ret=-0.8%

## Risk & Drawdown
- Max drawdown: 10.73% over 761 days (recovered)
- Annualized: return +4.7%, volatility 5.9% (fraction of booksize)
- Hit rate: 50.9% positive days
- Tail shape: skew -0.02, excess kurtosis +1.98

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.09, max 2.65, latest -0.34

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +4.93%; worst month: -2.28%
Positive months: 58%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.99
- Sideways: S=0.94
- Bear: S=-2.21

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_newa2v1300_tstk, 5))` S=0.64, F=0.34, INFERIOR
Direction gap: -0.18 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_newa2v1300_tstk)`: S=-0.31, F=-0.13, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa2v1300_tstk / close)`: S=-0.41, F=-0.20, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa2v1300_tstk, 5))`: S=0.64, F=0.34, T=34.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newa2v1300_tstk / close)` | TOP3000 | 0.81 | 0.51 | 10.7% | 60% | bull-only |
| `rank(fnd6_newa2v1300_tstk)` | TOP3000 | 0.67 | 0.40 | 14.3% | 60% | bull-only |
| `rank(ts_delta(fnd6_newa2v1300_tstk, 5))` | TOP200 | 0.40 | 0.23 | 28.5% | 80% | bull-only |
| `rank(fnd6_newa2v1300_tstk / close)` | TOP1000 | 0.40 | 0.20 | 10.1% | 60% | bull-only |
| `rank(fnd6_newa2v1300_tstk)` | TOP1000 | 0.30 | 0.13 | 12.8% | 60% | bull-only |
| `rank(fnd6_newa2v1300_tstk / close)` | TOP500 | 0.29 | 0.13 | 14.1% | 60% | bull-only |
| `rank(ts_delta(fnd6_newa2v1300_tstk, 5))` | TOP500 | 0.25 | 0.09 | 39.2% | 80% | mixed |
| `rank(fnd6_newa2v1300_tstk)` | TOP500 | 0.17 | 0.06 | 17.8% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_tstkc: 0.997 (strongly positively correlated)
- fnd6_newqv1300_tstkq: 0.992 (strongly positively correlated)
- fnd6_newa2v1300_tstkn: 0.979 (strongly positively correlated)
- fnd6_newqv1300_tstknq: 0.968 (strongly positively correlated)
- fnd6_newa2v1300_oibdp: 0.932 (strongly positively correlated)

Redundancy cluster #13: 127 similar fields, mean |rho| 0.82 (representative: anl4_bvps_flag). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_rd_exp_flag | analyst4 | -0.50 | 1.71 | +0.68 | -0.91 | yes |
| max_adjusted_net_profit_guidance | analyst4 | -0.40 | 1.40 | +0.59 | -0.93 | yes |
| news_open_vol | news12 | -0.41 | 1.58 | +0.65 | -0.25 | yes |
| net_profit_adjusted_min_guidance | analyst4 | -0.34 | 1.50 | +0.55 | -0.95 | yes |
| fn_def_tax_assets_liab_net_a | fundamental2 | -0.43 | 1.47 | +0.56 | -0.48 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
