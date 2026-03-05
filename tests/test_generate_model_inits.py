"""Tests for the scripts/generate_model_inits.py code generation script."""

import textwrap
from pathlib import Path

import pytest
from scripts.generate_model_inits import (
    build_all_list,
    build_dynamic_imports,
    build_type_checking_imports,
    discover_symbols,
    generate_init,
    scan_package,
)


@pytest.fixture
def tmp_models_dir(tmp_path):
    """Create a temporary models directory with sample files."""
    entities_dir = tmp_path / "entities"
    entities_dir.mkdir()
    (entities_dir / "__init__.py").write_text("")

    enums_dir = tmp_path / "enums"
    enums_dir.mkdir()
    (enums_dir / "__init__.py").write_text("")

    return tmp_path


class TestDiscoverSymbols:
    def test_discovers_classes(self, tmp_path):
        f = tmp_path / "models.py"
        f.write_text(textwrap.dedent("""\
            from pydantic import BaseModel

            class Foo(BaseModel):
                x: int

            class Bar(BaseModel):
                y: str
            """))
        assert discover_symbols(f) == ["Foo", "Bar"]

    def test_discovers_type_aliases(self, tmp_path):
        f = tmp_path / "enums.py"
        f.write_text(textwrap.dedent("""\
            from typing import Literal

            SeasonType = Literal["PRE", "REG", "POST"]
            """))
        assert discover_symbols(f) == ["SeasonType"]

    def test_discovers_mixed(self, tmp_path):
        f = tmp_path / "mixed.py"
        f.write_text(textwrap.dedent("""\
            from typing import Literal
            from pydantic import BaseModel

            GameStatus = Literal["SCHEDULED", "FINAL"]

            class Game(BaseModel):
                status: GameStatus
            """))
        assert discover_symbols(f) == ["GameStatus", "Game"]

    def test_skips_private_names(self, tmp_path):
        f = tmp_path / "private.py"
        f.write_text(textwrap.dedent("""\
            _INTERNAL = "hidden"

            class _PrivateClass:
                pass

            class PublicClass:
                pass
            """))
        assert discover_symbols(f) == ["PublicClass"]

    def test_empty_file(self, tmp_path):
        f = tmp_path / "empty.py"
        f.write_text("")
        assert discover_symbols(f) == []


class TestScanPackage:
    def test_scans_subdirectories(self, tmp_models_dir):
        (tmp_models_dir / "entities" / "game.py").write_text(textwrap.dedent("""\
            class Game:
                pass

            class GameExtension:
                pass
            """))
        (tmp_models_dir / "enums" / "season_type.py").write_text(textwrap.dedent("""\
            from typing import Literal
            SeasonType = Literal["PRE", "REG"]
            """))
        result = scan_package(tmp_models_dir, ["entities", "enums"])
        assert result == {
            "Game": ".entities.game",
            "GameExtension": ".entities.game",
            "SeasonType": ".enums.season_type",
        }

    def test_skips_init_files(self, tmp_models_dir):
        (tmp_models_dir / "entities" / "__init__.py").write_text(
            "class ShouldBeSkipped: pass"
        )
        (tmp_models_dir / "entities" / "real.py").write_text("class RealModel: pass")
        result = scan_package(tmp_models_dir, ["entities"])
        assert "ShouldBeSkipped" not in result
        assert result == {"RealModel": ".entities.real"}

    def test_scans_extra_files(self, tmp_models_dir):
        (tmp_models_dir / "base.py").write_text("class BaseModel: pass")
        result = scan_package(tmp_models_dir, ["entities"], extra_files=["base.py"])
        assert result == {"BaseModel": ".base"}

    def test_missing_subdir_is_skipped(self, tmp_models_dir):
        result = scan_package(tmp_models_dir, ["nonexistent"])
        assert result == {}


