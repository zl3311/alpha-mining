---
field: news_mins_20_chg
dataset: news12
best_template: rank_delta
best_sharpe: 126.96
best_fitness: 516.32
best_universe: TOP200
grade: SPECTACULAR
submittability: blocked_HIGH_TURNOVER
n_sims: 21
regime_profile: mixed
n_variations_with_pnl: 5
max_drawdown: -0.0
ann_vol: 0.0424
hit_rate: 0.0016
rolling_sharpe_min: 1.0
rolling_sharpe_max: 1.412
redundancy_cluster: 84
negated_best_sharpe: 0.44
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.28
n_negated_sims: 4
direction_gap: -126.52
---
# news_mins_20_chg (news12)

*The minimum of L or S above for 20-minute bucket*

## Signal Profile
- `rank(news_mins_20_chg)`: S=0.36, F=0.34, T=34.5%, INFERIOR (TOP1000)
- `rank(news_mins_20_chg / close)`: S=0.15, F=0.11, T=34.9%, INFERIOR (TOP3000)
- `rank(ts_delta(news_mins_20_chg, 5))`: S=126.96, F=516.32, T=100.0%, SPECTACULAR (TOP200)
- `-rank(news_mins_20_chg)`: S=-0.36, F=-0.34, T=34.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(news_mins_20_chg, 5))`: S=-0.02, F=0.00, T=3.2%, INFERIOR (TOP3000)
- `ts_zscore(news_mins_20_chg, 22)`: S=0.66, F=1.13, T=13.7%, AVERAGE (TOP3000)
- `ts_mean(news_mins_20_chg, 10)`: S=-0.18, F=-0.11, T=42.2%, INFERIOR (TOP3000)
- `rank(ts_rank(news_mins_20_chg, 22))`: S=-0.38, F=-0.41, T=28.7%, INFERIOR (TOP3000)
- `rank(-1 * news_mins_20_chg)`: S=0.30, F=0.15, T=139.3%, INFERIOR (TOP3000)
- `rank(-1 * news_mins_20_chg / close)`: S=0.44, F=0.28, T=138.9%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 21F/0P
- HIGH_TURNOVER: 4F/17P
- LOW_FITNESS: 19F/2P
- LOW_SHARPE: 20F/1P
- LOW_SUB_UNIVERSE_SHARPE: 8F/11P
- LOW_TURNOVER: 1F/20P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.64, Consistency 20% positive years (1/5)
Yearly breakdown:
  - 2019: S=0.00 (negative), ret=+0.0%
  - 2020: S=1.48 (moderate), ret=+13.2%
  - 2021: S=0.00 (negative), ret=+0.0%
  - 2022: S=0.00 (negative), ret=+0.0%
  - 2023: S=0.00 (negative), ret=+0.0%

## Risk & Drawdown
- Max drawdown: -0.00% over 0 days (recovered)
- Annualized: return +2.7%, volatility 4.2% (fraction of booksize)
- Hit rate: 0.2% positive days
- Tail shape: skew +25.11, excess kurtosis +633.95

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min 1.00, max 1.41, latest 1.00

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2019
Best month: +13.23%; worst month: +13.23%
Positive months: 100%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.00
- Sideways: S=0.76
- Bear: S=0.79

## Negated Direction
Best negated: `rank(-1 * news_mins_20_chg / close)` S=0.44, F=0.28, INFERIOR
Direction gap: -126.52 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * news_mins_20_chg)`: S=0.30, F=0.15, T=139.3%, INFERIOR (TOP3000)
- `rank(-1 * news_mins_20_chg / close)`: S=0.44, F=0.28, T=138.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(news_mins_20_chg, 5))`: S=-0.02, F=0.00, T=3.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(news_mins_20_chg, 5))` | TOP200 | 0.64 | 516.32 | -0.0% | 20% | mixed |
| `rank(news_mins_20_chg)` | TOP1000 | 0.36 | 0.34 | 145.1% | 40% | all-weather |
| `rank(news_mins_20_chg)` | TOP200 | 0.28 | 0.27 | 50.9% | 60% | mixed |
| `rank(ts_delta(news_mins_20_chg, 5))` | TOP1000 | 0.10 | 0.04 | 11.3% | 40% | weak |
| `rank(ts_delta(news_mins_20_chg, 5))` | TOP500 | 0.09 | 0.03 | 7.8% | 20% | mixed |

## Correlation Notes
Top correlates:
- news_mins_20_pct_up: 1.000 (strongly positively correlated)
- fn_business_combination_assets_aquired_goodwill_q: -0.206 (weakly negatively correlated)
- min_free_cash_flow_per_share_guidance: 0.167 (weakly positively correlated)
- free_cash_flow_per_share_max_guidance: 0.167 (weakly positively correlated)
- pv13_revere_key_sector_total: 0.157 (weakly positively correlated)

Redundancy cluster #84: 2 similar fields, mean |rho| 1.0 (representative: news_mins_20_pct_up). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by HIGH_TURNOVER. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
