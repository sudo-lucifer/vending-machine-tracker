import json
from typing import List

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from vending_machine_management.dataclasses.stock_dataclass import StockDataclass
from vending_machine_management.models.stock import Stock
from vending_machine_management.serializers.stock.stock_serializer import StockSerializer
from vending_machine_management.tests.model_instances.stock_mode_instance import stock_instance


class TestListStockView(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.stock_1: Stock = stock_instance.make()
        cls.stock_2: Stock = stock_instance.make()

    def test_list_stock(self):
        url = reverse("stock:list")
        response = self.client.get(url)

        expected_result: List[StockDataclass] = [
            StockSerializer(self.stock_1).data,
            StockSerializer(self.stock_2).data,
        ]
        response_data: List[StockDataclass] = json.loads(json.dumps(response.data))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(expected_result, response_data)
