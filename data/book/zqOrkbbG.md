---
alpha_id: "zqOrkbbG"
name: "Accrued Liability Analyst Buzz"
tags:
  - "accrual"
  - "analyst"
  - "buzz"
  - "session_20260613-001"
submitted: null
session: "20260613-001"
grade: "EXCELLENT"
sharpe: 1.82
fitness: 2.01
turnover: 0.1176
expression: "ts_decay_linear(rank(fn_accrued_liab_q / close) + rank(anl4_cfi_flag) + rank(anl4_bvps_flag) + rank(ts_mean(scl12_buzz, 5)), 5)"
family: "accrual_analyst_buzz"
neutralization: "SUBINDUSTRY"
decay: 6
self_corr_max: 0.6202
status: "ACTIVE"
brain_url: "https://platform.worldquantbrain.com/alpha/zqOrkbbG"
---

# Alpha: zqOrkbbG

## Expression

```
ts_decay_linear(rank(fn_accrued_liab_q / close) + rank(anl4_cfi_flag) + rank(anl4_bvps_flag) + rank(ts_mean(scl12_buzz, 5)), 5)
```

## Mechanism

This alpha combines accrued liabilities, analyst cash-flow/book-value revision
flags, and social buzz breadth. The likely mechanism is quality and financing
information diffusion: accrued liabilities and analyst revisions identify firms
where balance-sheet obligations and expectations are changing, while buzz adds a
coverage/attention stabilizer without the high self-correlation of direct
revision-reversal terms.

## Self-Correlation Profile

BRAIN self-correlation check passed at 0.6202, with top observed peer
`xARzmVEW` at 0.620. This is below the 0.70 threshold and does not require the
Sharpe-premium escape.

## Post-Submission

BRAIN check reported this alpha as ACTIVE on 2026-06-17. The exact submission
date was not inferred from the API output.
