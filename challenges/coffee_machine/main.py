from time import sleep

from coffee_machine.core import CoffeeMachine
from helpers.core import clear_terminal, is_float
from interface.ascii import COFFEE_MACHINE_LOGO


def main() -> None:
    coffee_machine = CoffeeMachine()
    coffee_machine.turn_on()

    print(COFFEE_MACHINE_LOGO)
    while coffee_machine.working:
        try:
            print(coffee_machine.coffees)
            coffee_name = input(f"What do you like to order? ")

            if coffee_name == "report":
                coffee_machine.generate_report()
                print("-" * 50)
                continue

            if coffee_name == "refill":
                coffee_machine.refill_resources()
                print("-" * 50)
                continue

            if coffee_name == "off":
                coffee_machine.turn_off()
                continue

            cash = input(f"Insert the cash: €")
            if not is_float(cash):
                print(f"\nThe cash provided is not acceptable!")
                continue

            print("-" * 50)
            change = coffee_machine.buy(coffee_name, float(cash))

            if change > 0:
                print(f"\nHere is your change: €{change:.2f}")

            if change != float(cash):
                print(f"\nThanks for buying a {coffee_name} with us! Enjoy ☕")
            print("-" * 50)
        except TypeError as exception_message:
            print(f"The cash provided is not acceptable!")
        except ValueError as exception_message:
            print(exception_message)
        except:
            print("\nSomething went wrong! Please try again later.")
            coffee_machine.turn_off()


if __name__ == "__main__":
    main()
