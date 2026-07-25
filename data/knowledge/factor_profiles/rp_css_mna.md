---
field: rp_css_mna
dataset: news18
best_template: rank_delta
best_sharpe: 1.12
best_fitness: 0.24
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 20
regime_profile: all-weather
n_variations_with_pnl: 6
max_drawdown: 0.0879
ann_vol: 0.0662
hit_rate: 0.5215
rolling_sharpe_min: -1.088
rolling_sharpe_max: 3.23
top_merge_partner: est_rd_expense
negated_best_sharpe: -0.04
negated_best_template: neg_rank
negated_best_fitness: 0.0
n_negated_sims: 4
direction_gap: -1.16
---
# rp_css_mna (news18)

*Composite sentiment score of mergers and acquisitions-related news*

## Signal Profile
- `rank(rp_css_mna)`: S=0.78, F=0.18, T=129.8%, INFERIOR (TOP200)
- `rank(ts_delta(rp_css_mna, 5))`: S=1.12, F=0.24, T=166.3%, INFERIOR (TOP3000)
- `-rank(rp_css_mna)`: S=-0.04, F=0.00, T=149.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(rp_css_mna, 5))`: S=-1.12, F=-0.24, T=166.3%, INFERIOR (TOP3000)
- `-ts_zscore(rp_css_mna, 63)`: S=0.25, F=0.02, T=150.7%, INFERIOR (TOP3000)
- `ts_mean(rp_css_mna, 10)`: S=-0.65, F=-0.25, T=21.6%, INFERIOR (TOP3000)
- `rank(ts_rank(rp_css_mna, 22))`: S=-0.23, F=-0.02, T=152.6%, INFERIOR (TOP3000)
- `rank(-1 * rp_css_mna)`: S=-0.66, F=-0.09, T=161.8%, INFERIOR (TOP3000)
- `rank(-1 * rp_css_mna / close)`: S=-0.47, F=-0.06, T=162.0%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 4F/16P
- HIGH_TURNOVER: 19F/1P
- LOW_FITNESS: 20F/0P
- LOW_SHARPE: 20F/0P
- LOW_SUB_UNIVERSE_SHARPE: 6F/12P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 1.12, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=-0.03 (negative), ret=-0.2%
  - 2020: S=0.22 (weak), ret=+1.4%
  - 2021: S=0.96 (moderate), ret=+7.7%
  - 2022: S=1.79 (strong), ret=+9.5%
  - 2023: S=3.05 (strong), ret=+17.7%

## Risk & Drawdown
- Max drawdown: 8.79% over 612 days (recovered)
- Annualized: return +7.4%, volatility 6.6% (fraction of booksize)
- Hit rate: 52.1% positive days
- Tail shape: skew +0.61, excess kurtosis +4.26

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.09, max 3.23, latest 3.06

## Yearly & Monthly Returns
Best year (by Sharpe): 2023; worst year: 2019
Best month: +6.35%; worst month: -4.54%
Positive months: 61%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=0.99
- Sideways: S=0.77
- Bear: S=1.53

## Negated Direction
Best negated: `-rank(rp_css_mna)` S=-0.04, F=0.00, INFERIOR
Direction gap: -1.16 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * rp_css_mna)`: S=-0.66, F=-0.09, T=161.8%, INFERIOR (TOP3000)
- `rank(-1 * rp_css_mna / close)`: S=-0.47, F=-0.06, T=162.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(rp_css_mna, 5))`: S=-1.12, F=-0.24, T=166.3%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(rp_css_mna, 5))` | TOP3000 | 1.12 | 0.24 | 8.8% | 80% | all-weather |
| `rank(rp_css_mna)` | TOP200 | 0.80 | 0.18 | 10.6% | 80% | mixed |
| `rank(rp_css_mna)` | TOP3000 | 0.67 | 0.09 | 8.5% | 80% | mixed |
| `rank(ts_delta(rp_css_mna, 5))` | TOP1000 | 0.48 | 0.07 | 10.6% | 80% | mixed |
| `rank(ts_delta(rp_css_mna, 5))` | TOP500 | 0.35 | 0.05 | 17.2% | 80% | weak |
| `rank(rp_css_mna)` | TOP500 | 0.39 | 0.05 | 9.6% | 60% | mixed |

## Correlation Notes
Top correlates:
- rp_ess_credit_ratings: 0.153 (weakly positively correlated)
- rp_css_credit_ratings: 0.135 (weakly positively correlated)
- anl4_qfv4_div_mean: 0.119 (weakly positively correlated)
- est_dividend_ps: 0.113 (weakly positively correlated)
- est_tbv_ps: 0.087 (weakly positively correlated)

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| est_rd_expense | analyst4 | -0.01 | 1.58 | +0.46 | -0.81 | yes |
| anl4_cfo_flag | analyst4 | -0.02 | 1.60 | +0.48 | -0.42 | yes |
| implied_volatility_mean_30 | option8 | -0.00 | 1.63 | +0.44 | -0.73 | yes |
| implied_volatility_call_20 | option8 | -0.01 | 1.69 | +0.43 | -0.68 | yes |
| implied_volatility_put_30 | option8 | +0.00 | 1.65 | +0.43 | -0.64 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, rank_value_norm, trade_when
