"""Skeleton tests for the NFL win probability endpoints."""

import pytest


@pytest.mark.skip(reason="TODO: implement end-to-end test for WinProbability.get_plays_win_probability")
def test_get_plays_win_probability_returns_charts(nfl_win_probability):
    """Ensure play-level win probability data is extracted with drive context."""
    # TODO: assert on sequence of plays and win probability deltas.
    assert nfl_win_probability is not None


@pytest.mark.skip(reason="TODO: implement aggregation test for WinProbability.get_win_probability_min")
def test_get_win_probability_min_collapses_series(nfl_win_probability):
    """Validate minified win probability response is handled with proper ordering."""
    # TODO: confirm condensed payloads still expose summary metrics.
    assert nfl_win_probability is not None
