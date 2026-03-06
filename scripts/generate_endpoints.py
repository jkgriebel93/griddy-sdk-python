#!/usr/bin/env python3
"""Generate endpoint and request model files from YAML specs.

Reads endpoint specification YAML files from the ``specs/`` directory and
generates:
  - Request model files (Pydantic BaseModel classes)
  - Endpoint implementation files (config methods with @sdk_endpoints)

Usage:
    python scripts/generate_endpoints.py                # Generate all
    python scripts/generate_endpoints.py --check        # Verify (for CI)
    python scripts/generate_endpoints.py --request-models-only  # Only request models
    python scripts/generate_endpoints.py --endpoints-only       # Only endpoint files
"""

import sys
import textwrap
from pathlib import Path

import yaml

PROJECT_ROOT = Path(__file__).resolve().parent.parent
SPECS_DIR = PROJECT_ROOT / "specs"

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

PRIMITIVE_TYPES = {"int", "str", "bool", "float"}

# Maps spec type names to Python typing imports needed
TYPING_IMPORTS_NEEDED = {
    "List[str]": "List",
    "List[int]": "List",
    "Optional": "Optional",
}


def _python_type(type_str: str, required: bool) -> str:
    """Convert a spec type string to a Python type annotation."""
    if not required:
        return f"Optional[{type_str}]"
    return type_str


def _needs_alias(param: dict) -> bool:
    """Check if a param needs a pydantic alias (camelCase conversion)."""
    return "alias" in param


def _default_repr(default: object) -> str:
    """Convert a default value to its Python repr."""
    if default is None:
        return "None"
    if isinstance(default, bool):
        return str(default)
    if isinstance(default, str):
        return repr(default)
    return str(default)


def _collect_typing_imports(params: list[dict]) -> set[str]:
    """Determine which typing imports are needed for a set of params."""
    imports = set()
    for p in params:
        if not p.get("required", False):
            imports.add("Optional")
        type_str = p["type"]
        if type_str.startswith("List["):
            imports.add("List")
    return imports


def _collect_enum_imports(params: list[dict]) -> list[str]:
    """Collect enum import statements needed by request model params."""
    seen = set()
    imports = []
    for p in params:
        enum_import = p.get("enum_import")
        if enum_import and enum_import not in seen:
            seen.add(enum_import)
            # e.g. "griddy.nfl.models.enums.season_type_enum.SeasonTypeEnum"
            # -> "from griddy.nfl.models.enums.season_type_enum import SeasonTypeEnum"
            parts = enum_import.rsplit(".", 1)
            imports.append(f"from {parts[0]} import {parts[1]}")
    return sorted(imports)


# ---------------------------------------------------------------------------
# Request model generation
# ---------------------------------------------------------------------------


