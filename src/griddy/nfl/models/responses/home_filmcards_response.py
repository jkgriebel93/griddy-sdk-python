from __future__ import annotations

from typing import List

from typing_extensions import TypedDict

from griddy.nfl.models.entities.film_card import FilmCard, FilmCardTypedDict
from griddy.nfl.types import BaseModel


class HomeFilmCardsResponseTypedDict(TypedDict):
    cards: List[FilmCardTypedDict]
    title: str
    r"""Title of the film card collection"""


class HomeFilmCardsResponse(BaseModel):
    cards: List[FilmCard]

    title: str
    r"""Title of the film card collection"""
