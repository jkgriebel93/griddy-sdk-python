"""Tests for the scripts/generate_endpoints.py code generation script."""

import textwrap
from pathlib import Path

import pytest
from scripts.generate_endpoints import (
    generate_endpoint_file,
    generate_request_model,
    load_specs,
)

# ---------------------------------------------------------------------------
# Request model generation
# ---------------------------------------------------------------------------


class TestGenerateRequestModel:
    def test_required_primitive_field_compact_format(self):
        """Required primitive fields use compact 2-line Annotated format."""
        spec = {
            "class_name": "TestRequest",
            "params": [
                {"name": "season", "type": "int", "required": True, "doc": "Year"},
            ],
        }
        result = generate_request_model(spec)
        assert "int, FieldMetadata(" in result
        assert "class TestRequest(BaseModel):" in result

    def test_optional_field_expanded_format(self):
        """Optional fields use expanded multi-line Annotated format."""
        spec = {
            "class_name": "TestRequest",
            "params": [
                {
                    "name": "limit",
                    "type": "int",
                    "required": False,
                    "default": 50,
                    "doc": "Max results",
                },
            ],
        }
        result = generate_request_model(spec)
        assert "Optional[int],\n" in result
        assert "= 50" in result

    def test_alias_field_expanded_format(self):
        """Fields with aliases use expanded multi-line format."""
        spec = {
            "class_name": "TestRequest",
            "params": [
                {
                    "name": "season_type",
                    "type": "str",
                    "alias": "seasonType",
                    "required": True,
                    "doc": "Season type",
                },
            ],
        }
        result = generate_request_model(spec)
        assert 'pydantic.Field(alias="seasonType")' in result
        assert "import pydantic" in result

    def test_required_enum_field_expanded_format(self):
        """Required non-primitive fields use expanded format."""
        spec = {
            "class_name": "TestRequest",
            "params": [
                {
                    "name": "week",
                    "type": "WeekEnum",
                    "required": True,
                    "doc": "Week",
                    "enum_import": "griddy.nfl.models.enums.week.WeekEnum",
                },
            ],
        }
        result = generate_request_model(spec)
        assert "WeekEnum,\n" in result
        assert "from griddy.nfl.models.enums.week import WeekEnum" in result

    def test_list_type_imports(self):
        """List types generate correct typing import."""
        spec = {
            "class_name": "TestRequest",
            "params": [
                {
                    "name": "teams",
                    "type": "List[str]",
                    "required": False,
                    "default": None,
                    "doc": "Team filter",
                },
            ],
        }
        result = generate_request_model(spec)
        assert "from typing import List, Optional" in result
        assert "Optional[List[str]]" in result

    def test_no_alias_no_pydantic_import(self):
        """Without aliases, pydantic is not imported."""
        spec = {
            "class_name": "TestRequest",
            "params": [
                {"name": "season", "type": "int", "required": True, "doc": "Year"},
            ],
        }
        result = generate_request_model(spec)
        assert "import pydantic" not in result

    def test_module_docstring(self):
        """Module docstring is included when specified."""
        spec = {
            "class_name": "TestRequest",
            "module_docstring": "Request model for test endpoint.",
            "params": [
                {"name": "season", "type": "int", "required": True, "doc": "Year"},
            ],
        }
        result = generate_request_model(spec)
        assert result.startswith('"""Request model for test endpoint."""')

    def test_class_docstring(self):
        """Class docstring is included when specified."""
        spec = {
            "class_name": "TestRequest",
            "class_docstring": "Request for getting test data.",
            "params": [
                {"name": "season", "type": "int", "required": True, "doc": "Year"},
            ],
        }
        result = generate_request_model(spec)
        assert '    """Request for getting test data."""' in result

    def test_default_none(self):
        """None defaults are rendered correctly."""
        spec = {
            "class_name": "TestRequest",
            "params": [
                {
                    "name": "sort_key",
                    "type": "str",
                    "required": False,
                    "default": None,
                    "doc": "Sort field",
                },
            ],
        }
        result = generate_request_model(spec)
        assert "= None" in result

    def test_default_bool(self):
        """Boolean defaults are rendered correctly."""
        spec = {
            "class_name": "TestRequest",
            "params": [
                {
                    "name": "qualified",
                    "type": "bool",
                    "required": False,
                    "default": True,
                    "doc": "Qualified filter",
                },
            ],
        }
        result = generate_request_model(spec)
        assert "= True" in result


# ---------------------------------------------------------------------------
# Endpoint file generation
# ---------------------------------------------------------------------------


