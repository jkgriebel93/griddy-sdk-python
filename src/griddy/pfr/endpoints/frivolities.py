"""Frivolities endpoint for Pro Football Reference.

Provides:
- ``get_multi_team_players()`` — Players who played for multiple teams/franchises
  (``/friv/players-who-played-for-multiple-teams-franchises.fcgi``)
"""

from typing import Optional

from griddy.pfr.parsers.multi_team_players import MultiTeamPlayersParser

from ..basesdk import BaseSDK, EndpointConfig
from ..models import MultiTeamPlayers

_parser = MultiTeamPlayersParser()


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
            parser=_parser.parse,
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
