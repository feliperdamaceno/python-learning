from dataclasses import dataclass, field

from .resource_management import Resource


@dataclass
class Product:
    name: str
    price: float
    recipe: list[Resource]


@dataclass
class ProductManagement:
    _products: list[Product] = field(init=False, repr=False, default_factory=list)

    @property
    def products(self) -> list[str]:
        return [product.name for product in self._products]

    def create_products(self, products: list[Product]) -> None:
        self._products.extend(products)

    def get_product(self, product_name: str) -> Product:
        product = [
            product for product in self._products if product.name == product_name
        ]

        if not product:
            raise ValueError(f"The product {product_name} has not been found")

        return product[0]
