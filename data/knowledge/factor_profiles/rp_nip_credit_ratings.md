---
field: rp_nip_credit_ratings
dataset: news18
best_template: rank_delta
best_sharpe: 1.06
best_fitness: 0.5
best_universe: TOP200
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 20
regime_profile: all-weather
n_variations_with_pnl: 6
max_drawdown: 0.0161
ann_vol: 0.0241
hit_rate: 0.0219
rolling_sharpe_min: -0.638
rolling_sharpe_max: 2.539
top_merge_partner: fn_line_of_credit_facility_amount_out_q
negated_best_sharpe: 0.85
negated_best_template: neg_rank_level
negated_best_fitness: 0.29
n_negated_sims: 4
direction_gap: -0.21
---
# rp_nip_credit_ratings (news18)

*News impact projection of credit ratings news*

## Signal Profile
- `rank(rp_nip_credit_ratings)`: S=0.63, F=0.23, T=111.2%, INFERIOR (TOP500)
- `rank(ts_delta(rp_nip_credit_ratings, 5))`: S=1.06, F=0.50, T=4.5%, INFERIOR (TOP200)
- `-rank(rp_nip_credit_ratings)`: S=-0.19, F=-0.03, T=139.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(rp_nip_credit_ratings, 5))`: S=-0.61, F=-0.31, T=77.3%, INFERIOR (TOP3000)
- `ts_zscore(rp_nip_credit_ratings, 22)`: S=0.49, F=0.17, T=105.5%, INFERIOR (TOP3000)
- `ts_mean(rp_nip_credit_ratings, 10)`: S=0.12, F=0.02, T=38.5%, INFERIOR (TOP3000)
- `rank(ts_rank(rp_nip_credit_ratings, 22))`: S=-0.41, F=-0.12, T=127.5%, INFERIOR (TOP3000)
- `rank(-1 * rp_nip_credit_ratings)`: S=0.85, F=0.29, T=163.5%, INFERIOR (TOP3000)
- `rank(-1 * rp_nip_credit_ratings / close)`: S=0.32, F=0.07, T=167.6%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 20F/0P
- HIGH_TURNOVER: 13F/7P
- LOW_FITNESS: 20F/0P
- LOW_SHARPE: 20F/0P
- LOW_SUB_UNIVERSE_SHARPE: 7F/11P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.96, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=1.03 (moderate), ret=+1.0%
  - 2020: S=1.74 (strong), ret=+7.1%
  - 2021: S=-0.02 (negative), ret=-0.0%
  - 2022: S=0.67 (moderate), ret=+1.5%
  - 2023: S=1.81 (strong), ret=+1.8%

## Risk & Drawdown
- Max drawdown: 1.61% over 428 days (recovered)
- Annualized: return +2.3%, volatility 2.4% (fraction of booksize)
- Hit rate: 2.2% positive days
- Tail shape: skew +14.07, excess kurtosis +315.39

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.64, max 2.54, latest 1.80

## Yearly & Monthly Returns
Best year (by Sharpe): 2023; worst year: 2021
Best month: +5.14%; worst month: -0.57%
Positive months: 72%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=1.72
- Sideways: S=-0.14
- Bear: S=1.09

## Negated Direction
Best negated: `rank(-1 * rp_nip_credit_ratings)` S=0.85, F=0.29, INFERIOR
Direction gap: -0.21 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * rp_nip_credit_ratings)`: S=0.85, F=0.29, T=163.5%, INFERIOR (TOP3000)
- `rank(-1 * rp_nip_credit_ratings / close)`: S=0.32, F=0.07, T=167.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(rp_nip_credit_ratings, 5))`: S=-0.61, F=-0.31, T=77.3%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(rp_nip_credit_ratings, 5))` | TOP200 | 0.96 | 0.50 | 1.6% | 80% | all-weather |
| `rank(ts_delta(rp_nip_credit_ratings, 5))` | TOP1000 | 0.58 | 0.41 | 16.5% | 80% | all-weather |
| `rank(ts_delta(rp_nip_credit_ratings, 5))` | TOP500 | 0.60 | 0.35 | 17.6% | 80% | all-weather |
| `rank(ts_delta(rp_nip_credit_ratings, 5))` | TOP3000 | 0.61 | 0.31 | 25.3% | 80% | mixed |
| `rank(rp_nip_credit_ratings)` | TOP500 | 0.63 | 0.23 | 25.2% | 60% | mixed |
| `rank(rp_nip_credit_ratings)` | TOP1000 | 0.18 | 0.03 | 48.9% | 40% | mixed |

## Correlation Notes
Top correlates:
- min_free_cash_flow_per_share_guidance: 0.178 (weakly positively correlated)
- free_cash_flow_per_share_max_guidance: 0.178 (weakly positively correlated)
- fnd2_q_flintasamt1expythree: 0.147 (weakly positively correlated)
- fnd2_q_flintasamt1expytwo: 0.126 (weakly positively correlated)
- fnd2_q_flintasamt1expyfour: 0.123 (weakly positively correlated)

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| fn_line_of_credit_facility_amount_out_q | fundamental2 | -0.05 | 1.52 | +0.39 | -0.84 | yes |
| fnd6_exre | fundamental6 | -0.04 | 1.42 | +0.40 | -0.60 | yes |
| anl4_ebitda_number | analyst4 | -0.05 | 1.45 | +0.41 | -0.35 | yes |
| fn_repayments_of_lt_debt_q | fundamental2 | -0.04 | 1.46 | +0.38 | -0.67 | yes |
| fnd6_dclo | fundamental6 | -0.01 | 1.33 | +0.37 | -0.71 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, rank_value_norm, trade_when
