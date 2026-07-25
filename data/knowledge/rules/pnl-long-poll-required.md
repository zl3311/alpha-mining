---
category: "rule"
severity: "critical"
scope: "infrastructure"
discovered: "20260705 (PnL backfill bug fix)"
---

# BRAIN PnL Endpoint Requires Long-Polling

## The rule

`GET /alphas/{id}/recordsets/pnl` uses a long-poll pattern. The first request
often returns `HTTP 200 + empty body + Retry-After: 1.0`. This means "generating,
try again in 1 second" — NOT "no PnL available."

Must retry whenever:
- Status is 200
- Body is empty (< 10 bytes)
- `Retry-After` header is present

Genuine "no PnL" = 200 + empty body + NO `Retry-After` header.

## Key facts

- ALL simulated alphas have PnL regardless of grade (INFERIOR included)
- The long-poll typically resolves in 1-3 retries (1-3 seconds)
- Up to 8 retries is safe; genuine empties return immediately (no Retry-After)
- `x-ratelimit-remaining-hour: 0` with empty body = hard rate limit (different from long-poll)

## Historical context

Before this fix (deployed 2026-07-05), the HF server's `brain_client.get_alpha_pnl()`
treated all empty 200 responses with `remaining > 0` as "genuinely empty" and stored
them permanently in `pnl_metadata` as `status='empty'`. This caused ~24,000 alphas
to be incorrectly marked as having no PnL. The fix adds long-poll retry logic and
raises `PnlRateLimitError` for the hard rate-limit case.

## Code reference

- Server fix: `server/app/brain_client.py` — `get_alpha_pnl()` with 8-attempt loop
- Reset endpoint: `POST /v1/pnl/reset-status` (accepts list of alpha_ids)
- External reference: [brainapi-go-sdk](https://github.com/wh0amibjm/brainapi-go-sdk)
  documents this pattern in "BRAIN protocol gotchas"
