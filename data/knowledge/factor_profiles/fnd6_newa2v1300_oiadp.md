---
field: fnd6_newa2v1300_oiadp
dataset: fundamental6
best_template: rank_delta
best_sharpe: 0.96
best_fitness: 0.71
best_universe: TOP200
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: all-weather
n_variations_with_pnl: 7
max_drawdown: 0.2247
ann_vol: 0.1987
hit_rate: 0.5045
rolling_sharpe_min: -0.676
rolling_sharpe_max: 2.719
top_merge_partner: analyst_revision_rank_derivative
redundancy_cluster: 39
negated_best_sharpe: 0.26
negated_best_template: neg_rank_level
negated_best_fitness: 0.16
n_negated_sims: 10
direction_gap: -0.7
---
# fnd6_newa2v1300_oiadp (fundamental6)

*Operating Income After Depreciation*

## Signal Profile
- `rank(fnd6_newa2v1300_oiadp)`: S=0.19, F=0.08, T=0.9%, INFERIOR (TOP3000)
- `rank(fnd6_newa2v1300_oiadp / close)`: S=0.41, F=0.25, T=1.3%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_newa2v1300_oiadp, 5))`: S=0.96, F=0.71, T=35.0%, INFERIOR (TOP200)
- `-rank(fnd6_newa2v1300_oiadp)`: S=-0.09, F=-0.03, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa2v1300_oiadp, 5))`: S=-0.96, F=-0.71, T=34.6%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_newa2v1300_oiadp, 63)`: S=-0.06, F=-0.01, T=19.2%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newa2v1300_oiadp, 10)`: S=0.18, F=0.07, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newa2v1300_oiadp, 22))`: S=-0.10, F=-0.02, T=14.7%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa2v1300_oiadp)`: S=0.26, F=0.16, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa2v1300_oiadp / close)`: S=0.16, F=0.07, T=2.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 11F/21P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 11F/9P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.95, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=1.19 (moderate), ret=+13.0%
  - 2020: S=1.54 (strong), ret=+25.2%
  - 2021: S=0.72 (moderate), ret=+15.8%
  - 2022: S=0.86 (moderate), ret=+24.7%
  - 2023: S=0.95 (moderate), ret=+14.1%

## Risk & Drawdown
- Max drawdown: 22.47% over 30 days (recovered)
- Annualized: return +18.9%, volatility 19.9% (fraction of booksize)
- Hit rate: 50.4% positive days
- Tail shape: skew -0.71, excess kurtosis +23.22

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.68, max 2.72, latest 1.03

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2021
Best month: +18.26%; worst month: -8.74%
Positive months: 58%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=0.68
- Sideways: S=0.88
- Bear: S=1.40

## Negated Direction
Best negated: `rank(-1 * fnd6_newa2v1300_oiadp)` S=0.26, F=0.16, INFERIOR
Direction gap: -0.70 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_newa2v1300_oiadp)`: S=0.26, F=0.16, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa2v1300_oiadp / close)`: S=0.16, F=0.07, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa2v1300_oiadp, 5))`: S=-0.96, F=-0.71, T=34.6%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_newa2v1300_oiadp, 5))` | TOP200 | 0.95 | 0.71 | 22.5% | 100% | all-weather |
| `rank(fnd6_newa2v1300_oiadp / close)` | TOP3000 | 0.40 | 0.25 | 28.3% | 60% | bull-only |
| `rank(ts_delta(fnd6_newa2v1300_oiadp, 5))` | TOP500 | 0.43 | 0.19 | 17.2% | 80% | all-weather |
| `rank(fnd6_newa2v1300_oiadp / close)` | TOP1000 | 0.26 | 0.15 | 28.2% | 60% | bull-only |
| `rank(ts_delta(fnd6_newa2v1300_oiadp, 5))` | TOP1000 | 0.36 | 0.12 | 18.1% | 60% | mixed |
| `rank(fnd6_newa2v1300_oiadp)` | TOP3000 | 0.18 | 0.08 | 43.5% | 60% | bull-only |
| `rank(fnd6_newa2v1300_oiadp)` | TOP1000 | 0.07 | 0.03 | 44.9% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_newa1v1300_ebit: 1.000 (strongly positively correlated)
- ebit: 1.000 (strongly positively correlated)
- fnd6_newa2v1300_pi: 0.501 (moderately positively correlated)
- fnd6_newa2v1300_re: 0.482 (moderately positively correlated)
- fnd6_newa1v1300_epspi: 0.472 (moderately positively correlated)

Redundancy cluster #39: 3 similar fields, mean |rho| 1.0 (representative: ebit). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| analyst_revision_rank_derivative | model16 | -0.12 | 1.42 | +0.47 | +0.97 | yes |
| earnings_certainty_rank_derivative | model16 | -0.12 | 1.42 | +0.47 | +0.97 | yes |
| relative_valuation_rank_derivative | model16 | -0.12 | 1.42 | +0.47 | +0.97 | yes |
| systematic_risk_last_360_days | model51 | -0.20 | 1.44 | +0.43 | +0.30 | yes |
| growth_potential_rank_derivative | model16 | -0.12 | 1.38 | +0.43 | +0.97 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
