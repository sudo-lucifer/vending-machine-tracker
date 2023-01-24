from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from vending_machine_management.tests.model_instances.machine_model_instance import machine_instance
from vending_machine_management.tests.model_instances.product_model_inatance import product_instance
from vending_machine_management.tests.model_instances.stock_mode_instance import stock_instance


class TestDeleteStockView(APITestCase):
    @classmethod
    def setUpTestData(cls):
        product_1 = product_instance.make()
        machine_1 = machine_instance.make()
        cls.stock = stock_instance.make(product=product_1, machine=machine_1)

    def test_delete_single_stock(self):
        url = reverse("stock:delete", kwargs={"id": self.stock.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_single_stock_not_found(self):
        url = reverse("stock:delete", kwargs={"id": self.stock.id + 1})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
