---
pattern: "sales-count-densifier-decorrelates-oc"
discovered: "20260717-001"
applicable_to: "event-magnitude blends that need fitness lift without crossing the 0.7 self-corr wall"
confidence: "medium"
best_alpha_id: "N1rY5ZJg"
---

# Pattern: Sales-Estimate-Count Densifier Decorrelates Overnight-Gap Boost

## Template

```
ts_decay_linear(
  rank(abs(ts_delta(FIELD / close, 3)))
  + rank(-1 * equity / assets)
  + rank(FRESH_FLAG)
  + rank(fnd6_ivaco / close)
  + rank(fnd6_drlt / close)
  + rank(open / close - 1)
  + rank(sales_estimate_count_quarterly),
  5)
```

## When to Use

Use when a base event-magnitude blend is GOOD with self-corr PASS, and adding
`open/close - 1` alone pushes fitness to ~2.0 but fails self-corr (~0.72–0.73).
The sales-coverage densifier both lifts fitness past the EXCELLENT threshold
and pulls correlation back below 0.70.

## Evidence (session 20260717-001)

| Variant | Alpha | S | F | Self-corr |
|---------|-------|---|---|-----------|
| base (ffo, no OC) | mLbEAk05 | 1.78 | 1.58 | PASS 0.665 |
| + OC | XgndlqrX | 2.05 | 2.00 | FAIL 0.725 |
| + OC + sales_count | **N1rY5ZJg** | **2.23** | **2.20** | **PASS 0.664** |
