---
alpha_id: "O0Z6NE0b"
name: "msaq_event_magnitude_ivaco_drlt_ffo_buzz_market"
status: "ACTIVE"
submitted: "2026-07-14"
session: "20260713-001"
grade: "EXCELLENT"
sharpe: 2.10
fitness: 2.02
turnover: 0.127
expression: "ts_decay_linear(rank(abs(ts_delta(fnd6_newqv1300_msaq / close, 3))) + rank(fnd6_ivaco / close) + rank(fnd6_drlt / close) + rank(anl4_ffo_flag) + rank(ts_mean(scl12_buzz, 10) * (-1 * returns)), 5)"
family: "msaq_event_magnitude_market_neutral"
fields:
  - "fnd6_newqv1300_msaq"
  - "fnd6_ivaco"
  - "fnd6_drlt"
  - "anl4_ffo_flag"
  - "scl12_buzz"
  - "returns"
neutralization: "MARKET"
decay: 6
delay: 1
truncation: 0.08
region: "USA"
universe: "TOP3000"
self_corr_max: 0.528
self_corr_peer: "closest ACTIVE peer within event-magnitude family (WjGVJ7bN-lineage), MARKET-neutralized"
self_corr_result: "PASS (confirmed post-submission: BRAIN status ACTIVE, /alphas/{id}/check returns f=0/ALL PASS; platform acceptance is itself the authoritative SELF_CORRELATION confirmation, consistent with the wpl5eP5v/YP0bLdzA/WjGVJ7bN precedent where the check is no longer listed as a distinct sub-check once ACTIVE)"
self_corr_method: "local_pnl_correlation_vs_46_active_book_entries; BRAIN authoritative /alphas/{id}/check and /correlations/self both returned SELF_CORRELATION: PENDING across repeated polling (10 retries x multiple attempts spanning >20 minutes) -- consistent with the platform-latency pattern documented for this candidate family in session 20260711-001"
self_corr_caveat: "The identical expression under SUBINDUSTRY (alpha KP9V7YLz, same session) scored local PnL corr 0.646 (RISKY) against the same event-magnitude family; switching to MARKET neutralization dropped it to 0.528 (SAFE), consistent with the market-neut-decorrelation pattern's documented 0.10-0.20 correlation reduction. (The original 'Re-verify with a fresh /check poll before submission' note is now moot -- this alpha was submitted 2026-07-14 and is ACTIVE.)"
tags:
  - "fnd6_newqv1300_msaq"
  - "anl4_ffo_flag"
  - "event_magnitude"
  - "market_neutral"
  - "session_20260713-001"
brain_url: "https://platform.worldquantbrain.com/alpha/O0Z6NE0b"
---

# O0Z6NE0b — MSAQ Event-Magnitude + Ivaco + Drlt + FFO-Revision + Buzz (MARKET-neutral)

## Expression

```
ts_decay_linear(rank(abs(ts_delta(fnd6_newqv1300_msaq / close, 3))) + rank(fnd6_ivaco / close) + rank(fnd6_drlt / close) + rank(anl4_ffo_flag) + rank(ts_mean(scl12_buzz, 10) * (-1 * returns)), 5)
```

## Mechanism

Extends the proven `event-magnitude-abs-ts-delta` template (previously validated
on `fnd6_itci`, `fnd6_newqv1300_ppegtq`, `fnd6_tlcf`, `fnd6_txw`,
`fn_liab_fair_val_l2_q`) to a genuinely fresh anchor field never used in any
prior book entry or factor profile:

1. **OCI marketable-security event magnitude** (`rank(abs(ts_delta(fnd6_newqv1300_msaq / close, 3)))`):
   `fnd6_newqv1300_msaq` (Accumulated Other Comprehensive Income — Marketable
   Security Adjustments) measures unrealized mark-to-market gains/losses on
   available-for-sale securities. A large 3-day swing in this value relative to
   price signals a re-marking event (rate shock, portfolio reallocation, or an
   accounting reclassification) that the market underreacts to, independent of
   direction — the same underlying mechanism as the fair-value-liability and
   inventory event-magnitude siblings already in the book.
