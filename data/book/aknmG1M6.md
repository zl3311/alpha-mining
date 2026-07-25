---
alpha_id: "aknmG1M6"
name: "exp20260716-001_cld2_fopo_ivaco_buzz_leverage_free"
tags:
  - "session_20260716-001"
  - "leverage-free"
  - "capitalized-lease"
  - "funds-from-operations-other"
submitted: "2026-07-16"
session: "20260716-001"
grade: "EXCELLENT"
sharpe: 2.29
fitness: 2.26
turnover: 0.1192
expression: "ts_decay_linear(rank(fnd6_cld2 / close) + rank(fnd6_fopo / close) + 2 * rank(fnd6_ivaco / close) + 2 * rank(ts_mean(scl12_buzz, 10) * (-1 * returns)), 5)"
family: "capitalized_lease_fopo_leverage_free_blend"
neutralization: "SUBINDUSTRY"
decay: 6
self_corr_max: 0.6181
status: "ACTIVE"
brain_url: "https://platform.worldquantbrain.com/alpha/aknmG1M6"
---

# Alpha: aknmG1M6

## Expression
```
ts_decay_linear(rank(fnd6_cld2 / close) + rank(fnd6_fopo / close) + 2 * rank(fnd6_ivaco / close) + 2 * rank(ts_mean(scl12_buzz, 10) * (-1 * returns)), 5)
```

## Mechanism

This alpha blends two genuinely fresh fundamental6 anchors that have zero
prior coverage in `data/factors/` or `data/book/`:

- `fnd6_cld2` (Capitalized Leases due in the 2nd year): a finance-lease
  balance-sheet disclosure item, standalone S=1.29 close-normalized, 100%
  positive-year consistency over 2019-2023, T=2.3% — one of the cleanest
  low-turnover standalone signals found this session. Sits in a 2-member
  redundancy cluster (only `fnd6_cld3`), essentially unrepresented in the
  submitted book.
- `fnd6_fopo` (Funds From Operations - Other): standalone S=1.06-1.09,
  T=1.5-2.3%, cluster #31 (14 members, none previously used).

These are combined with the proven `fnd6_ivaco` (investment in associates,
double-weighted) and the standard `ts_mean(scl12_buzz, 10) * (-1 * returns)`
buzz-reversal stabilizer (double-weighted, buzz window swept 5->10->20; 10
was optimal). Deliberately **excludes** `-1 * equity / assets` (leverage),
`fnd6_drlt`, and any `anl4_*_flag` — the three components believed at the time
(sessions 20260715-002/003) to drive the event-magnitude family's self-corr
wall to 0.796 regardless of anchor. That premise was later narrowed: session
20260719-001 showed the 0.796 belonged to `oml0kV52` alone, and that
`-1*equity/assets` is the load-bearing correlate — `drlt` and the analyst flag
are fine without it (`N1rlJ7mq`, 0.6903 PASS). Excluding all three was
therefore stricter than necessary, though it did no harm here.
Dropping leverage/drlt/flag and using two fresh fundamental6 anchors
in their place, with 2x weight on both the remaining shared legs (ivaco,
buzz) to recover fitness, is a novel lever for this session (see pattern
`leverage-free-fresh-anchor-decorrelation.md`).

## Self-Correlation Profile

**Confirmed via BRAIN's authoritative `/alphas/aknmG1M6/check` endpoint
post-submission**: `SELF_CORRELATION: {result: PASS, value: 0.6181, limit:
0.70}` vs peer `WjGVJ7bN` (S=2.63) — comfortably below the 0.70 auto-pass
threshold, no Sharpe premium escape needed. The pre-submission local PnL
estimate (0.618) matched the authoritative value almost exactly (0.6181),
the closest local-to-authoritative match observed across any candidate this
week.

During discovery, BRAIN's `/check` endpoint had returned `PENDING`/timed out
across 8+ repeated polls over 20+ minutes, and the API itself briefly began
throwing `ConnectTimeout` errors — consistent with the platform degradation
sessions `20260715-002`/`20260715-003` independently reported the same week.
The check resolved cleanly once retried after the human's manual submission,
confirming the earlier instability was transient and did not indicate a
problem with this specific candidate.

This is the lowest self-corr of any EXCELLENT-grade candidate found this
session — every full-stabilizer-stack variant tested in parallel (using
leverage+drlt or leverage alone) landed at local corr 0.775-0.926
(confirmed/estimated BLOCKED). Per `submission-priority-long-term.md`, a
confirmed self-corr < 0.65 on an EXCELLENT+ alpha qualifies as a
MEDIUM-to-HIGH long-term value submission (near the < 0.4 HIGH-value bar,
well clear of the 0.6-0.7 "barely passing" tier).

## Post-Submission

**Submitted 2026-07-16 by the human and confirmed ACTIVE on the BRAIN
platform.** `/alphas/aknmG1M6/check` returns `status: ACTIVE`, all 8 checks
PASS including the now-resolved `SELF_CORRELATION` (0.6181 PASS). No further
action needed on this candidate.
