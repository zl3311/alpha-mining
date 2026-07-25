---
field: news_mov_vol
dataset: news12
best_template: rank_level
best_sharpe: 0.31
best_fitness: 0.09
best_universe: TOP200
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 21
regime_profile: mixed
n_variations_with_pnl: 4
max_drawdown: 0.2347
ann_vol: 0.0955
hit_rate: 0.4972
rolling_sharpe_min: -1.908
rolling_sharpe_max: 1.833
negated_best_sharpe: 0.06
negated_best_template: neg_rank
negated_best_fitness: 0.01
n_negated_sims: 4
direction_gap: -0.25
---
# news_mov_vol (news12)

*30-day moving average of session volume*

## Signal Profile
- `rank(news_mov_vol)`: S=0.31, F=0.09, T=38.9%, INFERIOR (TOP200)
- `rank(news_mov_vol / close)`: S=-0.02, F=0.00, T=60.8%, INFERIOR (TOP3000)
- `rank(ts_delta(news_mov_vol, 5))`: S=0.19, F=0.03, T=76.7%, INFERIOR (TOP500)
- `-rank(news_mov_vol)`: S=0.06, F=0.01, T=60.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(news_mov_vol, 5))`: S=0.00, F=0.00, T=97.2%, INFERIOR (TOP3000)
- `ts_zscore(news_mov_vol, 22)`: S=0.29, F=0.05, T=67.6%, INFERIOR (TOP3000)
- `ts_mean(news_mov_vol, 10)`: S=0.08, F=0.02, T=3.9%, INFERIOR (TOP3000)
- `rank(ts_rank(news_mov_vol, 22))`: S=0.19, F=0.02, T=69.7%, INFERIOR (TOP3000)
- `rank(-1 * news_mov_vol)`: S=-0.18, F=-0.02, T=72.2%, INFERIOR (TOP3000)
- `rank(-1 * news_mov_vol / close)`: S=0.01, F=0.00, T=72.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 20F/1P
- HIGH_TURNOVER: 9F/12P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 21F/0P
- LOW_SUB_UNIVERSE_SHARPE: 9F/10P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.32, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.82 (moderate), ret=+4.8%
  - 2020: S=0.57 (moderate), ret=+6.1%
  - 2021: S=-0.44 (negative), ret=-5.5%
  - 2022: S=-0.04 (negative), ret=-0.4%
  - 2023: S=1.45 (moderate), ret=+10.1%

## Risk & Drawdown
- Max drawdown: 23.47% over 1019 days (not yet recovered, ongoing at window end)
- Annualized: return +3.1%, volatility 9.6% (fraction of booksize)
- Hit rate: 49.7% positive days
- Tail shape: skew +0.33, excess kurtosis +2.29

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.91, max 1.83, latest 1.50

## Yearly & Monthly Returns
Best year (by Sharpe): 2023; worst year: 2021
Best month: +10.46%; worst month: -6.59%
Positive months: 51%

## Regime Profile
Regime profile: **mixed**
- Bull: S=-0.14
- Sideways: S=-0.55
- Bear: S=1.47

## Negated Direction
Best negated: `-rank(news_mov_vol)` S=0.06, F=0.01, INFERIOR
Direction gap: -0.25 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * news_mov_vol)`: S=-0.18, F=-0.02, T=72.2%, INFERIOR (TOP3000)
- `rank(-1 * news_mov_vol / close)`: S=0.01, F=0.00, T=72.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(news_mov_vol, 5))`: S=0.00, F=0.00, T=97.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(news_mov_vol)` | TOP200 | 0.32 | 0.09 | 23.5% | 60% | mixed |
| `rank(ts_delta(news_mov_vol, 5))` | TOP500 | 0.19 | 0.03 | 12.0% | 80% | mixed |
| `rank(news_mov_vol)` | TOP3000 | 0.18 | 0.02 | 25.5% | 60% | bear-only |
| `rank(ts_delta(news_mov_vol, 5))` | TOP200 | 0.14 | 0.02 | 29.8% | 80% | mixed |

## Correlation Notes
Top correlates:
- volume: 0.901 (strongly positively correlated)
- news_curr_vol: 0.877 (strongly positively correlated)
- fnd6_cshtrq: 0.859 (strongly positively correlated)
- anl4_epsa_flag: 0.761 (strongly positively correlated)
- fn_antidilutive_securities_excl_from_eps_a: 0.695 (moderately positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
