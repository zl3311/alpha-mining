---
field: fnd6_newa1v1300_aociother
dataset: fundamental6
best_template: rank_delta
best_sharpe: 0.83
best_fitness: 0.61
best_universe: TOP1000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: all-weather
n_variations_with_pnl: 8
max_drawdown: 0.4576
ann_vol: 0.1717
hit_rate: 0.4996
rolling_sharpe_min: -1.686
rolling_sharpe_max: 2.447
top_merge_partner: parkinson_volatility_120
negated_best_sharpe: 0.23
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.09
n_negated_sims: 10
direction_gap: -0.6
---
# fnd6_newa1v1300_aociother (fundamental6)

*Accum Other Comp Inc - Other Adjustments*

## Signal Profile
- `rank(fnd6_newa1v1300_aociother)`: S=0.42, F=0.15, T=2.2%, INFERIOR (TOP1000)
- `rank(fnd6_newa1v1300_aociother / close)`: S=0.41, F=0.15, T=2.2%, INFERIOR (TOP1000)
- `rank(ts_delta(fnd6_newa1v1300_aociother, 5))`: S=0.83, F=0.61, T=26.2%, INFERIOR (TOP1000)
- `-rank(fnd6_newa1v1300_aociother)`: S=-0.42, F=-0.15, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa1v1300_aociother, 5))`: S=-0.15, F=-0.05, T=19.3%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_newa1v1300_aociother, 63)`: S=0.02, F=0.00, T=11.1%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newa1v1300_aociother, 10)`: S=0.23, F=0.09, T=1.8%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newa1v1300_aociother, 22))`: S=0.36, F=0.21, T=19.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_aociother)`: S=0.22, F=0.08, T=3.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_aociother / close)`: S=0.23, F=0.09, T=3.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 5F/15P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.83, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=-0.58 (negative), ret=-11.8%
  - 2020: S=1.17 (moderate), ret=+22.9%
  - 2021: S=1.14 (moderate), ret=+15.1%
  - 2022: S=1.38 (moderate), ret=+24.0%
  - 2023: S=1.75 (strong), ret=+20.0%

## Risk & Drawdown
- Max drawdown: 45.76% over 774 days (recovered)
- Annualized: return +14.3%, volatility 17.2% (fraction of booksize)
- Hit rate: 50.0% positive days
- Tail shape: skew +0.36, excess kurtosis +32.77

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.69, max 2.45, latest 1.72

## Yearly & Monthly Returns
Best year (by Sharpe): 2023; worst year: 2019
Best month: +14.90%; worst month: -12.03%
Positive months: 63%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=1.31
- Sideways: S=0.09
- Bear: S=1.17

## Negated Direction
Best negated: `rank(-1 * fnd6_newa1v1300_aociother / close)` S=0.23, F=0.09, INFERIOR
Direction gap: -0.60 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_newa1v1300_aociother)`: S=0.22, F=0.08, T=3.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_aociother / close)`: S=0.23, F=0.09, T=3.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa1v1300_aociother, 5))`: S=-0.15, F=-0.05, T=19.3%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_newa1v1300_aociother, 5))` | TOP1000 | 0.83 | 0.61 | 45.8% | 80% | all-weather |
| `rank(ts_delta(fnd6_newa1v1300_aociother, 5))` | TOP500 | 0.59 | 0.36 | 16.1% | 40% | bull-only |
| `rank(ts_delta(fnd6_newa1v1300_aociother, 5))` | TOP200 | 0.52 | 0.33 | 21.6% | 80% | mixed |
| `rank(fnd6_newa1v1300_aociother / close)` | TOP1000 | 0.42 | 0.15 | 8.9% | 60% | mixed |
| `rank(fnd6_newa1v1300_aociother)` | TOP1000 | 0.44 | 0.15 | 9.0% | 60% | mixed |
| `rank(ts_delta(fnd6_newa1v1300_aociother, 5))` | TOP3000 | 0.30 | 0.13 | 38.5% | 60% | bull-only |
| `rank(fnd6_newa1v1300_aociother)` | TOP500 | 0.16 | 0.04 | 12.7% | 40% | bear-only |
| `rank(fnd6_newa1v1300_aociother / close)` | TOP500 | 0.14 | 0.03 | 12.4% | 60% | bear-only |

## Correlation Notes
Top correlates:
- fnd6_newa1v1300_acominc: 0.204 (weakly positively correlated)
- fnd6_ciother: 0.203 (weakly positively correlated)
- fnd6_txpd: -0.192 (weakly negatively correlated)
- fnd6_reajo: 0.167 (weakly positively correlated)
- fnd6_newa1v1300_ibc: 0.166 (weakly positively correlated)

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| parkinson_volatility_120 | option8 | -0.13 | 1.20 | +0.30 | -0.92 | yes |
| reporting_currency_code_9 | analyst4 | +0.01 | 1.16 | +0.33 | -0.65 | yes |
| pv13_revere_key_sector_total | pv13 | +0.01 | 1.19 | +0.34 | -0.50 | yes |
| anl4_tbvps_number | analyst4 | -0.10 | 1.21 | +0.35 | -0.31 | yes |
| systematic_risk_last_60_days | model51 | -0.06 | 1.21 | +0.34 | -0.29 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
