---
field: fnd6_txtubadjust
dataset: fundamental6
best_template: rank_level
best_sharpe: 0.85
best_fitness: 0.62
best_universe: TOP200
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bear-only
n_variations_with_pnl: 8
max_drawdown: 0.1756
ann_vol: 0.0793
hit_rate: 0.5247
rolling_sharpe_min: -1.306
rolling_sharpe_max: 2.884
top_merge_partner: fnd2_currstatelocaltxexp
negated_best_sharpe: 0.78
negated_best_template: rank_neg_delta
negated_best_fitness: 0.57
n_negated_sims: 10
direction_gap: -0.07
---
# fnd6_txtubadjust (fundamental6)

*Other Unrecognized Tax Benefit Adjustment*

## Signal Profile
- `rank(fnd6_txtubadjust)`: S=0.85, F=0.62, T=3.2%, INFERIOR (TOP200)
- `rank(fnd6_txtubadjust / close)`: S=0.83, F=0.61, T=3.2%, INFERIOR (TOP200)
- `rank(ts_delta(fnd6_txtubadjust, 5))`: S=-0.14, F=-0.04, T=18.4%, INFERIOR (TOP500)
- `-rank(fnd6_txtubadjust)`: S=-0.51, F=-0.22, T=2.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_txtubadjust, 5))`: S=0.78, F=0.57, T=23.4%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_txtubadjust, 63)`: S=0.26, F=0.19, T=12.6%, INFERIOR (TOP3000)
- `ts_mean(fnd6_txtubadjust, 10)`: S=0.25, F=0.10, T=2.1%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_txtubadjust, 22))`: S=0.51, F=0.30, T=22.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_txtubadjust)`: S=-0.51, F=-0.22, T=2.7%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_txtubadjust / close)`: S=-0.50, F=-0.21, T=2.7%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 13F/19P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/15P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.85, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=2.15 (strong), ret=+12.0%
  - 2020: S=2.41 (strong), ret=+15.4%
  - 2021: S=1.14 (moderate), ret=+10.0%
  - 2022: S=-0.71 (negative), ret=-7.2%
  - 2023: S=0.40 (weak), ret=+2.8%

## Risk & Drawdown
- Max drawdown: 17.56% over 669 days (not yet recovered, ongoing at window end)
- Annualized: return +6.7%, volatility 7.9% (fraction of booksize)
- Hit rate: 52.5% positive days
- Tail shape: skew +0.10, excess kurtosis +2.96

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.31, max 2.88, latest 0.47

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2022
Best month: +8.27%; worst month: -3.40%
Positive months: 61%

## Regime Profile
Regime profile: **bear-only**
- Bull: S=-0.65
- Sideways: S=1.59
- Bear: S=1.86

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_txtubadjust, 5))` S=0.78, F=0.57, INFERIOR
Direction gap: -0.07 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_txtubadjust)`: S=-0.51, F=-0.22, T=2.7%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_txtubadjust / close)`: S=-0.50, F=-0.21, T=2.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_txtubadjust, 5))`: S=0.78, F=0.57, T=23.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_txtubadjust)` | TOP200 | 0.85 | 0.62 | 17.6% | 80% | bear-only |
| `rank(fnd6_txtubadjust / close)` | TOP200 | 0.83 | 0.61 | 17.8% | 80% | bear-only |
| `rank(fnd6_txtubadjust / close)` | TOP500 | 0.84 | 0.51 | 10.2% | 80% | bear-only |
| `rank(fnd6_txtubadjust)` | TOP500 | 0.84 | 0.51 | 10.4% | 80% | bear-only |
| `rank(fnd6_txtubadjust)` | TOP1000 | 0.53 | 0.22 | 14.1% | 80% | bear-only |
| `rank(fnd6_txtubadjust / close)` | TOP1000 | 0.52 | 0.21 | 14.1% | 80% | bear-only |
| `rank(fnd6_txtubadjust)` | TOP3000 | 0.42 | 0.14 | 9.7% | 60% | bear-only |
| `rank(fnd6_txtubadjust / close)` | TOP3000 | 0.40 | 0.13 | 9.5% | 60% | bear-only |

## Correlation Notes
Top correlates:
- fnd6_recta: 0.458 (moderately positively correlated)
- cashflow_fin: 0.433 (moderately positively correlated)
- fnd6_newa1v1300_fincf: 0.433 (moderately positively correlated)
- fnd6_dcvt: 0.432 (moderately positively correlated)
- fn_accum_oth_income_loss_net_of_tax_a: 0.430 (moderately positively correlated)

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| fnd2_currstatelocaltxexp | fundamental2 | -0.36 | 1.49 | +0.64 | -0.79 | yes |
| anl4_fcf_low | analyst4 | -0.37 | 1.50 | +0.65 | -0.62 | yes |
| anl4_fcf_mean | analyst4 | -0.35 | 1.55 | +0.64 | -0.67 | yes |
| anl4_fcf_median | analyst4 | -0.35 | 1.55 | +0.64 | -0.68 | yes |
| est_fcf_ps | analyst4 | -0.36 | 1.45 | +0.60 | -0.79 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
