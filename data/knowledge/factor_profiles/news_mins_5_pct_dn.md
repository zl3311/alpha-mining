---
field: news_mins_5_pct_dn
dataset: news12
best_template: rank_delta
best_sharpe: 0.76
best_fitness: 0.58
best_universe: TOP200
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 20
regime_profile: mixed
n_variations_with_pnl: 6
max_drawdown: 0.3869
ann_vol: 0.3396
hit_rate: 0.1976
rolling_sharpe_min: -1.206
rolling_sharpe_max: 2.809
negated_best_sharpe: -0.09
negated_best_template: neg_rank
negated_best_fitness: -0.01
n_negated_sims: 4
direction_gap: -0.85
---
# news_mins_5_pct_dn (news12)

*Number of minutes before the price decreased by at least 5 percent after the news release*

## Signal Profile
- `rank(news_mins_5_pct_dn)`: S=1.13, F=0.47, T=165.4%, INFERIOR (TOP3000)
- `rank(ts_delta(news_mins_5_pct_dn, 5))`: S=0.76, F=0.58, T=44.4%, INFERIOR (TOP200)
- `-rank(news_mins_5_pct_dn)`: S=-0.09, F=-0.01, T=164.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(news_mins_5_pct_dn, 5))`: S=-0.12, F=-0.03, T=154.0%, INFERIOR (TOP3000)
- `ts_zscore(news_mins_5_pct_dn, 22)`: S=0.17, F=0.04, T=159.3%, INFERIOR (TOP3000)
- `ts_mean(news_mins_5_pct_dn, 10)`: S=-0.35, F=-0.12, T=36.7%, INFERIOR (TOP3000)
- `rank(ts_rank(news_mins_5_pct_dn, 22))`: S=0.18, F=0.04, T=163.6%, INFERIOR (TOP3000)
- `rank(-1 * news_mins_5_pct_dn)`: S=-1.13, F=-0.47, T=165.4%, INFERIOR (TOP3000)
- `rank(-1 * news_mins_5_pct_dn / close)`: S=-0.49, F=-0.14, T=161.5%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 19F/1P
- HIGH_TURNOVER: 17F/3P
- LOW_FITNESS: 20F/0P
- LOW_SHARPE: 20F/0P
- LOW_SUB_UNIVERSE_SHARPE: 9F/9P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.75, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=-0.72 (negative), ret=-3.6%
  - 2020: S=0.42 (weak), ret=+18.1%
  - 2021: S=0.05 (weak), ret=+2.0%
  - 2022: S=2.09 (strong), ret=+90.9%
  - 2023: S=1.30 (moderate), ret=+17.9%

## Risk & Drawdown
- Max drawdown: 38.69% over 540 days (recovered)
- Annualized: return +25.6%, volatility 34.0% (fraction of booksize)
- Hit rate: 19.8% positive days
- Tail shape: skew +1.92, excess kurtosis +36.69

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.21, max 2.81, latest 1.55

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2019
Best month: +42.18%; worst month: -15.84%
Positive months: 67%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.48
- Sideways: S=0.72
- Bear: S=1.13

## Negated Direction
Best negated: `-rank(news_mins_5_pct_dn)` S=-0.09, F=-0.01, INFERIOR
Direction gap: -0.85 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * news_mins_5_pct_dn)`: S=-1.13, F=-0.47, T=165.4%, INFERIOR (TOP3000)
- `rank(-1 * news_mins_5_pct_dn / close)`: S=-0.49, F=-0.14, T=161.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(news_mins_5_pct_dn, 5))`: S=-0.12, F=-0.03, T=154.0%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(news_mins_5_pct_dn, 5))` | TOP200 | 0.75 | 0.58 | 38.7% | 80% | mixed |
| `rank(news_mins_5_pct_dn)` | TOP3000 | 1.15 | 0.47 | 45.5% | 80% | weak |
| `rank(ts_delta(news_mins_5_pct_dn, 5))` | TOP1000 | 0.36 | 0.17 | 108.7% | 80% | mixed |
| `rank(news_mins_5_pct_dn)` | TOP500 | 0.37 | 0.11 | 74.0% | 80% | bear-only |
| `rank(ts_delta(news_mins_5_pct_dn, 5))` | TOP3000 | 0.11 | 0.03 | 212.8% | 80% | mixed |
| `rank(ts_delta(news_mins_5_pct_dn, 5))` | TOP500 | 0.11 | 0.03 | 98.7% | 60% | weak |

## Correlation Notes
Top correlates:
- fnd6_prcc: -0.119 (weakly negatively correlated)
- anl4_ebitda_std: -0.119 (weakly negatively correlated)
- fnd6_newqv1300_ciderglq: 0.118 (weakly positively correlated)
- fnd6_prccq: -0.117 (weakly negatively correlated)
- fnd6_prchq: -0.116 (weakly negatively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, rank_value_norm, trade_when
