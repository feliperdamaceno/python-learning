from game.ascii import LOGO, STAGES
from game.hangman import HangmanGame


def clear_terminal():
    print("\033[H\033[J", end="")


def main():
    print(LOGO)

    game = HangmanGame()
    game.start()

    while game.running:
        guess = input("\nGuess a letter: ").lower()
        is_not_correct = game.guess_word(guess)

        clear_terminal()
        print(game.word)
        print(STAGES[game.lifes])

        if is_not_correct:
            print(f"You guessed {guess.upper()}, which is not part of the word!")
            print("You lose a life!")
            continue

    if game.lifes == 0:
        print(f"\nThe world was {game._word.upper()}!")
        return print(f"You ran out of lifes, try again!")

    print(f"\nYou Win!")


if __name__ == "__main__":
    main()
