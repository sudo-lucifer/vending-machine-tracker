from django.test import TestCase

from vending_machine_management.dataclasses.product_dataclass import ProductDataclass
from vending_machine_management.models.product import Product
from vending_machine_management.serializers.product_serializer import ProductSerializer
from vending_machine_management.tests.model_instances.product_model_inatance import product_instance


class TestProductDataclass(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.product: Product = product_instance.make()

    def test_product_dataclass_from_model(self):
        expected_result: ProductDataclass = ProductSerializer(self.product).data
        dataclass_result_from_model: ProductDataclass = ProductDataclass.from_model(
            product_instance=self.product
        ).to_dict()
        self.assertEqual(expected_result, dataclass_result_from_model)
