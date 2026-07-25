---
field: systematic_risk_last_60_days
dataset: model51
best_template: rank_delta
best_sharpe: 0.87
best_fitness: 0.4
best_universe: TOP200
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 21
regime_profile: all-weather
n_variations_with_pnl: 4
max_drawdown: 0.2009
ann_vol: 0.113
hit_rate: 0.5117
rolling_sharpe_min: -0.974
rolling_sharpe_max: 3.006
top_merge_partner: net_debt_amount
negated_best_sharpe: 0.02
negated_best_template: neg_rank
negated_best_fitness: 0.0
n_negated_sims: 4
direction_gap: -0.85
---
# systematic_risk_last_60_days (model51)

*The portion of the security’s return variance attributed to systematic (market) risk, quantified as R² from a regression on SPY, over the last 60 calendar days*

## Signal Profile
- `rank(systematic_risk_last_60_days)`: S=0.11, F=0.03, T=19.5%, INFERIOR (TOP3000)
- `rank(systematic_risk_last_60_days / close)`: S=-0.02, F=0.00, T=13.4%, INFERIOR (TOP3000)
- `rank(ts_delta(systematic_risk_last_60_days, 5))`: S=0.87, F=0.40, T=47.4%, INFERIOR (TOP200)
- `-rank(systematic_risk_last_60_days)`: S=0.02, F=0.00, T=17.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(systematic_risk_last_60_days, 5))`: S=-0.50, F=-0.12, T=52.8%, INFERIOR (TOP3000)
- `-ts_zscore(systematic_risk_last_60_days, 63)`: S=0.31, F=0.10, T=23.1%, INFERIOR (TOP3000)
- `ts_mean(systematic_risk_last_60_days, 10)`: S=0.10, F=0.04, T=6.4%, INFERIOR (TOP3000)
- `rank(ts_rank(systematic_risk_last_60_days, 22))`: S=-0.56, F=-0.18, T=33.8%, INFERIOR (TOP3000)
- `rank(-1 * systematic_risk_last_60_days)`: S=-0.11, F=-0.03, T=19.5%, INFERIOR (TOP3000)
- `rank(-1 * systematic_risk_last_60_days / close)`: S=-0.01, F=0.00, T=15.7%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 21F/0P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 21F/0P
- LOW_SUB_UNIVERSE_SHARPE: 7F/12P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.87, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=1.39 (moderate), ret=+8.0%
  - 2020: S=1.52 (strong), ret=+16.5%
  - 2021: S=-0.13 (negative), ret=-1.8%
  - 2022: S=1.28 (moderate), ret=+19.4%
  - 2023: S=0.85 (moderate), ret=+6.2%

## Risk & Drawdown
- Max drawdown: 20.09% over 372 days (recovered)
- Annualized: return +9.9%, volatility 11.3% (fraction of booksize)
- Hit rate: 51.2% positive days
- Tail shape: skew +0.98, excess kurtosis +7.26

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.97, max 3.01, latest 0.87

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2021
Best month: +9.71%; worst month: -5.53%
Positive months: 58%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=0.94
- Sideways: S=0.23
- Bear: S=1.38

## Negated Direction
Best negated: `-rank(systematic_risk_last_60_days)` S=0.02, F=0.00, INFERIOR
Direction gap: -0.85 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * systematic_risk_last_60_days)`: S=-0.11, F=-0.03, T=19.5%, INFERIOR (TOP3000)
- `rank(-1 * systematic_risk_last_60_days / close)`: S=-0.01, F=0.00, T=15.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(systematic_risk_last_60_days, 5))`: S=-0.50, F=-0.12, T=52.8%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(systematic_risk_last_60_days, 5))` | TOP200 | 0.87 | 0.40 | 20.1% | 80% | all-weather |
| `rank(ts_delta(systematic_risk_last_60_days, 5))` | TOP3000 | 0.51 | 0.12 | 12.0% | 60% | mixed |
| `rank(ts_delta(systematic_risk_last_60_days, 5))` | TOP500 | 0.21 | 0.04 | 14.8% | 80% | mixed |
| `rank(systematic_risk_last_60_days)` | TOP3000 | 0.12 | 0.03 | 39.7% | 60% | bear-only |

## Correlation Notes
Top correlates:
- correlation_last_60_days_spy: 0.740 (strongly positively correlated)
- beta_last_60_days_spy: 0.622 (moderately positively correlated)
- systematic_risk_last_30_days: 0.497 (moderately positively correlated)
- systematic_risk_last_360_days: 0.464 (moderately positively correlated)
- beta_last_360_days_spy: 0.339 (weakly positively correlated)

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| net_debt_amount | analyst4 | -0.20 | 1.37 | +0.47 | -0.82 | yes |
| fnd6_txs | fundamental6 | -0.21 | 1.35 | +0.47 | -0.75 | yes |
| fnd6_dn | fundamental6 | -0.25 | 1.39 | +0.50 | -0.41 | yes |
| anl4_fcf_mean | analyst4 | -0.22 | 1.40 | +0.49 | -0.58 | yes |
| anl4_fcf_median | analyst4 | -0.22 | 1.40 | +0.48 | -0.59 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
