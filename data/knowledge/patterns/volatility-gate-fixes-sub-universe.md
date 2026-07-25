---
pattern: "volatility-gate-fixes-low-sub-universe"
discovered: "20260617-001"
applicable_to: "multi-leg blends with strong overall Sharpe but LOW_SUB_UNIVERSE_SHARPE failure"
confidence: "high"
---

# Pattern: Volatility-Regime Gate Repairs LOW_SUB_UNIVERSE_SHARPE

## The problem

A multi-leg blend whose value/event legs (e.g. `fnd6_itci/close`, `fnd6_acdo`)
concentrate signal in smaller/mid caps can have strong overall Sharpe yet FAIL
`LOW_SUB_UNIVERSE_SHARPE` (the liquid sub-universe Sharpe is below ~43% of the
headline). Adding dense breadth legs (`open/close-1`, `ts_mean(scl12_buzz,5)`,
`sales_estimate_count`) raises sub-universe Sharpe but also raises overall
Sharpe, so the ~43% bar moves up in lockstep and the check still fails.

## The fix

Wrap the smoothed blend in a realized-volatility regime gate:

```
trade_when(
  ts_std_dev(returns, 20) > 0.02,
  ts_decay_linear(<multi-leg blend>, 5),
  ts_std_dev(returns, 20) < 0.01
)
```

The gate concentrates exposure into high-volatility periods, where the liquid
sub-universe Sharpe is structurally higher. This lifts the sub-universe ratio
ABOVE the ~43% bar while preserving EXCELLENT grade — and, as a bonus, it
trades less often, which LOWERED self-correlation in the observed case
(0.61 -> 0.55).

## Concrete discovery

`0m7lnAEr` (EXCELLENT, S=2.08, F=2.01) = volatility-gated
`IV270_spread + itci/close + acdo + anl4_netdebt_flag + ts_mean(buzz,5) + open/close-1`.
The ungated base (`e7rwP2wd`, SPECTACULAR S=2.36) and the breadth-augmented
ungated variants (`E5w7AKwL` S=2.77) all FAILED `LOW_SUB_UNIVERSE_SHARPE`; only
the volatility-gated form passed all 8 checks. Authoritative self-corr PASS at
0.548 vs `LLR0n261`.

## When to use

Apply to any blend that passes every check EXCEPT `LOW_SUB_UNIVERSE_SHARPE`,
especially when the signal leans on small/mid-cap fundamental legs. Prefer
raw breadth stabilizers (NOT `flag*(-ret)` or `buzz*(-ret)` reversal drivers,
which inflate self-correlation).
