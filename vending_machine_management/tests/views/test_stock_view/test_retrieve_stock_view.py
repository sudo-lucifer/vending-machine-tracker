import json
from typing import Dict

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from vending_machine_management.serializers.stock.stock_serializer import StockSerializer
from vending_machine_management.tests.model_instances.machine_model_instance import machine_instance
from vending_machine_management.tests.model_instances.product_model_inatance import product_instance
from vending_machine_management.tests.model_instances.stock_mode_instance import stock_instance


class TestRetrieveStockView(APITestCase):
    @classmethod
    def setUpTestData(cls):
        product_1 = product_instance.make()
        machine_1 = machine_instance.make()
        cls.stock = stock_instance.make(product=product_1, machine=machine_1)

    def test_retrieve_single_stock(self):
        url = reverse("stock:detail", kwargs={"id": self.stock.id})
        response = self.client.get(url)

        expected_result: Dict[str, str] = StockSerializer(self.stock).data
        response_data: Dict[str, str] = json.loads(json.dumps(response.data))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(expected_result, response_data)

    def test_retrieve_single_stock_not_found(self):
        url = reverse("stock:detail", kwargs={"id": self.stock.id + 1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
