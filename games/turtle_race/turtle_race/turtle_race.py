from random import randint
from tkinter import messagebox, simpledialog
from turtle import Screen, Turtle, _Screen

COLOR_OPTIONS = ("RED", "BLUE", "GREEN", "ORANGE", "PURPLE")
TURTLE_SIZE = 15
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 500
START_POSITION = -500 + TURTLE_SIZE
END_POSITION = 500


class TurtleRace:
    def __init__(self) -> None:
        self.screen: _Screen = Screen()
        self.running: bool = False
        self.guess: str | None = None
        self.winner: str | None = None
        self.turtles: list[Turtle] = self.__create_turtles()

        self.screen.setup(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
        self.__set_turtle_settings()

    def __create_turtles(self) -> list[Turtle]:
        return [Turtle() for _ in COLOR_OPTIONS]

    def __set_turtle_settings(self) -> None:
        for turtle, color in zip(self.turtles, COLOR_OPTIONS):
            turtle.shape("turtle")
            turtle.color(color)
            turtle.pensize(TURTLE_SIZE)
            turtle.penup()

    def __set_turtle_start_position(self) -> None:
        vertical_position = 100

        for turtle in self.turtles:
            turtle.goto(START_POSITION, vertical_position)
            vertical_position -= 50

    def __get_player_guess(self) -> str | None:
        turtle_options = " | ".join([color.lower() for color in COLOR_OPTIONS])
        guess = simpledialog.askstring(
            "Chose a color",
            f"{turtle_options}\n\nWhich one you think is going to win?",
        )
        return guess

    def __guess_winner(self) -> None:
        while True:
            self.guess = self.__get_player_guess() or ""
            if self.guess.upper() not in COLOR_OPTIONS:
                messagebox.showwarning("Ops!", "This turtle is not available!")
                continue
            break

    def __check_guess(self) -> None:
        if self.guess == self.winner:
            messagebox.showinfo("Winner", f"You got it! {self.winner} is the winner!")
            return
        messagebox.showinfo("Winner", f"You loose! {self.winner} is the winner!")

    def __move_turtles(self) -> None:
        self.running = True
        while self.running:
            for turtle in self.turtles:
                turtle.forward(randint(2, 10))
                if turtle.xcor() >= END_POSITION:
                    self.winner = turtle.color()[0].lower()
                    self.__check_guess()
                    self.running = False
                    break

    def start_race(self) -> None:
        self.__set_turtle_start_position()
        self.__guess_winner()
        self.__move_turtles()
