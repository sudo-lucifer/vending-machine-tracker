from django.test import TestCase

from vending_machine_management.dataclasses.machine_dataclass import MachineDataclass
from vending_machine_management.dataclasses.product_dataclass import ProductDataclass
from vending_machine_management.dataclasses.stock_dataclass import StockDataclass
from vending_machine_management.models.stock import Stock
from vending_machine_management.tests.model_instances.stock_mode_instance import stock_instance


class TestStockDataclass(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.stock: Stock = stock_instance.make()

    def test_stock_dataclass_from_model(self):
        expected_result: StockDataclass = StockDataclass(
            id=self.stock.id,
            machine=MachineDataclass.from_model(machine_instance=self.stock.machine),
            product=ProductDataclass.from_model(product_instance=self.stock.product),
        )
        dataclass_result_from_model: StockDataclass = StockDataclass.from_model(stock_instance=self.stock)
        self.assertEqual(expected_result, dataclass_result_from_model)
