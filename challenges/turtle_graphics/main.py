from turtle import Turtle

from drawings import Painting


def main():
    turtle = Turtle()

    drawing = Painting(engine=turtle)
    drawing.draw()

    turtle.screen.mainloop()


if __name__ == "__main__":
    main()
