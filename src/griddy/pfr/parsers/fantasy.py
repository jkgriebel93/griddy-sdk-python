"""Parser for PFR Fantasy Rankings pages.

Handles:
- ``/years/{year}/fantasy.htm`` — Top Fantasy Players (table ``#fantasy``)
- ``/fantasy/{position}-fantasy-matchups.htm`` — Fantasy Matchups
  (table ``#fantasy_stats``)
- ``/years/{year}/fantasy-points-against-{position}.htm`` — Fantasy Points
  Allowed (table ``#fantasy_def``)
- ``/years/{year}/redzone-passing.htm`` — Red Zone Passing
  (table ``#fantasy_rz``)
- ``/years/{year}/redzone-receiving.htm`` — Red Zone Receiving
  (table ``#fantasy_rz``)
- ``/years/{year}/redzone-rushing.htm`` — Red Zone Rushing
  (table ``#fantasy_rz``)
"""

from typing import Any, Dict, List

from bs4 import BeautifulSoup, Tag

from ._column_registry import (
    FANTASY_MATCHUPS,
    FANTASY_POINTS_ALLOWED,
    FANTASY_RZ_PASSING,
    FANTASY_RZ_RECEIVING,
    FANTASY_RZ_RUSHING,
    FANTASY_TOP_PLAYERS,
)
from ._helpers import safe_int, safe_numeric, safe_pct