2. **Investing-activities-other** (`rank(fnd6_ivaco / close)`) and **deferred
   revenue, long-term** (`rank(fnd6_drlt / close)`): the family's standard
   sub-universe-breadth stabilizers.
3. **FFO analyst-revision flag** (`rank(anl4_ffo_flag)`): funds-from-operations
   forecast-revision flag, never used in any prior book entry. Standalone
   AVERAGE via `rank(ts_delta(F,5))` (S=1.35, F=1.39); used here in raw
   `rank()` form as an analyst-conviction densifier, following the
   `event-magnitude-fresh-stabilizer` pattern (swap one shared leg for a field
   unused anywhere in the family to decorrelate cheaply).
4. **Buzz-reversal stabilizer** (`rank(ts_mean(scl12_buzz, 10) * (-1 * returns))`):
   100%-coverage sentiment-reversal factor; lifts fitness at low correlation
   cost per the `event-magnitude-buzz-boost` pattern (buzz window 10 tuned
   marginally better than the default 5 for this specific candidate).
5. **MARKET neutralization** (the key decorrelation lever this session): the
   identical 5-leg expression under the family's default SUBINDUSTRY
   neutralization (alpha `KP9V7YLz`, same session, S=2.83 F=2.49) scored a
   RISKY 0.646 local correlation against the existing event-magnitude family
   (whose `leverage + ivaco + buzz` skeleton is now shared by 6+ ACTIVE
   siblings). Switching to MARKET dropped correlation to 0.528 (SAFE) while
   only costing ~0.47 fitness (2.49 → 2.02) — the `market-neut-decorrelation`
   pattern's documented decorrelation-vs-fitness tradeoff, applied for the
   first time specifically to break the event-magnitude family's saturated
   skeleton (see new pattern:
   `data/knowledge/patterns/market-neutral-event-magnitude-escape.md`).

## Discovery Path (session 20260713-001, summary — full detail in session results.md)

1. **Round 1 (21 sims)**: tested genuinely novel operator-tree shapes flagged
   explicitly untested by prior sessions — directional gating of a fundamental
   by another SLOW fundamental's own trend (not price/volume), `ts_arg_max`
   recency-of-extreme, multi-horizon regime-divergence spreads, dynamic
   correlation between two non-return series, `quantile()` bucketing — on two
   fresh anchors (`fnd6_newqv1300_msaq`, `current_ratio`). All novel structures
   capped at INFERIOR/AVERAGE (best: directional-gating hybrid, S=1.83 F=1.32).
   The proven event-magnitude template applied to `msaq` immediately reached
   EXCELLENT aggregate metrics (`vRlY5MPd`, S=2.59 F=2.43) but authoritative
   BRAIN `/check` confirmed **FAIL** at self-corr 0.8827 vs `WjGVJ7bN` — msaq is
   economically close enough to the family's existing tax/flow-adjustment
   anchors that it inherits high correlation, similar to the prior `dltis`
   dead-end.
2. **Rounds 2-3 (20 sims)**: amplified the novel directional-gating structure
   (`rank(-1*equity/assets) * sign(ts_delta(msaq,d)) + stabilizer(s)`), which
   authoritatively confirmed self-corr **PASS at 0.5667** (`QPVWnxKK`) — but
   fitness capped at GOOD (F<=1.88) regardless of window/decay/leg tuning;
   turnover stayed structurally high (18-27%) because the discrete `sign()`
   gate flips too often.
3. **Round 4 (8 sims)**: tried `current_ratio` (a liquidity ratio, economically
   distinct from tax/debt items) as the event-magnitude anchor instead of
   `msaq`. Reached EXCELLENT (`gJMr9zAK`, S=2.20 F=2.06) but local PnL
   correlation was **worse** (0.922) than `msaq` — confirming the correlation
   driver is now the family's shared `leverage + ivaco + buzz` skeleton itself,
   not anchor-field economic proximity. Recorded as a new rule (see
   `data/knowledge/rules/event-magnitude-leverage-ivaco-skeleton-saturated.md`).
