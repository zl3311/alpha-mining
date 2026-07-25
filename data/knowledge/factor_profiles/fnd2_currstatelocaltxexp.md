---
field: fnd2_currstatelocaltxexp
dataset: fundamental2
best_template: rank_value_norm
best_sharpe: 0.85
best_fitness: 0.62
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 7
max_drawdown: 0.1232
ann_vol: 0.0772
hit_rate: 0.5215
rolling_sharpe_min: -1.127
rolling_sharpe_max: 2.137
top_merge_partner: anl4_rd_exp_flag
redundancy_cluster: 13
negated_best_sharpe: 0.55
negated_best_template: neg_rank_level
negated_best_fitness: 0.45
n_negated_sims: 10
direction_gap: -0.3
---
# fnd2_currstatelocaltxexp (fundamental2)

*Income Tax Expense, Current - State & Local*

## Signal Profile
- `rank(fnd2_currstatelocaltxexp)`: S=0.44, F=0.26, T=1.0%, INFERIOR (TOP3000)
- `rank(fnd2_currstatelocaltxexp / close)`: S=0.85, F=0.62, T=1.3%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd2_currstatelocaltxexp, 5))`: S=0.84, F=0.47, T=34.4%, INFERIOR (TOP3000)
- `-rank(fnd2_currstatelocaltxexp)`: S=0.02, F=0.00, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_currstatelocaltxexp, 5))`: S=-0.41, F=-0.21, T=28.9%, INFERIOR (TOP3000)
- `-ts_zscore(fnd2_currstatelocaltxexp, 63)`: S=-0.28, F=-0.14, T=16.8%, INFERIOR (TOP3000)
- `ts_mean(fnd2_currstatelocaltxexp, 10)`: S=-0.04, F=-0.01, T=0.9%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd2_currstatelocaltxexp, 22))`: S=0.45, F=0.23, T=15.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_currstatelocaltxexp)`: S=0.55, F=0.45, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_currstatelocaltxexp / close)`: S=0.51, F=0.39, T=2.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 11F/9P
- LOW_TURNOVER: 2F/30P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.84, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.81 (moderate), ret=+2.7%
  - 2020: S=-0.20 (negative), ret=-1.3%
  - 2021: S=0.92 (moderate), ret=+8.5%
  - 2022: S=1.70 (strong), ret=+18.6%
  - 2023: S=0.57 (moderate), ret=+3.3%

## Risk & Drawdown
- Max drawdown: 12.32% over 336 days (recovered)
- Annualized: return +6.5%, volatility 7.7% (fraction of booksize)
- Hit rate: 52.1% positive days
- Tail shape: skew +0.10, excess kurtosis +1.91

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.13, max 2.14, latest 0.45

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +5.83%; worst month: -2.79%
Positive months: 59%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.95
- Sideways: S=1.19
- Bear: S=-2.31

## Negated Direction
Best negated: `rank(-1 * fnd2_currstatelocaltxexp)` S=0.55, F=0.45, INFERIOR
Direction gap: -0.30 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd2_currstatelocaltxexp)`: S=0.55, F=0.45, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_currstatelocaltxexp / close)`: S=0.51, F=0.39, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_currstatelocaltxexp, 5))`: S=-0.41, F=-0.21, T=28.9%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd2_currstatelocaltxexp / close)` | TOP3000 | 0.84 | 0.62 | 12.3% | 80% | bull-only |
| `rank(ts_delta(fnd2_currstatelocaltxexp, 5))` | TOP3000 | 0.85 | 0.47 | 16.7% | 80% | mixed |
| `rank(ts_delta(fnd2_currstatelocaltxexp, 5))` | TOP1000 | 0.74 | 0.42 | 31.8% | 80% | mixed |
| `rank(fnd2_currstatelocaltxexp)` | TOP3000 | 0.43 | 0.26 | 27.7% | 80% | bull-only |
| `rank(ts_delta(fnd2_currstatelocaltxexp, 5))` | TOP500 | 0.31 | 0.12 | 38.2% | 60% | mixed |
| `rank(ts_delta(fnd2_currstatelocaltxexp, 5))` | TOP200 | 0.14 | 0.04 | 37.9% | 40% | mixed |
| `rank(fnd2_currstatelocaltxexp / close)` | TOP1000 | 0.10 | 0.04 | 20.6% | 40% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_txs: 0.951 (strongly positively correlated)
- fnd2_a_curritxexp: 0.949 (strongly positively correlated)
- fnd6_newa2v1300_oibdp: 0.942 (strongly positively correlated)
- ebitda: 0.942 (strongly positively correlated)
- fnd6_newa1v1300_ebitda: 0.942 (strongly positively correlated)

Redundancy cluster #13: 127 similar fields, mean |rho| 0.82 (representative: anl4_bvps_flag). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_rd_exp_flag | analyst4 | -0.52 | 1.86 | +0.84 | -0.92 | yes |
| fnd6_txtubadjust | fundamental6 | -0.36 | 1.49 | +0.64 | -0.79 | yes |
| max_adjusted_net_profit_guidance | analyst4 | -0.37 | 1.46 | +0.61 | -0.85 | yes |
| net_profit_adjusted_min_guidance | analyst4 | -0.32 | 1.53 | +0.58 | -0.80 | yes |
| news_open_vol | news12 | -0.36 | 1.56 | +0.64 | -0.18 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
