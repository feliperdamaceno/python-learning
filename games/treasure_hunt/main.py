from game.ascii import TREASURE_CHEST
from game.questions import QUESTIONS


def main():
    print(TREASURE_CHEST)
    print("Welcome to Treasure Island.")
    print("Your mission is to find the treasure.\n")

    first_answer = input(QUESTIONS["FIRST"]).upper()
    if first_answer != "LEFT":
        return print("You fell into a hole. Game Over!")

    second_answer = input(QUESTIONS["SECOND"]).upper()
    if second_answer != "WAIT":
        return print("You get attacked by an angry trout. Game Over!")

    third_answer = input(QUESTIONS["THIRD"]).upper()
    match third_answer:
        case "RED":
            print("It's a room full of fire. Game Over!")
        case "YELLOW":
            print("You found the treasure! You Win!")
        case "BLUE":
            print("You enter a room of beasts. Game Over!")
        case _:
            print("You chose a door that doesn't exist. Game Over!")


if __name__ == "__main__":
    main()
