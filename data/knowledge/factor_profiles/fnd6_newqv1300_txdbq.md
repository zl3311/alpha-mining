---
field: fnd6_newqv1300_txdbq
dataset: fundamental6
best_template: rank_delta
best_sharpe: 0.86
best_fitness: 0.53
best_universe: TOP200
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: all-weather
n_variations_with_pnl: 7
max_drawdown: 0.2907
ann_vol: 0.1731
hit_rate: 0.502
rolling_sharpe_min: -1.48
rolling_sharpe_max: 3.54
top_merge_partner: news_mins_5_chg
redundancy_cluster: 53
negated_best_sharpe: 0.57
negated_best_template: rank_neg_delta
negated_best_fitness: 0.18
n_negated_sims: 10
direction_gap: -0.29
---
# fnd6_newqv1300_txdbq (fundamental6)

*Deferred Taxes - Balance Sheet*

## Signal Profile
- `rank(fnd6_newqv1300_txdbq)`: S=0.49, F=0.31, T=3.3%, INFERIOR (TOP3000)
- `rank(fnd6_newqv1300_txdbq / close)`: S=0.64, F=0.42, T=3.4%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_newqv1300_txdbq, 5))`: S=0.86, F=0.53, T=39.6%, INFERIOR (TOP200)
- `-rank(fnd6_newqv1300_txdbq)`: S=-0.08, F=-0.02, T=4.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_txdbq, 5))`: S=0.57, F=0.18, T=39.1%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_newqv1300_txdbq, 63)`: S=0.12, F=0.02, T=19.2%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newqv1300_txdbq, 10)`: S=-0.11, F=-0.03, T=2.1%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newqv1300_txdbq, 22))`: S=0.16, F=0.03, T=17.7%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_txdbq)`: S=-0.49, F=-0.31, T=3.3%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_txdbq / close)`: S=-0.64, F=-0.42, T=3.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 10F/22P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 16F/13P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.84, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.58 (negative), ret=-6.2%
  - 2020: S=-0.86 (negative), ret=-16.3%
  - 2021: S=1.49 (moderate), ret=+28.0%
  - 2022: S=2.50 (strong), ret=+47.4%
  - 2023: S=1.21 (moderate), ret=+18.9%

## Risk & Drawdown
- Max drawdown: 29.07% over 739 days (recovered)
- Annualized: return +14.6%, volatility 17.3% (fraction of booksize)
- Hit rate: 50.2% positive days
- Tail shape: skew -0.25, excess kurtosis +4.15

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.48, max 3.54, latest 1.20

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +14.21%; worst month: -15.63%
Positive months: 59%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=1.57
- Sideways: S=-0.06
- Bear: S=1.13

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_newqv1300_txdbq, 5))` S=0.57, F=0.18, INFERIOR
Direction gap: -0.29 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_newqv1300_txdbq)`: S=-0.49, F=-0.31, T=3.3%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_txdbq / close)`: S=-0.64, F=-0.42, T=3.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_txdbq, 5))`: S=0.57, F=0.18, T=39.1%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_newqv1300_txdbq, 5))` | TOP200 | 0.84 | 0.53 | 29.1% | 60% | all-weather |
| `rank(fnd6_newqv1300_txdbq / close)` | TOP3000 | 0.64 | 0.42 | 17.2% | 60% | bull-only |
| `rank(fnd6_newqv1300_txdbq)` | TOP3000 | 0.48 | 0.31 | 26.7% | 60% | bull-only |
| `rank(fnd6_newqv1300_txdbq / close)` | TOP500 | 0.26 | 0.13 | 30.0% | 60% | bull-only |
| `rank(fnd6_newqv1300_txdbq / close)` | TOP1000 | 0.21 | 0.09 | 20.8% | 60% | bull-only |
| `rank(fnd6_newqv1300_txdbq)` | TOP500 | 0.10 | 0.03 | 39.3% | 60% | bull-only |
| `rank(fnd6_newqv1300_txdbq)` | TOP1000 | 0.07 | 0.02 | 31.1% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_newqv1300_txditcq: 0.973 (strongly positively correlated)
- implied_volatility_mean_20: 0.133 (weakly positively correlated)
- implied_volatility_put_20: 0.131 (weakly positively correlated)
- implied_volatility_put_90: 0.118 (weakly positively correlated)
- unsystematic_risk_last_90_days: 0.115 (weakly positively correlated)

Redundancy cluster #53: 2 similar fields, mean |rho| 0.973 (representative). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| news_mins_5_chg | news12 | -0.00 | 1.19 | +0.34 | -0.86 | yes |
| multi_factor_static_score_derivative | model16 | +0.04 | 1.16 | +0.32 | -0.70 | yes |
| growth_potential_rank_derivative | model16 | +0.04 | 1.20 | +0.31 | -0.75 | yes |
| min_gross_income_guidance | analyst4 | +0.01 | 1.17 | +0.30 | -0.84 | yes |
| reporting_currency_code_9 | analyst4 | -0.01 | 1.18 | +0.33 | -0.48 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
