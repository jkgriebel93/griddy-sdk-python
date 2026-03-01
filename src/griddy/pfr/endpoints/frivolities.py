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
"""

from typing import Optional

from griddy.pfr.parsers.birthdays import BirthdaysParser
from griddy.pfr.parsers.birthplaces import BirthplacesParser
from griddy.pfr.parsers.multi_team_players import MultiTeamPlayersParser
from griddy.pfr.parsers.statistical_milestones import StatisticalMilestonesParser
from griddy.pfr.parsers.upcoming_milestones import UpcomingMilestonesParser

from ..basesdk import BaseSDK, EndpointConfig
from ..models import (
    Birthdays,
    BirthplaceFiltered,
    BirthplaceLanding,
    MultiTeamPlayers,
    StatisticalMilestones,
    UpcomingMilestones,
)

_multi_team_parser = MultiTeamPlayersParser()
_milestones_parser = StatisticalMilestonesParser()
_upcoming_parser = UpcomingMilestonesParser()
_birthdays_parser = BirthdaysParser()
_birthplaces_parser = BirthplacesParser()


class Frivolities(BaseSDK):
    """Sub-SDK for PFR Frivolities & Fun Stuff pages."""

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
            parser=_multi_team_parser.parse,
            response_type=MultiTeamPlayers,
            query_params=query,
            timeout_ms=timeout_ms,
        )

    def get_multi_team_players(
        self,
        *,
        t1: str,
        t2: str,
        t3: Optional[str] = None,
        t4: Optional[str] = None,
        exclusively: bool = False,
        timeout_ms: Optional[int] = None,
    ) -> MultiTeamPlayers:
        """Fetch players who played for multiple teams/franchises.

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
        config = self._get_multi_team_players_config(
            t1=t1,
            t2=t2,
            t3=t3,
            t4=t4,
            exclusively=exclusively,
            timeout_ms=timeout_ms,
        )
        data = self._execute_endpoint(config)
        return MultiTeamPlayers.model_validate(data)

    # ── Statistical Milestones ──────────────────────────────────────

    def _get_statistical_milestones_config(
        self,
        *,
        stat: str,
        timeout_ms: Optional[int] = None,
    ) -> EndpointConfig:
        return EndpointConfig(
            path_template="/friv/milestones.cgi",
            operation_id="getStatisticalMilestones",
            wait_for_element="#milestones",
            parser=_milestones_parser.parse,
            response_type=StatisticalMilestones,
            query_params={"stat": stat},
            timeout_ms=timeout_ms,
        )

    def get_statistical_milestones(
        self,
        *,
        stat: str,
        timeout_ms: Optional[int] = None,
    ) -> StatisticalMilestones:
        """Fetch statistical milestones and career leaders for a stat.

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
        config = self._get_statistical_milestones_config(
            stat=stat,
            timeout_ms=timeout_ms,
        )
        data = self._execute_endpoint(config)
        return StatisticalMilestones.model_validate(data)

    # ── Upcoming Milestones ───────────────────────────────────────

    def _get_upcoming_milestones_config(
        self,
        *,
        timeout_ms: Optional[int] = None,
    ) -> EndpointConfig:
        return EndpointConfig(
            path_template="/friv/upcoming-milestones.htm",
            operation_id="getUpcomingMilestones",
            wait_for_element="#upcoming_milestones",
            parser=_upcoming_parser.parse,
            response_type=UpcomingMilestones,
            timeout_ms=timeout_ms,
        )

    def get_upcoming_milestones(
        self,
        *,
        timeout_ms: Optional[int] = None,
    ) -> UpcomingMilestones:
        """Fetch upcoming milestones and leaderboard movements.

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
        config = self._get_upcoming_milestones_config(timeout_ms=timeout_ms)
        data = self._execute_endpoint(config)
        return UpcomingMilestones.model_validate(data)

    # ── Birthdays ──────────────────────────────────────────────────

    def _get_birthdays_config(
        self,
        *,
        month: int,
        day: int,
        timeout_ms: Optional[int] = None,
    ) -> EndpointConfig:
        return EndpointConfig(
            path_template="/friv/birthdays.cgi",
            operation_id="getBirthdays",
            wait_for_element="#birthdays",
            parser=_birthdays_parser.parse,
            response_type=Birthdays,
            query_params={"month": str(month), "day": str(day)},
            timeout_ms=timeout_ms,
        )

    def get_birthdays(
        self,
        *,
        month: int,
        day: int,
        timeout_ms: Optional[int] = None,
    ) -> Birthdays:
        """Fetch NFL players born on a given month and day.

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
        config = self._get_birthdays_config(month=month, day=day, timeout_ms=timeout_ms)
        data = self._execute_endpoint(config)
        return Birthdays.model_validate(data)

    # ── Birthplaces ───────────────────────────────────────────────────

    def _get_birthplaces_config(
        self,
        *,
        timeout_ms: Optional[int] = None,
    ) -> EndpointConfig:
        return EndpointConfig(
            path_template="/friv/birthplaces.htm",
            operation_id="getBirthplaces",
            wait_for_element="#birthplaces",
            parser=_birthplaces_parser.parse_landing,
            response_type=BirthplaceLanding,
            timeout_ms=timeout_ms,
        )

    def get_birthplaces(
        self,
        *,
        timeout_ms: Optional[int] = None,
    ) -> BirthplaceLanding:
        """Fetch the birthplaces landing page with location summaries.

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
        config = self._get_birthplaces_config(timeout_ms=timeout_ms)
        data = self._execute_endpoint(config)
        return BirthplaceLanding.model_validate(data)

    def _get_birthplace_players_config(
        self,
        *,
        country: str,
        state: str = "",
        timeout_ms: Optional[int] = None,
    ) -> EndpointConfig:
        return EndpointConfig(
            path_template="/friv/birthplaces.cgi",
            operation_id="getBirthplacePlayers",
            wait_for_element="#birthplaces",
            parser=_birthplaces_parser.parse_filtered,
            response_type=BirthplaceFiltered,
            query_params={"country": country, "state": state},
            timeout_ms=timeout_ms,
        )

    def get_birthplace_players(
        self,
        *,
        country: str,
        state: str = "",
        timeout_ms: Optional[int] = None,
    ) -> BirthplaceFiltered:
        """Fetch NFL players born in a specific country/state.

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
        config = self._get_birthplace_players_config(
            country=country, state=state, timeout_ms=timeout_ms
        )
        data = self._execute_endpoint(config)
        return BirthplaceFiltered.model_validate(data)
