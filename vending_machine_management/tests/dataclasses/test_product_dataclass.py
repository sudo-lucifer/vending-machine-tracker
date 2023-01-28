from django.test import TestCase

from vending_machine_management.dataclasses.product_dataclass import ProductDataclass
from vending_machine_management.models.product import Product
from vending_machine_management.serializers.product_serializer import ProductSerializer
from vending_machine_management.tests.model_instances.product_model_inatance import product_instance


class TestProductDataclass(TestCase):
    """Test class for product dataclass with product query instance."""

    @classmethod
    def setUpTestData(cls) -> None:
        """Test hook to mock product instance in database.

        :return: None
        """
        cls.product: Product = product_instance.make()

    def test_product_dataclass_from_model(self) -> None:
        """Test from_model() to return the dataclass version of product query instance."""
        expected_result: ProductDataclass = ProductSerializer(self.product).data
        dataclass_result_from_model: ProductDataclass = ProductDataclass.from_model(
            product_instance=self.product
        ).to_dict()
        self.assertEqual(expected_result, dataclass_result_from_model)