class FantasyParser:
    """Parses PFR Fantasy Rankings pages into structured data dicts."""

    def parse_top_players(self, html: str) -> Dict[str, Any]:
        """Parse the top fantasy players page.

        Returns:
            A dict with key ``players``.
        """
        soup = BeautifulSoup(html, "html.parser")

        table = soup.find("table", id="fantasy")
        if table is None:
            return {"players": []}

        players = self._parse_player_rows(table)
        return {"players": players}

    def _parse_player_rows(self, table: Tag) -> List[Dict[str, Any]]:
        """Extract player rows from the fantasy table."""
        tbody = table.find("tbody")
        if tbody is None:
            return []

        players: List[Dict[str, Any]] = []

        for tr in tbody.find_all("tr"):
            if "thead" in (tr.get("class") or []):
                continue

            row: Dict[str, Any] = {}
            all_empty = True

            for cell in tr.find_all(["th", "td"]):
                stat = cell.get("data-stat", "")
                if not stat:
                    continue

                text = cell.get_text(strip=True).replace("\xa0", " ")
                if text:
                    all_empty = False

                link = cell.find("a")

                if stat == "ranker":
                    row["rank"] = safe_int(text)
                elif stat == "player":
                    row["player"] = text or None
                    if link:
                        row["player_href"] = link.get("href")
                    player_id = cell.get("data-append-csv")
                    if player_id:
                        row["player_id"] = player_id
                elif stat == "team":
                    row["team"] = text or None
                    if link:
                        row["team_href"] = link.get("href")
                elif stat == "fantasy_pos":
                    row["fantasy_pos"] = text or None
                elif stat == "age":
                    row["age"] = safe_int(text)
                elif stat in FANTASY_TOP_PLAYERS.int_columns:
                    row[stat] = safe_int(text)
                elif stat in FANTASY_TOP_PLAYERS.float_columns:
                    row[stat] = safe_numeric(text)

            if not all_empty:
                players.append(row)

        return players

    # ── Matchups (/fantasy/{position}-fantasy-matchups.htm) ──────────

    def parse_matchups(self, html: str) -> Dict[str, Any]:
        """Parse a fantasy matchups page.

        Works for any position (QB, WR, RB, TE) since the parser reads
        whichever ``data-stat`` columns are present in the table.

        Returns:
            A dict with key ``players``.
        """
        soup = BeautifulSoup(html, "html.parser")

        table = soup.find("table", id="fantasy_stats")
        if table is None:
            return {"players": []}

        players = self._parse_matchup_rows(table)
        return {"players": players}

    def _parse_matchup_rows(self, table: Tag) -> List[Dict[str, Any]]:
        """Extract player rows from the fantasy_stats matchup table."""
        tbody = table.find("tbody")
        if tbody is None:
            return []

        players: List[Dict[str, Any]] = []

        for tr in tbody.find_all("tr"):
            if "thead" in (tr.get("class") or []):
                continue

            row: Dict[str, Any] = {}
            all_empty = True

            for cell in tr.find_all(["th", "td"]):
                stat = cell.get("data-stat", "")
                if not stat:
                    continue

                text = cell.get_text(strip=True).replace("\xa0", " ")
                if text:
                    all_empty = False

                link = cell.find("a")

                if stat == "player":
                    row["player"] = text or None
                    if link:
                        row["player_href"] = link.get("href")
                    player_id = cell.get("data-append-csv")
                    if player_id:
                        row["player_id"] = player_id
                elif stat == "team":
                    row["team"] = text or None
                    if link:
                        row["team_href"] = link.get("href")
                elif stat == "opp":
                    row["opp"] = text or None
                    if link:
                        row["opp_href"] = link.get("href")
                elif stat == "injury":
                    row["injury"] = text or None
                elif stat == "snaps":
                    row["snaps"] = text or None
                elif stat == "at_or_vs":
                    row["at_or_vs"] = text or None
                elif stat == "ranker":
                    row["rank"] = safe_int(text)
                elif stat in FANTASY_MATCHUPS.int_columns:
                    row[stat] = safe_int(text)
                elif stat in FANTASY_MATCHUPS.float_columns:
                    row[stat] = safe_numeric(text)

            if not all_empty:
                players.append(row)

        return players

    # ── Points Allowed (/years/{year}/fantasy-points-against-{pos}.htm) ──

    def parse_points_allowed(self, html: str) -> Dict[str, Any]:
        """Parse a fantasy points allowed page.

        Works for any position (QB, WR, RB, TE) since the parser reads
        whichever ``data-stat`` columns are present in the table.

        Returns:
            A dict with key ``teams``.
        """
        soup = BeautifulSoup(html, "html.parser")

        table = soup.find("table", id="fantasy_def")
        if table is None:
            return {"teams": []}

        teams = self._parse_points_allowed_rows(table)
        return {"teams": teams}

    def _parse_points_allowed_rows(self, table: Tag) -> List[Dict[str, Any]]:
        """Extract team rows from the fantasy_def table."""
        tbody = table.find("tbody")
        if tbody is None:
            return []

        teams: List[Dict[str, Any]] = []

        for tr in tbody.find_all("tr"):
            if "thead" in (tr.get("class") or []):
                continue

            row: Dict[str, Any] = {}
            all_empty = True

            for cell in tr.find_all(["th", "td"]):
                stat = cell.get("data-stat", "")
                if not stat:
                    continue

                text = cell.get_text(strip=True).replace("\xa0", " ")
                if text:
                    all_empty = False

                link = cell.find("a")

                if stat == "team":
                    row["team"] = text or None
                    if link:
                        row["team_href"] = link.get("href")
                elif stat in FANTASY_POINTS_ALLOWED.int_columns:
                    row[stat] = safe_int(text)
                elif stat in FANTASY_POINTS_ALLOWED.float_columns:
                    row[stat] = safe_numeric(text)

            if not all_empty:
                teams.append(row)

        return teams

    # ── Red Zone Passing (/years/{year}/redzone-passing.htm) ───────────

    def parse_redzone_passing(self, html: str) -> Dict[str, Any]:
        """Parse the red zone passing page.

        Returns:
            A dict with key ``players``.
        """
        soup = BeautifulSoup(html, "html.parser")

        table = soup.find("table", id="fantasy_rz")
        if table is None:
            return {"players": []}

        players = self._parse_rz_passing_rows(table)
        return {"players": players}

    def _parse_rz_passing_rows(self, table: Tag) -> List[Dict[str, Any]]:
        """Extract player rows from the red zone passing table."""
        tbody = table.find("tbody")
        if tbody is None:
            return []

        players: List[Dict[str, Any]] = []

        for tr in tbody.find_all("tr"):
            if "thead" in (tr.get("class") or []):
                continue

            row: Dict[str, Any] = {}
            all_empty = True

            for cell in tr.find_all(["th", "td"]):
                stat = cell.get("data-stat", "")
                if not stat:
                    continue

                text = cell.get_text(strip=True).replace("\xa0", " ")
                if text:
                    all_empty = False

                link = cell.find("a")

                if stat == "player":
                    row["player"] = text or None
                    if link:
                        row["player_href"] = link.get("href")
                    player_id = cell.get("data-append-csv")
                    if player_id:
                        row["player_id"] = player_id
                elif stat == "team":
                    row["team"] = text or None
                    if link:
                        row["team_href"] = link.get("href")
                elif stat == "link":
                    if link:
                        row["link_href"] = link.get("href")
                elif stat in FANTASY_RZ_PASSING.int_columns:
                    row[stat] = safe_int(text)
                elif stat in FANTASY_RZ_PASSING.float_columns:
                    row[stat] = safe_numeric(text)

            if not all_empty:
                players.append(row)

        return players

    # ── Red Zone Receiving (/years/{year}/redzone-receiving.htm) ───────

    def parse_redzone_receiving(self, html: str) -> Dict[str, Any]:
        """Parse the red zone receiving page.

        Returns:
            A dict with key ``players``.
        """
        soup = BeautifulSoup(html, "html.parser")

        table = soup.find("table", id="fantasy_rz")
        if table is None:
            return {"players": []}

        players = self._parse_rz_receiving_rows(table)
        return {"players": players}

    def _parse_rz_receiving_rows(self, table: Tag) -> List[Dict[str, Any]]:
        """Extract player rows from the red zone receiving table."""
        tbody = table.find("tbody")
        if tbody is None:
            return []

        players: List[Dict[str, Any]] = []

        for tr in tbody.find_all("tr"):
            if "thead" in (tr.get("class") or []):
                continue

            row: Dict[str, Any] = {}
            all_empty = True

            for cell in tr.find_all(["th", "td"]):
                stat = cell.get("data-stat", "")
                if not stat:
                    continue

                text = cell.get_text(strip=True).replace("\xa0", " ")
                if text:
                    all_empty = False

                link = cell.find("a")

                if stat == "player":
                    row["player"] = text or None
                    if link:
                        row["player_href"] = link.get("href")
                    player_id = cell.get("data-append-csv")
                    if player_id:
                        row["player_id"] = player_id
                elif stat == "team":
                    row["team"] = text or None
                    if link:
                        row["team_href"] = link.get("href")
                elif stat == "link":
                    if link:
                        row["link_href"] = link.get("href")
                elif stat in FANTASY_RZ_RECEIVING.int_columns:
                    row[stat] = safe_int(text)
                elif stat in FANTASY_RZ_RECEIVING.pct_columns:
                    row[stat] = safe_pct(text)

            if not all_empty:
                players.append(row)

        return players

    # ── Red Zone Rushing (/years/{year}/redzone-rushing.htm) ──────────

    def parse_redzone_rushing(self, html: str) -> Dict[str, Any]:
        """Parse the red zone rushing page.

        Returns:
            A dict with key ``players``.
        """
        soup = BeautifulSoup(html, "html.parser")

        table = soup.find("table", id="fantasy_rz")
        if table is None:
            return {"players": []}

        players = self._parse_rz_rushing_rows(table)
        return {"players": players}

    def _parse_rz_rushing_rows(self, table: Tag) -> List[Dict[str, Any]]:
        """Extract player rows from the red zone rushing table."""
        tbody = table.find("tbody")
        if tbody is None:
            return []

        players: List[Dict[str, Any]] = []

        for tr in tbody.find_all("tr"):
            if "thead" in (tr.get("class") or []):
                continue

            row: Dict[str, Any] = {}
            all_empty = True

            for cell in tr.find_all(["th", "td"]):
                stat = cell.get("data-stat", "")
                if not stat:
                    continue

                text = cell.get_text(strip=True).replace("\xa0", " ")
                if text:
                    all_empty = False

                link = cell.find("a")

                if stat == "player":
                    row["player"] = text or None
                    if link:
                        row["player_href"] = link.get("href")
                    player_id = cell.get("data-append-csv")
                    if player_id:
                        row["player_id"] = player_id
                elif stat == "team":
                    row["team"] = text or None
                    if link:
                        row["team_href"] = link.get("href")
                elif stat == "link":
                    if link:
                        row["link_href"] = link.get("href")
                elif stat in FANTASY_RZ_RUSHING.int_columns:
                    row[stat] = safe_int(text)
                elif stat in FANTASY_RZ_RUSHING.pct_columns:
                    row[stat] = safe_pct(text)

            if not all_empty:
                players.append(row)

        return players
