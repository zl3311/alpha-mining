---
field: fn_debt_instrument_carrying_amount_q
dataset: fundamental2
best_template: rank_value_norm
best_sharpe: 0.78
best_fitness: 0.45
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 10
max_drawdown: 0.0814
ann_vol: 0.0541
hit_rate: 0.4939
rolling_sharpe_min: -1.386
rolling_sharpe_max: 2.557
redundancy_cluster: 1
negated_best_sharpe: 0.42
negated_best_template: rank_neg_delta
negated_best_fitness: 0.21
n_negated_sims: 10
direction_gap: -0.36
---
# fn_debt_instrument_carrying_amount_q (fundamental2)

*Debt carrying amount*

## Signal Profile
- `rank(fn_debt_instrument_carrying_amount_q)`: S=0.49, F=0.25, T=0.8%, INFERIOR (TOP3000)
- `rank(fn_debt_instrument_carrying_amount_q / close)`: S=0.78, F=0.45, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_delta(fn_debt_instrument_carrying_amount_q, 5))`: S=0.43, F=0.19, T=24.4%, INFERIOR (TOP3000)
- `-rank(fn_debt_instrument_carrying_amount_q)`: S=-0.26, F=-0.10, T=1.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_debt_instrument_carrying_amount_q, 5))`: S=0.42, F=0.21, T=24.1%, INFERIOR (TOP3000)
- `ts_zscore(fn_debt_instrument_carrying_amount_q, 22)`: S=0.38, F=0.21, T=30.6%, INFERIOR (TOP3000)
- `ts_mean(fn_debt_instrument_carrying_amount_q, 10)`: S=0.13, F=0.03, T=0.8%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_debt_instrument_carrying_amount_q, 22))`: S=0.00, F=0.00, T=12.0%, INFERIOR (TOP3000)
- `rank(-1 * fn_debt_instrument_carrying_amount_q)`: S=-0.12, F=-0.04, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * fn_debt_instrument_carrying_amount_q / close)`: S=-0.19, F=-0.07, T=1.9%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 6F/14P
- LOW_TURNOVER: 2F/30P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.77, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.20 (negative), ret=-0.8%
  - 2020: S=1.33 (moderate), ret=+9.2%
  - 2021: S=1.21 (moderate), ret=+6.9%
  - 2022: S=1.29 (moderate), ret=+6.6%
  - 2023: S=-0.37 (negative), ret=-1.5%

## Risk & Drawdown
- Max drawdown: 8.14% over 476 days (recovered)
- Annualized: return +4.2%, volatility 5.4% (fraction of booksize)
- Hit rate: 49.4% positive days
- Tail shape: skew +0.54, excess kurtosis +2.07

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.39, max 2.56, latest -0.26

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2023
Best month: +5.28%; worst month: -3.19%
Positive months: 61%

## Regime Profile
Regime profile: **mixed**
- Bull: S=2.51
- Sideways: S=0.08
- Bear: S=-0.49

## Negated Direction
Best negated: `rank(-1 * ts_delta(fn_debt_instrument_carrying_amount_q, 5))` S=0.42, F=0.21, INFERIOR
Direction gap: -0.36 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fn_debt_instrument_carrying_amount_q)`: S=-0.12, F=-0.04, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * fn_debt_instrument_carrying_amount_q / close)`: S=-0.19, F=-0.07, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_debt_instrument_carrying_amount_q, 5))`: S=0.42, F=0.21, T=24.1%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fn_debt_instrument_carrying_amount_q / close)` | TOP3000 | 0.77 | 0.45 | 8.1% | 60% | mixed |
| `rank(fn_debt_instrument_carrying_amount_q / close)` | TOP1000 | 0.52 | 0.27 | 7.9% | 80% | bull-only |
| `rank(fn_debt_instrument_carrying_amount_q)` | TOP3000 | 0.48 | 0.25 | 16.1% | 60% | bull-only |
| `rank(ts_delta(fn_debt_instrument_carrying_amount_q, 5))` | TOP3000 | 0.43 | 0.19 | 11.8% | 60% | bull-only |
| `rank(fn_debt_instrument_carrying_amount_q / close)` | TOP500 | 0.37 | 0.18 | 10.2% | 40% | bull-only |
| `rank(fn_debt_instrument_carrying_amount_q)` | TOP1000 | 0.24 | 0.10 | 15.5% | 60% | bull-only |
| `rank(fn_debt_instrument_carrying_amount_q / close)` | TOP200 | 0.18 | 0.07 | 18.5% | 60% | bull-only |
| `rank(ts_delta(fn_debt_instrument_carrying_amount_q, 5))` | TOP500 | 0.22 | 0.07 | 21.0% | 20% | bull-only |
| `rank(fn_debt_instrument_carrying_amount_q)` | TOP200 | 0.10 | 0.04 | 23.9% | 40% | bull-only |
| `rank(fn_debt_instrument_carrying_amount_q)` | TOP500 | 0.07 | 0.02 | 22.9% | 40% | bull-only |

## Correlation Notes
Top correlates:
- fn_debt_instrument_carrying_amount_a: 0.926 (strongly positively correlated)
- fn_interest_paid_net_a: 0.911 (strongly positively correlated)
- fnd6_newa2v1300_xint: 0.895 (strongly positively correlated)
- fnd6_intpn: 0.893 (strongly positively correlated)
- fnd6_newqv1300_xintq: 0.892 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
