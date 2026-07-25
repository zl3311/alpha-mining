---
field: anl4_totassets_high
dataset: analyst4
best_template: rank_value_norm
best_sharpe: 0.78
best_fitness: 0.54
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 10
max_drawdown: 0.0835
ann_vol: 0.0785
hit_rate: 0.4874
rolling_sharpe_min: -0.834
rolling_sharpe_max: 2.492
redundancy_cluster: 1
negated_best_sharpe: 0.19
negated_best_template: neg_rank_level
negated_best_fitness: 0.09
n_negated_sims: 10
direction_gap: -0.59
---
# anl4_totassets_high (analyst4)

*Total Assets - The highest estimation*

## Signal Profile
- `rank(anl4_totassets_high)`: S=0.64, F=0.48, T=1.1%, INFERIOR (TOP3000)
- `rank(anl4_totassets_high / close)`: S=0.78, F=0.54, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_delta(anl4_totassets_high, 5))`: S=0.93, F=0.31, T=36.7%, INFERIOR (TOP3000)
- `-rank(anl4_totassets_high)`: S=-0.28, F=-0.15, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_totassets_high, 5))`: S=-0.31, F=-0.10, T=34.6%, INFERIOR (TOP3000)
- `ts_zscore(anl4_totassets_high, 22)`: S=0.44, F=0.15, T=35.6%, INFERIOR (TOP3000)
- `ts_mean(anl4_totassets_high, 10)`: S=-0.09, F=-0.02, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_totassets_high, 22))`: S=0.00, F=0.00, T=13.7%, INFERIOR (TOP3000)
- `rank(-1 * anl4_totassets_high)`: S=0.19, F=0.09, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * anl4_totassets_high / close)`: S=0.06, F=0.02, T=2.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 5F/27P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 15F/5P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.77, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.27 (weak), ret=+1.4%
  - 2020: S=0.12 (weak), ret=+1.1%
  - 2021: S=1.55 (strong), ret=+14.6%
  - 2022: S=0.96 (moderate), ret=+6.4%
  - 2023: S=1.06 (moderate), ret=+6.1%

## Risk & Drawdown
- Max drawdown: 8.35% over 203 days (recovered)
- Annualized: return +6.0%, volatility 7.8% (fraction of booksize)
- Hit rate: 48.7% positive days
- Tail shape: skew +0.71, excess kurtosis +3.22

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.83, max 2.49, latest 1.18

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2020
Best month: +7.88%; worst month: -3.36%
Positive months: 56%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.62
- Sideways: S=0.33
- Bear: S=-0.98

## Negated Direction
Best negated: `rank(-1 * anl4_totassets_high)` S=0.19, F=0.09, INFERIOR
Direction gap: -0.59 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * anl4_totassets_high)`: S=0.19, F=0.09, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * anl4_totassets_high / close)`: S=0.06, F=0.02, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_totassets_high, 5))`: S=-0.31, F=-0.10, T=34.6%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_totassets_high / close)` | TOP3000 | 0.77 | 0.54 | 8.3% | 100% | bull-only |
| `rank(anl4_totassets_high)` | TOP3000 | 0.63 | 0.48 | 29.4% | 80% | bull-only |
| `rank(ts_delta(anl4_totassets_high, 5))` | TOP3000 | 0.94 | 0.31 | 5.6% | 100% | all-weather |
| `rank(anl4_totassets_high / close)` | TOP1000 | 0.40 | 0.22 | 13.4% | 80% | bull-only |
| `rank(anl4_totassets_high)` | TOP1000 | 0.27 | 0.15 | 31.8% | 60% | bull-only |
| `rank(ts_delta(anl4_totassets_high, 5))` | TOP1000 | 0.41 | 0.11 | 9.2% | 60% | mixed |
| `rank(ts_delta(anl4_totassets_high, 5))` | TOP200 | 0.32 | 0.10 | 17.1% | 80% | weak |
| `rank(anl4_totassets_high / close)` | TOP500 | 0.22 | 0.10 | 28.4% | 80% | bull-only |
| `rank(anl4_totassets_high)` | TOP500 | 0.15 | 0.07 | 46.9% | 60% | bull-only |
| `rank(ts_delta(anl4_totassets_high, 5))` | TOP500 | 0.15 | 0.03 | 17.1% | 60% | mixed |

## Correlation Notes
Top correlates:
- anl4_totassets_median: 1.000 (strongly positively correlated)
- anl4_totassets_mean: 1.000 (strongly positively correlated)
- anl4_totassets_low: 0.999 (strongly positively correlated)
- est_tot_assets: 0.978 (strongly positively correlated)
- anl4_totassets_value: 0.971 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
