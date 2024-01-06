from dataclasses import dataclass, field


@dataclass
class Bidder:
    name: str
    bid: float


@dataclass
class AuctionHouse:
    _bidders: list[Bidder] = field(init=False, repr=False, default_factory=list)

    def add_bidder(self, bidder: Bidder):
        self._bidders.append(bidder)

    def get_winner(self):
        greater_bid = max([bidder.bid for bidder in self._bidders])
        winner = [bidder for bidder in self._bidders if bidder.bid == greater_bid][0]
        return winner
