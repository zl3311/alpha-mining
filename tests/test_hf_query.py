"""Tests for scripts/hf_query.py --tag SQL clause construction.

Covers:
- build_tag_clause for present/absent/empty tags
- clause shape (LIKE wildcard, table alias) so --gate-passers/--new-24h filter
"""

import importlib.util
from pathlib import Path

import pytest

_SCRIPT = Path(__file__).resolve().parent.parent / "scripts" / "hf_query.py"
_spec = importlib.util.spec_from_file_location("hf_query", _SCRIPT)
hf_query = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(hf_query)


@pytest.mark.parametrize("empty", [None, ""])
def test_build_tag_clause_empty_returns_blank(empty):
    assert hf_query.build_tag_clause(empty) == ""


def test_build_tag_clause_basic():
    clause = hf_query.build_tag_clause("20260604-001")
    assert clause == " AND j.tags_json LIKE '%20260604-001%'"


def test_build_tag_clause_starts_with_and_space():
    clause = hf_query.build_tag_clause("zscore_r3")
    assert clause.startswith(" AND ")


def test_build_tag_clause_uses_like_wildcards():
    clause = hf_query.build_tag_clause("mytag")
    assert "LIKE '%mytag%'" in clause


def test_build_tag_clause_targets_jobs_alias():
    clause = hf_query.build_tag_clause("x")
    assert "j.tags_json" in clause


def test_build_tag_clause_composes_into_where():
    # Mimic the f-string composition used in main() to ensure valid SQL shape.
    tag_clause = hf_query.build_tag_clause("sess1")
    sql = f"WHERE r.sharpe >= 1.25 AND r.fitness >= 1.0{tag_clause} ORDER BY r.fitness DESC"
    assert "AND r.fitness >= 1.0 AND j.tags_json LIKE '%sess1%' ORDER BY" in sql
