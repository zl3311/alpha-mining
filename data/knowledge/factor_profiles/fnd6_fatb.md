---
field: fnd6_fatb
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 0.61
best_fitness: 0.46
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 5
max_drawdown: 0.2536
ann_vol: 0.116
hit_rate: 0.4996
rolling_sharpe_min: -2.514
rolling_sharpe_max: 2.568
redundancy_cluster: 13
negated_best_sharpe: 0.4
negated_best_template: rank_neg_delta
negated_best_fitness: 0.2
n_negated_sims: 10
direction_gap: -0.21
---
# fnd6_fatb (fundamental6)

*Plant, Property and Equipment at Cost - Buildings*

## Signal Profile
- `rank(fnd6_fatb)`: S=0.45, F=0.31, T=1.9%, INFERIOR (TOP3000)
- `rank(fnd6_fatb / close)`: S=0.61, F=0.46, T=2.0%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_fatb, 5))`: S=-0.01, F=0.00, T=37.5%, INFERIOR (TOP1000)
- `-rank(fnd6_fatb)`: S=-0.26, F=-0.15, T=2.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_fatb, 5))`: S=0.40, F=0.20, T=31.0%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_fatb, 22)`: S=0.29, F=0.15, T=19.0%, INFERIOR (TOP3000)
- `ts_mean(fnd6_fatb, 10)`: S=0.19, F=0.08, T=1.8%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_fatb, 22))`: S=0.35, F=0.17, T=20.3%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_fatb)`: S=-0.02, F=0.00, T=3.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_fatb / close)`: S=-0.07, F=-0.02, T=3.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 22F/7P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.60, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.45 (negative), ret=-2.3%
  - 2020: S=-2.01 (negative), ret=-16.0%
  - 2021: S=1.63 (strong), ret=+23.5%
  - 2022: S=1.48 (moderate), ret=+24.7%
  - 2023: S=0.52 (moderate), ret=+4.4%

## Risk & Drawdown
- Max drawdown: 25.36% over 1040 days (recovered)
- Annualized: return +7.0%, volatility 11.6% (fraction of booksize)
- Hit rate: 50.0% positive days
- Tail shape: skew +0.02, excess kurtosis +2.11

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.51, max 2.57, latest 0.31

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2020
Best month: +10.07%; worst month: -4.79%
Positive months: 52%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.07
- Sideways: S=0.63
- Bear: S=-2.75

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_fatb, 5))` S=0.40, F=0.20, INFERIOR
Direction gap: -0.21 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_fatb)`: S=-0.02, F=0.00, T=3.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_fatb / close)`: S=-0.07, F=-0.02, T=3.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_fatb, 5))`: S=0.40, F=0.20, T=31.0%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_fatb / close)` | TOP3000 | 0.60 | 0.46 | 25.4% | 60% | bull-only |
| `rank(fnd6_fatb)` | TOP3000 | 0.45 | 0.31 | 38.2% | 60% | bull-only |
| `rank(fnd6_fatb / close)` | TOP1000 | 0.32 | 0.21 | 30.2% | 40% | bull-only |
| `rank(fnd6_fatb)` | TOP1000 | 0.25 | 0.15 | 41.9% | 40% | bull-only |
| `rank(fnd6_fatb / close)` | TOP500 | 0.06 | 0.02 | 50.0% | 40% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_fatp: 0.962 (strongly positively correlated)
- fnd6_newa1v1300_ebitda: 0.942 (strongly positively correlated)
- fnd6_newa2v1300_oibdp: 0.942 (strongly positively correlated)
- ebitda: 0.942 (strongly positively correlated)
- operating_profit_before_depr_amort: 0.936 (strongly positively correlated)

Redundancy cluster #13: 127 similar fields, mean |rho| 0.82 (representative: anl4_bvps_flag). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
