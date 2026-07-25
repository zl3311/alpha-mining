---
field: fnd6_weburl
dataset: fundamental6
best_template: ts_zscore
best_sharpe: 1.13
best_fitness: 2.26
best_universe: TOP3000
grade: EXCELLENT
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 5
max_drawdown: 0.2545
ann_vol: 0.1881
hit_rate: 0.4826
rolling_sharpe_min: -1.645
rolling_sharpe_max: 2.545
negated_best_sharpe: 0.87
negated_best_template: neg_rank_level
negated_best_fitness: 0.68
n_negated_sims: 10
direction_gap: -0.26
---
# fnd6_weburl (fundamental6)

*WEB URL code for the company*

## Signal Profile
- `rank(fnd6_weburl)`: S=0.07, F=0.02, T=1.8%, INFERIOR (TOP200)
- `rank(fnd6_weburl / close)`: S=0.19, F=0.08, T=2.2%, INFERIOR (TOP200)
- `rank(ts_delta(fnd6_weburl, 5))`: S=0.56, F=0.52, T=9.7%, INFERIOR (TOP200)
- `-rank(fnd6_weburl)`: S=0.38, F=0.20, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_weburl, 5))`: S=0.56, F=0.41, T=17.9%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_weburl, 63)`: S=1.13, F=2.26, T=5.0%, EXCELLENT (TOP3000)
- `ts_mean(fnd6_weburl, 10)`: S=-0.40, F=-0.22, T=1.3%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_weburl, 22))`: S=0.32, F=0.32, T=12.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_weburl)`: S=0.87, F=0.68, T=0.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_weburl / close)`: S=0.28, F=0.15, T=1.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 31F/1P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 16F/13P
- LOW_TURNOVER: 4F/28P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.59, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.91 (moderate), ret=+10.6%
  - 2020: S=-0.28 (negative), ret=-5.7%
  - 2021: S=0.70 (moderate), ret=+17.9%
  - 2022: S=0.24 (weak), ret=+4.3%
  - 2023: S=2.20 (strong), ret=+27.0%

## Risk & Drawdown
- Max drawdown: 25.45% over 353 days (recovered)
- Annualized: return +11.0%, volatility 18.8% (fraction of booksize)
- Hit rate: 48.3% positive days
- Tail shape: skew +1.72, excess kurtosis +17.21

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.65, max 2.54, latest 2.20

## Yearly & Monthly Returns
Best year (by Sharpe): 2023; worst year: 2020
Best month: +17.47%; worst month: -12.55%
Positive months: 49%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=0.94
- Sideways: S=1.52
- Bear: S=-0.67

## Negated Direction
Best negated: `rank(-1 * fnd6_weburl)` S=0.87, F=0.68, INFERIOR
Direction gap: -0.26 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_weburl)`: S=0.87, F=0.68, T=0.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_weburl / close)`: S=0.28, F=0.15, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_weburl, 5))`: S=0.56, F=0.41, T=17.9%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_weburl, 5))` | TOP200 | 0.59 | 0.52 | 25.4% | 80% | bull-only |
| `rank(ts_delta(fnd6_weburl, 5))` | TOP500 | 0.24 | 0.15 | 64.7% | 60% | weak |
| `rank(ts_delta(fnd6_weburl, 5))` | TOP1000 | 0.18 | 0.09 | 94.3% | 60% | bull-only |
| `rank(fnd6_weburl / close)` | TOP200 | 0.20 | 0.08 | 33.1% | 60% | bear-only |
| `rank(fnd6_weburl)` | TOP200 | 0.08 | 0.02 | 36.4% | 60% | bear-only |

## Correlation Notes
Top correlates:
- fnd6_itcb: 0.492 (moderately positively correlated)
- min_stock_option_expense_guidance: 0.451 (moderately positively correlated)
- stock_option_expense_max_guidance_qtr: 0.451 (moderately positively correlated)
- pv13_ustomergraphrank_hub_rank: 0.415 (moderately positively correlated)
- unsystematic_risk_last_30_days: -0.387 (weakly negatively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
