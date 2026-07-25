---
field: fnd6_cshtrq
dataset: fundamental6
best_template: ts_zscore
best_sharpe: 0.82
best_fitness: 0.49
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 8
max_drawdown: 0.2046
ann_vol: 0.0952
hit_rate: 0.5012
rolling_sharpe_min: -1.473
rolling_sharpe_max: 2.151
negated_best_sharpe: 0.72
negated_best_template: rank_neg_delta
negated_best_fitness: 0.48
n_negated_sims: 10
direction_gap: -0.1
---
# fnd6_cshtrq (fundamental6)

*Common Shares Traded - Quarter*

## Signal Profile
- `rank(fnd6_cshtrq)`: S=0.35, F=0.17, T=2.1%, INFERIOR (TOP200)
- `rank(fnd6_cshtrq / close)`: S=0.35, F=0.18, T=2.2%, INFERIOR (TOP200)
- `rank(ts_delta(fnd6_cshtrq, 5))`: S=-0.19, F=-0.06, T=24.1%, INFERIOR (TOP500)
- `-rank(fnd6_cshtrq)`: S=-0.21, F=-0.07, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_cshtrq, 5))`: S=0.72, F=0.48, T=31.1%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_cshtrq, 63)`: S=0.82, F=0.49, T=8.8%, INFERIOR (TOP3000)
- `ts_mean(fnd6_cshtrq, 10)`: S=0.21, F=0.09, T=1.7%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_cshtrq, 22))`: S=-1.00, F=-0.71, T=10.6%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_cshtrq)`: S=-0.36, F=-0.16, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_cshtrq / close)`: S=-0.12, F=-0.04, T=1.6%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 10F/22P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 7F/22P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.36, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.71 (moderate), ret=+3.7%
  - 2020: S=0.91 (moderate), ret=+9.1%
  - 2021: S=-0.35 (negative), ret=-4.4%
  - 2022: S=-0.04 (negative), ret=-0.4%
  - 2023: S=1.20 (moderate), ret=+9.0%

## Risk & Drawdown
- Max drawdown: 20.46% over 1019 days (not yet recovered, ongoing at window end)
- Annualized: return +3.5%, volatility 9.5% (fraction of booksize)
- Hit rate: 50.1% positive days
- Tail shape: skew +0.32, excess kurtosis +2.06

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.47, max 2.15, latest 1.28

## Yearly & Monthly Returns
Best year (by Sharpe): 2023; worst year: 2021
Best month: +11.18%; worst month: -5.96%
Positive months: 54%

## Regime Profile
Regime profile: **mixed**
- Bull: S=-0.16
- Sideways: S=-0.60
- Bear: S=1.76

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_cshtrq, 5))` S=0.72, F=0.48, INFERIOR
Direction gap: -0.10 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_cshtrq)`: S=-0.36, F=-0.16, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_cshtrq / close)`: S=-0.12, F=-0.04, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_cshtrq, 5))`: S=0.72, F=0.48, T=31.1%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_cshtrq / close)` | TOP200 | 0.36 | 0.18 | 20.5% | 60% | mixed |
| `rank(fnd6_cshtrq)` | TOP200 | 0.37 | 0.17 | 18.8% | 60% | mixed |
| `rank(fnd6_cshtrq)` | TOP3000 | 0.36 | 0.16 | 19.3% | 60% | bear-only |
| `rank(fnd6_cshtrq)` | TOP500 | 0.23 | 0.08 | 16.4% | 40% | bear-only |
| `rank(fnd6_cshtrq / close)` | TOP500 | 0.19 | 0.07 | 26.9% | 80% | bear-only |
| `rank(fnd6_cshtrq)` | TOP1000 | 0.21 | 0.07 | 21.9% | 80% | bear-only |
| `rank(fnd6_cshtrq / close)` | TOP1000 | 0.15 | 0.05 | 33.9% | 40% | bear-only |
| `rank(fnd6_cshtrq / close)` | TOP3000 | 0.12 | 0.04 | 43.2% | 60% | bear-only |

## Correlation Notes
Top correlates:
- anl4_epsa_flag: 0.920 (strongly positively correlated)
- volume: 0.876 (strongly positively correlated)
- news_mov_vol: 0.859 (strongly positively correlated)
- anl4_afv4_eps_number: 0.806 (strongly positively correlated)
- fn_antidilutive_securities_excl_from_eps_a: 0.777 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
