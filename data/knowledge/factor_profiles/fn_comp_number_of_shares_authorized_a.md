---
field: fn_comp_number_of_shares_authorized_a
dataset: fundamental2
best_template: rank_value_norm
best_sharpe: 0.53
best_fitness: 0.35
best_universe: TOP200
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: all-weather
n_variations_with_pnl: 6
max_drawdown: 0.1697
ann_vol: 0.101
hit_rate: 0.5045
rolling_sharpe_min: -0.882
rolling_sharpe_max: 1.676
negated_best_sharpe: 0.23
negated_best_template: neg_rank_level
negated_best_fitness: 0.08
n_negated_sims: 10
direction_gap: -0.3
---
# fn_comp_number_of_shares_authorized_a (fundamental2)

*Count of unique IDs of industry participants. Industry stands for an aggregate view of all  equity clearance activity for the date, symbol, and transaction type in question.*

## Signal Profile
- `rank(fn_comp_number_of_shares_authorized_a)`: S=-0.04, F=0.00, T=1.2%, INFERIOR (TOP1000)
- `rank(fn_comp_number_of_shares_authorized_a / close)`: S=0.53, F=0.35, T=2.3%, INFERIOR (TOP200)
- `rank(ts_delta(fn_comp_number_of_shares_authorized_a, 5))`: S=0.18, F=0.06, T=27.0%, INFERIOR (TOP1000)
- `-rank(fn_comp_number_of_shares_authorized_a)`: S=0.04, F=0.00, T=1.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_comp_number_of_shares_authorized_a, 5))`: S=-0.17, F=-0.06, T=23.3%, INFERIOR (TOP3000)
- `-ts_zscore(fn_comp_number_of_shares_authorized_a, 63)`: S=0.22, F=0.13, T=8.5%, INFERIOR (TOP3000)
- `ts_mean(fn_comp_number_of_shares_authorized_a, 10)`: S=0.18, F=0.12, T=2.3%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_comp_number_of_shares_authorized_a, 22))`: S=-0.27, F=-0.14, T=16.0%, INFERIOR (TOP3000)
- `rank(-1 * fn_comp_number_of_shares_authorized_a)`: S=0.23, F=0.08, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * fn_comp_number_of_shares_authorized_a / close)`: S=-0.37, F=-0.16, T=2.0%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 13F/19P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 12F/17P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.52, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.80 (moderate), ret=+6.6%
  - 2020: S=1.02 (moderate), ret=+11.1%
  - 2021: S=-0.53 (negative), ret=-6.2%
  - 2022: S=1.19 (moderate), ret=+13.0%
  - 2023: S=0.21 (weak), ret=+1.4%

## Risk & Drawdown
- Max drawdown: 16.97% over 393 days (recovered)
- Annualized: return +5.3%, volatility 10.1% (fraction of booksize)
- Hit rate: 50.4% positive days
- Tail shape: skew +0.47, excess kurtosis +3.06

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.88, max 1.68, latest 0.30

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2021
Best month: +7.79%; worst month: -5.72%
Positive months: 51%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=1.01
- Sideways: S=-0.13
- Bear: S=0.62

## Negated Direction
Best negated: `rank(-1 * fn_comp_number_of_shares_authorized_a)` S=0.23, F=0.08, INFERIOR
Direction gap: -0.30 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fn_comp_number_of_shares_authorized_a)`: S=0.23, F=0.08, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * fn_comp_number_of_shares_authorized_a / close)`: S=-0.37, F=-0.16, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_comp_number_of_shares_authorized_a, 5))`: S=-0.17, F=-0.06, T=23.3%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fn_comp_number_of_shares_authorized_a / close)` | TOP200 | 0.52 | 0.35 | 17.0% | 80% | all-weather |
| `rank(fn_comp_number_of_shares_authorized_a / close)` | TOP1000 | 0.40 | 0.18 | 7.0% | 80% | mixed |
| `rank(fn_comp_number_of_shares_authorized_a / close)` | TOP500 | 0.36 | 0.16 | 7.6% | 80% | bull-only |
| `rank(ts_delta(fn_comp_number_of_shares_authorized_a, 5))` | TOP1000 | 0.20 | 0.06 | 41.7% | 60% | weak |
| `rank(fn_comp_number_of_shares_authorized_a / close)` | TOP3000 | 0.15 | 0.04 | 22.1% | 40% | mixed |
| `rank(ts_delta(fn_comp_number_of_shares_authorized_a, 5))` | TOP500 | 0.12 | 0.03 | 52.9% | 40% | mixed |

## Correlation Notes
Top correlates:
- fnd6_newa1v1300_cshi: 0.529 (moderately positively correlated)
- fnd6_mfma1_csho: 0.529 (moderately positively correlated)
- fnd6_cshpri: 0.528 (moderately positively correlated)
- fnd6_newa1v1300_cshfd: 0.527 (moderately positively correlated)
- fnd6_newa1v1300_csho: 0.527 (moderately positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
