"""Test model_serializer methods on models that define them.

Instantiates each model with defaults and calls .model_dump() to exercise
the serialize_model wrap method and its branching logic.
"""

import importlib
from datetime import date, datetime, timezone
from typing import Any, Dict, get_type_hints

import pytest

from griddy.nfl.types.basemodel import BaseModel

# Models that can be instantiated with no arguments (all fields optional)
_OPTIONAL_MODELS = [
    ("griddy.nfl.models.entities.boxscore_site", "BoxscoreSite"),
    ("griddy.nfl.models.entities.current_game", "CurrentGame"),
    ("griddy.nfl.models.entities.futures_market", "FuturesMarket"),
    ("griddy.nfl.models.entities.game", "Game"),
    ("griddy.nfl.models.entities.game_site", "GameSite"),
    (
        "griddy.nfl.models.entities.multiple_rankings_category",
        "MultipleRankingsCategoryPagination",
    ),
    ("griddy.nfl.models.entities.pagination", "Pagination"),
    ("griddy.nfl.models.entities.player", "Player"),
    ("griddy.nfl.models.entities.player_detail", "PlayerDetail"),
    ("griddy.nfl.models.entities.player_search_result", "PlayerSearchResult"),
    ("griddy.nfl.models.entities.pro_game", "ProGame"),
    ("griddy.nfl.models.entities.pro_team", "ProTeam"),
    ("griddy.nfl.models.entities.scheduled_game", "ScheduledGame"),
    ("griddy.nfl.models.entities.site", "Site"),
    ("griddy.nfl.models.entities.team", "Team"),
    ("griddy.nfl.models.entities.team_info", "TeamInfo"),
    ("griddy.nfl.models.entities.team_matchup_rankings", "TeamMatchupRankings"),
    ("griddy.nfl.models.entities.venue", "Venue"),
    ("griddy.nfl.models.entities.weekly_game_detail", "WeeklyGameDetail"),
    ("griddy.nfl.models.entities.weekly_player", "WeeklyPlayer"),
    (
        "griddy.nfl.models.responses.game_preview_response",
        "GamePreviewResponse",
    ),
]


@pytest.mark.unit
class TestModelSerializers:
    @pytest.mark.parametrize(
        "module_path,class_name",
        _OPTIONAL_MODELS,
        ids=[f"{m}.{c}" for m, c in _OPTIONAL_MODELS],
    )
    def test_default_instance_model_dump(self, module_path, class_name):
        """Model with all defaults should serialize without errors."""
        mod = importlib.import_module(module_path)
        klass = getattr(mod, class_name)
        instance = klass()
        result = instance.model_dump()
        assert isinstance(result, dict)

    @pytest.mark.parametrize(
        "module_path,class_name",
        _OPTIONAL_MODELS,
        ids=[f"{m}.{c}" for m, c in _OPTIONAL_MODELS],
    )
    def test_model_dump_by_alias(self, module_path, class_name):
        """model_dump(by_alias=True) should also work."""
        mod = importlib.import_module(module_path)
        klass = getattr(mod, class_name)
        instance = klass()
        result = instance.model_dump(by_alias=True)
        assert isinstance(result, dict)


@pytest.mark.unit
class TestModelsWithRequiredFields:
    """Test serializer models that have required fields."""

    def test_coaches_film_video(self):
        from griddy.nfl.models.entities.coaches_film_video import CoachesFilmVideo
        from griddy.nfl.models.entities.video_game_play_ids import VideoGamePlayIds

        ids = VideoGamePlayIds(
            away_team_id="team1",
            game_id="game1",
            home_team_id="team2",
            play_id="1",
        )
        instance = CoachesFilmVideo(
            camera_source="Broadcast",
            description="Test play",
            duration="00:05",
            external_id="ext123",
            ids=ids,
            title="Test Title",
            type="video",
        )
        result = instance.model_dump()
        assert isinstance(result, dict)
        assert result["cameraSource"] == "Broadcast"

    def test_insight(self):
        from griddy.nfl.models.entities.insight import Insight

        now = datetime.now(tz=timezone.utc)
        instance = Insight(
            created_at=now,
            created_by="system",
            date_=date.today(),
            id="ins123",
            season=2024,
            season_type="REG",
            tags=["tag1"],
            team_abbr="PHI",
            team_id="team123",
            title="Test Insight",
            updated_at=now,
            updated_by="system",
            week=1,
        )
        result = instance.model_dump()
        assert isinstance(result, dict)
        assert result["season"] == 2024

    def test_play_win_probability(self):
        from griddy.nfl.models.entities.play_win_probability import PlayWinProbability

        instance = PlayWinProbability(
            down=1,
            home_score=7,
            play_description="Pass complete",
            play_id=100,
            possession_team_id="team1",
            pre_snap_home_score=7,
            pre_snap_visitor_score=3,
            quarter=1,
            sequence=1.0,
            visitor_score=3,
            yards_to_go=10,
        )
        result = instance.model_dump()
        assert isinstance(result, dict)
        assert result["down"] == 1

    def test_player_week_projected_points(self):
        from griddy.nfl.models.entities.player_week_projected_points import (
            PlayerWeekProjectedPointsAttributes,
        )

        instance = PlayerWeekProjectedPointsAttributes(
            player_id="player1",
            season=2024,
            settings_code="STD",
            week=1,
        )
        result = instance.model_dump()
        assert isinstance(result, dict)

    def test_player_week_projected_stats(self):
        from griddy.nfl.models.entities.player_week_projected_stats import (
            PlayerWeekProjectedStatsAttributes,
        )

        instance = PlayerWeekProjectedStatsAttributes(
            player_id="player1",
            season=2024,
            week=1,
        )
        result = instance.model_dump()
        assert isinstance(result, dict)


@pytest.mark.unit
class TestSerializerBranchCoverage:
    """Test specific branches of the serialize_model method."""

    def test_player_with_set_nullable_field(self):
        """Setting a nullable field to None should include it in output."""
        from griddy.nfl.models.entities.player import Player

        player = Player(draft_club=None)
        result = player.model_dump()
        assert "draftClub" in result
        assert result["draftClub"] is None

    def test_player_with_unset_nullable_field(self):
        """Unset nullable fields should be omitted from output."""
        from griddy.nfl.models.entities.player import Player

        player = Player()
        result = player.model_dump()
        assert "draftClub" not in result

    def test_player_with_set_value(self):
        """Setting a field to a real value should include it."""
        from griddy.nfl.models.entities.player import Player

        player = Player(display_name="Patrick Mahomes")
        result = player.model_dump()
        assert result["displayName"] == "Patrick Mahomes"

    def test_game_preview_response_with_null_preview(self):
        """Setting preview to None should include it (optional+nullable)."""
        from griddy.nfl.models.responses.game_preview_response import (
            GamePreviewResponse,
        )

        response = GamePreviewResponse(preview=None)
        result = response.model_dump()
        assert "preview" in result
        assert result["preview"] is None
