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
"""

from typing import Optional

from griddy.pfr.parsers.birthdays import BirthdaysParser
from griddy.pfr.parsers.birthplaces import BirthplacesParser
from griddy.pfr.parsers.cups_of_coffee import CupsOfCoffeeParser
from griddy.pfr.parsers.multi_team_players import MultiTeamPlayersParser
from griddy.pfr.parsers.non_qb_passers import NonQBPassersParser
from griddy.pfr.parsers.non_skill_pos_td import NonSkillPosTdParser
from griddy.pfr.parsers.octopus_tracker import OctopusTrackerParser
from griddy.pfr.parsers.players_born_before import PlayersBornBeforeParser
from griddy.pfr.parsers.qb_wins import QBWinsParser
from griddy.pfr.parsers.statistical_milestones import StatisticalMilestonesParser
from griddy.pfr.parsers.uniform_numbers import UniformNumbersParser
from griddy.pfr.parsers.upcoming_milestones import UpcomingMilestonesParser

from ..basesdk import BaseSDK, EndpointConfig
from ..models import (
    Birthdays,
    BirthplaceFiltered,
    BirthplaceLanding,
    CupsOfCoffee,
    MultiTeamPlayers,
    NonQBPassers,
    NonSkillPosTdScorers,
    OctopusTracker,
    PlayersBornBefore,
    QBWins,
    StatisticalMilestones,
    UniformNumbers,
    UpcomingMilestones,
)

_multi_team_parser = MultiTeamPlayersParser()
_milestones_parser = StatisticalMilestonesParser()
_upcoming_parser = UpcomingMilestonesParser()
_birthdays_parser = BirthdaysParser()
_birthplaces_parser = BirthplacesParser()
_born_before_parser = PlayersBornBeforeParser()
_uniform_numbers_parser = UniformNumbersParser()
_qb_wins_parser = QBWinsParser()
_non_qb_passers_parser = NonQBPassersParser()
_non_skill_pos_td_parser = NonSkillPosTdParser()
_octopus_tracker_parser = OctopusTrackerParser()
_cups_of_coffee_parser = CupsOfCoffeeParser()


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

    # ── Players Born Before a Date ────────────────────────────────────

    def _get_players_born_before_config(
        self,
        *,
        month: int,
        day: int,
        year: int,
        timeout_ms: Optional[int] = None,
    ) -> EndpointConfig:
        return EndpointConfig(
            path_template="/friv/age.cgi",
            operation_id="getPlayersBornBefore",
            wait_for_element="#players",
            parser=_born_before_parser.parse,
            response_type=PlayersBornBefore,
            query_params={
                "month": str(month),
                "day": str(day),
                "year": str(year),
            },
            timeout_ms=timeout_ms,
        )

    def get_players_born_before(
        self,
        *,
        month: int,
        day: int,
        year: int,
        timeout_ms: Optional[int] = None,
    ) -> PlayersBornBefore:
        """Fetch active players born on or before a given date.

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
        config = self._get_players_born_before_config(
            month=month, day=day, year=year, timeout_ms=timeout_ms
        )
        data = self._execute_endpoint(config)
        return PlayersBornBefore.model_validate(data)

    # ── Players By Uniform Number ──────────────────────────────────────

    def _get_uniform_numbers_config(
        self,
        *,
        number: int,
        team: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> EndpointConfig:
        query: dict[str, str] = {"number": str(number)}
        if team:
            query["team"] = team

        return EndpointConfig(
            path_template="/players/uniform.cgi",
            operation_id="getUniformNumbers",
            wait_for_element="#uniform_number",
            parser=_uniform_numbers_parser.parse,
            response_type=UniformNumbers,
            query_params=query,
            timeout_ms=timeout_ms,
        )

    def get_uniform_numbers(
        self,
        *,
        number: int,
        team: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> UniformNumbers:
        """Fetch players who wore a specific uniform number.

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
        config = self._get_uniform_numbers_config(
            number=number, team=team, timeout_ms=timeout_ms
        )
        data = self._execute_endpoint(config)
        return UniformNumbers.model_validate(data)

    # ── Quarterback Wins vs. Each Franchise ──────────────────────────────

    def _get_qb_wins_vs_franchises_config(
        self,
        *,
        timeout_ms: Optional[int] = None,
    ) -> EndpointConfig:
        return EndpointConfig(
            path_template="/friv/qb-wins.htm",
            operation_id="getQBWinsVsFranchises",
            wait_for_element="#qb_wins",
            parser=_qb_wins_parser.parse,
            response_type=QBWins,
            timeout_ms=timeout_ms,
        )

    def get_qb_wins_vs_franchises(
        self,
        *,
        timeout_ms: Optional[int] = None,
    ) -> QBWins:
        """Fetch quarterbacks who beat every (or nearly every) franchise.

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
        config = self._get_qb_wins_vs_franchises_config(timeout_ms=timeout_ms)
        data = self._execute_endpoint(config)
        return QBWins.model_validate(data)

    # ── Non-Quarterback Passers ──────────────────────────────────────────

    def _get_non_qb_passers_config(
        self,
        *,
        timeout_ms: Optional[int] = None,
    ) -> EndpointConfig:
        return EndpointConfig(
            path_template="/friv/nonqb.htm",
            operation_id="getNonQBPassers",
            wait_for_element="#nonqb_passers",
            parser=_non_qb_passers_parser.parse,
            response_type=NonQBPassers,
            timeout_ms=timeout_ms,
        )

    def get_non_qb_passers(
        self,
        *,
        timeout_ms: Optional[int] = None,
    ) -> NonQBPassers:
        """Fetch non-quarterback players who have thrown a pass.

        Scrapes the PFR page at ``/friv/nonqb.htm`` and returns a list
        of non-QB players with their passing statistics.

        Args:
            timeout_ms: Optional timeout in milliseconds for the page
                selector.

        Returns:
            A :class:`~griddy.pfr.models.NonQBPassers` instance
            containing the player entries with passing stats.
        """
        config = self._get_non_qb_passers_config(timeout_ms=timeout_ms)
        data = self._execute_endpoint(config)
        return NonQBPassers.model_validate(data)

    # ── Non-Skill Position TD Scorers ─────────────────────────────────────

    def _get_non_skill_pos_td_scorers_config(
        self,
        *,
        timeout_ms: Optional[int] = None,
    ) -> EndpointConfig:
        return EndpointConfig(
            path_template="/friv/odd_td.htm",
            operation_id="getNonSkillPosTdScorers",
            wait_for_element="#odd_scorers",
            parser=_non_skill_pos_td_parser.parse,
            response_type=NonSkillPosTdScorers,
            timeout_ms=timeout_ms,
        )

    def get_non_skill_pos_td_scorers(
        self,
        *,
        timeout_ms: Optional[int] = None,
    ) -> NonSkillPosTdScorers:
        """Fetch non-skill position players who scored an offensive TD.

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
        config = self._get_non_skill_pos_td_scorers_config(timeout_ms=timeout_ms)
        data = self._execute_endpoint(config)
        return NonSkillPosTdScorers.model_validate(data)

    # ── Octopus Tracker ────────────────────────────────────────────────────

    def _get_octopus_tracker_config(
        self,
        *,
        timeout_ms: Optional[int] = None,
    ) -> EndpointConfig:
        return EndpointConfig(
            path_template="/friv/octopus-tracker.htm",
            operation_id="getOctopusTracker",
            wait_for_element="#octopus",
            parser=_octopus_tracker_parser.parse,
            response_type=OctopusTracker,
            timeout_ms=timeout_ms,
        )

    def get_octopus_tracker(
        self,
        *,
        timeout_ms: Optional[int] = None,
    ) -> OctopusTracker:
        """Fetch octopus TD + 2pt conversion scorers since 1994.

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
        config = self._get_octopus_tracker_config(timeout_ms=timeout_ms)
        data = self._execute_endpoint(config)
        return OctopusTracker.model_validate(data)

    # ── Cups of Coffee ──────────────────────────────────────────────────────

    def _get_cups_of_coffee_config(
        self,
        *,
        timeout_ms: Optional[int] = None,
    ) -> EndpointConfig:
        return EndpointConfig(
            path_template="/friv/coffee.htm",
            operation_id="getCupsOfCoffee",
            wait_for_element="#coffee",
            parser=_cups_of_coffee_parser.parse,
            response_type=CupsOfCoffee,
            timeout_ms=timeout_ms,
        )

    def get_cups_of_coffee(
        self,
        *,
        timeout_ms: Optional[int] = None,
    ) -> CupsOfCoffee:
        """Fetch players who played only a single game in the NFL.

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
        config = self._get_cups_of_coffee_config(timeout_ms=timeout_ms)
        data = self._execute_endpoint(config)
        return CupsOfCoffee.model_validate(data)
