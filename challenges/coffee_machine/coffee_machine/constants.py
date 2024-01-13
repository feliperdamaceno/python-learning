from .payment_processor import Product
from .resource_management import Resource

RESOURCES = [
    Resource(name="water", quantity=300, unit="ml"),
    Resource(name="coffee", quantity=100, unit="g"),
    Resource(name="milk", quantity=200, unit="ml"),
]

COFFEES = [
    Product(
        name="espresso",
        price=1.5,
        recipe=[Resource("water", 50, "ml"), Resource("coffee", 18, "g")],
    ),
    Product(
        name="latte",
        price=2.5,
        recipe=[
            Resource("water", 200, "ml"),
            Resource("coffee", 24, "g"),
            Resource("milk", 150, "ml"),
        ],
    ),
    Product(
        name="cappuccino",
        price=3,
        recipe=[
            Resource("water", 250, "ml"),
            Resource("coffee", 24, "g"),
            Resource("milk", 100, "ml"),
        ],
    ),
]
