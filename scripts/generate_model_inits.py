#!/usr/bin/env python3
"""Auto-generate __init__.py files for model packages.

Scans model subdirectories (entities, enums, requests, responses) using AST
to discover all public symbols (classes and type aliases), then generates
__init__.py files with:
  - TYPE_CHECKING imports for IDE support
  - __all__ list
  - _dynamic_imports dict for lazy loading
  - __getattr__ and __dir__ functions

Usage:
    python scripts/generate_model_inits.py [--check]

Options:
    --check   Verify that generated files match current files (for CI).
              Exits with code 1 if files would change.
"""

import ast
import sys
import textwrap
from collections import defaultdict
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
MODELS_DIR_NFL = PROJECT_ROOT / "src" / "griddy" / "nfl" / "models"
MODELS_DIR_PFR = PROJECT_ROOT / "src" / "griddy" / "pfr" / "models"


def discover_symbols(file_path: Path) -> list[str]:
    """Parse a Python file and return all public symbol names."""
    source = file_path.read_text()
    tree = ast.parse(source, filename=str(file_path))
    symbols = []
    for node in ast.iter_child_nodes(tree):
        if isinstance(node, ast.ClassDef) and not node.name.startswith("_"):
            symbols.append(node.name)
        elif isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and not target.id.startswith("_"):
                    symbols.append(target.id)
    return symbols


def scan_package(
    models_dir: Path,
    subdirs: list[str],
    extra_files: list[str] | None = None,
) -> dict[str, str]:
    """Scan subdirectories for model files and build symbol-to-module mapping.

    Returns a dict mapping symbol names to relative module paths
    (e.g., "Game" -> ".entities.game").
    """
    symbol_map: dict[str, str] = {}
    for subdir in subdirs:
        subdir_path = models_dir / subdir
        if not subdir_path.is_dir():
            continue
        for file_path in sorted(subdir_path.glob("*.py")):
            if file_path.name == "__init__.py":
                continue
            module_stem = file_path.stem
            relative_module = f".{subdir}.{module_stem}"
            for symbol in discover_symbols(file_path):
                symbol_map[symbol] = relative_module

    if extra_files:
        for extra in extra_files:
            file_path = models_dir / extra
            if file_path.exists():
                module_stem = file_path.stem
                relative_module = f".{module_stem}"
                for symbol in discover_symbols(file_path):
                    symbol_map[symbol] = relative_module

    return symbol_map


LINE_LENGTH = 88


def _isort_key(name: str) -> str:
    """Match isort's default sorting: lowercase, with leading underscores last."""
    return name.lower()


def build_type_checking_imports(symbol_map: dict[str, str], package_base: str) -> str:
    """Build the TYPE_CHECKING import block matching isort's formatting."""
    module_to_symbols: dict[str, list[str]] = defaultdict(list)
    for symbol, rel_module in symbol_map.items():
        abs_module = f"{package_base}{rel_module}"
        module_to_symbols[abs_module].append(symbol)

    lines = []
    lines.append("if TYPE_CHECKING:")
    for module in sorted(module_to_symbols):
        symbols = sorted(module_to_symbols[module], key=_isort_key)
        if len(symbols) == 1:
            single_line = f"    from {module} import {symbols[0]}"
            if len(single_line) <= LINE_LENGTH:
                lines.append(single_line)
            else:
                lines.append(f"    from {module} import (")
                lines.append(f"        {symbols[0]},")
                lines.append("    )")
        else:
            lines.append(f"    from {module} import (")
            for sym in symbols:
                lines.append(f"        {sym},")
            lines.append("    )")
    return "\n".join(lines)


def build_all_list(symbol_map: dict[str, str]) -> str:
    """Build the __all__ list."""
    symbols = sorted(symbol_map.keys())
    lines = ["__all__ = ["]
    for sym in symbols:
        lines.append(f'    "{sym}",')
    lines.append("]")
    return "\n".join(lines)


def build_dynamic_imports(symbol_map: dict[str, str]) -> str:
    """Build the _dynamic_imports dict."""
    lines = ["_dynamic_imports: dict[str, str] = {"]
    for sym in sorted(symbol_map.keys()):
        lines.append(f'    "{sym}": "{symbol_map[sym]}",')
    lines.append("}")
    return "\n".join(lines)


GETATTR_AND_DIR = textwrap.dedent("""\

    def __getattr__(attr_name: str) -> object:
        module_name = _dynamic_imports.get(attr_name)
        if module_name is None:
            raise AttributeError(
                f"No {attr_name} found in _dynamic_imports for module name -> {__name__} "
            )

        try:
            module = dynamic_import(module_name, __package__)
            result = getattr(module, attr_name)
            return result
        except ImportError as e:
            raise ImportError(
                f"Failed to import {attr_name} from {module_name}: {e}"
            ) from e
        except AttributeError as e:
            raise AttributeError(
                f"Failed to get {attr_name} from {module_name}: {e}"
            ) from e


    def __dir__():
        lazy_attrs = builtins.list(_dynamic_imports.keys())
        return builtins.sorted(lazy_attrs)
""").lstrip("\n")


def generate_init(
    models_dir: Path,
    package_base: str,
    subdirs: list[str],
    extra_files: list[str] | None = None,
) -> str:
    """Generate the full __init__.py content for a models package."""
    symbol_map = scan_package(models_dir, subdirs, extra_files)

    parts = [
        "# This file is auto-generated by scripts/generate_model_inits.py.",
        "# Do not edit manually.",
        "# isort: skip_file",
        "",
        "import builtins",
        "from typing import TYPE_CHECKING",
        "",
        "from griddy.core._import import dynamic_import",
        "",
        build_type_checking_imports(symbol_map, package_base),
        "",
        build_all_list(symbol_map),
        "",
        build_dynamic_imports(symbol_map),
        "",
        "",
        GETATTR_AND_DIR,
    ]
    return "\n".join(parts)


def main() -> int:
    check_mode = "--check" in sys.argv

    configs = [
        {
            "models_dir": MODELS_DIR_NFL,
            "package_base": "griddy.nfl.models",
            "subdirs": ["entities", "enums", "requests", "responses"],
        },
        {
            "models_dir": MODELS_DIR_PFR,
            "package_base": "griddy.pfr.models",
            "subdirs": ["entities"],
            "extra_files": ["base.py"],
        },
    ]

    any_changed = False
    for config in configs:
        models_dir = config["models_dir"]
        init_path = models_dir / "__init__.py"
        generated = generate_init(
            models_dir=models_dir,
            package_base=config["package_base"],
            subdirs=config["subdirs"],
            extra_files=config.get("extra_files"),
        )

        if check_mode:
            if init_path.exists():
                current = init_path.read_text()
            else:
                current = ""
            if current != generated:
                print(f"MISMATCH: {init_path} is out of date.")
                print("Run 'python scripts/generate_model_inits.py' to regenerate.")
                any_changed = True
            else:
                print(f"OK: {init_path}")
        else:
            init_path.write_text(generated)
            print(f"Generated: {init_path}")

    if check_mode and any_changed:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
