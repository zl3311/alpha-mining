---
field: anl4_gric_value
dataset: analyst4
best_template: rank_value_norm
best_sharpe: 0.73
best_fitness: 0.54
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 5
max_drawdown: 0.171
ann_vol: 0.093
hit_rate: 0.5028
rolling_sharpe_min: -1.498
rolling_sharpe_max: 2.499
redundancy_cluster: 1
negated_best_sharpe: 0.49
negated_best_template: rank_neg_delta
negated_best_fitness: 0.12
n_negated_sims: 10
direction_gap: -0.24
---
# anl4_gric_value (analyst4)

*Gross income- announced financial value*

## Signal Profile
- `rank(anl4_gric_value)`: S=0.41, F=0.28, T=1.6%, INFERIOR (TOP3000)
- `rank(anl4_gric_value / close)`: S=0.73, F=0.54, T=2.1%, INFERIOR (TOP3000)
- `rank(ts_delta(anl4_gric_value, 5))`: S=-0.21, F=-0.05, T=37.2%, INFERIOR (TOP500)
- `-rank(anl4_gric_value)`: S=-0.12, F=-0.05, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_gric_value, 5))`: S=0.49, F=0.12, T=38.6%, INFERIOR (TOP3000)
- `ts_zscore(anl4_gric_value, 22)`: S=0.10, F=0.02, T=39.4%, INFERIOR (TOP3000)
- `ts_mean(anl4_gric_value, 10)`: S=0.03, F=0.01, T=1.5%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_gric_value, 22))`: S=0.34, F=0.11, T=16.3%, INFERIOR (TOP3000)
- `rank(-1 * anl4_gric_value)`: S=-0.41, F=-0.28, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * anl4_gric_value / close)`: S=-0.73, F=-0.54, T=2.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 6F/26P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 15F/14P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.73, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.14 (negative), ret=-0.8%
  - 2020: S=-1.00 (negative), ret=-8.7%
  - 2021: S=1.28 (moderate), ret=+16.5%
  - 2022: S=1.98 (strong), ret=+21.1%
  - 2023: S=0.91 (moderate), ret=+5.0%

## Risk & Drawdown
- Max drawdown: 17.10% over 545 days (recovered)
- Annualized: return +6.8%, volatility 9.3% (fraction of booksize)
- Hit rate: 50.3% positive days
- Tail shape: skew +0.21, excess kurtosis +2.19

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.50, max 2.50, latest 0.84

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +11.30%; worst month: -5.29%
Positive months: 54%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.59
- Sideways: S=0.30
- Bear: S=-2.64

## Negated Direction
Best negated: `rank(-1 * ts_delta(anl4_gric_value, 5))` S=0.49, F=0.12, INFERIOR
Direction gap: -0.24 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * anl4_gric_value)`: S=-0.41, F=-0.28, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * anl4_gric_value / close)`: S=-0.73, F=-0.54, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_gric_value, 5))`: S=0.49, F=0.12, T=38.6%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_gric_value / close)` | TOP3000 | 0.73 | 0.54 | 17.1% | 60% | bull-only |
| `rank(anl4_gric_value)` | TOP3000 | 0.41 | 0.28 | 46.3% | 80% | bull-only |
| `rank(anl4_gric_value / close)` | TOP1000 | 0.25 | 0.12 | 30.3% | 60% | bull-only |
| `rank(anl4_gric_value)` | TOP1000 | 0.11 | 0.05 | 50.4% | 60% | bull-only |
| `rank(anl4_gric_value / close)` | TOP500 | 0.07 | 0.02 | 45.4% | 60% | bull-only |

## Correlation Notes
Top correlates:
- gross_income_reported_value: 1.000 (strongly positively correlated)
- gross_income_total: 0.979 (strongly positively correlated)
- fnd6_newa1v1300_gp: 0.959 (strongly positively correlated)
- revenue: 0.951 (strongly positively correlated)
- fnd6_newqv1300_revtq: 0.951 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
