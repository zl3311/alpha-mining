---
field: rp_nip_credit
dataset: news18
best_template: rank_delta
best_sharpe: 0.41
best_fitness: 0.21
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 21
regime_profile: weak
n_variations_with_pnl: 4
max_drawdown: 0.2098
ann_vol: 0.1255
hit_rate: 0.0891
rolling_sharpe_min: -2.008
rolling_sharpe_max: 1.745
negated_best_sharpe: 0.04
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.0
n_negated_sims: 4
direction_gap: -0.37
---
# rp_nip_credit (news18)

*News impact projection of credit news*

## Signal Profile
- `rank(rp_nip_credit)`: S=0.25, F=0.06, T=154.4%, INFERIOR (TOP1000)
- `rank(rp_nip_credit / close)`: S=0.23, F=0.05, T=155.3%, INFERIOR (TOP3000)
- `rank(ts_delta(rp_nip_credit, 5))`: S=0.41, F=0.21, T=20.2%, INFERIOR (TOP3000)
- `-rank(rp_nip_credit)`: S=-0.25, F=-0.06, T=154.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(rp_nip_credit, 5))`: S=-0.41, F=-0.21, T=20.2%, INFERIOR (TOP3000)
- `-ts_zscore(rp_nip_credit, 63)`: S=-0.23, F=-0.06, T=143.6%, INFERIOR (TOP3000)
- `ts_mean(rp_nip_credit, 10)`: S=-0.12, F=-0.02, T=38.7%, INFERIOR (TOP3000)
- `rank(ts_rank(rp_nip_credit, 22))`: S=0.01, F=0.00, T=145.8%, INFERIOR (TOP3000)
- `rank(-1 * rp_nip_credit)`: S=-0.26, F=-0.05, T=179.5%, INFERIOR (TOP3000)
- `rank(-1 * rp_nip_credit / close)`: S=0.04, F=0.00, T=179.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 21F/0P
- HIGH_TURNOVER: 13F/8P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 21F/0P
- LOW_SUB_UNIVERSE_SHARPE: 10F/9P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.40, Consistency 40% positive years (2/5)
Yearly breakdown:
  - 2019: S=-1.14 (negative), ret=-4.1%
  - 2020: S=-0.19 (negative), ret=-2.4%
  - 2021: S=0.09 (weak), ret=+0.8%
  - 2022: S=-0.32 (negative), ret=-2.0%
  - 2023: S=1.53 (strong), ret=+32.5%

## Risk & Drawdown
- Max drawdown: 20.98% over 1514 days (recovered)
- Annualized: return +5.1%, volatility 12.6% (fraction of booksize)
- Hit rate: 8.9% positive days
- Tail shape: skew +8.03, excess kurtosis +174.92

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.01, max 1.75, latest 1.53

## Yearly & Monthly Returns
Best year (by Sharpe): 2023; worst year: 2019
Best month: +12.58%; worst month: -7.93%
Positive months: 51%

## Regime Profile
Regime profile: **weak**
- Bull: S=0.07
- Sideways: S=1.11
- Bear: S=-0.36

## Negated Direction
Best negated: `rank(-1 * rp_nip_credit / close)` S=0.04, F=0.00, INFERIOR
Direction gap: -0.37 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * rp_nip_credit)`: S=-0.26, F=-0.05, T=179.5%, INFERIOR (TOP3000)
- `rank(-1 * rp_nip_credit / close)`: S=0.04, F=0.00, T=179.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(rp_nip_credit, 5))`: S=-0.41, F=-0.21, T=20.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(rp_nip_credit, 5))` | TOP3000 | 0.40 | 0.21 | 21.0% | 40% | weak |
| `rank(rp_nip_credit)` | TOP1000 | 0.25 | 0.06 | 37.7% | 60% | mixed |
| `rank(ts_delta(rp_nip_credit, 5))` | TOP500 | 0.14 | 0.05 | 17.0% | 40% | mixed |
| `rank(rp_nip_credit)` | TOP3000 | 0.26 | 0.05 | 44.0% | 60% | weak |

## Correlation Notes
Top correlates:
- fnd6_txdbcl: -0.120 (weakly negatively correlated)
- fnd2_a_stkdrgprdvalnewissues: -0.116 (weakly negatively correlated)
- fnd6_newqv1300_tfvceq: -0.112 (weakly negatively correlated)
- news_mins_10_chg: -0.109 (weakly negatively correlated)
- fnd6_acqgdwl: -0.103 (weakly negatively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
