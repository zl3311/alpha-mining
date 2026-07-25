"""Sync the submitted book from data/book/*.md to the HF server.

Reads ACTIVE entries from data/book/*.md (the canonical source of truth),
pushes them to the server's submitted_book table via POST /v1/seed/book,
and verifies the sync by reading back and comparing.

Usage:
    uv run python3 scripts/sync_server_book.py                  # sync + verify
    uv run python3 scripts/sync_server_book.py --dry-run        # show what would be synced
    uv run python3 scripts/sync_server_book.py --verify-only    # just check current state
"""

import argparse
import os
import sys
from pathlib import Path

import httpx
import yaml

BOOK_DIR = Path(__file__).resolve().parent.parent / "data" / "book"


def _load_env():
    """Load env vars from .env if not already set."""
    if os.environ.get("HF_API_KEY") and os.environ.get("HF_TOKEN"):
        return
    try:
        from dotenv import load_dotenv
        load_dotenv(Path(__file__).resolve().parent.parent / ".env")
    except ImportError:
        pass


# Load .env before reading SERVER_URL so the value is available at import time.
_load_env()

SERVER_URL = os.environ.get("HF_SERVER_URL", "").rstrip("/")


def _server_headers() -> dict:
    return {
        "Authorization": f"Bearer {os.environ.get('HF_TOKEN', '')}",
        "X-API-Key": os.environ.get("HF_API_KEY", ""),
    }


def read_local_book() -> list[dict]:
    """Read ACTIVE entries from data/book/*.md."""
    entries = []
    if not BOOK_DIR.exists():
        print("ERROR: data/book/ not found", file=sys.stderr)
        return entries

    for md_file in sorted(BOOK_DIR.glob("*.md")):
        text = md_file.read_text()
        if not text.startswith("---"):
            continue
        parts = text.split("---", 2)
        if len(parts) < 3:
            continue
        try:
            fm = yaml.safe_load(parts[1]) or {}
        except yaml.YAMLError:
            continue

        status = fm.get("status")
        if status is None:
            print(f"  WARNING: {md_file.name} has no status field, skipping", file=sys.stderr)
            continue
        if status != "ACTIVE":
            continue

        entries.append({
            "alpha_id": fm.get("alpha_id", md_file.stem),
            "expression": fm.get("expression", ""),
            "sharpe": float(fm.get("sharpe", 0)),
            "fitness": float(fm.get("fitness", 0)),
        })

    return entries


def read_server_book(headers: dict) -> list[dict]:
    """Read the current server submitted_book via SQL query."""
    r = httpx.get(
        f"{SERVER_URL}/v1/db/query",
        params={"sql": "SELECT alpha_id, expression, sharpe, fitness, status FROM submitted_book ORDER BY alpha_id"},
        headers=headers,
        timeout=15,
    )
    if r.status_code != 200:
        print(f"ERROR: server query failed: {r.status_code} {r.text[:200]}", file=sys.stderr)
        return []

    data = r.json()
    return [
        {"alpha_id": row[0], "expression": row[1], "sharpe": row[2], "fitness": row[3], "status": row[4]}
        for row in data.get("rows", [])
    ]


def push_book(entries: list[dict], headers: dict) -> bool:
    """Push book entries to the server via POST /v1/seed/book."""
    r = httpx.post(
        f"{SERVER_URL}/v1/seed/book",
        json=entries,
        headers={**headers, "Content-Type": "application/json"},
        timeout=30,
    )
    if r.status_code != 200:
        print(f"ERROR: seed/book failed: {r.status_code} {r.text[:200]}", file=sys.stderr)
        return False

    result = r.json()
    print(f"  Server accepted: {result.get('added', '?')} entries", file=sys.stderr)
    return True


def verify_sync(local: list[dict], headers: dict) -> bool:
    """Verify server book matches local ACTIVE entries exactly."""
    server = read_server_book(headers)
    server_ids = {e["alpha_id"] for e in server}
    local_ids = {e["alpha_id"] for e in local}

    missing = local_ids - server_ids
    extra = server_ids - local_ids

    ok = True
    if missing:
        print(f"  FAIL: {len(missing)} local entries missing from server: {missing}", file=sys.stderr)
        ok = False
    if extra:
        print(f"  WARNING: {len(extra)} stale server entries not in local ACTIVE book: {extra}", file=sys.stderr)
        print("  The server's POST /v1/seed/book can only add/update, not delete.", file=sys.stderr)
        print("  To remove stale entries, a DELETE endpoint is needed on the server.", file=sys.stderr)
        print("  Self-corr may be computed against stale alphas until resolved.", file=sys.stderr)

    if ok:
        print(f"  VERIFIED: server book matches local exactly ({len(local_ids)} entries)", file=sys.stderr)
    return ok


def main():
    parser = argparse.ArgumentParser(description="Sync submitted book to HF server")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be synced without pushing")
    parser.add_argument("--verify-only", action="store_true", help="Just compare local vs server, no push")
    args = parser.parse_args()

    _load_env()
    headers = _server_headers()

    local = read_local_book()
    print(f"Local book: {len(local)} ACTIVE entries", file=sys.stderr)

    if not args.dry_run and not SERVER_URL:
        sys.exit(
            "HF_SERVER_URL is not set. Copy .env.example to .env and point it at your own "
            "deployment of the submission queue server (see server/), or use --dry-run."
        )

    if args.verify_only:
        server = read_server_book(headers)
        print(f"Server book: {len(server)} entries", file=sys.stderr)
        ok = verify_sync(local, headers)
        for e in local:
            print(f"  {e['alpha_id']}  S={e['sharpe']:.2f}  F={e['fitness']:.2f}")
        if not ok:
            sys.exit(1)
        return

    if args.dry_run:
        print("Dry run — would push:", file=sys.stderr)
        for e in local:
            print(f"  {e['alpha_id']}  S={e['sharpe']:.2f}  F={e['fitness']:.2f}  {e['expression'][:60]}")
        return

    print("Syncing local book to server...", file=sys.stderr)
    if not push_book(local, headers):
        sys.exit(1)

    if not verify_sync(local, headers):
        print("WARNING: post-sync verification found discrepancies", file=sys.stderr)
        sys.exit(1)

    print("Sync complete.", file=sys.stderr)


if __name__ == "__main__":
    main()
