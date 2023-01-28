import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from vending_machine_management.dataclasses.product_dataclass import ProductDataclass
from vending_machine_management.models.product import Product
from vending_machine_management.serializers.product_serializer import ProductSerializer
from vending_machine_management.tests.model_instances.product_model_inatance import product_instance


class TestRetrieveProductView(APITestCase):
    """Test class for getting one product detail."""

    @classmethod
    def setUpTestData(cls) -> None:
        """Test hook to mock product instance in database.

        :return: None
        """
        cls.product_1: Product = product_instance.make()

    def test_retrieve_single_product(self) -> None:
        """Test getting one existing product detail."""
        url = reverse("product:retrieve-update-destroy", kwargs={"id": self.product_1.id})
        response = self.client.get(url)

        expected_result: ProductDataclass = ProductSerializer(self.product_1).data
        response_data: ProductDataclass = json.loads(json.dumps(response.data))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(expected_result, response_data)

    def test_retrieve_single_product_not_found(self):
        """Test getting non-existing product detail."""
        url = reverse("product:retrieve-update-destroy", kwargs={"id": self.product_1.id + 1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
