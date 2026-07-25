---
field: snt_value_fast_d1
dataset: socialmedia12
best_template: rank_level
best_sharpe: 0.88
best_fitness: 0.22
best_universe: TOP1000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 26
regime_profile: all-weather
n_variations_with_pnl: 4
max_drawdown: 0.0634
ann_vol: 0.0411
hit_rate: 0.5069
rolling_sharpe_min: -1.256
rolling_sharpe_max: 3.034
top_merge_partner: anl4_ptpr_flag
negated_best_sharpe: 0.59
negated_best_template: rank_neg_delta
negated_best_fitness: 0.14
n_negated_sims: 10
direction_gap: -0.29
---
# snt_value_fast_d1 (socialmedia12)

*Negative sentiment score/indicator for current day, with missing values filled as 0*

## Signal Profile
- `rank(snt_value_fast_d1)`: S=0.88, F=0.22, T=56.3%, INFERIOR (TOP1000)
- `rank(ts_delta(snt_value_fast_d1, 5))`: S=0.39, F=0.06, T=71.4%, INFERIOR (TOP1000)
- `-rank(snt_value_fast_d1)`: S=-0.88, F=-0.22, T=56.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(snt_value_fast_d1, 5))`: S=0.59, F=0.14, T=69.2%, INFERIOR (TOP3000)
- `ts_zscore(snt_value_fast_d1, 22)`: S=0.40, F=0.07, T=58.7%, INFERIOR (TOP3000)
- `ts_mean(snt_value_fast_d1, 10)`: S=0.36, F=0.17, T=19.8%, INFERIOR (TOP3000)
- `rank(ts_rank(snt_value_fast_d1, 22))`: S=0.58, F=0.11, T=63.2%, INFERIOR (TOP3000)
- `rank(-1 * snt_value_fast_d1)`: S=0.31, F=0.06, T=57.9%, INFERIOR (TOP3000)
- `rank(-1 * snt_value_fast_d1 / close)`: S=0.16, F=0.02, T=57.5%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 1F/25P
- HIGH_TURNOVER: 4F/22P
- LOW_FITNESS: 26F/0P
- LOW_SHARPE: 26F/0P
- LOW_SUB_UNIVERSE_SHARPE: 2F/13P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.89, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=-0.68 (negative), ret=-2.0%
  - 2020: S=2.48 (strong), ret=+9.2%
  - 2021: S=0.72 (moderate), ret=+4.1%
  - 2022: S=1.06 (moderate), ret=+4.3%
  - 2023: S=0.66 (moderate), ret=+2.2%

## Risk & Drawdown
- Max drawdown: 6.34% over 490 days (recovered)
- Annualized: return +3.6%, volatility 4.1% (fraction of booksize)
- Hit rate: 50.7% positive days
- Tail shape: skew +0.90, excess kurtosis +8.40

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.26, max 3.03, latest 0.69

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2019
Best month: +3.44%; worst month: -1.80%
Positive months: 54%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=1.26
- Sideways: S=0.16
- Bear: S=1.12

## Negated Direction
Best negated: `rank(-1 * ts_delta(snt_value_fast_d1, 5))` S=0.59, F=0.14, INFERIOR
Direction gap: -0.29 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * snt_value_fast_d1)`: S=0.31, F=0.06, T=57.9%, INFERIOR (TOP3000)
- `rank(-1 * snt_value_fast_d1 / close)`: S=0.16, F=0.02, T=57.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(snt_value_fast_d1, 5))`: S=0.59, F=0.14, T=69.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(snt_value_fast_d1)` | TOP1000 | 0.89 | 0.22 | 6.3% | 80% | all-weather |
| `rank(ts_delta(snt_value_fast_d1, 5))` | TOP1000 | 0.38 | 0.06 | 6.7% | 80% | mixed |
| `rank(snt_value_fast_d1)` | TOP500 | 0.20 | 0.02 | 6.7% | 60% | mixed |
| `rank(ts_delta(snt_value_fast_d1, 5))` | TOP500 | 0.19 | 0.02 | 9.7% | 40% | bull-only |

## Correlation Notes
Top correlates:
- snt_value: 0.368 (weakly positively correlated)
- fnd6_prchq: 0.343 (weakly positively correlated)
- implied_volatility_call_30 - implied_volatility_call_270: 0.328 (weakly positively correlated)
- anl4_afv4_cfps_number: 0.324 (weakly positively correlated)
- fnd6_beta: 0.320 (weakly positively correlated)

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_ptpr_flag | analyst_revision | -0.25 | 1.77 | +0.49 | -0.77 | yes |
| implied_volatility_mean_skew_270 | option8 | -0.23 | 1.49 | +0.47 | -0.90 | yes |
| max_capital_expenditure_guidance | analyst4 | -0.18 | 1.37 | +0.49 | -0.66 | yes |
| min_capital_expenditure_guidance | analyst4 | -0.18 | 1.40 | +0.48 | -0.67 | yes |
| rel_num_part | pv13 | -0.27 | 1.79 | +0.52 | -0.31 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, rank_value_norm, trade_when
