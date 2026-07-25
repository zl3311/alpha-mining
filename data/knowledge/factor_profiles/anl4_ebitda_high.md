---
field: anl4_ebitda_high
dataset: analyst4
best_template: rank_value_norm
best_sharpe: 0.97
best_fitness: 0.78
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 9
max_drawdown: 0.1451
ann_vol: 0.0845
hit_rate: 0.519
rolling_sharpe_min: -1.427
rolling_sharpe_max: 2.924
top_merge_partner: rp_ess_revenue
redundancy_cluster: 1
negated_best_sharpe: 0.16
negated_best_template: rank_neg_delta
negated_best_fitness: 0.03
n_negated_sims: 10
direction_gap: -0.81
---
# anl4_ebitda_high (analyst4)

*Earnings before interest, taxes, depreciation, and amortization - the highest estimation*

## Signal Profile
- `rank(anl4_ebitda_high)`: S=0.53, F=0.38, T=1.1%, INFERIOR (TOP3000)
- `rank(anl4_ebitda_high / close)`: S=0.97, F=0.78, T=1.5%, INFERIOR (TOP3000)
- `rank(ts_delta(anl4_ebitda_high, 5))`: S=0.42, F=0.09, T=36.5%, INFERIOR (TOP3000)
- `-rank(anl4_ebitda_high)`: S=-0.29, F=-0.16, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_ebitda_high, 5))`: S=0.16, F=0.03, T=36.9%, INFERIOR (TOP3000)
- `ts_zscore(anl4_ebitda_high, 22)`: S=0.28, F=0.07, T=35.6%, INFERIOR (TOP3000)
- `ts_mean(anl4_ebitda_high, 10)`: S=0.20, F=0.09, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_ebitda_high, 22))`: S=-0.13, F=-0.02, T=14.0%, INFERIOR (TOP3000)
- `rank(-1 * anl4_ebitda_high)`: S=-0.16, F=-0.07, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * anl4_ebitda_high / close)`: S=-0.26, F=-0.12, T=2.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 1F/31P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 22F/7P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.97, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.03 (weak), ret=+0.1%
  - 2020: S=-0.75 (negative), ret=-6.1%
  - 2021: S=1.63 (strong), ret=+18.8%
  - 2022: S=2.00 (strong), ret=+19.8%
  - 2023: S=1.60 (strong), ret=+7.4%

## Risk & Drawdown
- Max drawdown: 14.51% over 294 days (recovered)
- Annualized: return +8.2%, volatility 8.5% (fraction of booksize)
- Hit rate: 51.9% positive days
- Tail shape: skew +0.24, excess kurtosis +2.32

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.43, max 2.92, latest 1.46

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +9.69%; worst month: -3.09%
Positive months: 56%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.58
- Sideways: S=0.86
- Bear: S=-2.24

## Negated Direction
Best negated: `rank(-1 * ts_delta(anl4_ebitda_high, 5))` S=0.16, F=0.03, INFERIOR
Direction gap: -0.81 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * anl4_ebitda_high)`: S=-0.16, F=-0.07, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * anl4_ebitda_high / close)`: S=-0.26, F=-0.12, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_ebitda_high, 5))`: S=0.16, F=0.03, T=36.9%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_ebitda_high / close)` | TOP3000 | 0.97 | 0.78 | 14.5% | 80% | bull-only |
| `rank(anl4_ebitda_high)` | TOP3000 | 0.52 | 0.38 | 38.4% | 80% | bull-only |
| `rank(anl4_ebitda_high / close)` | TOP1000 | 0.54 | 0.36 | 20.0% | 80% | bull-only |
| `rank(anl4_ebitda_high)` | TOP1000 | 0.28 | 0.16 | 40.8% | 60% | bull-only |
| `rank(anl4_ebitda_high / close)` | TOP500 | 0.25 | 0.12 | 34.6% | 60% | bull-only |
| `rank(ts_delta(anl4_ebitda_high, 5))` | TOP3000 | 0.46 | 0.09 | 8.6% | 80% | mixed |
| `rank(anl4_ebitda_high)` | TOP500 | 0.15 | 0.07 | 47.4% | 60% | bull-only |
| `rank(anl4_ebitda_high / close)` | TOP200 | 0.14 | 0.06 | 30.5% | 60% | bull-only |
| `rank(anl4_ebitda_high)` | TOP200 | 0.09 | 0.03 | 42.0% | 60% | bull-only |

## Correlation Notes
Top correlates:
- anl4_medianepsbfam: 0.996 (strongly positively correlated)
- anl4_ebitda_mean: 0.996 (strongly positively correlated)
- est_ebitda: 0.989 (strongly positively correlated)
- anl4_ebitda_low: 0.987 (strongly positively correlated)
- fnd6_newa1v1300_gp: 0.952 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| rp_ess_revenue | news18 | -0.35 | 1.61 | +0.64 | -0.71 | yes |
| anl4_rd_exp_flag | analyst4 | -0.41 | 1.81 | +0.79 | -0.68 | no |
| fnd6_txtubadjust | fundamental6 | -0.28 | 1.52 | +0.55 | -0.90 | yes |
| sharesout | pv1 | -0.19 | 1.55 | +0.52 | -0.60 | yes |
| systematic_risk_last_360_days | model51 | -0.18 | 1.54 | +0.53 | -0.47 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
