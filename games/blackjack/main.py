from time import sleep

from game.ascii import LOGO
from game.core import Blackjack


def main():
    blackjack = Blackjack()

    print(LOGO)
    print("Let's play Blackjack!\n")

    blackjack.start()
    while blackjack.running:
        print("-" * 50)
        print(f"Player hand: {' | '.join(blackjack.player.hand)}")
        print(f"Dealer hand: {blackjack.dealer.hand[0]}")

        hit = input('\nDo you want to draw another card? "Y" or "N": ').strip().upper()

        if hit == "N":
            blackjack.end()
            continue

        print("-" * 50)
        print("Player draws another card...")
        blackjack.player.draw()
        sleep(1.5)

        if blackjack.player.score >= 21:
            blackjack.end()

    if blackjack.player.score != 21:
        while blackjack.dealer.score < 17:
            print("-" * 50)
            print("Dealer draws another card...")
            blackjack.dealer.draw()
            sleep(1.5)

    result = blackjack.get_result()
    print("-" * 50)
    print(f"The result is: {result}\n")

    print(f"Player hand: {' | '.join(blackjack.player.hand)}")
    print(f"Player score: {blackjack.player.score}\n")

    print(f"Dealer hand: {' | '.join(blackjack.dealer.hand)}")
    print(f"Dealer score: {blackjack.dealer.score}")


if __name__ == "__main__":
    main()
