import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from vending_machine_management.dataclasses.stock_dataclass import StockDataclass
from vending_machine_management.serializers.stock.stock_serializer import StockSerializer
from vending_machine_management.tests.model_instances.stock_mode_instance import stock_instance


class TestRetrieveStockView(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.stock = stock_instance.make()

    def test_retrieve_single_stock(self):
        url = reverse("stock:detail", kwargs={"id": self.stock.id})
        response = self.client.get(url)

        expected_result: StockDataclass = StockSerializer(self.stock).data
        response_data: StockDataclass = json.loads(json.dumps(response.data))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(expected_result, response_data)

    def test_retrieve_single_stock_not_found(self):
        url = reverse("stock:detail", kwargs={"id": self.stock.id + 1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
