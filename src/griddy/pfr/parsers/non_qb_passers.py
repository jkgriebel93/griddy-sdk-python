"""Parser for the PFR 'Non-Quarterback Passing' page.

Parses ``/friv/nonqb.htm`` including the table listing non-QB players
who have thrown a pass in the NFL (post-1960) with their passing stats.
"""

from typing import Any, Dict, List, Optional

from bs4 import BeautifulSoup, Tag

from ._helpers import safe_float, safe_int

# Columns that should be parsed as integers.
_INT_COLS = frozenset(
    {
        "year_min",
        "year_max",
        "pass_cmp",
        "pass_att",
        "pass_yds",
        "pass_td",
        "pass_int",
        "pass_long",
        "pass_sacked",
        "pass_sacked_yds",
    }
)

# Columns that should be parsed as floats.
_FLOAT_COLS = frozenset(
    {
        "pass_cmp_perc",
        "pass_td_perc",
        "pass_int_perc",
        "pass_yds_per_att",
        "pass_adj_yds_per_att",
        "pass_yds_per_cmp",
        "pass_yds_per_g",
        "pass_rating",
        "qbr",
        "pass_sacked_perc",
        "pass_net_yds_per_att",
        "pass_adj_net_yds_per_att",
    }
)


class NonQBPassersParser:
    """Parses the PFR non-quarterback passers page."""

    @staticmethod
    def _extract_title(soup: BeautifulSoup) -> str:
        """Extract the page title.

        The page uses an ``<h2>`` rather than an ``<h1>`` for the main
        heading, so we fall back to the ``<title>`` tag.
        """
        content = soup.find("div", id="content")
        if content:
            h2 = content.find("h2")
            if h2:
                return h2.get_text(strip=True)
        title_tag = soup.find("title")
        if title_tag:
            return title_tag.get_text(strip=True)
        return ""

    def _parse_table(self, table: Tag) -> List[Dict[str, Any]]:
        """Parse the nonqb_passers stats table."""
        entries: List[Dict[str, Any]] = []

        tbody = table.find("tbody")
        if tbody is None:
            return entries

        for row in tbody.find_all("tr"):
            classes = row.get("class") or []
            if "thead" in classes or "over_header" in classes:
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

            # Position (plain text)
            pos_cell = row.find(["th", "td"], {"data-stat": "pos"})
            pos = pos_cell.get_text(strip=True) if pos_cell else ""

            entry: Dict[str, Any] = {
                "player": player_name,
                "player_href": player_href,
                "player_id": player_id,
                "pos": pos,
            }

            # Parse all numeric stat columns
            for col in _INT_COLS | _FLOAT_COLS:
                cell = row.find(["th", "td"], {"data-stat": col})
                if cell is None:
                    entry[col] = None
                    continue
                raw = cell.get_text(strip=True)
                if not raw:
                    entry[col] = None
                elif col in _INT_COLS:
                    entry[col] = safe_int(raw)
                else:
                    entry[col] = safe_float(raw)

            entries.append(entry)

        return entries

    def parse(self, html: str) -> Dict[str, Any]:
        """Parse the non-quarterback passers page.

        Args:
            html: Raw HTML of the PFR non-QB passers page.

        Returns:
            A dict ready for ``NonQBPassers.model_validate()``.

        Raises:
            ValueError: If the nonqb_passers table is not found.
        """
        soup = BeautifulSoup(html, "html.parser")

        title = self._extract_title(soup)

        table = soup.find("table", id="nonqb_passers")
        if table is None:
            raise ValueError("Could not find nonqb_passers table in the HTML.")

        entries = self._parse_table(table)

        return {
            "title": title,
            "entries": entries,
        }
