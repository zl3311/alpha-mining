---
field: max_adjusted_eps_guidance_2
dataset: analyst4
best_template: rank_delta
best_sharpe: 0.78
best_fitness: 0.35
best_universe: TOP200
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 4
max_drawdown: 0.1185
ann_vol: 0.0875
hit_rate: 0.5004
rolling_sharpe_min: -0.865
rolling_sharpe_max: 3.26
top_merge_partner: operating_expense
redundancy_cluster: 40
negated_best_sharpe: 0.21
negated_best_template: rank_neg_delta
negated_best_fitness: 0.04
n_negated_sims: 10
direction_gap: -0.57
---
# max_adjusted_eps_guidance_2 (analyst4)

*The maximum guidance value for adjusted earnings per share on an annual basis.*

## Signal Profile
- `rank(max_adjusted_eps_guidance_2)`: S=0.30, F=0.15, T=0.7%, INFERIOR (TOP3000)
- `rank(max_adjusted_eps_guidance_2 / close)`: S=0.09, F=0.03, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_delta(max_adjusted_eps_guidance_2, 5))`: S=0.78, F=0.35, T=33.4%, INFERIOR (TOP200)
- `-rank(max_adjusted_eps_guidance_2)`: S=-0.10, F=-0.03, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(max_adjusted_eps_guidance_2, 5))`: S=0.21, F=0.04, T=36.3%, INFERIOR (TOP3000)
- `-ts_zscore(max_adjusted_eps_guidance_2, 63)`: S=0.35, F=0.10, T=21.9%, INFERIOR (TOP3000)
- `ts_mean(max_adjusted_eps_guidance_2, 10)`: S=0.10, F=0.03, T=1.8%, INFERIOR (TOP3000)
- `rank(ts_rank(max_adjusted_eps_guidance_2, 22))`: S=-0.12, F=-0.02, T=12.8%, INFERIOR (TOP3000)
- `rank(-1 * max_adjusted_eps_guidance_2)`: S=0.06, F=0.02, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * max_adjusted_eps_guidance_2 / close)`: S=0.08, F=0.02, T=2.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 2F/30P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 21F/8P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.80, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.54 (moderate), ret=+3.7%
  - 2020: S=2.56 (strong), ret=+21.1%
  - 2021: S=0.22 (weak), ret=+2.0%
  - 2022: S=0.51 (moderate), ret=+5.1%
  - 2023: S=0.29 (weak), ret=+2.5%

## Risk & Drawdown
- Max drawdown: 11.85% over 529 days (not yet recovered, ongoing at window end)
- Annualized: return +7.0%, volatility 8.8% (fraction of booksize)
- Hit rate: 50.0% positive days
- Tail shape: skew +0.66, excess kurtosis +5.78

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.86, max 3.26, latest 0.38

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2021
Best month: +5.83%; worst month: -4.58%
Positive months: 54%

## Regime Profile
Regime profile: **mixed**
- Bull: S=-0.33
- Sideways: S=0.60
- Bear: S=2.47

## Negated Direction
Best negated: `rank(-1 * ts_delta(max_adjusted_eps_guidance_2, 5))` S=0.21, F=0.04, INFERIOR
Direction gap: -0.57 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * max_adjusted_eps_guidance_2)`: S=0.06, F=0.02, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * max_adjusted_eps_guidance_2 / close)`: S=0.08, F=0.02, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(max_adjusted_eps_guidance_2, 5))`: S=0.21, F=0.04, T=36.3%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(max_adjusted_eps_guidance_2, 5))` | TOP200 | 0.80 | 0.35 | 11.8% | 100% | mixed |
| `rank(max_adjusted_eps_guidance_2)` | TOP3000 | 0.29 | 0.15 | 32.0% | 60% | bull-only |
| `rank(max_adjusted_eps_guidance_2)` | TOP1000 | 0.09 | 0.03 | 31.5% | 40% | bull-only |
| `rank(max_adjusted_eps_guidance_2 / close)` | TOP3000 | 0.09 | 0.03 | 52.8% | 60% | bull-only |

## Correlation Notes
Top correlates:
- max_stock_option_expense_guidance: 0.848 (strongly positively correlated)
- min_stock_option_expense_guidance_2: 0.848 (strongly positively correlated)
- dividend_max_guidance_quarterly: 0.842 (strongly positively correlated)
- dividend_max_guidance_value: 0.842 (strongly positively correlated)
- dividend_min_guidance_value: 0.838 (strongly positively correlated)

Redundancy cluster #40: 20 similar fields, mean |rho| 0.904 (representative: net_profit_adjusted_min_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| operating_expense | fundamental6 | -0.25 | 1.32 | +0.49 | -0.95 | yes |
| fnd6_newqv1300_xoprq | fundamental6 | -0.25 | 1.32 | +0.49 | -0.95 | yes |
| fnd6_newqv1300_xsgaq | fundamental6 | -0.23 | 1.30 | +0.49 | -0.93 | yes |
| sga_expense | fundamental6 | -0.23 | 1.30 | +0.49 | -0.93 | yes |
| implied_volatility_mean_skew_150 | option8 | -0.24 | 1.34 | +0.49 | -0.90 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
