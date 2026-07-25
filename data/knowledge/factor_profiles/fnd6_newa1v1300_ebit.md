---
field: fnd6_newa1v1300_ebit
dataset: fundamental6
best_template: rank_delta
best_sharpe: 0.95
best_fitness: 0.7
best_universe: TOP200
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: all-weather
n_variations_with_pnl: 7
max_drawdown: 0.2247
ann_vol: 0.1988
hit_rate: 0.5012
rolling_sharpe_min: -0.706
rolling_sharpe_max: 2.72
top_merge_partner: relative_valuation_rank_derivative
redundancy_cluster: 39
negated_best_sharpe: 0.27
negated_best_template: neg_rank_level
negated_best_fitness: 0.17
n_negated_sims: 10
direction_gap: -0.68
---
# fnd6_newa1v1300_ebit (fundamental6)

*Earnings Before Interest and Taxes*

## Signal Profile
- `rank(fnd6_newa1v1300_ebit)`: S=0.19, F=0.09, T=0.9%, INFERIOR (TOP3000)
- `rank(fnd6_newa1v1300_ebit / close)`: S=0.41, F=0.25, T=1.3%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_newa1v1300_ebit, 5))`: S=0.95, F=0.70, T=35.0%, INFERIOR (TOP200)
- `-rank(fnd6_newa1v1300_ebit)`: S=-0.09, F=-0.03, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa1v1300_ebit, 5))`: S=-1.01, F=-0.76, T=35.0%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_newa1v1300_ebit, 63)`: S=-0.06, F=-0.01, T=19.2%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newa1v1300_ebit, 10)`: S=0.17, F=0.06, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newa1v1300_ebit, 22))`: S=-0.09, F=-0.02, T=14.6%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_ebit)`: S=0.27, F=0.17, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_ebit / close)`: S=0.19, F=0.09, T=2.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 11F/21P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 12F/8P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.95, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=1.18 (moderate), ret=+13.0%
  - 2020: S=1.52 (strong), ret=+25.0%
  - 2021: S=0.70 (moderate), ret=+15.3%
  - 2022: S=0.86 (moderate), ret=+24.6%
  - 2023: S=0.97 (moderate), ret=+14.3%

## Risk & Drawdown
- Max drawdown: 22.47% over 30 days (recovered)
- Annualized: return +18.8%, volatility 19.9% (fraction of booksize)
- Hit rate: 50.1% positive days
- Tail shape: skew -0.71, excess kurtosis +23.17

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.71, max 2.72, latest 1.05

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2021
Best month: +18.25%; worst month: -8.74%
Positive months: 59%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=0.67
- Sideways: S=0.88
- Bear: S=1.39

## Negated Direction
Best negated: `rank(-1 * fnd6_newa1v1300_ebit)` S=0.27, F=0.17, INFERIOR
Direction gap: -0.68 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_newa1v1300_ebit)`: S=0.27, F=0.17, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_ebit / close)`: S=0.19, F=0.09, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa1v1300_ebit, 5))`: S=-1.01, F=-0.76, T=35.0%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_newa1v1300_ebit, 5))` | TOP200 | 0.95 | 0.70 | 22.5% | 100% | all-weather |
| `rank(fnd6_newa1v1300_ebit / close)` | TOP3000 | 0.40 | 0.25 | 28.3% | 60% | bull-only |
| `rank(ts_delta(fnd6_newa1v1300_ebit, 5))` | TOP500 | 0.44 | 0.19 | 17.0% | 80% | all-weather |
| `rank(fnd6_newa1v1300_ebit / close)` | TOP1000 | 0.25 | 0.14 | 28.2% | 60% | bull-only |
| `rank(ts_delta(fnd6_newa1v1300_ebit, 5))` | TOP1000 | 0.37 | 0.12 | 17.8% | 60% | mixed |
| `rank(fnd6_newa1v1300_ebit)` | TOP3000 | 0.18 | 0.09 | 43.4% | 60% | bull-only |
| `rank(fnd6_newa1v1300_ebit)` | TOP1000 | 0.07 | 0.03 | 44.8% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_newa2v1300_oiadp: 1.000 (strongly positively correlated)
- ebit: 1.000 (strongly positively correlated)
- fnd6_newa2v1300_pi: 0.502 (moderately positively correlated)
- fnd6_newa2v1300_re: 0.482 (moderately positively correlated)
- fnd6_newa1v1300_epspi: 0.472 (moderately positively correlated)

Redundancy cluster #39: 3 similar fields, mean |rho| 1.0 (representative: ebit). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| relative_valuation_rank_derivative | model16 | -0.12 | 1.42 | +0.47 | +0.96 | yes |
| earnings_certainty_rank_derivative | model16 | -0.12 | 1.42 | +0.47 | +0.96 | yes |
| analyst_revision_rank_derivative | model16 | -0.12 | 1.42 | +0.47 | +0.96 | yes |
| growth_potential_rank_derivative | model16 | -0.12 | 1.38 | +0.43 | +0.96 | yes |
| systematic_risk_last_360_days | model51 | -0.20 | 1.44 | +0.43 | +0.26 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
