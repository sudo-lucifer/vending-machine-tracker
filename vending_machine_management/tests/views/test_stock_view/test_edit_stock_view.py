import json
from typing import Dict

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from vending_machine_management.serializers.machine_serializer import MachineSerializer
from vending_machine_management.serializers.product_serializer import ProductSerializer
from vending_machine_management.tests.model_instances.machine_model_instance import machine_instance
from vending_machine_management.tests.model_instances.product_model_inatance import product_instance
from vending_machine_management.tests.model_instances.stock_mode_instance import stock_instance


class TestEditStockView(APITestCase):
    @classmethod
    def setUpTestData(cls):
        product_2 = product_instance.make()
        machine_2 = machine_instance.make()
        stock_1 = stock_instance.make(product=product_2, machine=machine_2)
        cls.product_1 = product_instance.make()
        cls.machine_1 = machine_instance.make()
        cls.stock_1 = stock_1
        cls.stock_2 = stock_instance.make()
        cls.url = reverse("stock:edit", kwargs={"id": stock_1.id})

    def test_edit_stock_invalid_input(self):
        response = self.client.put(self.url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        request_body: Dict[str, int] = {"machine": self.machine_1.id}
        response = self.client.put(self.url, data=request_body)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        request_body: Dict[str, int] = {"product": self.product_1.id}
        response = self.client.put(self.url, data=request_body)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_edit_stock_correct_input(self):
        request_body: Dict[str, int] = {"machine": self.machine_1.id, "product": self.product_1.id, "amount": 100}

        response = self.client.put(self.url, data=request_body)

        response_machine: Dict[str, str] = json.loads(json.dumps(response.data['machine']))
        response_product: Dict[str, str] = json.loads(json.dumps(response.data['product']))
        expected_product: Dict[str, str] = ProductSerializer(self.product_1).data
        expected_machine: Dict[str, str] = MachineSerializer(self.machine_1).data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(int(response.data["id"]), self.stock_1.id)
        self.assertEqual(int(response.data["amount"]), 100)
        self.assertEqual(response_product, expected_product)
        self.assertEqual(response_machine, expected_machine)

    def test_add_stock_duplicate_machine_or_product(self):
        request_body: Dict[str, int] = {"machine": self.stock_2.machine.id, "product": self.stock_2.product.id}
        response = self.client.put(self.url, data=request_body)
        self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)
