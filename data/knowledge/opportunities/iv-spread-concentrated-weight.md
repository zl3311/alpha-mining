---
category: "opportunity"
priority: "resolved"
resolved_session: "20260604-001"
---

# Fix IV Spread CONCENTRATED_WEIGHT — RESOLVED

**Resolved 2026-06-04** in session 20260604-001.

Solution: pure options expression without fundamentals, using zscore + ts_mean smoothing:

```
ts_decay_linear(zscore(ts_mean(implied_volatility_call_270 - implied_volatility_put_270, 22)), 10)
```

Candidate alpha vRm07LP3 — EXCELLENT, ALL PASS, self-corr 0.309. Pending manual submission.

See pattern: `data/knowledge/patterns/iv-spread-zscore-tsmean.md`
