from turtle import Turtle

from helpers import random_255_color


class Decagon:
    def __init__(self, engine: Turtle) -> None:
        self.engine = engine

        self.engine.screen.colormode(255)

    def draw(self) -> None:
        self.engine.penup()
        self.engine.forward(60)
        self.engine.pendown()

        for sides in range(3, 11):
            self.engine.color(random_255_color())
            angle = 360 / sides
            for _ in range(sides):
                self.engine.right(angle)
                self.engine.forward(100)
