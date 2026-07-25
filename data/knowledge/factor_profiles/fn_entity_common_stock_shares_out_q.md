---
field: fn_entity_common_stock_shares_out_q
dataset: fundamental2
best_template: ts_mean
best_sharpe: 0.86
best_fitness: 0.71
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: all-weather
n_variations_with_pnl: 5
max_drawdown: 0.1178
ann_vol: 0.0654
hit_rate: 0.5053
rolling_sharpe_min: -1.117
rolling_sharpe_max: 1.766
negated_best_sharpe: 0.91
negated_best_template: rank_neg_delta
negated_best_fitness: 0.44
n_negated_sims: 10
direction_gap: 0.05
---
# fn_entity_common_stock_shares_out_q (fundamental2)

*Indicate number of shares or other units outstanding of each of registrant's classes of capital or common stock or other ownership interests, if and as stated on cover of related periodic report. Where multiple classes or units exist define each class/interest by adding class of stock items such as Common Class A [Member], Common Class B [Member] or Partnership Interest [Member] onto the Instrument [Domain] of the Entity Listings, Instrument.*

## Signal Profile
- `rank(fn_entity_common_stock_shares_out_q)`: S=0.18, F=0.05, T=1.3%, INFERIOR (TOP1000)
- `rank(fn_entity_common_stock_shares_out_q / close)`: S=0.39, F=0.18, T=1.7%, INFERIOR (TOP500)
- `rank(ts_delta(fn_entity_common_stock_shares_out_q, 5))`: S=0.40, F=0.17, T=38.2%, INFERIOR (TOP200)
- `-rank(fn_entity_common_stock_shares_out_q)`: S=-0.18, F=-0.05, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_entity_common_stock_shares_out_q, 5))`: S=0.91, F=0.44, T=36.3%, INFERIOR (TOP3000)
- `-ts_zscore(fn_entity_common_stock_shares_out_q, 63)`: S=0.13, F=0.04, T=19.6%, INFERIOR (TOP3000)
- `ts_mean(fn_entity_common_stock_shares_out_q, 10)`: S=0.86, F=0.71, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_entity_common_stock_shares_out_q, 22))`: S=-0.29, F=-0.10, T=16.2%, INFERIOR (TOP3000)
- `rank(-1 * fn_entity_common_stock_shares_out_q)`: S=-0.18, F=-0.05, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * fn_entity_common_stock_shares_out_q / close)`: S=-0.30, F=-0.13, T=1.5%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 12F/17P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.39, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.23 (weak), ret=+1.0%
  - 2020: S=-0.01 (negative), ret=-0.1%
  - 2021: S=0.36 (weak), ret=+2.9%
  - 2022: S=1.11 (moderate), ret=+6.7%
  - 2023: S=0.42 (weak), ret=+2.1%

## Risk & Drawdown
- Max drawdown: 11.78% over 934 days (not yet recovered, ongoing at window end)
- Annualized: return +2.6%, volatility 6.5% (fraction of booksize)
- Hit rate: 50.5% positive days
- Tail shape: skew +0.40, excess kurtosis +1.46

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.12, max 1.77, latest 0.58

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +4.80%; worst month: -3.26%
Positive months: 54%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=1.32
- Sideways: S=-0.91
- Bear: S=0.64

## Negated Direction
Best negated: `rank(-1 * ts_delta(fn_entity_common_stock_shares_out_q, 5))` S=0.91, F=0.44, INFERIOR
Direction gap: +0.05 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fn_entity_common_stock_shares_out_q)`: S=-0.18, F=-0.05, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * fn_entity_common_stock_shares_out_q / close)`: S=-0.30, F=-0.13, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_entity_common_stock_shares_out_q, 5))`: S=0.91, F=0.44, T=36.3%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fn_entity_common_stock_shares_out_q / close)` | TOP500 | 0.39 | 0.18 | 11.8% | 80% | all-weather |
| `rank(ts_delta(fn_entity_common_stock_shares_out_q, 5))` | TOP200 | 0.40 | 0.17 | 26.4% | 60% | mixed |
| `rank(fn_entity_common_stock_shares_out_q / close)` | TOP1000 | 0.30 | 0.13 | 19.6% | 80% | mixed |
| `rank(fn_entity_common_stock_shares_out_q / close)` | TOP200 | 0.18 | 0.06 | 23.6% | 80% | mixed |
| `rank(fn_entity_common_stock_shares_out_q)` | TOP1000 | 0.18 | 0.05 | 9.7% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_newqv1300_cshprq: 0.910 (strongly positively correlated)
- fnd6_newqv1300_cshoq: 0.909 (strongly positively correlated)
- fnd6_newqv1300_cshiq: 0.909 (strongly positively correlated)
- fnd6_mfmq_cshprq: 0.909 (strongly positively correlated)
- fnd6_newqv1300_cshfdq: 0.909 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
