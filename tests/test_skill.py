"""
Tests for the Cursor skill file structure and content.
Validates that the skill is properly formatted and contains essential information.
"""

from pathlib import Path

import pytest

_REPO_ROOT = Path(__file__).resolve().parents[1]
SKILL_PATH = _REPO_ROOT / ".cursor" / "skills" / "alpha-mining" / "SKILL.md"


def _read_skill():
    if not SKILL_PATH.exists():
        pytest.skip(f"SKILL.md not found at {SKILL_PATH}")
    return SKILL_PATH.read_text()


class TestSkillStructure:
    def test_frontmatter_has_name(self):
        content = _read_skill()
        assert "name: alpha-mining" in content

    def test_frontmatter_has_description(self):
        content = _read_skill()
        assert "description:" in content

    def test_under_500_lines(self):
        content = _read_skill()
        assert len(content.splitlines()) <= 500

    def test_contains_reference_section(self):
        content = _read_skill()
        assert "Alpha Mining Reference" in content or "Alpha Mining Workflow" in content

    def test_contains_operator_reference(self):
        content = _read_skill()
        assert "ts_corr" in content
        assert "ts_delay" in content
        assert "ts_arg_max" in content

    def test_contains_operator_gotchas(self):
        content = _read_skill()
        assert "ts_delay" in content
        assert "ts_corr" in content

    def test_contains_submission_gates(self):
        content = _read_skill()
        assert "1.25" in content
        assert "1.0" in content

    def test_contains_cli_examples(self):
        content = _read_skill()
        assert "uv run python3 -m alpha_mining" in content
        assert "--expression" in content or "-e " in content
        assert "--ingest" in content
