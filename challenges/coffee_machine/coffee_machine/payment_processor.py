from dataclasses import dataclass, field

from .product_management import Product


@dataclass
class PaymentProcessor:
    _earnings: float = field(init=False, repr=False, default=0)

    @property
    def earnings(self) -> float:
        return self._earnings

    def check_sufficient_funds(self, product: Product, cash: float) -> bool:
        return product.price > cash

    def process_transaction(self, product: Product, cash: float) -> float:
        self._earnings += product.price
        return cash - product.price
