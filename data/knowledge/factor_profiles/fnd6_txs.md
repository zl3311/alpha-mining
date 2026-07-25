---
field: fnd6_txs
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 0.85
best_fitness: 0.65
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 4
max_drawdown: 0.1309
ann_vol: 0.0863
hit_rate: 0.5093
rolling_sharpe_min: -1.289
rolling_sharpe_max: 2.555
top_merge_partner: anl4_rd_exp_flag
redundancy_cluster: 13
negated_best_sharpe: 0.48
negated_best_template: neg_rank_level
negated_best_fitness: 0.38
n_negated_sims: 10
direction_gap: -0.37
---
# fnd6_txs (fundamental6)

*Income Taxes - State*

## Signal Profile
- `rank(fnd6_txs)`: S=0.56, F=0.38, T=1.9%, INFERIOR (TOP3000)
- `rank(fnd6_txs / close)`: S=0.85, F=0.65, T=2.1%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_txs, 5))`: S=0.03, F=0.00, T=31.1%, INFERIOR (TOP500)
- `-rank(fnd6_txs)`: S=-0.08, F=-0.02, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_txs, 5))`: S=0.31, F=0.14, T=24.5%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_txs, 63)`: S=0.05, F=0.01, T=18.1%, INFERIOR (TOP3000)
- `ts_mean(fnd6_txs, 10)`: S=0.10, F=0.03, T=1.7%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_txs, 22))`: S=-0.30, F=-0.12, T=21.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_txs)`: S=0.48, F=0.38, T=3.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_txs / close)`: S=0.47, F=0.35, T=3.6%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/6P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.84, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.46 (weak), ret=+1.6%
  - 2020: S=-0.35 (negative), ret=-2.3%
  - 2021: S=1.53 (strong), ret=+16.3%
  - 2022: S=1.19 (moderate), ret=+14.6%
  - 2023: S=0.82 (moderate), ret=+5.4%

## Risk & Drawdown
- Max drawdown: 13.09% over 332 days (recovered)
- Annualized: return +7.2%, volatility 8.6% (fraction of booksize)
- Hit rate: 50.9% positive days
- Tail shape: skew +0.05, excess kurtosis +2.04

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.29, max 2.56, latest 0.67

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2020
Best month: +5.60%; worst month: -3.24%
Positive months: 54%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.87
- Sideways: S=0.84
- Bear: S=-1.87

## Negated Direction
Best negated: `rank(-1 * fnd6_txs)` S=0.48, F=0.38, INFERIOR
Direction gap: -0.37 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_txs)`: S=0.48, F=0.38, T=3.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_txs / close)`: S=0.47, F=0.35, T=3.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_txs, 5))`: S=0.31, F=0.14, T=24.5%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_txs / close)` | TOP3000 | 0.84 | 0.65 | 13.1% | 80% | bull-only |
| `rank(fnd6_txs)` | TOP3000 | 0.55 | 0.38 | 24.1% | 80% | bull-only |
| `rank(fnd6_txs / close)` | TOP1000 | 0.22 | 0.11 | 17.6% | 40% | bull-only |
| `rank(fnd6_txs)` | TOP1000 | 0.07 | 0.02 | 30.5% | 40% | bull-only |

## Correlation Notes
Top correlates:
- fnd2_currstatelocaltxexp: 0.951 (strongly positively correlated)
- fnd6_txc: 0.936 (strongly positively correlated)
- fnd6_oprepsx: 0.934 (strongly positively correlated)
- fnd6_mfma2_opeps: 0.934 (strongly positively correlated)
- fnd6_newa2v1300_opeps: 0.934 (strongly positively correlated)

Redundancy cluster #13: 127 similar fields, mean |rho| 0.82 (representative: anl4_bvps_flag). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_rd_exp_flag | analyst4 | -0.52 | 1.90 | +0.87 | -0.73 | yes |
| news_open_vol | news12 | -0.44 | 1.64 | +0.71 | -0.64 | yes |
| max_adjusted_net_profit_guidance | analyst4 | -0.39 | 1.49 | +0.65 | -0.93 | yes |
| anl4_afv4_dts_spe | analyst4 | -0.39 | 1.66 | +0.67 | -0.55 | yes |
| net_profit_adjusted_min_guidance | analyst4 | -0.34 | 1.55 | +0.61 | -0.94 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
