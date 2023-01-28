import json
from typing import List

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from vending_machine_management.dataclasses.product_dataclass import ProductDataclass
from vending_machine_management.models.product import Product
from vending_machine_management.serializers.product_serializer import ProductSerializer
from vending_machine_management.tests.model_instances.product_model_inatance import product_instance


class TestListProductView(APITestCase):
    """Test class for listing all product in database."""

    @classmethod
    def setUpTestData(cls) -> None:
        """Test hook to 2 mock product instances in database.

        :return: None
        """
        cls.product_1: Product = product_instance.make()
        cls.product_2: Product = product_instance.make()

    def test_list_product(self) -> None:
        """Test listing all products in database."""
        url = reverse("product:list-create")

        response = self.client.get(url)

        expected_result: List[ProductDataclass] = [
            ProductSerializer(self.product_1).data,
            ProductSerializer(self.product_2).data,
        ]
        response_data: List[ProductDataclass] = json.loads(json.dumps(response.data))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(expected_result, response_data)
