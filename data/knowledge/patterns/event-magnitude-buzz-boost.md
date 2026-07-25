---
pattern: "event-magnitude-buzz-boost"
discovered: "20260709-001"
independently_confirmed: "20260710-001"
applicable_to: "event-magnitude-abs-ts-delta family (fundamental6/fundamental2 fields)"
confidence: "high"
best_alpha_id: "WjGVJ7bN"
best_sharpe: 2.63
best_fitness: 2.68
---

# Pattern: Buzz-Stabilizer 5th Leg Boosts Event-Magnitude Blends to SPECTACULAR

## Template

```
ts_decay_linear(rank(abs(ts_delta(FIELD / close, 3))) + rank(-1 * equity / assets) + rank(fnd6_ivaco / close) + rank(fnd6_drlt / close) + rank(ts_mean(scl12_buzz, 5) * (-1 * returns)), 5)
```

SUBINDUSTRY neutralization, platform decay=6, TOP3000.

## Evidence

| FIELD | Base 4-factor (no buzz) | +buzz 5th leg | Delta |
|-------|--------------------------|---------------|-------|
| `fnd6_tlcf` | GOOD S=1.89 F=1.79 (`blqLGagK`) | **EXCELLENT S=2.13 F=2.22** (`rKlo39p1`) | F +0.43 |
| `fnd6_txw` | GOOD S=2.01 F=1.78 (`e70xEm0M`) | **SPECTACULAR S=2.63 F=2.68** (`WjGVJ7bN`) | F +0.90 |
| `fnd6_mrct` | AVERAGE S=1.56 F=1.36 (`88QzbdZW`) | GOOD S=1.80 F=1.75 (`88Qe266a`) | F +0.39 |
| `fn_prepaid_expense_q` | AVERAGE S=1.54 F=1.40 (`E5Eex5l1`) | GOOD S=1.77 F=1.77 (`wplEWG9Y`) | F +0.37 |

Session `20260710-001` independently confirmed and generalized the discovery
from session `20260709-001` for `fnd6_tlcf` (GOOD F=1.79 → EXCELLENT F=2.22
with the same buzz 5th leg). Across 4 fields tested, the
buzz-stabilizer boost is consistent (+0.37 to +0.90 fitness) but the
MAGNITUDE varies a lot by field — `fnd6_txw` got by far the largest lift and
crossed a full grade tier (GOOD → SPECTACULAR), while `mrct`/`prepaid_expense_q`
only crossed AVERAGE → GOOD.

## Why It Works

`ts_mean(scl12_buzz, 5) * (-1 * returns)` has 100% coverage and captures a
temporally orthogonal (attention-driven contrarian) signal that fills the gap
days of the sparse quarterly fundamental event leg — the same mechanism as the
`buzz-stabilizer` pattern, but layered onto an already-4-factor blend instead
of a single factor. Because buzz is dense and daily while the event-magnitude
leg is sparse/quarterly, the two barely compete for the same PnL days, so the
combination is closer to additive-diversifying than diluting.

## Self-Correlation Note

Adding the buzz leg kept `fnd6_txw` submittable despite its 0.7096 correlation
with the now-ACTIVE `wpl5eP5v`: WjGVJ7bN clears the Sharpe-premium escape
(2.63 > 1.10 × 2.09). The anchor field's novelty still matters, but all
candidates require a fresh self-correlation check because later submissions
can change the top ACTIVE peer.

## When to Use

Apply this 5th-leg addition to ANY event-magnitude 4-factor blend
(`event-magnitude + leverage + ivaco + drlt`) that reaches GOOD/AVERAGE but not
EXCELLENT/SPECTACULAR on its own — it is close to a free upgrade. Always test
both the 4-factor and 5-factor (+buzz) forms; the lift size is field-dependent
and not guaranteed to cross a grade boundary.
