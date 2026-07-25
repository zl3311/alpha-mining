---
field: fnd2_ebitfr
dataset: fundamental2
best_template: rank_delta
best_sharpe: 0.88
best_fitness: 0.66
best_universe: TOP200
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: all-weather
n_variations_with_pnl: 4
max_drawdown: 0.232
ann_vol: 0.1856
hit_rate: 0.502
rolling_sharpe_min: -0.41
rolling_sharpe_max: 2.395
top_merge_partner: growth_potential_rank_derivative
negated_best_sharpe: 0.49
negated_best_template: rank_neg_delta
negated_best_fitness: 0.23
n_negated_sims: 10
direction_gap: -0.39
---
# fnd2_ebitfr (fundamental2)

*EBIT, Foreign*

## Signal Profile
- `rank(fnd2_ebitfr)`: S=0.06, F=0.01, T=1.3%, INFERIOR (TOP1000)
- `rank(fnd2_ebitfr / close)`: S=0.15, F=0.05, T=1.5%, INFERIOR (TOP1000)
- `rank(ts_delta(fnd2_ebitfr, 5))`: S=0.88, F=0.66, T=29.0%, INFERIOR (TOP200)
- `-rank(fnd2_ebitfr)`: S=-0.06, F=-0.01, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_ebitfr, 5))`: S=0.49, F=0.23, T=33.5%, INFERIOR (TOP3000)
- `-ts_zscore(fnd2_ebitfr, 63)`: S=0.38, F=0.23, T=16.2%, INFERIOR (TOP3000)
- `ts_mean(fnd2_ebitfr, 10)`: S=0.11, F=0.03, T=0.9%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd2_ebitfr, 22))`: S=-0.02, F=0.00, T=14.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_ebitfr)`: S=0.08, F=0.02, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_ebitfr / close)`: S=0.02, F=0.00, T=1.8%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 21F/8P
- LOW_TURNOVER: 2F/30P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.88, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=1.03 (moderate), ret=+16.4%
  - 2020: S=0.22 (weak), ret=+4.4%
  - 2021: S=1.92 (strong), ret=+42.2%
  - 2022: S=0.45 (weak), ret=+8.0%
  - 2023: S=0.64 (moderate), ret=+9.3%

## Risk & Drawdown
- Max drawdown: 23.20% over 358 days (recovered)
- Annualized: return +16.4%, volatility 18.6% (fraction of booksize)
- Hit rate: 50.2% positive days
- Tail shape: skew +1.35, excess kurtosis +14.41

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.41, max 2.40, latest 0.60

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2020
Best month: +19.32%; worst month: -9.65%
Positive months: 52%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=0.88
- Sideways: S=0.80
- Bear: S=0.98

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd2_ebitfr, 5))` S=0.49, F=0.23, INFERIOR
Direction gap: -0.39 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd2_ebitfr)`: S=0.08, F=0.02, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_ebitfr / close)`: S=0.02, F=0.00, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_ebitfr, 5))`: S=0.49, F=0.23, T=33.5%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd2_ebitfr, 5))` | TOP200 | 0.88 | 0.66 | 23.2% | 100% | all-weather |
| `rank(ts_delta(fnd2_ebitfr, 5))` | TOP3000 | 0.35 | 0.14 | 19.1% | 60% | mixed |
| `rank(fnd2_ebitfr / close)` | TOP1000 | 0.14 | 0.05 | 31.0% | 60% | bull-only |
| `rank(fnd2_ebitfr / close)` | TOP3000 | 0.08 | 0.03 | 22.7% | 40% | bull-only |

## Correlation Notes
Top correlates:
- fnd2_unrgtxbnfinregfprtxps: 0.320 (weakly positively correlated)
- fnd2_ebitdm: 0.278 (weakly positively correlated)
- fnd2_a_flintasamt1expyfour: 0.236 (weakly positively correlated)
- fnd6_newa1v1300_ebit: 0.206 (weakly positively correlated)
- ebit: 0.206 (weakly positively correlated)

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| growth_potential_rank_derivative | model16 | -0.10 | 1.32 | +0.43 | -0.72 | yes |
| analyst_revision_rank_derivative | model16 | -0.10 | 1.35 | +0.42 | -0.68 | yes |
| relative_valuation_rank_derivative | model16 | -0.10 | 1.35 | +0.42 | -0.68 | yes |
| earnings_certainty_rank_derivative | model16 | -0.10 | 1.35 | +0.42 | -0.68 | yes |
| multi_factor_static_score_derivative | model16 | -0.10 | 1.28 | +0.40 | -0.75 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
