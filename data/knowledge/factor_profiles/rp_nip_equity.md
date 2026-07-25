---
field: rp_nip_equity
dataset: news18
best_template: rank_level
best_sharpe: 0.56
best_fitness: 0.12
best_universe: TOP200
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 21
regime_profile: mixed
n_variations_with_pnl: 3
max_drawdown: 0.1285
ann_vol: 0.0832
hit_rate: 0.4947
rolling_sharpe_min: -1.27
rolling_sharpe_max: 1.959
negated_best_sharpe: 0.31
negated_best_template: neg_rank
negated_best_fitness: 0.03
n_negated_sims: 4
direction_gap: -0.25
---
# rp_nip_equity (news18)

*News impact projection of equity action news*

## Signal Profile
- `rank(rp_nip_equity)`: S=0.56, F=0.12, T=105.2%, INFERIOR (TOP200)
- `rank(rp_nip_equity / close)`: S=-0.29, F=-0.04, T=115.1%, INFERIOR (TOP3000)
- `rank(ts_delta(rp_nip_equity, 5))`: S=0.41, F=0.05, T=165.7%, INFERIOR (TOP3000)
- `-rank(rp_nip_equity)`: S=0.31, F=0.03, T=126.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(rp_nip_equity, 5))`: S=-0.41, F=-0.05, T=165.7%, INFERIOR (TOP3000)
- `-ts_zscore(rp_nip_equity, 63)`: S=0.37, F=0.04, T=132.7%, INFERIOR (TOP3000)
- `ts_mean(rp_nip_equity, 10)`: S=0.07, F=0.01, T=17.0%, INFERIOR (TOP3000)
- `rank(ts_rank(rp_nip_equity, 22))`: S=-0.59, F=-0.08, T=135.4%, INFERIOR (TOP3000)
- `rank(-1 * rp_nip_equity)`: S=0.15, F=0.01, T=144.1%, INFERIOR (TOP3000)
- `rank(-1 * rp_nip_equity / close)`: S=0.05, F=0.00, T=136.9%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 2F/19P
- HIGH_TURNOVER: 20F/1P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 21F/0P
- LOW_SUB_UNIVERSE_SHARPE: 11F/8P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.56, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.38 (weak), ret=+3.0%
  - 2020: S=1.75 (strong), ret=+14.8%
  - 2021: S=0.58 (moderate), ret=+5.6%
  - 2022: S=0.03 (weak), ret=+0.2%
  - 2023: S=-0.19 (negative), ret=-1.0%

## Risk & Drawdown
- Max drawdown: 12.85% over 765 days (not yet recovered, ongoing at window end)
- Annualized: return +4.6%, volatility 8.3% (fraction of booksize)
- Hit rate: 49.5% positive days
- Tail shape: skew +0.74, excess kurtosis +7.20

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.27, max 1.96, latest -0.19

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2023
Best month: +9.10%; worst month: -5.10%
Positive months: 56%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.09
- Sideways: S=0.82
- Bear: S=0.87

## Negated Direction
Best negated: `-rank(rp_nip_equity)` S=0.31, F=0.03, INFERIOR
Direction gap: -0.25 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * rp_nip_equity)`: S=0.15, F=0.01, T=144.1%, INFERIOR (TOP3000)
- `rank(-1 * rp_nip_equity / close)`: S=0.05, F=0.00, T=136.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(rp_nip_equity, 5))`: S=-0.41, F=-0.05, T=165.7%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(rp_nip_equity)` | TOP200 | 0.56 | 0.12 | 12.8% | 80% | mixed |
| `rank(ts_delta(rp_nip_equity, 5))` | TOP3000 | 0.42 | 0.05 | 10.6% | 80% | mixed |
| `rank(ts_delta(rp_nip_equity, 5))` | TOP1000 | 0.32 | 0.03 | 7.6% | 60% | all-weather |

## Correlation Notes
Top correlates:
- rp_nip_ptg: 0.602 (moderately positively correlated)
- rp_nip_price: 0.350 (weakly positively correlated)
- rp_nip_insider: 0.323 (weakly positively correlated)
- parkinson_volatility_150: 0.299 (weakly positively correlated)
- parkinson_volatility_180: 0.298 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
