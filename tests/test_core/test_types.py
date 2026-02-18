"""Tests for griddy.core.types and griddy.core.utils.logger modules."""

from unittest.mock import patch

import pytest

from griddy.core.types import UNSET, BaseModel, Nullable, OptionalNullable
from griddy.core.types.basemodel import UNSET_SENTINEL, Unset


@pytest.mark.unit
class TestUnset:
    def test_unset_is_falsy(self):
        assert not UNSET

    def test_unset_bool_is_false(self):
        assert bool(UNSET) is False

    def test_unset_is_singleton(self):
        assert UNSET is UNSET

    def test_unset_is_instance_of_unset_class(self):
        assert isinstance(UNSET, Unset)

    def test_unset_serializes_to_sentinel(self):
        result = UNSET.model_dump()
        assert result == UNSET_SENTINEL


@pytest.mark.unit
class TestBaseModel:
    def test_populate_by_name(self):
        class MyModel(BaseModel):
            my_field: str

        m = MyModel(my_field="test")
        assert m.my_field == "test"

    def test_arbitrary_types_allowed(self):
        class Custom:
            pass

        class MyModel(BaseModel):
            custom: Custom

        c = Custom()
        m = MyModel(custom=c)
        assert m.custom is c

    def test_protected_namespaces_disabled(self):
        # Should not raise on model_ prefix
        class MyModel(BaseModel):
            model_type: str = "test"

        m = MyModel()
        assert m.model_type == "test"


@pytest.mark.unit
class TestGetDefaultLogger:
    def test_returns_noop_logger_by_default(self):
        from griddy.core.utils.logger import NoOpLogger, get_default_logger

        logger = get_default_logger()
        assert isinstance(logger, NoOpLogger)

    def test_returns_real_logger_when_env_set(self):
        import logging

        from griddy.core.utils.logger import get_default_logger

        with patch.dict("os.environ", {"GRIDDY_TEST_DEBUG": "1"}):
            logger = get_default_logger(env_var="GRIDDY_TEST_DEBUG")
            assert isinstance(logger, logging.Logger)

    def test_noop_logger_debug_does_nothing(self):
        from griddy.core.utils.logger import NoOpLogger

        logger = NoOpLogger()
        # Should not raise
        logger.debug("test message %s", "arg")
