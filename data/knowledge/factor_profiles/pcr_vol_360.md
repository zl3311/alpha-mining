---
field: pcr_vol_360
dataset: option9
best_template: rank_level
best_sharpe: 0.72
best_fitness: 0.2
best_universe: TOP500
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 21
regime_profile: mixed
n_variations_with_pnl: 4
max_drawdown: 0.0933
ann_vol: 0.0536
hit_rate: 0.5336
rolling_sharpe_min: -1.715
rolling_sharpe_max: 2.949
negated_best_sharpe: -0.38
negated_best_template: neg_rank_value_norm
negated_best_fitness: -0.07
n_negated_sims: 4
direction_gap: -1.1
---
# pcr_vol_360 (option9)

*Ratio of put volume to call volume on a stock's options with expiration 360 days in the future*

## Signal Profile
- `rank(pcr_vol_360)`: S=0.72, F=0.20, T=49.7%, INFERIOR (TOP500)
- `rank(pcr_vol_360 / close)`: S=0.32, F=0.07, T=46.5%, INFERIOR (TOP3000)
- `rank(ts_delta(pcr_vol_360, 5))`: S=0.95, F=0.16, T=85.9%, INFERIOR (TOP3000)
- `-rank(pcr_vol_360)`: S=-0.74, F=-0.18, T=48.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(pcr_vol_360, 5))`: S=-0.95, F=-0.16, T=85.9%, INFERIOR (TOP3000)
- `ts_zscore(pcr_vol_360, 22)`: S=0.27, F=0.03, T=60.0%, INFERIOR (TOP3000)
- `ts_mean(pcr_vol_360, 10)`: S=-0.10, F=-0.02, T=18.6%, INFERIOR (TOP3000)
- `rank(ts_rank(pcr_vol_360, 22))`: S=0.76, F=0.15, T=66.0%, INFERIOR (TOP3000)
- `rank(-1 * pcr_vol_360)`: S=-0.58, F=-0.12, T=56.2%, INFERIOR (TOP3000)
- `rank(-1 * pcr_vol_360 / close)`: S=-0.38, F=-0.07, T=58.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 21F/0P
- HIGH_TURNOVER: 7F/14P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 21F/0P
- LOW_SUB_UNIVERSE_SHARPE: 8F/11P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.71, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.42 (weak), ret=+1.4%
  - 2020: S=-0.74 (negative), ret=-3.1%
  - 2021: S=1.79 (strong), ret=+15.5%
  - 2022: S=0.89 (moderate), ret=+4.0%
  - 2023: S=0.20 (weak), ret=+0.8%

## Risk & Drawdown
- Max drawdown: 9.33% over 226 days (recovered)
- Annualized: return +3.8%, volatility 5.4% (fraction of booksize)
- Hit rate: 53.4% positive days
- Tail shape: skew +0.32, excess kurtosis +4.14

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.72, max 2.95, latest 0.16

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2020
Best month: +4.07%; worst month: -4.98%
Positive months: 59%

## Regime Profile
Regime profile: **mixed**
- Bull: S=1.96
- Sideways: S=0.15
- Bear: S=-0.43

## Negated Direction
Best negated: `rank(-1 * pcr_vol_360 / close)` S=-0.38, F=-0.07, INFERIOR
Direction gap: -1.10 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * pcr_vol_360)`: S=-0.58, F=-0.12, T=56.2%, INFERIOR (TOP3000)
- `rank(-1 * pcr_vol_360 / close)`: S=-0.38, F=-0.07, T=58.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(pcr_vol_360, 5))`: S=-0.95, F=-0.16, T=85.9%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(pcr_vol_360)` | TOP500 | 0.71 | 0.20 | 9.3% | 80% | mixed |
| `rank(pcr_vol_360)` | TOP1000 | 0.72 | 0.18 | 6.6% | 80% | mixed |
| `rank(ts_delta(pcr_vol_360, 5))` | TOP3000 | 0.95 | 0.16 | 5.4% | 60% | all-weather |
| `rank(pcr_vol_360)` | TOP3000 | 0.58 | 0.12 | 5.0% | 80% | mixed |

## Correlation Notes
Top correlates:
- min_free_cashflow_per_share_guidance: 0.588 (moderately positively correlated)
- shareholders_equity_min_guidance: 0.588 (moderately positively correlated)
- min_total_assets_guidance: 0.588 (moderately positively correlated)
- max_free_cashflow_per_share_guidance: 0.588 (moderately positively correlated)
- shareholders_equity_max_guidance: 0.588 (moderately positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
