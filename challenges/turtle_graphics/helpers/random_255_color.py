from random import randint


def random_255_color() -> tuple[int, int, int]:
    return (randint(0, 255), randint(0, 255), randint(0, 255))
