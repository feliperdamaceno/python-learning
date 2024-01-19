from random import randint
from turtle import Turtle

from helpers import random_255_color


class RandomWalk:
    def __init__(self, engine: Turtle) -> None:
        self.engine = engine

        self.engine.screen.colormode(255)
        self.engine.pensize(width=5)
        self.engine.speed(10)

    def draw(self) -> None:
        for _ in range(100):
            direction = randint(1, 4) * 90
            self.engine.pencolor(random_255_color())
            self.engine.setheading(direction)
            self.engine.forward(25)
