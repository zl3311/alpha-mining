---
field: beta_last_90_days_spy
dataset: model51
best_template: ts_zscore
best_sharpe: 0.34
best_fitness: 0.13
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 21
regime_profile: bear-only
n_variations_with_pnl: 2
max_drawdown: 0.4262
ann_vol: 0.1773
hit_rate: 0.4866
rolling_sharpe_min: -1.387
rolling_sharpe_max: 2.419
negated_best_sharpe: -0.04
negated_best_template: neg_rank_value_norm
negated_best_fitness: -0.01
n_negated_sims: 4
direction_gap: -0.38
---
# beta_last_90_days_spy (model51)

*The rolling beta value of the security relative to SPY, calculated via regression over the last 90 calendar days, representing market sensitivity*

## Signal Profile
- `rank(beta_last_90_days_spy)`: S=0.14, F=0.06, T=12.5%, INFERIOR (TOP3000)
- `rank(beta_last_90_days_spy / close)`: S=0.06, F=0.02, T=11.6%, INFERIOR (TOP3000)
- `rank(ts_delta(beta_last_90_days_spy, 5))`: S=0.07, F=0.01, T=42.3%, INFERIOR (TOP3000)
- `-rank(beta_last_90_days_spy)`: S=-0.07, F=-0.02, T=13.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(beta_last_90_days_spy, 5))`: S=-0.07, F=-0.01, T=42.3%, INFERIOR (TOP3000)
- `-ts_zscore(beta_last_90_days_spy, 63)`: S=0.34, F=0.13, T=19.7%, INFERIOR (TOP3000)
- `ts_mean(beta_last_90_days_spy, 10)`: S=0.15, F=0.08, T=4.6%, INFERIOR (TOP3000)
- `rank(ts_rank(beta_last_90_days_spy, 22))`: S=-0.29, F=-0.08, T=29.1%, INFERIOR (TOP3000)
- `rank(-1 * beta_last_90_days_spy)`: S=-0.14, F=-0.06, T=12.5%, INFERIOR (TOP3000)
- `rank(-1 * beta_last_90_days_spy / close)`: S=-0.04, F=-0.01, T=10.6%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 21F/0P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 21F/0P
- LOW_SUB_UNIVERSE_SHARPE: 11F/8P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.14, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.58 (moderate), ret=+5.2%
  - 2020: S=1.74 (strong), ret=+26.9%
  - 2021: S=0.29 (weak), ret=+4.2%
  - 2022: S=-1.02 (negative), ret=-28.6%
  - 2023: S=0.31 (weak), ret=+4.4%

## Risk & Drawdown
- Max drawdown: 42.62% over 781 days (not yet recovered, ongoing at window end)
- Annualized: return +2.5%, volatility 17.7% (fraction of booksize)
- Hit rate: 48.7% positive days
- Tail shape: skew +0.31, excess kurtosis +2.25

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.39, max 2.42, latest 0.51

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2022
Best month: +10.08%; worst month: -12.06%
Positive months: 56%

## Regime Profile
Regime profile: **bear-only**
- Bull: S=-1.47
- Sideways: S=-0.09
- Bear: S=2.30

## Negated Direction
Best negated: `rank(-1 * beta_last_90_days_spy / close)` S=-0.04, F=-0.01, INFERIOR
Direction gap: -0.38 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * beta_last_90_days_spy)`: S=-0.14, F=-0.06, T=12.5%, INFERIOR (TOP3000)
- `rank(-1 * beta_last_90_days_spy / close)`: S=-0.04, F=-0.01, T=10.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(beta_last_90_days_spy, 5))`: S=-0.07, F=-0.01, T=42.3%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(beta_last_90_days_spy)` | TOP3000 | 0.14 | 0.06 | 42.6% | 80% | bear-only |
| `rank(beta_last_90_days_spy)` | TOP500 | 0.13 | 0.05 | 46.9% | 80% | bear-only |

## Correlation Notes
Top correlates:
- systematic_risk_last_90_days: 0.983 (strongly positively correlated)
- fnd6_mfmq_ibcomq: -0.859 (strongly negatively correlated)
- fnd6_newqv1300_cibegniq: -0.859 (strongly negatively correlated)
- income: -0.859 (strongly negatively correlated)
- fnd6_newqv1300_dilavq: -0.842 (strongly negatively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
