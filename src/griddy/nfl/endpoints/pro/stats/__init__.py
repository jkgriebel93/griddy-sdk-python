from typing import Optional

from griddy.nfl.endpoints.pro import ProSDK
from griddy.nfl.sdkconfiguration import SDKConfiguration


class PlayerSeasonStats(ProSDK):
    def __init__(
        self, category: str, sdk_config: SDKConfiguration, parent_ref: Optional[object]
    ):

        super().__init__(sdk_config, parent_ref)
        self.category = category

    def summary(self):
        pass

    def per_game(self):
        pass

    def ngs_advanced_metrics(self):
        pass


class PlayerGameStats(ProSDK):
    def __init__(
        self, category: str, sdk_config: SDKConfiguration, parent_ref: Optional[object]
    ):
        super().__init__(sdk_config, parent_ref)
        self.category = category

    def summary(self):
        pass

    def ngs_advanced_metrics(self):
        pass


class PlayerStats(ProSDK):
    # TODO: I'm not sure if I've nailed the inheritance structure here
    def __init__(
        self, category: str, sdk_config: SDKConfiguration, parent_ref: Optional[object]
    ):
        super().__init__(sdk_config, parent_ref)
        self.category = category
        self.season = PlayerSeasonStats(
            category=category, sdk_config=sdk_config, parent_ref=parent_ref
        )
        self.game = PlayerGameStats(
            category=category, sdk_config=sdk_config, parent_ref=parent_ref
        )
