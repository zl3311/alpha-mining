---
field: anl4_ebitda_mean
dataset: analyst4
best_template: rank_value_norm
best_sharpe: 0.93
best_fitness: 0.75
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 9
max_drawdown: 0.1547
ann_vol: 0.0879
hit_rate: 0.5126
rolling_sharpe_min: -1.581
rolling_sharpe_max: 2.984
top_merge_partner: rp_ess_revenue
redundancy_cluster: 1
negated_best_sharpe: 0.34
negated_best_template: rank_neg_delta
negated_best_fitness: 0.08
n_negated_sims: 10
direction_gap: -0.59
---
# anl4_ebitda_mean (analyst4)

*Earnings before interest, taxes, depreciation and amortization - mean of estimations*

## Signal Profile
- `rank(anl4_ebitda_mean)`: S=0.51, F=0.36, T=1.0%, INFERIOR (TOP3000)
- `rank(anl4_ebitda_mean / close)`: S=0.93, F=0.75, T=1.4%, INFERIOR (TOP3000)
- `rank(ts_delta(anl4_ebitda_mean, 5))`: S=0.49, F=0.11, T=36.0%, INFERIOR (TOP3000)
- `-rank(anl4_ebitda_mean)`: S=-0.25, F=-0.13, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_ebitda_mean, 5))`: S=0.34, F=0.08, T=36.4%, INFERIOR (TOP3000)
- `ts_zscore(anl4_ebitda_mean, 22)`: S=-0.02, F=0.00, T=33.7%, INFERIOR (TOP3000)
- `ts_mean(anl4_ebitda_mean, 10)`: S=0.21, F=0.09, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_ebitda_mean, 22))`: S=-0.01, F=0.00, T=14.3%, INFERIOR (TOP3000)
- `rank(-1 * anl4_ebitda_mean)`: S=-0.15, F=-0.06, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * anl4_ebitda_mean / close)`: S=-0.22, F=-0.10, T=2.1%, INFERIOR (TOP3000)

## Check Summary
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 23F/6P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.92, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.09 (weak), ret=+0.4%
  - 2020: S=-0.86 (negative), ret=-7.0%
  - 2021: S=1.68 (strong), ret=+19.7%
  - 2022: S=1.93 (strong), ret=+21.0%
  - 2023: S=1.12 (moderate), ret=+5.6%

## Risk & Drawdown
- Max drawdown: 15.47% over 315 days (recovered)
- Annualized: return +8.1%, volatility 8.8% (fraction of booksize)
- Hit rate: 51.3% positive days
- Tail shape: skew +0.21, excess kurtosis +2.24

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.58, max 2.98, latest 0.97

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +10.04%; worst month: -3.48%
Positive months: 54%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.54
- Sideways: S=0.92
- Bear: S=-2.41

## Negated Direction
Best negated: `rank(-1 * ts_delta(anl4_ebitda_mean, 5))` S=0.34, F=0.08, INFERIOR
Direction gap: -0.59 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * anl4_ebitda_mean)`: S=-0.15, F=-0.06, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * anl4_ebitda_mean / close)`: S=-0.22, F=-0.10, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_ebitda_mean, 5))`: S=0.34, F=0.08, T=36.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_ebitda_mean / close)` | TOP3000 | 0.92 | 0.75 | 15.5% | 80% | bull-only |
| `rank(anl4_ebitda_mean)` | TOP3000 | 0.50 | 0.36 | 39.0% | 80% | bull-only |
| `rank(anl4_ebitda_mean / close)` | TOP1000 | 0.48 | 0.30 | 21.3% | 60% | bull-only |
| `rank(anl4_ebitda_mean)` | TOP1000 | 0.25 | 0.13 | 41.9% | 60% | bull-only |
| `rank(ts_delta(anl4_ebitda_mean, 5))` | TOP3000 | 0.52 | 0.11 | 6.8% | 60% | mixed |
| `rank(anl4_ebitda_mean / close)` | TOP500 | 0.21 | 0.10 | 36.0% | 60% | bull-only |
| `rank(anl4_ebitda_mean)` | TOP500 | 0.14 | 0.06 | 48.1% | 60% | bull-only |
| `rank(anl4_ebitda_mean / close)` | TOP200 | 0.13 | 0.05 | 33.0% | 60% | bull-only |
| `rank(anl4_ebitda_mean)` | TOP200 | 0.08 | 0.03 | 43.5% | 60% | bull-only |

## Correlation Notes
Top correlates:
- anl4_medianepsbfam: 1.000 (strongly positively correlated)
- anl4_ebitda_low: 0.997 (strongly positively correlated)
- anl4_ebitda_high: 0.996 (strongly positively correlated)
- est_ebitda: 0.994 (strongly positively correlated)
- anl4_ebit_high: 0.955 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| rp_ess_revenue | news18 | -0.34 | 1.57 | +0.65 | -0.80 | yes |
| anl4_rd_exp_flag | analyst4 | -0.43 | 1.81 | +0.79 | -0.74 | no |
| fnd6_txtubadjust | fundamental6 | -0.30 | 1.50 | +0.57 | -0.86 | yes |
| news_open_vol | news12 | -0.20 | 1.45 | +0.53 | -0.57 | yes |
| sharesout | pv1 | -0.20 | 1.54 | +0.51 | -0.68 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
