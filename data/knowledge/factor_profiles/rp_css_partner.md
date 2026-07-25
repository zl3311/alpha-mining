---
field: rp_css_partner
dataset: news18
best_template: neg_rank_value_norm
best_sharpe: 1.28
best_fitness: 0.36
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_FITNESS
n_sims: 20
regime_profile: mixed
n_variations_with_pnl: 5
max_drawdown: 0.1476
ann_vol: 0.104
hit_rate: 0.4955
rolling_sharpe_min: -0.928
rolling_sharpe_max: 2.024
negated_best_sharpe: 1.28
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.36
n_negated_sims: 4
direction_gap: 0.76
---
# rp_css_partner (news18)

*Composite sentiment score of partnership news*

## Signal Profile
- `rank(rp_css_partner)`: S=0.25, F=0.04, T=127.5%, INFERIOR (TOP200)
- `rank(ts_delta(rp_css_partner, 5))`: S=0.52, F=0.11, T=142.2%, INFERIOR (TOP500)
- `-rank(rp_css_partner)`: S=0.58, F=0.11, T=144.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(rp_css_partner, 5))`: S=-0.41, F=-0.07, T=150.8%, INFERIOR (TOP3000)
- `-ts_zscore(rp_css_partner, 63)`: S=0.20, F=0.02, T=143.0%, INFERIOR (TOP3000)
- `ts_mean(rp_css_partner, 10)`: S=-0.43, F=-0.12, T=29.7%, INFERIOR (TOP3000)
- `rank(ts_rank(rp_css_partner, 22))`: S=-0.06, F=0.00, T=145.8%, INFERIOR (TOP3000)
- `rank(-1 * rp_css_partner)`: S=1.30, F=0.34, T=152.2%, INFERIOR (TOP3000)
- `rank(-1 * rp_css_partner / close)`: S=1.28, F=0.36, T=149.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 16F/4P
- HIGH_TURNOVER: 19F/1P
- LOW_FITNESS: 20F/0P
- LOW_SHARPE: 18F/2P
- LOW_SUB_UNIVERSE_SHARPE: 9F/9P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.56, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.72 (moderate), ret=+6.2%
  - 2020: S=0.47 (weak), ret=+5.7%
  - 2021: S=0.36 (weak), ret=+3.6%
  - 2022: S=1.75 (strong), ret=+18.9%
  - 2023: S=-0.69 (negative), ret=-5.8%

## Risk & Drawdown
- Max drawdown: 14.76% over 872 days (recovered)
- Annualized: return +5.9%, volatility 10.4% (fraction of booksize)
- Hit rate: 49.5% positive days
- Tail shape: skew +1.01, excess kurtosis +8.28

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.93, max 2.02, latest -0.67

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2023
Best month: +7.33%; worst month: -7.45%
Positive months: 56%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.93
- Sideways: S=0.49
- Bear: S=0.25

## Negated Direction
Best negated: `rank(-1 * rp_css_partner / close)` S=1.28, F=0.36, INFERIOR
Direction gap: +0.76 (negated - positive best Sharpe). NEGATION DOMINANT — field is significantly stronger when reversed.

Negated template variants:
- `rank(-1 * rp_css_partner)`: S=1.30, F=0.34, T=152.2%, INFERIOR (TOP3000)
- `rank(-1 * rp_css_partner / close)`: S=1.28, F=0.36, T=149.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(rp_css_partner, 5))`: S=-0.41, F=-0.07, T=150.8%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(rp_css_partner, 5))` | TOP1000 | 0.56 | 0.11 | 14.8% | 80% | mixed |
| `rank(ts_delta(rp_css_partner, 5))` | TOP500 | 0.52 | 0.11 | 13.2% | 80% | all-weather |
| `rank(ts_delta(rp_css_partner, 5))` | TOP3000 | 0.41 | 0.07 | 16.6% | 80% | mixed |
| `rank(ts_delta(rp_css_partner, 5))` | TOP200 | 0.39 | 0.07 | 14.8% | 80% | mixed |
| `rank(rp_css_partner)` | TOP200 | 0.26 | 0.04 | 33.7% | 60% | mixed |

## Correlation Notes
Top correlates:
- shareholders_equity_total_2: 0.131 (weakly positively correlated)
- fn_new_shares_options_a: 0.108 (weakly positively correlated)
- fnd6_newqv1300_tfvceq: 0.101 (weakly positively correlated)
- news_pct_10min: -0.091 (weakly negatively correlated)
- fn_excess_tax_benefit_from_share_based_comp_fin_activities_q: 0.089 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_FITNESS. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, rank_value_norm, trade_when
