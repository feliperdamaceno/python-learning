from dataclasses import dataclass
from random import choice, randint, random

from .constants import LETTERS, NUMBERS, SYMBOLS


@dataclass
class PasswordSeed:
    letters: int = 0
    numbers: int = 0
    symbols: int = 0


# I know there is a shuffle method in random, but I wanted to implement my own 😝
def shuffle(x: list) -> list:
    temp = x.copy()
    output = []

    for _ in range(len(x)):
        output.append(temp.pop(randint(0, len(temp) - 1)))

    return output


def password_generator(seed: PasswordSeed) -> str:
    password = []

    for _ in range(seed.letters):
        letter = choice(LETTERS)

        if random() < 0.4:  # 0.4 is equivalent to 40% True values.
            letter = letter.upper()

        password.append(letter)

    password.extend([choice(NUMBERS) for _ in range(seed.numbers)])
    password.extend([choice(NUMBERS) for _ in range(seed.numbers)])
    password.extend([choice(SYMBOLS) for _ in range(seed.symbols)])

    password = shuffle(password)

    return "".join(password)
