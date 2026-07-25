---
category: "dead_zone"
entity_type: "template"
template: "rank(F)*rank(F) | rank(max(F1,F2)-min(F1,F2)) | rank(anl4_FLAG)*rank(-1*sentiment)"
discovered: "20260709-001"
expressions_tested: 12
best_sharpe: 1.36
status: "dead_end"
confidence: "medium"
---

# Templates: Convex Self-Product, Dispersion, and Flag×Sentiment Interaction

Three genuinely novel operator-tree shapes from `novelty-required.md`'s
"Non-linear combinations" and "Cross-Family Interaction Grid" sections, tested
on already-strong standalone fields (`fnd6_ivaco`, `rel_num_all`,
`enterprise_value`, `anl4_netdebt_flag`) to isolate whether the STRUCTURE (not
field freshness) could produce signal. All failed to clear even GOOD grade.

## Evidence (session 20260709-001)

| Template | Expression | S | F |
|----------|-----------|---|---|
| Convex self-product | `rank(fnd6_ivaco/close) * rank(fnd6_ivaco/close)` | 1.31 | 0.81 |
| Convex self-product | `rank(rel_num_all) * rank(rel_num_all)` | 1.04 | 0.81 |
| Convex self-product | `rank(-1*enterprise_value/close) * rank(-1*enterprise_value/close)` | -0.27 | -0.09 |
| Dispersion | `rank(max(fnd6_drlt/close,fnd6_dlto/close)-min(...))` | 1.36 | 1.06 |
| Dispersion | `rank(max(fnd6_ivaco/close,fnd6_acdo/close)-min(...))` | 0.29 | 0.10 |
| Flag x sentiment | `rank(anl4_netdebt_flag) * rank(-1*scl12_buzz)` | 1.18 | 0.43 |
| Flag x sentiment | `rank(anl4_netdebt_flag) * rank(-1*snt_value)` | 0.92 | 0.37 |
| Flag x sentiment | `rank(-1*scl12_buzz) * rank(ts_delta(close,10))` | -1.05 | -0.34 |

## Why they fail

- **Convex self-product** (`rank(F)*rank(F)`): squaring a rank collapses sign
  information (both extremes get the same high value), which is economically
  backwards for signed fundamental signals — extreme LOW values should predict
  differently than extreme HIGH values in most of these fields.
- **Dispersion between two correlated fields** (`max-min`): when F1/F2 are from
  the same economic family (both leverage, or both capital-allocation), the
  spread between them is mostly noise, not a distinct signal dimension. The
  `drlt`/`dlto` pair's best result (F=1.06, AVERAGE) is the least bad but still
  below submission gates.
- **Flag × sentiment interaction**: multiplying a sparse, zero-dominated
  analyst flag by a dense sentiment score produces a doubly-sparse, high-noise
  signal. `anl4_*_flag` fields need the `zscore-accumulated-revision` template
  (`zscore(ts_sum(flag,22))`) to be usable at all (per that pattern) — raw
  `rank(flag)` interactions (as tested here) are known-inferior per the
  zscore-accumulated-revision pattern's own rank-vs-zscore comparison table.

## Rule

Do not pursue `rank(F)*rank(F)` self-products, `max-min` dispersion between
same-family fields, or raw `rank(anl4_flag) * rank(sentiment)` products as
standalone signals. If flag×sentiment interaction is revisited, use
`zscore(ts_sum(flag,22))` as the flag leg, not `rank(flag)`.
