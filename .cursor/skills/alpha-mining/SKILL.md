---
name: alpha-mining
description: >-
  FASTEXPR operator reference, simulation settings, and CLI commands for
  WorldQuant BRAIN. This is a reference skill, not a workflow driver.
  For mining workflows, read the mining-session skill instead.
  Trigger on: operator, FASTEXPR, expression syntax, simulation settings,
  CLI command, submit alpha, list alphas, screen, ingest paper.
---

# Alpha Mining Reference

For the mining workflow, read the `mining-session` skill.
This file is an operator and CLI reference only.

## CLI Commands

All commands use `uv run python3 -m alpha_mining` from the project root.

### Simulate an expression on BRAIN
```bash
uv run python3 -m alpha_mining -e "<FASTEXPR expression>" -s cursor
```

### Pre-screen locally (free, seconds)
```bash
uv run python3 -m alpha_mining --screen "rank(ts_mean(close, 10) - close)"
uv run python3 -m alpha_mining --screen "expr1" --screen "expr2" --screen "expr3"
```
Verdicts: PROMISING (IC > 0.015) -> send to BRAIN. WEAK (IC > 0.01) -> maybe. DEAD -> skip.

### List and submit alphas
```bash
uv run python3 -m alpha_mining --list-alphas
uv run python3 -m alpha_mining --submit-alpha <brain_alpha_id> --submit-name "name" --submit-tags "tag1,tag2"
```

WARNING: `--submit-alpha` sets metadata AND performs the official scoring
submission (irreversible, consumes a submission slot). Do NOT use it just to
label an alpha.

### Set metadata WITHOUT submitting

Alphas simulated through the HF queue exist on the platform but are unlabeled.
To set name/tags/description only (no submission):

```bash
uv run python3 scripts/brain_metadata.py --alpha-id <brain_alpha_id> \
  --name "name" --tags "tag1,tag2" --desc "mechanism summary"
# or derive from a book entry:
uv run python3 scripts/brain_metadata.py --alpha-id <brain_alpha_id> --from-book data/book/<id>.md
```

### View results
```bash
uv run python3 -m alpha_mining --stats
uv run python3 -m alpha_mining --top 10
```

### Ingest a research paper
```bash
uv run python3 -m alpha_mining --ingest <path_to_pdf>
```

## Default Simulation Settings

| Setting | Default | Override flag |
|---------|---------|---------------|
| Region | USA | `--region` |
| Universe | TOP3000 | `--universe` |
| Decay | 6 | `--decay` |
| Neutralization | SUBINDUSTRY | `--neutralization` |
| Language | FASTEXPR | `-l` |
| Delay | 1 | (not overridable via CLI) |
| Truncation | 0.08 | (not overridable via CLI) |

## FASTEXPR Operator Quick Reference

### Data fields
`close`, `open`, `high`, `low`, `volume`, `vwap`, `returns`, `adv20`, `cap`, `sharesout`

### Cross-sectional operators
`rank(x)`, `zscore(x)`, `scale(x)`, `quantile(x)`, `reverse(x)`

### Time-series operators
`ts_delta(x,d)`, `ts_mean(x,d)`, `ts_rank(x,d)`, `ts_std_dev(x,d)`,
`ts_corr(x,y,d)`, `ts_arg_max(x,d)`, `ts_arg_min(x,d)`, `ts_delay(x,d)`,
`ts_decay_linear(x,d)`, `ts_zscore(x,d)`, `ts_sum(x,d)`

### Group operators
`group_neutralize(x,g)`, `group_rank(x,g)`, `group_zscore(x,g)`

Groups: `market`, `sector`, `industry`, `subindustry`

### Conditional
`trade_when(cond, alpha, exit_cond)`

### Operator naming gotchas (cause HTTP 400 if wrong)

| Wrong | Correct |
|-------|---------|
| `delay(x, d)` | `ts_delay(x, d)` |
| `correlation(x, y, d)` | `ts_corr(x, y, d)` |
| `ts_argmax(x, d)` | `ts_arg_max(x, d)` |
| `ts_argmin(x, d)` | `ts_arg_min(x, d)` |
| `delta(x, d)` | `ts_delta(x, d)` |
| `stddev(x, d)` | `ts_std_dev(x, d)` |
| `decay_linear(x, d)` | `ts_decay_linear(x, d)` |

## Submission Gates (USA TOP3000)

An alpha must pass ALL of these:
- Sharpe >= 1.25
- Fitness >= 1.0 (`sqrt(abs(returns) / max(turnover, 0.125)) * sharpe`)
- Turnover between 1% and 70%
- All 8 BRAIN checks PASS (see `brain-check` skill)
- Self-correlation < 0.7 vs submitted book, OR candidate Sharpe >= 1.10x max correlated peer Sharpe (see `pnl-correlation` skill and `data/knowledge/rules/self-corr-threshold.md`)
- Yearly consistency (aggregate passing is not sufficient)

## Related Skills

- **mining-session**: The workflow driver. Start here.
- **hf-server**: How to use the HF submission queue
- **brain-check**: BRAIN submission check details
- **pnl-correlation**: Self-correlation analysis
- **econ-reasoning**: Economic mechanism taxonomy
