---
field: anl4_ebit_high
dataset: analyst4
best_template: rank_value_norm
best_sharpe: 0.71
best_fitness: 0.5
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 8
max_drawdown: 0.2007
ann_vol: 0.0873
hit_rate: 0.4996
rolling_sharpe_min: -2.204
rolling_sharpe_max: 2.832
redundancy_cluster: 13
negated_best_sharpe: 0.39
negated_best_template: rank_neg_delta
negated_best_fitness: 0.13
n_negated_sims: 10
direction_gap: -0.32
---
# anl4_ebit_high (analyst4)

*Earnings before interest and taxes - The highest estimation*

## Signal Profile
- `rank(anl4_ebit_high)`: S=0.43, F=0.28, T=1.2%, INFERIOR (TOP3000)
- `rank(anl4_ebit_high / close)`: S=0.71, F=0.50, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_delta(anl4_ebit_high, 5))`: S=0.54, F=0.15, T=36.9%, INFERIOR (TOP1000)
- `-rank(anl4_ebit_high)`: S=-0.17, F=-0.07, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_ebit_high, 5))`: S=0.39, F=0.13, T=35.5%, INFERIOR (TOP3000)
- `ts_zscore(anl4_ebit_high, 22)`: S=0.31, F=0.08, T=35.4%, INFERIOR (TOP3000)
- `ts_mean(anl4_ebit_high, 10)`: S=0.04, F=0.01, T=1.3%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_ebit_high, 22))`: S=0.45, F=0.16, T=14.0%, INFERIOR (TOP3000)
- `rank(-1 * anl4_ebit_high)`: S=0.01, F=0.00, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * anl4_ebit_high / close)`: S=0.01, F=0.00, T=2.3%, INFERIOR (TOP3000)

## Check Summary
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 15F/5P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.71, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.16 (negative), ret=-0.7%
  - 2020: S=-1.56 (negative), ret=-10.8%
  - 2021: S=1.52 (strong), ret=+17.2%
  - 2022: S=2.02 (strong), ret=+22.8%
  - 2023: S=0.26 (weak), ret=+1.7%

## Risk & Drawdown
- Max drawdown: 20.07% over 772 days (recovered)
- Annualized: return +6.2%, volatility 8.7% (fraction of booksize)
- Hit rate: 50.0% positive days
- Tail shape: skew +0.10, excess kurtosis +1.72

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.20, max 2.83, latest 0.05

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +9.12%; worst month: -3.98%
Positive months: 52%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.56
- Sideways: S=0.72
- Bear: S=-2.91

## Negated Direction
Best negated: `rank(-1 * ts_delta(anl4_ebit_high, 5))` S=0.39, F=0.13, INFERIOR
Direction gap: -0.32 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * anl4_ebit_high)`: S=0.01, F=0.00, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * anl4_ebit_high / close)`: S=0.01, F=0.00, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_ebit_high, 5))`: S=0.39, F=0.13, T=35.5%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_ebit_high / close)` | TOP3000 | 0.71 | 0.50 | 20.1% | 60% | bull-only |
| `rank(anl4_ebit_high)` | TOP3000 | 0.43 | 0.28 | 38.1% | 60% | bull-only |
| `rank(anl4_ebit_high / close)` | TOP1000 | 0.35 | 0.20 | 23.4% | 60% | bull-only |
| `rank(ts_delta(anl4_ebit_high, 5))` | TOP1000 | 0.55 | 0.15 | 10.9% | 60% | mixed |
| `rank(anl4_ebit_high / close)` | TOP500 | 0.24 | 0.12 | 34.8% | 60% | bull-only |
| `rank(anl4_ebit_high)` | TOP1000 | 0.16 | 0.07 | 42.1% | 60% | bull-only |
| `rank(anl4_ebit_high)` | TOP500 | 0.14 | 0.06 | 49.8% | 60% | bull-only |
| `rank(ts_delta(anl4_ebit_high, 5))` | TOP3000 | 0.28 | 0.04 | 9.0% | 60% | mixed |

## Correlation Notes
Top correlates:
- anl4_ebit_median: 0.994 (strongly positively correlated)
- anl4_ebit_mean: 0.993 (strongly positively correlated)
- est_ebit: 0.992 (strongly positively correlated)
- anl4_ebit_low: 0.982 (strongly positively correlated)
- anl4_ptp_high: 0.979 (strongly positively correlated)

Redundancy cluster #13: 127 similar fields, mean |rho| 0.82 (representative: anl4_bvps_flag). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
