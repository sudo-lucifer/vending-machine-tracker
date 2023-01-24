import json
from typing import Dict

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from vending_machine_management.serializers.product_serializer import ProductSerializer
from vending_machine_management.tests.model_instances.product_model_inatance import product_instance


class TestRetrieveProductView(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.product_1 = product_instance.make()

    def test_retrieve_single_product(self):
        url = reverse("product:retrieve-update-destroy", kwargs={"id": self.product_1.id})

        response = self.client.get(url)

        expected_result: Dict[str, str] = ProductSerializer(self.product_1).data
        response_data: Dict[str, str] = json.loads(json.dumps(response.data))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(expected_result, response_data)

    def test_retrieve_single_product_not_found(self):
        url = reverse("product:retrieve-update-destroy", kwargs={"id": self.product_1.id + 1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
