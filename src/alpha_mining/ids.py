"""
Globally unique entity ID generation for multi-client access.

Format: <prefix>_<unix_timestamp>_<6-char hex>
  - prefix: entity type (sess, paper, hyp, alpha, sim, result)
  - unix_timestamp: seconds since epoch (sortable by creation time)
  - 6-char hex: random bytes for uniqueness within the same second

Examples:
  paper_1747388400_a1b2c3
  hyp_1747388502_x4y5z6
  alpha_1747389100_m7n8o9

These IDs are stable across clients (Cursor, web app, chatbot, cloud scraper)
and self-describing (the prefix identifies the entity type).
Integer auto-increment PKs remain for internal DB joins.
"""

from __future__ import annotations

import os
import time

PREFIXES = {
    "session": "sess",
    "paper": "paper",
    "paper_image": "pimg",
    "hypothesis": "hyp",
    "alpha": "alpha",
    "simulation": "sim",
    "result": "result",
}


def generate_entity_id(prefix: str) -> str:
    """
    Generate a globally unique entity ID.

    Args:
        prefix: Entity type prefix (e.g. "paper", "hyp", "alpha").
            Can be a full name (looked up in PREFIXES) or a raw prefix.

    Returns:
        ID string like "paper_1747388400_a1b2c3".
    """
    short = PREFIXES.get(prefix, prefix)
    ts = int(time.time())
    hash_part = os.urandom(3).hex()
    return f"{short}_{ts}_{hash_part}"


def parse_entity_id(entity_id: str) -> tuple[str, int, str]:
    """
    Parse an entity ID into its components.

    Returns:
        Tuple of (prefix, timestamp, hash).

    Raises:
        ValueError: If the ID format is invalid.
    """
    parts = entity_id.split("_")
    if len(parts) < 3:
        raise ValueError(f"Invalid entity ID format: {entity_id}")
    prefix = parts[0]
    try:
        ts = int(parts[1])
    except ValueError:
        raise ValueError(f"Invalid timestamp in entity ID: {entity_id}")
    hash_part = "_".join(parts[2:])
    return prefix, ts, hash_part


def entity_type(entity_id: str) -> str:
    """Extract the entity type from an ID prefix."""
    prefix = entity_id.split("_")[0]
    reverse = {v: k for k, v in PREFIXES.items()}
    return reverse.get(prefix, prefix)
