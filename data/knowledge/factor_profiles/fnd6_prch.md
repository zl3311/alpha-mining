---
field: fnd6_prch
dataset: fundamental6
best_template: rank_neg_delta
best_sharpe: 0.77
best_fitness: 0.34
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 5
max_drawdown: 0.2656
ann_vol: 0.1612
hit_rate: 0.4826
rolling_sharpe_min: -1.063
rolling_sharpe_max: 1.54
negated_best_sharpe: 0.77
negated_best_template: rank_neg_delta
negated_best_fitness: 0.34
n_negated_sims: 10
direction_gap: 0.42
---
# fnd6_prch (fundamental6)

*Price High - Annual*

## Signal Profile
- `rank(fnd6_prch)`: S=0.21, F=0.08, T=0.9%, INFERIOR (TOP3000)
- `rank(fnd6_prch / close)`: S=0.35, F=0.23, T=4.6%, INFERIOR (TOP500)
- `rank(ts_delta(fnd6_prch, 5))`: S=-0.10, F=-0.01, T=36.2%, INFERIOR (TOP500)
- `-rank(fnd6_prch)`: S=-0.06, F=-0.01, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_prch, 5))`: S=0.77, F=0.34, T=34.1%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_prch, 22)`: S=0.19, F=0.04, T=39.9%, INFERIOR (TOP3000)
- `ts_mean(fnd6_prch, 10)`: S=0.21, F=0.08, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_prch, 22))`: S=-0.21, F=-0.06, T=12.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_prch)`: S=0.22, F=0.09, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_prch / close)`: S=-0.14, F=-0.06, T=5.0%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 5F/27P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/7P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.35, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.05 (weak), ret=+0.5%
  - 2020: S=0.99 (moderate), ret=+16.8%
  - 2021: S=0.30 (weak), ret=+3.2%
  - 2022: S=-0.28 (negative), ret=-6.8%
  - 2023: S=1.12 (moderate), ret=+13.7%

## Risk & Drawdown
- Max drawdown: 26.56% over 914 days (not yet recovered, ongoing at window end)
- Annualized: return +5.6%, volatility 16.1% (fraction of booksize)
- Hit rate: 48.3% positive days
- Tail shape: skew +0.81, excess kurtosis +3.86

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.06, max 1.54, latest 1.22

## Yearly & Monthly Returns
Best year (by Sharpe): 2023; worst year: 2022
Best month: +10.81%; worst month: -9.37%
Positive months: 58%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.18
- Sideways: S=-0.83
- Bear: S=1.58

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_prch, 5))` S=0.77, F=0.34, INFERIOR
Direction gap: +0.42 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fnd6_prch)`: S=0.22, F=0.09, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_prch / close)`: S=-0.14, F=-0.06, T=5.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_prch, 5))`: S=0.77, F=0.34, T=34.1%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_prch / close)` | TOP500 | 0.35 | 0.23 | 26.6% | 80% | mixed |
| `rank(fnd6_prch / close)` | TOP1000 | 0.23 | 0.14 | 29.1% | 60% | mixed |
| `rank(fnd6_prch)` | TOP3000 | 0.20 | 0.08 | 38.6% | 80% | bull-only |
| `rank(fnd6_prch / close)` | TOP200 | 0.13 | 0.06 | 29.4% | 60% | weak |
| `rank(fnd6_prch / close)` | TOP3000 | 0.12 | 0.05 | 39.9% | 40% | bear-only |

## Correlation Notes
Top correlates:
- fnd6_prchq: 0.848 (strongly positively correlated)
- fnd6_prcc: 0.847 (strongly positively correlated)
- fn_oth_comp_fair_value_a: 0.771 (strongly positively correlated)
- fn_allocated_share_based_compensation_expense_a: 0.763 (strongly positively correlated)
- fn_comp_not_rec_a: 0.760 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
