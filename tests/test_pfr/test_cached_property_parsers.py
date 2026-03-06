"""Tests verifying that all PFR endpoint classes use cached_property for parsers."""

from functools import cached_property

import pytest


@pytest.mark.unit
class TestCachedPropertyParsers:
    """Verify that parser instantiation uses cached_property across all endpoints."""

    def test_games_parser_is_cached_property(self):
        from griddy.pfr.endpoints.games import Games

        assert isinstance(Games.__dict__["_parser"], cached_property), (
            "Games._parser should be a cached_property"
        )

    def test_schedule_parser_is_cached_property(self):
        from griddy.pfr.endpoints.schedule import Schedule

        assert isinstance(Schedule.__dict__["_parser"], cached_property), (
            "Schedule._parser should be a cached_property"
        )

    def test_teams_parsers_are_cached_property(self):
        from griddy.pfr.endpoints.teams import Teams

        assert isinstance(Teams.__dict__["_team_season_parser"], cached_property), (
            "Teams._team_season_parser should be a cached_property"
        )
        assert isinstance(Teams.__dict__["_franchise_parser"], cached_property), (
            "Teams._franchise_parser should be a cached_property"
        )

    def test_players_parser_is_cached_property(self):
        from griddy.pfr.endpoints.players import Players

        assert isinstance(Players.__dict__["_parser"], cached_property)

    def test_coaches_parser_is_cached_property(self):
        from griddy.pfr.endpoints.coaches import Coaches

        assert isinstance(Coaches.__dict__["_parser"], cached_property)

    def test_officials_parser_is_cached_property(self):
        from griddy.pfr.endpoints.officials import Officials

        assert isinstance(Officials.__dict__["_parser"], cached_property)

    def test_stadiums_parser_is_cached_property(self):
        from griddy.pfr.endpoints.stadiums import Stadiums

        assert isinstance(Stadiums.__dict__["_parser"], cached_property)

    def test_executives_parser_is_cached_property(self):
        from griddy.pfr.endpoints.executives import Executives

        assert isinstance(Executives.__dict__["_parser"], cached_property)

    def test_draft_parser_is_cached_property(self):
        from griddy.pfr.endpoints.draft import Draft

        assert isinstance(Draft.__dict__["_parser"], cached_property)

    def test_fantasy_parser_is_cached_property(self):
        from griddy.pfr.endpoints.fantasy import Fantasy

        assert isinstance(Fantasy.__dict__["_parser"], cached_property)

    def test_awards_parser_is_cached_property(self):
        from griddy.pfr.endpoints.awards import Awards

        assert isinstance(Awards.__dict__["_parser"], cached_property)

    def test_hof_parser_is_cached_property(self):
        from griddy.pfr.endpoints.hof import Hof

        assert isinstance(Hof.__dict__["_parser"], cached_property)

    def test_schools_parser_is_cached_property(self):
        from griddy.pfr.endpoints.schools import Schools

        assert isinstance(Schools.__dict__["_parser"], cached_property)

    def test_superbowl_parser_is_cached_property(self):
        from griddy.pfr.endpoints.superbowl import SuperBowl

        assert isinstance(SuperBowl.__dict__["_parser"], cached_property)

    def test_leaders_parser_is_cached_property(self):
        from griddy.pfr.endpoints.leaders import Leaders

        assert isinstance(Leaders.__dict__["_parser"], cached_property)

    def test_probowl_parser_is_cached_property(self):
        from griddy.pfr.endpoints.probowl import ProBowl

        assert isinstance(ProBowl.__dict__["_parser"], cached_property)

    def test_seasons_parser_is_cached_property(self):
        from griddy.pfr.endpoints.seasons import Seasons

        assert isinstance(Seasons.__dict__["_parser"], cached_property)

    def test_frivolities_parsers_are_cached_property(self):
        from griddy.pfr.endpoints.frivolities import Frivolities

        expected = [
            "_multi_team_parser",
            "_milestones_parser",
            "_upcoming_parser",
            "_birthdays_parser",
            "_birthplaces_parser",
            "_born_before_parser",
            "_uniform_numbers_parser",
            "_qb_wins_parser",
            "_non_qb_passers_parser",
            "_non_skill_pos_td_parser",
            "_octopus_tracker_parser",
            "_overtime_ties_parser",
            "_cups_of_coffee_parser",
            "_multi_sport_players_parser",
            "_pronunciation_guide_parser",
            "_last_undefeated_parser",
            "_standings_on_date_parser",
        ]
        for attr in expected:
            assert isinstance(Frivolities.__dict__[attr], cached_property), (
                f"Frivolities.{attr} should be a cached_property"
            )


@pytest.mark.unit
class TestCachedPropertyCachingBehavior:
    """Verify that cached_property actually caches the parser instance."""

    def test_games_parser_returns_same_instance(self):
        from griddy.pfr.endpoints.games import Games

        games = Games.__new__(Games)
        parser1 = games._parser
        parser2 = games._parser
        assert parser1 is parser2

    def test_teams_parsers_return_same_instances(self):
        from griddy.pfr.endpoints.teams import Teams

        teams = Teams.__new__(Teams)
        p1 = teams._team_season_parser
        p2 = teams._team_season_parser
        assert p1 is p2

        f1 = teams._franchise_parser
        f2 = teams._franchise_parser
        assert f1 is f2

    def test_no_module_level_parser_singletons(self):
        """Ensure no module-level _parser = ...() singletons remain."""
        import griddy.pfr.endpoints.awards as awards
        import griddy.pfr.endpoints.coaches as coaches
        import griddy.pfr.endpoints.draft as draft
        import griddy.pfr.endpoints.executives as executives
        import griddy.pfr.endpoints.fantasy as fantasy
        import griddy.pfr.endpoints.frivolities as frivolities
        import griddy.pfr.endpoints.games as games
        import griddy.pfr.endpoints.hof as hof
        import griddy.pfr.endpoints.leaders as leaders
        import griddy.pfr.endpoints.officials as officials
        import griddy.pfr.endpoints.players as players
        import griddy.pfr.endpoints.probowl as probowl
        import griddy.pfr.endpoints.schedule as schedule
        import griddy.pfr.endpoints.schools as schools
        import griddy.pfr.endpoints.seasons as seasons
        import griddy.pfr.endpoints.stadiums as stadiums
        import griddy.pfr.endpoints.superbowl as superbowl
        import griddy.pfr.endpoints.teams as teams

        modules = [
            awards,
            coaches,
            draft,
            executives,
            fantasy,
            frivolities,
            games,
            hof,
            leaders,
            officials,
            players,
            probowl,
            schedule,
            schools,
            seasons,
            stadiums,
            superbowl,
            teams,
        ]

        for mod in modules:
            for name, val in vars(mod).items():
                if name.startswith("_") and name.endswith("_parser"):
                    # It should NOT be a parser instance at module level
                    assert not hasattr(val, "parse"), (
                        f"{mod.__name__}.{name} is a module-level parser "
                        f"singleton — should be a cached_property instead"
                    )
