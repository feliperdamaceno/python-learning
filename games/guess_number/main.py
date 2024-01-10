from game.ascii import LOGO
from game.core import GuessNumber


def main():
    guess_number = GuessNumber()
    guess_number.start()
    guess_number.randomize()

    print(LOGO)
    print("Let's play a Guessing Game!")
    print("I'll randomly select a number from 1 to 100, you have to guess!\n")
    level = input('Select the level of difficulty "easy" or "hard": ').strip().lower()

    if level not in ["easy", "hard"]:
        print(f"The level {level} is not available.")
        return

    guess_number.select_difficulty(level)

    while guess_number.running:
        print("-" * 50)
        print(f"You have {guess_number.tentatives} tentatives.")
        guess = int(input("\nGuess the number: ").strip())

        is__guess_correct = guess_number.guess(guess)

        if is__guess_correct:
            guess_number.end()

        if guess_number.tentatives == 0:
            print("\nYou ran out of tentatives!")
            guess_number.end()


if __name__ == "__main__":
    main()
