"""Skeleton tests for the NFL scores endpoints."""

import pytest


@pytest.mark.skip(reason="TODO: implement endpoint contract test for Scores.get_live_game_scores")
def test_get_live_game_scores_returns_live_scores(mocked_nfl_sdk):
    """Validate that live score payloads are parsed into LiveScoresResponse."""
    # TODO: patch BaseSDK.do_request to return fixture data and assert on the model.
    # Example shape: models.LiveScoresResponse(games=[...])
    scores = mocked_nfl_sdk.scores
    assert scores is not None


@pytest.mark.skip(reason="TODO: implement error handling test for Scores.get_live_game_scores")
def test_get_live_game_scores_handles_api_errors(mocked_nfl_sdk, monkeypatch):
    """Ensure API errors raise GriddyNFLDefaultError once HTTP status codes are mocked."""
    # TODO: monkeypatch the HTTP layer to raise errors and assert the exception.
    scores = mocked_nfl_sdk.scores
    assert scores is not None
