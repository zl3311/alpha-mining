---
field: pv13_revere_zipcode
dataset: pv13
best_template: rank_delta
best_sharpe: 0.77
best_fitness: 0.55
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 24
regime_profile: all-weather
n_variations_with_pnl: 2
max_drawdown: 0.2463
ann_vol: 0.212
hit_rate: 0.5166
rolling_sharpe_min: -0.998
rolling_sharpe_max: 1.96
negated_best_sharpe: 0.4
negated_best_template: rank_neg_delta
negated_best_fitness: 0.3
n_negated_sims: 10
direction_gap: -0.37
---
# pv13_revere_zipcode (pv13)

*Zip code*

## Signal Profile
- `rank(pv13_revere_zipcode)`: S=0.17, F=0.04, T=1.3%, INFERIOR (TOP1000)
- `rank(ts_delta(pv13_revere_zipcode, 5))`: S=0.77, F=0.55, T=31.9%, INFERIOR (TOP3000)
- `-rank(pv13_revere_zipcode)`: S=-0.17, F=-0.04, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(pv13_revere_zipcode, 5))`: S=0.40, F=0.30, T=13.4%, INFERIOR (TOP3000)
- `-ts_zscore(pv13_revere_zipcode, 63)`: S=-0.15, F=-0.08, T=2.1%, INFERIOR (TOP3000)
- `ts_mean(pv13_revere_zipcode, 10)`: S=0.24, F=0.11, T=1.4%, INFERIOR (TOP3000)
- `rank(ts_rank(pv13_revere_zipcode, 22))`: S=-0.31, F=-0.22, T=14.8%, INFERIOR (TOP3000)
- `rank(-1 * pv13_revere_zipcode)`: S=0.29, F=0.12, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * pv13_revere_zipcode / close)`: S=0.02, F=0.00, T=2.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 11F/13P
- LOW_FITNESS: 24F/0P
- LOW_SHARPE: 24F/0P
- LOW_SUB_UNIVERSE_SHARPE: 8F/5P
- LOW_TURNOVER: 1F/23P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.76, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=1.43 (moderate), ret=+27.3%
  - 2020: S=0.50 (weak), ret=+9.3%
  - 2021: S=0.09 (weak), ret=+1.9%
  - 2022: S=0.52 (moderate), ret=+13.6%
  - 2023: S=1.46 (moderate), ret=+27.2%

## Risk & Drawdown
- Max drawdown: 24.63% over 373 days (recovered)
- Annualized: return +16.2%, volatility 21.2% (fraction of booksize)
- Hit rate: 51.7% positive days
- Tail shape: skew -0.29, excess kurtosis +5.31

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.00, max 1.96, latest 1.41

## Yearly & Monthly Returns
Best year (by Sharpe): 2023; worst year: 2021
Best month: +18.95%; worst month: -9.84%
Positive months: 64%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=0.90
- Sideways: S=0.44
- Bear: S=0.93

## Negated Direction
Best negated: `rank(-1 * ts_delta(pv13_revere_zipcode, 5))` S=0.40, F=0.30, INFERIOR
Direction gap: -0.37 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * pv13_revere_zipcode)`: S=0.29, F=0.12, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * pv13_revere_zipcode / close)`: S=0.02, F=0.00, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(pv13_revere_zipcode, 5))`: S=0.40, F=0.30, T=13.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(pv13_revere_zipcode, 5))` | TOP3000 | 0.76 | 0.55 | 24.6% | 100% | all-weather |
| `rank(pv13_revere_zipcode)` | TOP1000 | 0.18 | 0.04 | 10.2% | 60% | bear-only |

## Correlation Notes
Top correlates:
- pv13_revere_index_cap: 0.123 (weakly positively correlated)
- pv13_revere_index_value: 0.119 (weakly positively correlated)
- fnd6_zipcode: 0.102 (weakly positively correlated)
- parkinson_volatility_30: -0.093 (weakly negatively correlated)
- pv13_com_rk_au: 0.092 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, rank_value_norm, trade_when
