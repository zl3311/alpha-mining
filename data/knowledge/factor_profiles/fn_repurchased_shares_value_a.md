---
field: fn_repurchased_shares_value_a
dataset: fundamental2
best_template: rank_delta
best_sharpe: 0.69
best_fitness: 0.39
best_universe: TOP500
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 6
max_drawdown: 0.3611
ann_vol: 0.1553
hit_rate: 0.5117
rolling_sharpe_min: -1.862
rolling_sharpe_max: 3.267
negated_best_sharpe: 0.14
negated_best_template: neg_rank
negated_best_fitness: 0.04
n_negated_sims: 10
direction_gap: -0.55
---
# fn_repurchased_shares_value_a (fundamental2)

*Shares repurchased and either retired or put into treasury stock, likely as part of a share buyback plan.*

## Signal Profile
- `rank(fn_repurchased_shares_value_a)`: S=0.25, F=0.09, T=0.8%, INFERIOR (TOP3000)
- `rank(fn_repurchased_shares_value_a / close)`: S=0.66, F=0.34, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_delta(fn_repurchased_shares_value_a, 5))`: S=0.69, F=0.39, T=33.9%, INFERIOR (TOP500)
- `-rank(fn_repurchased_shares_value_a)`: S=0.14, F=0.04, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_repurchased_shares_value_a, 5))`: S=0.15, F=0.03, T=34.2%, INFERIOR (TOP3000)
- `ts_zscore(fn_repurchased_shares_value_a, 22)`: S=0.06, F=0.01, T=21.1%, INFERIOR (TOP3000)
- `ts_mean(fn_repurchased_shares_value_a, 10)`: S=-0.13, F=-0.05, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_repurchased_shares_value_a, 22))`: S=-0.12, F=-0.03, T=14.8%, INFERIOR (TOP3000)
- `rank(-1 * fn_repurchased_shares_value_a)`: S=-0.25, F=-0.09, T=0.8%, INFERIOR (TOP3000)
- `rank(-1 * fn_repurchased_shares_value_a / close)`: S=-0.66, F=-0.34, T=1.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 13F/19P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 15F/14P
- LOW_TURNOVER: 4F/28P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.69, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=1.95 (strong), ret=+24.9%
  - 2020: S=1.84 (strong), ret=+26.2%
  - 2021: S=0.09 (weak), ret=+1.4%
  - 2022: S=-1.16 (negative), ret=-22.2%
  - 2023: S=1.63 (strong), ret=+22.5%

## Risk & Drawdown
- Max drawdown: 36.11% over 580 days (recovered)
- Annualized: return +10.8%, volatility 15.5% (fraction of booksize)
- Hit rate: 51.2% positive days
- Tail shape: skew +0.15, excess kurtosis +5.31

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.86, max 3.27, latest 1.57

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2022
Best month: +12.39%; worst month: -10.06%
Positive months: 59%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.55
- Sideways: S=1.84
- Bear: S=-0.10

## Negated Direction
Best negated: `-rank(fn_repurchased_shares_value_a)` S=0.14, F=0.04, INFERIOR
Direction gap: -0.55 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fn_repurchased_shares_value_a)`: S=-0.25, F=-0.09, T=0.8%, INFERIOR (TOP3000)
- `rank(-1 * fn_repurchased_shares_value_a / close)`: S=-0.66, F=-0.34, T=1.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_repurchased_shares_value_a, 5))`: S=0.15, F=0.03, T=34.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fn_repurchased_shares_value_a, 5))` | TOP500 | 0.69 | 0.39 | 36.1% | 80% | mixed |
| `rank(fn_repurchased_shares_value_a / close)` | TOP3000 | 0.66 | 0.34 | 8.5% | 80% | bull-only |
| `rank(fn_repurchased_shares_value_a)` | TOP3000 | 0.24 | 0.09 | 22.8% | 80% | bull-only |
| `rank(fn_repurchased_shares_value_a / close)` | TOP1000 | 0.20 | 0.07 | 10.8% | 60% | bull-only |
| `rank(ts_delta(fn_repurchased_shares_value_a, 5))` | TOP200 | 0.16 | 0.05 | 23.0% | 40% | weak |
| `rank(ts_delta(fn_repurchased_shares_value_a, 5))` | TOP1000 | 0.19 | 0.05 | 29.9% | 40% | mixed |

## Correlation Notes
Top correlates:
- fn_payments_for_repurchase_of_common_stock_a: 0.706 (strongly positively correlated)
- fn_repurchased_shares_a: 0.272 (weakly positively correlated)
- fnd6_cidergl: 0.191 (weakly positively correlated)
- fn_proceeds_from_issuance_of_common_stock_a: 0.181 (weakly positively correlated)
- fnd6_prchq: -0.157 (weakly negatively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
