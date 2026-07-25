---
field: fnd6_tlcf
dataset: fundamental6
best_template: rank_level
best_sharpe: 1.1
best_fitness: 0.72
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: all-weather
n_variations_with_pnl: 9
max_drawdown: 0.0757
ann_vol: 0.0484
hit_rate: 0.5215
rolling_sharpe_min: -0.441
rolling_sharpe_max: 3.167
top_merge_partner: implied_volatility_mean_skew_360
redundancy_cluster: 27
negated_best_sharpe: 0.58
negated_best_template: rank_neg_delta
negated_best_fitness: 0.4
n_negated_sims: 10
direction_gap: -0.52
---
# fnd6_tlcf (fundamental6)

*Tax Loss Carry Forward*

## Signal Profile
- `rank(fnd6_tlcf)`: S=1.10, F=0.72, T=1.8%, INFERIOR (TOP3000)
- `rank(fnd6_tlcf / close)`: S=0.54, F=0.33, T=3.2%, INFERIOR (TOP500)
- `rank(ts_delta(fnd6_tlcf, 5))`: S=0.47, F=0.24, T=42.6%, INFERIOR (TOP3000)
- `-rank(fnd6_tlcf)`: S=-0.66, F=-0.36, T=2.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_tlcf, 5))`: S=0.58, F=0.40, T=24.6%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_tlcf, 22)`: S=0.40, F=0.25, T=21.5%, INFERIOR (TOP3000)
- `ts_mean(fnd6_tlcf, 10)`: S=0.36, F=0.17, T=2.2%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_tlcf, 22))`: S=-0.64, F=-0.43, T=20.3%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_tlcf)`: S=-0.18, F=-0.07, T=3.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_tlcf / close)`: S=-0.37, F=-0.21, T=3.7%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 13F/19P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 11F/9P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 1.10, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.81 (moderate), ret=+2.6%
  - 2020: S=2.37 (strong), ret=+9.1%
  - 2021: S=1.89 (strong), ret=+7.5%
  - 2022: S=-0.10 (negative), ret=-0.7%
  - 2023: S=1.46 (moderate), ret=+7.6%

## Risk & Drawdown
- Max drawdown: 7.57% over 463 days (recovered)
- Annualized: return +5.3%, volatility 4.8% (fraction of booksize)
- Hit rate: 52.1% positive days
- Tail shape: skew +0.27, excess kurtosis +2.15

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.44, max 3.17, latest 1.52

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2022
Best month: +3.68%; worst month: -2.15%
Positive months: 56%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=1.06
- Sideways: S=0.60
- Bear: S=1.69

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_tlcf, 5))` S=0.58, F=0.40, INFERIOR
Direction gap: -0.52 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_tlcf)`: S=-0.18, F=-0.07, T=3.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_tlcf / close)`: S=-0.37, F=-0.21, T=3.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_tlcf, 5))`: S=0.58, F=0.40, T=24.6%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_tlcf)` | TOP3000 | 1.10 | 0.72 | 7.6% | 80% | all-weather |
| `rank(fnd6_tlcf)` | TOP1000 | 0.68 | 0.36 | 8.8% | 80% | all-weather |
| `rank(fnd6_tlcf / close)` | TOP500 | 0.56 | 0.33 | 14.0% | 60% | mixed |
| `rank(fnd6_tlcf / close)` | TOP1000 | 0.50 | 0.28 | 18.6% | 80% | bear-only |
| `rank(fnd6_tlcf)` | TOP500 | 0.53 | 0.27 | 13.0% | 80% | mixed |
| `rank(ts_delta(fnd6_tlcf, 5))` | TOP3000 | 0.46 | 0.24 | 50.2% | 60% | mixed |
| `rank(fnd6_tlcf / close)` | TOP3000 | 0.44 | 0.24 | 21.1% | 80% | bear-only |
| `rank(fnd6_tlcf / close)` | TOP200 | 0.39 | 0.21 | 23.8% | 60% | mixed |
| `rank(fnd6_tlcf)` | TOP200 | 0.21 | 0.07 | 23.3% | 80% | mixed |

## Correlation Notes
Top correlates:
- fnd2_a_dfdtxava: 0.862 (strongly positively correlated)
- fn_allocated_share_based_compensation_expense_a: 0.716 (strongly positively correlated)
- fnd6_cshtr: 0.708 (strongly positively correlated)
- fnd6_stkcpa: 0.700 (moderately positively correlated)
- fn_comp_not_rec_a: 0.697 (moderately positively correlated)

Redundancy cluster #27: 3 similar fields, mean |rho| 0.78 (representative). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| implied_volatility_mean_skew_360 | option8 | -0.16 | 1.68 | +0.57 | -0.73 | yes |
| implied_volatility_mean_skew_1080 | option8 | -0.19 | 1.65 | +0.55 | -0.59 | yes |
| implied_volatility_mean_skew_720 | option8 | -0.18 | 1.65 | +0.54 | -0.62 | yes |
| implied_volatility_mean_skew_180 | option8 | -0.12 | 1.57 | +0.47 | -0.88 | yes |
| implied_volatility_mean_skew_270 | option8 | -0.14 | 1.58 | +0.47 | -0.78 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
