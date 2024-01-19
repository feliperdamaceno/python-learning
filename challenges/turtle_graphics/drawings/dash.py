from turtle import Turtle


class Dash:
    def __init__(self, engine: Turtle) -> None:
        self.engine = engine

    def draw(self) -> None:
        self.engine.up()
        self.engine.backward(250)

        for index in range(50):
            self.engine.down()
            if index % 2 == 0:
                self.engine.up()
            self.engine.forward(10)
