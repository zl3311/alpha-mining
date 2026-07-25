---
field: news_spy_last
dataset: news12
best_template: rank_level
best_sharpe: 0.27
best_fitness: 0.04
best_universe: TOP200
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 21
regime_profile: weak
n_variations_with_pnl: 3
max_drawdown: 0.1373
ann_vol: 0.0762
hit_rate: 0.4891
rolling_sharpe_min: -2.001
rolling_sharpe_max: 1.568
negated_best_sharpe: 0.36
negated_best_template: rank_neg_delta
negated_best_fitness: 0.04
n_negated_sims: 4
direction_gap: 0.09
---
# news_spy_last (news12)

*SPY last price at the time of the news*

## Signal Profile
- `rank(news_spy_last)`: S=0.27, F=0.04, T=99.0%, INFERIOR (TOP200)
- `rank(news_spy_last / close)`: S=-0.05, F=-0.01, T=60.3%, INFERIOR (TOP3000)
- `rank(ts_delta(news_spy_last, 5))`: S=-0.05, F=0.00, T=110.7%, INFERIOR (TOP200)
- `-rank(news_spy_last)`: S=0.20, F=0.02, T=113.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(news_spy_last, 5))`: S=0.36, F=0.04, T=138.8%, INFERIOR (TOP3000)
- `ts_zscore(news_spy_last, 22)`: S=0.16, F=0.01, T=97.2%, INFERIOR (TOP3000)
- `ts_mean(news_spy_last, 10)`: S=-0.71, F=-0.25, T=32.7%, INFERIOR (TOP3000)
- `rank(ts_rank(news_spy_last, 22))`: S=-0.31, F=-0.03, T=100.9%, INFERIOR (TOP3000)
- `rank(-1 * news_spy_last)`: S=-0.35, F=-0.03, T=120.9%, INFERIOR (TOP3000)
- `rank(-1 * news_spy_last / close)`: S=0.17, F=0.03, T=70.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 1F/20P
- HIGH_TURNOVER: 19F/2P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 21F/0P
- LOW_SUB_UNIVERSE_SHARPE: 6F/13P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.26, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.44 (negative), ret=-2.6%
  - 2020: S=1.14 (moderate), ret=+8.0%
  - 2021: S=0.53 (moderate), ret=+5.5%
  - 2022: S=-0.81 (negative), ret=-6.3%
  - 2023: S=0.93 (moderate), ret=+5.0%

## Risk & Drawdown
- Max drawdown: 13.73% over 763 days (not yet recovered, ongoing at window end)
- Annualized: return +2.0%, volatility 7.6% (fraction of booksize)
- Hit rate: 48.9% positive days
- Tail shape: skew +0.23, excess kurtosis +4.35

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.00, max 1.57, latest 0.84

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2022
Best month: +7.55%; worst month: -6.92%
Positive months: 48%

## Regime Profile
Regime profile: **weak**
- Bull: S=-0.02
- Sideways: S=0.38
- Bear: S=0.45

## Negated Direction
Best negated: `rank(-1 * ts_delta(news_spy_last, 5))` S=0.36, F=0.04, INFERIOR
Direction gap: +0.09 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * news_spy_last)`: S=-0.35, F=-0.03, T=120.9%, INFERIOR (TOP3000)
- `rank(-1 * news_spy_last / close)`: S=0.17, F=0.03, T=70.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(news_spy_last, 5))`: S=0.36, F=0.04, T=138.8%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(news_spy_last)` | TOP200 | 0.26 | 0.04 | 13.7% | 60% | weak |
| `rank(news_spy_last)` | TOP500 | 0.28 | 0.03 | 5.7% | 60% | mixed |
| `rank(news_spy_last)` | TOP3000 | 0.33 | 0.03 | 5.6% | 80% | mixed |

## Correlation Notes
Top correlates:
- unsystematic_risk_last_30_days: 0.154 (weakly positively correlated)
- anl4_cff_value: 0.147 (weakly positively correlated)
- financing_cashflow_reported_value: 0.147 (weakly positively correlated)
- anl4_cfi_mean: 0.130 (weakly positively correlated)
- anl4_cfi_median: 0.129 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
