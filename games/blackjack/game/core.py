from dataclasses import dataclass, field
from random import choice

from .constants import CARD_SUITS, CARD_VALUES


@dataclass
class Card:
    suit: str
    value: int = field(init=False)

    def __post_init__(self):
        self.value = CARD_VALUES[self.suit]


@dataclass
class Player:
    _hand: list[Card] = field(init=False, repr=False)
    _score: int = field(init=False, repr=False)

    def __post_init__(self):
        self._hand = [Card(choice(CARD_SUITS)), Card(choice(CARD_SUITS))]

    @property
    def hand(self):
        return [card.suit for card in self._hand]

    @property
    def score(self):
        total = sum([card.value for card in self._hand])

        aces = [card.suit for card in self._hand if card.suit == "A"]
        for _ in aces:
            if total > 21:
                total -= 10

        return total

    def draw(self):
        self._hand.append(Card(choice(CARD_SUITS)))


@dataclass
class Blackjack:
    dealer: Player = field(default_factory=Player)
    player: Player = field(default_factory=Player)
    running: bool = False

    def get_result(self):
        if (self.dealer.score == 21) or (self.player.score > 21):
            return "Dealer Wins"

        if (self.player.score == 21) or (self.dealer.score > 21):
            return "Player Wins"

        if self.player.score < self.dealer.score:
            return "Dealer Wins"

        if self.player.score > self.dealer.score:
            return "Player Wins"

        return "Draw"

    def start(self):
        self.running = True

    def end(self):
        self.running = False
