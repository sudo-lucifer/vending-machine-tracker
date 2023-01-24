from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from vending_machine_management.models.machine import Machine
from vending_machine_management.tests.model_instances.machine_model_instance import machine_instance


class TestDeleteMachineView(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.machine_1: Machine = machine_instance.make()

    def test_delete_single_machine(self):
        url = reverse("vending_machine:retrieve-update-destroy", kwargs={"id": self.machine_1.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_single_machine_not_found(self):
        url = reverse("vending_machine:retrieve-update-destroy", kwargs={"id": self.machine_1.id + 1})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
