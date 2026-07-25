---
field: fn_liab_fair_val_l1_a
dataset: fundamental2
cluster: fundamental2_balance_sheet_liab
coverage: 0.3604
community_alphas: 18614
best_template: neg_rank_value_norm
best_sharpe: 0.61
best_fitness: 0.26
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: weak
n_variations_with_pnl: 5
max_drawdown: 0.1042
ann_vol: 0.0688
hit_rate: 0.519
rolling_sharpe_min: -0.792
rolling_sharpe_max: 2.336
negated_best_sharpe: 0.61
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.26
n_negated_sims: 10
direction_gap: 0.13
---
# fn_liab_fair_val_l1_a (fundamental2)

*Liabilities Fair Value, Recurring, Level 1*

## Signal Profile
- `rank(fn_liab_fair_val_l1_a)`: S=0.36, F=0.16, T=1.8%, INFERIOR (TOP200)
- `rank(fn_liab_fair_val_l1_a / close)`: S=0.42, F=0.20, T=2.0%, INFERIOR (TOP200)
- `rank(ts_delta(fn_liab_fair_val_l1_a, 5))`: S=0.11, F=0.03, T=29.2%, INFERIOR (TOP1000)
- `-rank(fn_liab_fair_val_l1_a)`: S=0.46, F=0.17, T=1.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_liab_fair_val_l1_a, 5))`: S=0.00, F=0.00, T=28.9%, INFERIOR (TOP3000)
- `ts_zscore(fn_liab_fair_val_l1_a, 22)`: S=0.09, F=0.03, T=9.7%, INFERIOR (TOP3000)
- `ts_mean(fn_liab_fair_val_l1_a, 10)`: S=0.48, F=0.25, T=0.8%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_liab_fair_val_l1_a, 22))`: S=-0.29, F=-0.16, T=16.3%, INFERIOR (TOP3000)
- `rank(-1 * fn_liab_fair_val_l1_a)`: S=0.46, F=0.17, T=1.1%, INFERIOR (TOP3000)
- `rank(-1 * fn_liab_fair_val_l1_a / close)`: S=0.61, F=0.26, T=1.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 13F/19P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/15P
- LOW_TURNOVER: 3F/29P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.43, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.41 (weak), ret=+1.9%
  - 2020: S=1.79 (strong), ret=+11.1%
  - 2021: S=-0.04 (negative), ret=-0.3%
  - 2022: S=-0.50 (negative), ret=-3.9%
  - 2023: S=0.87 (moderate), ret=+5.8%

## Risk & Drawdown
- Max drawdown: 10.42% over 1108 days (recovered)
- Annualized: return +3.0%, volatility 6.9% (fraction of booksize)
- Hit rate: 51.9% positive days
- Tail shape: skew +0.07, excess kurtosis +1.55

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.79, max 2.34, latest 0.78

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2022
Best month: +4.03%; worst month: -4.65%
Positive months: 52%

## Regime Profile
Regime profile: **weak**
- Bull: S=-0.32
- Sideways: S=1.40
- Bear: S=0.44

## Negated Direction
Best negated: `rank(-1 * fn_liab_fair_val_l1_a / close)` S=0.61, F=0.26, INFERIOR
Direction gap: +0.13 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fn_liab_fair_val_l1_a)`: S=0.46, F=0.17, T=1.1%, INFERIOR (TOP3000)
- `rank(-1 * fn_liab_fair_val_l1_a / close)`: S=0.61, F=0.26, T=1.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_liab_fair_val_l1_a, 5))`: S=0.00, F=0.00, T=28.9%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fn_liab_fair_val_l1_a / close)` | TOP200 | 0.43 | 0.20 | 10.4% | 60% | weak |
| `rank(fn_liab_fair_val_l1_a)` | TOP200 | 0.37 | 0.16 | 11.5% | 80% | weak |
| `rank(fn_liab_fair_val_l1_a)` | TOP500 | 0.33 | 0.11 | 13.9% | 60% | mixed |
| `rank(fn_liab_fair_val_l1_a / close)` | TOP500 | 0.23 | 0.06 | 15.7% | 60% | mixed |
| `rank(ts_delta(fn_liab_fair_val_l1_a, 5))` | TOP1000 | 0.10 | 0.03 | 51.1% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fn_accum_oth_income_loss_net_of_tax_a: 0.314 (weakly positively correlated)
- fnd6_recta: 0.314 (weakly positively correlated)
- goodwill: -0.311 (weakly negatively correlated)
- fnd6_newqv1300_gdwlq: -0.311 (weakly negatively correlated)
- fnd6_loxdr: -0.311 (weakly negatively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
