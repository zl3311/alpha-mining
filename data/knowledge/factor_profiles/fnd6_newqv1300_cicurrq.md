---
field: fnd6_newqv1300_cicurrq
dataset: fundamental6
best_template: rank_delta
best_sharpe: 0.72
best_fitness: 0.33
best_universe: TOP500
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 5
max_drawdown: 0.2522
ann_vol: 0.1681
hit_rate: 0.5085
rolling_sharpe_min: -1.03
rolling_sharpe_max: 2.651
negated_best_sharpe: 0.23
negated_best_template: neg_rank_level
negated_best_fitness: 0.07
n_negated_sims: 10
direction_gap: -0.49
---
# fnd6_newqv1300_cicurrq (fundamental6)

*Comp Inc - Currency Trans Adj*

## Signal Profile
- `rank(fnd6_newqv1300_cicurrq)`: S=0.16, F=0.06, T=10.9%, INFERIOR (TOP200)
- `rank(fnd6_newqv1300_cicurrq / close)`: S=0.17, F=0.07, T=10.8%, INFERIOR (TOP200)
- `rank(ts_delta(fnd6_newqv1300_cicurrq, 5))`: S=0.72, F=0.33, T=56.1%, INFERIOR (TOP500)
- `-rank(fnd6_newqv1300_cicurrq)`: S=-0.03, F=0.00, T=8.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_cicurrq, 5))`: S=0.10, F=0.01, T=46.8%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_newqv1300_cicurrq, 63)`: S=-0.29, F=-0.08, T=23.0%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newqv1300_cicurrq, 10)`: S=0.39, F=0.17, T=5.4%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newqv1300_cicurrq, 22))`: S=0.14, F=0.03, T=21.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_cicurrq)`: S=0.23, F=0.07, T=6.6%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_cicurrq / close)`: S=0.16, F=0.04, T=6.6%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 10F/22P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/16P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.72, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=2.15 (strong), ret=+24.5%
  - 2020: S=0.94 (moderate), ret=+17.8%
  - 2021: S=-0.64 (negative), ret=-12.2%
  - 2022: S=1.66 (strong), ret=+29.0%
  - 2023: S=0.04 (weak), ret=+0.6%

## Risk & Drawdown
- Max drawdown: 25.22% over 474 days (recovered)
- Annualized: return +12.2%, volatility 16.8% (fraction of booksize)
- Hit rate: 50.8% positive days
- Tail shape: skew +0.31, excess kurtosis +8.60

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.03, max 2.65, latest 0.03

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2021
Best month: +13.66%; worst month: -10.54%
Positive months: 59%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.68
- Sideways: S=1.28
- Bear: S=0.17

## Negated Direction
Best negated: `rank(-1 * fnd6_newqv1300_cicurrq)` S=0.23, F=0.07, INFERIOR
Direction gap: -0.49 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_newqv1300_cicurrq)`: S=0.23, F=0.07, T=6.6%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_cicurrq / close)`: S=0.16, F=0.04, T=6.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_cicurrq, 5))`: S=0.10, F=0.01, T=46.8%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_newqv1300_cicurrq, 5))` | TOP500 | 0.72 | 0.33 | 25.2% | 80% | mixed |
| `rank(ts_delta(fnd6_newqv1300_cicurrq, 5))` | TOP1000 | 0.30 | 0.08 | 33.8% | 40% | mixed |
| `rank(fnd6_newqv1300_cicurrq / close)` | TOP200 | 0.18 | 0.07 | 24.9% | 60% | mixed |
| `rank(fnd6_newqv1300_cicurrq)` | TOP200 | 0.17 | 0.06 | 25.8% | 80% | mixed |
| `rank(fnd6_newqv1300_cicurrq / close)` | TOP1000 | 0.17 | 0.05 | 15.9% | 60% | mixed |

## Correlation Notes
Top correlates:
- fnd6_newqv1300_rectaq: 0.541 (moderately positively correlated)
- fnd6_newqv1300_acomincq: 0.356 (weakly positively correlated)
- fn_oth_income_loss_fx_transaction_and_tax_translation_adj_q: 0.260 (weakly positively correlated)
- fn_oth_income_loss_net_of_tax_q: 0.154 (weakly positively correlated)
- fnd6_sppe: 0.128 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
