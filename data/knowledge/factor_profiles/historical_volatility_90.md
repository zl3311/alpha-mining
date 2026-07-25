---
field: historical_volatility_90
dataset: option8
best_template: ts_zscore
best_sharpe: 0.72
best_fitness: 0.32
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 27
regime_profile: all-weather
n_variations_with_pnl: 6
max_drawdown: 0.0882
ann_vol: 0.0632
hit_rate: 0.5166
rolling_sharpe_min: -1.545
rolling_sharpe_max: 2.586
top_merge_partner: unsystematic_risk_last_90_days
redundancy_cluster: 48
negated_best_sharpe: 0.03
negated_best_template: neg_rank_level
negated_best_fitness: 0.01
n_negated_sims: 10
direction_gap: -0.69
---
# historical_volatility_90 (option8)

*Historical close-to-close volatility for approximately 90 calendar days*

## Signal Profile
- `rank(historical_volatility_90)`: S=0.13, F=0.06, T=6.2%, INFERIOR (TOP200)
- `rank(historical_volatility_90 / close)`: S=0.03, F=0.01, T=3.8%, INFERIOR (TOP3000)
- `rank(ts_delta(historical_volatility_90, 5))`: S=0.79, F=0.31, T=33.3%, INFERIOR (TOP3000)
- `-rank(historical_volatility_90)`: S=-0.06, F=-0.02, T=5.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(historical_volatility_90, 5))`: S=-0.79, F=-0.31, T=33.3%, INFERIOR (TOP3000)
- `ts_zscore(historical_volatility_90, 22)`: S=0.72, F=0.32, T=23.1%, INFERIOR (TOP3000)
- `ts_mean(historical_volatility_90, 10)`: S=-0.22, F=-0.15, T=3.8%, INFERIOR (TOP3000)
- `rank(ts_rank(historical_volatility_90, 22))`: S=0.62, F=0.24, T=26.0%, INFERIOR (TOP3000)
- `rank(-1 * historical_volatility_90)`: S=0.03, F=0.01, T=4.6%, INFERIOR (TOP3000)
- `rank(-1 * historical_volatility_90 / close)`: S=0.05, F=0.01, T=3.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 26F/1P
- LOW_FITNESS: 27F/0P
- LOW_SHARPE: 27F/0P
- LOW_SUB_UNIVERSE_SHARPE: 11F/14P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.80, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.17 (weak), ret=+0.5%
  - 2020: S=0.72 (moderate), ret=+6.0%
  - 2021: S=1.16 (moderate), ret=+6.5%
  - 2022: S=1.84 (strong), ret=+13.8%
  - 2023: S=-0.46 (negative), ret=-2.0%

## Risk & Drawdown
- Max drawdown: 8.82% over 392 days (recovered)
- Annualized: return +5.1%, volatility 6.3% (fraction of booksize)
- Hit rate: 51.7% positive days
- Tail shape: skew +0.74, excess kurtosis +6.04

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.54, max 2.59, latest -0.32

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2023
Best month: +6.11%; worst month: -3.43%
Positive months: 64%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=1.30
- Sideways: S=-0.79
- Bear: S=1.48

## Negated Direction
Best negated: `rank(-1 * historical_volatility_90)` S=0.03, F=0.01, INFERIOR
Direction gap: -0.69 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * historical_volatility_90)`: S=0.03, F=0.01, T=4.6%, INFERIOR (TOP3000)
- `rank(-1 * historical_volatility_90 / close)`: S=0.05, F=0.01, T=3.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(historical_volatility_90, 5))`: S=-0.79, F=-0.31, T=33.3%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(historical_volatility_90, 5))` | TOP3000 | 0.80 | 0.31 | 8.8% | 80% | all-weather |
| `rank(ts_delta(historical_volatility_90, 5))` | TOP1000 | 0.55 | 0.19 | 11.1% | 60% | all-weather |
| `rank(ts_delta(historical_volatility_90, 5))` | TOP500 | 0.35 | 0.10 | 14.8% | 60% | all-weather |
| `rank(historical_volatility_90)` | TOP500 | 0.14 | 0.06 | 67.3% | 60% | bear-only |
| `rank(historical_volatility_90)` | TOP200 | 0.14 | 0.06 | 68.3% | 60% | bear-only |
| `rank(ts_delta(historical_volatility_90, 5))` | TOP200 | 0.17 | 0.05 | 19.2% | 40% | all-weather |

## Correlation Notes
Top correlates:
- parkinson_volatility_90: 0.870 (strongly positively correlated)
- parkinson_volatility_120: 0.684 (moderately positively correlated)
- historical_volatility_120: 0.653 (moderately positively correlated)
- historical_volatility_10 - historical_volatility_180: 0.614 (moderately positively correlated)
- historical_volatility_60: 0.594 (moderately positively correlated)

Redundancy cluster #48: 4 similar fields, mean |rho| 0.738 (representative: parkinson_volatility_120). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| unsystematic_risk_last_90_days | model51 | -0.30 | 1.77 | +0.45 | +0.73 | yes |
| cashflow_per_share_minimum | analyst4 | -0.17 | 1.25 | +0.40 | -0.40 | yes |
| unsystematic_risk_last_60_days | model51 | -0.22 | 1.45 | +0.43 | +0.81 | yes |
| anl4_gric_std | analyst4 | -0.17 | 1.28 | +0.42 | +0.59 | yes |
| fnd6_newqv1300_miiq | fundamental6 | -0.16 | 1.29 | +0.42 | +0.32 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
