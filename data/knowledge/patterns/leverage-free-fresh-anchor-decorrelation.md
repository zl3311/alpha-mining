---
pattern: "leverage-free-fresh-anchor-decorrelation"
discovered: "20260716-001"
applicable_to: "fresh fundamental6/fundamental2 anchors when the classic event-magnitude stabilizer stack (leverage+ivaco+drlt+flag+buzz) is self-corr BLOCKED"
confidence: "high (2 fresh anchors tested; aknmG1M6 subsequently BRAIN-confirmed at 0.6181 PASS and ACTIVE, and the leverage-drop lever independently reproduced by N1rlJ7mq at 0.6903 PASS)"
best_alpha_id: "aknmG1M6"
best_sharpe: 2.29
best_fitness: 2.26
best_self_corr_local: 0.618
---

# Pattern: Drop Leverage + drlt, Double-Weight ivaco + Buzz, Use Two Fresh Anchors

## The problem

By 2026-07-16 the classic event-magnitude stabilizer stack (`-1*equity/assets`
+ `fnd6_ivaco` + `fnd6_drlt`/`fnd6_fatl` + any `anl4_*_flag` +
`ts_mean(scl12_buzz,d)*(-1*returns)`) is confirmed BLOCKED for self-corr
regardless of anchor freshness **whenever the leverage leg is present** (see
rule `stabilizer-stack-block-generalizes-beyond-pstkrv.md`; the rule was
originally written without the leverage qualifier and narrowed on 20260719-001,
once `N1rlJ7mq` was found to pass at 0.6903 while retaining `drlt` and an
analyst flag). A fresh anchor alone,
or with only 1-2 other fresh anchors, caps at AVERAGE grade (F~1.0-1.3) —
insufficient fitness. Removing shared legs for decorrelation trades directly
against fitness.

## The fix

1. Pick TWO fresh, small-redundancy-cluster anchors (not one) — e.g.
   `fnd6_cld2` (cluster #14, 2 members) and `fnd6_fopo` (cluster #31, 14
   members, none previously used), both in ratio form (`F / close`), NOT
   the `abs(ts_delta(...))` event-magnitude transform (which underperformed
   the plain ratio for both fields this session).
2. Keep only TWO of the classic shared legs — `fnd6_ivaco` and
   `ts_mean(scl12_buzz, d) * (-1 * returns)` — and DROP `-1*equity/assets`
   and `fnd6_drlt`/`fnd6_fatl`/any analyst flag entirely.
3. Double-weight BOTH retained shared legs (`2 * rank(fnd6_ivaco/close)` and
   `2 * rank(ts_mean(scl12_buzz,10)*(-1*returns))`) to recover the fitness
   lost by dropping leverage/drlt.
4. Sweep the buzz window: 10 outperformed 5 and 20 in this test (F=2.26 vs
   2.03 and 2.13 respectively) — window=10 is the new default to try first
   for this specific 4-leg skeleton.

```
ts_decay_linear(rank(ANCHOR_1 / close) + rank(ANCHOR_2 / close) + 2 * rank(fnd6_ivaco / close) + 2 * rank(ts_mean(scl12_buzz, 10) * (-1 * returns)), 5)
```

## Evidence (session 20260716-001, `fnd6_cld2` + `fnd6_fopo`)

| Variant | S | F | T | Local self-corr |
|---------|---|---|---|------------------|
| Full stack incl. leverage+drlt (baseline, BLOCKED) | 1.87-2.03 | 1.87-2.03 | 9-11% | 0.775 |
| Drop leverage+drlt, keep 1x ivaco+buzz | 1.99 | 1.93 | 9.9% | GOOD, not EXCELLENT |
| Drop leverage+drlt, 2x ivaco + 2x buzz(w5) | 2.21 | 2.05 | 15.8% | 0.655 |
| Drop leverage+drlt, 1x ivaco + 2x buzz(w20) | 2.23 | 2.13 | 15.1% | 0.641 |
| **Drop leverage+drlt, 2x ivaco + 2x buzz(w10)** | **2.29** | **2.26** | **11.9%** | **0.618** (best) |

Local self-corr dropped from 0.775 (blocked baseline) to 0.618 (best variant)
— a 0.157 reduction — while fitness simultaneously IMPROVED from 2.03 to
2.26. This is a genuine free lunch relative to the blocked baseline, not a
fitness-for-correlation tradeoff, because leverage/drlt were contributing
more to shared correlation than to unique fitness once TWO fresh anchors
plus double-weighted ivaco/buzz are already present.

## When to use

- When a fresh anchor's full-stack form reaches EXCELLENT fitness but is
  self-corr BLOCKED (>0.75) against the book's event-magnitude family.
- Requires TWO fresh anchors (a single fresh anchor + this 2-leg stabilizer
  set capped at GOOD, F~1.6-1.9, in this session's tests) — budget for
  finding a second orthogonal fresh anchor before expecting EXCELLENT.

## Caveats — read before reusing

- **0.618-0.655 local corr is still in the "RISKY" uncertainty band**, not a
  confident PASS. `self-corr-pnl-gap.md` warns local estimates can
  underestimate BRAIN's true value by 1.45-1.6x when raw fields are shared
  verbatim — this candidate DOES share `ivaco` and `buzz*(-1*returns)`
  verbatim with 4-6 other book members, so some gap is plausible even though
  the shared-leg count is lower than the confirmed-BLOCKED full-stack cases.
- **Now BRAIN-confirmed.** The `/check` endpoint returned PENDING or timed out
  throughout discovery (20+ minutes, 8 attempts, ending in `ConnectTimeout`
  amid the platform degradation also reported by sessions `20260715-002`/`003`),
  so the 0.618 figure was a local estimate at the time. It has since resolved:
  `SELF_CORRELATION {result: PASS, value: 0.6181}`, and `aknmG1M6` is ACTIVE.
  The local estimate was accurate to within 0.001, another ~1.0x data point for
  this family.
- Dropping ivaco or buzz (not just de-weighting) collapses fitness to
  AVERAGE (F<=1.27) — both legs, at 2x weight, are necessary; this is not a
  fully leg-free solution, just a leverage/drlt/flag-free one.
