---
field: rp_nip_partner
dataset: news18
best_template: ts_mean
best_sharpe: 0.56
best_fitness: 0.17
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 21
regime_profile: mixed
n_variations_with_pnl: 1
max_drawdown: 0.246
ann_vol: 0.0782
hit_rate: 0.5231
rolling_sharpe_min: -2.668
rolling_sharpe_max: 2.885
negated_best_sharpe: 0.42
negated_best_template: rank_neg_delta
negated_best_fitness: 0.07
n_negated_sims: 4
direction_gap: -0.14
---
# rp_nip_partner (news18)

*News impact projection of partnership news*

## Signal Profile
- `rank(rp_nip_partner)`: S=0.79, F=0.16, T=151.2%, INFERIOR (TOP3000)
- `rank(rp_nip_partner / close)`: S=0.08, F=0.01, T=123.4%, INFERIOR (TOP3000)
- `rank(ts_delta(rp_nip_partner, 5))`: S=-0.42, F=-0.07, T=150.0%, INFERIOR (TOP3000)
- `-rank(rp_nip_partner)`: S=-0.15, F=-0.01, T=143.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(rp_nip_partner, 5))`: S=0.42, F=0.07, T=150.0%, INFERIOR (TOP3000)
- `ts_zscore(rp_nip_partner, 22)`: S=0.15, F=0.01, T=140.5%, INFERIOR (TOP3000)
- `ts_mean(rp_nip_partner, 10)`: S=0.56, F=0.17, T=29.7%, INFERIOR (TOP3000)
- `rank(ts_rank(rp_nip_partner, 22))`: S=0.04, F=0.00, T=146.4%, INFERIOR (TOP3000)
- `rank(-1 * rp_nip_partner)`: S=-0.79, F=-0.16, T=151.2%, INFERIOR (TOP3000)
- `rank(-1 * rp_nip_partner / close)`: S=-0.45, F=-0.09, T=133.8%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 11F/10P
- HIGH_TURNOVER: 20F/1P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 21F/0P
- LOW_SUB_UNIVERSE_SHARPE: 12F/7P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.78, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.27 (weak), ret=+1.9%
  - 2020: S=2.32 (strong), ret=+18.3%
  - 2021: S=1.91 (strong), ret=+16.1%
  - 2022: S=1.53 (strong), ret=+11.7%
  - 2023: S=-2.62 (negative), ret=-18.2%

## Risk & Drawdown
- Max drawdown: 24.60% over 315 days (not yet recovered, ongoing at window end)
- Annualized: return +6.1%, volatility 7.8% (fraction of booksize)
- Hit rate: 52.3% positive days
- Tail shape: skew +0.04, excess kurtosis +0.81

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.67, max 2.88, latest -2.33

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2023
Best month: +5.92%; worst month: -5.86%
Positive months: 63%

## Regime Profile
Regime profile: **mixed**
- Bull: S=-0.29
- Sideways: S=0.32
- Bear: S=2.17

## Negated Direction
Best negated: `rank(-1 * ts_delta(rp_nip_partner, 5))` S=0.42, F=0.07, INFERIOR
Direction gap: -0.14 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * rp_nip_partner)`: S=-0.79, F=-0.16, T=151.2%, INFERIOR (TOP3000)
- `rank(-1 * rp_nip_partner / close)`: S=-0.45, F=-0.09, T=133.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(rp_nip_partner, 5))`: S=0.42, F=0.07, T=150.0%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(rp_nip_partner)` | TOP3000 | 0.78 | 0.16 | 24.6% | 80% | mixed |

## Correlation Notes
Top correlates:
- parkinson_volatility_20: 0.163 (weakly positively correlated)
- historical_volatility_20: 0.146 (weakly positively correlated)
- fnd6_txtubsoflimit: -0.140 (weakly negatively correlated)
- fnd6_txtubxintbs: -0.136 (weakly negatively correlated)
- fn_income_tax_expense_q: -0.136 (weakly negatively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
