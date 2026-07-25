---
field: anl4_gric_number
dataset: analyst4
best_template: rank_level
best_sharpe: 0.75
best_fitness: 0.41
best_universe: TOP500
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: all-weather
n_variations_with_pnl: 6
max_drawdown: 0.0594
ann_vol: 0.0509
hit_rate: 0.5198
rolling_sharpe_min: -1.143
rolling_sharpe_max: 2.682
negated_best_sharpe: 0.16
negated_best_template: neg_rank_level
negated_best_fitness: 0.05
n_negated_sims: 10
direction_gap: -0.59
---
# anl4_gric_number (analyst4)

*Gross income - number of estimations*

## Signal Profile
- `rank(anl4_gric_number)`: S=0.75, F=0.41, T=4.2%, INFERIOR (TOP500)
- `rank(anl4_gric_number / close)`: S=0.39, F=0.21, T=3.5%, INFERIOR (TOP500)
- `rank(ts_delta(anl4_gric_number, 5))`: S=0.04, F=0.01, T=32.8%, INFERIOR (TOP200)
- `-rank(anl4_gric_number)`: S=-0.57, F=-0.24, T=3.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_gric_number, 5))`: S=-0.04, F=-0.01, T=32.8%, INFERIOR (TOP3000)
- `-ts_zscore(anl4_gric_number, 63)`: S=0.22, F=0.06, T=19.5%, INFERIOR (TOP3000)
- `ts_mean(anl4_gric_number, 10)`: S=0.50, F=0.22, T=3.4%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_gric_number, 22))`: S=-0.01, F=0.00, T=13.0%, INFERIOR (TOP3000)
- `rank(-1 * anl4_gric_number)`: S=0.16, F=0.05, T=4.7%, INFERIOR (TOP3000)
- `rank(-1 * anl4_gric_number / close)`: S=-0.19, F=-0.08, T=3.8%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 4F/28P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 8F/12P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.78, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=-0.23 (negative), ret=-0.9%
  - 2020: S=2.16 (strong), ret=+10.8%
  - 2021: S=1.25 (moderate), ret=+6.5%
  - 2022: S=0.33 (weak), ret=+2.0%
  - 2023: S=0.23 (weak), ret=+1.0%

## Risk & Drawdown
- Max drawdown: 5.94% over 428 days (recovered)
- Annualized: return +4.0%, volatility 5.1% (fraction of booksize)
- Hit rate: 52.0% positive days
- Tail shape: skew +0.18, excess kurtosis +0.65

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.14, max 2.68, latest 0.26

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2019
Best month: +3.07%; worst month: -2.38%
Positive months: 63%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=0.81
- Sideways: S=-0.82
- Bear: S=2.24

## Negated Direction
Best negated: `rank(-1 * anl4_gric_number)` S=0.16, F=0.05, INFERIOR
Direction gap: -0.59 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * anl4_gric_number)`: S=0.16, F=0.05, T=4.7%, INFERIOR (TOP3000)
- `rank(-1 * anl4_gric_number / close)`: S=-0.19, F=-0.08, T=3.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_gric_number, 5))`: S=-0.04, F=-0.01, T=32.8%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_gric_number)` | TOP500 | 0.78 | 0.41 | 5.9% | 80% | all-weather |
| `rank(anl4_gric_number)` | TOP3000 | 0.65 | 0.25 | 5.5% | 80% | all-weather |
| `rank(anl4_gric_number)` | TOP1000 | 0.61 | 0.24 | 5.6% | 80% | mixed |
| `rank(anl4_gric_number / close)` | TOP500 | 0.40 | 0.21 | 24.2% | 60% | mixed |
| `rank(anl4_gric_number / close)` | TOP1000 | 0.26 | 0.12 | 30.1% | 40% | bear-only |
| `rank(anl4_gric_number / close)` | TOP200 | 0.20 | 0.08 | 22.6% | 80% | mixed |

## Correlation Notes
Top correlates:
- anl4_ptp_number: 0.359 (weakly positively correlated)
- anl4_ebit_number: 0.236 (weakly positively correlated)
- anl4_netprofit_number: 0.234 (weakly positively correlated)
- max_gross_income_guidance: 0.224 (weakly positively correlated)
- min_gross_income_guidance: 0.223 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
