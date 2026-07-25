---
field: systematic_risk_last_360_days
dataset: model51
best_template: rank_delta
best_sharpe: 1.01
best_fitness: 0.47
best_universe: TOP200
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 21
regime_profile: all-weather
n_variations_with_pnl: 8
max_drawdown: 0.1387
ann_vol: 0.1063
hit_rate: 0.5117
rolling_sharpe_min: -0.997
rolling_sharpe_max: 2.505
top_merge_partner: anl4_fcf_high
negated_best_sharpe: -0.14
negated_best_template: neg_rank_value_norm
negated_best_fitness: -0.05
n_negated_sims: 4
direction_gap: -1.15
---
# systematic_risk_last_360_days (model51)

*The portion of the security’s return variance attributed to systematic (market) risk, quantified as R² from a regression on SPY, over the last 360 calendar days*

## Signal Profile
- `rank(systematic_risk_last_360_days)`: S=0.37, F=0.23, T=16.4%, INFERIOR (TOP3000)
- `rank(systematic_risk_last_360_days / close)`: S=0.08, F=0.02, T=11.5%, INFERIOR (TOP3000)
- `rank(ts_delta(systematic_risk_last_360_days, 5))`: S=1.01, F=0.47, T=50.9%, INFERIOR (TOP200)
- `-rank(systematic_risk_last_360_days)`: S=-0.17, F=-0.08, T=13.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(systematic_risk_last_360_days, 5))`: S=-0.92, F=-0.26, T=61.5%, INFERIOR (TOP3000)
- `ts_zscore(systematic_risk_last_360_days, 22)`: S=0.18, F=0.03, T=34.6%, INFERIOR (TOP3000)
- `ts_mean(systematic_risk_last_360_days, 10)`: S=0.30, F=0.22, T=3.3%, INFERIOR (TOP3000)
- `rank(ts_rank(systematic_risk_last_360_days, 22))`: S=0.03, F=0.00, T=37.7%, INFERIOR (TOP3000)
- `rank(-1 * systematic_risk_last_360_days)`: S=-0.37, F=-0.23, T=16.4%, INFERIOR (TOP3000)
- `rank(-1 * systematic_risk_last_360_days / close)`: S=-0.14, F=-0.05, T=14.0%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 21F/0P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 21F/0P
- LOW_SUB_UNIVERSE_SHARPE: 6F/13P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 1.01, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=1.19 (moderate), ret=+5.9%
  - 2020: S=1.82 (strong), ret=+14.7%
  - 2021: S=1.68 (strong), ret=+18.6%
  - 2022: S=1.01 (moderate), ret=+16.5%
  - 2023: S=-0.37 (negative), ret=-3.1%

## Risk & Drawdown
- Max drawdown: 13.87% over 83 days (recovered)
- Annualized: return +10.8%, volatility 10.6% (fraction of booksize)
- Hit rate: 51.2% positive days
- Tail shape: skew +1.37, excess kurtosis +14.11

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.00, max 2.50, latest -0.28

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2023
Best month: +10.01%; worst month: -7.48%
Positive months: 66%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=1.17
- Sideways: S=0.83
- Bear: S=1.03

## Negated Direction
Best negated: `rank(-1 * systematic_risk_last_360_days / close)` S=-0.14, F=-0.05, INFERIOR
Direction gap: -1.15 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * systematic_risk_last_360_days)`: S=-0.37, F=-0.23, T=16.4%, INFERIOR (TOP3000)
- `rank(-1 * systematic_risk_last_360_days / close)`: S=-0.14, F=-0.05, T=14.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(systematic_risk_last_360_days, 5))`: S=-0.92, F=-0.26, T=61.5%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(systematic_risk_last_360_days, 5))` | TOP200 | 1.01 | 0.47 | 13.9% | 80% | all-weather |
| `rank(ts_delta(systematic_risk_last_360_days, 5))` | TOP3000 | 0.92 | 0.26 | 7.8% | 80% | all-weather |
| `rank(ts_delta(systematic_risk_last_360_days, 5))` | TOP500 | 0.74 | 0.25 | 11.9% | 80% | mixed |
| `rank(systematic_risk_last_360_days)` | TOP3000 | 0.38 | 0.23 | 31.1% | 80% | bear-only |
| `rank(ts_delta(systematic_risk_last_360_days, 5))` | TOP1000 | 0.71 | 0.22 | 9.0% | 80% | all-weather |
| `rank(systematic_risk_last_360_days)` | TOP500 | 0.32 | 0.19 | 33.5% | 80% | bear-only |
| `rank(systematic_risk_last_360_days)` | TOP1000 | 0.18 | 0.08 | 37.9% | 80% | bear-only |
| `rank(systematic_risk_last_360_days)` | TOP200 | 0.11 | 0.03 | 41.7% | 60% | bear-only |

## Correlation Notes
Top correlates:
- systematic_risk_last_60_days: 0.464 (moderately positively correlated)
- implied_volatility_mean_90: 0.420 (moderately positively correlated)
- implied_volatility_put_20: 0.417 (moderately positively correlated)
- implied_volatility_mean_120: 0.415 (moderately positively correlated)
- beta_last_360_days_spy: 0.415 (moderately positively correlated)

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_fcf_high | analyst4 | -0.22 | 1.60 | +0.58 | -0.33 | yes |
| fnd6_newa1v1300_dpact | fundamental6 | -0.20 | 1.61 | +0.58 | +0.06 | yes |
| fnd6_dpvieb | fundamental6 | -0.20 | 1.62 | +0.58 | +0.06 | yes |
| fnd6_newa2v1300_sale | fundamental6 | -0.16 | 1.56 | +0.54 | -0.37 | yes |
| fnd6_newa2v1300_revt | fundamental6 | -0.16 | 1.56 | +0.54 | -0.37 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