4. **Round 5 (6 sims)**: removed `leverage` (`-1*equity/assets`) entirely from
   the blend to escape the shared skeleton. Removing leverage AND ivaco
   together collapsed fitness to INFERIOR (F<=0.67). Removing only leverage
   while keeping `ivaco + drlt` together preserved GOOD-grade fitness
   (`P03PGeex`, S=2.03 F=1.70, turnover only 6.5%) with local corr 0.590 — an
   improvement but still not clearly SAFE given shared-field inflation.
5. **Round 6 (4 sims)**: added the buzz stabilizer back to the leverage-free
   `ivaco + drlt + ffo_flag` combo. Reached **EXCELLENT** (`KP9V7YLz`, S=2.83
   F=2.49) — the best fitness of the session — but local corr was RISKY at
   0.646 (top mutual peer 0.81 with a same-round sibling).
6. **Round 7-8 (9 sims)**: applied MARKET neutralization to `KP9V7YLz`'s exact
   expression (the family's leverage-premium mechanism requires SUBINDUSTRY
   per `leverage-premium.md`, but this variant no longer uses leverage, so the
   usual MARKET penalty does not apply the same way). The MARKET variant
   dropped correlation to SAFE (0.527-0.528 across buzz-window tuning) while a
   `buzz window=10` tune recovered fitness back over the EXCELLENT threshold —
   **`O0Z6NE0b`**, EXCELLENT S=2.10 F=2.02 T=12.7%, self-corr 0.528 SAFE.

## Self-Correlation

Local PnL correlation vs the full 46-alpha ACTIVE book: **0.528** — comfortably
below the 0.70 auto-pass threshold, no Sharpe premium needed. The identical
expression under SUBINDUSTRY (`KP9V7YLz`) scored 0.646 (RISKY) against the same
peers — MARKET neutralization is the specific lever that produced the safe
margin here.

**Caveat (resolved)**: BRAIN's authoritative `/alphas/{id}/check` and
`/correlations/self` endpoints returned `SELF_CORRELATION: PENDING` across
repeated polling during the discovery session (consistent with the
platform-latency pattern first documented in session 20260711-001, where the
same endpoints lagged >90 minutes even for already-ACTIVE control alphas).
The check has since resolved in this alpha's favour — it was submitted
2026-07-14 and accepted, so no further verification is outstanding.

## BRAIN Checks

All 7 computable checks PASS (verified via `scripts/brain_check.py`):

| Check | Result |
|-------|--------|
| LOW_SHARPE | PASS (2.10 vs 1.25) |
| LOW_FITNESS | PASS (2.02 vs 1.00) |
| LOW_TURNOVER / HIGH_TURNOVER | PASS (12.7%, within 1-70%) |
| CONCENTRATED_WEIGHT | PASS |
| LOW_SUB_UNIVERSE_SHARPE | PASS |
| MATCHES_COMPETITION | PASS |
| SELF_CORRELATION | PASS (PENDING at session time; local estimate 0.528, since confirmed by platform acceptance) |

## Post-Submission

Submitted by the human on 2026-07-14 and confirmed **ACTIVE** on the BRAIN
platform. `/alphas/O0Z6NE0b/check` returns `status: ACTIVE`, grade EXCELLENT,
S=2.10, F=2.02, `f=0` (all computable checks PASS). As with `YP0bLdzA` and
`wpl5eP5v` in prior sessions, `SELF_CORRELATION` is no longer listed as a
distinct pending sub-check once ACTIVE — the platform's acceptance of the
submission is itself confirmation that the authoritative self-correlation
check passed, validating the MARKET-neutral leverage-drop escape route
(`data/knowledge/patterns/market-neutral-event-magnitude-escape.md`) as a
proven, not just locally-estimated, decorrelation technique.
