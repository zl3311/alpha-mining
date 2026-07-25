---
field: rp_css_insider
dataset: news18
best_template: rank_delta
best_sharpe: 0.61
best_fitness: 0.13
best_universe: TOP500
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 20
regime_profile: mixed
n_variations_with_pnl: 7
max_drawdown: 0.2126
ann_vol: 0.1284
hit_rate: 0.5304
rolling_sharpe_min: -1.693
rolling_sharpe_max: 2.73
negated_best_sharpe: 0.27
negated_best_template: rank_neg_delta
negated_best_fitness: 0.03
n_negated_sims: 4
direction_gap: -0.34
---
# rp_css_insider (news18)

*Composite sentiment score of insider trading news*

## Signal Profile
- `rank(rp_css_insider)`: S=0.42, F=0.08, T=128.9%, INFERIOR (TOP200)
- `rank(ts_delta(rp_css_insider, 5))`: S=0.61, F=0.13, T=165.0%, INFERIOR (TOP500)
- `-rank(rp_css_insider)`: S=-0.42, F=-0.06, T=142.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(rp_css_insider, 5))`: S=0.27, F=0.03, T=176.3%, INFERIOR (TOP3000)
- `ts_zscore(rp_css_insider, 22)`: S=0.43, F=0.06, T=150.6%, INFERIOR (TOP3000)
- `ts_mean(rp_css_insider, 10)`: S=0.20, F=0.04, T=20.5%, INFERIOR (TOP3000)
- `rank(ts_rank(rp_css_insider, 22))`: S=0.09, F=0.01, T=151.9%, INFERIOR (TOP3000)
- `rank(-1 * rp_css_insider)`: S=-0.41, F=-0.05, T=151.9%, INFERIOR (TOP3000)
- `rank(-1 * rp_css_insider / close)`: S=-0.35, F=-0.04, T=154.7%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 9F/11P
- HIGH_TURNOVER: 19F/1P
- LOW_FITNESS: 20F/0P
- LOW_SHARPE: 20F/0P
- LOW_SUB_UNIVERSE_SHARPE: 7F/11P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.63, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.04 (negative), ret=-0.6%
  - 2020: S=1.94 (strong), ret=+27.1%
  - 2021: S=1.22 (moderate), ret=+16.6%
  - 2022: S=-0.48 (negative), ret=-6.3%
  - 2023: S=0.46 (weak), ret=+2.8%

## Risk & Drawdown
- Max drawdown: 21.26% over 637 days (not yet recovered, ongoing at window end)
- Annualized: return +8.1%, volatility 12.8% (fraction of booksize)
- Hit rate: 53.0% positive days
- Tail shape: skew +0.35, excess kurtosis +8.07

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.69, max 2.73, latest 0.44

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2022
Best month: +9.18%; worst month: -10.39%
Positive months: 54%

## Regime Profile
Regime profile: **mixed**
- Bull: S=-0.12
- Sideways: S=0.05
- Bear: S=1.91

## Negated Direction
Best negated: `rank(-1 * ts_delta(rp_css_insider, 5))` S=0.27, F=0.03, INFERIOR
Direction gap: -0.34 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * rp_css_insider)`: S=-0.41, F=-0.05, T=151.9%, INFERIOR (TOP3000)
- `rank(-1 * rp_css_insider / close)`: S=-0.35, F=-0.04, T=154.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(rp_css_insider, 5))`: S=0.27, F=0.03, T=176.3%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(rp_css_insider, 5))` | TOP500 | 0.63 | 0.13 | 21.3% | 60% | mixed |
| `rank(rp_css_insider)` | TOP500 | 0.49 | 0.08 | 17.2% | 60% | all-weather |
| `rank(ts_delta(rp_css_insider, 5))` | TOP1000 | 0.45 | 0.08 | 31.7% | 80% | mixed |
| `rank(rp_css_insider)` | TOP200 | 0.43 | 0.08 | 13.5% | 80% | mixed |
| `rank(rp_css_insider)` | TOP1000 | 0.46 | 0.06 | 12.1% | 60% | mixed |
| `rank(rp_css_insider)` | TOP3000 | 0.44 | 0.05 | 7.3% | 80% | mixed |
| `rank(ts_delta(rp_css_insider, 5))` | TOP200 | 0.20 | 0.03 | 37.5% | 60% | mixed |

## Correlation Notes
Top correlates:
- fnd6_newa1v1300_fca: -0.105 (weakly negatively correlated)
- rp_css_ptg: 0.104 (weakly positively correlated)
- rp_nip_legal: -0.103 (weakly negatively correlated)
- rp_css_price: 0.097 (weakly positively correlated)
- beta_last_60_days_spy: 0.095 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, rank_value_norm, trade_when