class TestBuildTypeCheckingImports:
    def test_single_import(self):
        symbol_map = {"Game": ".entities.game"}
        result = build_type_checking_imports(symbol_map, "griddy.nfl.models")
        expected = textwrap.dedent("""\
        if TYPE_CHECKING:
            from griddy.nfl.models.entities.game import Game""")
        assert result == expected

    def test_multiple_imports_from_same_module(self):
        symbol_map = {
            "Game": ".entities.game",
            "GameExtension": ".entities.game",
        }
        result = build_type_checking_imports(symbol_map, "griddy.nfl.models")
        expected = textwrap.dedent("""\
        if TYPE_CHECKING:
            from griddy.nfl.models.entities.game import (
                Game,
                GameExtension,
            )""")
        assert result == expected

    def test_sorted_modules_and_symbols(self):
        symbol_map = {
            "Zebra": ".entities.zoo",
            "Alpha": ".entities.alpha",
            "Beta": ".entities.alpha",
        }
        result = build_type_checking_imports(symbol_map, "pkg.models")
        assert result == textwrap.dedent("""\
        if TYPE_CHECKING:
            from pkg.models.entities.alpha import (
                Alpha,
                Beta,
            )
            from pkg.models.entities.zoo import Zebra""")

    def test_long_single_import_wraps(self):
        symbol_map = {
            "VeryLongClassName": ".entities.very_long_module_name_that_exceeds_line_limit",
        }
        result = build_type_checking_imports(symbol_map, "griddy.nfl.models")
        assert "import (\n" in result
        assert "        VeryLongClassName,\n" in result
        assert "    )" in result


class TestBuildAllList:
    def test_sorted_output(self):
        symbol_map = {"Zebra": ".z", "Alpha": ".a", "Mid": ".m"}
        result = build_all_list(symbol_map)
        assert result == textwrap.dedent("""\
        __all__ = [
            "Alpha",
            "Mid",
            "Zebra",
        ]""")


class TestBuildDynamicImports:
    def test_sorted_output(self):
        symbol_map = {"Zebra": ".entities.zoo", "Alpha": ".entities.alpha"}
        result = build_dynamic_imports(symbol_map)
        assert result == textwrap.dedent("""\
        _dynamic_imports: dict[str, str] = {
            "Alpha": ".entities.alpha",
            "Zebra": ".entities.zoo",
        }""")


class TestGenerateInit:
    def test_full_generation(self, tmp_models_dir):
        (tmp_models_dir / "entities" / "game.py").write_text(textwrap.dedent("""\
            class Game:
                pass
            """))
        result = generate_init(tmp_models_dir, "griddy.nfl.models", ["entities"])
        assert "# This file is auto-generated" in result
        assert "import builtins" in result
        assert "from typing import TYPE_CHECKING" in result
        assert "from griddy.core._import import dynamic_import" in result
        assert "from griddy.nfl.models.entities.game import Game" in result
        assert '"Game"' in result
        assert '".entities.game"' in result
        assert "def __getattr__" in result
        assert "def __dir__" in result
        assert "# isort: skip_file" in result


class TestCheckMode:
    def test_check_passes_when_up_to_date(self, tmp_models_dir):
        (tmp_models_dir / "entities" / "game.py").write_text("class Game: pass")
        content = generate_init(tmp_models_dir, "griddy.nfl.models", ["entities"])
        init_path = tmp_models_dir / "__init__.py"
        init_path.write_text(content)
        assert init_path.read_text() == content

    def test_check_detects_mismatch(self, tmp_models_dir):
        (tmp_models_dir / "entities" / "game.py").write_text("class Game: pass")
        content = generate_init(tmp_models_dir, "griddy.nfl.models", ["entities"])
        init_path = tmp_models_dir / "__init__.py"
        init_path.write_text("# outdated content")
        assert init_path.read_text() != content


class TestActualModelPackages:
    """Verify that the generated __init__.py files for the actual
    NFL and PFR model packages are up to date."""

    def test_nfl_models_init_up_to_date(self):
        models_dir = (
            Path(__file__).resolve().parent.parent / "src" / "griddy" / "nfl" / "models"
        )
        generated = generate_init(
            models_dir,
            "griddy.nfl.models",
            ["entities", "enums", "requests", "responses"],
        )
        current = (models_dir / "__init__.py").read_text()
        assert current == generated, (
            "NFL models __init__.py is out of date. "
            "Run 'python scripts/generate_model_inits.py' to regenerate."
        )

    def test_pfr_models_init_up_to_date(self):
        models_dir = (
            Path(__file__).resolve().parent.parent / "src" / "griddy" / "pfr" / "models"
        )
        generated = generate_init(
            models_dir,
            "griddy.pfr.models",
            ["entities"],
            extra_files=["base.py"],
        )
        current = (models_dir / "__init__.py").read_text()
        assert current == generated, (
            "PFR models __init__.py is out of date. "
            "Run 'python scripts/generate_model_inits.py' to regenerate."
        )
