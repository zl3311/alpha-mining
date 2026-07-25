---
category: "pattern"
discovered: "20260611-001"
applicable_to: "fundamental6, event_detection"
---

# Event Magnitude via abs(ts_delta) Template

Novel event detection template — captures the SIZE of fundamental field changes
regardless of direction. Markets underreact to the magnitude of inventory events.

## Template

```
rank(abs(ts_delta(FIELD / close, D))) + rank(-1 * equity / assets) + rank(STABILIZER / close)
```

| Parameter | Recommended | Notes |
|-----------|-------------|-------|
| FIELD | fnd6_itci | Only itci produces strong signal; drlt/acdo/fatl/dlto/ivaco alone are INFERIOR |
| D (event window) | 3 | d=3 marginally > d=5 > d=10 > d=22; all produce GOOD+ standalone |
| STABILIZER | fnd6_drlt | Fixes LOW_SUB_UNIVERSE_SHARPE; ivaco also works (lower fitness) |
| Platform decay | 6 | Default; decay=10 untested at submission |
| Neutralization | SUBINDUSTRY | MARKET kills leverage component (S drops 50%+) |
| Universe | TOP3000 | |

## Best Results

| Alpha | Expression | S | F | BRAIN | Self-Corr |
|-------|-----------|---|---|-------|-----------|
| 0m8GV1Pp | d=3 + leverage + drlt | 2.64 | 2.77 | ALL PASS | 0.549 PASS |
| le0gY6Ze | d=5 + leverage + drlt | 2.62 | 2.74 | ALL PASS | 0.547 PASS |
| 88LGM8Ga | d=5 + leverage + ivaco | 2.64 | 2.69 | ALL PASS | 0.605 PASS |

## Mechanism

`abs(ts_delta(itci/close, D))` detects the magnitude of inventory/total capital
investment ratio changes. Large changes in EITHER direction signal a fundamental
event — inventory build (anticipating demand) or drawdown (fulfilling
demand/writeoff). The market underreacts to event SIZE, not direction.

Combined with leverage premium (high-debt firms earn subindustry risk premium)
and a stabilizer factor (drlt provides broad coverage across subindustries).

## Why abs(ts_delta) Works for itci but Not Other Fields

Inventory (itci) has discrete event dynamics — most of the time it's stable,
with occasional large jumps from supply chain events, production changes, or
writedowns. Other fundamental6 fields change more gradually, so the abs(delta)
template adds less information vs their level.

## What Doesn't Work

| Variant | Result |
|---------|--------|
| `zscore(abs(ts_delta(...)))` instead of `rank(abs(ts_delta(...)))` | Kills Sharpe (1.99→1.45) |
| `abs(ts_delta(drlt, 5))` standalone | AVERAGE S=1.27 |
| `abs(ts_delta(acdo, 5))` standalone | INFERIOR |
| `abs(ts_delta(dlto, 5))` standalone | AVERAGE S=1.27 |
| MARKET neutralization | 0 gate-passers |
| vol-gating the event signal | AVERAGE (hurts) |
| 2-factor (no stabilizer) | SPECTACULAR but FAILS SUB_UNIVERSE |
| `+ rank(ts_mean(scl12_buzz, 5))` as stabilizer | AVERAGE (buzz hurts fitness) |

## Critical Constraints

- **SUBINDUSTRY only** — MARKET kills leverage (and event signal is intra-industry)
- **Must include a stabilizer third factor** — 2-factor version always fails
  LOW_SUB_UNIVERSE_SHARPE (itci has uneven subindustry performance)
- **drlt is the best stabilizer** — acdo also works (F=2.80!) but fails SUB_UNIVERSE;
  fatl/dlto work but lower grade (EXCELLENT not SPECTACULAR)
- After submitting ONE event+leverage alpha, all others blocked by mutual self-corr
