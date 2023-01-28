from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from vending_machine_management.models.product import Product
from vending_machine_management.tests.model_instances.product_model_inatance import product_instance


class TestDeleteProductView(APITestCase):
    """Test class for deleting product in database."""

    @classmethod
    def setUpTestData(cls) -> None:
        """Test hook to mock product instance in database.

        :return: None
        """
        cls.product_1: Product = product_instance.make()

    def test_delete_single_product(self) -> None:
        """Test deleting one existing product."""
        url = reverse("product:retrieve-update-destroy", kwargs={"id": self.product_1.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_single_product_not_found(self) -> None:
        """Test deleting one non-existing product."""
        url = reverse("product:retrieve-update-destroy", kwargs={"id": self.product_1.id + 1})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
