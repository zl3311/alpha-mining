"""
Export simulation results to human-readable markdown files.

Writes to data/exports/{name}.md for Cursor review and git tracking.
"""

from __future__ import annotations

import json
import logging
from pathlib import Path

from .storage.db import AlphaDB

logger = logging.getLogger(__name__)

_EXPORT_DIR = Path("data/exports")

_TEMPLATE = """\
# {name}

**Expression:** `{expression}`
**Alpha ID:** {alpha_eid}

## Metrics

| Metric | Value |
|--------|-------|
| Sharpe | {sharpe:.3f} |
| Fitness | {fitness:.3f} |
| Turnover | {turnover:.1%} |
| Returns | {returns:.4f} |
| Drawdown | {drawdown:.4f} |
| Submittable | {submittable} |

## Simulation Config

```json
{config_json}
```

## BRAIN

- Simulation ID: {sim_eid}
- Platform URL: {platform_url}
"""


def export_result_markdown(
    row: dict,
    output_dir: Path = _EXPORT_DIR,
) -> Path:
    """
    Write a single result as a markdown file.

    Args:
        row: Dict from db.get_top_results() with joined alpha/simulation data.
        output_dir: Directory to write to.

    Returns:
        Path to the written file.
    """
    output_dir.mkdir(parents=True, exist_ok=True)

    name = row.get("name", "unnamed")
    safe_name = name.replace("/", "_").replace(" ", "_")[:80]

    sharpe = row.get("sharpe", 0)
    fitness = row.get("fitness", 0)
    turnover = row.get("turnover", 0)
    submittable = "Yes" if (sharpe >= 1.25 and fitness >= 1.0 and 0.01 <= turnover <= 0.70) else "No"

    config_raw = row.get("sim_config_json", "{}")
    try:
        config_json = json.dumps(json.loads(config_raw), indent=2)
    except (json.JSONDecodeError, TypeError):
        config_json = config_raw

    content = _TEMPLATE.format(
        name=name,
        expression=row.get("expression", ""),
        alpha_eid=row.get("alpha_eid", ""),
        sharpe=sharpe,
        fitness=fitness,
        turnover=turnover,
        returns=row.get("returns", 0),
        drawdown=row.get("drawdown", 0),
        submittable=submittable,
        config_json=config_json,
        sim_eid=row.get("sim_eid", ""),
        platform_url=row.get("platform_url", ""),
    )

    file_path = output_dir / f"{safe_name}.md"
    file_path.write_text(content, encoding="utf-8")
    logger.info("Exported %s", file_path)
    return file_path


async def export_top_results(
    db: AlphaDB,
    limit: int = 20,
    output_dir: Path = _EXPORT_DIR,
) -> list[Path]:
    """
    Export top results from the database to markdown files.

    Args:
        db: Active database connection.
        limit: Max number of results to export.
        output_dir: Directory to write to.

    Returns:
        List of paths to written files.
    """
    rows = await db.get_top_results(limit=limit)
    if not rows:
        logger.info("No results to export")
        return []

    paths = []
    for row in rows:
        path = export_result_markdown(row, output_dir)
        paths.append(path)

    logger.info("Exported %d results to %s", len(paths), output_dir)
    return paths
