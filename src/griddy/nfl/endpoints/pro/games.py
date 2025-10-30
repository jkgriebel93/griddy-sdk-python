from griddy.nfl.endpoints.pro import ProSDK
from griddy.nfl.endpoints.pro.mixins import GameContentMixin, GameScheduleMixin


class Games(ProSDK, GameScheduleMixin, GameContentMixin):
    pass
