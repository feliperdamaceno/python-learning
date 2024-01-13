from dataclasses import dataclass, field

from .constants import COFFEES, RESOURCES
from .payment_processor import PaymentProcessor
from .product_management import Product, ProductManagement
from .resource_management import ResourceManagement


@dataclass
class CoffeeMachine:
    _resource_management: ResourceManagement = field(
        init=False, repr=False, default_factory=ResourceManagement
    )
    _product_management: ProductManagement = field(
        init=False, repr=False, default_factory=ProductManagement
    )
    _payment_processor: PaymentProcessor = field(
        init=False, repr=False, default_factory=PaymentProcessor
    )
    working: bool = False

    def __post_init__(self) -> None:
        self._resource_management.create_resources(RESOURCES)
        self._product_management.create_products(COFFEES)

    @property
    def coffees(self) -> str:
        return " / ".join(self._product_management.products)

    def turn_on(self) -> None:
        self.working = True

    def turn_off(self) -> None:
        self.working = False

    def generate_report(self) -> None:
        for resource in self._resource_management.resources:
            print(f"{resource.name.capitalize()}: {resource.quantity}{resource.unit}")
        print(f"Earnings: €{self._payment_processor.earnings:.2f}")

    def buy(self, coffee_name: str, cash: float) -> float:
        coffee = self._product_management.get_product(coffee_name)

        insufficient_funds = self._payment_processor.check_sufficient_funds(
            coffee, cash
        )
        if insufficient_funds:
            print(f"The cash provided is not enough to buy a {coffee.name}")
            return cash

        enough_resources = self.__check_resources(coffee)
        if not enough_resources:
            return cash

        self.__make_coffee(coffee)

        return self._payment_processor.process_transaction(coffee, cash)

    def refill_resources(self):
        self._resource_management.reset_resources()

    def __check_resources(self, coffee: Product) -> bool:
        missing_resources = []

        resources = zip(coffee.recipe, self._resource_management.resources)
        for product_resource, storage_resource in resources:
            if product_resource.quantity > storage_resource.quantity:
                missing_resources.append(storage_resource.name)
                continue

        if missing_resources:
            for resource in missing_resources:
                print(f"Sorry there is not enough {resource}.")
            return False

        return True

    def __make_coffee(self, coffee: Product) -> None:
        for resource in coffee.recipe:
            self._resource_management.use_resource(resource.name, resource.quantity)
