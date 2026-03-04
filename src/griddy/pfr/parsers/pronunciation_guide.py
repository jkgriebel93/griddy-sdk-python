"""Parser for the PFR 'Pronunciation Guide' page.

Parses ``/friv/pronunciation-guide.htm`` which contains a ``<ul>`` list
of player names with their phonetic pronunciations.  Unlike most PFR
frivolity pages, this one does **not** use a ``<table>``; the data lives
in ``<li>`` elements inside the first ``<ul>`` within ``#content``.
"""

from typing import Any, Dict, List, Optional

from bs4 import BeautifulSoup, Tag

from griddy.pfr.errors import ParsingError


class PronunciationGuideParser:
    """Parses the PFR 'Pronunciation Guide' page."""

    @staticmethod
    def _extract_title(soup: BeautifulSoup) -> str:
        """Extract the page title from ``<h1>`` inside ``#content``."""
        content = soup.find("div", id="content")
        if content:
            h1 = content.find("h1")
            if h1:
                return h1.get_text(strip=True)
        title_tag = soup.find("title")
        if title_tag:
            return title_tag.get_text(strip=True)
        return ""

    @staticmethod
    def _extract_player_id(href: str) -> Optional[str]:
        """Extract the player ID from a PFR player href.

        ``/players/A/AaitIs00.htm`` → ``AaitIs00``
        """
        return href.rsplit("/", 1)[-1].replace(".htm", "") if href else None

    def _parse_list(self, ul: Tag) -> List[Dict[str, Any]]:
        """Parse the ``<ul>`` of pronunciation entries."""
        entries: List[Dict[str, Any]] = []

        for li in ul.find_all("li"):
            anchor = li.find("a")
            if anchor is None:
                continue

            href: Optional[str] = anchor.get("href") or None
            if href and not href.startswith("/players/"):
                continue

            player_name = anchor.get_text(strip=True)
            if not player_name:
                continue

            # Pronunciation text follows the <a> tag as a text node.
            pronunciation_node = anchor.next_sibling
            pronunciation = pronunciation_node.strip() if pronunciation_node else ""

            entries.append(
                {
                    "player": player_name,
                    "player_href": href,
                    "player_id": self._extract_player_id(href) if href else None,
                    "pronunciation": pronunciation,
                }
            )

        return entries

    def parse(self, html: str) -> Dict[str, Any]:
        """Parse the pronunciation guide page.

        Args:
            html: Raw HTML of the PFR pronunciation guide page.

        Returns:
            A dict ready for ``PronunciationGuide.model_validate()``.

        Raises:
            ParsingError: If the pronunciation list is not found.
        """
        soup = BeautifulSoup(html, "html.parser")

        title = self._extract_title(soup)

        content = soup.find("div", id="content")
        if content is None:
            raise ParsingError(
                "Could not find #content div in the HTML.",
                selector="content",
                html_sample=html[:500],
            )

        ul = content.find("ul")
        if ul is None:
            raise ParsingError(
                "Could not find pronunciation list in the HTML.",
                selector="content ul",
                html_sample=html[:500],
            )

        entries = self._parse_list(ul)

        return {
            "title": title,
            "entries": entries,
        }
