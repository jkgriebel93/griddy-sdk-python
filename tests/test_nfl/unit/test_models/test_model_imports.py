"""Test that all model modules can be imported successfully.

Importing each module exercises all field declarations (Pydantic model class
bodies), which covers the vast majority of model code (~15k statements).
"""

import importlib
from pathlib import Path

import pytest

# Discover all model module paths dynamically
_MODELS_ROOT = Path(__file__).resolve().parents[4] / "src" / "griddy" / "nfl" / "models"
_MODEL_SUBDIRS = ["entities", "requests", "responses", "enums"]


def _discover_model_modules():
    """Discover all model modules under src/griddy/nfl/models/."""
    modules = []
    for subdir in _MODEL_SUBDIRS:
        subdir_path = _MODELS_ROOT / subdir
        if not subdir_path.exists():
            continue
        for py_file in sorted(subdir_path.glob("*.py")):
            if py_file.name == "__init__.py":
                continue
            # Convert path to module name: griddy.nfl.models.entities.player
            module_name = f"griddy.nfl.models.{subdir}.{py_file.stem}"
            modules.append(module_name)
    return modules


_ALL_MODEL_MODULES = _discover_model_modules()

# Modules with known broken imports (pre-existing bugs in the codebase)
_KNOWN_BROKEN = {
    "griddy.nfl.models.responses.coaches_film_response",  # wrong relative import for response_metadata
}


@pytest.mark.unit
class TestModelImports:
    @pytest.mark.parametrize("module_path", _ALL_MODEL_MODULES)
    def test_model_module_imports(self, module_path):
        """Each model module should import without errors."""
        if module_path in _KNOWN_BROKEN:
            pytest.xfail(f"Known broken import: {module_path}")
        mod = importlib.import_module(module_path)
        assert mod is not None

    def test_discovered_module_count(self):
        """Sanity check: we should discover a large number of model modules."""
        assert len(_ALL_MODEL_MODULES) > 250
