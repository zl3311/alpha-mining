---
field: anl4_medianepsbfam
dataset: analyst4
best_template: rank_value_norm
best_sharpe: 0.93
best_fitness: 0.75
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 10
max_drawdown: 0.1539
ann_vol: 0.0877
hit_rate: 0.5126
rolling_sharpe_min: -1.567
rolling_sharpe_max: 2.98
top_merge_partner: rp_ess_revenue
redundancy_cluster: 1
negated_best_sharpe: 0.12
negated_best_template: rank_neg_delta
negated_best_fitness: 0.02
n_negated_sims: 10
direction_gap: -0.81
---
# anl4_medianepsbfam (analyst4)

*Earnings before interest, taxes, depreciation and amortization - median of estimations*

## Signal Profile
- `rank(anl4_medianepsbfam)`: S=0.51, F=0.36, T=1.0%, INFERIOR (TOP3000)
- `rank(anl4_medianepsbfam / close)`: S=0.93, F=0.75, T=1.4%, INFERIOR (TOP3000)
- `rank(ts_delta(anl4_medianepsbfam, 5))`: S=0.47, F=0.10, T=36.4%, INFERIOR (TOP3000)
- `-rank(anl4_medianepsbfam)`: S=-0.25, F=-0.13, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_medianepsbfam, 5))`: S=0.12, F=0.02, T=36.9%, INFERIOR (TOP3000)
- `ts_zscore(anl4_medianepsbfam, 22)`: S=0.25, F=0.05, T=34.6%, INFERIOR (TOP3000)
- `ts_mean(anl4_medianepsbfam, 10)`: S=0.21, F=0.09, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_medianepsbfam, 22))`: S=-0.15, F=-0.03, T=14.2%, INFERIOR (TOP3000)
- `rank(-1 * anl4_medianepsbfam)`: S=-0.14, F=-0.05, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * anl4_medianepsbfam / close)`: S=-0.23, F=-0.10, T=2.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 1F/31P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 19F/10P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.93, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.09 (weak), ret=+0.5%
  - 2020: S=-0.85 (negative), ret=-6.9%
  - 2021: S=1.68 (strong), ret=+19.7%
  - 2022: S=1.92 (strong), ret=+20.8%
  - 2023: S=1.14 (moderate), ret=+5.6%

## Risk & Drawdown
- Max drawdown: 15.39% over 315 days (recovered)
- Annualized: return +8.1%, volatility 8.8% (fraction of booksize)
- Hit rate: 51.3% positive days
- Tail shape: skew +0.21, excess kurtosis +2.25

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.57, max 2.98, latest 0.99

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +10.03%; worst month: -3.45%
Positive months: 54%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.54
- Sideways: S=0.92
- Bear: S=-2.41

## Negated Direction
Best negated: `rank(-1 * ts_delta(anl4_medianepsbfam, 5))` S=0.12, F=0.02, INFERIOR
Direction gap: -0.81 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * anl4_medianepsbfam)`: S=-0.14, F=-0.05, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * anl4_medianepsbfam / close)`: S=-0.23, F=-0.10, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_medianepsbfam, 5))`: S=0.12, F=0.02, T=36.9%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_medianepsbfam / close)` | TOP3000 | 0.93 | 0.75 | 15.4% | 80% | bull-only |
| `rank(anl4_medianepsbfam)` | TOP3000 | 0.50 | 0.36 | 38.9% | 80% | bull-only |
| `rank(anl4_medianepsbfam / close)` | TOP1000 | 0.49 | 0.32 | 21.3% | 60% | bull-only |
| `rank(anl4_medianepsbfam)` | TOP1000 | 0.25 | 0.13 | 41.9% | 60% | bull-only |
| `rank(ts_delta(anl4_medianepsbfam, 5))` | TOP3000 | 0.52 | 0.10 | 7.2% | 60% | mixed |
| `rank(anl4_medianepsbfam / close)` | TOP500 | 0.22 | 0.10 | 36.2% | 60% | bull-only |
| `rank(anl4_medianepsbfam / close)` | TOP200 | 0.13 | 0.05 | 33.2% | 60% | bull-only |
| `rank(anl4_medianepsbfam)` | TOP500 | 0.13 | 0.05 | 48.2% | 60% | bull-only |
| `rank(ts_delta(anl4_medianepsbfam, 5))` | TOP200 | 0.19 | 0.04 | 13.3% | 60% | mixed |
| `rank(anl4_medianepsbfam)` | TOP200 | 0.07 | 0.03 | 43.4% | 60% | bull-only |

## Correlation Notes
Top correlates:
- anl4_ebitda_mean: 1.000 (strongly positively correlated)
- anl4_ebitda_low: 0.996 (strongly positively correlated)
- anl4_ebitda_high: 0.996 (strongly positively correlated)
- est_ebitda: 0.994 (strongly positively correlated)
- anl4_ebit_high: 0.954 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| rp_ess_revenue | news18 | -0.35 | 1.58 | +0.65 | -0.79 | yes |
| anl4_rd_exp_flag | analyst4 | -0.43 | 1.82 | +0.79 | -0.73 | no |
| fnd6_txtubadjust | fundamental6 | -0.30 | 1.50 | +0.57 | -0.87 | yes |
| news_open_vol | news12 | -0.20 | 1.45 | +0.53 | -0.58 | yes |
| sharesout | pv1 | -0.20 | 1.54 | +0.51 | -0.67 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
