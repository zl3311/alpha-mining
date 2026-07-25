---
field: fnd6_fic
dataset: fundamental6
best_template: rank_delta
best_sharpe: 0.55
best_fitness: 0.56
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 3
max_drawdown: 0.4226
ann_vol: 0.241
hit_rate: 0.4785
rolling_sharpe_min: -0.996
rolling_sharpe_max: 1.855
negated_best_sharpe: 0.63
negated_best_template: neg_rank_level
negated_best_fitness: 0.39
n_negated_sims: 10
direction_gap: 0.08
---
# fnd6_fic (fundamental6)

*identifies the country in which the company is incorporated or legally registered*

## Signal Profile
- `rank(fnd6_fic)`: S=-0.22, F=-0.09, T=2.0%, INFERIOR (TOP500)
- `rank(fnd6_fic / close)`: S=-0.02, F=0.00, T=2.3%, INFERIOR (TOP200)
- `rank(ts_delta(fnd6_fic, 5))`: S=0.55, F=0.56, T=11.4%, INFERIOR (TOP3000)
- `-rank(fnd6_fic)`: S=0.40, F=0.20, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_fic, 5))`: S=-0.23, F=-0.15, T=11.4%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_fic, 63)`: S=0.00, F=0.00, T=0.0%, UNKNOWN (TOP3000)
- `ts_mean(fnd6_fic, 10)`: S=0.01, F=0.00, T=1.5%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_fic, 22))`: S=0.50, F=0.55, T=5.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_fic)`: S=0.63, F=0.39, T=1.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_fic / close)`: S=0.29, F=0.14, T=1.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 30F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/14P
- LOW_TURNOVER: 2F/30P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.54, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=1.45 (moderate), ret=+28.5%
  - 2020: S=0.06 (weak), ret=+1.4%
  - 2021: S=1.30 (moderate), ret=+34.9%
  - 2022: S=-0.42 (negative), ret=-12.2%
  - 2023: S=0.65 (moderate), ret=+10.9%

## Risk & Drawdown
- Max drawdown: 42.26% over 704 days (not yet recovered, ongoing at window end)
- Annualized: return +13.0%, volatility 24.1% (fraction of booksize)
- Hit rate: 47.9% positive days
- Tail shape: skew +1.12, excess kurtosis +20.60

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.00, max 1.85, latest 0.56

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2022
Best month: +18.12%; worst month: -13.50%
Positive months: 61%

## Regime Profile
Regime profile: **mixed**
- Bull: S=1.21
- Sideways: S=-0.01
- Bear: S=0.39

## Negated Direction
Best negated: `rank(-1 * fnd6_fic)` S=0.63, F=0.39, INFERIOR
Direction gap: +0.08 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fnd6_fic)`: S=0.63, F=0.39, T=1.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_fic / close)`: S=0.29, F=0.14, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_fic, 5))`: S=-0.23, F=-0.15, T=11.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_fic, 5))` | TOP3000 | 0.54 | 0.56 | 42.3% | 80% | mixed |
| `rank(ts_delta(fnd6_fic, 5))` | TOP200 | 0.37 | 0.25 | 28.5% | 60% | bull-only |
| `rank(ts_delta(fnd6_fic, 5))` | TOP500 | 0.31 | 0.20 | 31.7% | 40% | bull-only |

## Correlation Notes
Top correlates:
- max_share_buyback_guidance: 0.398 (weakly positively correlated)
- min_adjusted_funds_from_operations_adj_guidance: 0.398 (weakly positively correlated)
- max_total_goodwill_guidance_2: 0.398 (weakly positively correlated)
- min_custom_eps_guidance: 0.398 (weakly positively correlated)
- max_adjusted_funds_from_operations_adj_guidance: 0.398 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
