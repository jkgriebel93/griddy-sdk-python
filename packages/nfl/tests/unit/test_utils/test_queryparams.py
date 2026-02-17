"""Tests for griddy.nfl.utils.queryparams."""

from typing import Dict, List, Optional

import pytest
from pydantic import Field
from typing_extensions import Annotated

from griddy_nfl.types.basemodel import BaseModel
from griddy_nfl.utils.metadata import FieldMetadata, QueryParamMetadata
from griddy_nfl.utils.queryparams import get_query_params


class SimpleQueryParams(BaseModel):
    season: Annotated[
        Optional[int],
        Field(alias="season"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    week: Annotated[
        Optional[int],
        Field(alias="week"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None


class ListQueryParams(BaseModel):
    tags: Annotated[
        Optional[List[str]],
        Field(alias="tags"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None


class NonExplodeListParams(BaseModel):
    tags: Annotated[
        Optional[List[str]],
        Field(alias="tags"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=False)),
    ] = None


class PipeDelimitedParams(BaseModel):
    ids: Annotated[
        Optional[List[str]],
        Field(alias="ids"),
        FieldMetadata(query=QueryParamMetadata(style="pipeDelimited", explode=False)),
    ] = None


class DeepObjectParams(BaseModel):
    filter_obj: Annotated[
        Optional[Dict[str, str]],
        Field(alias="filter"),
        FieldMetadata(query=QueryParamMetadata(style="deepObject", explode=True)),
    ] = None


@pytest.mark.unit
class TestGetQueryParams:
    def test_scalar_form_explode(self):
        params = SimpleQueryParams(season=2024, week=1)
        result = get_query_params(params)
        assert result == {"season": ["2024"], "week": ["1"]}

    def test_none_values_skipped(self):
        params = SimpleQueryParams(season=2024)
        result = get_query_params(params)
        assert "season" in result
        assert "week" not in result

    def test_list_form_explode(self):
        params = ListQueryParams(tags=["a", "b", "c"])
        result = get_query_params(params)
        assert result == {"tags": ["a", "b", "c"]}

    def test_list_form_non_explode(self):
        params = NonExplodeListParams(tags=["a", "b", "c"])
        result = get_query_params(params)
        assert "tags" in result
        assert result["tags"] == ["a,b,c"]

    def test_pipe_delimited(self):
        params = PipeDelimitedParams(ids=["1", "2", "3"])
        result = get_query_params(params)
        assert "ids" in result
        assert result["ids"] == ["1|2|3"]

    def test_deep_object(self):
        params = DeepObjectParams(filter_obj={"name": "test", "type": "game"})
        result = get_query_params(params)
        assert "filter[name]" in result
        assert result["filter[name]"] == ["test"]
        assert "filter[type]" in result
        assert result["filter[type]"] == ["game"]

    def test_non_model_returns_empty(self):
        result = get_query_params("not a model")
        assert result == {}

    def test_empty_model(self):
        params = SimpleQueryParams()
        result = get_query_params(params)
        assert result == {}
