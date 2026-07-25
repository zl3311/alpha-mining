---
field: anl4_af_eps_value
dataset: analyst4
best_template: rank_value_norm
best_sharpe: 0.5
best_fitness: 0.35
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 7
max_drawdown: 0.237
ann_vol: 0.1211
hit_rate: 0.485
rolling_sharpe_min: -1.833
rolling_sharpe_max: 2.554
negated_best_sharpe: 0.17
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.08
n_negated_sims: 10
direction_gap: -0.33
---
# anl4_af_eps_value (analyst4)

*Earnings Per Share - Actual Value*

## Signal Profile
- `rank(anl4_af_eps_value)`: S=0.20, F=0.09, T=1.0%, INFERIOR (TOP3000)
- `rank(anl4_af_eps_value / close)`: S=0.50, F=0.35, T=1.9%, INFERIOR (TOP3000)
- `rank(ts_delta(anl4_af_eps_value, 5))`: S=0.47, F=0.22, T=34.7%, INFERIOR (TOP500)
- `-rank(anl4_af_eps_value)`: S=-0.08, F=-0.02, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_af_eps_value, 5))`: S=-0.09, F=-0.02, T=35.2%, INFERIOR (TOP3000)
- `ts_zscore(anl4_af_eps_value, 22)`: S=-0.08, F=-0.02, T=28.7%, INFERIOR (TOP3000)
- `ts_mean(anl4_af_eps_value, 10)`: S=0.05, F=0.01, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_af_eps_value, 22))`: S=-0.47, F=-0.24, T=14.9%, INFERIOR (TOP3000)
- `rank(-1 * anl4_af_eps_value)`: S=0.16, F=0.07, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * anl4_af_eps_value / close)`: S=0.17, F=0.08, T=2.8%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/6P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.48, Consistency 40% positive years (2/5)
Yearly breakdown:
  - 2019: S=-0.18 (negative), ret=-0.9%
  - 2020: S=-1.08 (negative), ret=-10.8%
  - 2021: S=1.34 (moderate), ret=+19.1%
  - 2022: S=1.30 (moderate), ret=+22.2%
  - 2023: S=-0.12 (negative), ret=-1.1%

## Risk & Drawdown
- Max drawdown: 23.70% over 1037 days (recovered)
- Annualized: return +5.8%, volatility 12.1% (fraction of booksize)
- Hit rate: 48.5% positive days
- Tail shape: skew +0.12, excess kurtosis +2.05

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.83, max 2.55, latest -0.29

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2020
Best month: +8.95%; worst month: -6.01%
Positive months: 54%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.13
- Sideways: S=0.13
- Bear: S=-2.76

## Negated Direction
Best negated: `rank(-1 * anl4_af_eps_value / close)` S=0.17, F=0.08, INFERIOR
Direction gap: -0.33 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * anl4_af_eps_value)`: S=0.16, F=0.07, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * anl4_af_eps_value / close)`: S=0.17, F=0.08, T=2.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_af_eps_value, 5))`: S=-0.09, F=-0.02, T=35.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_af_eps_value / close)` | TOP3000 | 0.48 | 0.35 | 23.7% | 40% | bull-only |
| `rank(ts_delta(anl4_af_eps_value, 5))` | TOP500 | 0.46 | 0.22 | 26.3% | 80% | mixed |
| `rank(ts_delta(anl4_af_eps_value, 5))` | TOP3000 | 0.39 | 0.14 | 15.9% | 60% | all-weather |
| `rank(anl4_af_eps_value / close)` | TOP1000 | 0.22 | 0.13 | 28.0% | 40% | bull-only |
| `rank(ts_delta(anl4_af_eps_value, 5))` | TOP1000 | 0.29 | 0.10 | 20.6% | 60% | mixed |
| `rank(anl4_af_eps_value)` | TOP3000 | 0.19 | 0.09 | 43.5% | 60% | bull-only |
| `rank(ts_delta(anl4_af_eps_value, 5))` | TOP200 | 0.22 | 0.08 | 72.2% | 60% | mixed |

## Correlation Notes
Top correlates:
- fnd6_newa2v1300_opeps: 0.978 (strongly positively correlated)
- fnd6_mfma2_opeps: 0.977 (strongly positively correlated)
- fnd6_oprepsx: 0.977 (strongly positively correlated)
- fnd6_newa2v1300_oibdp: 0.957 (strongly positively correlated)
- ebitda: 0.957 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
