---
field: anl4_totassets_median
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
max_drawdown: 0.0838
ann_vol: 0.0789
hit_rate: 0.485
rolling_sharpe_min: -0.817
rolling_sharpe_max: 2.486
redundancy_cluster: 1
negated_best_sharpe: 0.21
negated_best_template: rank_neg_delta
negated_best_fitness: 0.04
n_negated_sims: 10
direction_gap: -0.56
---
# anl4_totassets_median (analyst4)

*Total Assets - median of estimations*

## Signal Profile
- `rank(anl4_totassets_median)`: S=0.64, F=0.48, T=1.1%, INFERIOR (TOP3000)
- `rank(anl4_totassets_median / close)`: S=0.77, F=0.54, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_delta(anl4_totassets_median, 5))`: S=0.85, F=0.26, T=36.6%, INFERIOR (TOP3000)
- `-rank(anl4_totassets_median)`: S=-0.27, F=-0.14, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_totassets_median, 5))`: S=0.21, F=0.04, T=37.1%, INFERIOR (TOP3000)
- `ts_zscore(anl4_totassets_median, 22)`: S=0.34, F=0.10, T=35.1%, INFERIOR (TOP3000)
- `ts_mean(anl4_totassets_median, 10)`: S=-0.10, F=-0.03, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_totassets_median, 22))`: S=-0.36, F=-0.11, T=13.8%, INFERIOR (TOP3000)
- `rank(-1 * anl4_totassets_median)`: S=-0.15, F=-0.06, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * anl4_totassets_median / close)`: S=-0.21, F=-0.09, T=2.0%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 5F/27P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 20F/9P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.77, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.24 (weak), ret=+1.3%
  - 2020: S=0.10 (weak), ret=+1.0%
  - 2021: S=1.54 (strong), ret=+14.8%
  - 2022: S=1.00 (moderate), ret=+6.7%
  - 2023: S=1.05 (moderate), ret=+5.9%

## Risk & Drawdown
- Max drawdown: 8.38% over 203 days (recovered)
- Annualized: return +6.1%, volatility 7.9% (fraction of booksize)
- Hit rate: 48.5% positive days
- Tail shape: skew +0.72, excess kurtosis +3.27

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.82, max 2.49, latest 1.16

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2020
Best month: +7.95%; worst month: -3.33%
Positive months: 56%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.63
- Sideways: S=0.31
- Bear: S=-1.01

## Negated Direction
Best negated: `rank(-1 * ts_delta(anl4_totassets_median, 5))` S=0.21, F=0.04, INFERIOR
Direction gap: -0.56 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * anl4_totassets_median)`: S=-0.15, F=-0.06, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * anl4_totassets_median / close)`: S=-0.21, F=-0.09, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_totassets_median, 5))`: S=0.21, F=0.04, T=37.1%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_totassets_median / close)` | TOP3000 | 0.77 | 0.54 | 8.4% | 100% | bull-only |
| `rank(anl4_totassets_median)` | TOP3000 | 0.63 | 0.48 | 29.6% | 80% | bull-only |
| `rank(ts_delta(anl4_totassets_median, 5))` | TOP3000 | 0.85 | 0.26 | 6.0% | 100% | mixed |
| `rank(anl4_totassets_median / close)` | TOP1000 | 0.38 | 0.21 | 13.7% | 80% | bull-only |
| `rank(anl4_totassets_median)` | TOP1000 | 0.26 | 0.14 | 32.6% | 60% | bull-only |
| `rank(ts_delta(anl4_totassets_median, 5))` | TOP1000 | 0.46 | 0.11 | 10.6% | 60% | mixed |
| `rank(ts_delta(anl4_totassets_median, 5))` | TOP200 | 0.32 | 0.10 | 17.4% | 80% | mixed |
| `rank(anl4_totassets_median / close)` | TOP500 | 0.20 | 0.09 | 28.9% | 80% | bull-only |
| `rank(anl4_totassets_median)` | TOP500 | 0.14 | 0.06 | 47.4% | 60% | bull-only |

## Correlation Notes
Top correlates:
- anl4_totassets_mean: 1.000 (strongly positively correlated)
- anl4_totassets_high: 1.000 (strongly positively correlated)
- anl4_totassets_low: 1.000 (strongly positively correlated)
- est_tot_assets: 0.978 (strongly positively correlated)
- anl4_totassets_value: 0.971 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
