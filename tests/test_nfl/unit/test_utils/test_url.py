"""Tests for griddy.nfl.utils.url."""

from typing import Optional, Union

import pytest
from pydantic import Field
from typing_extensions import Annotated

from griddy.nfl.types.basemodel import BaseModel
from griddy.nfl.utils.metadata import FieldMetadata, PathParamMetadata
from griddy.nfl.utils.url import generate_url, is_optional, remove_suffix, template_url


@pytest.mark.unit
class TestTemplateUrl:
    def test_single_substitution(self):
        result = template_url("https://api.nfl.com/{version}/games", {"version": "v3"})
        assert result == "https://api.nfl.com/v3/games"

    def test_multiple_substitutions(self):
        result = template_url(
            "https://api.nfl.com/{version}/{resource}",
            {"version": "v3", "resource": "games"},
        )
        assert result == "https://api.nfl.com/v3/games"

    def test_no_params(self):
        result = template_url("https://api.nfl.com/games", {})
        assert result == "https://api.nfl.com/games"


@pytest.mark.unit
class TestRemoveSuffix:
    @pytest.mark.parametrize(
        "string,suffix,expected",
        [
            pytest.param("hello_world", "_world", "hello", id="suffix_present"),
            pytest.param("hello", "_world", "hello", id="suffix_absent"),
            pytest.param("hello", "", "hello", id="empty_suffix"),
            pytest.param("", "suffix", "", id="empty_string"),
        ],
    )
    def test_remove_suffix(self, string, suffix, expected):
        assert remove_suffix(string, suffix) == expected


@pytest.mark.unit
class TestIsOptional:
    @pytest.mark.parametrize(
        "type_hint,expected",
        [
            pytest.param(Optional[str], True, id="Optional_str"),
            pytest.param(str, False, id="plain_str"),
            pytest.param(Union[str, None], True, id="Union_str_None"),
            pytest.param(Union[str, int], False, id="Union_str_int"),
        ],
    )
    def test_is_optional(self, type_hint, expected):
        assert is_optional(type_hint) is expected


@pytest.mark.unit
class TestGenerateUrl:
    def test_simple_path_params(self):
        class PathParams(BaseModel):
            game_id: Annotated[
                str,
                Field(alias="gameId"),
                FieldMetadata(path=PathParamMetadata()),
            ] = ""

        params = PathParams(game_id="12345")
        result = generate_url("https://api.nfl.com", "/games/{gameId}", params)
        assert result == "https://api.nfl.com/games/12345"

    def test_server_url_trailing_slash(self):
        class PathParams(BaseModel):
            pass

        result = generate_url("https://api.nfl.com/", "/games", PathParams())
        assert result == "https://api.nfl.com/games"

    def test_non_model_path_params(self):
        result = generate_url("https://api.nfl.com", "/games", "not_a_model")
        assert result == "https://api.nfl.com/games"
