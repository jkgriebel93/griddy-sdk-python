from typing import List, Optional

import pydantic
from typing_extensions import Annotated

from griddy.nfl.types import BaseModel


class Tweet(BaseModel):
    """Tweet associated with a draft pick."""

    account: str
    sent: bool


class DraftPick(BaseModel):
    """Individual NFL Draft pick with player and team details."""

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
