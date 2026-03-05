from __future__ import annotations

from typing import List

from griddy.nfl.models.entities.film_card import FilmCard
from griddy.nfl.types import BaseModel


class HomeFilmCardsResponse(BaseModel):
    cards: List[FilmCard]

    title: str
    r"""Title of the film card collection"""
