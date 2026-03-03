import importlib

import pytest

from griddy.nfl import GriddyNFL
from griddy.nfl.endpoints.ngs import NextGenStats
from griddy.nfl.endpoints.pro.stats import StatsSDK
from griddy.nfl.endpoints.regular.football.stats import FootballStatsSDK


@pytest.mark.unit
class TestGriddyNFLSDK:
    def test_pro_endpoints_are_routed_to_pro_server(self):
        pass


def _collect_sub_sdk_map_entries():
    """Collect all _sub_sdk_map entries across NFL SDK classes for parametrize."""
    entries = []
    classes = [GriddyNFL, NextGenStats, StatsSDK, FootballStatsSDK]
    for cls in classes:
        for attr_name, (module_path, class_name) in cls._sub_sdk_map.items():
            entries.append(
                pytest.param(
                    module_path,
                    class_name,
                    id=f"{cls.__name__}.{attr_name}",
                )
            )
    return entries


@pytest.mark.unit
class TestSubSdkMapImportable:
    """Validate every _sub_sdk_map entry across all NFL SDK classes is importable."""

    @pytest.mark.parametrize("module_path,class_name", _collect_sub_sdk_map_entries())
    def test_module_importable_and_class_exists(self, module_path, class_name):
        """Each _sub_sdk_map entry must point to a real module and class."""
        module = importlib.import_module(module_path)
        klass = getattr(module, class_name)
        assert callable(klass), f"{module_path}.{class_name} should be callable"
