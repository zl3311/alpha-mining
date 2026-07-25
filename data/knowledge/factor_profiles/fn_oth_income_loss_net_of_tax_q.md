---
field: fn_oth_income_loss_net_of_tax_q
dataset: fundamental2
best_template: rank_delta
best_sharpe: 0.8
best_fitness: 0.4
best_universe: TOP500
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: all-weather
n_variations_with_pnl: 9
max_drawdown: 0.1091
ann_vol: 0.1095
hit_rate: 0.5142
rolling_sharpe_min: -0.459
rolling_sharpe_max: 2.875
negated_best_sharpe: 0.31
negated_best_template: neg_rank_level
negated_best_fitness: 0.09
n_negated_sims: 10
direction_gap: -0.49
---
# fn_oth_income_loss_net_of_tax_q (fundamental2)

*Amount after tax and reclassification adjustments of other comprehensive income (loss).*

## Signal Profile
- `rank(fn_oth_income_loss_net_of_tax_q)`: S=0.32, F=0.13, T=4.7%, INFERIOR (TOP200)
- `rank(fn_oth_income_loss_net_of_tax_q / close)`: S=0.53, F=0.27, T=4.7%, INFERIOR (TOP200)
- `rank(ts_delta(fn_oth_income_loss_net_of_tax_q, 5))`: S=0.80, F=0.40, T=35.8%, INFERIOR (TOP500)
- `-rank(fn_oth_income_loss_net_of_tax_q)`: S=0.05, F=0.01, T=4.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_oth_income_loss_net_of_tax_q, 5))`: S=-0.33, F=-0.08, T=36.5%, INFERIOR (TOP3000)
- `ts_zscore(fn_oth_income_loss_net_of_tax_q, 22)`: S=-0.14, F=-0.03, T=37.5%, INFERIOR (TOP3000)
- `ts_mean(fn_oth_income_loss_net_of_tax_q, 10)`: S=0.58, F=0.27, T=3.4%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_oth_income_loss_net_of_tax_q, 22))`: S=0.32, F=0.09, T=16.7%, INFERIOR (TOP3000)
- `rank(-1 * fn_oth_income_loss_net_of_tax_q)`: S=0.31, F=0.09, T=3.4%, INFERIOR (TOP3000)
- `rank(-1 * fn_oth_income_loss_net_of_tax_q / close)`: S=0.15, F=0.03, T=3.5%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 10F/22P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 15F/14P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.80, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=-0.28 (negative), ret=-1.9%
  - 2020: S=1.26 (moderate), ret=+12.0%
  - 2021: S=0.46 (weak), ret=+5.1%
  - 2022: S=0.35 (weak), ret=+4.5%
  - 2023: S=1.84 (strong), ret=+23.1%

## Risk & Drawdown
- Max drawdown: 10.91% over 274 days (recovered)
- Annualized: return +8.7%, volatility 10.9% (fraction of booksize)
- Hit rate: 51.4% positive days
- Tail shape: skew +1.62, excess kurtosis +17.86

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.46, max 2.88, latest 1.76

## Yearly & Monthly Returns
Best year (by Sharpe): 2023; worst year: 2019
Best month: +11.41%; worst month: -8.39%
Positive months: 63%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=0.52
- Sideways: S=1.08
- Bear: S=0.78

## Negated Direction
Best negated: `rank(-1 * fn_oth_income_loss_net_of_tax_q)` S=0.31, F=0.09, INFERIOR
Direction gap: -0.49 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fn_oth_income_loss_net_of_tax_q)`: S=0.31, F=0.09, T=3.4%, INFERIOR (TOP3000)
- `rank(-1 * fn_oth_income_loss_net_of_tax_q / close)`: S=0.15, F=0.03, T=3.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_oth_income_loss_net_of_tax_q, 5))`: S=-0.33, F=-0.08, T=36.5%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fn_oth_income_loss_net_of_tax_q, 5))` | TOP500 | 0.80 | 0.40 | 10.9% | 80% | all-weather |
| `rank(ts_delta(fn_oth_income_loss_net_of_tax_q, 5))` | TOP1000 | 0.75 | 0.31 | 15.4% | 60% | mixed |
| `rank(fn_oth_income_loss_net_of_tax_q / close)` | TOP200 | 0.52 | 0.27 | 12.9% | 80% | all-weather |
| `rank(fn_oth_income_loss_net_of_tax_q / close)` | TOP500 | 0.35 | 0.13 | 11.7% | 60% | mixed |
| `rank(fn_oth_income_loss_net_of_tax_q)` | TOP200 | 0.33 | 0.13 | 13.4% | 80% | all-weather |
| `rank(ts_delta(fn_oth_income_loss_net_of_tax_q, 5))` | TOP3000 | 0.36 | 0.08 | 21.1% | 80% | weak |
| `rank(ts_delta(fn_oth_income_loss_net_of_tax_q, 5))` | TOP200 | 0.20 | 0.06 | 28.7% | 20% | mixed |
| `rank(fn_oth_income_loss_net_of_tax_q / close)` | TOP1000 | 0.18 | 0.04 | 8.4% | 40% | weak |
| `rank(fn_oth_income_loss_net_of_tax_q)` | TOP500 | 0.14 | 0.03 | 11.7% | 60% | weak |

## Correlation Notes
Top correlates:
- fn_oth_income_loss_fx_transaction_and_tax_translation_adj_q: 0.397 (weakly positively correlated)
- fn_incremental_shares_attributable_to_share_based_payment_q: 0.321 (weakly positively correlated)
- fn_avg_diluted_sharesout_adj_q: 0.299 (weakly positively correlated)
- fn_oth_income_loss_derivatives_qualifying_as_hedges_of_tax_q: 0.176 (weakly positively correlated)
- fnd6_newqv1300_cicurrq: 0.154 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
