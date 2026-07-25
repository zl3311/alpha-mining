---
id: "20260717-001-results"
session: "20260717-001"
total_expressions: 52
gate_passers: 15
best_sharpe: 2.41
best_fitness: 2.30
best_alpha_id: "N1rY5ZJg"
---

# Results: Session 20260717-001

## Summary Metrics

| Metric | Value |
|--------|-------|
| Expressions tested | 52 |
| Gate-passers (S>=1.25, F>=1.0) | ~15 |
| Best Sharpe (any) | 2.41 (`d50NEaAK`, blocked self-corr) |
| Best submittable | `N1rY5ZJg` S=2.23 F=2.20 |
| Budget used | 52 / unlimited |
| Simulation path | local BrainClient |

## Submittable Candidate

| Alpha | Grade | S | F | T | Self-corr | Verdict |
|-------|-------|---|---|---|-----------|---------|
| [N1rY5ZJg](https://platform.worldquantbrain.com/alpha/N1rY5ZJg) | EXCELLENT | 2.23 | 2.20 | 7.8% | PASS 0.6638 | **SAFE** |

Expression:

```
ts_decay_linear(rank(abs(ts_delta(fn_liab_fair_val_a / close, 3))) + rank(-1 * equity / assets) + rank(anl4_ffo_flag) + rank(fnd6_ivaco / close) + rank(fnd6_drlt / close) + rank(open / close - 1) + rank(sales_estimate_count_quarterly), 5)
```

## Notable Gate-Passers (checked)

| Alpha | Grade | S | F | Self-corr | Verdict |
|-------|-------|---|---|-----------|---------|
| LL106da6 | EXCELLENT | 2.25 | 2.16 | FAIL 0.794 | BLOCKED |
| 3qR8apVg | EXCELLENT | 2.33 | 2.28 | FAIL 0.802 | BLOCKED |
| d50NEaAK | EXCELLENT | 2.41 | 2.30 | FAIL 0.824 | BLOCKED |
| MPQJKeOk | EXCELLENT | 2.26 | 2.21 | FAIL 0.786 | BLOCKED |
| XgndlqrX | GOOD | 2.05 | 2.00 | FAIL 0.725 | BLOCKED |
| j20q9wJe | EXCELLENT | 2.06 | 2.01 | FAIL 0.722 | BLOCKED |
| mLbEAk05 | GOOD | 1.78 | 1.58 | PASS 0.665 | below EXCELLENT |
| MPQJ8QR6 | GOOD | 1.96 | 1.88 | PASS 0.692 | below EXCELLENT |
| QPVwl0EQ | GOOD | 1.98 | 1.77 | PASS 0.678 | below EXCELLENT |
| A1Pobg9Y | GOOD | 1.82 | 1.63 | FAIL 0.758 | BLOCKED |
| JjO6YkZA | GOOD | 1.70 | 1.57 | FAIL 0.814 | BLOCKED |

## Round Files

- `round1_results.json` (18)
- `round2_results.json` (18)
- `round3_results.json` (16)
- `selfcorr_r1.txt`, `selfcorr_r2.txt`, `selfcorr_r3.txt`, `selfcorr_winner.txt`
