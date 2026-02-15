import importlib
import sys
from typing import TYPE_CHECKING, Optional

from griddy.nfl.basesdk import BaseSDK
from griddy.nfl.sdkconfiguration import SDKConfiguration

if TYPE_CHECKING:
    from griddy.nfl.endpoints.regular.football.stats.historical import HistoricalStats
    from griddy.nfl.endpoints.regular.football.stats.live import LiveStats


class FootballStatsSDK(BaseSDK):
    r"""Aggregates historical and live football statistics endpoints"""

    historical: "HistoricalStats"
    r"""Historical game statistics (team and player level)"""
    live: "LiveStats"
    r"""Live game statistics (team and player level)"""

    _sub_sdk_map = {
        "historical": (
            "griddy.nfl.endpoints.regular.football.stats.historical",
            "HistoricalStats",
        ),
        "live": (
            "griddy.nfl.endpoints.regular.football.stats.live",
            "LiveStats",
        ),
    }

    def __init__(self, sdk_config: SDKConfiguration, parent_ref: Optional[object]):
        super().__init__(sdk_config=sdk_config, parent_ref=parent_ref)

    def dynamic_import(self, modname, retries=3):
        for attempt in range(retries):
            try:
                return importlib.import_module(modname)
            except KeyError:
                sys.modules.pop(modname, None)
                if attempt == retries - 1:
                    break
        raise KeyError(f"Failed to import module '{modname}' after {retries} attempts")

    def __getattr__(self, name: str):
        if name in self._sub_sdk_map:
            module_path, class_name = self._sub_sdk_map[name]
            try:
                module = self.dynamic_import(module_path)
                klass = getattr(module, class_name)
                instance = klass(self.sdk_configuration, parent_ref=self.parent_ref)
                setattr(self, name, instance)
                return instance
            except ImportError as e:
                raise AttributeError(
                    f"Failed to import module {module_path} for attribute {name}: {e}"
                ) from e
            except AttributeError as e:
                raise AttributeError(
                    f"Failed to find class {class_name} in module {module_path}: {e}"
                ) from e

        raise AttributeError(
            f"'{type(self).__name__}' object has no attribute '{name}'"
        )

    def __dir__(self):
        default_attrs = list(super().__dir__())
        lazy_attrs = list(self._sub_sdk_map.keys())
        return sorted(list(set(default_attrs + lazy_attrs)))
