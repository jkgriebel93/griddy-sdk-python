"""Skeleton tests for the NFL season schedule endpoints."""

import pytest


@pytest.mark.skip(reason="TODO: implement coverage test for SeasonSchedule.get_schedule_season_weeks")
def test_get_schedule_season_weeks_returns_calendar(nfl_season_schedule):
    """Validate that week metadata is parsed into the schedule model."""
    # TODO: craft sample response covering bye weeks and preseason to verify mapping.
    assert nfl_season_schedule is not None
