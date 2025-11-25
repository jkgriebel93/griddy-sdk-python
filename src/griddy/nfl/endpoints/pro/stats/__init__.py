import importlib
import sys
from typing import TYPE_CHECKING, Optional

from griddy.nfl.endpoints.pro import ProSDK
from griddy.nfl.sdkconfiguration import SDKConfiguration

if TYPE_CHECKING:
    from griddy.nfl.endpoints.pro.stats.defense import PlayerDefenseStats
    from griddy.nfl.endpoints.pro.stats.fantasy import Fantasy
    from griddy.nfl.endpoints.pro.stats.passing import PlayerPassingStats
    from griddy.nfl.endpoints.pro.stats.receiving import PlayerReceivingStats
    from griddy.nfl.endpoints.pro.stats.rushing import PlayerRushingStats
    from griddy.nfl.endpoints.pro.stats.team_defense import TeamDefenseStats
    from griddy.nfl.endpoints.pro.stats.team_offense import TeamOffenseStats


class StatsSDK(ProSDK):
    r"""Aggregates all player and team statistics endpoints"""

    passing: "PlayerPassingStats"
    r"""Player passing statistics"""
    receiving: "PlayerReceivingStats"
    r"""Player receiving statistics"""
    rushing: "PlayerRushingStats"
    r"""Player rushing statistics"""
    defense: "PlayerDefenseStats"
    r"""Player defensive statistics"""
    team_offense: "TeamOffenseStats"
    r"""Team offensive statistics"""
    team_defense: "TeamDefenseStats"
    r"""Team defensive statistics"""
    fantasy: "Fantasy"
    r"""Fantasy statistics"""

    _sub_sdk_map = {
        "passing": (
            "griddy.nfl.endpoints.pro.stats.passing",
            "PlayerPassingStats",
        ),
        "receiving": (
            "griddy.nfl.endpoints.pro.stats.receiving",
            "PlayerReceivingStats",
        ),
        "rushing": (
            "griddy.nfl.endpoints.pro.stats.rushing",
            "PlayerRushingStats",
        ),
        "defense": (
            "griddy.nfl.endpoints.pro.stats.defense",
            "PlayerDefenseStats",
        ),
        "team_offense": (
            "griddy.nfl.endpoints.pro.stats.team_offense",
            "TeamOffenseStats",
        ),
        "team_defense": (
            "griddy.nfl.endpoints.pro.stats.team_defense",
            "TeamDefenseStats",
        ),
        "fantasy": (
            "griddy.nfl.endpoints.pro.stats.fantasy",
            "Fantasy",
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
