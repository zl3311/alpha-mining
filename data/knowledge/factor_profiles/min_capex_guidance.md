---
field: min_capex_guidance
dataset: analyst4
best_template: rank_level
best_sharpe: 0.63
best_fitness: 0.57
best_universe: TOP200
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 5
max_drawdown: 0.1943
ann_vol: 0.1665
hit_rate: 0.519
rolling_sharpe_min: -0.994
rolling_sharpe_max: 3.289
redundancy_cluster: 86
negated_best_sharpe: 0.39
negated_best_template: rank_neg_delta
negated_best_fitness: 0.1
n_negated_sims: 10
direction_gap: -0.24
---
# min_capex_guidance (analyst4)

*Minimum guidance value for Capital Expenditures*

## Signal Profile
- `rank(min_capex_guidance)`: S=0.63, F=0.57, T=2.8%, INFERIOR (TOP200)
- `rank(min_capex_guidance / close)`: S=0.07, F=0.02, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_delta(min_capex_guidance, 5))`: S=0.46, F=0.16, T=33.7%, INFERIOR (TOP200)
- `-rank(min_capex_guidance)`: S=-0.26, F=-0.10, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(min_capex_guidance, 5))`: S=0.39, F=0.10, T=36.4%, INFERIOR (TOP3000)
- `-ts_zscore(min_capex_guidance, 63)`: S=0.46, F=0.18, T=20.6%, INFERIOR (TOP3000)
- `ts_mean(min_capex_guidance, 10)`: S=0.27, F=0.11, T=1.8%, INFERIOR (TOP3000)
- `rank(ts_rank(min_capex_guidance, 22))`: S=-0.06, F=-0.01, T=12.8%, INFERIOR (TOP3000)
- `rank(-1 * min_capex_guidance)`: S=-0.50, F=-0.30, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * min_capex_guidance / close)`: S=0.01, F=0.00, T=2.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 3F/29P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 16F/13P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.62, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=-0.97 (negative), ret=-9.9%
  - 2020: S=2.11 (strong), ret=+36.3%
  - 2021: S=0.50 (weak), ret=+12.8%
  - 2022: S=0.07 (weak), ret=+0.8%
  - 2023: S=0.90 (moderate), ret=+10.8%

## Risk & Drawdown
- Max drawdown: 19.43% over 475 days (recovered)
- Annualized: return +10.4%, volatility 16.7% (fraction of booksize)
- Hit rate: 51.9% positive days
- Tail shape: skew -1.56, excess kurtosis +25.82

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.99, max 3.29, latest 0.95

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2019
Best month: +13.85%; worst month: -11.37%
Positive months: 51%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.01
- Sideways: S=0.85
- Bear: S=1.27

## Negated Direction
Best negated: `rank(-1 * ts_delta(min_capex_guidance, 5))` S=0.39, F=0.10, INFERIOR
Direction gap: -0.24 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * min_capex_guidance)`: S=-0.50, F=-0.30, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * min_capex_guidance / close)`: S=0.01, F=0.00, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(min_capex_guidance, 5))`: S=0.39, F=0.10, T=36.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(min_capex_guidance)` | TOP200 | 0.62 | 0.57 | 19.4% | 80% | mixed |
| `rank(min_capex_guidance)` | TOP500 | 0.49 | 0.30 | 13.6% | 60% | mixed |
| `rank(ts_delta(min_capex_guidance, 5))` | TOP200 | 0.47 | 0.16 | 18.5% | 60% | bear-only |
| `rank(min_capex_guidance)` | TOP1000 | 0.26 | 0.10 | 10.2% | 60% | bear-only |
| `rank(min_capex_guidance / close)` | TOP3000 | 0.06 | 0.02 | 48.5% | 60% | bull-only |

## Correlation Notes
Top correlates:
- capital_expenditure_max_guidance_qtr: 1.000 (strongly positively correlated)
- news_pe_ratio: 0.356 (weakly positively correlated)
- fnd6_mfmq_cheq: -0.333 (weakly negatively correlated)
- cash_st: -0.332 (weakly negatively correlated)
- fnd6_newqv1300_chq: -0.325 (weakly negatively correlated)

Redundancy cluster #86: 2 similar fields, mean |rho| 1.0 (representative: capital_expenditure_max_guidance_qtr). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
