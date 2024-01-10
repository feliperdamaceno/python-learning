from dataclasses import dataclass
from enum import Enum
from random import randint


class Levels(Enum):
    easy = 10
    hard = 5


@dataclass
class GuessNumber:
    running: bool = False
    tentatives: int = 0
    number: int = 0

    def start(self):
        self.running = True

    def end(self):
        self.running = False

    def select_difficulty(self, level: Levels):
        self.tentatives = Levels[level].value

    def randomize(self):
        self.number = randint(1, 100)

    def guess(self, guess: int):
        if self.number > guess:
            self.tentatives -= 1
            print("\nToo Low")
            return False

        if self.number < guess:
            self.tentatives -= 1
            print("\nToo High")
            return False

        print(f"\nYou got it! The answer was {self.number}")
        return True
