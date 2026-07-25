---
type: "submit-candidate"
alpha_id: "JjpzQAze"
status: "SUBMITTED"
priority: "medium"
grade: "EXCELLENT"
sharpe: 2.30
fitness: 2.05
turnover: 0.117
self_corr_max: 0.6813
self_corr_method: "brain_check_authoritative"
neutralization: "SUBINDUSTRY"
decay: 6
family: "investment_intraday_analyst_product"
session: "20260629-001"
brain_url: "https://platform.worldquantbrain.com/alpha/JjpzQAze"
queued: "2026-06-29"
long_term_value: "MEDIUM"
---

# Submit JjpzQAze (ivaco product interaction)

## Expression
```
ts_decay_linear(rank(fnd6_ivaco / close) * rank(open / close - 1) * rank(anl4_bvps_flag), 5)
```

## Why submittable
- Self-corr 0.6813 vs current book (PASS, auto-pass under 0.7); all 7 computable BRAIN checks pass.
- Grade EXCELLENT, S=2.30, F=2.05, T=11.7%.
- Structurally novel: 3-way multiplicative interaction (vs additive blends in book).
- Uses fnd6_ivaco which is underrepresented in the book.

## Reviewer action
Submit on the BRAIN platform if desired, then set `status: SUBMITTED` in this
file and flip `data/book/JjpzQAze.md` to `status: ACTIVE`. If declined, set
`status: REJECTED`.
