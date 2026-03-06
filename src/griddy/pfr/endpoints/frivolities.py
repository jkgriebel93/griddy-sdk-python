"""Frivolities endpoint for Pro Football Reference.

Provides:
- ``get_multi_team_players()`` — Players who played for multiple teams/franchises
  (``/friv/players-who-played-for-multiple-teams-franchises.fcgi``)
- ``get_statistical_milestones()`` — Milestone watch and career leaders
  (``/friv/milestones.cgi``)
- ``get_upcoming_milestones()`` — Upcoming milestones and leaderboard movement
  (``/friv/upcoming-milestones.htm``)
- ``get_birthdays()`` — Players born on a given month/day
  (``/friv/birthdays.cgi``)
- ``get_birthplaces()`` — Location summary with player counts
  (``/friv/birthplaces.htm``)
- ``get_birthplace_players()`` — Players born in a specific country/state
  (``/friv/birthplaces.cgi``)
- ``get_players_born_before()`` — Active players born on or before a date
  (``/friv/age.cgi``)
- ``get_uniform_numbers()`` — Players who wore a specific uniform number
  (``/players/uniform.cgi``)
- ``get_qb_wins_vs_franchises()`` — QBs who beat every (or nearly every) franchise
  (``/friv/qb-wins.htm``)
- ``get_non_qb_passers()`` — Non-QB players who have thrown a pass
  (``/friv/nonqb.htm``)
- ``get_non_skill_pos_td_scorers()`` — Non-skill position TD scorers
  (``/friv/odd_td.htm``)
- ``get_octopus_tracker()`` — Octopus TD + 2pt conversion scorers
  (``/friv/octopus-tracker.htm``)
- ``get_cups_of_coffee()`` — Players with a single game played
  (``/friv/coffee.htm``)
- ``get_multi_sport_players()`` — Athletes who played multiple sports
  (``/friv/multisport.htm``)
- ``get_pronunciation_guide()`` — Player name pronunciation guide
  (``/friv/pronunciation-guide.htm``)
- ``get_overtime_ties()`` — Tied games since sudden-death overtime (1974)
  (``/friv/nfl-ties.htm``)
- ``get_last_undefeated()`` — Last undefeated team(s) in every season
  (``/friv/last-undefeated.htm``)
- ``get_standings_on_date()`` — NFL standings as of a specific date or week
  (``/boxscores/standings.cgi``)
"""

from functools import cached_property
from typing import Optional

from griddy.core.decorators import sdk_endpoints
from griddy.pfr.parsers.birthdays import BirthdaysParser
from griddy.pfr.parsers.birthplaces import BirthplacesParser
from griddy.pfr.parsers.cups_of_coffee import CupsOfCoffeeParser
from griddy.pfr.parsers.last_undefeated import LastUndefeatedParser
from griddy.pfr.parsers.multi_sport_players import MultiSportPlayersParser
from griddy.pfr.parsers.multi_team_players import MultiTeamPlayersParser
from griddy.pfr.parsers.non_qb_passers import NonQBPassersParser
from griddy.pfr.parsers.non_skill_pos_td import NonSkillPosTdParser
from griddy.pfr.parsers.octopus_tracker import OctopusTrackerParser
from griddy.pfr.parsers.overtime_ties import OvertimeTiesParser
from griddy.pfr.parsers.players_born_before import PlayersBornBeforeParser
from griddy.pfr.parsers.pronunciation_guide import PronunciationGuideParser
from griddy.pfr.parsers.qb_wins import QBWinsParser
from griddy.pfr.parsers.standings_on_date import StandingsOnDateParser
from griddy.pfr.parsers.statistical_milestones import StatisticalMilestonesParser
from griddy.pfr.parsers.uniform_numbers import UniformNumbersParser
from griddy.pfr.parsers.upcoming_milestones import UpcomingMilestonesParser

