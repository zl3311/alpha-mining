---
category: "rule"
severity: "critical"
updated: "20260606"
---

# Self-Correlation Threshold

## Confirmed Model (2026-06-06)

BRAIN self-correlation check uses a **0.7 threshold** with a **1.10x Sharpe
premium escape**:

- **Corr <= 0.7** vs all book entries → **auto PASS** (no Sharpe requirement).
- **Corr > 0.7** but candidate Sharpe >= 1.10x max correlated peer Sharpe → **PASS**.
- **Corr > 0.7** and candidate Sharpe < 1.10x max correlated peer Sharpe → **FAIL**.

## Previous Understanding (superseded)

Earlier observations suggested a threshold of ~0.62 (0.622 passed for 0mzQQvX8,
0.633 failed for blvvlQAR). These were correct observations but misattributed
to the correlation threshold itself. The 0.62/0.63 boundary was likely the result
of the Sharpe premium calculation at those specific Sharpe values — not a lower
correlation threshold.

## Practical Target

- For candidates with **no shared data fields** with book entries: target PnL
  corr < 0.7 (local PnL ≈ BRAIN self-corr).
- For candidates that **share data fields**: target PnL corr < 0.44
  (BRAIN inflates by 1.45-1.6x; see `self-corr-pnl-gap` rule).
- Even above 0.7, submission can succeed if Sharpe premium is met.
  Verify via `/alphas/{id}/check` endpoint.

## Authoritative Check

Use the BRAIN `/alphas/{id}/check` endpoint. It returns `SELF_CORRELATION`
with `result` (PASS/FAIL), `value`, and `limit` fields. The result is
authoritative and accounts for the Sharpe premium escape.
