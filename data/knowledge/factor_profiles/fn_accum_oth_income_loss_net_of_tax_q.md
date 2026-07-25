---
field: fn_accum_oth_income_loss_net_of_tax_q
dataset: fundamental2
best_template: rank_ts_rank
best_sharpe: 0.65
best_fitness: 0.3
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bear-only
n_variations_with_pnl: 8
max_drawdown: 0.3036
ann_vol: 0.108
hit_rate: 0.5158
rolling_sharpe_min: -1.594
rolling_sharpe_max: 3.377
negated_best_sharpe: 0.52
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.24
n_negated_sims: 10
direction_gap: -0.13
---
# fn_accum_oth_income_loss_net_of_tax_q (fundamental2)

*Accumulated change in equity from transactions and other events and circumstances from non-owner sources, net of tax effect, at period end. Excludes Net Income (Loss), and accumulated changes in equity from transactions resulting from investments by owners and distributions to owners. Includes foreign currency translation items, certain pension adjustments, unrealized gains and losses on certain investments in debt and equity securities, other than temporary impairment (OTTI) losses related to factors other than credit losses on available-for-sale and held-to-maturity debt securities that an entity does not intend to sell and it is not more likely than not that the entity will be required to sell before recovery of the amortized cost basis, as well as changes in the fair value of derivatives related to the effective portion of a designated cash flow hedge.*

## Signal Profile
- `rank(fn_accum_oth_income_loss_net_of_tax_q)`: S=0.19, F=0.08, T=2.0%, INFERIOR (TOP200)
- `rank(fn_accum_oth_income_loss_net_of_tax_q / close)`: S=0.22, F=0.10, T=2.1%, INFERIOR (TOP200)
- `rank(ts_delta(fn_accum_oth_income_loss_net_of_tax_q, 5))`: S=0.24, F=0.05, T=36.5%, INFERIOR (TOP3000)
- `-rank(fn_accum_oth_income_loss_net_of_tax_q)`: S=0.15, F=0.05, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_accum_oth_income_loss_net_of_tax_q, 5))`: S=-0.24, F=-0.05, T=36.5%, INFERIOR (TOP3000)
- `-ts_zscore(fn_accum_oth_income_loss_net_of_tax_q, 63)`: S=-0.33, F=-0.10, T=18.4%, INFERIOR (TOP3000)
- `ts_mean(fn_accum_oth_income_loss_net_of_tax_q, 10)`: S=0.35, F=0.15, T=0.9%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_accum_oth_income_loss_net_of_tax_q, 22))`: S=0.65, F=0.30, T=16.3%, INFERIOR (TOP3000)
- `rank(-1 * fn_accum_oth_income_loss_net_of_tax_q)`: S=0.36, F=0.16, T=1.0%, INFERIOR (TOP3000)
- `rank(-1 * fn_accum_oth_income_loss_net_of_tax_q / close)`: S=0.52, F=0.24, T=1.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 10F/22P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 11F/18P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.23, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.84 (moderate), ret=+4.9%
  - 2020: S=2.80 (strong), ret=+24.8%
  - 2021: S=-0.27 (negative), ret=-3.2%
  - 2022: S=-1.17 (negative), ret=-18.2%
  - 2023: S=0.49 (weak), ret=+4.0%

## Risk & Drawdown
- Max drawdown: 30.36% over 1067 days (not yet recovered, ongoing at window end)
- Annualized: return +2.5%, volatility 10.8% (fraction of booksize)
- Hit rate: 51.6% positive days
- Tail shape: skew +0.20, excess kurtosis +3.07

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.59, max 3.38, latest 0.52

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2022
Best month: +3.91%; worst month: -9.03%
Positive months: 59%

## Regime Profile
Regime profile: **bear-only**
- Bull: S=-1.50
- Sideways: S=0.54
- Bear: S=2.72

## Negated Direction
Best negated: `rank(-1 * fn_accum_oth_income_loss_net_of_tax_q / close)` S=0.52, F=0.24, INFERIOR
Direction gap: -0.13 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fn_accum_oth_income_loss_net_of_tax_q)`: S=0.36, F=0.16, T=1.0%, INFERIOR (TOP3000)
- `rank(-1 * fn_accum_oth_income_loss_net_of_tax_q / close)`: S=0.52, F=0.24, T=1.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_accum_oth_income_loss_net_of_tax_q, 5))`: S=-0.24, F=-0.05, T=36.5%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fn_accum_oth_income_loss_net_of_tax_q / close)` | TOP200 | 0.23 | 0.10 | 30.4% | 60% | bear-only |
| `rank(fn_accum_oth_income_loss_net_of_tax_q)` | TOP200 | 0.20 | 0.08 | 31.8% | 60% | bear-only |
| `rank(ts_delta(fn_accum_oth_income_loss_net_of_tax_q, 5))` | TOP3000 | 0.29 | 0.05 | 17.3% | 80% | mixed |
| `rank(fn_accum_oth_income_loss_net_of_tax_q)` | TOP500 | 0.16 | 0.05 | 30.3% | 60% | bear-only |
| `rank(ts_delta(fn_accum_oth_income_loss_net_of_tax_q, 5))` | TOP1000 | 0.19 | 0.04 | 18.6% | 60% | bull-only |
| `rank(ts_delta(fn_accum_oth_income_loss_net_of_tax_q, 5))` | TOP500 | 0.17 | 0.03 | 21.3% | 60% | mixed |
| `rank(fn_accum_oth_income_loss_net_of_tax_q / close)` | TOP500 | 0.11 | 0.02 | 29.6% | 60% | bear-only |
| `rank(ts_delta(fn_accum_oth_income_loss_net_of_tax_q, 5))` | TOP200 | 0.10 | 0.02 | 36.6% | 60% | mixed |

## Correlation Notes
Top correlates:
- fn_accum_oth_income_loss_net_of_tax_a: 0.901 (strongly positively correlated)
- est_cashflow_fin: 0.818 (strongly positively correlated)
- fnd6_recta: 0.803 (strongly positively correlated)
- anl4_cff_median: 0.795 (strongly positively correlated)
- cashflow_dividends: -0.791 (strongly negatively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
