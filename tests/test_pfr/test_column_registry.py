"""Tests for the shared ColumnMetadata registry."""

import pytest

from griddy.pfr.parsers._column_registry import (
    AWARDS,
    BIRTHPLACES_FILTERED,
    BIRTHPLACES_LANDING,
    COACH_CHALLENGES,
    COACH_HISTORY,
    COACH_RANKS,
    COACH_RESULTS,
    COACH_RESULTS_FOOTER,
    DRAFT,
    FANTASY_MATCHUPS,
    FANTASY_POINTS_ALLOWED,
    FANTASY_RZ_PASSING,
    FANTASY_RZ_RECEIVING,
    FANTASY_RZ_RUSHING,
    FANTASY_TOP_PLAYERS,
    OFFICIAL_GAMES,
    OFFICIAL_STATS,
    SCHEDULE,
    SEASON_PLAYOFF_RESULTS,
    SEASON_PLAYOFF_STANDINGS,
    SEASON_STANDINGS,
    TEAM_FRANCHISE,
    TEAM_SEASON_GAMES,
    ColumnMetadata,
)


class TestColumnMetadata:
    """Tests for the ColumnMetadata dataclass."""

    def test_default_empty_frozensets(self) -> None:
        meta = ColumnMetadata()
        assert meta.int_columns == frozenset()
        assert meta.float_columns == frozenset()
        assert meta.pct_columns == frozenset()

    def test_frozen(self) -> None:
        meta = ColumnMetadata(int_columns=frozenset({"a"}))
        with pytest.raises(AttributeError):
            meta.int_columns = frozenset({"b"})  # type: ignore[misc]

    def test_membership_check(self) -> None:
        meta = ColumnMetadata(
            int_columns=frozenset({"g", "wins"}),
            float_columns=frozenset({"srs_total"}),
        )
        assert "g" in meta.int_columns
        assert "wins" in meta.int_columns
        assert "srs_total" in meta.float_columns
        assert "losses" not in meta.int_columns

    def test_no_overlap_between_fields(self) -> None:
        """int, float, and pct columns should never overlap within an instance."""
        all_instances = [
            AWARDS,
            BIRTHPLACES_FILTERED,
            BIRTHPLACES_LANDING,
            COACH_CHALLENGES,
            COACH_HISTORY,
            COACH_RANKS,
            COACH_RESULTS,
            COACH_RESULTS_FOOTER,
            DRAFT,
            FANTASY_MATCHUPS,
            FANTASY_POINTS_ALLOWED,
            FANTASY_RZ_PASSING,
            FANTASY_RZ_RECEIVING,
            FANTASY_RZ_RUSHING,
            FANTASY_TOP_PLAYERS,
            OFFICIAL_GAMES,
            OFFICIAL_STATS,
            SCHEDULE,
            SEASON_PLAYOFF_RESULTS,
            SEASON_PLAYOFF_STANDINGS,
            SEASON_STANDINGS,
            TEAM_FRANCHISE,
            TEAM_SEASON_GAMES,
        ]
        for instance in all_instances:
            overlap_if = instance.int_columns & instance.float_columns
            overlap_ip = instance.int_columns & instance.pct_columns
            overlap_fp = instance.float_columns & instance.pct_columns
            assert not overlap_if, f"{instance} has int/float overlap: {overlap_if}"
            assert not overlap_ip, f"{instance} has int/pct overlap: {overlap_ip}"
            assert not overlap_fp, f"{instance} has float/pct overlap: {overlap_fp}"


class TestRegistryInstances:
    """Verify specific registry instances have expected columns."""

    def test_schedule_has_int_columns(self) -> None:
        assert "pts_win" in SCHEDULE.int_columns
        assert "pts_lose" in SCHEDULE.int_columns
        assert SCHEDULE.float_columns == frozenset()

    def test_draft_has_both(self) -> None:
        assert "draft_round" in DRAFT.int_columns
        assert "sacks" in DRAFT.float_columns
        assert "forty_yd" in DRAFT.float_columns

    def test_fantasy_rz_receiving_uses_pct(self) -> None:
        assert "catch_pct" in FANTASY_RZ_RECEIVING.pct_columns
        assert "targets" in FANTASY_RZ_RECEIVING.int_columns
        assert FANTASY_RZ_RECEIVING.float_columns == frozenset()

    def test_fantasy_rz_rushing_uses_pct(self) -> None:
        assert "rush_att_pct" in FANTASY_RZ_RUSHING.pct_columns
        assert "rush_att" in FANTASY_RZ_RUSHING.int_columns

    def test_coach_ranks_all_int(self) -> None:
        assert len(COACH_RANKS.int_columns) == 31
        assert COACH_RANKS.float_columns == frozenset()

    def test_team_franchise_float(self) -> None:
        assert "mov" in TEAM_FRANCHISE.float_columns
        assert "srs_total" in TEAM_FRANCHISE.float_columns

    def test_all_instances_are_nonempty(self) -> None:
        """Every registry instance should have at least one column defined."""
        all_instances = [
            AWARDS,
            BIRTHPLACES_FILTERED,
            BIRTHPLACES_LANDING,
            COACH_CHALLENGES,
            COACH_HISTORY,
            COACH_RANKS,
            COACH_RESULTS,
            COACH_RESULTS_FOOTER,
            DRAFT,
            FANTASY_MATCHUPS,
            FANTASY_POINTS_ALLOWED,
            FANTASY_RZ_PASSING,
            FANTASY_RZ_RECEIVING,
            FANTASY_RZ_RUSHING,
            FANTASY_TOP_PLAYERS,
            OFFICIAL_GAMES,
            OFFICIAL_STATS,
            SCHEDULE,
            SEASON_PLAYOFF_RESULTS,
            SEASON_PLAYOFF_STANDINGS,
            SEASON_STANDINGS,
            TEAM_FRANCHISE,
            TEAM_SEASON_GAMES,
        ]
        for instance in all_instances:
            total = (
                len(instance.int_columns)
                + len(instance.float_columns)
                + len(instance.pct_columns)
            )
            assert total > 0, f"{instance} has no columns defined"
