from typing import Dict

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from vending_machine_management.tests.model_instances.machine_model_instance import machine_instance


class TestAddMachineView(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.machine_1 = machine_instance.make()
        cls.location = "Location 1"
        cls.url = reverse("vending_machine:list-create")

    def test_add_machine_invalid_input(self):
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        request_body: Dict[str, str] = {"name": "Test 1"}
        response = self.client.post(self.url, data=request_body)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        request_body: Dict[str, str] = {"location": self.location}
        response = self.client.post(self.url, data=request_body)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_add_machine_correct_input(self):
        request_body: Dict[str, str] = {"name": "Test 1", "location": self.location}
        response = self.client.post(self.url, data=request_body)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], request_body['name'])
        self.assertEqual(response.data['location'], request_body['location'])

    def test_add_machine_duplicate_name(self):
        request_body: Dict[str, str] = {"name": self.machine_1.name, "location": self.location}
        response = self.client.post(self.url, data=request_body)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
