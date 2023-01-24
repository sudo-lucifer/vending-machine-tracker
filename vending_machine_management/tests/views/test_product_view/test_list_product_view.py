import json
from typing import Dict, List

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from vending_machine_management.serializers.product_serializer import ProductSerializer
from vending_machine_management.tests.model_instances.product_model_inatance import product_instance


class TestListProductView(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.product_1 = product_instance.make()
        cls.product_2 = product_instance.make()

    def test_list_product(self):
        url = reverse("product:list-create")

        response = self.client.get(url)

        expected_result: List[Dict[str, str]] = [
            ProductSerializer(self.product_1).data,
            ProductSerializer(self.product_2).data,
        ]
        response_data: List[Dict[str, str]] = json.loads(json.dumps(response.data))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(expected_result, response_data)
