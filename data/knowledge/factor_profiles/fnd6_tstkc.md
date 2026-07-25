---
field: fnd6_tstkc
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 0.83
best_fitness: 0.52
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 8
max_drawdown: 0.1097
ann_vol: 0.059
hit_rate: 0.5093
rolling_sharpe_min: -2.133
rolling_sharpe_max: 2.642
top_merge_partner: anl4_rd_exp_flag
redundancy_cluster: 13
negated_best_sharpe: 0.75
negated_best_template: rank_neg_delta
negated_best_fitness: 0.41
n_negated_sims: 10
direction_gap: -0.08
---
# fnd6_tstkc (fundamental6)

*Treasury Stock - Common*

## Signal Profile
- `rank(fnd6_tstkc)`: S=0.70, F=0.41, T=1.6%, INFERIOR (TOP3000)
- `rank(fnd6_tstkc / close)`: S=0.83, F=0.52, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_tstkc, 5))`: S=0.21, F=0.08, T=20.1%, INFERIOR (TOP200)
- `-rank(fnd6_tstkc)`: S=-0.31, F=-0.13, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_tstkc, 5))`: S=0.75, F=0.41, T=37.9%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_tstkc, 22)`: S=0.04, F=0.01, T=16.0%, INFERIOR (TOP3000)
- `ts_mean(fnd6_tstkc, 10)`: S=-0.11, F=-0.03, T=1.4%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_tstkc, 22))`: S=-0.05, F=-0.01, T=18.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_tstkc)`: S=-0.70, F=-0.41, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_tstkc / close)`: S=-0.83, F=-0.52, T=1.6%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 20F/9P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.82, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=1.18 (moderate), ret=+2.9%
  - 2020: S=-1.61 (negative), ret=-6.6%
  - 2021: S=1.65 (strong), ret=+11.3%
  - 2022: S=1.90 (strong), ret=+16.5%
  - 2023: S=-0.07 (negative), ret=-0.4%

## Risk & Drawdown
- Max drawdown: 10.97% over 761 days (recovered)
- Annualized: return +4.8%, volatility 5.9% (fraction of booksize)
- Hit rate: 50.9% positive days
- Tail shape: skew -0.03, excess kurtosis +2.11

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.13, max 2.64, latest -0.24

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +4.97%; worst month: -2.33%
Positive months: 59%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.03
- Sideways: S=0.94
- Bear: S=-2.21

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_tstkc, 5))` S=0.75, F=0.41, INFERIOR
Direction gap: -0.08 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_tstkc)`: S=-0.70, F=-0.41, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_tstkc / close)`: S=-0.83, F=-0.52, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_tstkc, 5))`: S=0.75, F=0.41, T=37.9%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_tstkc / close)` | TOP3000 | 0.82 | 0.52 | 11.0% | 60% | bull-only |
| `rank(fnd6_tstkc)` | TOP3000 | 0.69 | 0.41 | 14.5% | 60% | bull-only |
| `rank(fnd6_tstkc / close)` | TOP1000 | 0.38 | 0.19 | 10.8% | 60% | bull-only |
| `rank(fnd6_tstkc)` | TOP1000 | 0.29 | 0.13 | 13.2% | 60% | bull-only |
| `rank(fnd6_tstkc / close)` | TOP500 | 0.27 | 0.11 | 16.0% | 60% | bull-only |
| `rank(ts_delta(fnd6_tstkc, 5))` | TOP200 | 0.20 | 0.08 | 27.2% | 60% | weak |
| `rank(fnd6_tstkc)` | TOP500 | 0.15 | 0.05 | 19.6% | 60% | bull-only |
| `rank(ts_delta(fnd6_tstkc, 5))` | TOP500 | 0.12 | 0.04 | 45.2% | 60% | weak |

## Correlation Notes
Top correlates:
- fnd6_newa2v1300_tstk: 0.997 (strongly positively correlated)
- fnd6_newqv1300_tstkq: 0.989 (strongly positively correlated)
- fnd6_newa2v1300_tstkn: 0.979 (strongly positively correlated)
- fnd6_newqv1300_tstknq: 0.967 (strongly positively correlated)
- fnd6_newa2v1300_oibdp: 0.929 (strongly positively correlated)

Redundancy cluster #13: 127 similar fields, mean |rho| 0.82 (representative: anl4_bvps_flag). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_rd_exp_flag | analyst4 | -0.50 | 1.72 | +0.69 | -0.92 | yes |
| news_open_vol | news12 | -0.41 | 1.59 | +0.67 | -0.27 | yes |
| max_adjusted_net_profit_guidance | analyst4 | -0.40 | 1.41 | +0.59 | -0.94 | yes |
| net_profit_adjusted_min_guidance | analyst4 | -0.35 | 1.51 | +0.57 | -0.95 | yes |
| fn_def_tax_assets_liab_net_a | fundamental2 | -0.43 | 1.48 | +0.57 | -0.45 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
