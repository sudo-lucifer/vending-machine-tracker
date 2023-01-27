from dataclasses import dataclass

from dataclasses_json import dataclass_json

from vending_machine_management.models.product import Product


@dataclass_json
@dataclass
class ProductDataclass:
    """Dataclass for product model."""

    id: int
    name: str
    price: float

    @classmethod
    def from_model(cls, product_instance: Product) -> 'ProductDataclass':
        """Categorize raw product model to dataclass.

        :param product_instance: query instance from product model
        :return: dataclass representation of product query instance
        """
        return cls(id=product_instance.id, name=product_instance.name, price=float(product_instance.price))
