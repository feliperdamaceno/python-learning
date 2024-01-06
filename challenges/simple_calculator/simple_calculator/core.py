from dataclasses import dataclass

Numeric = int | float


@dataclass
class SimpleCalculator:
    def __add(self, a: Numeric, b: Numeric):
        return a + b

    def __subtract(self, a: Numeric, b: Numeric):
        return a - b

    def __multiply(self, a: Numeric, b: Numeric):
        return a * b

    def __divide(self, a: Numeric, b: Numeric):
        return a / b

    def calculate(self, a: Numeric, b: Numeric, operation: str):
        match operation:
            case "+":
                return self.__add(a, b)
            case "-":
                return self.__subtract(a, b)
            case "*":
                return self.__multiply(a, b)
            case "/":
                return self.__divide(a, b)
            case _:
                return 0
