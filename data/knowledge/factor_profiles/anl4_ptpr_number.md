---
field: anl4_ptpr_number
dataset: analyst4
best_template: rank_level
best_sharpe: 0.82
best_fitness: 0.58
best_universe: TOP200
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 11
max_drawdown: 0.1006
ann_vol: 0.0771
hit_rate: 0.5231
rolling_sharpe_min: -0.463
rolling_sharpe_max: 2.518
top_merge_partner: fnd6_optex
negated_best_sharpe: 0.13
negated_best_template: rank_neg_delta
negated_best_fitness: 0.03
n_negated_sims: 10
direction_gap: -0.69
---
# anl4_ptpr_number (analyst4)

*Reported Pretax Income - number of estimations*

## Signal Profile
- `rank(anl4_ptpr_number)`: S=0.82, F=0.58, T=4.2%, INFERIOR (TOP200)
- `rank(anl4_ptpr_number / close)`: S=0.33, F=0.16, T=3.1%, INFERIOR (TOP200)
- `rank(ts_delta(anl4_ptpr_number, 5))`: S=0.87, F=0.37, T=36.2%, INFERIOR (TOP3000)
- `-rank(anl4_ptpr_number)`: S=-0.64, F=-0.30, T=3.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_ptpr_number, 5))`: S=0.13, F=0.03, T=33.5%, INFERIOR (TOP3000)
- `ts_zscore(anl4_ptpr_number, 22)`: S=0.15, F=0.04, T=33.3%, INFERIOR (TOP3000)
- `ts_mean(anl4_ptpr_number, 10)`: S=0.43, F=0.20, T=3.0%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_ptpr_number, 22))`: S=-0.06, F=-0.01, T=13.1%, INFERIOR (TOP3000)
- `rank(-1 * anl4_ptpr_number)`: S=-0.37, F=-0.15, T=3.5%, INFERIOR (TOP3000)
- `rank(-1 * anl4_ptpr_number / close)`: S=-0.24, F=-0.09, T=2.7%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 10F/22P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 17F/12P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.84, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=1.38 (moderate), ret=+8.1%
  - 2020: S=0.69 (moderate), ret=+4.7%
  - 2021: S=0.01 (weak), ret=+0.1%
  - 2022: S=1.40 (moderate), ret=+13.1%
  - 2023: S=0.81 (moderate), ret=+5.7%

## Risk & Drawdown
- Max drawdown: 10.06% over 504 days (recovered)
- Annualized: return +6.5%, volatility 7.7% (fraction of booksize)
- Hit rate: 52.3% positive days
- Tail shape: skew -0.17, excess kurtosis +1.64

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.46, max 2.52, latest 0.85

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2021
Best month: +5.18%; worst month: -5.41%
Positive months: 68%

## Regime Profile
Regime profile: **mixed**
- Bull: S=1.29
- Sideways: S=1.00
- Bear: S=0.17

## Negated Direction
Best negated: `rank(-1 * ts_delta(anl4_ptpr_number, 5))` S=0.13, F=0.03, INFERIOR
Direction gap: -0.69 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * anl4_ptpr_number)`: S=-0.37, F=-0.15, T=3.5%, INFERIOR (TOP3000)
- `rank(-1 * anl4_ptpr_number / close)`: S=-0.24, F=-0.09, T=2.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_ptpr_number, 5))`: S=0.13, F=0.03, T=33.5%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_ptpr_number)` | TOP200 | 0.84 | 0.58 | 10.1% | 100% | mixed |
| `rank(ts_delta(anl4_ptpr_number, 5))` | TOP3000 | 0.90 | 0.37 | 18.9% | 60% | all-weather |
| `rank(anl4_ptpr_number)` | TOP1000 | 0.65 | 0.30 | 11.1% | 40% | bull-only |
| `rank(anl4_ptpr_number)` | TOP3000 | 0.67 | 0.28 | 4.4% | 80% | mixed |
| `rank(ts_delta(anl4_ptpr_number, 5))` | TOP200 | 0.50 | 0.24 | 17.4% | 80% | mixed |
| `rank(anl4_ptpr_number / close)` | TOP200 | 0.35 | 0.16 | 17.7% | 60% | mixed |
| `rank(anl4_ptpr_number)` | TOP500 | 0.38 | 0.15 | 14.2% | 60% | bull-only |
| `rank(anl4_ptpr_number / close)` | TOP500 | 0.24 | 0.09 | 18.9% | 40% | mixed |
| `rank(anl4_ptpr_number / close)` | TOP1000 | 0.18 | 0.07 | 21.7% | 60% | bear-only |
| `rank(anl4_ptpr_number / close)` | TOP3000 | 0.12 | 0.04 | 38.7% | 40% | bear-only |
| `rank(ts_delta(anl4_ptpr_number, 5))` | TOP1000 | 0.17 | 0.03 | 29.0% | 60% | weak |

## Correlation Notes
Top correlates:
- unsystematic_risk_last_30_days: -0.313 (weakly negatively correlated)
- fnd6_itcb: 0.301 (weakly positively correlated)
- implied_volatility_mean_skew_150: 0.289 (weakly positively correlated)
- implied_volatility_mean_skew_120: 0.285 (weakly positively correlated)
- implied_volatility_mean_skew_60: 0.283 (weakly positively correlated)

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| fnd6_optex | fundamental6 | -0.17 | 1.34 | +0.44 | -0.24 | yes |
| sharesout | pv1 | -0.18 | 1.45 | +0.42 | -0.40 | yes |
| news_open_vol | news12 | -0.19 | 1.38 | +0.45 | +0.82 | yes |
| parkinson_volatility_90 | option8 | -0.09 | 1.28 | +0.39 | -0.62 | yes |
| systematic_risk_last_360_days | model51 | -0.16 | 1.42 | +0.41 | -0.28 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
