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


class TestAddStockView(APITestCase):
    @classmethod
    def setUpTestData(cls):
        product_2 = product_instance.make()
        machine_2 = machine_instance.make()
        cls.product_1 = product_instance.make()
        cls.machine_1 = machine_instance.make()
        cls.stock = stock_instance.make(product=product_2, machine=machine_2)
        cls.url = reverse("stock:create")

    def test_add_stock_invalid_input(self):
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        request_body: Dict[str, int] = {"machine": self.machine_1.id}
        response = self.client.post(self.url, data=request_body)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        request_body: Dict[str, int] = {"product": self.product_1.id}
        response = self.client.post(self.url, data=request_body)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_add_stock_correct_input(self):
        request_body: Dict[str, int] = {"machine": self.machine_1.id, "product": self.product_1.id}

        response = self.client.post(self.url, data=request_body)

        response_product: Dict[str, str] = json.loads(json.dumps(response.data['product']))
        response_machine: Dict[str, str] = json.loads(json.dumps(response.data['machine']))
        expected_product: Dict[str, str] = ProductSerializer(self.product_1).data
        expected_machine: Dict[str, str] = MachineSerializer(self.machine_1).data
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response_product, expected_product)
        self.assertEqual(response_machine, expected_machine)

    def test_add_stock_duplicate_name(self):
        request_body: Dict[str, int] = {"machine": self.stock.machine.id, "product": self.stock.product.id}
        response = self.client.post(self.url, data=request_body)
        self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)
