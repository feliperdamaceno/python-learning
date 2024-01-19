from turtle import Turtle


class Square:
    def __init__(self, engine: Turtle) -> None:
        self.engine = engine

    def draw(self) -> None:
        self.engine.up()
        self.engine.backward(50)
        self.engine.down()

        for _ in range(4):
            self.engine.forward(100)
            self.engine.left(90)
