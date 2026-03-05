"""Tests for griddy.core.utils.forms."""

from typing import Annotated, List, Optional

import pytest
from pydantic import BaseModel, Field

from griddy.core.utils.forms import (
    _populate_form,
    serialize_form_data,
)
from griddy.core.utils.metadata import FieldMetadata, FormMetadata


class SimpleModel(BaseModel):
    name: Annotated[
        str,
        Field(alias="name"),
        FieldMetadata(form=FormMetadata(style="form", explode=True)),
    ]
    age: Annotated[
        int,
        Field(alias="age"),
        FieldMetadata(form=FormMetadata(style="form", explode=True)),
    ]


@pytest.mark.unit
class TestPopulateForm:
    def test_simple_value(self):
        form = {}
        result = _populate_form("key", True, "value", ",", form)
        assert result == {"key": ["value"]}

    def test_none_value_skipped(self):
        form = {}
        result = _populate_form("key", True, None, ",", form)
        assert result == {}

    def test_dict_explode(self):
        form = {}
        result = _populate_form("key", True, {"a": "1", "b": "2"}, ",", form)
        assert result == {"a": ["1"], "b": ["2"]}

    def test_dict_no_explode(self):
        form = {}
        result = _populate_form("key", False, {"a": "1", "b": "2"}, ",", form)
        assert result == {"key": ["a,1,b,2"]}

    def test_list_explode(self):
        form = {}
        result = _populate_form("key", True, ["a", "b", "c"], ",", form)
        assert result == {"key": ["a", "b", "c"]}

    def test_list_no_explode(self):
        form = {}
        result = _populate_form("key", False, ["a", "b", "c"], ",", form)
        assert result == {"key": ["a,b,c"]}

    def test_pydantic_model_explode(self):
        model = SimpleModel(name="test", age=25)
        form = {}
        result = _populate_form("data", True, model, ",", form)
        assert result == {"name": ["test"], "age": ["25"]}

    def test_pydantic_model_no_explode(self):
        model = SimpleModel(name="test", age=25)
        form = {}
        result = _populate_form("data", False, model, ",", form)
        assert result == {"data": ["name,test,age,25"]}


@pytest.mark.unit
class TestSerializeFormData:
    def test_pydantic_model(self):
        model = SimpleModel(name="test", age=25)
        result = serialize_form_data(model)
        assert result == {"name": ["test"], "age": ["25"]}

    def test_dict_input(self):
        result = serialize_form_data({"key": "value", "num": 42})
        assert result == {"key": ["value"], "num": ["42"]}

    def test_invalid_type_raises(self):
        with pytest.raises(TypeError, match="Invalid request body type"):
            serialize_form_data("not valid")
