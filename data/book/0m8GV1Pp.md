---
alpha_id: "0m8GV1Pp"
name: "event3d_leverage_drlt_blend"
tags:
  - "event_magnitude"
  - "leverage"
  - "fundamental6"
  - "fnd6_itci"
  - "fnd6_drlt"
  - "equity_assets"
  - "abs_ts_delta"
  - "session_20260611-001"
  - "spectacular"
  - "best_variant"
expression: "rank(abs(ts_delta(fnd6_itci / close, 3))) + rank(-1 * equity / assets) + rank(fnd6_drlt / close)"
sharpe: 2.64
fitness: 2.77
turnover: 0.041
grade: "SPECTACULAR"
family: "event_leverage_fundamental"
mechanism: "Novel event detection (3-day window) via absolute inventory change magnitude combined with financial leverage premium and deferred revenue quality. abs(ts_delta(itci/close, 3)) captures the SIZE of recent inventory events regardless of direction — market underreacts to event magnitude."
fields:
  - "fnd6_itci"
  - "equity"
  - "assets"
  - "fnd6_drlt"
neutralization: "SUBINDUSTRY"
decay: 6
universe: "TOP3000"
region: "USA"
self_corr_max: 0.5492
self_corr_peer: "MPbgqZ7o"
self_corr_verdict: "PASS"
brain_checks: "ALL_PASS"
status: "ACTIVE"
session: "20260611-001"
discovered: "2026-06-11"
brain_url: "https://platform.worldquantbrain.com/alpha/0m8GV1Pp"
---

# 0m8GV1Pp — Event Magnitude (3d) + Leverage + Deferred Revenue

## Expression

`rank(abs(ts_delta(fnd6_itci / close, 3))) + rank(-1 * equity / assets) + rank(fnd6_drlt / close)`

## Mechanism

Three-factor blend exploiting:
1. **Event magnitude (3-day)**: `abs(ts_delta(itci/close, 3))` — large inventory
   changes in either direction signal fundamental events the market underreacts
   to. The 3-day window captures more recent events than the 5-day variant.
2. **Leverage premium**: `rank(-1 * equity/assets)` — high-leverage firms earn
   a risk premium within their subindustry
3. **Deferred revenue quality**: `rank(drlt/close)` — high deferred revenue
   signals backlog strength and future revenue visibility. Also serves as a
   SUB_UNIVERSE stabilizer.

## Why Submittable

- Self-corr 0.5492 vs book (SAFE — well below 0.70 threshold)
- All 8 BRAIN checks PASS (verified via /alphas/{id}/check)
- SPECTACULAR grade, S=2.64, F=2.77
- Novel template family — abs(ts_delta) event detection is structurally unique
- Best variant found across window sweep (d=3,5,10), normalization sweep
  (rank vs zscore), third-factor sweep (drlt, acdo, fatl, dlto, ivaco), and
  wrapper sweep (raw, ts_decay_linear)

## Variant Family

| Alpha | S | F | Variant | BRAIN | Self-Corr |
|-------|---|---|---------|-------|-----------|
| 0m8GV1Pp | 2.64 | 2.77 | d=3 + drlt | ALL PASS | 0.5492 PASS |
| le0gY6Ze | 2.62 | 2.74 | d=5 + drlt | ALL PASS | 0.5466 PASS |
| pw7W23p6 | 2.62 | 2.74 | decay wrap + drlt | ALL PASS | — |
| 88LGM8Ga | 2.64 | 2.69 | d=5 + ivaco | ALL PASS | 0.6047 PASS |
| A13LA2GX | 2.20 | 2.50 | d=5 + fatl | ALL PASS | — |
| j2gV7oP9 | 2.25 | 2.44 | d=5 + dlto | ALL PASS | — |

## Risk Assessment

Top correlated peer is MPbgqZ7o (fundamental_sentiment, corr=0.549). Both use
fundamental6 dataset but different mechanism families. After submission, all
other event+leverage variants will be blocked by mutual self-corr.

## Post-Submission

BRAIN check reported this alpha as ACTIVE on 2026-06-17.
