from enum import Enum


class CHOICES(Enum):
    ROCK = "ROCK"
    PAPER = "PAPER"
    SCISSORS = "SCISSORS"


CHOICE_EMOJI = {CHOICES.ROCK: "🪨", CHOICES.PAPER: "📄", CHOICES.SCISSORS: "✂️"}
