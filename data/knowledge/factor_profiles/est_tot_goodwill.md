---
field: est_tot_goodwill
dataset: analyst4
best_template: ts_zscore
best_sharpe: 0.54
best_fitness: 0.26
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 3
max_drawdown: 0.2173
ann_vol: 0.1288
hit_rate: 0.4955
rolling_sharpe_min: -1.602
rolling_sharpe_max: 2.488
negated_best_sharpe: 0.41
negated_best_template: neg_rank_level
negated_best_fitness: 0.25
n_negated_sims: 10
direction_gap: -0.13
---
# est_tot_goodwill (analyst4)

*Total Goodwill - mean of estimations*

## Signal Profile
- `rank(est_tot_goodwill)`: S=0.16, F=0.05, T=0.7%, INFERIOR (TOP3000)
- `rank(est_tot_goodwill / close)`: S=0.34, F=0.14, T=0.9%, INFERIOR (TOP3000)
- `rank(ts_delta(est_tot_goodwill, 5))`: S=0.48, F=0.21, T=33.4%, INFERIOR (TOP200)
- `-rank(est_tot_goodwill)`: S=0.05, F=0.01, T=1.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(est_tot_goodwill, 5))`: S=0.18, F=0.04, T=34.4%, INFERIOR (TOP3000)
- `-ts_zscore(est_tot_goodwill, 63)`: S=0.54, F=0.26, T=18.9%, INFERIOR (TOP3000)
- `ts_mean(est_tot_goodwill, 10)`: S=-0.32, F=-0.16, T=0.8%, INFERIOR (TOP3000)
- `rank(ts_rank(est_tot_goodwill, 22))`: S=0.44, F=0.17, T=13.7%, INFERIOR (TOP3000)
- `rank(-1 * est_tot_goodwill)`: S=0.41, F=0.25, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * est_tot_goodwill / close)`: S=0.31, F=0.15, T=1.6%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 9F/23P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 18F/11P
- LOW_TURNOVER: 3F/29P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.47, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=-0.06 (negative), ret=-0.6%
  - 2020: S=0.99 (moderate), ret=+11.8%
  - 2021: S=0.54 (moderate), ret=+7.2%
  - 2022: S=0.70 (moderate), ret=+10.4%
  - 2023: S=0.08 (weak), ret=+1.0%

## Risk & Drawdown
- Max drawdown: 21.73% over 424 days (recovered)
- Annualized: return +6.1%, volatility 12.9% (fraction of booksize)
- Hit rate: 49.5% positive days
- Tail shape: skew +0.25, excess kurtosis +3.13

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.60, max 2.49, latest 0.25

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2019
Best month: +11.83%; worst month: -8.36%
Positive months: 54%

## Regime Profile
Regime profile: **mixed**
- Bull: S=1.00
- Sideways: S=-0.00
- Bear: S=0.40

## Negated Direction
Best negated: `rank(-1 * est_tot_goodwill)` S=0.41, F=0.25, INFERIOR
Direction gap: -0.13 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * est_tot_goodwill)`: S=0.41, F=0.25, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * est_tot_goodwill / close)`: S=0.31, F=0.15, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(est_tot_goodwill, 5))`: S=0.18, F=0.04, T=34.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(est_tot_goodwill, 5))` | TOP200 | 0.47 | 0.21 | 21.7% | 80% | mixed |
| `rank(est_tot_goodwill / close)` | TOP3000 | 0.32 | 0.14 | 10.9% | 60% | bull-only |
| `rank(est_tot_goodwill)` | TOP3000 | 0.15 | 0.05 | 29.5% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_sppiv: 0.147 (weakly positively correlated)
- historical_volatility_30: 0.126 (weakly positively correlated)
- fnd2_a_sbcpnargmsptawervl: 0.125 (weakly positively correlated)
- fnd6_cstkcv: -0.123 (weakly negatively correlated)
- earnings_per_share_nongaap_value: -0.121 (weakly negatively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
