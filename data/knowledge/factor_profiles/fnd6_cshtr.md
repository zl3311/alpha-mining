---
field: fnd6_cshtr
dataset: fundamental6
best_template: rank_level
best_sharpe: 1.01
best_fitness: 0.68
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: all-weather
n_variations_with_pnl: 9
max_drawdown: 0.0607
ann_vol: 0.0566
hit_rate: 0.5304
rolling_sharpe_min: -0.78
rolling_sharpe_max: 3.191
top_merge_partner: implied_volatility_mean_skew_1080
redundancy_cluster: 27
negated_best_sharpe: 0.73
negated_best_template: rank_neg_delta
negated_best_fitness: 0.48
n_negated_sims: 10
direction_gap: -0.28
---
# fnd6_cshtr (fundamental6)

*Common Shares Traded - Annual*

## Signal Profile
- `rank(fnd6_cshtr)`: S=1.01, F=0.68, T=1.0%, INFERIOR (TOP3000)
- `rank(fnd6_cshtr / close)`: S=0.58, F=0.37, T=2.0%, INFERIOR (TOP200)
- `rank(ts_delta(fnd6_cshtr, 5))`: S=0.78, F=0.53, T=24.8%, INFERIOR (TOP500)
- `-rank(fnd6_cshtr)`: S=-0.78, F=-0.45, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_cshtr, 5))`: S=0.73, F=0.48, T=30.8%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_cshtr, 22)`: S=0.36, F=0.32, T=9.8%, INFERIOR (TOP3000)
- `ts_mean(fnd6_cshtr, 10)`: S=0.84, F=0.58, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_cshtr, 22))`: S=-0.60, F=-0.41, T=11.3%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_cshtr)`: S=-1.01, F=-0.68, T=1.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_cshtr / close)`: S=-0.40, F=-0.23, T=1.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 11F/18P
- LOW_TURNOVER: 4F/28P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 1.01, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.95 (moderate), ret=+3.8%
  - 2020: S=1.82 (strong), ret=+9.5%
  - 2021: S=2.18 (strong), ret=+10.0%
  - 2022: S=0.13 (weak), ret=+0.9%
  - 2023: S=0.61 (moderate), ret=+3.9%

## Risk & Drawdown
- Max drawdown: 6.07% over 472 days (recovered)
- Annualized: return +5.7%, volatility 5.7% (fraction of booksize)
- Hit rate: 53.0% positive days
- Tail shape: skew +0.19, excess kurtosis +0.95

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.78, max 3.19, latest 0.58

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2022
Best month: +4.83%; worst month: -2.78%
Positive months: 58%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=1.14
- Sideways: S=0.99
- Bear: S=0.90

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_cshtr, 5))` S=0.73, F=0.48, INFERIOR
Direction gap: -0.28 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_cshtr)`: S=-1.01, F=-0.68, T=1.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_cshtr / close)`: S=-0.40, F=-0.23, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_cshtr, 5))`: S=0.73, F=0.48, T=30.8%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_cshtr)` | TOP3000 | 1.01 | 0.68 | 6.1% | 100% | all-weather |
| `rank(ts_delta(fnd6_cshtr, 5))` | TOP500 | 0.79 | 0.53 | 16.2% | 80% | mixed |
| `rank(fnd6_cshtr)` | TOP1000 | 0.78 | 0.45 | 8.2% | 80% | all-weather |
| `rank(fnd6_cshtr)` | TOP500 | 0.72 | 0.41 | 6.2% | 80% | all-weather |
| `rank(fnd6_cshtr / close)` | TOP200 | 0.60 | 0.37 | 14.6% | 100% | all-weather |
| `rank(fnd6_cshtr)` | TOP200 | 0.57 | 0.31 | 12.0% | 100% | all-weather |
| `rank(fnd6_cshtr / close)` | TOP500 | 0.50 | 0.28 | 16.3% | 60% | mixed |
| `rank(fnd6_cshtr / close)` | TOP3000 | 0.40 | 0.23 | 29.0% | 80% | bear-only |
| `rank(fnd6_cshtr / close)` | TOP1000 | 0.39 | 0.20 | 21.4% | 60% | mixed |

## Correlation Notes
Top correlates:
- adv20: 0.818 (strongly positively correlated)
- fnd2_a_dfdtxava: 0.769 (strongly positively correlated)
- fnd6_tlcf: 0.708 (strongly positively correlated)
- news_open_vol: 0.707 (strongly positively correlated)
- fn_comp_non_opt_nonvested_number_q: 0.697 (moderately positively correlated)

Redundancy cluster #27: 3 similar fields, mean |rho| 0.78 (representative: fnd6_tlcf). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| implied_volatility_mean_skew_1080 | option8 | -0.41 | 1.87 | +0.86 | -0.26 | yes |
| implied_volatility_mean_skew_720 | option8 | -0.41 | 1.86 | +0.85 | -0.28 | yes |
| implied_volatility_mean_skew_360 | option8 | -0.38 | 1.89 | +0.78 | -0.48 | yes |
| implied_volatility_mean_skew_270 | option8 | -0.35 | 1.77 | +0.74 | -0.53 | yes |
| implied_volatility_mean_skew_180 | option8 | -0.34 | 1.76 | +0.69 | -0.57 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
