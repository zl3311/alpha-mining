---
field: fn_oth_income_loss_fx_transaction_and_tax_translation_adj_q
dataset: fundamental2
best_template: rank_delta
best_sharpe: 0.78
best_fitness: 0.37
best_universe: TOP500
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 5
max_drawdown: 0.1284
ann_vol: 0.1066
hit_rate: 0.5069
rolling_sharpe_min: -0.668
rolling_sharpe_max: 2.321
negated_best_sharpe: 0.34
negated_best_template: neg_rank_level
negated_best_fitness: 0.13
n_negated_sims: 10
direction_gap: -0.44
---
# fn_oth_income_loss_fx_transaction_and_tax_translation_adj_q (fundamental2)

*Amount after tax and reclassification adjustments of gain (loss) on foreign currency translation adjustments, foreign currency transactions designated and effective as economic hedges of a net investment in a foreign entity and intra-entity foreign currency transactions that are of a long-term-investment nature.*

## Signal Profile
- `rank(fn_oth_income_loss_fx_transaction_and_tax_translation_adj_q)`: S=0.20, F=0.07, T=4.7%, INFERIOR (TOP200)
- `rank(fn_oth_income_loss_fx_transaction_and_tax_translation_adj_q / close)`: S=0.29, F=0.12, T=4.8%, INFERIOR (TOP200)
- `rank(ts_delta(fn_oth_income_loss_fx_transaction_and_tax_translation_adj_q, 5))`: S=0.78, F=0.37, T=35.9%, INFERIOR (TOP500)
- `-rank(fn_oth_income_loss_fx_transaction_and_tax_translation_adj_q)`: S=0.19, F=0.06, T=4.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_oth_income_loss_fx_transaction_and_tax_translation_adj_q, 5))`: S=-0.38, F=-0.11, T=36.4%, INFERIOR (TOP3000)
- `-ts_zscore(fn_oth_income_loss_fx_transaction_and_tax_translation_adj_q, 63)`: S=0.12, F=0.02, T=19.0%, INFERIOR (TOP3000)
- `ts_mean(fn_oth_income_loss_fx_transaction_and_tax_translation_adj_q, 10)`: S=-0.17, F=-0.05, T=3.5%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_oth_income_loss_fx_transaction_and_tax_translation_adj_q, 22))`: S=0.04, F=0.00, T=16.7%, INFERIOR (TOP3000)
- `rank(-1 * fn_oth_income_loss_fx_transaction_and_tax_translation_adj_q)`: S=0.34, F=0.13, T=3.7%, INFERIOR (TOP3000)
- `rank(-1 * fn_oth_income_loss_fx_transaction_and_tax_translation_adj_q / close)`: S=0.16, F=0.04, T=3.8%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 10F/22P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 8F/21P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.79, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=1.95 (strong), ret=+13.0%
  - 2020: S=0.25 (weak), ret=+2.5%
  - 2021: S=1.12 (moderate), ret=+13.0%
  - 2022: S=-0.31 (negative), ret=-4.0%
  - 2023: S=1.74 (strong), ret=+16.8%

## Risk & Drawdown
- Max drawdown: 12.84% over 327 days (recovered)
- Annualized: return +8.4%, volatility 10.7% (fraction of booksize)
- Hit rate: 50.7% positive days
- Tail shape: skew +0.13, excess kurtosis +5.95

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.67, max 2.32, latest 1.75

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2022
Best month: +10.30%; worst month: -6.75%
Positive months: 61%

## Regime Profile
Regime profile: **mixed**
- Bull: S=-0.24
- Sideways: S=1.78
- Bear: S=1.02

## Negated Direction
Best negated: `rank(-1 * fn_oth_income_loss_fx_transaction_and_tax_translation_adj_q)` S=0.34, F=0.13, INFERIOR
Direction gap: -0.44 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fn_oth_income_loss_fx_transaction_and_tax_translation_adj_q)`: S=0.34, F=0.13, T=3.7%, INFERIOR (TOP3000)
- `rank(-1 * fn_oth_income_loss_fx_transaction_and_tax_translation_adj_q / close)`: S=0.16, F=0.04, T=3.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_oth_income_loss_fx_transaction_and_tax_translation_adj_q, 5))`: S=-0.38, F=-0.11, T=36.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fn_oth_income_loss_fx_transaction_and_tax_translation_adj_q, 5))` | TOP500 | 0.79 | 0.37 | 12.8% | 80% | mixed |
| `rank(ts_delta(fn_oth_income_loss_fx_transaction_and_tax_translation_adj_q, 5))` | TOP1000 | 0.39 | 0.12 | 12.8% | 60% | mixed |
| `rank(fn_oth_income_loss_fx_transaction_and_tax_translation_adj_q / close)` | TOP200 | 0.30 | 0.12 | 20.3% | 80% | weak |
| `rank(ts_delta(fn_oth_income_loss_fx_transaction_and_tax_translation_adj_q, 5))` | TOP3000 | 0.44 | 0.11 | 15.0% | 60% | mixed |
| `rank(fn_oth_income_loss_fx_transaction_and_tax_translation_adj_q)` | TOP200 | 0.21 | 0.07 | 20.0% | 60% | weak |

## Correlation Notes
Top correlates:
- fn_oth_income_loss_net_of_tax_q: 0.397 (weakly positively correlated)
- fnd6_newqv1300_cicurrq: 0.260 (weakly positively correlated)
- fn_effect_of_exchange_rate_on_cash_and_equiv_q: 0.195 (weakly positively correlated)
- fnd6_newqv1300_rectaq: 0.148 (weakly positively correlated)
- fnd6_newqv1300_acomincq: 0.141 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
