from simple_calculator.core import Numeric, SimpleCalculator


def convert_to_numeric(string: str) -> Numeric:
    if string.isdigit():
        return int(string)
    return float(string)


def clear_terminal():
    print("\033[H\033[J", end="")


def main():
    OPERATIONS = ("+", "-", "*", "/")
    calculator = SimpleCalculator()

    try:
        while True:
            a = convert_to_numeric(input("Write the first number: "))

            print(" ".join(OPERATIONS))
            operation = input("Pick an operation: ")

            if operation not in OPERATIONS:
                print("This operation is not available!")
                break

            b = convert_to_numeric(input("Write the second number: "))

            total = calculator.calculate(a, b, operation)
            print(f"The total is: {total}")

            keep_running = input('Do you want to continue? "Y" or "N": ').upper()
            if keep_running == "N":
                break

            clear_terminal()
    except ValueError:
        print("The input is not a number!")
    except:
        print("\nSomething went wrong!")


if __name__ == "__main__":
    main()
