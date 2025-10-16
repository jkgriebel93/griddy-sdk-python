"""Skeleton tests for the NFL football endpoints."""

import pytest


@pytest.mark.skip(reason="TODO: implement parsing test for Football.get_weekly_game_details")
def test_get_weekly_game_details_returns_games(nfl_football):
    """Outline verifying that game metadata is normalized from the API payload."""
    # TODO: stub BaseSDK.do_request to provide fixture data and assert the parsed models.
    assert nfl_football is not None


@pytest.mark.skip(reason="TODO: implement pagination test for Football.get_football_games")
def test_get_football_games_supports_filters(nfl_football):
    """Ensure query parameters are forwarded and multiple pages are aggregated."""
    # TODO: parametrise season/week filters and validate outgoing request construction.
    assert nfl_football is not None


@pytest.mark.skip(reason="TODO: implement box score parsing test for Football.get_football_box_score")
def test_get_football_box_score_parses_stats(nfl_football):
    """Confirm player and team stats are mapped into the SDK models."""
    # TODO: build fixture covering offense/defense splits and verify the resulting model.
    assert nfl_football is not None


@pytest.mark.skip(reason="TODO: implement play-by-play ingestion test for Football.get_play_by_play")
def test_get_play_by_play_orders_plays(nfl_football):
    """Check each play entry is sorted and contains derived timeline fields."""
    # TODO: simulate drive/play payload and validate ordering logic.
    assert nfl_football is not None


@pytest.mark.skip(reason="TODO: implement draft info fixture for Football.get_draft_info")
def test_get_draft_info_maps_prospects(nfl_football):
    """Validate positional data and draft metadata are captured in models."""
    # TODO: verify the SDK handles future year inputs and optional fields.
    assert nfl_football is not None
