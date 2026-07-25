---
type: "submit-candidate"
alpha_id: "78w5d35x"
status: "SUBMITTED"
priority: "high"
grade: "SPECTACULAR"
sharpe: 2.34
fitness: 3.10
turnover: 0.104
self_corr_max: 0.797
neutralization: "MARKET"
decay: 6
family: "dd1q_intraday_analyst_blend"
session: "20260702-001"
brain_url: "https://platform.worldquantbrain.com/alpha/78w5d35x"
queued: "2026-07-02"
long_term_value: "HIGH"
---

# Submit 78w5d35x (dd1q intraday analyst blend)

## Expression
```
ts_decay_linear(rank(fnd6_dd1q / close) + rank(anl4_ptpr_flag) + rank(fnd6_itci / close) + rank(open/close - 1), 5)
```

## Why submittable
- Self-corr 0.797 vs current book (PASS via Sharpe premium: 2.34 > 1.10×1.87); all computable BRAIN checks pass.
- Grade SPECTACULAR, S=2.34, F=3.10.
- Novel dd1q anchor with MARKET neutralization — HIGH LONG-TERM VALUE.

## Reviewer action
Submit on the BRAIN platform if desired, then set `status: SUBMITTED` and flip
`data/book/78w5d35x.md` to `status: ACTIVE`. If declined, set `status: REJECTED`.
