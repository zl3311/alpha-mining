---
field: fnd2_a_dfdtxava
dataset: fundamental2
best_template: rank_neg_delta
best_sharpe: 1.28
best_fitness: 0.88
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_FITNESS
n_sims: 32
regime_profile: all-weather
n_variations_with_pnl: 8
max_drawdown: 0.063
ann_vol: 0.0461
hit_rate: 0.519
rolling_sharpe_min: -0.445
rolling_sharpe_max: 2.55
top_merge_partner: implied_volatility_mean_skew_1080
redundancy_cluster: 27
negated_best_sharpe: 1.28
negated_best_template: rank_neg_delta
negated_best_fitness: 0.88
n_negated_sims: 10
direction_gap: 0.35
---
# fnd2_a_dfdtxava (fundamental2)

*Amount of deferred tax assets for which it is more likely than not that a tax benefit will not be realized.*

## Signal Profile
- `rank(fnd2_a_dfdtxava)`: S=0.93, F=0.54, T=0.8%, INFERIOR (TOP3000)
- `rank(fnd2_a_dfdtxava / close)`: S=0.69, F=0.42, T=1.8%, INFERIOR (TOP500)
- `rank(ts_delta(fnd2_a_dfdtxava, 5))`: S=-0.46, F=-0.23, T=34.2%, INFERIOR (TOP500)
- `-rank(fnd2_a_dfdtxava)`: S=-0.71, F=-0.36, T=1.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_a_dfdtxava, 5))`: S=1.28, F=0.88, T=34.3%, INFERIOR (TOP3000)
- `-ts_zscore(fnd2_a_dfdtxava, 63)`: S=0.45, F=0.27, T=17.1%, INFERIOR (TOP3000)
- `ts_mean(fnd2_a_dfdtxava, 10)`: S=0.17, F=0.05, T=1.0%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd2_a_dfdtxava, 22))`: S=-0.63, F=-0.39, T=14.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_a_dfdtxava)`: S=-0.93, F=-0.54, T=0.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_a_dfdtxava / close)`: S=-0.39, F=-0.20, T=1.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 29F/3P
- LOW_SUB_UNIVERSE_SHARPE: 16F/13P
- LOW_TURNOVER: 5F/27P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.94, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.79 (moderate), ret=+2.2%
  - 2020: S=1.53 (strong), ret=+6.4%
  - 2021: S=1.03 (moderate), ret=+3.9%
  - 2022: S=0.14 (weak), ret=+0.8%
  - 2023: S=1.51 (strong), ret=+7.8%

## Risk & Drawdown
- Max drawdown: 6.30% over 435 days (recovered)
- Annualized: return +4.3%, volatility 4.6% (fraction of booksize)
- Hit rate: 51.9% positive days
- Tail shape: skew +0.19, excess kurtosis +1.44

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.45, max 2.55, latest 1.60

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2022
Best month: +3.56%; worst month: -1.87%
Positive months: 56%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=1.04
- Sideways: S=0.91
- Bear: S=0.85

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd2_a_dfdtxava, 5))` S=1.28, F=0.88, INFERIOR
Direction gap: +0.35 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fnd2_a_dfdtxava)`: S=-0.93, F=-0.54, T=0.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_a_dfdtxava / close)`: S=-0.39, F=-0.20, T=1.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_a_dfdtxava, 5))`: S=1.28, F=0.88, T=34.3%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd2_a_dfdtxava)` | TOP3000 | 0.94 | 0.54 | 6.3% | 100% | all-weather |
| `rank(fnd2_a_dfdtxava)` | TOP500 | 0.88 | 0.53 | 6.9% | 80% | mixed |
| `rank(fnd2_a_dfdtxava / close)` | TOP500 | 0.71 | 0.42 | 10.9% | 80% | mixed |
| `rank(fnd2_a_dfdtxava)` | TOP1000 | 0.72 | 0.36 | 6.5% | 80% | mixed |
| `rank(fnd2_a_dfdtxava / close)` | TOP200 | 0.50 | 0.27 | 17.3% | 80% | mixed |
| `rank(fnd2_a_dfdtxava / close)` | TOP3000 | 0.39 | 0.20 | 22.5% | 80% | bear-only |
| `rank(fnd2_a_dfdtxava / close)` | TOP1000 | 0.41 | 0.19 | 14.9% | 80% | mixed |
| `rank(fnd2_a_dfdtxava)` | TOP200 | 0.41 | 0.18 | 15.2% | 80% | mixed |

## Correlation Notes
Top correlates:
- fnd6_tlcf: 0.862 (strongly positively correlated)
- fnd6_cshtr: 0.769 (strongly positively correlated)
- fnd2_unrgtxbnfinregfcrps: 0.713 (strongly positively correlated)
- fn_allocated_share_based_compensation_expense_a: 0.699 (moderately positively correlated)
- fn_comp_non_opt_nonvested_number_q: 0.697 (moderately positively correlated)

Redundancy cluster #27: 3 similar fields, mean |rho| 0.78 (representative: fnd6_tlcf). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| implied_volatility_mean_skew_1080 | option8 | -0.25 | 1.59 | +0.58 | -0.65 | yes |
| implied_volatility_mean_skew_720 | option8 | -0.25 | 1.59 | +0.57 | -0.66 | yes |
| fnd6_newqv1300_tstknq | fundamental6 | -0.19 | 1.45 | +0.51 | -0.80 | yes |
| min_capital_expenditure_guidance | analyst4 | -0.17 | 1.44 | +0.50 | -0.69 | yes |
| implied_volatility_mean_skew_360 | option8 | -0.21 | 1.61 | +0.51 | -0.64 | yes |

## Actionability
Blocked by LOW_FITNESS. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
