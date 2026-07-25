---
field: fnd6_prcc
dataset: fundamental6
best_template: rank_neg_delta
best_sharpe: 0.58
best_fitness: 0.22
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: weak
n_variations_with_pnl: 4
max_drawdown: 0.2186
ann_vol: 0.1567
hit_rate: 0.4826
rolling_sharpe_min: -1.17
rolling_sharpe_max: 1.183
negated_best_sharpe: 0.58
negated_best_template: rank_neg_delta
negated_best_fitness: 0.22
n_negated_sims: 10
direction_gap: 0.37
---
# fnd6_prcc (fundamental6)

*Price Close - Annual*

## Signal Profile
- `rank(fnd6_prcc)`: S=0.17, F=0.07, T=1.0%, INFERIOR (TOP3000)
- `rank(fnd6_prcc / close)`: S=0.21, F=0.11, T=5.7%, INFERIOR (TOP1000)
- `rank(ts_delta(fnd6_prcc, 5))`: S=-0.06, F=-0.01, T=36.1%, INFERIOR (TOP500)
- `-rank(fnd6_prcc)`: S=0.06, F=0.01, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_prcc, 5))`: S=0.58, F=0.22, T=34.2%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_prcc, 63)`: S=0.23, F=0.07, T=17.9%, INFERIOR (TOP3000)
- `ts_mean(fnd6_prcc, 10)`: S=0.15, F=0.05, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_prcc, 22))`: S=-0.11, F=-0.02, T=12.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_prcc)`: S=0.38, F=0.21, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_prcc / close)`: S=0.14, F=0.06, T=6.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 5F/27P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 16F/4P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.20, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.60 (moderate), ret=+4.7%
  - 2020: S=0.79 (moderate), ret=+15.9%
  - 2021: S=0.21 (weak), ret=+2.4%
  - 2022: S=-0.53 (negative), ret=-11.9%
  - 2023: S=0.49 (weak), ret=+3.9%

## Risk & Drawdown
- Max drawdown: 21.86% over 896 days (not yet recovered, ongoing at window end)
- Annualized: return +3.1%, volatility 15.7% (fraction of booksize)
- Hit rate: 48.3% positive days
- Tail shape: skew +1.15, excess kurtosis +7.11

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.17, max 1.18, latest 0.74

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2022
Best month: +9.69%; worst month: -8.18%
Positive months: 54%

## Regime Profile
Regime profile: **weak**
- Bull: S=0.44
- Sideways: S=-0.40
- Bear: S=0.35

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_prcc, 5))` S=0.58, F=0.22, INFERIOR
Direction gap: +0.37 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fnd6_prcc)`: S=0.38, F=0.21, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_prcc / close)`: S=0.14, F=0.06, T=6.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_prcc, 5))`: S=0.58, F=0.22, T=34.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_prcc / close)` | TOP1000 | 0.20 | 0.11 | 21.9% | 80% | weak |
| `rank(fnd6_prcc / close)` | TOP3000 | 0.18 | 0.10 | 25.9% | 80% | mixed |
| `rank(fnd6_prcc)` | TOP3000 | 0.16 | 0.07 | 43.5% | 80% | bull-only |
| `rank(fnd6_prcc / close)` | TOP500 | 0.11 | 0.05 | 21.1% | 60% | mixed |

## Correlation Notes
Top correlates:
- fnd6_prcl: 0.867 (strongly positively correlated)
- fnd6_prch: 0.847 (strongly positively correlated)
- fn_oth_comp_fair_value_a: 0.740 (strongly positively correlated)
- fnd6_prchq: 0.723 (strongly positively correlated)
- fn_oth_comp_grants_weighted_avg_grant_date_fair_value_a: 0.692 (moderately positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
