def clear_terminal():
    print("\033[H\033[J", end="")


def is_float(string: str):
    try:
        float(string)
        return True
    except ValueError:
        return False