def generate_request_model(model_spec: dict) -> str:
    """Generate a request model file from a model spec."""
    params = model_spec["params"]
    class_name = model_spec["class_name"]
    module_docstring = model_spec.get("module_docstring")
    class_docstring = model_spec.get("class_docstring")

    typing_imports = _collect_typing_imports(params)
    enum_imports = _collect_enum_imports(params)

    lines = []

    if module_docstring:
        lines.append(f'"""{module_docstring}"""')
        lines.append("")

    lines.append("from __future__ import annotations")
    lines.append("")

    # Typing imports
    typing_list = sorted(typing_imports)
    if typing_list:
        lines.append(f"from typing import {', '.join(typing_list)}")
        lines.append("")

    # pydantic import (only if aliases are used)
    has_alias = any(_needs_alias(p) for p in params)
    if has_alias:
        lines.append("import pydantic")

    lines.append("from typing_extensions import Annotated")
    lines.append("")

    # Enum imports
    for imp in enum_imports:
        lines.append(imp)

    lines.append("from griddy.nfl.types import BaseModel")
    lines.append("from griddy.nfl.utils import FieldMetadata, QueryParamMetadata")
    lines.append("")
    lines.append("")
    lines.append(f"class {class_name}(BaseModel):")

    if class_docstring:
        lines.append(f'    """{class_docstring}"""')
        lines.append("")

    for p in params:
        type_str = p["type"]
        required = p.get("required", False)
        alias = p.get("alias")
        default = p.get("default")
        doc = p.get("doc", "")

        python_type = _python_type(type_str, required)

        # Build Annotated contents
        annotated_parts = [python_type]
        if alias:
            annotated_parts.append(f'pydantic.Field(alias="{alias}")')
        annotated_parts.append(
            "FieldMetadata(query=QueryParamMetadata(" 'style="form", explode=True))'
        )

        # Format the field
        # Compact format: required primitive fields with no alias
        # Expanded format: optional, alias, or non-primitive fields
        use_compact = required and not alias and type_str in PRIMITIVE_TYPES
        if use_compact:
            annotation = (
                f"Annotated[\n"
                f"        {annotated_parts[0]}, "
                f"{annotated_parts[1]}\n"
                f"    ]"
            )
        else:
            annotation = "Annotated[\n"
            for i, part in enumerate(annotated_parts):
                annotation += f"        {part},\n"
            annotation += "    ]"

        if required:
            lines.append(f"    {p['name']}: {annotation}")
        else:
            default_str = _default_repr(default)
            lines.append(f"    {p['name']}: {annotation} = {default_str}")

        if doc:
            lines.append(f'    r"""{doc}"""')
        lines.append("")

    # Remove trailing blank line inside class, add final newline
    if lines and lines[-1] == "":
        lines.pop()
    lines.append("")

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Endpoint file generation
# ---------------------------------------------------------------------------


# Error code constant imports by name
ERROR_CODE_IMPORTS = {
    "COLLECTION_ERROR_CODES": "griddy.core._constants",
    "RESOURCE_ERROR_CODES": "griddy.core._constants",
    "STATS_ERROR_CODES": "griddy.core._constants",
    "SECURED_RESOURCE_ERROR_CODES": "griddy.core._constants",
    "NGS_ERROR_CODES": "griddy.core._constants",
    "PARAMETERLESS_ERROR_CODES": "griddy.core._constants",
}


# Types that are imported from typing, not from models
TYPING_TYPES = {"List", "Dict", "Set", "Tuple", "Mapping"}


def _build_endpoint_method_params(params: list[dict]) -> list[str]:
    """Build parameter lines for a config method signature."""
    lines = []
    for p in params:
        type_str = p["type"]
        required = p.get("required", False)

        # Map spec types to the types used in endpoint signatures
        endpoint_type = type_str
        # Check if the base type (before [) is a primitive or typing type
        base_type = type_str.split("[")[0]
        if base_type not in PRIMITIVE_TYPES and base_type not in TYPING_TYPES:
            # Enum types are accessed via models.*
            endpoint_type = f"models.{type_str}"

        if required:
            python_type = endpoint_type
        else:
            python_type = f"Optional[{endpoint_type}]"

        if required:
            lines.append(f"        {p['name']}: {python_type},")
        else:
            default_str = _default_repr(p.get("default"))
            lines.append(f"        {p['name']}: {python_type} = {default_str},")

    return lines


