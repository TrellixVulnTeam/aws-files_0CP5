from dataclasses import dataclass, field
from typing import List


RANKS = '2 3 4 5 6 7 8 9 J Q K A'.split()
SUITS = '♣ ♢ ♡ ♠'.split()


@dataclass
class Position:
    name: str
    longitude: float = 0.0
    lattitude: float = 0.0

@dataclass
class Capital(Position):
    country: str = 'India'

@dataclass(frozen=True)
class PlayingCard:
    #sort_index: int = field(init=False, repr=False)
    rank: str
    suit: str

    """
    def __post_init__(self):
        self.sort_index = (RANKS.index(self.rank) * len(SUITS)
                           + SUITS.index(self.suit))

    def __str__(self):
        return f'{self.suit}{self.rank}'
    """



def make_deck():
    return [PlayingCard(r,s) for s in SUITS for r in RANKS]

@dataclass(frozen=True)
class Deck:
    cards: List[PlayingCard] #= field(default_factory=make_deck)

