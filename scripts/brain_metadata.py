"""Set BRAIN alpha metadata (name, tags, description) WITHOUT submitting.

This is the canonical metadata-only path for the HF queue workflow. Alphas
simulated through the HF submission queue exist on the BRAIN platform but have
NO name/tags/description until they are labeled. The official submit flow
(`alpha_mining --submit-alpha`) couples metadata with scoring submission; this
script decouples them so an agent can label a candidate on the platform during
result-analysis, leaving the human to perform the final submit manually.

It wraps `BrainClient.set_alpha_properties` (PATCH /alphas/{id}) and never calls
the submit endpoint.

Usage:
    # Explicit metadata
    uv run python3 scripts/brain_metadata.py --alpha-id vRm07LP3 \
        --name "iv_spread_zscore_tsmean22_market" \
        --tags "options,iv_spread,H-006,session_20260604-001" \
        --desc "Call-put IV spread, MARKET neut, self-corr 0.309"

    # Read name/tags/description from a data/book/<id>.md frontmatter
    uv run python3 scripts/brain_metadata.py --alpha-id vRm07LP3 \
        --from-book data/book/vRm07LP3.md

    # Machine-readable confirmation
    uv run python3 scripts/brain_metadata.py --alpha-id vRm07LP3 \
        --from-book data/book/vRm07LP3.md --json
"""

import argparse
import asyncio
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

ROOT = Path(__file__).resolve().parent.parent


def _parse_frontmatter(path: Path) -> dict:
    """Read YAML frontmatter from a markdown file.

    Args:
        path: Path to a frontmatter markdown file.

    Returns:
        The parsed frontmatter mapping, or an empty dict if absent/malformed.
    """
    import yaml

    text = path.read_text()
    if not text.startswith("---"):
        return {}
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}
    try:
        return yaml.safe_load(parts[1]) or {}
    except yaml.YAMLError:
        return {}


def _metadata_from_book(book_path: Path) -> tuple[str, list[str], str]:
    """Derive name, tags, and description from a data/book/<id>.md file.

    The description falls back to the frontmatter `family` plus expression when
    no explicit description field is present, so the platform always gets a
    meaningful label.

    Args:
        book_path: Path to the book entry markdown file.

    Returns:
        A tuple of (name, tags, description). Missing fields are returned empty.
    """
    fm = _parse_frontmatter(book_path)
    name = str(fm.get("name", "") or "")
    tags_raw = fm.get("tags", []) or []
    tags = [str(t) for t in tags_raw] if isinstance(tags_raw, list) else []
    description = str(fm.get("description", "") or "")
    if not description:
        family = fm.get("family", "")
        expr = fm.get("expression", "")
        bits = [b for b in (family, expr) if b]
        description = " | ".join(bits)
    return name, tags, description


async def _run(alpha_id: str, name: str, tags: list[str], description: str, as_json: bool) -> int:
    """Apply metadata to a single alpha and verify the result.

    Args:
        alpha_id: BRAIN alpha ID (8-char, from the platform URL).
        name: Display name to set (empty to leave unchanged).
        tags: Tag list to set (empty list leaves unchanged).
        description: Description to set (empty to leave unchanged).
        as_json: When True, print a machine-readable JSON result.

    Returns:
        Process exit code: 0 on success, 1 on failure.
    """
    from alpha_mining.brain.client import BrainClient
    from alpha_mining.config import get_settings

    settings = get_settings()
    async with BrainClient(settings) as client:
        result = await client.set_alpha_properties(
            alpha_id,
            name=name,
            tags=tags or None,
            description=description,
        )

    url = f"https://platform.worldquantbrain.com/alpha/{alpha_id}"
    if isinstance(result, dict) and "error" in result:
        if as_json:
            print(json.dumps({"alpha_id": alpha_id, "ok": False, "error": result}, indent=2))
        else:
            print(f"ERROR setting metadata for {alpha_id}: {result}")
        return 1

    applied = {
        "alpha_id": alpha_id,
        "ok": True,
        "name": result.get("name", name),
        "tags": result.get("tags", tags),
        "url": url,
    }
    if as_json:
        print(json.dumps(applied, indent=2))
    else:
        print(f"Updated {alpha_id}")
        print(f"  name: {applied['name']}")
        print(f"  tags: {applied['tags']}")
        if description:
            print(f"  desc: {description[:100]}")
        print(f"  {url}")
    return 0


def main() -> None:
    """CLI entry point: parse args, resolve metadata source, apply via PATCH."""
    parser = argparse.ArgumentParser(
        description="Set BRAIN alpha metadata (name/tags/description) without submitting"
    )
    parser.add_argument("--alpha-id", required=True, help="BRAIN alpha ID to label")
    parser.add_argument("--name", default="", help="Display name to set")
    parser.add_argument("--tags", default="", help="Comma-separated tags")
    parser.add_argument("--desc", default="", help="Description text")
    parser.add_argument(
        "--from-book",
        help="Path to data/book/<id>.md; reads name/tags/description from frontmatter "
        "(explicit flags override book values)",
    )
    parser.add_argument("--json", action="store_true", help="Machine-readable JSON output")
    args = parser.parse_args()

    name, tags, description = args.name, [], args.desc
    if args.tags:
        tags = [t.strip() for t in args.tags.split(",") if t.strip()]

    if args.from_book:
        book_path = Path(args.from_book)
        if not book_path.is_absolute():
            book_path = ROOT / book_path
        if not book_path.exists():
            print(f"ERROR: book file not found: {book_path}", file=sys.stderr)
            sys.exit(1)
        b_name, b_tags, b_desc = _metadata_from_book(book_path)
        # Explicit flags take precedence over book-derived values.
        name = name or b_name
        tags = tags or b_tags
        description = description or b_desc

    if not (name or tags or description):
        print(
            "ERROR: nothing to set. Provide --name/--tags/--desc or --from-book.",
            file=sys.stderr,
        )
        sys.exit(1)

    exit_code = asyncio.run(_run(args.alpha_id, name, tags, description, args.json))
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
