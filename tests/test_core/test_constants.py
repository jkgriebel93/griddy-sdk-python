"""Verify that all error code constants are centralized in core/_constants.py.

Guards against two regressions:
1. Locally-defined error code constants in endpoint files (e.g., NGS_ERROR_CODES)
2. Inline error code lists that should use named constants
"""

import ast
import inspect
from pathlib import Path

import pytest

from griddy.core._constants import (
    COLLECTION_ERROR_CODES,
    NGS_ERROR_CODES,
    PARAMETERLESS_ERROR_CODES,
    RESOURCE_ERROR_CODES,
    SECURED_RESOURCE_ERROR_CODES,
    STATS_ERROR_CODES,
)

# ── constant value correctness ──────────────────────────────────────


class TestConstantValues:
    """Verify each constant has the expected error codes."""

    def test_collection_error_codes(self) -> None:
        assert COLLECTION_ERROR_CODES == ["400", "401", "4XX", "500", "5XX"]

    def test_resource_error_codes(self) -> None:
        assert RESOURCE_ERROR_CODES == ["400", "401", "404", "4XX", "500", "5XX"]

    def test_stats_error_codes(self) -> None:
        assert STATS_ERROR_CODES == ["400", "401", "403", "4XX", "500", "5XX"]

    def test_secured_resource_error_codes(self) -> None:
        assert SECURED_RESOURCE_ERROR_CODES == [
            "400",
            "401",
            "403",
            "404",
            "4XX",
            "500",
            "5XX",
        ]

    def test_ngs_error_codes(self) -> None:
        assert NGS_ERROR_CODES == [
            "400",
            "401",
            "403",
            "404",
            "4XX",
            "500",
            "5XX",
        ]

    def test_parameterless_error_codes(self) -> None:
        assert PARAMETERLESS_ERROR_CODES == ["401", "4XX", "500", "5XX"]


# ── no local error code constant definitions ────────────────────────

import griddy.core._constants as _constants_module

_CORE_DIR = Path(inspect.getfile(_constants_module)).parent
ENDPOINTS_DIR = _CORE_DIR.parent / "nfl" / "endpoints"


def _find_local_error_code_assignments(directory: Path) -> list[tuple[str, str, int]]:
    """Find any module-level assignments whose name ends with ERROR_CODES.

    Returns list of (file_path, variable_name, line_number) tuples.
    """
    violations: list[tuple[str, str, int]] = []
    for py_file in directory.rglob("*.py"):
        # Skip __init__.py and __pycache__
        if py_file.name.startswith("__"):
            continue
        try:
            tree = ast.parse(py_file.read_text())
        except SyntaxError:
            continue
        for node in ast.walk(tree):
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name) and target.id.endswith(
                        "ERROR_CODES"
                    ):
                        violations.append(
                            (
                                str(py_file.relative_to(directory)),
                                target.id,
                                node.lineno,
                            )
                        )
    return violations


class TestNoDuplicateErrorCodeDefinitions:
    """Ensure no endpoint files define their own error code constants."""

    def test_no_local_error_code_constants_in_endpoints(self) -> None:
        violations = _find_local_error_code_assignments(ENDPOINTS_DIR)
        if violations:
            msg_lines = [
                "Found locally-defined error code constants in endpoint files:"
            ]
            for filepath, varname, lineno in violations:
                msg_lines.append(f"  {filepath}:{lineno} - {varname}")
            msg_lines.append(
                "\nAll error code constants should be imported from griddy.core._constants"
            )
            pytest.fail("\n".join(msg_lines))


# ── NGS endpoints use centralized import ─────────────────────────────

NGS_DIR = ENDPOINTS_DIR / "ngs"


def _find_error_status_codes_usage(directory: Path) -> list[tuple[str, int, str]]:
    """Find error_status_codes= assignments in endpoint config methods.

    Returns list of (file_path, line_number, value_repr) for inline list literals.
    """
    violations: list[tuple[str, int, str]] = []
    for py_file in directory.rglob("*.py"):
        if py_file.name.startswith("__"):
            continue
        try:
            tree = ast.parse(py_file.read_text())
        except SyntaxError:
            continue
        for node in ast.walk(tree):
            if isinstance(node, ast.keyword) and node.arg == "error_status_codes":
                if isinstance(node.value, ast.List):
                    elts = [
                        elt.value
                        for elt in node.value.elts
                        if isinstance(elt, ast.Constant)
                    ]
                    violations.append(
                        (
                            str(py_file.relative_to(directory.parent.parent)),
                            node.value.lineno,
                            str(elts),
                        )
                    )
    return violations


class TestNoInlineErrorCodeLists:
    """Ensure endpoint files use named constants, not inline lists."""

    def test_ngs_endpoints_use_named_constants(self) -> None:
        violations = _find_error_status_codes_usage(NGS_DIR)
        if violations:
            msg_lines = ["Found inline error_status_codes lists in NGS endpoint files:"]
            for filepath, lineno, value in violations:
                msg_lines.append(f"  {filepath}:{lineno} - {value}")
            msg_lines.append(
                "\nUse NGS_ERROR_CODES from griddy.core._constants instead"
            )
            pytest.fail("\n".join(msg_lines))

    def test_pro_endpoints_use_named_constants(self) -> None:
        pro_dir = ENDPOINTS_DIR / "pro"
        violations = _find_error_status_codes_usage(pro_dir)
        if violations:
            msg_lines = ["Found inline error_status_codes lists in pro endpoint files:"]
            for filepath, lineno, value in violations:
                msg_lines.append(f"  {filepath}:{lineno} - {value}")
            msg_lines.append(
                "\nUse a named constant from griddy.core._constants instead"
            )
            pytest.fail("\n".join(msg_lines))

    def test_regular_endpoints_use_named_constants(self) -> None:
        regular_dir = ENDPOINTS_DIR / "regular"
        violations = _find_error_status_codes_usage(regular_dir)
        if violations:
            msg_lines = [
                "Found inline error_status_codes lists in regular endpoint files:"
            ]
            for filepath, lineno, value in violations:
                msg_lines.append(f"  {filepath}:{lineno} - {value}")
            msg_lines.append(
                "\nUse a named constant from griddy.core._constants instead"
            )
            pytest.fail("\n".join(msg_lines))
