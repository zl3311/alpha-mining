---
field: systematic_risk_last_90_days
dataset: model51
cluster: model51_other
coverage: 0.9619
community_alphas: 1949
best_template: ts_mean
best_sharpe: 0.24
best_fitness: 0.16
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 21
regime_profile: bear-only
n_variations_with_pnl: 6
max_drawdown: 0.3494
ann_vol: 0.1664
hit_rate: 0.4899
rolling_sharpe_min: -1.152
rolling_sharpe_max: 2.773
negated_best_sharpe: -0.07
negated_best_template: neg_rank_value_norm
negated_best_fitness: -0.02
n_negated_sims: 4
direction_gap: -0.31
---
# systematic_risk_last_90_days (model51)

*The portion of the security’s return variance attributed to systematic (market) risk, quantified as R² from a regression on SPY, over the last 90 calendar days*

## Signal Profile
- `rank(systematic_risk_last_90_days)`: S=0.28, F=0.14, T=17.8%, INFERIOR (TOP3000)
- `rank(systematic_risk_last_90_days / close)`: S=0.05, F=0.01, T=12.5%, INFERIOR (TOP3000)
- `rank(ts_delta(systematic_risk_last_90_days, 5))`: S=0.34, F=0.07, T=53.9%, INFERIOR (TOP3000)
- `-rank(systematic_risk_last_90_days)`: S=-0.13, F=-0.05, T=15.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(systematic_risk_last_90_days, 5))`: S=-0.34, F=-0.07, T=53.9%, INFERIOR (TOP3000)
- `-ts_zscore(systematic_risk_last_90_days, 63)`: S=0.20, F=0.05, T=22.7%, INFERIOR (TOP3000)
- `ts_mean(systematic_risk_last_90_days, 10)`: S=0.24, F=0.16, T=5.1%, INFERIOR (TOP3000)
- `rank(ts_rank(systematic_risk_last_90_days, 22))`: S=-0.39, F=-0.11, T=34.1%, INFERIOR (TOP3000)
- `rank(-1 * systematic_risk_last_90_days)`: S=-0.28, F=-0.14, T=17.8%, INFERIOR (TOP3000)
- `rank(-1 * systematic_risk_last_90_days / close)`: S=-0.07, F=-0.02, T=14.9%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 21F/0P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 21F/0P
- LOW_SUB_UNIVERSE_SHARPE: 8F/11P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.29, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.51 (moderate), ret=+4.4%
  - 2020: S=2.21 (strong), ret=+33.0%
  - 2021: S=0.25 (weak), ret=+3.4%
  - 2022: S=-0.84 (negative), ret=-21.7%
  - 2023: S=0.33 (weak), ret=+4.4%

## Risk & Drawdown
- Max drawdown: 34.94% over 781 days (not yet recovered, ongoing at window end)
- Annualized: return +4.8%, volatility 16.6% (fraction of booksize)
- Hit rate: 49.0% positive days
- Tail shape: skew +0.32, excess kurtosis +2.22

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.15, max 2.77, latest 0.53

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2022
Best month: +10.37%; worst month: -12.11%
Positive months: 54%

## Regime Profile
Regime profile: **bear-only**
- Bull: S=-1.26
- Sideways: S=-0.14
- Bear: S=2.54

## Negated Direction
Best negated: `rank(-1 * systematic_risk_last_90_days / close)` S=-0.07, F=-0.02, INFERIOR
Direction gap: -0.31 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * systematic_risk_last_90_days)`: S=-0.28, F=-0.14, T=17.8%, INFERIOR (TOP3000)
- `rank(-1 * systematic_risk_last_90_days / close)`: S=-0.07, F=-0.02, T=14.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(systematic_risk_last_90_days, 5))`: S=-0.34, F=-0.07, T=53.9%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(systematic_risk_last_90_days)` | TOP3000 | 0.29 | 0.14 | 34.9% | 80% | bear-only |
| `rank(ts_delta(systematic_risk_last_90_days, 5))` | TOP3000 | 0.34 | 0.07 | 15.5% | 40% | mixed |
| `rank(systematic_risk_last_90_days)` | TOP500 | 0.16 | 0.06 | 42.5% | 60% | bear-only |
| `rank(systematic_risk_last_90_days)` | TOP1000 | 0.14 | 0.05 | 42.0% | 60% | bear-only |
| `rank(ts_delta(systematic_risk_last_90_days, 5))` | TOP1000 | 0.20 | 0.04 | 16.7% | 60% | weak |
| `rank(ts_delta(systematic_risk_last_90_days, 5))` | TOP500 | 0.18 | 0.03 | 15.7% | 60% | mixed |

## Correlation Notes
Top correlates:
- beta_last_90_days_spy: 0.983 (strongly positively correlated)
- fnd6_mfmq_ibcomq: -0.863 (strongly negatively correlated)
- fnd6_newqv1300_cibegniq: -0.862 (strongly negatively correlated)
- income: -0.862 (strongly negatively correlated)
- fnd6_newqv1300_dilavq: -0.844 (strongly negatively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
