---
field: anl4_ebitda_flag
dataset: analyst4
best_template: rank_delta
best_sharpe: 0.6
best_fitness: 0.5
best_universe: TOP500
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 7
max_drawdown: 0.8085
ann_vol: 0.3167
hit_rate: 0.4883
rolling_sharpe_min: -1.818
rolling_sharpe_max: 3.775
negated_best_sharpe: 0.27
negated_best_template: neg_rank_level
negated_best_fitness: 0.17
n_negated_sims: 10
direction_gap: -0.33
---
# anl4_ebitda_flag (analyst4)

*Earnings before interest, taxes, depreciation and amortization - forecast type (revision/new/...)*

## Signal Profile
- `rank(anl4_ebitda_flag)`: S=0.38, F=0.14, T=1.8%, INFERIOR (TOP3000)
- `rank(anl4_ebitda_flag / close)`: S=0.29, F=0.15, T=2.6%, INFERIOR (TOP200)
- `rank(ts_delta(anl4_ebitda_flag, 5))`: S=0.60, F=0.50, T=27.7%, INFERIOR (TOP500)
- `-rank(anl4_ebitda_flag)`: S=-0.20, F=-0.07, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_ebitda_flag, 5))`: S=0.11, F=0.05, T=17.0%, INFERIOR (TOP3000)
- `-ts_zscore(anl4_ebitda_flag, 63)`: S=0.15, F=0.09, T=15.5%, INFERIOR (TOP3000)
- `ts_mean(anl4_ebitda_flag, 10)`: S=0.54, F=0.45, T=4.3%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_ebitda_flag, 22))`: S=0.02, F=0.00, T=18.3%, INFERIOR (TOP3000)
- `rank(-1 * anl4_ebitda_flag)`: S=0.27, F=0.17, T=2.7%, INFERIOR (TOP3000)
- `rank(-1 * anl4_ebitda_flag / close)`: S=-0.29, F=-0.15, T=2.6%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 16F/16P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 8F/12P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.59, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.58 (moderate), ret=+15.1%
  - 2020: S=-1.62 (negative), ret=-63.8%
  - 2021: S=2.25 (strong), ret=+95.6%
  - 2022: S=2.37 (strong), ret=+52.1%
  - 2023: S=-0.46 (negative), ret=-6.7%

## Risk & Drawdown
- Max drawdown: 80.85% over 636 days (recovered)
- Annualized: return +18.8%, volatility 31.7% (fraction of booksize)
- Hit rate: 48.8% positive days
- Tail shape: skew +0.68, excess kurtosis +8.26

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.82, max 3.77, latest -0.61

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +23.35%; worst month: -35.55%
Positive months: 60%

## Regime Profile
Regime profile: **mixed**
- Bull: S=1.44
- Sideways: S=0.81
- Bear: S=-0.31

## Negated Direction
Best negated: `rank(-1 * anl4_ebitda_flag)` S=0.27, F=0.17, INFERIOR
Direction gap: -0.33 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * anl4_ebitda_flag)`: S=0.27, F=0.17, T=2.7%, INFERIOR (TOP3000)
- `rank(-1 * anl4_ebitda_flag / close)`: S=-0.29, F=-0.15, T=2.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_ebitda_flag, 5))`: S=0.11, F=0.05, T=17.0%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(anl4_ebitda_flag, 5))` | TOP500 | 0.59 | 0.50 | 80.8% | 60% | mixed |
| `rank(anl4_ebitda_flag / close)` | TOP200 | 0.30 | 0.15 | 22.3% | 80% | mixed |
| `rank(anl4_ebitda_flag)` | TOP3000 | 0.38 | 0.14 | 15.9% | 80% | bull-only |
| `rank(ts_delta(anl4_ebitda_flag, 5))` | TOP3000 | 0.24 | 0.09 | 51.1% | 80% | mixed |
| `rank(anl4_ebitda_flag)` | TOP1000 | 0.20 | 0.07 | 28.8% | 60% | bull-only |
| `rank(anl4_ebitda_flag)` | TOP500 | 0.12 | 0.05 | 45.0% | 80% | bull-only |
| `rank(anl4_ebitda_flag / close)` | TOP500 | 0.09 | 0.02 | 29.6% | 60% | bear-only |

## Correlation Notes
Top correlates:
- fnd6_newa1v1300_acominc: -0.118 (weakly negatively correlated)
- guidance_reporting_currency: -0.118 (weakly negatively correlated)
- anl4_af_eps_value: 0.112 (weakly positively correlated)
- fnd2_a_curritxexp: 0.112 (weakly positively correlated)
- fn_income_tax_expense_a: 0.111 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
