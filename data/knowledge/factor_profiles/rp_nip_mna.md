---
field: rp_nip_mna
dataset: news18
best_template: rank_ts_rank
best_sharpe: 0.91
best_fitness: 0.16
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 21
regime_profile: mixed
n_variations_with_pnl: 3
max_drawdown: 0.0888
ann_vol: 0.0526
hit_rate: 0.5198
rolling_sharpe_min: -1.149
rolling_sharpe_max: 1.883
negated_best_sharpe: -0.07
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.0
n_negated_sims: 4
direction_gap: -0.98
---
# rp_nip_mna (news18)

*News impact projection of mergers and acquisitions-related news*

## Signal Profile
- `rank(rp_nip_mna)`: S=0.53, F=0.07, T=150.6%, INFERIOR (TOP1000)
- `rank(rp_nip_mna / close)`: S=0.09, F=0.01, T=138.0%, INFERIOR (TOP3000)
- `rank(ts_delta(rp_nip_mna, 5))`: S=0.50, F=0.07, T=160.8%, INFERIOR (TOP1000)
- `-rank(rp_nip_mna)`: S=-0.53, F=-0.07, T=150.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(rp_nip_mna, 5))`: S=-0.21, F=-0.02, T=167.8%, INFERIOR (TOP3000)
- `ts_zscore(rp_nip_mna, 22)`: S=0.77, F=0.13, T=151.2%, INFERIOR (TOP3000)
- `ts_mean(rp_nip_mna, 10)`: S=0.02, F=0.00, T=22.7%, INFERIOR (TOP3000)
- `rank(ts_rank(rp_nip_mna, 22))`: S=0.91, F=0.16, T=154.5%, INFERIOR (TOP3000)
- `rank(-1 * rp_nip_mna)`: S=-0.10, F=-0.01, T=162.7%, INFERIOR (TOP3000)
- `rank(-1 * rp_nip_mna / close)`: S=-0.07, F=0.00, T=154.6%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 3F/18P
- HIGH_TURNOVER: 20F/1P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 21F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/5P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.53, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.55 (moderate), ret=+2.8%
  - 2020: S=0.95 (moderate), ret=+4.8%
  - 2021: S=0.28 (weak), ret=+1.8%
  - 2022: S=0.71 (moderate), ret=+3.6%
  - 2023: S=0.21 (weak), ret=+0.8%

## Risk & Drawdown
- Max drawdown: 8.88% over 616 days (recovered)
- Annualized: return +2.8%, volatility 5.3% (fraction of booksize)
- Hit rate: 52.0% positive days
- Tail shape: skew -0.43, excess kurtosis +4.49

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.15, max 1.88, latest 0.15

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2023
Best month: +3.57%; worst month: -3.28%
Positive months: 58%

## Regime Profile
Regime profile: **mixed**
- Bull: S=-0.18
- Sideways: S=-0.11
- Bear: S=1.91

## Negated Direction
Best negated: `rank(-1 * rp_nip_mna / close)` S=-0.07, F=0.00, INFERIOR
Direction gap: -0.98 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * rp_nip_mna)`: S=-0.10, F=-0.01, T=162.7%, INFERIOR (TOP3000)
- `rank(-1 * rp_nip_mna / close)`: S=-0.07, F=0.00, T=154.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(rp_nip_mna, 5))`: S=-0.21, F=-0.02, T=167.8%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(rp_nip_mna, 5))` | TOP1000 | 0.51 | 0.07 | 16.2% | 80% | mixed |
| `rank(rp_nip_mna)` | TOP1000 | 0.53 | 0.07 | 8.9% | 100% | mixed |
| `rank(ts_delta(rp_nip_mna, 5))` | TOP3000 | 0.21 | 0.02 | 22.6% | 60% | mixed |

## Correlation Notes
Top correlates:
- beta_last_90_days_spy: 0.159 (weakly positively correlated)
- systematic_risk_last_90_days: 0.154 (weakly positively correlated)
- return_equity: -0.145 (weakly negatively correlated)
- pcr_oi_30: -0.143 (weakly negatively correlated)
- pcr_oi_1080: -0.142 (weakly negatively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
