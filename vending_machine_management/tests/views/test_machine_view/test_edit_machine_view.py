import random
import string
from typing import Dict

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from vending_machine_management.models.machine import Machine
from vending_machine_management.tests.model_instances.machine_model_instance import machine_instance


class TestEditMachineView(APITestCase):
    @classmethod
    def setUpTestData(cls):
        machine_1: Machine = machine_instance.make()
        cls.machine_1: Machine = machine_1
        cls.machine_2: Machine = machine_instance.make()
        cls.url = reverse("vending_machine:retrieve-update-destroy", kwargs={"id": machine_1.id})

    def test_edit_single_machine_invalid_input(self):
        response = self.client.put(self.url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        request_body: Dict[str, str] = {"name": "Test 1"}
        response = self.client.put(self.url, data=request_body)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        request_body: Dict[str, str] = {"location": "Location 1"}
        response = self.client.put(self.url, data=request_body)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_edit_machine_correct_input(self):
        new_machine_name: str = ''.join(random.choices(string.ascii_uppercase + string.digits, k=100))
        request_body: Dict[str, str] = {"name": new_machine_name, "location": self.machine_1.location}

        response = self.client.put(self.url, data=request_body)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], self.machine_1.id)
        self.assertEqual(response.data['name'], request_body['name'])
        self.assertEqual(response.data['location'], request_body['location'])

    def test_edit_machine_duplicate_name(self):
        request_body: Dict[str, str] = {"name": self.machine_2.name, "location": self.machine_1.location}
        response = self.client.put(self.url, data=request_body)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_edit_machine_not_found(self):
        url = reverse("vending_machine:retrieve-update-destroy", kwargs={"id": self.machine_2.id + 1})
        response = self.client.put(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
