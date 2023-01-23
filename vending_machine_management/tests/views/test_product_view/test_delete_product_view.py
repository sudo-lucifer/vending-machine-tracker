from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from vending_machine_management.tests.model_instances.product_model_inatance import product_instance


class TestDeleteProductView(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.product_1 = product_instance.make()

    def test_delete_single_machine(self):
        url = reverse("product:retrieve-update-destroy", kwargs={"id": self.product_1.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_single_machine_not_found(self):
        url = reverse("product:retrieve-update-destroy", kwargs={"id": self.product_1.id + 1})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
