---
field: anl4_totassets_low
dataset: analyst4
best_template: rank_value_norm
best_sharpe: 0.77
best_fitness: 0.54
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 9
max_drawdown: 0.0843
ann_vol: 0.0793
hit_rate: 0.4883
rolling_sharpe_min: -0.801
rolling_sharpe_max: 2.474
redundancy_cluster: 1
negated_best_sharpe: 0.24
negated_best_template: neg_rank_level
negated_best_fitness: 0.13
n_negated_sims: 10
direction_gap: -0.53
---
# anl4_totassets_low (analyst4)

*Total Assets - The lowest estimation*

## Signal Profile
- `rank(anl4_totassets_low)`: S=0.64, F=0.48, T=1.1%, INFERIOR (TOP3000)
- `rank(anl4_totassets_low / close)`: S=0.77, F=0.54, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_delta(anl4_totassets_low, 5))`: S=0.86, F=0.27, T=36.8%, INFERIOR (TOP3000)
- `-rank(anl4_totassets_low)`: S=-0.25, F=-0.13, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_totassets_low, 5))`: S=-0.43, F=-0.16, T=34.7%, INFERIOR (TOP3000)
- `ts_zscore(anl4_totassets_low, 22)`: S=0.86, F=0.39, T=35.5%, INFERIOR (TOP3000)
- `ts_mean(anl4_totassets_low, 10)`: S=-0.12, F=-0.04, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_totassets_low, 22))`: S=-0.35, F=-0.11, T=13.7%, INFERIOR (TOP3000)
- `rank(-1 * anl4_totassets_low)`: S=0.24, F=0.13, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * anl4_totassets_low / close)`: S=0.07, F=0.02, T=2.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 8F/24P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 17F/3P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.76, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.20 (weak), ret=+1.1%
  - 2020: S=0.08 (weak), ret=+0.8%
  - 2021: S=1.53 (strong), ret=+14.8%
  - 2022: S=1.04 (moderate), ret=+7.0%
  - 2023: S=1.03 (moderate), ret=+5.8%

## Risk & Drawdown
- Max drawdown: 8.43% over 281 days (recovered)
- Annualized: return +6.0%, volatility 7.9% (fraction of booksize)
- Hit rate: 48.8% positive days
- Tail shape: skew +0.71, excess kurtosis +3.28

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.80, max 2.47, latest 1.15

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2020
Best month: +8.00%; worst month: -3.26%
Positive months: 54%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.66
- Sideways: S=0.29
- Bear: S=-1.06

## Negated Direction
Best negated: `rank(-1 * anl4_totassets_low)` S=0.24, F=0.13, INFERIOR
Direction gap: -0.53 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * anl4_totassets_low)`: S=0.24, F=0.13, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * anl4_totassets_low / close)`: S=0.07, F=0.02, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_totassets_low, 5))`: S=-0.43, F=-0.16, T=34.7%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_totassets_low / close)` | TOP3000 | 0.76 | 0.54 | 8.4% | 100% | bull-only |
| `rank(anl4_totassets_low)` | TOP3000 | 0.63 | 0.48 | 29.8% | 80% | bull-only |
| `rank(ts_delta(anl4_totassets_low, 5))` | TOP3000 | 0.86 | 0.27 | 6.0% | 100% | mixed |
| `rank(ts_delta(anl4_totassets_low, 5))` | TOP1000 | 0.74 | 0.24 | 7.8% | 80% | mixed |
| `rank(anl4_totassets_low / close)` | TOP1000 | 0.37 | 0.20 | 14.1% | 80% | bull-only |
| `rank(ts_delta(anl4_totassets_low, 5))` | TOP200 | 0.43 | 0.16 | 15.1% | 40% | mixed |
| `rank(anl4_totassets_low)` | TOP1000 | 0.25 | 0.13 | 33.5% | 60% | bull-only |
| `rank(anl4_totassets_low / close)` | TOP500 | 0.19 | 0.08 | 29.3% | 80% | bull-only |
| `rank(anl4_totassets_low)` | TOP500 | 0.12 | 0.05 | 47.9% | 60% | bull-only |

## Correlation Notes
Top correlates:
- anl4_totassets_median: 1.000 (strongly positively correlated)
- anl4_totassets_mean: 1.000 (strongly positively correlated)
- anl4_totassets_high: 0.999 (strongly positively correlated)
- est_tot_assets: 0.978 (strongly positively correlated)
- anl4_totassets_value: 0.971 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
