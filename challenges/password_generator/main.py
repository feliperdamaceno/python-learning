from password.generator import PasswordSeed, password_generator


def main():
    print("Welcome to the dummy password generator!")

    seed = PasswordSeed()

    seed.letters = int(input("How many letters do you want to include?\n"))
    seed.numbers = int(input("How many numbers do you want to include?\n"))
    seed.symbols = int(input("How many symbols do you want to include?\n"))

    password = password_generator(seed)
    print(f"\nHere is your password: {password}")

    # This is a very dummy password generator, it should not be used in the real world.
    # For the sake of your security, please don't... 🫠


if __name__ == "__main__":
    main()
