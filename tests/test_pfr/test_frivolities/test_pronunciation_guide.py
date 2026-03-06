"""Tests for Pronunciation Guide endpoint."""

import pytest

from griddy.pfr.errors import ParsingError
from griddy.pfr.models import PronunciationEntry, PronunciationGuide
from griddy.pfr.sdk import GriddyPFR

from .conftest import FIXTURE_DIR, assert_endpoint_via_mock, assert_smoke
from .conftest import pronunciation_guide_parser as _parser

# -------------------------------------------------------------------------
# Fixtures
# -------------------------------------------------------------------------


@pytest.fixture(scope="module")
def pronunciation_guide_html() -> str:
    return (FIXTURE_DIR / "pronunciation_guide.html").read_text()


@pytest.fixture(scope="module")
def pronunciation_guide_parsed(pronunciation_guide_html: str) -> dict:
    return _parser.parse(pronunciation_guide_html)


@pytest.fixture(scope="module")
def pronunciation_guide_model(
    pronunciation_guide_parsed: dict,
) -> PronunciationGuide:
    return PronunciationGuide.model_validate(pronunciation_guide_parsed)


# =========================================================================
# Smoke tests
# =========================================================================


@pytest.mark.unit
class TestPronunciationGuideSmoke:
    def test_parse_returns_dict(self, pronunciation_guide_parsed):
        assert isinstance(pronunciation_guide_parsed, dict)

    def test_has_required_keys(self, pronunciation_guide_parsed):
        assert_smoke(pronunciation_guide_parsed, ["title", "entries"])

    def test_model_validates(self, pronunciation_guide_model):
        assert isinstance(pronunciation_guide_model, PronunciationGuide)


# =========================================================================
# Metadata
# =========================================================================


@pytest.mark.unit
class TestPronunciationGuideMetadata:
    def test_title(self, pronunciation_guide_model):
        assert (
            pronunciation_guide_model.title
            == "Current and Former Player Name Pronunciation Guide"
        )


# =========================================================================
# Entries
# =========================================================================


@pytest.mark.unit
class TestPronunciationGuideEntries:
    def test_entry_count(self, pronunciation_guide_model):
        assert len(pronunciation_guide_model.entries) == 2093

    def test_all_entries_are_pronunciation_entry(self, pronunciation_guide_model):
        for entry in pronunciation_guide_model.entries:
            assert isinstance(entry, PronunciationEntry)

    def test_first_entry(self, pronunciation_guide_model):
        first = pronunciation_guide_model.entries[0]
        assert first.player == "Isaako Aaitui"
        assert first.player_href == "/players/A/AaitIs00.htm"
        assert first.player_id == "AaitIs00"
        assert first.pronunciation == "e-saw-AH-co ah-ah-TWO-e"

    def test_last_entry(self, pronunciation_guide_model):
        last = pronunciation_guide_model.entries[-1]
        assert last.player == "Shane Zylstra"
        assert last.player_id == "ZylsSh00"
        assert last.pronunciation == "ZILL-struh"

    def test_parenthetical_pronunciation(self, pronunciation_guide_model):
        """David Blough uses parenthetical clarification."""
        blough = next(
            e for e in pronunciation_guide_model.entries if e.player == "David Blough"
        )
        assert 'BLAU (like "cow")' in blough.pronunciation

    def test_apostrophe_in_name(self, pronunciation_guide_model):
        """De'Von Achane has an apostrophe in first name."""
        achane = next(
            e for e in pronunciation_guide_model.entries if e.player == "De'Von Achane"
        )
        assert achane.player_id == "AchaDe00"
        assert achane.pronunciation == "duh-VAHN AY-chan"

    def test_name_with_suffix(self, pronunciation_guide_model):
        """Dorance Armstrong Jr. has a name suffix."""
        armstrong = next(
            e
            for e in pronunciation_guide_model.entries
            if e.player == "Dorance Armstrong Jr."
        )
        assert armstrong.pronunciation == "DOOR-intz"

    def test_tua_tagovailoa(self, pronunciation_guide_model):
        """Tua Tagovailoa is a well-known pronunciation example."""
        tua = next(
            e for e in pronunciation_guide_model.entries if e.player == "Tua Tagovailoa"
        )
        assert tua.player_id == "TagoTu00"
        assert tua.pronunciation == "TWO-uh TUNG-oh-vai-LO-uh"

    def test_all_entries_have_pronunciation(self, pronunciation_guide_model):
        for entry in pronunciation_guide_model.entries:
            assert entry.pronunciation, f"{entry.player} has empty pronunciation"

    def test_all_entries_have_player_href(self, pronunciation_guide_model):
        for entry in pronunciation_guide_model.entries:
            assert entry.player_href is not None
            assert entry.player_href.startswith("/players/")


# =========================================================================
# Parser error handling
# =========================================================================


@pytest.mark.unit
class TestPronunciationGuideParserErrors:
    def test_raises_on_missing_content_div(self):
        with pytest.raises(ParsingError, match="Could not find #content div"):
            _parser.parse("<html><body>No content</body></html>")

    def test_raises_on_missing_list(self):
        with pytest.raises(ParsingError, match="Could not find pronunciation list"):
            _parser.parse(
                '<html><body><div id="content"><h1>Title</h1></div></body></html>'
            )


# =========================================================================
# Endpoint config
# =========================================================================


@pytest.mark.unit
class TestPronunciationGuideEndpointConfig:
    def test_config(self):
        pfr = GriddyPFR()
        config = pfr.frivolities._get_pronunciation_guide_config()
        assert config.operation_id == "getPronunciationGuide"
        assert config.path_template == "/friv/pronunciation-guide.htm"
        assert config.wait_for_element == "#content ul"

    def test_endpoint_via_mock(self, pronunciation_guide_html):
        result = assert_endpoint_via_mock(
            pronunciation_guide_html,
            "get_pronunciation_guide",
            PronunciationGuide,
        )
        assert result.title == "Current and Former Player Name Pronunciation Guide"
        assert len(result.entries) == 2093
        assert result.entries[0].player == "Isaako Aaitui"