class TestGenerateEndpointFile:
    def test_config_builder_method(self):
        """Methods using a config_builder helper generate correctly."""
        spec = {
            "endpoint": {
                "class_name": "TestStats",
                "base_class": "PlayerStatsBase",
                "base_import": "griddy.nfl.endpoints.pro.stats.base",
                "decorator": "sdk_endpoints",
            },
            "methods": [
                {
                    "name": "season_summary",
                    "path": "/api/stats/test/season",
                    "operation_id": "getTestStatsBySeason",
                    "method": "GET",
                    "config_builder": "_make_stats_config",
                    "request_model": "GetTestStatsRequest",
                    "response_model": "TestStatsResponse",
                    "docstring": "Get test stats by season.",
                    "params": [
                        {
                            "name": "season",
                            "type": "int",
                            "required": True,
                            "doc": "Season year",
                        },
                    ],
                },
            ],
        }
        result = generate_endpoint_file(spec)
        assert "class TestStats(PlayerStatsBase):" in result
        assert "@sdk_endpoints" in result
        assert "def _get_season_summary_config(" in result
        assert "self._make_stats_config(" in result
        assert '"/api/stats/test/season",' in result
        assert "models.GetTestStatsRequest," in result

    def test_direct_endpoint_config(self):
        """Methods without config_builder generate direct EndpointConfig."""
        spec = {
            "endpoint": {
                "class_name": "TestEndpoint",
                "base_class": "NgsBaseSDK",
                "base_import": "griddy.nfl.endpoints.ngs",
                "decorator": "sdk_endpoints",
            },
            "methods": [
                {
                    "name": "get_data",
                    "path": "/api/data",
                    "operation_id": "getData",
                    "method": "GET",
                    "error_codes": "NGS_ERROR_CODES",
                    "request_model": "GetDataRequest",
                    "response_model": "DataResponse",
                    "params": [
                        {
                            "name": "season",
                            "type": "int",
                            "required": True,
                            "doc": "Season",
                        },
                    ],
                },
            ],
        }
        result = generate_endpoint_file(spec)
        assert "return EndpointConfig(" in result
        assert "error_status_codes=NGS_ERROR_CODES," in result
        assert "from griddy.core._constants import NGS_ERROR_CODES" in result

    def test_path_params_detected(self):
        """Path parameters are detected from curly braces in path."""
        spec = {
            "endpoint": {
                "class_name": "TestEndpoint",
                "base_class": "BaseSDK",
                "base_import": "griddy.nfl.basesdk",
                "decorator": "sdk_endpoints",
            },
            "methods": [
                {
                    "name": "get_item",
                    "path": "/api/items/{itemId}",
                    "operation_id": "getItem",
                    "method": "GET",
                    "error_codes": "RESOURCE_ERROR_CODES",
                    "request_model": "GetItemRequest",
                    "response_model": "ItemResponse",
                    "params": [
                        {
                            "name": "item_id",
                            "type": "str",
                            "required": True,
                            "doc": "Item ID",
                        },
                    ],
                },
            ],
        }
        result = generate_endpoint_file(spec)
        assert "request_has_path_params=True," in result

    def test_enum_types_prefixed_with_models(self):
        """Non-primitive types are prefixed with models. in endpoint signatures."""
        spec = {
            "endpoint": {
                "class_name": "TestEndpoint",
                "base_class": "BaseSDK",
                "base_import": "griddy.nfl.basesdk",
            },
            "methods": [
                {
                    "name": "get_data",
                    "path": "/api/data",
                    "operation_id": "getData",
                    "method": "GET",
                    "request_model": "GetDataRequest",
                    "response_model": "DataResponse",
                    "params": [
                        {
                            "name": "season_type",
                            "type": "SeasonTypeEnum",
                            "required": True,
                            "doc": "Season type",
                        },
                    ],
                },
            ],
        }
        result = generate_endpoint_file(spec)
        assert "models.SeasonTypeEnum," in result

    def test_list_types_not_prefixed_with_models(self):
        """List[str] should not become models.List[str]."""
        spec = {
            "endpoint": {
                "class_name": "TestEndpoint",
                "base_class": "BaseSDK",
                "base_import": "griddy.nfl.basesdk",
            },
            "methods": [
                {
                    "name": "get_data",
                    "path": "/api/data",
                    "operation_id": "getData",
                    "method": "GET",
                    "request_model": "GetDataRequest",
                    "response_model": "DataResponse",
                    "params": [
                        {
                            "name": "teams",
                            "type": "List[str]",
                            "required": False,
                            "default": None,
                            "doc": "Teams",
                        },
                    ],
                },
            ],
        }
        result = generate_endpoint_file(spec)
        assert "Optional[List[str]]" in result
        assert "models.List" not in result

    def test_module_docstring(self):
        """Module docstring is rendered at top of file."""
        spec = {
            "endpoint": {
                "class_name": "TestEndpoint",
                "base_class": "BaseSDK",
                "base_import": "griddy.nfl.basesdk",
                "module_docstring": "Test endpoint module.",
            },
            "methods": [
                {
                    "name": "get_data",
                    "path": "/api/data",
                    "operation_id": "getData",
                    "method": "GET",
                    "request_model": "GetDataRequest",
                    "response_model": "DataResponse",
                    "params": [],
                },
            ],
        }
        result = generate_endpoint_file(spec)
        assert result.startswith('"""Test endpoint module."""')

    def test_class_docstring(self):
        """Class docstring is rendered in the class body."""
        spec = {
            "endpoint": {
                "class_name": "TestEndpoint",
                "base_class": "BaseSDK",
                "base_import": "griddy.nfl.basesdk",
                "class_docstring": "Test endpoint class.",
            },
            "methods": [
                {
                    "name": "get_data",
                    "path": "/api/data",
                    "operation_id": "getData",
                    "method": "GET",
                    "request_model": "GetDataRequest",
                    "response_model": "DataResponse",
                    "params": [],
                },
            ],
        }
        result = generate_endpoint_file(spec)
        assert '    """Test endpoint class."""' in result


