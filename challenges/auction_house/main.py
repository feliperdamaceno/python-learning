from auction_house.core import AuctionHouse, Bidder
from interface.ascii import LOGO


def clear_terminal():
    print("\033[H\033[J", end="")


def main():
    auction_house = AuctionHouse()

    print(LOGO)
    print("Welcome to the Secret Auction House!")
    while True:
        name = input("What is the bidder's name? ").strip()
        bid = float(input("What is the bid? €"))

        auction_house.add_bidder(Bidder(name, bid))

        keep_bidding = input('Do you want to add another bidder? "Y" or "N":  ').upper()
        if keep_bidding == "N":
            break

        clear_terminal()

    winner = auction_house.get_winner()
    print(f"The winner was {winner.name} with a bid of €{winner.bid:.2f}")


if __name__ == "__main__":
    main()
