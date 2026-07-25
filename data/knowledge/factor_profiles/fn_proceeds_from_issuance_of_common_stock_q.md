---
field: fn_proceeds_from_issuance_of_common_stock_q
dataset: fundamental2
best_template: rank_neg_delta
best_sharpe: 0.88
best_fitness: 0.68
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 8
max_drawdown: 0.1047
ann_vol: 0.0562
hit_rate: 0.4947
rolling_sharpe_min: -1.896
rolling_sharpe_max: 2.304
negated_best_sharpe: 0.88
negated_best_template: rank_neg_delta
negated_best_fitness: 0.68
n_negated_sims: 10
direction_gap: 0.35
---
# fn_proceeds_from_issuance_of_common_stock_q (fundamental2)

*The cash inflow from the additional capital contribution to the entity.*

## Signal Profile
- `rank(fn_proceeds_from_issuance_of_common_stock_q)`: S=0.41, F=0.17, T=2.3%, INFERIOR (TOP1000)
- `rank(fn_proceeds_from_issuance_of_common_stock_q / close)`: S=0.46, F=0.21, T=2.4%, INFERIOR (TOP1000)
- `rank(ts_delta(fn_proceeds_from_issuance_of_common_stock_q, 5))`: S=-0.03, F=0.00, T=35.9%, INFERIOR (TOP3000)
- `-rank(fn_proceeds_from_issuance_of_common_stock_q)`: S=-0.41, F=-0.17, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_proceeds_from_issuance_of_common_stock_q, 5))`: S=0.88, F=0.68, T=34.8%, INFERIOR (TOP3000)
- `-ts_zscore(fn_proceeds_from_issuance_of_common_stock_q, 63)`: S=0.53, F=0.29, T=15.6%, INFERIOR (TOP3000)
- `ts_mean(fn_proceeds_from_issuance_of_common_stock_q, 10)`: S=0.01, F=0.00, T=2.4%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_proceeds_from_issuance_of_common_stock_q, 22))`: S=-0.17, F=-0.06, T=17.5%, INFERIOR (TOP3000)
- `rank(-1 * fn_proceeds_from_issuance_of_common_stock_q)`: S=-0.12, F=-0.04, T=3.2%, INFERIOR (TOP3000)
- `rank(-1 * fn_proceeds_from_issuance_of_common_stock_q / close)`: S=-0.26, F=-0.13, T=3.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 11F/21P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 10F/10P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.46, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-1.86 (negative), ret=-7.2%
  - 2020: S=-0.08 (negative), ret=-0.4%
  - 2021: S=1.80 (strong), ret=+13.4%
  - 2022: S=1.15 (moderate), ret=+6.6%
  - 2023: S=0.05 (weak), ret=+0.2%

## Risk & Drawdown
- Max drawdown: 10.47% over 760 days (recovered)
- Annualized: return +2.6%, volatility 5.6% (fraction of booksize)
- Hit rate: 49.5% positive days
- Tail shape: skew +0.47, excess kurtosis +3.86

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.90, max 2.30, latest 0.01

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2019
Best month: +5.90%; worst month: -3.63%
Positive months: 52%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.90
- Sideways: S=0.17
- Bear: S=0.29

## Negated Direction
Best negated: `rank(-1 * ts_delta(fn_proceeds_from_issuance_of_common_stock_q, 5))` S=0.88, F=0.68, INFERIOR
Direction gap: +0.35 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fn_proceeds_from_issuance_of_common_stock_q)`: S=-0.12, F=-0.04, T=3.2%, INFERIOR (TOP3000)
- `rank(-1 * fn_proceeds_from_issuance_of_common_stock_q / close)`: S=-0.26, F=-0.13, T=3.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_proceeds_from_issuance_of_common_stock_q, 5))`: S=0.88, F=0.68, T=34.8%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fn_proceeds_from_issuance_of_common_stock_q / close)` | TOP1000 | 0.46 | 0.21 | 10.5% | 60% | mixed |
| `rank(fn_proceeds_from_issuance_of_common_stock_q)` | TOP1000 | 0.40 | 0.17 | 10.7% | 60% | mixed |
| `rank(fn_proceeds_from_issuance_of_common_stock_q / close)` | TOP200 | 0.27 | 0.13 | 14.6% | 60% | bull-only |
| `rank(fn_proceeds_from_issuance_of_common_stock_q / close)` | TOP500 | 0.27 | 0.11 | 12.8% | 60% | bull-only |
| `rank(fn_proceeds_from_issuance_of_common_stock_q / close)` | TOP3000 | 0.33 | 0.11 | 9.4% | 60% | mixed |
| `rank(fn_proceeds_from_issuance_of_common_stock_q)` | TOP3000 | 0.33 | 0.10 | 7.2% | 60% | mixed |
| `rank(fn_proceeds_from_issuance_of_common_stock_q)` | TOP500 | 0.18 | 0.06 | 14.8% | 60% | bull-only |
| `rank(fn_proceeds_from_issuance_of_common_stock_q)` | TOP200 | 0.12 | 0.04 | 20.1% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd2_a_sbcpnargmsptawervl: -0.342 (weakly negatively correlated)
- fnd6_cstkcvq: 0.338 (weakly positively correlated)
- fnd6_cstkcv: 0.299 (weakly positively correlated)
- fn_debt_instrument_interest_rate_stated_percentage_q: 0.290 (weakly positively correlated)
- cash_flow_from_financing: -0.276 (weakly negatively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
