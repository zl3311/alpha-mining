---
field: fnd2_a_sbcpnargmsptawervl
dataset: fundamental2
best_template: rank_neg_delta
best_sharpe: 0.74
best_fitness: 0.45
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: weak
n_variations_with_pnl: 2
max_drawdown: 0.1344
ann_vol: 0.0685
hit_rate: 0.4996
rolling_sharpe_min: -1.034
rolling_sharpe_max: 1.659
negated_best_sharpe: 0.74
negated_best_template: rank_neg_delta
negated_best_fitness: 0.45
n_negated_sims: 10
direction_gap: 0.5
---
# fnd2_a_sbcpnargmsptawervl (fundamental2)

*Amount of accumulated difference between fair value of underlying shares on dates of exercise and exercise price on options exercised (or share units converted) into shares.*

## Signal Profile
- `rank(fnd2_a_sbcpnargmsptawervl)`: S=-0.02, F=0.00, T=2.1%, INFERIOR (TOP200)
- `rank(fnd2_a_sbcpnargmsptawervl / close)`: S=0.20, F=0.07, T=1.9%, INFERIOR (TOP500)
- `rank(ts_delta(fnd2_a_sbcpnargmsptawervl, 5))`: S=-0.16, F=-0.04, T=33.7%, INFERIOR (TOP3000)
- `-rank(fnd2_a_sbcpnargmsptawervl)`: S=0.41, F=0.20, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_a_sbcpnargmsptawervl, 5))`: S=0.74, F=0.45, T=33.4%, INFERIOR (TOP3000)
- `-ts_zscore(fnd2_a_sbcpnargmsptawervl, 63)`: S=0.24, F=0.12, T=16.8%, INFERIOR (TOP3000)
- `ts_mean(fnd2_a_sbcpnargmsptawervl, 10)`: S=-0.08, F=-0.02, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd2_a_sbcpnargmsptawervl, 22))`: S=-0.09, F=-0.02, T=14.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_a_sbcpnargmsptawervl)`: S=0.01, F=0.00, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_a_sbcpnargmsptawervl / close)`: S=-0.20, F=-0.07, T=1.9%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 19F/10P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.21, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=1.25 (moderate), ret=+4.8%
  - 2020: S=0.18 (weak), ret=+0.9%
  - 2021: S=-0.08 (negative), ret=-0.6%
  - 2022: S=-0.59 (negative), ret=-5.9%
  - 2023: S=1.34 (moderate), ret=+7.7%

## Risk & Drawdown
- Max drawdown: 13.44% over 592 days (recovered)
- Annualized: return +1.4%, volatility 6.9% (fraction of booksize)
- Hit rate: 50.0% positive days
- Tail shape: skew +0.39, excess kurtosis +3.18

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.03, max 1.66, latest 1.45

## Yearly & Monthly Returns
Best year (by Sharpe): 2023; worst year: 2022
Best month: +4.85%; worst month: -3.65%
Positive months: 56%

## Regime Profile
Regime profile: **weak**
- Bull: S=0.06
- Sideways: S=0.27
- Bear: S=0.33

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd2_a_sbcpnargmsptawervl, 5))` S=0.74, F=0.45, INFERIOR
Direction gap: +0.50 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fnd2_a_sbcpnargmsptawervl)`: S=0.01, F=0.00, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_a_sbcpnargmsptawervl / close)`: S=-0.20, F=-0.07, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_a_sbcpnargmsptawervl, 5))`: S=0.74, F=0.45, T=33.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd2_a_sbcpnargmsptawervl / close)` | TOP500 | 0.21 | 0.07 | 13.4% | 60% | weak |
| `rank(fnd2_a_sbcpnargmsptawervl / close)` | TOP200 | 0.12 | 0.03 | 23.5% | 80% | weak |

## Correlation Notes
Top correlates:
- fnd6_prch: 0.601 (moderately positively correlated)
- fn_comp_options_out_intrinsic_value_a: 0.574 (moderately positively correlated)
- fnd6_prcc: 0.549 (moderately positively correlated)
- fn_comp_not_rec_a: 0.521 (moderately positively correlated)
- fn_allocated_share_based_compensation_expense_a: 0.519 (moderately positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
