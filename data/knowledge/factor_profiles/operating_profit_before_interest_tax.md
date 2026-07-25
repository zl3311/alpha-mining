---
field: operating_profit_before_interest_tax
dataset: analyst4
best_template: rank_value_norm
best_sharpe: 0.42
best_fitness: 0.26
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 4
max_drawdown: 0.2983
ann_vol: 0.1175
hit_rate: 0.4996
rolling_sharpe_min: -3.146
rolling_sharpe_max: 2.29
negated_best_sharpe: 0.36
negated_best_template: rank_neg_delta
negated_best_fitness: 0.08
n_negated_sims: 10
direction_gap: -0.06
---
# operating_profit_before_interest_tax (analyst4)

*Earnings Before Interest and Taxes (EBIT) - Actual Value*

## Signal Profile
- `rank(operating_profit_before_interest_tax)`: S=0.19, F=0.09, T=1.0%, INFERIOR (TOP3000)
- `rank(operating_profit_before_interest_tax / close)`: S=0.42, F=0.26, T=1.4%, INFERIOR (TOP3000)
- `rank(ts_delta(operating_profit_before_interest_tax, 5))`: S=0.14, F=0.02, T=36.8%, INFERIOR (TOP500)
- `-rank(operating_profit_before_interest_tax)`: S=0.00, F=0.00, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(operating_profit_before_interest_tax, 5))`: S=0.36, F=0.08, T=35.2%, INFERIOR (TOP3000)
- `ts_zscore(operating_profit_before_interest_tax, 22)`: S=0.16, F=0.03, T=39.5%, INFERIOR (TOP3000)
- `ts_mean(operating_profit_before_interest_tax, 10)`: S=-0.07, F=-0.02, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_rank(operating_profit_before_interest_tax, 22))`: S=0.13, F=0.03, T=13.4%, INFERIOR (TOP3000)
- `rank(-1 * operating_profit_before_interest_tax)`: S=-0.19, F=-0.09, T=1.0%, INFERIOR (TOP3000)
- `rank(-1 * operating_profit_before_interest_tax / close)`: S=-0.42, F=-0.26, T=1.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 2F/30P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/15P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.41, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.17 (negative), ret=-0.9%
  - 2020: S=-2.11 (negative), ret=-15.7%
  - 2021: S=1.03 (moderate), ret=+14.6%
  - 2022: S=1.43 (moderate), ret=+24.3%
  - 2023: S=0.13 (weak), ret=+1.3%

## Risk & Drawdown
- Max drawdown: 29.83% over 807 days (recovered)
- Annualized: return +4.8%, volatility 11.8% (fraction of booksize)
- Hit rate: 50.0% positive days
- Tail shape: skew -0.01, excess kurtosis +1.63

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -3.15, max 2.29, latest -0.07

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +9.04%; worst month: -5.56%
Positive months: 46%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.06
- Sideways: S=0.69
- Bear: S=-3.52

## Negated Direction
Best negated: `rank(-1 * ts_delta(operating_profit_before_interest_tax, 5))` S=0.36, F=0.08, INFERIOR
Direction gap: -0.06 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * operating_profit_before_interest_tax)`: S=-0.19, F=-0.09, T=1.0%, INFERIOR (TOP3000)
- `rank(-1 * operating_profit_before_interest_tax / close)`: S=-0.42, F=-0.26, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(operating_profit_before_interest_tax, 5))`: S=0.36, F=0.08, T=35.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(operating_profit_before_interest_tax / close)` | TOP3000 | 0.41 | 0.26 | 29.8% | 60% | bull-only |
| `rank(operating_profit_before_interest_tax)` | TOP3000 | 0.18 | 0.09 | 45.6% | 60% | bull-only |
| `rank(operating_profit_before_interest_tax / close)` | TOP1000 | 0.19 | 0.09 | 30.8% | 60% | bull-only |
| `rank(ts_delta(operating_profit_before_interest_tax, 5))` | TOP500 | 0.14 | 0.02 | 17.6% | 80% | bull-only |

## Correlation Notes
Top correlates:
- net_income_adjusted: 0.988 (strongly positively correlated)
- pretax_income_total: 0.987 (strongly positively correlated)
- net_income_total_2: 0.982 (strongly positively correlated)
- fnd6_newa2v1300_oibdp: 0.979 (strongly positively correlated)
- ebitda: 0.979 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
