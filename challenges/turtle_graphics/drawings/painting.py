from turtle import Turtle

from helpers import random_255_color


class Painting:
    CIRCLE_SIZE = 25
    CIRCLE_QUANTITY = 10

    def __init__(self, engine: Turtle) -> None:
        self.engine = engine

        offset = (self.CIRCLE_SIZE * self.CIRCLE_QUANTITY) - self.CIRCLE_SIZE
        self.initial_x = -offset
        self.initial_y = -offset

        self.engine.screen.colormode(255)
        self.engine.hideturtle()
        self.engine.speed(0)
        self.engine.penup()
        self.engine.goto(self.initial_x, self.initial_y)

    def get_next_line_position(self, line: int) -> float:
        y_position = self.CIRCLE_SIZE * 2
        return self.initial_y + (y_position * line)

    def draw_circles(self) -> None:
        for position in range(self.CIRCLE_QUANTITY * 2):
            if position % 2 == 0:
                self.engine.dot(self.CIRCLE_SIZE, random_255_color())

            self.engine.forward(self.CIRCLE_SIZE)

    def draw(self) -> None:
        for line in range(self.CIRCLE_QUANTITY):
            self.engine.goto(self.initial_x, self.get_next_line_position(line))
            self.draw_circles()
