---
field: ebit
dataset: fundamental6
best_template: rank_delta
best_sharpe: 0.96
best_fitness: 0.71
best_universe: TOP200
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 37
regime_profile: all-weather
n_variations_with_pnl: 9
max_drawdown: 0.2249
ann_vol: 0.1988
hit_rate: 0.5036
rolling_sharpe_min: -0.672
rolling_sharpe_max: 2.719
top_merge_partner: earnings_certainty_rank_derivative
redundancy_cluster: 39
negated_best_sharpe: 0.27
negated_best_template: neg_rank_level
negated_best_fitness: 0.16
n_negated_sims: 10
direction_gap: -0.69
---
# ebit (fundamental6)

*Earnings Before Interest and Taxes*

## Signal Profile
- `rank(ebit)`: S=0.19, F=0.08, T=0.9%, INFERIOR (TOP3000)
- `rank(ebit / close)`: S=0.41, F=0.25, T=1.3%, INFERIOR (TOP3000)
- `rank(ts_delta(ebit, 5))`: S=0.96, F=0.71, T=35.0%, INFERIOR (TOP200)
- `ts_decay_linear(rank(ebit), 5)`: S=0.19, F=0.08, T=0.9%, INFERIOR (TOP3000)
- `trade_when(ts_std_dev(returns,20)>0.02, rank(ebit), ts_std_dev(returns,20)<0.01)`: S=0.13, F=0.05, T=1.9%, INFERIOR (TOP3000)
- `-rank(ebit)`: S=-0.07, F=-0.02, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(ebit, 5))`: S=-1.02, F=-0.78, T=34.9%, INFERIOR (TOP3000)
- `-ts_zscore(ebit, 63)`: S=-0.04, F=-0.01, T=19.3%, INFERIOR (TOP3000)
- `ts_mean(ebit, 10)`: S=0.16, F=0.06, T=1.0%, INFERIOR (TOP3000)
- `rank(ts_rank(ebit, 22))`: S=-0.10, F=-0.02, T=14.6%, INFERIOR (TOP3000)
- `rank(-1 * ebit)`: S=0.27, F=0.16, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * ebit / close)`: S=0.19, F=0.09, T=2.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/25P
- LOW_FITNESS: 37F/0P
- LOW_SHARPE: 37F/0P
- LOW_SUB_UNIVERSE_SHARPE: 17F/8P
- LOW_TURNOVER: 3F/34P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.96, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=1.18 (moderate), ret=+13.0%
  - 2020: S=1.52 (strong), ret=+25.0%
  - 2021: S=0.74 (moderate), ret=+16.2%
  - 2022: S=0.86 (moderate), ret=+24.8%
  - 2023: S=0.97 (moderate), ret=+14.4%

## Risk & Drawdown
- Max drawdown: 22.49% over 30 days (recovered)
- Annualized: return +19.1%, volatility 19.9% (fraction of booksize)
- Hit rate: 50.4% positive days
- Tail shape: skew -0.71, excess kurtosis +23.30

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.67, max 2.72, latest 1.06

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2021
Best month: +18.33%; worst month: -8.81%
Positive months: 59%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=0.68
- Sideways: S=0.87
- Bear: S=1.43

## Negated Direction
Best negated: `rank(-1 * ebit)` S=0.27, F=0.16, INFERIOR
Direction gap: -0.69 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * ebit)`: S=0.27, F=0.16, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * ebit / close)`: S=0.19, F=0.09, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(ebit, 5))`: S=-1.02, F=-0.78, T=34.9%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(ebit, 5))` | TOP200 | 0.96 | 0.71 | 22.5% | 100% | all-weather |
| `rank(ebit / close)` | TOP3000 | 0.40 | 0.25 | 28.1% | 60% | bull-only |
| `rank(ts_delta(ebit, 5))` | TOP500 | 0.44 | 0.20 | 16.4% | 80% | all-weather |
| `rank(ebit / close)` | TOP1000 | 0.24 | 0.13 | 28.6% | 60% | bull-only |
| `rank(ts_delta(ebit, 5))` | TOP1000 | 0.36 | 0.12 | 18.6% | 60% | mixed |
| `rank(ebit)` | TOP3000 | 0.18 | 0.08 | 43.2% | 60% | bull-only |
| `ts_decay_linear(rank(ebit), 5)` | TOP3000 | 0.18 | 0.08 | 43.3% | 60% | bull-only |
| `trade_when(ts_std_dev(returns,20)>0.02, rank(ebit), ts_std_dev(returns,20)<0.01)` | TOP3000 | 0.11 | 0.05 | 42.0% | 60% | bull-only |
| `rank(ebit)` | TOP1000 | 0.06 | 0.02 | 45.2% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_newa1v1300_ebit: 1.000 (strongly positively correlated)
- fnd6_newa2v1300_oiadp: 1.000 (strongly positively correlated)
- fnd6_newa2v1300_pi: 0.500 (moderately positively correlated)
- fnd6_newa2v1300_re: 0.481 (moderately positively correlated)
- fnd6_newa1v1300_epspi: 0.471 (moderately positively correlated)

Redundancy cluster #39: 3 similar fields, mean |rho| 1.0 (representative). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| earnings_certainty_rank_derivative | model16 | -0.12 | 1.43 | +0.47 | +0.96 | yes |
| analyst_revision_rank_derivative | model16 | -0.12 | 1.43 | +0.47 | +0.96 | yes |
| relative_valuation_rank_derivative | model16 | -0.12 | 1.43 | +0.47 | +0.96 | yes |
| systematic_risk_last_360_days | model51 | -0.20 | 1.45 | +0.44 | +0.28 | yes |
| growth_potential_rank_derivative | model16 | -0.12 | 1.39 | +0.43 | +0.96 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
