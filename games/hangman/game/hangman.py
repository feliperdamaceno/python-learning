from dataclasses import dataclass, field
from random import choice

from .ascii import STAGES
from .words import WORDS


@dataclass
class HangmanGame:
    word_list: tuple[str] = field(default_factory=lambda: WORDS)
    guesses: list[str] = field(default_factory=list)
    _word: str = field(init=False, repr=False, default="")
    lifes: int = 0
    running: bool = False

    @property
    def word(self) -> str:
        output = ""
        for letter in self._word:
            if letter not in self.guesses:
                output += "_"
                continue
            output += letter
        return output

    def __randomize_word(self):
        self._word = choice(self.word_list)

    def __reset_lifes(self):
        self.lifes = len(STAGES) - 1

    def __player_wins(self) -> bool:
        for letter in self._word:
            if letter not in self.guesses:
                return False
        return True

    def guess_word(self, guess: str) -> bool:
        is_not_correct = not guess in self._word

        if is_not_correct:
            self.lifes -= 1

        if guess not in self.guesses:
            self.guesses.append(guess)

        if self.lifes <= 0 or self.__player_wins():
            self.running = False

        self.__player_wins()

        return is_not_correct

    def start(self):
        self.__randomize_word()
        self.__reset_lifes()
        self.running = True
