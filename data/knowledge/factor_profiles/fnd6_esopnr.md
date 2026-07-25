---
field: fnd6_esopnr
dataset: fundamental6
best_template: rank_delta
best_sharpe: 0.46
best_fitness: 0.29
best_universe: TOP500
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 6
max_drawdown: 0.3169
ann_vol: 0.0999
hit_rate: 0.451
rolling_sharpe_min: -3.262
rolling_sharpe_max: 2.435
negated_best_sharpe: 0.31
negated_best_template: neg_rank
negated_best_fitness: 0.24
n_negated_sims: 10
direction_gap: -0.15
---
# fnd6_esopnr (fundamental6)

*Preferred ESOP Obligation - Non-Redeemable*

## Signal Profile
- `rank(fnd6_esopnr)`: S=0.29, F=0.20, T=4.6%, INFERIOR (TOP200)
- `rank(fnd6_esopnr / close)`: S=0.29, F=0.20, T=4.6%, INFERIOR (TOP200)
- `rank(ts_delta(fnd6_esopnr, 5))`: S=0.46, F=0.29, T=3.1%, INFERIOR (TOP500)
- `-rank(fnd6_esopnr)`: S=0.31, F=0.24, T=2.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_esopnr, 5))`: S=0.04, F=0.01, T=2.8%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_esopnr, 22)`: S=0.00, F=0.00, T=0.0%, UNKNOWN (TOP3000)
- `ts_mean(fnd6_esopnr, 10)`: S=-0.19, F=-0.11, T=0.5%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_esopnr, 22))`: S=-0.06, F=-0.01, T=3.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_esopnr)`: S=0.27, F=0.19, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_esopnr / close)`: S=0.27, F=0.19, T=2.5%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 32F/0P
- LOW_FITNESS: 30F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 10F/17P
- LOW_TURNOVER: 3F/29P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.43, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=2.12 (strong), ret=+10.8%
  - 2020: S=-1.72 (negative), ret=-13.2%
  - 2021: S=0.93 (moderate), ret=+15.1%
  - 2022: S=1.04 (moderate), ret=+10.3%
  - 2023: S=-0.33 (negative), ret=-2.0%

## Risk & Drawdown
- Max drawdown: 31.69% over 783 days (recovered)
- Annualized: return +4.3%, volatility 10.0% (fraction of booksize)
- Hit rate: 45.1% positive days
- Tail shape: skew +0.05, excess kurtosis +3.01

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -3.26, max 2.44, latest -0.34

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2020
Best month: +7.08%; worst month: -9.62%
Positive months: 55%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.04
- Sideways: S=1.25
- Bear: S=-2.36

## Negated Direction
Best negated: `-rank(fnd6_esopnr)` S=0.31, F=0.24, INFERIOR
Direction gap: -0.15 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_esopnr)`: S=0.27, F=0.19, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_esopnr / close)`: S=0.27, F=0.19, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_esopnr, 5))`: S=0.04, F=0.01, T=2.8%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_esopnr, 5))` | TOP500 | 0.43 | 0.29 | 31.7% | 60% | bull-only |
| `rank(ts_delta(fnd6_esopnr, 5))` | TOP3000 | 0.39 | 0.24 | 34.5% | 60% | bull-only |
| `rank(fnd6_esopnr / close)` | TOP200 | 0.28 | 0.20 | 32.4% | 60% | weak |
| `rank(fnd6_esopnr)` | TOP200 | 0.28 | 0.20 | 32.1% | 60% | weak |
| `rank(fnd6_esopnr / close)` | TOP500 | 0.09 | 0.04 | 34.0% | 60% | bull-only |
| `rank(fnd6_esopnr)` | TOP500 | 0.09 | 0.04 | 34.0% | 60% | bull-only |

## Correlation Notes
Top correlates:
- min_free_cashflow_per_share_guidance: 0.964 (strongly positively correlated)
- shareholders_equity_min_guidance: 0.964 (strongly positively correlated)
- min_total_assets_guidance: 0.964 (strongly positively correlated)
- max_free_cashflow_per_share_guidance: 0.964 (strongly positively correlated)
- shareholders_equity_max_guidance: 0.964 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
