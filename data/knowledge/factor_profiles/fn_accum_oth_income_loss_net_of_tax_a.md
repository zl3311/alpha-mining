---
field: fn_accum_oth_income_loss_net_of_tax_a
dataset: fundamental2
best_template: rank_neg_delta
best_sharpe: 1.17
best_fitness: 0.74
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bear-only
n_variations_with_pnl: 4
max_drawdown: 0.24
ann_vol: 0.1009
hit_rate: 0.5247
rolling_sharpe_min: -1.555
rolling_sharpe_max: 3.941
negated_best_sharpe: 1.17
negated_best_template: rank_neg_delta
negated_best_fitness: 0.74
n_negated_sims: 10
direction_gap: 0.57
---
# fn_accum_oth_income_loss_net_of_tax_a (fundamental2)

*Accumulated change in equity from transactions and other events and circumstances from non-owner sources, net of tax effect, at period end. Excludes Net Income (Loss), and accumulated changes in equity from transactions resulting from investments by owners and distributions to owners. Includes foreign currency translation items, certain pension adjustments, unrealized gains and losses on certain investments in debt and equity securities, other than temporary impairment (OTTI) losses related to factors other than credit losses on available-for-sale and held-to-maturity debt securities that an entity does not intend to sell and it is not more likely than not that the entity will be required to sell before recovery of the amortized cost basis, as well as changes in the fair value of derivatives related to the effective portion of a designated cash flow hedge.*

## Signal Profile
- `rank(fn_accum_oth_income_loss_net_of_tax_a)`: S=0.45, F=0.27, T=1.9%, INFERIOR (TOP200)
- `rank(fn_accum_oth_income_loss_net_of_tax_a / close)`: S=0.42, F=0.24, T=2.0%, INFERIOR (TOP200)
- `rank(ts_delta(fn_accum_oth_income_loss_net_of_tax_a, 5))`: S=-0.10, F=-0.02, T=31.2%, INFERIOR (TOP200)
- `-rank(fn_accum_oth_income_loss_net_of_tax_a)`: S=-0.03, F=0.00, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_accum_oth_income_loss_net_of_tax_a, 5))`: S=1.17, F=0.74, T=34.6%, INFERIOR (TOP3000)
- `ts_zscore(fn_accum_oth_income_loss_net_of_tax_a, 22)`: S=-0.27, F=-0.13, T=25.0%, INFERIOR (TOP3000)
- `ts_mean(fn_accum_oth_income_loss_net_of_tax_a, 10)`: S=0.60, F=0.34, T=0.9%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_accum_oth_income_loss_net_of_tax_a, 22))`: S=0.12, F=0.03, T=14.6%, INFERIOR (TOP3000)
- `rank(-1 * fn_accum_oth_income_loss_net_of_tax_a)`: S=0.16, F=0.04, T=0.9%, INFERIOR (TOP3000)
- `rank(-1 * fn_accum_oth_income_loss_net_of_tax_a / close)`: S=0.31, F=0.11, T=1.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/15P
- LOW_TURNOVER: 5F/27P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.47, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.81 (moderate), ret=+4.3%
  - 2020: S=3.58 (strong), ret=+27.8%
  - 2021: S=-0.01 (negative), ret=-0.1%
  - 2022: S=-1.19 (negative), ret=-16.1%
  - 2023: S=0.81 (moderate), ret=+7.4%

## Risk & Drawdown
- Max drawdown: 24.00% over 759 days (not yet recovered, ongoing at window end)
- Annualized: return +4.7%, volatility 10.1% (fraction of booksize)
- Hit rate: 52.5% positive days
- Tail shape: skew +0.09, excess kurtosis +2.17

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.55, max 3.94, latest 0.86

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2022
Best month: +5.49%; worst month: -9.50%
Positive months: 64%

## Regime Profile
Regime profile: **bear-only**
- Bull: S=-1.64
- Sideways: S=1.07
- Bear: S=3.24

## Negated Direction
Best negated: `rank(-1 * ts_delta(fn_accum_oth_income_loss_net_of_tax_a, 5))` S=1.17, F=0.74, INFERIOR
Direction gap: +0.57 (negated - positive best Sharpe). NEGATION DOMINANT — field is significantly stronger when reversed.

Negated template variants:
- `rank(-1 * fn_accum_oth_income_loss_net_of_tax_a)`: S=0.16, F=0.04, T=0.9%, INFERIOR (TOP3000)
- `rank(-1 * fn_accum_oth_income_loss_net_of_tax_a / close)`: S=0.31, F=0.11, T=1.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_accum_oth_income_loss_net_of_tax_a, 5))`: S=1.17, F=0.74, T=34.6%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fn_accum_oth_income_loss_net_of_tax_a)` | TOP200 | 0.47 | 0.27 | 24.0% | 60% | bear-only |
| `rank(fn_accum_oth_income_loss_net_of_tax_a / close)` | TOP200 | 0.44 | 0.24 | 25.1% | 60% | bear-only |
| `rank(fn_accum_oth_income_loss_net_of_tax_a)` | TOP500 | 0.44 | 0.22 | 25.6% | 60% | bear-only |
| `rank(fn_accum_oth_income_loss_net_of_tax_a / close)` | TOP500 | 0.37 | 0.16 | 26.9% | 60% | bear-only |

## Correlation Notes
Top correlates:
- fn_accum_oth_income_loss_net_of_tax_q: 0.901 (strongly positively correlated)
- fnd6_recta: 0.835 (strongly positively correlated)
- est_cashflow_fin: 0.830 (strongly positively correlated)
- fn_comp_fair_value_assumptions_weighted_avg_vol_rate_a: 0.799 (strongly positively correlated)
- parkinson_volatility_150: 0.799 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
