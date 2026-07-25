---
field: scl12_buzz
dataset: socialmedia12
cluster: socialmedia12_sentiment
coverage: 1.0
community_alphas: 20785
best_template: decay_linear
best_sharpe: 2.26
best_fitness: 2.95
best_universe: TOP3000
grade: SPECTACULAR
submittability: blocked_LOW_SUB_UNIVERSE_SHARPE
n_sims: 34
regime_profile: mixed
n_variations_with_pnl: 2
max_drawdown: 0.2045
ann_vol: 0.0818
hit_rate: 0.5182
rolling_sharpe_min: -2.125
rolling_sharpe_max: 3.478
redundancy_cluster: 97
negated_best_sharpe: 0.42
negated_best_template: neg_rank_level
negated_best_fitness: 0.07
n_negated_sims: 10
direction_gap: -1.84
---
# scl12_buzz (socialmedia12)

*relative sentiment volume*

## Signal Profile
- `rank(scl12_buzz)`: S=0.56, F=0.16, T=53.5%, INFERIOR (TOP200)
- `rank(ts_delta(scl12_buzz, 5))`: S=0.18, F=0.02, T=72.4%, INFERIOR (TOP1000)
- `ts_decay_linear(rank(scl12_buzz) * zscore(ts_mean(implied_volatility_call_270 - implied_volatility_put_270, 60)), 10)`: S=2.26, F=2.95, T=20.3%, SPECTACULAR (TOP3000)
- `-rank(scl12_buzz)`: S=0.09, F=0.01, T=46.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(scl12_buzz, 5))`: S=0.03, F=0.00, T=90.6%, INFERIOR (TOP3000)
- `ts_zscore(scl12_buzz, 22)`: S=0.10, F=0.01, T=61.6%, INFERIOR (TOP3000)
- `ts_mean(scl12_buzz, 10)`: S=-0.10, F=-0.03, T=17.8%, INFERIOR (TOP3000)
- `rank(ts_rank(scl12_buzz, 22))`: S=0.06, F=0.00, T=67.7%, INFERIOR (TOP3000)
- `rank(-1 * scl12_buzz)`: S=0.42, F=0.07, T=63.1%, INFERIOR (TOP3000)
- `rank(-1 * scl12_buzz / close)`: S=0.23, F=0.06, T=45.6%, INFERIOR (TOP3000)

## Check Summary
- HIGH_TURNOVER: 8F/26P
- LOW_FITNESS: 29F/5P
- LOW_SHARPE: 29F/5P
- LOW_SUB_UNIVERSE_SHARPE: 22F/10P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.56, Consistency 40% positive years (2/5)
Yearly breakdown:
  - 2019: S=-0.15 (negative), ret=-0.9%
  - 2020: S=-1.40 (negative), ret=-10.2%
  - 2021: S=-0.21 (negative), ret=-2.2%
  - 2022: S=2.15 (strong), ret=+21.0%
  - 2023: S=2.75 (strong), ret=+14.8%

## Risk & Drawdown
- Max drawdown: 20.45% over 1257 days (recovered)
- Annualized: return +4.6%, volatility 8.2% (fraction of booksize)
- Hit rate: 51.8% positive days
- Tail shape: skew +0.39, excess kurtosis +6.58

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.12, max 3.48, latest 2.72

## Yearly & Monthly Returns
Best year (by Sharpe): 2023; worst year: 2020
Best month: +7.35%; worst month: -4.33%
Positive months: 52%

## Regime Profile
Regime profile: **mixed**
- Bull: S=1.40
- Sideways: S=-0.13
- Bear: S=0.17

## Negated Direction
Best negated: `rank(-1 * scl12_buzz)` S=0.42, F=0.07, INFERIOR
Direction gap: -1.84 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * scl12_buzz)`: S=0.42, F=0.07, T=63.1%, INFERIOR (TOP3000)
- `rank(-1 * scl12_buzz / close)`: S=0.23, F=0.06, T=45.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(scl12_buzz, 5))`: S=0.03, F=0.00, T=90.6%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(scl12_buzz)` | TOP200 | 0.56 | 0.16 | 20.4% | 40% | mixed |
| `rank(scl12_buzz)` | TOP500 | 0.23 | 0.04 | 14.5% | 80% | mixed |

## Correlation Notes
Top correlates:
- scl12_buzz_fast_d1: 0.755 (strongly positively correlated)
- snt_buzz: -0.644 (moderately negatively correlated)
- snt_buzz_bfl_fast_d1: -0.331 (weakly negatively correlated)
- news_tot_ticks: 0.322 (weakly positively correlated)
- news_session_range: 0.310 (weakly positively correlated)

Redundancy cluster #97: 2 similar fields, mean |rho| 0.755 (representative). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Already in submitted book (alpha: ['vR56vdYd', 'MPbgqZ7o', 'omnopQ9k', 'xAR9Ybjp', 'np30Odjd']).
Blocked by LOW_SUB_UNIVERSE_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: rank_value_norm, trade_when
