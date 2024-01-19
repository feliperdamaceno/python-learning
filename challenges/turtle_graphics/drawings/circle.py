from turtle import Turtle


class Circle:
    def __init__(self, engine: Turtle) -> None:
        self.engine = engine

    def draw(self) -> None:
        for _ in range(360):
            self.engine.forward(2)
            self.engine.left(1)
