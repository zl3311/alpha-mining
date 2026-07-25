---
field: snt_buzz_bfl
dataset: socialmedia12
best_template: rank_level
best_sharpe: 0.77
best_fitness: 0.19
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 26
regime_profile: bear-only
n_variations_with_pnl: 3
max_drawdown: 0.0415
ann_vol: 0.0355
hit_rate: 0.5093
rolling_sharpe_min: -0.685
rolling_sharpe_max: 2.839
redundancy_cluster: 65
negated_best_sharpe: 0.39
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.16
n_negated_sims: 10
direction_gap: -0.38
---
# snt_buzz_bfl (socialmedia12)

*Negative relative sentiment volume measure for current day, with missing values filled as 1*

## Signal Profile
- `rank(snt_buzz_bfl)`: S=0.77, F=0.19, T=44.5%, INFERIOR (TOP3000)
- `rank(ts_delta(snt_buzz_bfl, 5))`: S=0.28, F=0.05, T=63.6%, INFERIOR (TOP200)
- `-rank(snt_buzz_bfl)`: S=-0.14, F=-0.02, T=41.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(snt_buzz_bfl, 5))`: S=-0.28, F=-0.05, T=63.6%, INFERIOR (TOP3000)
- `-ts_zscore(snt_buzz_bfl, 63)`: S=0.32, F=0.06, T=54.0%, INFERIOR (TOP3000)
- `ts_mean(snt_buzz_bfl, 10)`: S=0.08, F=0.02, T=18.0%, INFERIOR (TOP3000)
- `rank(ts_rank(snt_buzz_bfl, 22))`: S=0.11, F=0.01, T=61.8%, INFERIOR (TOP3000)
- `rank(-1 * snt_buzz_bfl)`: S=0.50, F=0.14, T=52.6%, INFERIOR (TOP3000)
- `rank(-1 * snt_buzz_bfl / close)`: S=0.39, F=0.16, T=25.8%, INFERIOR (TOP3000)

## Check Summary
- HIGH_TURNOVER: 1F/25P
- LOW_FITNESS: 26F/0P
- LOW_SHARPE: 26F/0P
- LOW_SUB_UNIVERSE_SHARPE: 7F/8P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.76, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.86 (moderate), ret=+2.2%
  - 2020: S=2.35 (strong), ret=+8.1%
  - 2021: S=0.33 (weak), ret=+1.5%
  - 2022: S=-0.41 (negative), ret=-1.4%
  - 2023: S=0.90 (moderate), ret=+2.8%

## Risk & Drawdown
- Max drawdown: 4.15% over 80 days (recovered)
- Annualized: return +2.7%, volatility 3.5% (fraction of booksize)
- Hit rate: 50.9% positive days
- Tail shape: skew +0.10, excess kurtosis +1.20

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.69, max 2.84, latest 1.08

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2022
Best month: +3.44%; worst month: -2.61%
Positive months: 61%

## Regime Profile
Regime profile: **bear-only**
- Bull: S=-0.51
- Sideways: S=1.59
- Bear: S=1.25

## Negated Direction
Best negated: `rank(-1 * snt_buzz_bfl / close)` S=0.39, F=0.16, INFERIOR
Direction gap: -0.38 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * snt_buzz_bfl)`: S=0.50, F=0.14, T=52.6%, INFERIOR (TOP3000)
- `rank(-1 * snt_buzz_bfl / close)`: S=0.39, F=0.16, T=25.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(snt_buzz_bfl, 5))`: S=-0.28, F=-0.05, T=63.6%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(snt_buzz_bfl)` | TOP3000 | 0.76 | 0.19 | 4.2% | 80% | bear-only |
| `rank(ts_delta(snt_buzz_bfl, 5))` | TOP200 | 0.31 | 0.05 | 22.1% | 60% | mixed |
| `rank(ts_delta(snt_buzz_bfl, 5))` | TOP3000 | 0.25 | 0.03 | 3.7% | 80% | bull-only |

## Correlation Notes
Top correlates:
- snt_buzz_ret: 0.771 (strongly positively correlated)
- pcr_vol_1080: -0.529 (moderately negatively correlated)
- snt_buzz_bfl_fast_d1: 0.520 (moderately positively correlated)
- pcr_vol_270: -0.487 (moderately negatively correlated)
- pcr_vol_180: -0.450 (moderately negatively correlated)

Redundancy cluster #65: 2 similar fields, mean |rho| 0.771 (representative). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, rank_value_norm, trade_when