def _build_config_method(method_spec: dict, endpoint_spec: dict) -> str:
    """Build a single _config method from a method spec."""
    name = method_spec["name"]
    path = method_spec["path"]
    operation_id = method_spec["operation_id"]
    request_model = method_spec["request_model"]
    response_model = method_spec["response_model"]
    docstring = method_spec.get("docstring", "").rstrip()
    params = method_spec["params"]
    config_builder = method_spec.get("config_builder")
    error_codes = method_spec.get("error_codes")

    lines = []

    # Method signature
    lines.append(f"    def _get_{name}_config(")
    lines.append("        self,")
    lines.append("        *,")

    # Domain params
    param_lines = _build_endpoint_method_params(params)
    lines.extend(param_lines)

    # Standard infra params
    lines.append("        retries: OptionalNullable[utils.RetryConfig] = UNSET,")
    lines.append("        server_url: Optional[str] = None,")
    lines.append("        timeout_ms: Optional[int] = None,")
    lines.append("        http_headers: Optional[Mapping[str, str]] = None,")
    lines.append("    ) -> EndpointConfig:")

    # Docstring
    if docstring:
        # First line goes on the r""" line, rest are indented with 8 spaces
        doc_lines = docstring.split("\n")
        lines.append(f'        r"""{doc_lines[0]}')
        for dl in doc_lines[1:]:
            if dl.strip():
                lines.append(f"        {dl}")
            else:
                lines.append("")
        lines.append("")
        lines.append("        Args:")
        for p in params:
            doc = p.get("doc", "")
            lines.append(f"            {p['name']}: {doc}")
        lines.append(
            "            retries: Override the default retry configuration "
            "for this method"
        )
        lines.append(
            "            server_url: Override the default server URL " "for this method"
        )
        lines.append(
            "            timeout_ms: Override the default request timeout "
            "configuration for this method in milliseconds"
        )
        lines.append(
            "            http_headers: Additional headers to set or "
            "replace on requests."
        )
        lines.append('        """')

    # Body - depends on whether we use a config_builder helper
    if config_builder:
        lines.append(f"        return self.{config_builder}(")
        lines.append(f'            "{path}",')
        lines.append(f'            "{operation_id}",')
        lines.append(f"            models.{request_model},")
        lines.append(f"            models.{response_model},")
        for p in params:
            lines.append(f"            {p['name']}={p['name']},")
        lines.append("            server_url=server_url,")
        lines.append("            timeout_ms=timeout_ms,")
        lines.append("            http_headers=http_headers,")
        lines.append("            retries=retries,")
        lines.append("        )")
    else:
        # Direct EndpointConfig construction
        lines.append("        return EndpointConfig(")
        lines.append(f'            method="{method_spec["method"]}",')
        lines.append(f'            path="{path}",')
        lines.append(f'            operation_id="{operation_id}",')

        # Build request model
        lines.append(f"            request=models.{request_model}(")
        for p in params:
            lines.append(f"                {p['name']}={p['name']},")
        lines.append("            ),")

        lines.append(f"            response_type=models.{response_model},")

        if error_codes:
            lines.append(f"            error_status_codes={error_codes},")

        # Detect path params
        has_path_params = "{" in path
        if has_path_params:
            lines.append("            request_has_path_params=True,")
        lines.append("            request_has_query_params=True,")
        lines.append("            server_url=server_url,")
        lines.append("            timeout_ms=timeout_ms,")
        lines.append("            http_headers=http_headers,")
        lines.append("            retries=retries,")
        lines.append("            return_raw_json=False,")
        lines.append("        )")

    return "\n".join(lines)


def generate_endpoint_file(spec: dict) -> str:
    """Generate a complete endpoint file from a spec."""
    ep = spec["endpoint"]
    methods = spec["methods"]

    class_name = ep["class_name"]
    base_class = ep["base_class"]
    base_import = ep["base_import"]
    decorator = ep.get("decorator")
    module_docstring = ep.get("module_docstring", "").rstrip()
    class_docstring = ep.get("class_docstring", "").rstrip()

    # Collect needed imports
    needs_list = False
    for m in methods:
        for p in m["params"]:
            if p["type"].startswith("List["):
                needs_list = True

    # Collect error code imports
    error_code_names = set()
    for m in methods:
        ec = m.get("error_codes")
        if ec:
            error_code_names.add(ec)

    lines = []

    # Imports - determine if we need __future__ annotations
    has_config_builder = any(m.get("config_builder") for m in methods)
    has_direct_config = not has_config_builder

    if module_docstring:
        lines.append(f'"""{module_docstring}"""')
        lines.append("")

    if has_direct_config:
        lines.append("from __future__ import annotations")
        lines.append("")

    # Typing imports
    typing_parts = []
    if needs_list:
        typing_parts.append("List")
    typing_parts.append("Mapping")
    typing_parts.append("Optional")
    lines.append(f"from typing import {', '.join(sorted(typing_parts))}")
    lines.append("")

    # Error code imports
    for ec_name in sorted(error_code_names):
        module = ERROR_CODE_IMPORTS.get(ec_name, "griddy.core._constants")
        lines.append(f"from {module} import {ec_name}")

    if decorator:
        lines.append("from griddy.core.decorators import sdk_endpoints")

    lines.append("from griddy.nfl import models, utils")
    lines.append("from griddy.nfl.basesdk import EndpointConfig")
    lines.append(f"from {base_import} import {base_class}")
    lines.append("from griddy.nfl.types import UNSET, OptionalNullable")

    # For NGS endpoints that import RetryConfig directly
    if base_class == "NgsBaseSDK":
        # Already imported via utils
        pass

    lines.append("")
    lines.append("")

    # Class definition
    if decorator:
        lines.append(f"@{decorator}")
    lines.append(f"class {class_name}({base_class}):")

    if class_docstring:
        doc_lines = class_docstring.split("\n")
        if len(doc_lines) == 1:
            lines.append(f'    """{doc_lines[0]}"""')
        else:
            lines.append(f'    """{doc_lines[0]}')
            for dl in doc_lines[1:]:
                lines.append(f"    {dl}" if dl.strip() else "")
            lines.append('    """')

    # Methods
    for i, m in enumerate(methods):
        lines.append("")
        lines.append(_build_config_method(m, ep))

    lines.append("")

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Spec loading
# ---------------------------------------------------------------------------


