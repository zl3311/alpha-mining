---
field: pcr_vol_1080
dataset: option9
best_template: rank_level
best_sharpe: 0.65
best_fitness: 0.13
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 21
regime_profile: weak
n_variations_with_pnl: 2
max_drawdown: 0.044
ann_vol: 0.0399
hit_rate: 0.5198
rolling_sharpe_min: -0.604
rolling_sharpe_max: 2.407
redundancy_cluster: 79
negated_best_sharpe: -0.1
negated_best_template: neg_rank
negated_best_fitness: -0.01
n_negated_sims: 4
direction_gap: -0.75
---
# pcr_vol_1080 (option9)

*Ratio of put volume to call volume on a stock's options with expiration 1080 days in the future.*

## Signal Profile
- `rank(pcr_vol_1080)`: S=0.65, F=0.13, T=61.1%, INFERIOR (TOP3000)
- `rank(pcr_vol_1080 / close)`: S=0.04, F=0.00, T=52.1%, INFERIOR (TOP3000)
- `rank(ts_delta(pcr_vol_1080, 5))`: S=0.68, F=0.09, T=86.3%, INFERIOR (TOP3000)
- `-rank(pcr_vol_1080)`: S=-0.10, F=-0.01, T=52.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(pcr_vol_1080, 5))`: S=-0.68, F=-0.09, T=86.3%, INFERIOR (TOP3000)
- `-ts_zscore(pcr_vol_1080, 63)`: S=0.42, F=0.07, T=56.6%, INFERIOR (TOP3000)
- `ts_mean(pcr_vol_1080, 10)`: S=0.21, F=0.06, T=18.8%, INFERIOR (TOP3000)
- `rank(ts_rank(pcr_vol_1080, 22))`: S=-0.38, F=-0.05, T=66.1%, INFERIOR (TOP3000)
- `rank(-1 * pcr_vol_1080)`: S=-0.65, F=-0.13, T=61.1%, INFERIOR (TOP3000)
- `rank(-1 * pcr_vol_1080 / close)`: S=-0.59, F=-0.13, T=63.0%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 21F/0P
- HIGH_TURNOVER: 7F/14P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 21F/0P
- LOW_SUB_UNIVERSE_SHARPE: 7F/12P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.65, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.13 (weak), ret=+0.4%
  - 2020: S=0.65 (moderate), ret=+2.9%
  - 2021: S=0.60 (moderate), ret=+2.9%
  - 2022: S=-0.03 (negative), ret=-0.1%
  - 2023: S=1.83 (strong), ret=+6.7%

## Risk & Drawdown
- Max drawdown: 4.40% over 301 days (recovered)
- Annualized: return +2.6%, volatility 4.0% (fraction of booksize)
- Hit rate: 52.0% positive days
- Tail shape: skew +0.05, excess kurtosis +1.34

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.60, max 2.41, latest 1.64

## Yearly & Monthly Returns
Best year (by Sharpe): 2023; worst year: 2022
Best month: +3.78%; worst month: -1.98%
Positive months: 54%

## Regime Profile
Regime profile: **weak**
- Bull: S=0.49
- Sideways: S=1.05
- Bear: S=0.46

## Negated Direction
Best negated: `-rank(pcr_vol_1080)` S=-0.10, F=-0.01, INFERIOR
Direction gap: -0.75 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * pcr_vol_1080)`: S=-0.65, F=-0.13, T=61.1%, INFERIOR (TOP3000)
- `rank(-1 * pcr_vol_1080 / close)`: S=-0.59, F=-0.13, T=63.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(pcr_vol_1080, 5))`: S=-0.68, F=-0.09, T=86.3%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(pcr_vol_1080)` | TOP3000 | 0.65 | 0.13 | 4.4% | 80% | weak |
| `rank(ts_delta(pcr_vol_1080, 5))` | TOP3000 | 0.68 | 0.09 | 4.2% | 60% | mixed |

## Correlation Notes
Top correlates:
- pcr_vol_270: 0.914 (strongly positively correlated)
- pcr_vol_180: 0.893 (strongly positively correlated)
- pcr_vol_150: 0.877 (strongly positively correlated)
- snt_buzz_bfl: -0.529 (moderately negatively correlated)
- fnd6_newa1v1300_bkvlps: -0.524 (moderately negatively correlated)

Redundancy cluster #79: 2 similar fields, mean |rho| 0.893 (representative). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
