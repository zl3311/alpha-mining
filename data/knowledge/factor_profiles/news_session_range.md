---
field: news_session_range
dataset: news12
best_template: rank_delta
best_sharpe: 0.76
best_fitness: 0.2
best_universe: TOP200
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 21
regime_profile: mixed
n_variations_with_pnl: 3
max_drawdown: 0.1589
ann_vol: 0.0917
hit_rate: 0.5158
rolling_sharpe_min: -1.396
rolling_sharpe_max: 2.838
redundancy_cluster: 62
negated_best_sharpe: 0.43
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.1
n_negated_sims: 4
direction_gap: -0.33
---
# news_session_range (news12)

*Difference between session high and session low price*

## Signal Profile
- `rank(news_session_range)`: S=0.05, F=0.00, T=65.8%, INFERIOR (TOP500)
- `rank(news_session_range / close)`: S=-0.08, F=-0.01, T=92.7%, INFERIOR (TOP3000)
- `rank(ts_delta(news_session_range, 5))`: S=0.76, F=0.20, T=102.0%, INFERIOR (TOP200)
- `-rank(news_session_range)`: S=0.09, F=0.01, T=77.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(news_session_range, 5))`: S=0.19, F=0.02, T=133.8%, INFERIOR (TOP3000)
- `ts_zscore(news_session_range, 22)`: S=-0.06, F=0.00, T=102.8%, INFERIOR (TOP3000)
- `ts_mean(news_session_range, 10)`: S=-0.23, F=-0.10, T=9.5%, INFERIOR (TOP3000)
- `rank(ts_rank(news_session_range, 22))`: S=-0.04, F=0.00, T=106.4%, INFERIOR (TOP3000)
- `rank(-1 * news_session_range)`: S=0.25, F=0.04, T=92.5%, INFERIOR (TOP3000)
- `rank(-1 * news_session_range / close)`: S=0.43, F=0.10, T=106.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 1F/20P
- HIGH_TURNOVER: 18F/3P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 21F/0P
- LOW_SUB_UNIVERSE_SHARPE: 7F/12P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.77, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.59 (moderate), ret=+4.0%
  - 2020: S=-0.26 (negative), ret=-2.6%
  - 2021: S=0.11 (weak), ret=+1.2%
  - 2022: S=2.22 (strong), ret=+23.6%
  - 2023: S=1.45 (moderate), ret=+8.4%

## Risk & Drawdown
- Max drawdown: 15.89% over 615 days (recovered)
- Annualized: return +7.1%, volatility 9.2% (fraction of booksize)
- Hit rate: 51.6% positive days
- Tail shape: skew +0.39, excess kurtosis +3.51

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.40, max 2.84, latest 1.44

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +8.34%; worst month: -5.00%
Positive months: 64%

## Regime Profile
Regime profile: **mixed**
- Bull: S=1.93
- Sideways: S=0.66
- Bear: S=-0.45

## Negated Direction
Best negated: `rank(-1 * news_session_range / close)` S=0.43, F=0.10, INFERIOR
Direction gap: -0.33 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * news_session_range)`: S=0.25, F=0.04, T=92.5%, INFERIOR (TOP3000)
- `rank(-1 * news_session_range / close)`: S=0.43, F=0.10, T=106.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(news_session_range, 5))`: S=0.19, F=0.02, T=133.8%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(news_session_range, 5))` | TOP200 | 0.77 | 0.20 | 15.9% | 80% | mixed |
| `rank(ts_delta(news_session_range, 5))` | TOP500 | 0.60 | 0.11 | 18.9% | 60% | bull-only |
| `rank(ts_delta(news_session_range, 5))` | TOP1000 | 0.27 | 0.03 | 15.2% | 40% | bull-only |

## Correlation Notes
Top correlates:
- news_atr_ratio: 0.829 (strongly positively correlated)
- news_range_stddev: 0.820 (strongly positively correlated)
- news_vol_stddev: 0.476 (moderately positively correlated)
- news_max_dn_amt: 0.428 (moderately positively correlated)
- news_tot_ticks: 0.424 (moderately positively correlated)

Redundancy cluster #62: 3 similar fields, mean |rho| 0.864 (representative). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
