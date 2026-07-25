"""Tests for the entity ID generator."""

import time

import pytest

from alpha_mining.ids import entity_type, generate_entity_id, parse_entity_id


class TestGenerateEntityId:
    def test_format(self):
        eid = generate_entity_id("paper")
        parts = eid.split("_")
        assert parts[0] == "paper"
        assert parts[1].isdigit()
        assert len(parts[2]) == 6

    @pytest.mark.parametrize("prefix", ["session", "paper", "hypothesis", "alpha", "simulation", "result"])
    def test_all_prefixes(self, prefix):
        eid = generate_entity_id(prefix)
        assert eid.startswith(("sess_", "paper_", "hyp_", "alpha_", "sim_", "result_"))

    def test_uniqueness(self):
        ids = {generate_entity_id("paper") for _ in range(100)}
        assert len(ids) == 100

    def test_timestamp_is_current(self):
        before = int(time.time())
        eid = generate_entity_id("paper")
        after = int(time.time())
        _, ts, _ = parse_entity_id(eid)
        assert before <= ts <= after

    def test_raw_prefix_passthrough(self):
        eid = generate_entity_id("custom")
        assert eid.startswith("custom_")


class TestParseEntityId:
    def test_roundtrip(self):
        eid = generate_entity_id("paper")
        prefix, ts, hash_part = parse_entity_id(eid)
        assert prefix == "paper"
        assert isinstance(ts, int)
        assert len(hash_part) == 6

    def test_invalid_format(self):
        with pytest.raises(ValueError):
            parse_entity_id("bad")

    def test_invalid_timestamp(self):
        with pytest.raises(ValueError):
            parse_entity_id("paper_notanumber_abc123")


class TestEntityType:
    def test_known_prefixes(self):
        assert entity_type("sess_123_abc") == "session"
        assert entity_type("paper_123_abc") == "paper"
        assert entity_type("hyp_123_abc") == "hypothesis"
        assert entity_type("alpha_123_abc") == "alpha"
        assert entity_type("sim_123_abc") == "simulation"
        assert entity_type("result_123_abc") == "result"

    def test_unknown_prefix(self):
        assert entity_type("custom_123_abc") == "custom"
