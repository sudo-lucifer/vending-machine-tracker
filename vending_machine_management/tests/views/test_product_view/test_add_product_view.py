import secrets
from typing import Dict

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from vending_machine_management.models.product import Product
from vending_machine_management.tests.model_instances.product_model_inatance import product_instance


class TestAddProductView(APITestCase):
    """Test class for adding one product to database."""

    @classmethod
    def setUpTestData(cls) -> None:
        """Test hook to mock product instance in database.

        :return: None
        """
        cls.product_1: Product = product_instance.make()
        cls.url = reverse("product:list-create")

    def test_add_product_invalid_input(self) -> None:
        """Test adding product with invalid input."""
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_add_product_correct_input(self) -> None:
        """Test adding product with random name (correct input)."""
        new_product_name: str = secrets.token_hex(16)
        request_body: Dict[str, str] = {"name": new_product_name}
        response = self.client.post(self.url, data=request_body)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], request_body['name'])
        self.assertEqual(float(response.data['price']), 0)

        new_product_name = secrets.token_hex(16)
        request_body: Dict[str, str] = {"name": new_product_name, "price": 60}
        response = self.client.post(self.url, data=request_body)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], request_body['name'])
        self.assertEqual(float(response.data['price']), request_body['price'])

    def test_add_product_duplicate_name(self) -> None:
        """Test adding product with duplicate name to existing product in database."""
        request_body: Dict[str, str] = {"name": self.product_1.name}
        response = self.client.post(self.url, data=request_body)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
