---
field: volume
dataset: pv1
best_template: rank_level
best_sharpe: 0.48
best_fitness: 0.28
best_universe: TOP200
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 21
regime_profile: all-weather
n_variations_with_pnl: 7
max_drawdown: 0.1638
ann_vol: 0.0887
hit_rate: 0.498
rolling_sharpe_min: -1.372
rolling_sharpe_max: 2.166
negated_best_sharpe: 0.14
negated_best_template: rank_neg_delta
negated_best_fitness: 0.02
n_negated_sims: 4
direction_gap: -0.34
---
# volume (pv1)

*Daily volume*

## Signal Profile
- `rank(volume)`: S=0.48, F=0.28, T=8.9%, INFERIOR (TOP200)
- `rank(volume / close)`: S=0.15, F=0.05, T=6.3%, INFERIOR (TOP3000)
- `rank(ts_delta(volume, 5))`: S=0.33, F=0.08, T=56.3%, INFERIOR (TOP200)
- `-rank(volume)`: S=-0.30, F=-0.13, T=10.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(volume, 5))`: S=0.14, F=0.02, T=57.0%, INFERIOR (TOP3000)
- `ts_zscore(volume, 22)`: S=0.45, F=0.12, T=44.1%, INFERIOR (TOP3000)
- `ts_mean(volume, 10)`: S=-0.03, F=-0.01, T=5.6%, INFERIOR (TOP3000)
- `rank(ts_rank(volume, 22))`: S=0.51, F=0.13, T=44.5%, INFERIOR (TOP3000)
- `rank(-1 * volume)`: S=-0.46, F=-0.24, T=9.1%, INFERIOR (TOP3000)
- `rank(-1 * volume / close)`: S=-0.14, F=-0.05, T=6.8%, INFERIOR (TOP3000)

## Check Summary
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 21F/0P
- LOW_SUB_UNIVERSE_SHARPE: 6F/13P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.49, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.88 (moderate), ret=+4.7%
  - 2020: S=0.41 (weak), ret=+3.8%
  - 2021: S=-0.16 (negative), ret=-1.9%
  - 2022: S=0.32 (weak), ret=+2.8%
  - 2023: S=1.92 (strong), ret=+11.7%

## Risk & Drawdown
- Max drawdown: 16.38% over 1019 days (not yet recovered, ongoing at window end)
- Annualized: return +4.3%, volatility 8.9% (fraction of booksize)
- Hit rate: 49.8% positive days
- Tail shape: skew +0.36, excess kurtosis +2.59

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.37, max 2.17, latest 1.99

## Yearly & Monthly Returns
Best year (by Sharpe): 2023; worst year: 2021
Best month: +9.12%; worst month: -4.13%
Positive months: 56%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=0.56
- Sideways: S=-0.53
- Bear: S=1.22

## Negated Direction
Best negated: `rank(-1 * ts_delta(volume, 5))` S=0.14, F=0.02, INFERIOR
Direction gap: -0.34 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * volume)`: S=-0.46, F=-0.24, T=9.1%, INFERIOR (TOP3000)
- `rank(-1 * volume / close)`: S=-0.14, F=-0.05, T=6.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(volume, 5))`: S=0.14, F=0.02, T=57.0%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(volume)` | TOP200 | 0.49 | 0.28 | 16.4% | 80% | all-weather |
| `rank(volume)` | TOP3000 | 0.47 | 0.24 | 16.0% | 60% | mixed |
| `rank(volume)` | TOP500 | 0.32 | 0.15 | 17.4% | 80% | mixed |
| `rank(volume)` | TOP1000 | 0.30 | 0.13 | 22.0% | 80% | bear-only |
| `rank(ts_delta(volume, 5))` | TOP200 | 0.32 | 0.08 | 17.8% | 80% | mixed |
| `rank(ts_delta(volume, 5))` | TOP500 | 0.28 | 0.05 | 17.3% | 60% | bull-only |
| `rank(ts_delta(volume, 5))` | TOP1000 | 0.25 | 0.04 | 12.7% | 60% | mixed |

## Correlation Notes
Top correlates:
- news_mov_vol: 0.901 (strongly positively correlated)
- fnd6_cshtrq: 0.876 (strongly positively correlated)
- news_curr_vol: 0.871 (strongly positively correlated)
- anl4_epsa_flag: 0.785 (strongly positively correlated)
- fn_antidilutive_securities_excl_from_eps_a: 0.682 (moderately positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
