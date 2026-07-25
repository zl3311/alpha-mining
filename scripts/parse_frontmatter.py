"""
Parse frontmatter markdown files for structured queries.

Reads YAML frontmatter from .md files and supports filtering, listing,
and extracting structured data across the V2 data directory.

Usage:
    uv run python3 scripts/parse_frontmatter.py --dir data/book --field grade
    uv run python3 scripts/parse_frontmatter.py --dir data/factors --filter "status=active" \
        --field field,family,standalone_sharpe
    uv run python3 scripts/parse_frontmatter.py --dir data/book --list-ids alpha_id
    uv run python3 scripts/parse_frontmatter.py --dir data/knowledge/rules
    uv run python3 scripts/parse_frontmatter.py --book-ids
"""

import argparse
import json
from pathlib import Path

import yaml


def parse_frontmatter(path: Path) -> tuple[dict, str]:
    text = path.read_text()
    if not text.startswith("---"):
        return {}, text

    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}, text

    try:
        fm = yaml.safe_load(parts[1]) or {}
    except yaml.YAMLError:
        fm = {}
    body = parts[2].strip()
    return fm, body


def scan_dir(dirpath: Path) -> list[tuple[Path, dict, str]]:
    results = []
    if not dirpath.exists():
        return results
    for md in sorted(dirpath.glob("*.md")):
        fm, body = parse_frontmatter(md)
        if fm:
            results.append((md, fm, body))
    return results


def matches_filter(fm: dict, filters: list[str]) -> bool:
    for f in filters:
        if "=" not in f:
            continue
        key, val = f.split("=", 1)
        actual = str(fm.get(key, ""))
        if actual.lower() != val.lower():
            return False
    return True


def main():
    parser = argparse.ArgumentParser(description="Query frontmatter markdown files")
    parser.add_argument("--dir", help="Directory to scan for .md files")
    parser.add_argument("--filter", nargs="*", default=[], help="key=value filters (AND logic)")
    parser.add_argument("--field", help="Comma-separated frontmatter fields to display")
    parser.add_argument("--list-ids", help="Just list values of this frontmatter field")
    parser.add_argument("--book-ids", action="store_true", help="Shortcut: list all alpha_id values from data/book/")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    args = parser.parse_args()

    root = Path(__file__).resolve().parent.parent

    if args.book_ids:
        book_dir = root / "data" / "book"
        ids = []
        for md in sorted(book_dir.glob("*.md")):
            fm, _ = parse_frontmatter(md)
            aid = fm.get("alpha_id", md.stem)
            status = fm.get("status", "UNKNOWN")
            if status in ("ACTIVE", "PENDING"):
                ids.append(aid)
        if args.json:
            print(json.dumps(ids))
        else:
            for aid in ids:
                print(aid)
        return

    if not args.dir:
        parser.print_help()
        return

    dirpath = root / args.dir if not Path(args.dir).is_absolute() else Path(args.dir)
    entries = scan_dir(dirpath)

    if args.filter:
        entries = [(p, fm, b) for p, fm, b in entries if matches_filter(fm, args.filter)]

    if args.list_ids:
        for _, fm, _ in entries:
            val = fm.get(args.list_ids)
            if val is not None:
                print(val)
        return

    fields = args.field.split(",") if args.field else None

    if args.json:
        out = []
        for p, fm, _ in entries:
            row = {"_file": p.name}
            if fields:
                row.update({f: fm.get(f) for f in fields})
            else:
                row.update(fm)
            out.append(row)
        print(json.dumps(out, indent=2, default=str))
        return

    for p, fm, _ in entries:
        if fields:
            vals = [str(fm.get(f, "")) for f in fields]
            print(f"{p.stem:>35}  " + "  ".join(f"{f}={v}" for f, v in zip(fields, vals)))
        else:
            print(f"\n--- {p.name} ---")
            for k, v in fm.items():
                print(f"  {k}: {v}")


if __name__ == "__main__":
    main()
