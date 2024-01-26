from enum import StrEnum
from turtle import Screen, Turtle


class KeyboardKeys(StrEnum):
    ESCAPE = "Escape"
    UP_ARROW = "Up"
    DOWN_ARROW = "Down"
    LEFT_ARROW = "Left"
    RIGHT_ARROW = "Right"
    DELETE = "Delete"


PEN_SPEED = 3
TURN_SPEED = 10


class EtchASketch:
    def __init__(self) -> None:
        self.engine = Turtle()
        self.screen = Screen()

    def go_forward(self) -> None:
        self.engine.forward(PEN_SPEED)

    def go_backward(self) -> None:
        self.engine.backward(PEN_SPEED)

    def turn_left(self) -> None:
        self.engine.left(TURN_SPEED)

    def turn_right(self) -> None:
        self.engine.right(TURN_SPEED)

    def clear_screen(self) -> None:
        self.engine.penup()
        self.engine.home()
        self.engine.pendown()
        self.engine.clear()

    def start(self) -> None:
        self.screen.listen()

        # Listeners
        self.screen.onkeypress(self.screen.bye, KeyboardKeys.ESCAPE)
        self.screen.onkeypress(self.go_forward, KeyboardKeys.UP_ARROW)
        self.screen.onkeypress(self.go_backward, KeyboardKeys.DOWN_ARROW)
        self.screen.onkeypress(self.turn_left, KeyboardKeys.LEFT_ARROW)
        self.screen.onkeypress(self.turn_right, KeyboardKeys.RIGHT_ARROW)
        self.screen.onkeypress(self.clear_screen, KeyboardKeys.DELETE)

        self.screen.mainloop()
