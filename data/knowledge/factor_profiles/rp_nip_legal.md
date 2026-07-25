---
field: rp_nip_legal
dataset: news18
best_template: ts_mean
best_sharpe: 0.52
best_fitness: 0.19
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 21
regime_profile: all-weather
n_variations_with_pnl: 4
max_drawdown: 0.2785
ann_vol: 0.165
hit_rate: 0.5304
rolling_sharpe_min: -0.957
rolling_sharpe_max: 2.321
negated_best_sharpe: 0.15
negated_best_template: rank_neg_delta
negated_best_fitness: 0.02
n_negated_sims: 4
direction_gap: -0.37
---
# rp_nip_legal (news18)

*News impact projection of legal news*

## Signal Profile
- `rank(rp_nip_legal)`: S=0.51, F=0.12, T=139.9%, INFERIOR (TOP200)
- `rank(rp_nip_legal / close)`: S=0.09, F=0.01, T=131.2%, INFERIOR (TOP3000)
- `rank(ts_delta(rp_nip_legal, 5))`: S=0.41, F=0.12, T=151.1%, INFERIOR (TOP500)
- `-rank(rp_nip_legal)`: S=-0.02, F=0.00, T=147.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(rp_nip_legal, 5))`: S=0.15, F=0.02, T=151.7%, INFERIOR (TOP3000)
- `-ts_zscore(rp_nip_legal, 63)`: S=0.37, F=0.07, T=147.8%, INFERIOR (TOP3000)
- `ts_mean(rp_nip_legal, 10)`: S=0.52, F=0.19, T=31.6%, INFERIOR (TOP3000)
- `rank(ts_rank(rp_nip_legal, 22))`: S=-0.39, F=-0.07, T=151.6%, INFERIOR (TOP3000)
- `rank(-1 * rp_nip_legal)`: S=-0.27, F=-0.05, T=149.9%, INFERIOR (TOP3000)
- `rank(-1 * rp_nip_legal / close)`: S=-0.53, F=-0.16, T=131.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 20F/1P
- HIGH_TURNOVER: 20F/1P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 21F/0P
- LOW_SUB_UNIVERSE_SHARPE: 5F/14P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.51, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=-0.86 (negative), ret=-12.5%
  - 2020: S=1.32 (moderate), ret=+20.9%
  - 2021: S=1.08 (moderate), ret=+15.8%
  - 2022: S=0.26 (weak), ret=+5.6%
  - 2023: S=0.84 (moderate), ret=+11.4%

## Risk & Drawdown
- Max drawdown: 27.85% over 457 days (recovered)
- Annualized: return +8.4%, volatility 16.5% (fraction of booksize)
- Hit rate: 53.0% positive days
- Tail shape: skew -1.17, excess kurtosis +12.90

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.96, max 2.32, latest 0.83

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2019
Best month: +11.56%; worst month: -11.38%
Positive months: 63%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=0.65
- Sideways: S=-0.29
- Bear: S=1.20

## Negated Direction
Best negated: `rank(-1 * ts_delta(rp_nip_legal, 5))` S=0.15, F=0.02, INFERIOR
Direction gap: -0.37 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * rp_nip_legal)`: S=-0.27, F=-0.05, T=149.9%, INFERIOR (TOP3000)
- `rank(-1 * rp_nip_legal / close)`: S=-0.53, F=-0.16, T=131.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(rp_nip_legal, 5))`: S=0.15, F=0.02, T=151.7%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(rp_nip_legal)` | TOP200 | 0.51 | 0.12 | 27.9% | 80% | all-weather |
| `rank(ts_delta(rp_nip_legal, 5))` | TOP500 | 0.43 | 0.12 | 46.2% | 80% | bull-only |
| `rank(rp_nip_legal)` | TOP500 | 0.41 | 0.09 | 36.5% | 60% | mixed |
| `rank(rp_nip_legal)` | TOP3000 | 0.27 | 0.05 | 38.0% | 60% | all-weather |

## Correlation Notes
Top correlates:
- rp_nip_society: 0.229 (weakly positively correlated)
- rp_nip_ptg: -0.121 (weakly negatively correlated)
- systematic_risk_last_360_days: -0.113 (weakly negatively correlated)
- beta_last_360_days_spy: -0.106 (weakly negatively correlated)
- fnd6_txndb: -0.106 (weakly negatively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
