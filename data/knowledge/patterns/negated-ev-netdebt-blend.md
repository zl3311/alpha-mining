---
pattern: "negated-ev-netdebt-blend"
discovered: "20260707-001"
applicable_to: "negated-direction fundamental blends needing decorrelation from the ptpr+intraday book cluster"
example_alpha: "2rLRzov8"
---

# Pattern: Negated-EV + Netdebt-Flag Blend (decorrelation recipe)

## Template

```
ts_decay_linear(
  rank(-1 * enterprise_value / close)
  + rank(anl4_netdebt_flag)
  + rank(<cash_quality_field>)
  + rank(<balance_sheet_field>)
  + rank(open/close - 1),
  5
)
```

- `<cash_quality_field>`: `fnd6_cshtr` (cash-to-revenue) or `fnd6_csho` (operating cash flow)
- `<balance_sheet_field>`: `fnd6_drlt` (long-term deferred revenue) as used by
  the winning expression. `fnd6_dlto` is a distinct long-term-other-debt field,
  not a synonym for total debt; test it as a separate variant.

## When to Use

When a negated-fundamental blend needs to decorrelate from the book's saturated
`anl4_ptpr_flag + open/close - 1` cluster (LLR0n261, O0ZOJbaq, O0pl2znv). The key
decorrelation move is **replacing `anl4_ptpr_flag` with `anl4_netdebt_flag`** — a
less-used analyst flag — while keeping the irreplaceable overnight-gap component.

## Why it decorrelates

Self-corr is dominated by the shared analyst-flag + intraday components, not by the
fundamental anchor's sign. Swapping `ptpr_flag` → `netdebt_flag` changes the shared
component and drops self-corr from ~0.94 (ptpr variant) to 0.6495 (netdebt variant),
below the 0.7 auto-pass threshold. The negated `enterprise_value` anchor adds further
decorrelation because no book entry uses EV (positive or negated).

## Example

`2rLRzov8` (EXCELLENT, S=2.06, F=2.13, T=12.8%, self-corr 0.6495 PASS):

```
ts_decay_linear(rank(-1 * enterprise_value / close) + rank(anl4_netdebt_flag) + rank(fnd6_cshtr) + rank(fnd6_drlt) + rank(open/close - 1), 5)
```

Config: SUBINDUSTRY, decay 6, delay 1, truncation 0.08, TOP3000, USA.

## Caveats

- Self-corr lands in the 0.6–0.7 band (LOW long-term value) — submittable but
  consumes correlation headroom. To reach HIGH long-term value (< 0.4), a more
  orthogonal analyst flag or a non-intraday signal leg would be needed.
- The `open/close - 1` leg is irreplaceable (per 20260702-002 / 20260703-001
  lessons); do not remove it.
