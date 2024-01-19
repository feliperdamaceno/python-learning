from turtle import Turtle

from helpers import random_255_color


class Spirograph:
    def __init__(self, engine: Turtle) -> None:
        self.engine = engine

        self.engine.screen.colormode(255)
        self.engine.speed(0)

    def draw(self) -> None:
        for position in range(0, 360, 5):
            self.engine.color(random_255_color())
            self.engine.setheading(position)
            self.engine.circle(100)
