---
alpha_id: "xAxxVG7N"
grade: "SPECTACULAR"
sharpe: 2.52
fitness: 3.73
turnover: 0.082
returns: 0.274
status: "PENDING"
family: "depreciation_iv60_debt_innovation_blend"
expression: "ts_decay_linear(rank(fnd6_newqv1300_dpactq / close) + zscore(ts_mean(implied_volatility_call_60 - implied_volatility_put_60, 44)) + rank(fnd6_dlto / close) + rank(anl4_rd_exp_flag) + rank(fnd6_tlcf / close), 5)"
settings:
  decay: 6
  neutralization: "SUBINDUSTRY"
  universe: "TOP3000"
  region: "USA"
brain_checks:
  LOW_SHARPE: "PASS (2.52 vs 1.25)"
  LOW_FITNESS: "PASS (3.73 vs 1.00)"
  LOW_TURNOVER: "PASS (0.082 vs 0.01)"
  HIGH_TURNOVER: "PASS (0.082 vs 0.70)"
  CONCENTRATED_WEIGHT: "PASS"
  LOW_SUB_UNIVERSE_SHARPE: "PASS (1.15 vs 1.09)"
  SELF_CORRELATION: "PENDING (local PnL corr=0.583 < 0.70)"
  MATCHES_COMPETITION: "PASS"
self_correlation:
  max_corr: 0.583
  top_peer: "88z7MM37 (fundamental_iv60_blend)"
  margin: 0.117
  verdict: "PASS (auto below 0.70 threshold)"
discovered: "20260623"
session: "20260623-001"
url: "https://platform.worldquantbrain.com/alpha/xAxxVG7N"
---

# Alpha xAxxVG7N — Depreciation × IV60 × Debt × Innovation × Tax Shield

## Mechanism

5-factor additive blend combining orthogonal economic dimensions:

1. **Asset intensity / age** (fnd6_newqv1300_dpactq / close) — Higher accumulated
   depreciation relative to price indicates capital-intensive firms with aging
   assets, often trading at deep discounts to replacement value.

2. **Options directional sentiment** (IV60 call-put spread, 44-day smoothed zscore) —
   Near-term implied volatility skew captures informed options flow and directional
   market expectations.

3. **Debt structure complexity** (fnd6_dlto / close) — Total other liabilities scaled
   by price reflects non-traditional financing sources (lease obligations, pension
   liabilities, contingent liabilities) that are often mispriced by equity investors.

4. **R&D innovation signal** (anl4_rd_exp_flag) — Analyst R&D expense revision flag
   captures sudden changes in innovation spending expectations, signaling shifts in
   long-term growth trajectory.

5. **Tax optimization value** (fnd6_tlcf / close) — Tax loss carryforward scaled by
   price represents accumulated tax shields that can offset future taxable income,
   providing optionality value often ignored by simple valuation models.

## Decorrelation from Book

Self-correlation with 88z7MM37 (the closest book entry, also uses IV60) is only 0.583
because:
- Different fundamental legs (dpactq/dlto/tlcf vs itci/drlt/acdo)
- Addition of analyst revision flag leg (absent in 88z7MM37)
- 5-factor dilution reduces IV60's contribution to total PnL

## Submission Notes

- SELF_CORRELATION BRAIN check shows PENDING (only computed on submission attempt)
- Local PnL correlation confirms 0.583 < 0.70 threshold (robust margin of 0.117)
- Even under conservative 1.1x BRAIN inflation: 0.583 × 1.1 = 0.641 (still passes)
- Sharpe premium escape not needed at this correlation level
