from typing import List, Optional

import pydantic
from typing_extensions import Annotated, NotRequired, TypedDict

from griddy.nfl.types import BaseModel

from .player import Player, PlayerTypedDict
from .team import Team, TeamTypedDict


class TweetTypedDict(TypedDict):
    account: str
    sent: bool


class DraftPickTypedDict(TypedDict):
    year: int
    draft_round: int
    draft_position: int
    draft_number_overall: int
    person_id: str
    pick_is_in: bool
    team_id: str
    trade_note: NotRequired[str]
    tweet_sent: bool
    tweets_sent: List[TweetTypedDict]


class Tweet(BaseModel):
    account: str
    sent: bool


class DraftPick(BaseModel):
    year: int
    draft_round: Annotated[int, pydantic.Field(alias="draftRound")]
    draft_position: Annotated[int, pydantic.Field(alias="draftPosition")]
    draft_number_overall: Annotated[int, pydantic.Field(alias="draftNumberOverall")]
    person_id: Annotated[str, pydantic.Field(alias="personId")]
    pick_is_in: Annotated[bool, pydantic.Field(alias="pickIsIn")]
    team_id: Annotated[str, pydantic.Field(alias="teamId")]
    trade_note: Annotated[Optional[str], pydantic.Field(alias="tradeNote")] = None
    tweet_sent: Annotated[int, pydantic.Field(alias="tweetSent")]
    tweets_sent: Annotated[List[Tweet], pydantic.Field(alias="tweetsSent")]
