---
field: fn_repurchased_shares_value_q
dataset: fundamental2
best_template: rank_value_norm
best_sharpe: 0.41
best_fitness: 0.14
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 5
max_drawdown: 0.0948
ann_vol: 0.0372
hit_rate: 0.5045
rolling_sharpe_min: -2.623
rolling_sharpe_max: 2.521
negated_best_sharpe: 0.26
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.08
n_negated_sims: 10
direction_gap: -0.15
---
# fn_repurchased_shares_value_q (fundamental2)

*Shares repurchased and either retired or put into treasury stock, likely as part of a share buyback plan.*

## Signal Profile
- `rank(fn_repurchased_shares_value_q)`: S=0.28, F=0.10, T=1.6%, INFERIOR (TOP3000)
- `rank(fn_repurchased_shares_value_q / close)`: S=0.41, F=0.14, T=1.8%, INFERIOR (TOP3000)
- `rank(ts_delta(fn_repurchased_shares_value_q, 5))`: S=0.17, F=0.04, T=36.6%, INFERIOR (TOP200)
- `-rank(fn_repurchased_shares_value_q)`: S=-0.21, F=-0.06, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_repurchased_shares_value_q, 5))`: S=-0.01, F=0.00, T=36.0%, INFERIOR (TOP3000)
- `-ts_zscore(fn_repurchased_shares_value_q, 63)`: S=0.16, F=0.03, T=17.6%, INFERIOR (TOP3000)
- `ts_mean(fn_repurchased_shares_value_q, 10)`: S=0.15, F=0.05, T=1.7%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_repurchased_shares_value_q, 22))`: S=-0.90, F=-0.46, T=16.2%, INFERIOR (TOP3000)
- `rank(-1 * fn_repurchased_shares_value_q)`: S=0.14, F=0.04, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * fn_repurchased_shares_value_q / close)`: S=0.26, F=0.08, T=2.6%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 10F/22P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 22F/7P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.40, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.87 (moderate), ret=+2.5%
  - 2020: S=-2.44 (negative), ret=-7.2%
  - 2021: S=1.57 (strong), ret=+7.1%
  - 2022: S=0.74 (moderate), ret=+3.3%
  - 2023: S=0.54 (moderate), ret=+1.7%

## Risk & Drawdown
- Max drawdown: 9.48% over 775 days (recovered)
- Annualized: return +1.5%, volatility 3.7% (fraction of booksize)
- Hit rate: 50.4% positive days
- Tail shape: skew -0.07, excess kurtosis +1.14

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.62, max 2.52, latest 0.36

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2020
Best month: +2.65%; worst month: -1.79%
Positive months: 48%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.52
- Sideways: S=0.91
- Bear: S=-2.68

## Negated Direction
Best negated: `rank(-1 * fn_repurchased_shares_value_q / close)` S=0.26, F=0.08, INFERIOR
Direction gap: -0.15 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fn_repurchased_shares_value_q)`: S=0.14, F=0.04, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * fn_repurchased_shares_value_q / close)`: S=0.26, F=0.08, T=2.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_repurchased_shares_value_q, 5))`: S=-0.01, F=0.00, T=36.0%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fn_repurchased_shares_value_q / close)` | TOP3000 | 0.40 | 0.14 | 9.5% | 80% | bull-only |
| `rank(fn_repurchased_shares_value_q)` | TOP3000 | 0.28 | 0.10 | 14.9% | 80% | bull-only |
| `rank(fn_repurchased_shares_value_q / close)` | TOP1000 | 0.21 | 0.06 | 10.7% | 60% | bull-only |
| `rank(fn_repurchased_shares_value_q)` | TOP1000 | 0.20 | 0.06 | 14.7% | 60% | bull-only |
| `rank(ts_delta(fn_repurchased_shares_value_q, 5))` | TOP200 | 0.18 | 0.04 | 30.2% | 40% | mixed |

## Correlation Notes
Top correlates:
- fnd6_cptmfmq_ceqq: 0.776 (strongly positively correlated)
- fnd6_cptnewqv1300_ceqq: 0.775 (strongly positively correlated)
- equity: 0.775 (strongly positively correlated)
- fnd6_newqv1300_seqq: 0.775 (strongly positively correlated)
- fnd6_newqv1300_teqq: 0.774 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