def load_specs() -> list[dict]:
    """Load all YAML spec files from the specs/ directory."""
    specs = []
    for yaml_file in sorted(SPECS_DIR.rglob("*.yaml")):
        with open(yaml_file) as f:
            spec = yaml.safe_load(f)
        spec["_source"] = str(yaml_file.relative_to(PROJECT_ROOT))
        specs.append(spec)
    return specs


# ---------------------------------------------------------------------------
# Generation orchestration
# ---------------------------------------------------------------------------


def generate_all(
    check: bool = False,
    request_models_only: bool = False,
    endpoints_only: bool = False,
) -> int:
    """Generate all files from specs. Returns 0 on success, 1 on drift."""
    specs = load_specs()
    any_changed = False

    for spec in specs:
        source = spec["_source"]

        # Generate request models
        if not endpoints_only:
            for model_spec in spec.get("request_models", []):
                file_path = PROJECT_ROOT / model_spec["file_path"]
                generated = generate_request_model(model_spec)

                if check:
                    if file_path.exists():
                        current = file_path.read_text()
                    else:
                        current = ""
                    if current != generated:
                        print(
                            f"MISMATCH: {model_spec['file_path']} "
                            f"differs from spec {source}"
                        )
                        any_changed = True
                    else:
                        print(f"OK: {model_spec['file_path']}")
                else:
                    file_path.parent.mkdir(parents=True, exist_ok=True)
                    file_path.write_text(generated)
                    print(f"Generated: {model_spec['file_path']}")

        # Generate endpoint files
        if not request_models_only:
            ep = spec.get("endpoint", {})
            file_path_str = ep.get("file_path")
            if file_path_str:
                file_path = PROJECT_ROOT / file_path_str
                generated = generate_endpoint_file(spec)

                if check:
                    if file_path.exists():
                        current = file_path.read_text()
                    else:
                        current = ""
                    if current != generated:
                        print(
                            f"MISMATCH: {file_path_str} " f"differs from spec {source}"
                        )
                        any_changed = True
                    else:
                        print(f"OK: {file_path_str}")
                else:
                    file_path.parent.mkdir(parents=True, exist_ok=True)
                    file_path.write_text(generated)
                    print(f"Generated: {file_path_str}")

    if check and any_changed:
        print(
            "\nDrift detected! Run 'python scripts/generate_endpoints.py' "
            "to regenerate."
        )
        return 1

    if check and not any_changed:
        print("\nAll generated files are up to date.")

    return 0


def main() -> int:
    check = "--check" in sys.argv
    request_models_only = "--request-models-only" in sys.argv
    endpoints_only = "--endpoints-only" in sys.argv
    return generate_all(
        check=check,
        request_models_only=request_models_only,
        endpoints_only=endpoints_only,
    )


if __name__ == "__main__":
    sys.exit(main())
