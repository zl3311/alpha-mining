---
field: pcr_oi_1080
dataset: option9
best_template: rank_level
best_sharpe: 0.61
best_fitness: 0.26
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 21
regime_profile: bull-only
n_variations_with_pnl: 1
max_drawdown: 0.1079
ann_vol: 0.0382
hit_rate: 0.5198
rolling_sharpe_min: -2.698
rolling_sharpe_max: 2.889
redundancy_cluster: 82
negated_best_sharpe: 0.16
negated_best_template: neg_rank
negated_best_fitness: 0.04
n_negated_sims: 4
direction_gap: -0.45
---
# pcr_oi_1080 (option9)

*Ratio of put option open interest to call option open interest for stock options expiring in 1080 days, representing longer-term positioning*

## Signal Profile
- `rank(pcr_oi_1080)`: S=0.61, F=0.26, T=8.2%, INFERIOR (TOP3000)
- `rank(pcr_oi_1080 / close)`: S=-0.02, F=0.00, T=7.8%, INFERIOR (TOP3000)
- `rank(ts_delta(pcr_oi_1080, 5))`: S=-0.21, F=-0.02, T=33.8%, INFERIOR (TOP3000)
- `-rank(pcr_oi_1080)`: S=0.16, F=0.04, T=8.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(pcr_oi_1080, 5))`: S=0.21, F=0.02, T=33.8%, INFERIOR (TOP3000)
- `-ts_zscore(pcr_oi_1080, 63)`: S=0.45, F=0.14, T=14.9%, INFERIOR (TOP3000)
- `ts_mean(pcr_oi_1080, 10)`: S=0.04, F=0.01, T=8.2%, INFERIOR (TOP3000)
- `rank(ts_rank(pcr_oi_1080, 22))`: S=-0.83, F=-0.29, T=21.2%, INFERIOR (TOP3000)
- `rank(-1 * pcr_oi_1080)`: S=-0.61, F=-0.26, T=8.2%, INFERIOR (TOP3000)
- `rank(-1 * pcr_oi_1080 / close)`: S=-0.21, F=-0.07, T=8.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 21F/0P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 21F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/6P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.61, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=2.77 (strong), ret=+5.8%
  - 2020: S=-2.01 (negative), ret=-5.8%
  - 2021: S=0.72 (moderate), ret=+2.9%
  - 2022: S=1.58 (strong), ret=+8.3%
  - 2023: S=0.05 (weak), ret=+0.2%

## Risk & Drawdown
- Max drawdown: 10.79% over 744 days (recovered)
- Annualized: return +2.3%, volatility 3.8% (fraction of booksize)
- Hit rate: 52.0% positive days
- Tail shape: skew +0.03, excess kurtosis +1.07

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.70, max 2.89, latest -0.17

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2020
Best month: +3.02%; worst month: -2.27%
Positive months: 54%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.11
- Sideways: S=1.49
- Bear: S=-1.94

## Negated Direction
Best negated: `-rank(pcr_oi_1080)` S=0.16, F=0.04, INFERIOR
Direction gap: -0.45 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * pcr_oi_1080)`: S=-0.61, F=-0.26, T=8.2%, INFERIOR (TOP3000)
- `rank(-1 * pcr_oi_1080 / close)`: S=-0.21, F=-0.07, T=8.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(pcr_oi_1080, 5))`: S=0.21, F=0.02, T=33.8%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(pcr_oi_1080)` | TOP3000 | 0.61 | 0.26 | 10.8% | 80% | bull-only |

## Correlation Notes
Top correlates:
- pcr_oi_720: 0.995 (strongly positively correlated)
- pcr_oi_360: 0.948 (strongly positively correlated)
- pcr_oi_270: 0.906 (strongly positively correlated)
- pcr_oi_all: 0.862 (strongly positively correlated)
- anl4_qfv4_eps_high: 0.805 (strongly positively correlated)

Redundancy cluster #82: 3 similar fields, mean |rho| 0.844 (representative: pcr_oi_10). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
