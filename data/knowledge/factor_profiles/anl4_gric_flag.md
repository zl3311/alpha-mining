---
field: anl4_gric_flag
dataset: analyst4
best_template: ts_mean
best_sharpe: 1.31
best_fitness: 1.28
best_universe: TOP3000
grade: AVERAGE
submittability: needs_upgrade
n_sims: 32
regime_profile: all-weather
n_variations_with_pnl: 5
max_drawdown: 0.0996
ann_vol: 0.0414
hit_rate: 0.5304
rolling_sharpe_min: -2.198
rolling_sharpe_max: 2.208
top_merge_partner: fnd6_newqv1300_miiq
negated_best_sharpe: 0.61
negated_best_template: rank_neg_delta
negated_best_fitness: 0.47
n_negated_sims: 10
direction_gap: -0.7
---
# anl4_gric_flag (analyst4)

*Gross income - forecast type (revision/new/...)*

## Signal Profile
- `rank(anl4_gric_flag)`: S=0.84, F=0.44, T=2.3%, INFERIOR (TOP3000)
- `rank(anl4_gric_flag / close)`: S=0.19, F=0.08, T=2.9%, INFERIOR (TOP200)
- `rank(ts_delta(anl4_gric_flag, 5))`: S=-0.10, F=-0.03, T=34.5%, INFERIOR (TOP3000)
- `-rank(anl4_gric_flag)`: S=-0.66, F=-0.35, T=3.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_gric_flag, 5))`: S=0.61, F=0.47, T=32.2%, INFERIOR (TOP3000)
- `-ts_zscore(anl4_gric_flag, 63)`: S=-0.07, F=-0.03, T=14.7%, INFERIOR (TOP3000)
- `ts_mean(anl4_gric_flag, 10)`: S=1.31, F=1.28, T=3.9%, AVERAGE (TOP3000)
- `rank(ts_rank(anl4_gric_flag, 22))`: S=-0.23, F=-0.12, T=17.2%, INFERIOR (TOP3000)
- `rank(-1 * anl4_gric_flag)`: S=-0.66, F=-0.35, T=3.1%, INFERIOR (TOP3000)
- `rank(-1 * anl4_gric_flag / close)`: S=-0.09, F=-0.03, T=2.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 31F/1P
- LOW_SHARPE: 31F/1P
- LOW_SUB_UNIVERSE_SHARPE: 14F/15P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.83, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.75 (negative), ret=-2.8%
  - 2020: S=-0.63 (negative), ret=-2.4%
  - 2021: S=1.88 (strong), ret=+9.4%
  - 2022: S=1.95 (strong), ret=+7.4%
  - 2023: S=1.36 (moderate), ret=+5.2%

## Risk & Drawdown
- Max drawdown: 9.96% over 739 days (recovered)
- Annualized: return +3.4%, volatility 4.1% (fraction of booksize)
- Hit rate: 53.0% positive days
- Tail shape: skew -0.24, excess kurtosis +1.93

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.20, max 2.21, latest 1.42

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2019
Best month: +4.76%; worst month: -2.20%
Positive months: 59%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=2.20
- Sideways: S=-0.74
- Bear: S=0.89

## Negated Direction
Best negated: `rank(-1 * ts_delta(anl4_gric_flag, 5))` S=0.61, F=0.47, INFERIOR
Direction gap: -0.70 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * anl4_gric_flag)`: S=-0.66, F=-0.35, T=3.1%, INFERIOR (TOP3000)
- `rank(-1 * anl4_gric_flag / close)`: S=-0.09, F=-0.03, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_gric_flag, 5))`: S=0.61, F=0.47, T=32.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_gric_flag)` | TOP3000 | 0.83 | 0.44 | 10.0% | 60% | all-weather |
| `rank(anl4_gric_flag)` | TOP1000 | 0.65 | 0.35 | 11.2% | 80% | all-weather |
| `rank(anl4_gric_flag)` | TOP500 | 0.32 | 0.15 | 17.0% | 60% | mixed |
| `rank(anl4_gric_flag / close)` | TOP200 | 0.20 | 0.08 | 24.9% | 80% | mixed |
| `rank(anl4_gric_flag / close)` | TOP1000 | 0.09 | 0.03 | 38.8% | 40% | bear-only |

## Correlation Notes
Top correlates:
- anl4_cfi_flag: 0.422 (moderately positively correlated)
- anl4_cff_flag: 0.416 (moderately positively correlated)
- anl4_cfo_flag: 0.410 (moderately positively correlated)
- anl4_totassets_flag: 0.403 (moderately positively correlated)
- anl4_capex_flag: 0.401 (moderately positively correlated)

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| fnd6_newqv1300_miiq | fundamental6 | -0.00 | 1.17 | +0.30 | -0.68 | yes |
| fnd6_dd | fundamental6 | -0.06 | 1.21 | +0.27 | -0.76 | yes |
| fn_treasury_stock_shares_a | fundamental2 | -0.04 | 1.22 | +0.35 | +0.22 | yes |
| rp_ess_revenue | news18 | -0.06 | 1.17 | +0.28 | -0.69 | yes |
| fnd6_txtubadjust | fundamental6 | +0.07 | 1.10 | +0.25 | -0.86 | yes |

## Actionability
Needs grade upgrade. Try decay_linear wrap, value normalization, or blend with complementary factor.
Untried templates: decay_linear, trade_when
