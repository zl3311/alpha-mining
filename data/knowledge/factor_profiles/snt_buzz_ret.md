---
field: snt_buzz_ret
dataset: socialmedia12
best_template: ts_mean
best_sharpe: 0.73
best_fitness: 0.59
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 26
regime_profile: bear-only
n_variations_with_pnl: 3
max_drawdown: 0.0716
ann_vol: 0.0343
hit_rate: 0.5166
rolling_sharpe_min: -2.009
rolling_sharpe_max: 2.718
redundancy_cluster: 65
negated_best_sharpe: 1.05
negated_best_template: rank_neg_delta
negated_best_fitness: 0.26
n_negated_sims: 10
direction_gap: 0.32
---
# snt_buzz_ret (socialmedia12)

*negative return of relative sentiment volume*

## Signal Profile
- `rank(snt_buzz_ret)`: S=0.68, F=0.17, T=37.9%, INFERIOR (TOP3000)
- `rank(ts_delta(snt_buzz_ret, 5))`: S=0.00, F=0.00, T=51.7%, INFERIOR (TOP200)
- `-rank(snt_buzz_ret)`: S=0.01, F=0.00, T=43.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(snt_buzz_ret, 5))`: S=1.05, F=0.26, T=58.8%, INFERIOR (TOP3000)
- `ts_zscore(snt_buzz_ret, 22)`: S=0.43, F=0.08, T=52.0%, INFERIOR (TOP3000)
- `ts_mean(snt_buzz_ret, 10)`: S=0.73, F=0.59, T=20.6%, INFERIOR (TOP3000)
- `rank(ts_rank(snt_buzz_ret, 22))`: S=-0.23, F=-0.03, T=48.9%, INFERIOR (TOP3000)
- `rank(-1 * snt_buzz_ret)`: S=0.01, F=0.00, T=43.9%, INFERIOR (TOP3000)
- `rank(-1 * snt_buzz_ret / close)`: S=0.22, F=0.03, T=42.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 1F/25P
- LOW_FITNESS: 26F/0P
- LOW_SHARPE: 26F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/10P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.68, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.69 (moderate), ret=+1.8%
  - 2020: S=2.69 (strong), ret=+10.0%
  - 2021: S=1.27 (moderate), ret=+5.0%
  - 2022: S=-1.76 (negative), ret=-5.8%
  - 2023: S=0.10 (weak), ret=+0.3%

## Risk & Drawdown
- Max drawdown: 7.16% over 724 days (not yet recovered, ongoing at window end)
- Annualized: return +2.3%, volatility 3.4% (fraction of booksize)
- Hit rate: 51.7% positive days
- Tail shape: skew +0.39, excess kurtosis +2.08

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.01, max 2.72, latest 0.15

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2022
Best month: +2.74%; worst month: -2.04%
Positive months: 52%

## Regime Profile
Regime profile: **bear-only**
- Bull: S=-0.86
- Sideways: S=1.02
- Bear: S=1.79

## Negated Direction
Best negated: `rank(-1 * ts_delta(snt_buzz_ret, 5))` S=1.05, F=0.26, INFERIOR
Direction gap: +0.32 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * snt_buzz_ret)`: S=0.01, F=0.00, T=43.9%, INFERIOR (TOP3000)
- `rank(-1 * snt_buzz_ret / close)`: S=0.22, F=0.03, T=42.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(snt_buzz_ret, 5))`: S=1.05, F=0.26, T=58.8%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(snt_buzz_ret)` | TOP3000 | 0.68 | 0.17 | 7.2% | 80% | bear-only |
| `rank(snt_buzz_ret)` | TOP200 | 0.21 | 0.04 | 20.4% | 80% | mixed |
| `rank(snt_buzz_ret)` | TOP500 | 0.14 | 0.02 | 10.5% | 40% | mixed |

## Correlation Notes
Top correlates:
- snt_buzz_bfl: 0.771 (strongly positively correlated)
- pcr_vol_1080: -0.456 (moderately negatively correlated)
- pcr_vol_270: -0.418 (moderately negatively correlated)
- snt_value: 0.407 (moderately positively correlated)
- pcr_vol_180: -0.372 (weakly negatively correlated)

Redundancy cluster #65: 2 similar fields, mean |rho| 0.771 (representative: snt_buzz_bfl). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, rank_value_norm, trade_when
