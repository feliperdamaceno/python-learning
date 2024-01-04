def calculate_tip(bill: float, tip_percentage: int = 0) -> float:
    total = ((bill * tip_percentage) / 100) + bill
    return round(total, 2)


def split_bill(bill: float, number_of_people: int) -> float:
    total = bill / number_of_people
    return round(total, 2)


def main():
    bill = float(input("What's the total of the bill?\n"))
    number_of_people = int(input("How many people to split the bill?\n"))
    tip = int(input("What percentage of tip would you like to give?\n"))

    bill_with_tip = calculate_tip(bill, tip)
    splitted_bill = split_bill(bill_with_tip, number_of_people)

    print(f"Each person should pay ${splitted_bill}")


if __name__ == "__main__":
    main()
