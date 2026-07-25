---
field: anl4_gric_low
dataset: analyst4
best_template: rank_value_norm
best_sharpe: 0.68
best_fitness: 0.44
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 7
max_drawdown: 0.0989
ann_vol: 0.0781
hit_rate: 0.4988
rolling_sharpe_min: -1.063
rolling_sharpe_max: 2.231
redundancy_cluster: 1
negated_best_sharpe: 0.12
negated_best_template: neg_rank_level
negated_best_fitness: 0.05
n_negated_sims: 10
direction_gap: -0.56
---
# anl4_gric_low (analyst4)

*Gross income - The lowest estimation*

## Signal Profile
- `rank(anl4_gric_low)`: S=0.45, F=0.30, T=1.1%, INFERIOR (TOP3000)
- `rank(anl4_gric_low / close)`: S=0.68, F=0.44, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_delta(anl4_gric_low, 5))`: S=0.50, F=0.16, T=36.9%, INFERIOR (TOP500)
- `-rank(anl4_gric_low)`: S=-0.18, F=-0.08, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_gric_low, 5))`: S=0.14, F=0.03, T=34.6%, INFERIOR (TOP3000)
- `ts_zscore(anl4_gric_low, 22)`: S=0.06, F=0.01, T=36.5%, INFERIOR (TOP3000)
- `ts_mean(anl4_gric_low, 10)`: S=0.09, F=0.03, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_gric_low, 22))`: S=0.30, F=0.09, T=14.0%, INFERIOR (TOP3000)
- `rank(-1 * anl4_gric_low)`: S=0.12, F=0.05, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * anl4_gric_low / close)`: S=0.11, F=0.04, T=2.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 4F/28P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/6P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.68, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.16 (negative), ret=-0.8%
  - 2020: S=-0.24 (negative), ret=-2.1%
  - 2021: S=1.13 (moderate), ret=+12.0%
  - 2022: S=1.46 (moderate), ret=+10.3%
  - 2023: S=1.42 (moderate), ret=+6.9%

## Risk & Drawdown
- Max drawdown: 9.89% over 115 days (recovered)
- Annualized: return +5.3%, volatility 7.8% (fraction of booksize)
- Hit rate: 49.9% positive days
- Tail shape: skew +0.38, excess kurtosis +2.88

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.06, max 2.23, latest 1.45

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +8.17%; worst month: -3.86%
Positive months: 52%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.15
- Sideways: S=0.22
- Bear: S=-1.81

## Negated Direction
Best negated: `rank(-1 * anl4_gric_low)` S=0.12, F=0.05, INFERIOR
Direction gap: -0.56 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * anl4_gric_low)`: S=0.12, F=0.05, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * anl4_gric_low / close)`: S=0.11, F=0.04, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_gric_low, 5))`: S=0.14, F=0.03, T=34.6%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_gric_low / close)` | TOP3000 | 0.68 | 0.44 | 9.9% | 60% | bull-only |
| `rank(anl4_gric_low)` | TOP3000 | 0.45 | 0.30 | 40.5% | 80% | bull-only |
| `rank(ts_delta(anl4_gric_low, 5))` | TOP500 | 0.51 | 0.16 | 21.2% | 40% | mixed |
| `rank(anl4_gric_low / close)` | TOP1000 | 0.24 | 0.11 | 22.0% | 60% | bull-only |
| `rank(ts_delta(anl4_gric_low, 5))` | TOP3000 | 0.42 | 0.10 | 6.8% | 60% | weak |
| `rank(ts_delta(anl4_gric_low, 5))` | TOP1000 | 0.36 | 0.09 | 10.5% | 60% | mixed |
| `rank(anl4_gric_low)` | TOP1000 | 0.17 | 0.08 | 46.2% | 60% | bull-only |

## Correlation Notes
Top correlates:
- anl4_gric_mean: 0.996 (strongly positively correlated)
- anl4_gric_median: 0.995 (strongly positively correlated)
- anl4_gric_high: 0.989 (strongly positively correlated)
- est_grossincome: 0.985 (strongly positively correlated)
- sales_estimate_minimum: 0.954 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
