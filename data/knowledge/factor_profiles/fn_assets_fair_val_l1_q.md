---
field: fn_assets_fair_val_l1_q
dataset: fundamental2
best_template: rank_neg_delta
best_sharpe: 0.59
best_fitness: 0.25
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 4
max_drawdown: 0.1574
ann_vol: 0.0622
hit_rate: 0.5134
rolling_sharpe_min: -1.866
rolling_sharpe_max: 2.218
negated_best_sharpe: 0.59
negated_best_template: rank_neg_delta
negated_best_fitness: 0.25
n_negated_sims: 10
direction_gap: 0.14
---
# fn_assets_fair_val_l1_q (fundamental2)

*Asset Fair Value, Recurring, Level 1*

## Signal Profile
- `rank(fn_assets_fair_val_l1_q)`: S=0.12, F=0.04, T=2.2%, INFERIOR (TOP200)
- `rank(fn_assets_fair_val_l1_q / close)`: S=0.10, F=0.03, T=2.3%, INFERIOR (TOP200)
- `rank(ts_delta(fn_assets_fair_val_l1_q, 5))`: S=-0.11, F=-0.03, T=36.8%, INFERIOR (TOP200)
- `-rank(fn_assets_fair_val_l1_q)`: S=-0.09, F=-0.02, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_assets_fair_val_l1_q, 5))`: S=0.59, F=0.25, T=36.1%, INFERIOR (TOP3000)
- `ts_zscore(fn_assets_fair_val_l1_q, 22)`: S=0.45, F=0.22, T=28.9%, INFERIOR (TOP3000)
- `ts_mean(fn_assets_fair_val_l1_q, 10)`: S=0.10, F=0.02, T=0.8%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_assets_fair_val_l1_q, 22))`: S=-0.18, F=-0.06, T=16.3%, INFERIOR (TOP3000)
- `rank(-1 * fn_assets_fair_val_l1_q)`: S=-0.03, F=0.00, T=0.9%, INFERIOR (TOP3000)
- `rank(-1 * fn_assets_fair_val_l1_q / close)`: S=0.17, F=0.05, T=1.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 11F/18P
- LOW_TURNOVER: 5F/27P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.16, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.11 (negative), ret=-0.4%
  - 2020: S=-0.95 (negative), ret=-6.3%
  - 2021: S=0.15 (weak), ret=+1.2%
  - 2022: S=1.15 (moderate), ret=+6.6%
  - 2023: S=0.78 (moderate), ret=+3.7%

## Risk & Drawdown
- Max drawdown: 15.74% over 1027 days (recovered)
- Annualized: return +1.0%, volatility 6.2% (fraction of booksize)
- Hit rate: 51.3% positive days
- Tail shape: skew -0.28, excess kurtosis +3.35

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.87, max 2.22, latest 0.75

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +4.60%; worst month: -5.22%
Positive months: 58%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=1.83
- Sideways: S=0.41
- Bear: S=-1.64

## Negated Direction
Best negated: `rank(-1 * ts_delta(fn_assets_fair_val_l1_q, 5))` S=0.59, F=0.25, INFERIOR
Direction gap: +0.14 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fn_assets_fair_val_l1_q)`: S=-0.03, F=0.00, T=0.9%, INFERIOR (TOP3000)
- `rank(-1 * fn_assets_fair_val_l1_q / close)`: S=0.17, F=0.05, T=1.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_assets_fair_val_l1_q, 5))`: S=0.59, F=0.25, T=36.1%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fn_assets_fair_val_l1_q)` | TOP200 | 0.14 | 0.04 | 28.4% | 60% | bull-only |
| `rank(fn_assets_fair_val_l1_q)` | TOP500 | 0.16 | 0.04 | 15.7% | 60% | bull-only |
| `rank(fn_assets_fair_val_l1_q / close)` | TOP200 | 0.12 | 0.03 | 30.5% | 60% | bull-only |
| `rank(fn_assets_fair_val_l1_q / close)` | TOP500 | 0.11 | 0.02 | 13.5% | 60% | bull-only |

## Correlation Notes
Top correlates:
- min_free_cashflow_per_share_guidance: 0.556 (moderately positively correlated)
- shareholders_equity_min_guidance: 0.556 (moderately positively correlated)
- min_total_assets_guidance: 0.556 (moderately positively correlated)
- max_free_cashflow_per_share_guidance: 0.556 (moderately positively correlated)
- shareholders_equity_max_guidance: 0.556 (moderately positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
