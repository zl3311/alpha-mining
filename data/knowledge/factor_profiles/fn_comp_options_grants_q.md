---
field: fn_comp_options_grants_q
dataset: fundamental2
best_template: rank_value_norm
best_sharpe: 0.57
best_fitness: 0.42
best_universe: TOP200
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 6
max_drawdown: 0.1681
ann_vol: 0.116
hit_rate: 0.5101
rolling_sharpe_min: -0.553
rolling_sharpe_max: 1.67
negated_best_sharpe: 0.17
negated_best_template: rank_neg_delta
negated_best_fitness: 0.08
n_negated_sims: 10
direction_gap: -0.4
---
# fn_comp_options_grants_q (fundamental2)

*Net number of share options (or share units) granted during the period.*

## Signal Profile
- `rank(fn_comp_options_grants_q)`: S=0.42, F=0.25, T=2.4%, INFERIOR (TOP200)
- `rank(fn_comp_options_grants_q / close)`: S=0.57, F=0.42, T=2.6%, INFERIOR (TOP200)
- `rank(ts_delta(fn_comp_options_grants_q, 5))`: S=-0.43, F=-0.21, T=35.1%, INFERIOR (TOP3000)
- `-rank(fn_comp_options_grants_q)`: S=-0.24, F=-0.07, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_comp_options_grants_q, 5))`: S=0.17, F=0.08, T=20.8%, INFERIOR (TOP3000)
- `-ts_zscore(fn_comp_options_grants_q, 63)`: S=0.09, F=0.05, T=13.8%, INFERIOR (TOP3000)
- `ts_mean(fn_comp_options_grants_q, 10)`: S=-0.10, F=-0.07, T=2.7%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_comp_options_grants_q, 22))`: S=-0.09, F=-0.03, T=17.7%, INFERIOR (TOP3000)
- `rank(-1 * fn_comp_options_grants_q)`: S=-0.42, F=-0.25, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * fn_comp_options_grants_q / close)`: S=-0.57, F=-0.42, T=2.6%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 13F/19P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 12F/8P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.59, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.83 (moderate), ret=+7.0%
  - 2020: S=0.11 (weak), ret=+1.3%
  - 2021: S=0.97 (moderate), ret=+12.0%
  - 2022: S=0.28 (weak), ret=+3.0%
  - 2023: S=0.82 (moderate), ret=+10.3%

## Risk & Drawdown
- Max drawdown: 16.81% over 169 days (not yet recovered, ongoing at window end)
- Annualized: return +6.9%, volatility 11.6% (fraction of booksize)
- Hit rate: 51.0% positive days
- Tail shape: skew +0.27, excess kurtosis +1.17

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.55, max 1.67, latest 0.87

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2020
Best month: +11.06%; worst month: -9.38%
Positive months: 61%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.19
- Sideways: S=0.16
- Bear: S=1.35

## Negated Direction
Best negated: `rank(-1 * ts_delta(fn_comp_options_grants_q, 5))` S=0.17, F=0.08, INFERIOR
Direction gap: -0.40 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fn_comp_options_grants_q)`: S=-0.42, F=-0.25, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * fn_comp_options_grants_q / close)`: S=-0.57, F=-0.42, T=2.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_comp_options_grants_q, 5))`: S=0.17, F=0.08, T=20.8%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fn_comp_options_grants_q / close)` | TOP200 | 0.59 | 0.42 | 16.8% | 100% | mixed |
| `rank(fn_comp_options_grants_q)` | TOP200 | 0.43 | 0.25 | 14.3% | 80% | all-weather |
| `rank(fn_comp_options_grants_q / close)` | TOP500 | 0.42 | 0.20 | 8.4% | 80% | mixed |
| `rank(fn_comp_options_grants_q / close)` | TOP1000 | 0.46 | 0.20 | 9.2% | 60% | mixed |
| `rank(fn_comp_options_grants_q)` | TOP1000 | 0.24 | 0.07 | 9.1% | 60% | bull-only |
| `rank(fn_comp_options_grants_q)` | TOP3000 | 0.12 | 0.02 | 9.6% | 80% | mixed |

## Correlation Notes
Top correlates:
- fnd6_cshtrq: 0.493 (moderately positively correlated)
- anl4_epsa_flag: 0.450 (moderately positively correlated)
- news_mov_vol: 0.420 (moderately positively correlated)
- volume: 0.419 (moderately positively correlated)
- anl4_afv4_eps_number: 0.417 (moderately positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
