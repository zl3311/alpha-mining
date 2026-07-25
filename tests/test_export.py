"""Tests for the export module."""

import json
from pathlib import Path

import pytest

from alpha_mining.export import export_result_markdown

_TEST_DIR = Path("/tmp/test_exports")


@pytest.fixture(autouse=True)
def cleanup():
    yield
    import shutil
    if _TEST_DIR.exists():
        shutil.rmtree(_TEST_DIR)


def _make_row(**overrides):
    row = {
        "name": "manual-20260516_0100-rank_close",
        "expression": "rank(close)",
        "alpha_eid": "alpha_1747388400_abc123",
        "sim_eid": "sim_1747388500_def456",
        "sharpe": 1.5,
        "fitness": 1.2,
        "turnover": 0.3,
        "returns": 0.01,
        "drawdown": 0.05,
        "platform_url": "https://platform.worldquantbrain.com/alpha/test",
        "sim_config_json": json.dumps({"region": "USA", "universe": "TOP3000"}),
    }
    row.update(overrides)
    return row


def test_export_creates_file():
    row = _make_row()
    path = export_result_markdown(row, _TEST_DIR)
    assert path.exists()
    assert path.suffix == ".md"


def test_export_content():
    row = _make_row()
    path = export_result_markdown(row, _TEST_DIR)
    content = path.read_text()
    assert "rank(close)" in content
    assert "1.500" in content
    assert "1.200" in content
    assert "alpha_1747388400_abc123" in content


def test_export_submittable_yes():
    row = _make_row(sharpe=1.5, fitness=1.2, turnover=0.3)
    path = export_result_markdown(row, _TEST_DIR)
    assert "Yes" in path.read_text()


def test_export_submittable_no():
    row = _make_row(sharpe=0.5, fitness=0.3, turnover=0.3)
    path = export_result_markdown(row, _TEST_DIR)
    assert "| Submittable | No |" in path.read_text()


def test_export_safe_filename():
    row = _make_row(name="a/b c")
    path = export_result_markdown(row, _TEST_DIR)
    assert "/" not in path.name
    assert " " not in path.name
