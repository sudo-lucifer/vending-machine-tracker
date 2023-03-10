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


class TestEditStockView(APITestCase):
    """Test class for editing one stock."""

    @classmethod
    def setUpTestData(cls) -> None:
        """Test hook for mocking 2 stocks instances (one for editing, another for testing duplicate).

        :return: None
        """
        stock_1: Stock = stock_instance.make()
        cls.product_1: Product = product_instance.make()
        cls.machine_1: Machine = machine_instance.make()
        cls.stock_1: Stock = stock_1
        cls.stock_2: Stock = stock_instance.make()
        cls.url = reverse("stock:edit", kwargs={"id": stock_1.id})

    def test_edit_stock_invalid_input(self) -> None:
        """Test put request method for editing stock with invalid input (missing machine or product key)."""
        response = self.client.put(self.url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        request_body: Dict[str, int] = {"machine": self.machine_1.id}
        response = self.client.put(self.url, data=request_body)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        request_body: Dict[str, int] = {"product": self.product_1.id}
        response = self.client.put(self.url, data=request_body)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_edit_stock_correct_input(self) -> None:
        """Test put request method for editing stock with correct input."""
        request_body: Dict[str, int] = {"machine": self.machine_1.id, "product": self.product_1.id, "amount": 100}

        response = self.client.put(self.url, data=request_body)

        response_machine: MachineDataclass = json.loads(json.dumps(response.data['machine']))
        response_product: ProductDataclass = json.loads(json.dumps(response.data['product']))
        expected_product: ProductDataclass = ProductSerializer(self.product_1).data
        expected_machine: MachineDataclass = MachineSerializer(self.machine_1).data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(int(response.data["id"]), self.stock_1.id)
        self.assertEqual(int(response.data["amount"]), 100)
        self.assertEqual(response_product, expected_product)
        self.assertEqual(response_machine, expected_machine)

    def test_partially_edit_stock_correct_input(self) -> None:
        """Test patch request method for editing stock."""
        request_body: Dict[str, int] = {"product": self.product_1.id}

        response = self.client.patch(self.url, data=request_body)

        expected_product: ProductDataclass = ProductSerializer(self.product_1).data
        response_product: ProductDataclass = json.loads(json.dumps(response.data['product']))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(int(response.data["id"]), self.stock_1.id)
        self.assertEqual(response_product, expected_product)

    def test_edit_stock_duplicate_machine_or_product(self) -> None:
        """Test editing stock with duplicate machine and product key pair."""
        request_body: Dict[str, int] = {"machine": self.stock_2.machine.id, "product": self.stock_2.product.id}
        response = self.client.put(self.url, data=request_body)
        self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)

    def test_edit_stock_not_found(self) -> None:
        """Test editing non-existing stock."""
        url = reverse("stock:edit", kwargs={"id": self.stock_2.id + 1})
        response = self.client.put(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