# ---------------------------------------------------------------------------
# Spec loading
# ---------------------------------------------------------------------------


class TestLoadSpecs:
    def test_loads_yaml_specs(self):
        """Specs are loaded from the specs/ directory."""
        specs = load_specs()
        assert len(specs) >= 2
        for spec in specs:
            assert "_source" in spec
            assert "endpoint" in spec
            assert "methods" in spec


# ---------------------------------------------------------------------------
# Drift detection (actual files vs specs)
# ---------------------------------------------------------------------------


class TestActualFileDrift:
    """Verify that generated files from specs match actual files on disk."""

    def test_pro_stats_passing_request_models(self):
        import yaml

        spec_path = (
            Path(__file__).resolve().parent.parent
            / "specs"
            / "nfl"
            / "pro"
            / "stats"
            / "passing.yaml"
        )
        with open(spec_path) as f:
            spec = yaml.safe_load(f)

        for model in spec["request_models"]:
            file_path = Path(__file__).resolve().parent.parent / model["file_path"]
            generated = generate_request_model(model)
            actual = file_path.read_text()
            assert actual == generated, (
                f"{model['file_path']} is out of date. "
                "Run 'python scripts/generate_endpoints.py' to regenerate."
            )

    def test_pro_stats_passing_endpoint(self):
        import yaml

        spec_path = (
            Path(__file__).resolve().parent.parent
            / "specs"
            / "nfl"
            / "pro"
            / "stats"
            / "passing.yaml"
        )
        with open(spec_path) as f:
            spec = yaml.safe_load(f)

        file_path = (
            Path(__file__).resolve().parent.parent / spec["endpoint"]["file_path"]
        )
        generated = generate_endpoint_file(spec)
        actual = file_path.read_text()
        assert actual == generated, (
            f"{spec['endpoint']['file_path']} is out of date. "
            "Run 'python scripts/generate_endpoints.py' to regenerate."
        )

    def test_ngs_stats_request_models(self):
        import yaml

        spec_path = (
            Path(__file__).resolve().parent.parent
            / "specs"
            / "nfl"
            / "ngs"
            / "stats.yaml"
        )
        with open(spec_path) as f:
            spec = yaml.safe_load(f)

        for model in spec["request_models"]:
            file_path = Path(__file__).resolve().parent.parent / model["file_path"]
            generated = generate_request_model(model)
            actual = file_path.read_text()
            assert actual == generated, (
                f"{model['file_path']} is out of date. "
                "Run 'python scripts/generate_endpoints.py' to regenerate."
            )

    def test_ngs_stats_endpoint(self):
        import yaml

        spec_path = (
            Path(__file__).resolve().parent.parent
            / "specs"
            / "nfl"
            / "ngs"
            / "stats.yaml"
        )
        with open(spec_path) as f:
            spec = yaml.safe_load(f)

        file_path = (
            Path(__file__).resolve().parent.parent / spec["endpoint"]["file_path"]
        )
        generated = generate_endpoint_file(spec)
        actual = file_path.read_text()
        assert actual == generated, (
            f"{spec['endpoint']['file_path']} is out of date. "
            "Run 'python scripts/generate_endpoints.py' to regenerate."
        )
