---
field: fnd6_cik
dataset: fundamental6
best_template: ts_zscore
best_sharpe: 1.31
best_fitness: 1.97
best_universe: TOP3000
grade: GOOD
submittability: blocked_LOW_TURNOVER
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 6
max_drawdown: 0.5909
ann_vol: 0.2456
hit_rate: 0.4777
rolling_sharpe_min: -2.198
rolling_sharpe_max: 2.565
negated_best_sharpe: 0.72
negated_best_template: neg_rank_level
negated_best_fitness: 0.52
n_negated_sims: 10
direction_gap: -0.59
---
# fnd6_cik (fundamental6)

*nonimportant technical code*

## Signal Profile
- `rank(fnd6_cik)`: S=0.11, F=0.04, T=1.8%, INFERIOR (TOP200)
- `rank(fnd6_cik / close)`: S=0.14, F=0.05, T=2.3%, INFERIOR (TOP200)
- `rank(ts_delta(fnd6_cik, 5))`: S=0.46, F=0.43, T=12.8%, INFERIOR (TOP3000)
- `-rank(fnd6_cik)`: S=0.16, F=0.06, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_cik, 5))`: S=0.07, F=0.03, T=12.9%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_cik, 63)`: S=1.31, F=1.97, T=0.7%, GOOD (TOP3000)
- `ts_mean(fnd6_cik, 10)`: S=-0.20, F=-0.08, T=1.4%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_cik, 22))`: S=0.57, F=0.63, T=6.6%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_cik)`: S=0.72, F=0.52, T=0.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_cik / close)`: S=0.20, F=0.09, T=1.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 30F/1P
- LOW_SHARPE: 31F/1P
- LOW_SUB_UNIVERSE_SHARPE: 13F/14P
- LOW_TURNOVER: 6F/26P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.45, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=-2.14 (negative), ret=-25.0%
  - 2020: S=0.64 (moderate), ret=+14.0%
  - 2021: S=1.28 (moderate), ret=+55.4%
  - 2022: S=0.42 (weak), ret=+7.6%
  - 2023: S=0.25 (weak), ret=+2.4%

## Risk & Drawdown
- Max drawdown: 59.09% over 184 days (recovered)
- Annualized: return +11.1%, volatility 24.6% (fraction of booksize)
- Hit rate: 47.8% positive days
- Tail shape: skew +4.01, excess kurtosis +59.16

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.20, max 2.56, latest 0.09

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2019
Best month: +71.15%; worst month: -32.26%
Positive months: 58%

## Regime Profile
Regime profile: **mixed**
- Bull: S=1.08
- Sideways: S=0.42
- Bear: S=-0.12

## Negated Direction
Best negated: `rank(-1 * fnd6_cik)` S=0.72, F=0.52, INFERIOR
Direction gap: -0.59 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_cik)`: S=0.72, F=0.52, T=0.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_cik / close)`: S=0.20, F=0.09, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_cik, 5))`: S=0.07, F=0.03, T=12.9%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_cik, 5))` | TOP3000 | 0.45 | 0.43 | 59.1% | 80% | mixed |
| `rank(ts_delta(fnd6_cik, 5))` | TOP500 | 0.45 | 0.35 | 29.2% | 80% | bull-only |
| `rank(fnd6_cik / close)` | TOP200 | 0.14 | 0.05 | 42.2% | 60% | bear-only |
| `rank(ts_delta(fnd6_cik, 5))` | TOP200 | 0.12 | 0.05 | 28.1% | 80% | bull-only |
| `rank(fnd6_cik)` | TOP200 | 0.12 | 0.04 | 48.2% | 40% | bear-only |
| `rank(fnd6_cik / close)` | TOP1000 | 0.09 | 0.02 | 41.8% | 40% | bear-only |

## Correlation Notes
Top correlates:
- fnd6_city: 0.269 (weakly positively correlated)
- fnd6_dn: 0.215 (weakly positively correlated)
- implied_volatility_mean_skew_270: 0.213 (weakly positively correlated)
- implied_volatility_mean_skew_60: 0.211 (weakly positively correlated)
- anl4_cfo_value: 0.209 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_TURNOVER. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
