---
field: fn_entity_common_stock_shares_out_a
dataset: fundamental2
best_template: ts_mean
best_sharpe: 0.33
best_fitness: 0.26
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 3
max_drawdown: 0.157
ann_vol: 0.0682
hit_rate: 0.4883
rolling_sharpe_min: -0.988
rolling_sharpe_max: 1.947
negated_best_sharpe: 0.31
negated_best_template: rank_neg_delta
negated_best_fitness: 0.15
n_negated_sims: 10
direction_gap: -0.02
---
# fn_entity_common_stock_shares_out_a (fundamental2)

*Indicate number of shares or other units outstanding of each of registrant's classes of capital or common stock or other ownership interests, if and as stated on cover of related periodic report. Where multiple classes or units exist define each class/interest by adding class of stock items such as Common Class A [Member], Common Class B [Member] or Partnership Interest [Member] onto the Instrument [Domain] of the Entity Listings, Instrument.*

## Signal Profile
- `rank(fn_entity_common_stock_shares_out_a)`: S=0.04, F=0.01, T=1.6%, INFERIOR (TOP500)
- `rank(fn_entity_common_stock_shares_out_a / close)`: S=0.41, F=0.19, T=1.8%, INFERIOR (TOP500)
- `rank(ts_delta(fn_entity_common_stock_shares_out_a, 5))`: S=-0.01, F=0.00, T=34.6%, INFERIOR (TOP1000)
- `-rank(fn_entity_common_stock_shares_out_a)`: S=-0.02, F=0.00, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_entity_common_stock_shares_out_a, 5))`: S=0.31, F=0.15, T=32.4%, INFERIOR (TOP3000)
- `-ts_zscore(fn_entity_common_stock_shares_out_a, 63)`: S=0.34, F=0.20, T=18.6%, INFERIOR (TOP3000)
- `ts_mean(fn_entity_common_stock_shares_out_a, 10)`: S=0.33, F=0.26, T=1.5%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_entity_common_stock_shares_out_a, 22))`: S=-0.19, F=-0.06, T=14.4%, INFERIOR (TOP3000)
- `rank(-1 * fn_entity_common_stock_shares_out_a)`: S=0.18, F=0.07, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * fn_entity_common_stock_shares_out_a / close)`: S=-0.08, F=-0.02, T=1.9%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 13F/19P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 5F/15P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.41, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.32 (weak), ret=+1.4%
  - 2020: S=0.31 (weak), ret=+2.4%
  - 2021: S=-0.61 (negative), ret=-5.5%
  - 2022: S=1.85 (strong), ret=+12.1%
  - 2023: S=0.69 (moderate), ret=+3.2%

## Risk & Drawdown
- Max drawdown: 15.70% over 583 days (recovered)
- Annualized: return +2.8%, volatility 6.8% (fraction of booksize)
- Hit rate: 48.8% positive days
- Tail shape: skew +0.45, excess kurtosis +1.75

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.99, max 1.95, latest 0.80

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2021
Best month: +4.02%; worst month: -3.63%
Positive months: 52%

## Regime Profile
Regime profile: **mixed**
- Bull: S=1.39
- Sideways: S=-0.60
- Bear: S=0.17

## Negated Direction
Best negated: `rank(-1 * ts_delta(fn_entity_common_stock_shares_out_a, 5))` S=0.31, F=0.15, INFERIOR
Direction gap: -0.02 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fn_entity_common_stock_shares_out_a)`: S=0.18, F=0.07, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * fn_entity_common_stock_shares_out_a / close)`: S=-0.08, F=-0.02, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_entity_common_stock_shares_out_a, 5))`: S=0.31, F=0.15, T=32.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fn_entity_common_stock_shares_out_a / close)` | TOP500 | 0.41 | 0.19 | 15.7% | 80% | mixed |
| `rank(fn_entity_common_stock_shares_out_a / close)` | TOP1000 | 0.25 | 0.09 | 14.3% | 60% | mixed |
| `rank(fn_entity_common_stock_shares_out_a / close)` | TOP200 | 0.09 | 0.02 | 23.4% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_mfmq_cshprq: 0.939 (strongly positively correlated)
- fnd6_newqv1300_cshfdq: 0.938 (strongly positively correlated)
- fnd6_newqv1300_cshprq: 0.938 (strongly positively correlated)
- fnd6_newqv1300_cshoq: 0.938 (strongly positively correlated)
- fnd6_newqv1300_csh12q: 0.930 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
