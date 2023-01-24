import random
import string
from typing import Dict

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from vending_machine_management.models.product import Product
from vending_machine_management.tests.model_instances.product_model_inatance import product_instance


class TestEditProductView(APITestCase):
    @classmethod
    def setUpTestData(cls):
        product_1: Product = product_instance.make()
        cls.product_1: Product = product_1
        cls.product_2: Product = product_instance.make()
        cls.url = reverse("product:retrieve-update-destroy", kwargs={"id": product_1.id})

    def test_edit_product_invalid_input(self):
        response = self.client.put(self.url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_edit_product_correct_input(self):
        new_product_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=100))
        request_body: Dict[str, str] = {"name": new_product_name}
        response = self.client.put(self.url, data=request_body)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], self.product_1.id)
        self.assertEqual(response.data['name'], request_body['name'])
        self.assertEqual(float(response.data['price']), 0)

        new_product_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=100))
        request_body: Dict[str, str] = {"name": new_product_name, "price": 60}
        response = self.client.put(self.url, data=request_body)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], request_body['name'])
        self.assertEqual(float(response.data['price']), request_body['price'])

    def test_edit_product_duplicate_name(self):
        request_body: Dict[str, str] = {"name": self.product_2.name}
        response = self.client.put(self.url, data=request_body)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_edit_product_not_found(self):
        url = reverse("product:retrieve-update-destroy", kwargs={"id": self.product_2.id + 1})
        response = self.client.put(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
