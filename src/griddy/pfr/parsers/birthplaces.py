"""Parser for the PFR Player Birthplaces pages.

Landing page (``/friv/birthplaces.htm``):
    Parses the summary table listing countries/states with player counts.

Filtered page (``/friv/birthplaces.cgi?country=...&state=...``):
    Parses the player table with career stats for a specific location.
"""

import re
from typing import Any, Dict, List, Optional

from bs4 import BeautifulSoup, Tag

from griddy.pfr.errors import ParsingError

from ._column_registry import BIRTHPLACES_FILTERED, BIRTHPLACES_LANDING
from ._helpers import safe_int


class BirthplacesParser:
    """Parses the PFR birthplaces pages (landing and filtered)."""

    # ── Landing page helpers ─────────────────────────────────────────

    @staticmethod
    def _extract_landing_title(soup: BeautifulSoup) -> str:
        """Extract the landing page title from the h2 section heading."""
        content = soup.find("div", id="content")
        if content:
            h2 = content.find("h2")
            if h2:
                return h2.get_text(strip=True)
        return ""

    def _parse_landing_table(self, table: Tag) -> List[Dict[str, Any]]:
        """Parse the birthplaces landing summary table."""
        entries: List[Dict[str, Any]] = []

        tbody = table.find("tbody")
        if tbody is None:
            return entries

        for row in tbody.find_all("tr"):
            classes = row.get("class") or []
            if "thead" in classes or "over_header" in classes:
                continue

            # Rank
            rank_cell = row.find(["th", "td"], {"data-stat": "ranker"})
            if not rank_cell:
                continue
            rank = safe_int(rank_cell.get_text(strip=True))
            if rank is None:
                continue

            # Country
            country_cell = row.find(["th", "td"], {"data-stat": "birth_country"})
            if not country_cell:
                continue
            birth_country = country_cell.get_text(strip=True)
            birth_country_href: Optional[str] = None
            country_link = country_cell.find("a")
            if country_link and country_link.get("href"):
                birth_country_href = country_link["href"]

            # State
            state_cell = row.find(["th", "td"], {"data-stat": "birth_state"})
            birth_state = state_cell.get_text(strip=True) if state_cell else None
            if not birth_state:
                birth_state = None

            entry: Dict[str, Any] = {
                "rank": rank,
                "birth_country": birth_country,
                "birth_country_href": birth_country_href,
                "birth_state": birth_state,
            }

            # Integer columns
            for col in BIRTHPLACES_LANDING.int_columns:
                cell = row.find(["th", "td"], {"data-stat": col})
                entry[col] = safe_int(cell.get_text(strip=True)) if cell else None

            # Player with most TDs
            td_player_cell = row.find(["th", "td"], {"data-stat": "player_most_td"})
            if td_player_cell:
                entry["player_most_td"] = td_player_cell.get_text(strip=True) or None
                entry["player_most_td_id"] = (
                    td_player_cell.get("data-append-csv") or None
                )
                td_link = td_player_cell.find("a")
                entry["player_most_td_href"] = (
                    td_link["href"] if td_link and td_link.get("href") else None
                )
            else:
                entry["player_most_td"] = None
                entry["player_most_td_href"] = None
                entry["player_most_td_id"] = None

            # Player with most games
            g_player_cell = row.find(["th", "td"], {"data-stat": "player_most_g"})
            if g_player_cell:
                entry["player_most_g"] = g_player_cell.get_text(strip=True) or None
                entry["player_most_g_id"] = g_player_cell.get("data-append-csv") or None
                g_link = g_player_cell.find("a")
                entry["player_most_g_href"] = (
                    g_link["href"] if g_link and g_link.get("href") else None
                )
            else:
                entry["player_most_g"] = None
                entry["player_most_g_href"] = None
                entry["player_most_g_id"] = None

            entries.append(entry)

        return entries

    def parse_landing(self, html: str) -> Dict[str, Any]:
        """Parse the birthplaces landing page.

        Args:
            html: Raw HTML of the PFR birthplaces landing page.

        Returns:
            A dict ready for ``BirthplaceLanding.model_validate()``.

        Raises:
            ParsingError: If the birthplaces table is not found.
        """
        soup = BeautifulSoup(html, "html.parser")

        title = self._extract_landing_title(soup)

        table = soup.find("table", id="birthplaces")
        if table is None:
            raise ParsingError(
                "Could not find birthplaces table in the HTML.",
                selector="birthplaces",
                html_sample=html[:500],
            )

        locations = self._parse_landing_table(table)

        return {
            "title": title,
            "locations": locations,
        }

    # ── Filtered page helpers ────────────────────────────────────────

    @staticmethod
    def _extract_filtered_title(soup: BeautifulSoup) -> str:
        """Extract the filtered page title from h1 inside #content."""
        content = soup.find("div", id="content")
        if content:
            h1 = content.find("h1")
            if h1:
                return h1.get_text(strip=True)
        return ""

    @staticmethod
    def _extract_country_state(title: str) -> tuple[str, str]:
        """Extract country and state from a title like
        'List of all NFL Players Born in Pennsylvania,  USA'.

        Returns:
            A ``(country, state)`` tuple. State may be empty.
        """
        match = re.search(r"Born in\s+(.+?)(?:,\s+(.+))?$", title)
        if match:
            state_or_country = match.group(1).strip()
            country = match.group(2).strip() if match.group(2) else ""
            if country:
                return country, state_or_country
            return state_or_country, ""
        return "", ""

    def _parse_filtered_table(self, table: Tag) -> List[Dict[str, Any]]:
        """Parse the birthplaces filtered player table."""
        entries: List[Dict[str, Any]] = []

        tbody = table.find("tbody")
        if tbody is None:
            return entries

        for row in tbody.find_all("tr"):
            classes = row.get("class") or []
            if "thead" in classes or "over_header" in classes:
                continue

            # Rank
            rank_cell = row.find(["th", "td"], {"data-stat": "ranker"})
            if not rank_cell:
                continue
            rank = safe_int(rank_cell.get_text(strip=True))
            if rank is None:
                continue

            # Player name, href, and id
            player_cell = row.find(["th", "td"], {"data-stat": "player"})
            if not player_cell:
                continue

            player_name = player_cell.get_text(strip=True)
            player_href: Optional[str] = None
            player_id: Optional[str] = player_cell.get("data-append-csv") or None

            link = player_cell.find("a")
            if link and link.get("href"):
                player_href = link["href"]

            # Position
            pos_cell = row.find(["th", "td"], {"data-stat": "pos"})
            pos = pos_cell.get_text(strip=True) if pos_cell else None
            if not pos:
                pos = None

            # Birth city
            city_cell = row.find(["th", "td"], {"data-stat": "birth_city"})
            birth_city = city_cell.get_text(strip=True) if city_cell else None
            if not birth_city:
                birth_city = None

            entry: Dict[str, Any] = {
                "rank": rank,
                "player": player_name,
                "player_href": player_href,
                "player_id": player_id,
                "pos": pos,
                "birth_city": birth_city,
            }

            # Integer stat columns
            for col in BIRTHPLACES_FILTERED.int_columns:
                cell = row.find(["th", "td"], {"data-stat": col})
                entry[col] = safe_int(cell.get_text(strip=True)) if cell else None

            entries.append(entry)

        return entries

    def parse_filtered(self, html: str) -> Dict[str, Any]:
        """Parse the birthplaces filtered (by location) page.

        Args:
            html: Raw HTML of the PFR birthplaces filtered page.

        Returns:
            A dict ready for ``BirthplaceFiltered.model_validate()``.

        Raises:
            ParsingError: If the birthplaces table is not found.
        """
        soup = BeautifulSoup(html, "html.parser")

        title = self._extract_filtered_title(soup)
        country, state = self._extract_country_state(title)

        table = soup.find("table", id="birthplaces")
        if table is None:
            raise ParsingError(
                "Could not find birthplaces table in the HTML.",
                selector="birthplaces",
                html_sample=html[:500],
            )

        players = self._parse_filtered_table(table)

        return {
            "title": title,
            "country": country,
            "state": state,
            "players": players,
        }
