"""HTML table parsers for Pro Football Reference pages.

Each parser function takes raw HTML and returns structured data extracted
from PFR's ``<table>`` elements using BeautifulSoup.
"""

from typing import Any, Dict, List, Optional

from bs4 import BeautifulSoup, Tag

# Columns in the PFR schedule table where the cell value should be cast to int.
_INT_COLUMNS = {"pts_win", "pts_lose", "yards_win", "to_win", "yards_lose", "to_lose"}

# Columns where we also want to extract the ``href`` from a child ``<a>`` tag.
_LINK_COLUMNS = {"winner", "loser", "boxscore_word"}


def _safe_int(value: str) -> Optional[int]:
    """Convert a string to int, returning None for empty/non-numeric values."""
    try:
        return int(value)
    except (ValueError, TypeError):
        return None


def _extract_cell(cell: Tag, stat: str) -> Dict[str, Any]:
    """Extract text and optional href from a single ``<td>`` or ``<th>``.

    Returns a dict with at least ``{stat: text_value}``.  For columns in
    ``_LINK_COLUMNS``, an additional ``{stat}_href`` key is added when a
    link is present.  For columns in ``_INT_COLUMNS`` the value is cast
    to ``int | None``.
    """
    text = cell.get_text(strip=True)
    result: Dict[str, Any] = {}

    if stat in _INT_COLUMNS:
        result[stat] = _safe_int(text)
    else:
        result[stat] = text

    if stat in _LINK_COLUMNS:
        link = cell.find("a")
        result[f"{stat}_href"] = link["href"] if link and link.get("href") else None

    return result


def parse_schedule_table(html: str) -> List[Dict[str, Any]]:
    """Parse the PFR season-schedule table into a list of game dicts.

    Looks for ``<table id="games">``, iterates over ``<tbody> <tr>`` rows,
    and skips:

    * Separator rows (``class="thead"``)
    * Rows where *all* data cells are empty (e.g. the "Playoffs" label row)

    Each returned dict contains the 14 ``data-stat`` columns plus ``_href``
    keys for link cells.

    Args:
        html: Raw HTML string of a PFR ``/years/{season}/games.htm`` page.

    Returns:
        A list of dicts, one per game.

    Raises:
        ValueError: If ``<table id="games">`` is not found in the HTML.
    """
    soup = BeautifulSoup(html, "html.parser")
    table = soup.find("table", id="games")
    if table is None:
        raise ValueError("Could not find <table id='games'> in the HTML.")

    tbody = table.find("tbody")
    if tbody is None:
        raise ValueError("Could not find <tbody> inside the games table.")

    games: List[Dict[str, Any]] = []

    for row in tbody.find_all("tr"):
        # Skip separator header rows that repeat column names mid-table.
        if "thead" in (row.get("class") or []):
            continue

        game: Dict[str, Any] = {}
        cells = row.find_all(["th", "td"])

        all_empty = True
        for cell in cells:
            stat = cell.get("data-stat")
            if not stat:
                continue
            extracted = _extract_cell(cell, stat)
            game.update(extracted)
            # Check if this cell has meaningful text content.
            text = cell.get_text(strip=True)
            if text and text != "Playoffs":
                all_empty = False

        # Skip label-only rows (e.g. the "Playoffs" divider).
        if all_empty:
            continue

        games.append(game)

    return games
