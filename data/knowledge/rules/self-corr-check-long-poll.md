---
category: "rule"
severity: "critical"
scope: "infrastructure"
discovered: "20260716 (self-corr /check polling harden; sessions 20260703–20260716)"
---

# BRAIN `/check` Self-Corr Requires Long-Polling

## The rule

`GET /alphas/{id}/check` is asynchronous for `SELF_CORRELATION`. Clients must
poll until that sub-check is terminal (`PASS` / `FAIL` / `ERROR`), not return
on the first non-empty checks payload.

Long-poll signal (same family as PnL):

- Status `200`
- Empty (or near-empty) body
- `Retry-After` header present → wait and retry

Also keep polling when the body includes checks but
`SELF_CORRELATION.result == "PENDING"`.

## Peak-load behavior

Observed across mining sessions 20260703–20260716:

| Symptom | Notes |
|---------|--------|
| PENDING 9–90+ minutes | Even ACTIVE control alphas can lag under load |
| HTTP 502 / 503 | Gateway degradation — retry, do not abort |
| HTTP 429 | Honor `Retry-After` |
| `httpx.ConnectTimeout` | Transient connectivity — retry |

Same alpha IDs often resolve cleanly later (off-peak or after platform recovery).
Default client budget: **900 seconds** (`--max-wait-seconds`); raise under load.

## API facts (confirmed 2026-07-16)

- `POST /alphas/{id}/check` → **HTTP 405** Method Not Allowed (GET only)
- Submitted alphas: `/check` returns only `ALREADY_SUBMITTED` (no
  `SELF_CORRELATION`); use `GET /alphas/{id}/correlations/self` for peers
- `GET /alphas/{id}` (alpha detail) can still show `SELF_CORRELATION: PENDING`
  after `/check` has already returned PASS/FAIL — do not use detail for
  authoritative self-corr
- Terminal results include `ERROR` (distinct from FAIL); do not coerce
  PENDING/ERROR to FAIL in printers

## Code reference

- Local CLI: `scripts/pnl_correlation.py` — `fetch_brain_check()` /
  `fetch_brain_self_corr()` with wall-clock budget and 5xx/timeout retry
- HF server: `server/app/brain_client.py` — `check_self_correlation()`
- Sibling rule: `data/knowledge/rules/pnl-long-poll-required.md`