from ..basesdk import BaseSDK, EndpointConfig
from ..models import (
    Birthdays,
    BirthplaceFiltered,
    BirthplaceLanding,
    CupsOfCoffee,
    LastUndefeated,
    MultiSportPlayers,
    MultiTeamPlayers,
    NonQBPassers,
    NonSkillPosTdScorers,
    OctopusTracker,
    OvertimeTies,
    PlayersBornBefore,
    PronunciationGuide,
    QBWins,
    StandingsOnDate,
    StatisticalMilestones,
    UniformNumbers,
    UpcomingMilestones,
)


@sdk_endpoints
class Frivolities(BaseSDK):
    """Sub-SDK for PFR Frivolities & Fun Stuff pages."""

    @cached_property
    def _multi_team_parser(self) -> MultiTeamPlayersParser:
        """Lazily instantiate and cache the multi-team players HTML parser."""
        return MultiTeamPlayersParser()

    @cached_property
    def _milestones_parser(self) -> StatisticalMilestonesParser:
        """Lazily instantiate and cache the statistical milestones HTML parser."""
        return StatisticalMilestonesParser()

    @cached_property
    def _upcoming_parser(self) -> UpcomingMilestonesParser:
        """Lazily instantiate and cache the upcoming milestones HTML parser."""
        return UpcomingMilestonesParser()

    @cached_property
    def _birthdays_parser(self) -> BirthdaysParser:
        """Lazily instantiate and cache the birthdays HTML parser."""
        return BirthdaysParser()

    @cached_property
    def _birthplaces_parser(self) -> BirthplacesParser:
        """Lazily instantiate and cache the birthplaces HTML parser."""
        return BirthplacesParser()

    @cached_property
    def _born_before_parser(self) -> PlayersBornBeforeParser:
        """Lazily instantiate and cache the players-born-before HTML parser."""
        return PlayersBornBeforeParser()

    @cached_property
    def _uniform_numbers_parser(self) -> UniformNumbersParser:
        """Lazily instantiate and cache the uniform numbers HTML parser."""
        return UniformNumbersParser()

    @cached_property
    def _qb_wins_parser(self) -> QBWinsParser:
        """Lazily instantiate and cache the QB wins HTML parser."""
        return QBWinsParser()

    @cached_property
    def _non_qb_passers_parser(self) -> NonQBPassersParser:
        """Lazily instantiate and cache the non-QB passers HTML parser."""
        return NonQBPassersParser()

    @cached_property
    def _non_skill_pos_td_parser(self) -> NonSkillPosTdParser:
        """Lazily instantiate and cache the non-skill position TD HTML parser."""
        return NonSkillPosTdParser()

    @cached_property
    def _octopus_tracker_parser(self) -> OctopusTrackerParser:
        """Lazily instantiate and cache the octopus tracker HTML parser."""
        return OctopusTrackerParser()

    @cached_property
    def _overtime_ties_parser(self) -> OvertimeTiesParser:
        """Lazily instantiate and cache the overtime ties HTML parser."""
        return OvertimeTiesParser()

    @cached_property
    def _cups_of_coffee_parser(self) -> CupsOfCoffeeParser:
        """Lazily instantiate and cache the cups of coffee HTML parser."""
        return CupsOfCoffeeParser()

    @cached_property
    def _multi_sport_players_parser(self) -> MultiSportPlayersParser:
        """Lazily instantiate and cache the multi-sport players HTML parser."""
        return MultiSportPlayersParser()

    @cached_property
    def _pronunciation_guide_parser(self) -> PronunciationGuideParser:
        """Lazily instantiate and cache the pronunciation guide HTML parser."""
        return PronunciationGuideParser()

    @cached_property
    def _last_undefeated_parser(self) -> LastUndefeatedParser:
        """Lazily instantiate and cache the last undefeated HTML parser."""
        return LastUndefeatedParser()

    @cached_property
    def _standings_on_date_parser(self) -> StandingsOnDateParser:
        """Lazily instantiate and cache the standings-on-date HTML parser."""
        return StandingsOnDateParser()

    # ── Players Who Played for Multiple Teams ─────────────────────────

    def _get_multi_team_players_config(
        self,
        *,
        t1: str,
        t2: str,
        t3: Optional[str] = None,
        t4: Optional[str] = None,
        exclusively: bool = False,
        timeout_ms: Optional[int] = None,
    ) -> EndpointConfig:
        r"""Fetch players who played for multiple teams/franchises.

        Scrapes the PFR page at
        ``/friv/players-who-played-for-multiple-teams-franchises.fcgi``
        and returns top players, passing/rushing/receiving stats, and
        the full player listing.

        Args:
            t1: PFR franchise abbreviation for team 1 (e.g. ``"crd"``).
            t2: PFR franchise abbreviation for team 2 (e.g. ``"atl"``).
            t3: Optional PFR franchise abbreviation for team 3.
            t4: Optional PFR franchise abbreviation for team 4.
            exclusively: If ``True``, only return players who played
                *exclusively* for the selected teams.
            timeout_ms: Optional timeout in milliseconds for the page
                selector.

        Returns:
            A :class:`~griddy.pfr.models.MultiTeamPlayers` instance
            containing top player summaries, stat tables, and the full
            player listing.
        """
        query: dict[str, str] = {"level": "franch", "t1": t1, "t2": t2}
        if t3:
            query["t3"] = t3
        if t4:
            query["t4"] = t4
        if exclusively:
            query["exclusively"] = "1"

        return EndpointConfig(
            path_template="/friv/players-who-played-for-multiple-teams-franchises.fcgi",
            operation_id="getMultiTeamPlayers",
            wait_for_element="#multifranchise_stats_0",
            parser=self._multi_team_parser.parse,
            response_type=MultiTeamPlayers,
            query_params=query,
            timeout_ms=timeout_ms,
        )

    # ── Statistical Milestones ──────────────────────────────────────

    def _get_statistical_milestones_config(
        self,
        *,
        stat: str,
        timeout_ms: Optional[int] = None,
    ) -> EndpointConfig:
        r"""Fetch statistical milestones and career leaders for a stat.

        Scrapes the PFR page at ``/friv/milestones.cgi`` and returns
        active players approaching milestone thresholds and the top-25
        career leaders.

        Args:
            stat: The stat category. One of: ``g``, ``pass_att``,
                ``pass_cmp``, ``pass_yds``, ``pass_td``, ``rush_att``,
                ``rush_yds``, ``rush_td``, ``rec``, ``rec_yds``,
                ``rec_td``, ``yds_from_scrimmage``, ``all_purpose_yds``,
                ``all_td``, ``scoring``, ``sacks``, ``def_int``,
                ``fga``, ``fgm``, ``punt``, ``punt_yds``.
            timeout_ms: Optional timeout in milliseconds for the page
                selector.

        Returns:
            A :class:`~griddy.pfr.models.StatisticalMilestones` instance
            containing milestone watch entries and career leaders.
        """
        return EndpointConfig(
            path_template="/friv/milestones.cgi",
            operation_id="getStatisticalMilestones",
            wait_for_element="#milestones",
            parser=self._milestones_parser.parse,
            response_type=StatisticalMilestones,
            query_params={"stat": stat},
            timeout_ms=timeout_ms,
        )

    # ── Upcoming Milestones ───────────────────────────────────────

    def _get_upcoming_milestones_config(
        self,
        *,
        timeout_ms: Optional[int] = None,
    ) -> EndpointConfig:
        r"""Fetch upcoming milestones and leaderboard movements.

        Scrapes the PFR page at ``/friv/upcoming-milestones.htm`` and
        returns players who may hit a milestone or move up the career
        leaderboard in their next game.

        Args:
            timeout_ms: Optional timeout in milliseconds for the page
                selector.

        Returns:
            A :class:`~griddy.pfr.models.UpcomingMilestones` instance
            containing milestone entries and leaderboard entries.
        """
        return EndpointConfig(
            path_template="/friv/upcoming-milestones.htm",
            operation_id="getUpcomingMilestones",
            wait_for_element="#upcoming_milestones",
            parser=self._upcoming_parser.parse,
            response_type=UpcomingMilestones,
            timeout_ms=timeout_ms,
        )

    # ── Birthdays ──────────────────────────────────────────────────

    def _get_birthdays_config(
        self,
        *,
        month: int,
        day: int,
        timeout_ms: Optional[int] = None,
    ) -> EndpointConfig:
        r"""Fetch NFL players born on a given month and day.

        Scrapes the PFR page at ``/friv/birthdays.cgi`` and returns
        a list of players with their career statistics.

        Args:
            month: Birth month (1–12).
            day: Birth day (1–31).
            timeout_ms: Optional timeout in milliseconds for the page
                selector.

        Returns:
            A :class:`~griddy.pfr.models.Birthdays` instance
            containing the player listing with career stats.
        """
        return EndpointConfig(
            path_template="/friv/birthdays.cgi",
            operation_id="getBirthdays",
            wait_for_element="#birthdays",
            parser=self._birthdays_parser.parse,
            response_type=Birthdays,
            query_params={"month": str(month), "day": str(day)},
            timeout_ms=timeout_ms,
        )

    # ── Birthplaces ───────────────────────────────────────────────────

    def _get_birthplaces_config(
        self,
        *,
        timeout_ms: Optional[int] = None,
    ) -> EndpointConfig:
        r"""Fetch the birthplaces landing page with location summaries.

        Scrapes the PFR page at ``/friv/birthplaces.htm`` and returns
        a table of countries and states with player counts, hall of
        famers, and notable player highlights.

        Args:
            timeout_ms: Optional timeout in milliseconds for the page
                selector.

        Returns:
            A :class:`~griddy.pfr.models.BirthplaceLanding` instance
            containing the location summary table.
        """
        return EndpointConfig(
            path_template="/friv/birthplaces.htm",
            operation_id="getBirthplaces",
            wait_for_element="#birthplaces",
            parser=self._birthplaces_parser.parse_landing,
            response_type=BirthplaceLanding,
            timeout_ms=timeout_ms,
        )

    def _get_birthplace_players_config(
        self,
        *,
        country: str,
        state: str = "",
        timeout_ms: Optional[int] = None,
    ) -> EndpointConfig:
        r"""Fetch NFL players born in a specific country/state.

        Scrapes the PFR page at ``/friv/birthplaces.cgi`` and returns
        a list of players born in the given location with their career
        statistics.

        Args:
            country: Country code (e.g. ``"USA"``).
            state: State abbreviation (e.g. ``"PA"``). Defaults to
                empty string for country-level results.
            timeout_ms: Optional timeout in milliseconds for the page
                selector.

        Returns:
            A :class:`~griddy.pfr.models.BirthplaceFiltered` instance
            containing the player listing with career stats.
        """
        return EndpointConfig(
            path_template="/friv/birthplaces.cgi",
            operation_id="getBirthplacePlayers",
            wait_for_element="#birthplaces",
            parser=self._birthplaces_parser.parse_filtered,
            response_type=BirthplaceFiltered,
            query_params={"country": country, "state": state},
            timeout_ms=timeout_ms,
        )

    # ── Players Born Before a Date ────────────────────────────────────

    def _get_players_born_before_config(
        self,
        *,
        month: int,
        day: int,
        year: int,
        timeout_ms: Optional[int] = None,
    ) -> EndpointConfig:
        r"""Fetch active players born on or before a given date.

        Scrapes the PFR page at ``/friv/age.cgi`` and returns a list of
        active players born on or before the specified date with their
        career statistics.

        Args:
            month: Birth month (1–12).
            day: Birth day (1–31).
            year: Birth year (e.g. ``1993``).
            timeout_ms: Optional timeout in milliseconds for the page
                selector.

        Returns:
            A :class:`~griddy.pfr.models.PlayersBornBefore` instance
            containing the player listing with career stats.
        """
        return EndpointConfig(
            path_template="/friv/age.cgi",
            operation_id="getPlayersBornBefore",
            wait_for_element="#players",
            parser=self._born_before_parser.parse,
            response_type=PlayersBornBefore,
            query_params={
                "month": str(month),
                "day": str(day),
                "year": str(year),
            },
            timeout_ms=timeout_ms,
        )

    # ── Players By Uniform Number ──────────────────────────────────────

    def _get_uniform_numbers_config(
        self,
        *,
        number: int,
        team: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> EndpointConfig:
        r"""Fetch players who wore a specific uniform number.

        Scrapes the PFR page at ``/players/uniform.cgi`` and returns
        a list of players who wore the specified number, optionally
        filtered by team/franchise.

        Args:
            number: The uniform number to look up (e.g. ``6``).
            team: Optional PFR team abbreviation (e.g. ``"pit"``).
                When omitted, returns all players across all teams.
            timeout_ms: Optional timeout in milliseconds for the page
                selector.

        Returns:
            A :class:`~griddy.pfr.models.UniformNumbers` instance
            containing the player listing.
        """
        query: dict[str, str] = {"number": str(number)}
        if team:
            query["team"] = team

        return EndpointConfig(
            path_template="/players/uniform.cgi",
            operation_id="getUniformNumbers",
            wait_for_element="#uniform_number",
            parser=self._uniform_numbers_parser.parse,
            response_type=UniformNumbers,
            query_params=query,
            timeout_ms=timeout_ms,
        )

    # ── Quarterback Wins vs. Each Franchise ──────────────────────────────

    def _get_qb_wins_vs_franchises_config(
        self,
        *,
        timeout_ms: Optional[int] = None,
    ) -> EndpointConfig:
        r"""Fetch quarterbacks who beat every (or nearly every) franchise.

        Scrapes the PFR page at ``/friv/qb-wins.htm`` and returns a list
        of quarterbacks with the number of franchises they beat and the
        franchises they did not beat.

        Args:
            timeout_ms: Optional timeout in milliseconds for the page
                selector.

        Returns:
            A :class:`~griddy.pfr.models.QBWins` instance containing
            the quarterback entries.
        """
        return EndpointConfig(
            path_template="/friv/qb-wins.htm",
            operation_id="getQBWinsVsFranchises",
            wait_for_element="#qb_wins",
            parser=self._qb_wins_parser.parse,
            response_type=QBWins,
            timeout_ms=timeout_ms,
        )

    # ── Non-Quarterback Passers ──────────────────────────────────────────

    def _get_non_qb_passers_config(
        self,
        *,
        timeout_ms: Optional[int] = None,
    ) -> EndpointConfig:
        r"""Fetch non-quarterback players who have thrown a pass.

        Scrapes the PFR page at ``/friv/nonqb.htm`` and returns a list
        of non-QB players with their passing statistics.

        Args:
            timeout_ms: Optional timeout in milliseconds for the page
                selector.

        Returns:
            A :class:`~griddy.pfr.models.NonQBPassers` instance
            containing the player entries with passing stats.
        """
        return EndpointConfig(
            path_template="/friv/nonqb.htm",
            operation_id="getNonQBPassers",
            wait_for_element="#nonqb_passers",
            parser=self._non_qb_passers_parser.parse,
            response_type=NonQBPassers,
            timeout_ms=timeout_ms,
        )

    # ── Non-Skill Position TD Scorers ─────────────────────────────────────

    def _get_non_skill_pos_td_scorers_config(
        self,
        *,
        timeout_ms: Optional[int] = None,
    ) -> EndpointConfig:
        r"""Fetch non-skill position players who scored an offensive TD.

        Scrapes the PFR page at ``/friv/odd_td.htm`` and returns a list
        of game-level instances where non-skill position players scored
        an offensive touchdown, with rushing and receiving stats.

        Args:
            timeout_ms: Optional timeout in milliseconds for the page
                selector.

        Returns:
            A :class:`~griddy.pfr.models.NonSkillPosTdScorers` instance
            containing the scoring entries.
        """
        return EndpointConfig(
            path_template="/friv/odd_td.htm",
            operation_id="getNonSkillPosTdScorers",
            wait_for_element="#odd_scorers",
            parser=self._non_skill_pos_td_parser.parse,
            response_type=NonSkillPosTdScorers,
            timeout_ms=timeout_ms,
        )

    # ── Octopus Tracker ────────────────────────────────────────────────────

    def _get_octopus_tracker_config(
        self,
        *,
        timeout_ms: Optional[int] = None,
    ) -> EndpointConfig:
        r"""Fetch octopus TD + 2pt conversion scorers since 1994.

        Scrapes the PFR page at ``/friv/octopus-tracker.htm`` and returns
        a list of game-level instances where a player scored both the
        touchdown and the two-point conversion on a single possession.

        Args:
            timeout_ms: Optional timeout in milliseconds for the page
                selector.

        Returns:
            A :class:`~griddy.pfr.models.OctopusTracker` instance
            containing the scoring entries.
        """
        return EndpointConfig(
            path_template="/friv/octopus-tracker.htm",
            operation_id="getOctopusTracker",
            wait_for_element="#octopus",
            parser=self._octopus_tracker_parser.parse,
            response_type=OctopusTracker,
            timeout_ms=timeout_ms,
        )

    # ── Cups of Coffee ──────────────────────────────────────────────────────

    def _get_cups_of_coffee_config(
        self,
        *,
        timeout_ms: Optional[int] = None,
    ) -> EndpointConfig:
        r"""Fetch players who played only a single game in the NFL.

        Scrapes the PFR page at ``/friv/coffee.htm`` and returns a list
        of players who had only one NFL game appearance, with their
        passing, rushing, and receiving statistics from that game.

        Args:
            timeout_ms: Optional timeout in milliseconds for the page
                selector.

        Returns:
            A :class:`~griddy.pfr.models.CupsOfCoffee` instance
            containing the player entries with career stats.
        """
        return EndpointConfig(
            path_template="/friv/coffee.htm",
            operation_id="getCupsOfCoffee",
            wait_for_element="#coffee",
            parser=self._cups_of_coffee_parser.parse,
            response_type=CupsOfCoffee,
            timeout_ms=timeout_ms,
        )

    # ── Multi-Sport Players ──────────────────────────────────────────────────

    def _get_multi_sport_players_config(
        self,
        *,
        timeout_ms: Optional[int] = None,
    ) -> EndpointConfig:
        r"""Fetch athletes who played multiple sports professionally.

        Scrapes the PFR page at ``/friv/multisport.htm`` and returns a
        list of athletes who played in the NFL and at least one other
        professional sport, with their NFL career statistics and links
        to other sports reference sites.

        Args:
            timeout_ms: Optional timeout in milliseconds for the page
                selector.

        Returns:
            A :class:`~griddy.pfr.models.MultiSportPlayers` instance
            containing the player entries with career stats and other
            sport links.
        """
        return EndpointConfig(
            path_template="/friv/multisport.htm",
            operation_id="getMultiSportPlayers",
            wait_for_element="#multisport",
            parser=self._multi_sport_players_parser.parse,
            response_type=MultiSportPlayers,
            timeout_ms=timeout_ms,
        )

    # ── Pronunciation Guide ──────────────────────────────────────────────────

    def _get_pronunciation_guide_config(
        self,
        *,
        timeout_ms: Optional[int] = None,
    ) -> EndpointConfig:
        r"""Fetch the player name pronunciation guide.

        Scrapes the PFR page at ``/friv/pronunciation-guide.htm`` and
        returns a list of player names with their phonetic pronunciations,
        sourced from NFL and team media guides.

        Args:
            timeout_ms: Optional timeout in milliseconds for the page
                selector.

        Returns:
            A :class:`~griddy.pfr.models.PronunciationGuide` instance
            containing the pronunciation entries.
        """
        return EndpointConfig(
            path_template="/friv/pronunciation-guide.htm",
            operation_id="getPronunciationGuide",
            wait_for_element="#content ul",
            parser=self._pronunciation_guide_parser.parse,
            response_type=PronunciationGuide,
            timeout_ms=timeout_ms,
        )

    # ── Overtime Ties ──────────────────────────────────────────────────────

    def _get_overtime_ties_config(
        self,
        *,
        timeout_ms: Optional[int] = None,
    ) -> EndpointConfig:
        r"""Fetch all tied games since sudden-death overtime (1974).

        Scrapes the PFR page at ``/friv/nfl-ties.htm`` and returns a list
        of all games that ended in a tie since sudden-death overtime was
        instituted in 1974.

        Args:
            timeout_ms: Optional timeout in milliseconds for the page
                selector.

        Returns:
            A :class:`~griddy.pfr.models.OvertimeTies` instance
            containing the tie game entries.
        """
        return EndpointConfig(
            path_template="/friv/nfl-ties.htm",
            operation_id="getOvertimeTies",
            wait_for_element="#ot_ties",
            parser=self._overtime_ties_parser.parse,
            response_type=OvertimeTies,
            timeout_ms=timeout_ms,
        )

    # ── Last Undefeated Team ────────────────────────────────────────────────

    def _get_last_undefeated_config(
        self,
        *,
        timeout_ms: Optional[int] = None,
    ) -> EndpointConfig:
        r"""Fetch the last undefeated team(s) in every season.

        Scrapes the PFR page at ``/friv/last-undefeated.htm`` and returns
        a season-by-season breakdown of the last undefeated team (or teams)
        in each league, including playoffs.

        Args:
            timeout_ms: Optional timeout in milliseconds for the page
                selector.

        Returns:
            A :class:`~griddy.pfr.models.LastUndefeated` instance
            containing the undefeated team entries.
        """
        return EndpointConfig(
            path_template="/friv/last-undefeated.htm",
            operation_id="getLastUndefeated",
            wait_for_element="#undefeated_teams",
            parser=self._last_undefeated_parser.parse,
            response_type=LastUndefeated,
            timeout_ms=timeout_ms,
        )

    # ── Standings on Any Date ────────────────────────────────────────────────

    def _get_standings_on_date_config(
        self,
        *,
        year: int,
        month: Optional[int] = None,
        day: Optional[int] = None,
        week: Optional[int] = None,
        timeout_ms: Optional[int] = None,
    ) -> EndpointConfig:
        r"""Fetch NFL standings as of a specific date or week.

        Scrapes the PFR page at ``/boxscores/standings.cgi`` and returns
        conference standings broken out by division, including win-loss
        records, point differentials, and margin of victory.

        Provide either ``week`` (for standings after a specific week) or
        ``month`` + ``day`` (for standings on a calendar date).

        Args:
            year: The season year (e.g. ``2024``).
            month: Calendar month (1–12). Required with ``day``.
            day: Calendar day (1–31). Required with ``month``.
            week: Week number (1–18). Alternative to month/day.
            timeout_ms: Optional timeout in milliseconds for the page
                selector.

        Returns:
            A :class:`~griddy.pfr.models.StandingsOnDate` instance
            containing team standings grouped by conference and division.

        Raises:
            ValueError: If neither ``week`` nor ``month``/``day`` are
                provided.
        """
        if week is not None:
            query: dict[str, str] = {"week": str(week), "year": str(year)}
        elif month is not None and day is not None:
            query = {
                "month": str(month),
                "day": str(day),
                "year": str(year),
            }
        else:
            raise ValueError("Provide either 'week' or both 'month' and 'day'.")

        return EndpointConfig(
            path_template="/boxscores/standings.cgi",
            operation_id="getStandingsOnDate",
            wait_for_element="#AFC",
            parser=self._standings_on_date_parser.parse,
            response_type=StandingsOnDate,
            query_params=query,
            timeout_ms=timeout_ms,
        )
