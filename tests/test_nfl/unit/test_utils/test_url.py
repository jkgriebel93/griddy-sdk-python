"""Tests for griddy.nfl.utils.url."""

from typing import Optional, Union

import pytest
from pydantic import Field
from typing_extensions import Annotated

from griddy.nfl.types.basemodel import BaseModel
from griddy.nfl.utils.metadata import FieldMetadata, PathParamMetadata
from griddy.nfl.utils.url import (
    generate_url,
    is_optional,
    remove_suffix,
    template_url,
)


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
    def test_suffix_present(self):
        assert remove_suffix("hello_world", "_world") == "hello"

    def test_suffix_not_present(self):
        assert remove_suffix("hello", "_world") == "hello"

    def test_empty_suffix(self):
        assert remove_suffix("hello", "") == "hello"

    def test_empty_string(self):
        assert remove_suffix("", "suffix") == ""


@pytest.mark.unit
class TestIsOptional:
    def test_optional_type(self):
        assert is_optional(Optional[str]) is True

    def test_non_optional_type(self):
        assert is_optional(str) is False

    def test_union_with_none(self):
        assert is_optional(Union[str, None]) is True

    def test_union_without_none(self):
        assert is_optional(Union[str, int]) is False


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
