import json
from typing import Dict

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from vending_machine_management.dataclasses.machine_dataclass import MachineDataclass
from vending_machine_management.dataclasses.product_dataclass import ProductDataclass
from vending_machine_management.models.machine import Machine
from vending_machine_management.models.product import Product
from vending_machine_management.models.stock import Stock
from vending_machine_management.serializers.machine_serializer import MachineSerializer
from vending_machine_management.serializers.product_serializer import ProductSerializer
from vending_machine_management.tests.model_instances.machine_model_instance import machine_instance
from vending_machine_management.tests.model_instances.product_model_inatance import product_instance
from vending_machine_management.tests.model_instances.stock_mode_instance import stock_instance


class TestAddStockView(APITestCase):
    """Test class for adding stock to database."""

    @classmethod
    def setUpTestData(cls) -> None:
        """Test hook for mocking stock, machine, product instances to database.

        Stock instance is for testing duplicate.

        :return:
        """
        cls.product_1: Product = product_instance.make()
        cls.machine_1: Machine = machine_instance.make()
        cls.stock: Stock = stock_instance.make()
        cls.url = reverse("stock:create")

    def test_add_stock_invalid_input(self) -> None:
        """Test adding stock with invalid input (missing machine or product key)."""
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        request_body: Dict[str, int] = {"machine": self.machine_1.id}
        response = self.client.post(self.url, data=request_body)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        request_body: Dict[str, int] = {"product": self.product_1.id}
        response = self.client.post(self.url, data=request_body)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_add_stock_correct_input(self) -> None:
        """Test adding stock with correct."""
        request_body: Dict[str, int] = {"machine": self.machine_1.id, "product": self.product_1.id}

        response = self.client.post(self.url, data=request_body)

        response_product: ProductDataclass = json.loads(json.dumps(response.data['product']))
        response_machine: MachineDataclass = json.loads(json.dumps(response.data['machine']))
        expected_product: ProductDataclass = ProductSerializer(self.product_1).data
        expected_machine: MachineDataclass = MachineSerializer(self.machine_1).data
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response_product, expected_product)
        self.assertEqual(response_machine, expected_machine)

    def test_add_stock_duplicate_machine_or_product(self) -> None:
        """Test adding stock with duplicate machine and product key pair."""
        request_body: Dict[str, int] = {"machine": self.stock.machine.id, "product": self.stock.product.id}
        response = self.client.post(self.url, data=request_body)
        self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)
