from random import choice

from game.choices import CHOICE_EMOJI, CHOICES


def main():
    try:
        player_input = input("What do you choose? rock | paper | scissors\n").upper()
        player_choice = CHOICES[player_input]
        computer_choice = choice([*CHOICES])

        print(f"\nYou chose {CHOICE_EMOJI[player_choice]}")
        print(f"Computer chose {CHOICE_EMOJI[computer_choice]}\n")

        if player_choice == computer_choice:
            return print("You draw!")

        match player_choice:
            case CHOICES.ROCK:
                if computer_choice == CHOICES.PAPER:
                    return print("You Loose!")
            case CHOICES.PAPER:
                if computer_choice == CHOICES.SCISSORS:
                    return print("You Loose!")
            case CHOICES.PAPER:
                if computer_choice == CHOICES.ROCK:
                    return print("You Loose!")

        print("You Win!")
    except KeyError:
        print("This choice is not available.")
    except:
        print("\nSomething went wrong, please try again.")


if __name__ == "__main__":
    main()
