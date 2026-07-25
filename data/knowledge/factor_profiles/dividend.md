---
field: dividend
dataset: pv1
cluster: pv1_cashflow
coverage: 1.0
community_alphas: 11753
best_template: ts_zscore
best_sharpe: 1.02
best_fitness: 0.3
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 21
regime_profile: mixed
n_variations_with_pnl: 4
max_drawdown: 0.0808
ann_vol: 0.0373
hit_rate: 0.5134
rolling_sharpe_min: -1.772
rolling_sharpe_max: 3.226
negated_best_sharpe: 0.19
negated_best_template: neg_rank_level
negated_best_fitness: 0.03
n_negated_sims: 4
direction_gap: -0.83
---
# dividend (pv1)

*Dividend*

## Signal Profile
- `rank(dividend)`: S=0.45, F=0.10, T=54.4%, INFERIOR (TOP1000)
- `rank(dividend / close)`: S=0.45, F=0.10, T=54.4%, INFERIOR (TOP3000)
- `rank(ts_delta(dividend, 5))`: S=0.68, F=0.14, T=57.0%, INFERIOR (TOP1000)
- `-rank(dividend)`: S=-0.45, F=-0.10, T=54.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(dividend, 5))`: S=-0.28, F=-0.03, T=56.6%, INFERIOR (TOP3000)
- `ts_zscore(dividend, 22)`: S=1.02, F=0.30, T=79.3%, INFERIOR (TOP3000)
- `ts_mean(dividend, 10)`: S=-0.21, F=-0.05, T=21.7%, INFERIOR (TOP3000)
- `rank(ts_rank(dividend, 22))`: S=-0.15, F=-0.03, T=15.6%, INFERIOR (TOP3000)
- `rank(-1 * dividend)`: S=0.19, F=0.03, T=52.3%, INFERIOR (TOP3000)
- `rank(-1 * dividend / close)`: S=0.19, F=0.03, T=52.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 5F/16P
- HIGH_TURNOVER: 1F/20P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 21F/0P
- LOW_SUB_UNIVERSE_SHARPE: 7F/12P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.69, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=2.66 (strong), ret=+8.2%
  - 2020: S=0.08 (weak), ret=+0.3%
  - 2021: S=-0.19 (negative), ret=-0.7%
  - 2022: S=1.02 (moderate), ret=+4.0%
  - 2023: S=0.29 (weak), ret=+0.9%

## Risk & Drawdown
- Max drawdown: 8.08% over 1340 days (not yet recovered, ongoing at window end)
- Annualized: return +2.6%, volatility 3.7% (fraction of booksize)
- Hit rate: 51.3% positive days
- Tail shape: skew +0.19, excess kurtosis +2.04

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.77, max 3.23, latest 0.34

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2021
Best month: +4.75%; worst month: -2.53%
Positive months: 61%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.85
- Sideways: S=1.69
- Bear: S=-0.38

## Negated Direction
Best negated: `rank(-1 * dividend)` S=0.19, F=0.03, INFERIOR
Direction gap: -0.83 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * dividend)`: S=0.19, F=0.03, T=52.3%, INFERIOR (TOP3000)
- `rank(-1 * dividend / close)`: S=0.19, F=0.03, T=52.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(dividend, 5))`: S=-0.28, F=-0.03, T=56.6%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(dividend, 5))` | TOP1000 | 0.69 | 0.14 | 8.1% | 80% | mixed |
| `rank(dividend)` | TOP1000 | 0.45 | 0.10 | 14.4% | 60% | bull-only |
| `rank(ts_delta(dividend, 5))` | TOP3000 | 0.28 | 0.03 | 6.6% | 60% | mixed |
| `rank(dividend)` | TOP500 | 0.17 | 0.02 | 13.0% | 60% | bull-only |

## Correlation Notes
Top correlates:
- adjfactor: -0.153 (weakly negatively correlated)
- news_mins_20_pct_up: 0.127 (weakly positively correlated)
- news_mins_20_chg: 0.127 (weakly positively correlated)
- single_sector_pureplay_company_count: -0.099 (weakly negatively correlated)
- primary_sector_focused_company_count: -0.091 (weakly negatively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
