"""Tests verifying docstrings and type annotations for the pfr/models module (TGF-169)."""

import importlib
import inspect
import pkgutil

import pytest

import griddy.pfr.models as models_pkg
import griddy.pfr.models.entities as entities_pkg


def _collect_classes_from_package(package):
    """Walk a package and return all Pydantic model / BaseModel classes."""
    classes = []
    pkg_path = package.__path__
    pkg_prefix = package.__name__ + "."

    for _importer, mod_name, _is_pkg in pkgutil.walk_packages(pkg_path, pkg_prefix):
        try:
            mod = importlib.import_module(mod_name)
        except Exception:
            continue
        for name, obj in inspect.getmembers(mod, inspect.isclass):
            if obj.__module__ == mod.__name__ and not name.startswith("_"):
                classes.append((obj, f"{mod.__name__}.{name}"))
    return classes


_ENTITY_CLASSES = _collect_classes_from_package(entities_pkg)


@pytest.mark.unit
class TestPFREntityDocstrings:
    @pytest.mark.parametrize(
        "cls,name",
        [
            pytest.param(cls, name, id=name.split(".")[-1])
            for cls, name in _ENTITY_CLASSES
        ],
    )
    def test_has_docstring(self, cls, name):
        assert cls.__doc__ is not None, f"{name} is missing a docstring"
        assert len(cls.__doc__.strip()) > 0, f"{name} has an empty docstring"


@pytest.mark.unit
class TestPFRModelsInitDocstringsAndTypes:
    def test_getattr_has_docstring(self):
        fn = models_pkg.__getattr__
        assert fn.__doc__ is not None, "__getattr__ is missing a docstring"
        assert len(fn.__doc__.strip()) > 0, "__getattr__ has an empty docstring"

    def test_dir_has_docstring(self):
        fn = models_pkg.__dir__
        assert fn.__doc__ is not None, "__dir__ is missing a docstring"
        assert len(fn.__doc__.strip()) > 0, "__dir__ has an empty docstring"

    def test_dir_has_return_type(self):
        hints = inspect.get_annotations(models_pkg.__dir__)
        assert "return" in hints, "__dir__ is missing a return type annotation"


@pytest.mark.unit
class TestPFREntityModuleDocstrings:
    @pytest.mark.parametrize(
        "mod_name",
        [
            pytest.param(mod_name, id=mod_name.rsplit(".", 1)[-1])
            for _importer, mod_name, _is_pkg in pkgutil.walk_packages(
                entities_pkg.__path__, entities_pkg.__name__ + "."
            )
        ],
    )
    def test_module_has_docstring(self, mod_name):
        mod = importlib.import_module(mod_name)
        assert mod.__doc__ is not None, f"{mod_name} is missing a module docstring"
        assert len(mod.__doc__.strip()) > 0, f"{mod_name} has an empty module docstring"
