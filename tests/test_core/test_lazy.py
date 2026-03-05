import pytest

from griddy.core._lazy import dynamic_dir, dynamic_getattr

SAMPLE_IMPORTS = {
    "Foo": ".foo_module",
    "Bar": ".bar_module",
}


class TestDynamicGetattr:
    def test_resolves_known_attr(self):
        result = dynamic_getattr(
            "SDKError",
            {"SDKError": ".sdkerror"},
            "griddy.core.errors",
            "griddy.core.errors",
        )
        from griddy.core.errors.sdkerror import SDKError

        assert result is SDKError

    def test_raises_attribute_error_for_unknown_attr(self):
        with pytest.raises(
            AttributeError, match="No Unknown found in _dynamic_imports"
        ):
            dynamic_getattr("Unknown", SAMPLE_IMPORTS, "some.package", "some.module")

    def test_raises_import_error_for_bad_module(self):
        bad_imports = {"Bad": ".nonexistent_module_xyz"}
        with pytest.raises((ImportError, KeyError)):
            dynamic_getattr("Bad", bad_imports, "griddy.core", "griddy.core")

    def test_raises_attribute_error_for_missing_attr_in_module(self):
        wrong_imports = {"NonExistent": ".sdkerror"}
        with pytest.raises(AttributeError, match="Failed to get"):
            dynamic_getattr(
                "NonExistent",
                wrong_imports,
                "griddy.core.errors",
                "griddy.core.errors",
            )


class TestDynamicDir:
    def test_returns_sorted_keys(self):
        result = dynamic_dir(SAMPLE_IMPORTS)
        assert result == ["Bar", "Foo"]

    def test_empty_imports(self):
        assert dynamic_dir({}) == []
