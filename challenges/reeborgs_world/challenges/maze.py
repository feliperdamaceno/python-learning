from mock.reeborgs_world import (
    at_goal,
    front_is_clear,
    move,
    right_is_clear,
    turn_left,
    wall_on_right,
)


def turn_right():
    turn_left()
    turn_left()
    turn_left()


while not at_goal():
    if right_is_clear():
        turn_right()

    if front_is_clear():
        move()

    while wall_on_right():
        if front_is_clear():
            move()
            continue
        turn_left()
