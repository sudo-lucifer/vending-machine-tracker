from dataclasses import dataclass

from dataclasses_json import dataclass_json

from vending_machine_management.dataclasses.machine_dataclass import MachineDataclass
from vending_machine_management.dataclasses.product_dataclass import ProductDataclass
from vending_machine_management.models.stock import Stock


@dataclass_json
@dataclass
class StockDataclass:
    """Dataclass for stock model."""

    id: int
    machine: MachineDataclass
    product: ProductDataclass

    @classmethod
    def from_model(cls, stock_instance: Stock) -> 'StockDataclass':
        """Categorize raw stock model to dataclass.

        :param stock_instance:  query instance from stock model
        :return: dataclass representation of stock query instance
        """
        return cls(
            id=stock_instance.id,
            machine=MachineDataclass.from_model(stock_instance.machine),
            product=ProductDataclass.from_model(stock_instance.product),
        )
