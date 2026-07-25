---
field: fn_new_shares_options_a
dataset: fundamental2
best_template: rank_delta
best_sharpe: 0.43
best_fitness: 0.19
best_universe: TOP1000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 5
max_drawdown: 0.2658
ann_vol: 0.1534
hit_rate: 0.4826
rolling_sharpe_min: -1.612
rolling_sharpe_max: 2.723
negated_best_sharpe: 0.36
negated_best_template: rank_neg_delta
negated_best_fitness: 0.14
n_negated_sims: 10
direction_gap: -0.07
---
# fn_new_shares_options_a (fundamental2)

*Number of share options (or share units) exercised during the current period.*

## Signal Profile
- `rank(fn_new_shares_options_a)`: S=0.14, F=0.04, T=1.8%, INFERIOR (TOP200)
- `rank(fn_new_shares_options_a / close)`: S=0.15, F=0.04, T=2.0%, INFERIOR (TOP200)
- `rank(ts_delta(fn_new_shares_options_a, 5))`: S=0.43, F=0.19, T=35.0%, INFERIOR (TOP1000)
- `-rank(fn_new_shares_options_a)`: S=0.23, F=0.07, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_new_shares_options_a, 5))`: S=0.36, F=0.14, T=34.6%, INFERIOR (TOP3000)
- `-ts_zscore(fn_new_shares_options_a, 63)`: S=-0.14, F=-0.05, T=17.3%, INFERIOR (TOP3000)
- `ts_mean(fn_new_shares_options_a, 10)`: S=-0.51, F=-0.47, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_new_shares_options_a, 22))`: S=0.17, F=0.06, T=14.7%, INFERIOR (TOP3000)
- `rank(-1 * fn_new_shares_options_a)`: S=0.19, F=0.06, T=1.0%, INFERIOR (TOP3000)
- `rank(-1 * fn_new_shares_options_a / close)`: S=0.07, F=0.01, T=1.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 13F/19P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/16P
- LOW_TURNOVER: 4F/28P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.44, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.37 (weak), ret=+5.0%
  - 2020: S=0.99 (moderate), ret=+17.6%
  - 2021: S=0.40 (weak), ret=+5.2%
  - 2022: S=1.55 (strong), ret=+23.3%
  - 2023: S=-1.21 (negative), ret=-17.8%

## Risk & Drawdown
- Max drawdown: 26.58% over 213 days (not yet recovered, ongoing at window end)
- Annualized: return +6.8%, volatility 15.3% (fraction of booksize)
- Hit rate: 48.3% positive days
- Tail shape: skew +0.77, excess kurtosis +8.36

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.61, max 2.72, latest -1.13

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2023
Best month: +11.38%; worst month: -9.45%
Positive months: 52%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.60
- Sideways: S=0.23
- Bear: S=0.46

## Negated Direction
Best negated: `rank(-1 * ts_delta(fn_new_shares_options_a, 5))` S=0.36, F=0.14, INFERIOR
Direction gap: -0.07 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fn_new_shares_options_a)`: S=0.19, F=0.06, T=1.0%, INFERIOR (TOP3000)
- `rank(-1 * fn_new_shares_options_a / close)`: S=0.07, F=0.01, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_new_shares_options_a, 5))`: S=0.36, F=0.14, T=34.6%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fn_new_shares_options_a, 5))` | TOP1000 | 0.44 | 0.19 | 26.6% | 80% | mixed |
| `rank(ts_delta(fn_new_shares_options_a, 5))` | TOP200 | 0.32 | 0.14 | 30.1% | 60% | mixed |
| `rank(fn_new_shares_options_a)` | TOP200 | 0.16 | 0.04 | 12.8% | 60% | mixed |
| `rank(fn_new_shares_options_a / close)` | TOP500 | 0.16 | 0.04 | 11.2% | 80% | mixed |
| `rank(fn_new_shares_options_a / close)` | TOP200 | 0.16 | 0.04 | 13.2% | 60% | all-weather |

## Correlation Notes
Top correlates:
- fn_amortization_of_intangible_assets_a: -0.164 (weakly negatively correlated)
- fnd2_dfdlocalitxexp: 0.130 (weakly positively correlated)
- fnd6_optlifeq: -0.115 (weakly negatively correlated)
- fn_proceeds_from_issuance_of_debt_q: -0.114 (weakly negatively correlated)
- min_share_count_guidance: 0.111 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
