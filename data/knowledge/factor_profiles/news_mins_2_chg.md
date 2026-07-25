---
field: news_mins_2_chg
dataset: news12
best_template: ts_zscore
best_sharpe: 0.76
best_fitness: 0.15
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 20
regime_profile: bull-only
n_variations_with_pnl: 2
max_drawdown: 0.1152
ann_vol: 0.0767
hit_rate: 0.5215
rolling_sharpe_min: -0.878
rolling_sharpe_max: 1.544
negated_best_sharpe: 0.24
negated_best_template: rank_neg_delta
negated_best_fitness: 0.03
n_negated_sims: 4
direction_gap: -0.52
---
# news_mins_2_chg (news12)

*Minimum number of minutes taken for price to move (up or down) 2 percentage points after the event*

## Signal Profile
- `rank(news_mins_2_chg)`: S=0.36, F=0.05, T=137.2%, INFERIOR (TOP3000)
- `rank(ts_delta(news_mins_2_chg, 5))`: S=0.28, F=0.05, T=144.6%, INFERIOR (TOP200)
- `-rank(news_mins_2_chg)`: S=-0.07, F=0.00, T=134.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(news_mins_2_chg, 5))`: S=0.24, F=0.03, T=161.3%, INFERIOR (TOP3000)
- `-ts_zscore(news_mins_2_chg, 63)`: S=0.76, F=0.15, T=135.7%, INFERIOR (TOP3000)
- `ts_mean(news_mins_2_chg, 10)`: S=-0.85, F=-0.33, T=26.4%, INFERIOR (TOP3000)
- `rank(ts_rank(news_mins_2_chg, 22))`: S=0.23, F=0.02, T=138.5%, INFERIOR (TOP3000)
- `rank(-1 * news_mins_2_chg)`: S=-0.36, F=-0.05, T=137.2%, INFERIOR (TOP3000)
- `rank(-1 * news_mins_2_chg / close)`: S=-0.06, F=0.00, T=129.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 16F/4P
- HIGH_TURNOVER: 19F/1P
- LOW_FITNESS: 20F/0P
- LOW_SHARPE: 20F/0P
- LOW_SUB_UNIVERSE_SHARPE: 5F/13P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.39, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.12 (negative), ret=-0.9%
  - 2020: S=2.01 (strong), ret=+11.7%
  - 2021: S=0.09 (weak), ret=+0.8%
  - 2022: S=0.78 (moderate), ret=+6.9%
  - 2023: S=-0.65 (negative), ret=-4.0%

## Risk & Drawdown
- Max drawdown: 11.52% over 297 days (recovered)
- Annualized: return +3.0%, volatility 7.7% (fraction of booksize)
- Hit rate: 52.1% positive days
- Tail shape: skew -0.64, excess kurtosis +4.83

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.88, max 1.54, latest -0.79

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2023
Best month: +4.41%; worst month: -8.73%
Positive months: 54%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=1.34
- Sideways: S=0.86
- Bear: S=-1.23

## Negated Direction
Best negated: `rank(-1 * ts_delta(news_mins_2_chg, 5))` S=0.24, F=0.03, INFERIOR
Direction gap: -0.52 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * news_mins_2_chg)`: S=-0.36, F=-0.05, T=137.2%, INFERIOR (TOP3000)
- `rank(-1 * news_mins_2_chg / close)`: S=-0.06, F=0.00, T=129.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(news_mins_2_chg, 5))`: S=0.24, F=0.03, T=161.3%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(news_mins_2_chg)` | TOP3000 | 0.39 | 0.05 | 11.5% | 60% | bull-only |
| `rank(ts_delta(news_mins_2_chg, 5))` | TOP200 | 0.31 | 0.05 | 31.3% | 80% | weak |

## Correlation Notes
Top correlates:
- news_mins_3_chg: 0.764 (strongly positively correlated)
- news_mins_1_pct_dn: 0.746 (strongly positively correlated)
- news_mins_2_pct_dn: 0.640 (moderately positively correlated)
- news_eod_vwap: 0.610 (moderately positively correlated)
- news_eod_low: 0.610 (moderately positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, rank_value_norm, trade_when
