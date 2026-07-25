---
field: fnd6_city
dataset: fundamental6
best_template: rank_delta
best_sharpe: 1.55
best_fitness: 1.76
best_universe: TOP3000
grade: GOOD
submittability: blocked_CONCENTRATED_WEIGHT
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 2
max_drawdown: 0.2781
ann_vol: 0.15
hit_rate: 0.4955
rolling_sharpe_min: -1.803
rolling_sharpe_max: 3.701
top_merge_partner: rank(scl12_buzz * (-1 * returns))
negated_best_sharpe: 0.75
negated_best_template: neg_rank_level
negated_best_fitness: 0.34
n_negated_sims: 10
direction_gap: -0.8
---
# fnd6_city (fundamental6)

*the city where a company's corporate headquarters or home office is located*

## Signal Profile
- `rank(fnd6_city)`: S=-0.11, F=-0.02, T=1.3%, INFERIOR (TOP1000)
- `rank(fnd6_city / close)`: S=0.00, F=0.00, T=1.6%, INFERIOR (TOP1000)
- `rank(ts_delta(fnd6_city, 5))`: S=1.55, F=1.76, T=18.0%, GOOD (TOP3000)
- `-rank(fnd6_city)`: S=0.11, F=0.02, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_city, 5))`: S=-0.87, F=-0.74, T=18.0%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_city, 22)`: S=0.44, F=0.49, T=2.5%, INFERIOR (TOP3000)
- `ts_mean(fnd6_city, 10)`: S=-0.24, F=-0.09, T=1.5%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_city, 22))`: S=0.32, F=0.25, T=10.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_city)`: S=0.75, F=0.34, T=0.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_city / close)`: S=0.28, F=0.12, T=1.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 31F/1P
- LOW_SHARPE: 31F/1P
- LOW_SUB_UNIVERSE_SHARPE: 21F/8P
- LOW_TURNOVER: 4F/28P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 1.56, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.34 (weak), ret=+2.4%
  - 2020: S=-1.25 (negative), ret=-15.7%
  - 2021: S=2.52 (strong), ret=+45.3%
  - 2022: S=3.04 (strong), ret=+60.2%
  - 2023: S=1.79 (strong), ret=+22.1%

## Risk & Drawdown
- Max drawdown: 27.81% over 566 days (recovered)
- Annualized: return +23.3%, volatility 15.0% (fraction of booksize)
- Hit rate: 49.5% positive days
- Tail shape: skew +1.50, excess kurtosis +9.76

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.80, max 3.70, latest 1.77

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +20.06%; worst month: -5.85%
Positive months: 56%

## Regime Profile
Regime profile: **mixed**
- Bull: S=2.55
- Sideways: S=1.98
- Bear: S=0.10

## Negated Direction
Best negated: `rank(-1 * fnd6_city)` S=0.75, F=0.34, INFERIOR
Direction gap: -0.80 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_city)`: S=0.75, F=0.34, T=0.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_city / close)`: S=0.28, F=0.12, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_city, 5))`: S=-0.87, F=-0.74, T=18.0%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_city, 5))` | TOP3000 | 1.56 | 1.76 | 27.8% | 80% | mixed |
| `rank(ts_delta(fnd6_city, 5))` | TOP500 | 0.19 | 0.10 | 62.8% | 80% | weak |

## Correlation Notes
Top correlates:
- max_share_buyback_guidance: 0.399 (weakly positively correlated)
- min_adjusted_funds_from_operations_adj_guidance: 0.399 (weakly positively correlated)
- max_total_goodwill_guidance_2: 0.399 (weakly positively correlated)
- min_custom_eps_guidance: 0.399 (weakly positively correlated)
- max_adjusted_funds_from_operations_adj_guidance: 0.399 (weakly positively correlated)

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| rank(scl12_buzz * (-1 * returns)) | socialmedia12 | -0.16 | 2.35 | +0.72 | -0.33 | yes |
| rank(fnd6_acdo) * rank(-1 * returns) | unknown | -0.17 | 2.58 | +0.71 | -0.21 | yes |
| implied_volatility_put_10 | option8 | -0.15 | 2.19 | +0.63 | -0.47 | yes |
| current_ratio | fundamental6 | -0.07 | 2.31 | +0.64 | +0.84 | yes |
| implied_volatility_mean_10 | option8 | -0.15 | 2.14 | +0.59 | -0.55 | yes |

## Actionability
Cataloged as active factor but not yet in submitted book.
Blocked by CONCENTRATED_WEIGHT. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
