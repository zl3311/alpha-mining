---
field: fn_assets_fair_val_l3_q
dataset: fundamental2
best_template: rank_delta
best_sharpe: 0.7
best_fitness: 0.42
best_universe: TOP500
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 7
max_drawdown: 0.2948
ann_vol: 0.1613
hit_rate: 0.4785
rolling_sharpe_min: -1.593
rolling_sharpe_max: 2.984
negated_best_sharpe: 0.16
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.04
n_negated_sims: 10
direction_gap: -0.54
---
# fn_assets_fair_val_l3_q (fundamental2)

*Asset Fair Value, Recurring, Level 3*

## Signal Profile
- `rank(fn_assets_fair_val_l3_q)`: S=0.36, F=0.10, T=0.8%, INFERIOR (TOP3000)
- `rank(fn_assets_fair_val_l3_q / close)`: S=0.24, F=0.06, T=0.9%, INFERIOR (TOP3000)
- `rank(ts_delta(fn_assets_fair_val_l3_q, 5))`: S=0.70, F=0.42, T=31.0%, INFERIOR (TOP500)
- `-rank(fn_assets_fair_val_l3_q)`: S=-0.25, F=-0.07, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_assets_fair_val_l3_q, 5))`: S=-0.50, F=-0.26, T=31.1%, INFERIOR (TOP3000)
- `ts_zscore(fn_assets_fair_val_l3_q, 22)`: S=0.16, F=0.05, T=20.2%, INFERIOR (TOP3000)
- `ts_mean(fn_assets_fair_val_l3_q, 10)`: S=0.42, F=0.21, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_assets_fair_val_l3_q, 22))`: S=-0.23, F=-0.10, T=17.7%, INFERIOR (TOP3000)
- `rank(-1 * fn_assets_fair_val_l3_q)`: S=0.13, F=0.03, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * fn_assets_fair_val_l3_q / close)`: S=0.16, F=0.04, T=1.5%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 15F/14P
- LOW_TURNOVER: 2F/30P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.70, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.62 (moderate), ret=+6.8%
  - 2020: S=0.07 (weak), ret=+0.8%
  - 2021: S=0.07 (weak), ret=+1.4%
  - 2022: S=2.56 (strong), ret=+50.9%
  - 2023: S=-0.37 (negative), ret=-4.9%

## Risk & Drawdown
- Max drawdown: 29.48% over 542 days (recovered)
- Annualized: return +11.2%, volatility 16.1% (fraction of booksize)
- Hit rate: 47.9% positive days
- Tail shape: skew +1.28, excess kurtosis +13.46

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.59, max 2.98, latest -0.41

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2023
Best month: +19.30%; worst month: -11.54%
Positive months: 63%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.28
- Sideways: S=0.20
- Bear: S=-1.66

## Negated Direction
Best negated: `rank(-1 * fn_assets_fair_val_l3_q / close)` S=0.16, F=0.04, INFERIOR
Direction gap: -0.54 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fn_assets_fair_val_l3_q)`: S=0.13, F=0.03, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * fn_assets_fair_val_l3_q / close)`: S=0.16, F=0.04, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_assets_fair_val_l3_q, 5))`: S=-0.50, F=-0.26, T=31.1%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fn_assets_fair_val_l3_q, 5))` | TOP500 | 0.70 | 0.42 | 29.5% | 80% | bull-only |
| `rank(ts_delta(fn_assets_fair_val_l3_q, 5))` | TOP1000 | 0.58 | 0.30 | 37.4% | 60% | bull-only |
| `rank(fn_assets_fair_val_l3_q)` | TOP3000 | 0.36 | 0.10 | 6.3% | 60% | bull-only |
| `rank(fn_assets_fair_val_l3_q)` | TOP1000 | 0.25 | 0.07 | 8.8% | 60% | bull-only |
| `rank(fn_assets_fair_val_l3_q / close)` | TOP3000 | 0.25 | 0.06 | 6.1% | 60% | mixed |
| `rank(fn_assets_fair_val_l3_q / close)` | TOP1000 | 0.19 | 0.05 | 7.9% | 60% | bull-only |
| `rank(ts_delta(fn_assets_fair_val_l3_q, 5))` | TOP3000 | 0.16 | 0.05 | 41.6% | 20% | weak |

## Correlation Notes
Top correlates:
- min_free_cashflow_per_share_guidance: 0.174 (weakly positively correlated)
- shareholders_equity_min_guidance: 0.174 (weakly positively correlated)
- min_total_assets_guidance: 0.174 (weakly positively correlated)
- max_free_cashflow_per_share_guidance: 0.174 (weakly positively correlated)
- shareholders_equity_max_guidance: 0.174 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
