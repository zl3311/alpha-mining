---
field: anl4_bvps_number
dataset: analyst4
best_template: rank_neg_delta
best_sharpe: 0.87
best_fitness: 0.61
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 5
max_drawdown: 0.2751
ann_vol: 0.1583
hit_rate: 0.5093
rolling_sharpe_min: -1.678
rolling_sharpe_max: 1.934
negated_best_sharpe: 0.87
negated_best_template: rank_neg_delta
negated_best_fitness: 0.61
n_negated_sims: 10
direction_gap: 0.25
---
# anl4_bvps_number (analyst4)

*Book value per share - number of estimations*

## Signal Profile
- `rank(anl4_bvps_number)`: S=0.53, F=0.19, T=2.8%, INFERIOR (TOP3000)
- `rank(anl4_bvps_number / close)`: S=0.30, F=0.15, T=2.2%, INFERIOR (TOP3000)
- `rank(ts_delta(anl4_bvps_number, 5))`: S=0.45, F=0.21, T=34.1%, INFERIOR (TOP500)
- `-rank(anl4_bvps_number)`: S=0.09, F=0.02, T=3.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_bvps_number, 5))`: S=0.87, F=0.61, T=34.8%, INFERIOR (TOP3000)
- `ts_zscore(anl4_bvps_number, 22)`: S=0.62, F=0.33, T=33.5%, INFERIOR (TOP3000)
- `ts_mean(anl4_bvps_number, 10)`: S=0.20, F=0.06, T=3.4%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_bvps_number, 22))`: S=0.58, F=0.31, T=14.2%, INFERIOR (TOP3000)
- `rank(-1 * anl4_bvps_number)`: S=0.66, F=0.49, T=4.2%, INFERIOR (TOP3000)
- `rank(-1 * anl4_bvps_number / close)`: S=0.26, F=0.12, T=3.0%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 10F/22P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 7F/13P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.45, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.80 (moderate), ret=+8.7%
  - 2020: S=-1.25 (negative), ret=-17.2%
  - 2021: S=0.73 (moderate), ret=+10.3%
  - 2022: S=-0.57 (negative), ret=-8.5%
  - 2023: S=1.92 (strong), ret=+41.8%

## Risk & Drawdown
- Max drawdown: 27.51% over 1220 days (recovered)
- Annualized: return +7.2%, volatility 15.8% (fraction of booksize)
- Hit rate: 50.9% positive days
- Tail shape: skew +1.33, excess kurtosis +18.36

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.68, max 1.93, latest 1.89

## Yearly & Monthly Returns
Best year (by Sharpe): 2023; worst year: 2020
Best month: +27.11%; worst month: -6.55%
Positive months: 51%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.92
- Sideways: S=0.66
- Bear: S=-0.39

## Negated Direction
Best negated: `rank(-1 * ts_delta(anl4_bvps_number, 5))` S=0.87, F=0.61, INFERIOR
Direction gap: +0.25 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * anl4_bvps_number)`: S=0.66, F=0.49, T=4.2%, INFERIOR (TOP3000)
- `rank(-1 * anl4_bvps_number / close)`: S=0.26, F=0.12, T=3.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_bvps_number, 5))`: S=0.87, F=0.61, T=34.8%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(anl4_bvps_number, 5))` | TOP500 | 0.45 | 0.21 | 27.5% | 60% | mixed |
| `rank(anl4_bvps_number)` | TOP3000 | 0.54 | 0.19 | 4.4% | 80% | all-weather |
| `rank(anl4_bvps_number / close)` | TOP3000 | 0.31 | 0.15 | 25.0% | 40% | bear-only |
| `rank(anl4_bvps_number / close)` | TOP500 | 0.23 | 0.09 | 19.8% | 40% | mixed |
| `rank(anl4_bvps_number / close)` | TOP1000 | 0.12 | 0.03 | 24.3% | 40% | mixed |

## Correlation Notes
Top correlates:
- fnd2_a_gwllimrml: 0.254 (weakly positively correlated)
- news_mins_20_pct_dn: 0.134 (weakly positively correlated)
- fnd2_propplteqflublgland: 0.134 (weakly positively correlated)
- dividend_min_guidance_quarterly: -0.123 (weakly negatively correlated)
- dividend_max_guidance_quarterly: -0.123 (weakly negatively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
