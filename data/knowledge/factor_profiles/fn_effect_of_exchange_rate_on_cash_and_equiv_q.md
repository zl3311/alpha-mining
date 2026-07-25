---
field: fn_effect_of_exchange_rate_on_cash_and_equiv_q
dataset: fundamental2
best_template: rank_delta
best_sharpe: 0.6
best_fitness: 0.38
best_universe: TOP500
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bear-only
n_variations_with_pnl: 5
max_drawdown: 0.2531
ann_vol: 0.1768
hit_rate: 0.5174
rolling_sharpe_min: -1.165
rolling_sharpe_max: 1.923
negated_best_sharpe: 0.2
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.05
n_negated_sims: 10
direction_gap: -0.4
---
# fn_effect_of_exchange_rate_on_cash_and_equiv_q (fundamental2)

*Amount of increase (decrease) from the effect of exchange rate changes on cash and cash equivalent balances held in foreign currencies.*

## Signal Profile
- `rank(fn_effect_of_exchange_rate_on_cash_and_equiv_q)`: S=0.36, F=0.11, T=1.7%, INFERIOR (TOP1000)
- `rank(fn_effect_of_exchange_rate_on_cash_and_equiv_q / close)`: S=0.53, F=0.20, T=1.9%, INFERIOR (TOP1000)
- `rank(ts_delta(fn_effect_of_exchange_rate_on_cash_and_equiv_q, 5))`: S=0.60, F=0.38, T=26.2%, INFERIOR (TOP500)
- `-rank(fn_effect_of_exchange_rate_on_cash_and_equiv_q)`: S=-0.36, F=-0.11, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_effect_of_exchange_rate_on_cash_and_equiv_q, 5))`: S=-0.65, F=-0.43, T=26.2%, INFERIOR (TOP3000)
- `ts_zscore(fn_effect_of_exchange_rate_on_cash_and_equiv_q, 22)`: S=-0.53, F=-0.31, T=29.9%, INFERIOR (TOP3000)
- `ts_mean(fn_effect_of_exchange_rate_on_cash_and_equiv_q, 10)`: S=-0.25, F=-0.08, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_effect_of_exchange_rate_on_cash_and_equiv_q, 22))`: S=-0.19, F=-0.07, T=13.7%, INFERIOR (TOP3000)
- `rank(-1 * fn_effect_of_exchange_rate_on_cash_and_equiv_q)`: S=0.18, F=0.04, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * fn_effect_of_exchange_rate_on_cash_and_equiv_q / close)`: S=0.20, F=0.05, T=2.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 17F/12P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.60, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.60 (moderate), ret=+5.5%
  - 2020: S=0.95 (moderate), ret=+14.2%
  - 2021: S=0.80 (moderate), ret=+24.2%
  - 2022: S=1.02 (moderate), ret=+16.0%
  - 2023: S=-1.12 (negative), ret=-7.6%

## Risk & Drawdown
- Max drawdown: 25.31% over 357 days (recovered)
- Annualized: return +10.7%, volatility 17.7% (fraction of booksize)
- Hit rate: 51.7% positive days
- Tail shape: skew +0.44, excess kurtosis +81.75

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.17, max 1.92, latest -1.13

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2023
Best month: +22.34%; worst month: -19.70%
Positive months: 59%

## Regime Profile
Regime profile: **bear-only**
- Bull: S=-0.69
- Sideways: S=1.79
- Bear: S=1.09

## Negated Direction
Best negated: `rank(-1 * fn_effect_of_exchange_rate_on_cash_and_equiv_q / close)` S=0.20, F=0.05, INFERIOR
Direction gap: -0.40 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fn_effect_of_exchange_rate_on_cash_and_equiv_q)`: S=0.18, F=0.04, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * fn_effect_of_exchange_rate_on_cash_and_equiv_q / close)`: S=0.20, F=0.05, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_effect_of_exchange_rate_on_cash_and_equiv_q, 5))`: S=-0.65, F=-0.43, T=26.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fn_effect_of_exchange_rate_on_cash_and_equiv_q, 5))` | TOP500 | 0.60 | 0.38 | 25.3% | 80% | bear-only |
| `rank(fn_effect_of_exchange_rate_on_cash_and_equiv_q / close)` | TOP1000 | 0.53 | 0.20 | 6.4% | 60% | mixed |
| `rank(ts_delta(fn_effect_of_exchange_rate_on_cash_and_equiv_q, 5))` | TOP1000 | 0.36 | 0.17 | 22.9% | 40% | mixed |
| `rank(fn_effect_of_exchange_rate_on_cash_and_equiv_q)` | TOP1000 | 0.36 | 0.11 | 6.1% | 60% | mixed |
| `rank(ts_delta(fn_effect_of_exchange_rate_on_cash_and_equiv_q, 5))` | TOP3000 | 0.12 | 0.03 | 36.8% | 60% | mixed |

## Correlation Notes
Top correlates:
- fn_effect_of_exchange_rate_on_cash_and_equiv_a: 0.298 (weakly positively correlated)
- fnd2_eixrtreclstatelocalitxes: 0.228 (weakly positively correlated)
- fn_new_shares_issued_a: -0.203 (weakly negatively correlated)
- fn_oth_income_loss_fx_transaction_and_tax_translation_adj_q: 0.195 (weakly positively correlated)
- fnd6_txndb: 0.176 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
