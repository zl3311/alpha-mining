---
type: "submit-candidate"
alpha_id: "0m7lnAEr"
status: "SUBMITTED"
priority: "high"
grade: "EXCELLENT"
sharpe: 2.08
fitness: 2.01
turnover: 0.148
self_corr_max: 0.5480
self_corr_method: "brain_check_authoritative"
self_corr_verdict: "PASS"
neutralization: "SUBINDUSTRY"
decay: 6
family: "iv_event_breadth_volregime"
session: "20260617-001"
brain_url: "https://platform.worldquantbrain.com/alpha/0m7lnAEr"
queued: "2026-06-17"
---

# Submit 0m7lnAEr (Volatility-Gated IV/Event Breadth Blend)

## Expression

`trade_when(ts_std_dev(returns, 20) > 0.02, ts_decay_linear(rank(ts_mean(implied_volatility_call_270 - implied_volatility_put_270, 10)) + rank(fnd6_itci / close) + rank(fnd6_acdo) + rank(anl4_netdebt_flag) + rank(ts_mean(scl12_buzz, 5)) + rank(open / close - 1), 5), ts_std_dev(returns, 20) < 0.01)`

## Why submittable (verified 2026-06-17)

- EXCELLENT grade, S=2.08, F=2.01, turnover 14.8%.
- All 8 computable BRAIN checks PASS (authoritative `/check`).
- Authoritative BRAIN SELF_CORRELATION PASS at 0.548 vs `LLR0n261` (limit 0.70).
- Labeled on the BRAIN platform via `brain_metadata.py`.

## Risk assessment

Top peer `LLR0n261` (S=2.51) at 0.548 — comfortable headroom below the 0.70
gate; no Sharpe-premium escape needed. Lowest-correlation EXCELLENT+ candidate
found after the event/leverage family was activated.

## Reviewer action

Submit on the BRAIN platform if desired, then set `status: SUBMITTED` and flip
`data/book/0m7lnAEr.md` to `status: ACTIVE`. If declined, set `status: REJECTED`.
