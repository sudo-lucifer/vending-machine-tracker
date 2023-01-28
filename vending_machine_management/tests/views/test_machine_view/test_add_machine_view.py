import secrets
from typing import Dict

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from vending_machine_management.models.machine import Machine
from vending_machine_management.tests.model_instances.machine_model_instance import machine_instance


class TestAddMachineView(APITestCase):
    """Test class for adding machine to database."""

    @classmethod
    def setUpTestData(cls) -> None:
        """Test hook to mock machine instance in database.

        :return: None
        """
        cls.machine_1: Machine = machine_instance.make()
        cls.location: str = "Location 1"
        cls.url = reverse("vending_machine:list-create")

    def test_add_machine_invalid_input(self) -> None:
        """Test sending request for create with invalid input."""
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        request_body: Dict[str, str] = {"name": "Test 1"}
        response = self.client.post(self.url, data=request_body)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        request_body: Dict[str, str] = {"location": self.location}
        response = self.client.post(self.url, data=request_body)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_add_machine_correct_input(self) -> None:
        """Test sending request for create with correct input (random name)."""
        new_machine_name: str = secrets.token_hex(16)
        request_body: Dict[str, str] = {"name": new_machine_name, "location": self.location}
        response = self.client.post(self.url, data=request_body)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], request_body['name'])
        self.assertEqual(response.data['location'], request_body['location'])

    def test_add_machine_duplicate_name(self) -> None:
        """Test sending request for create when machine already exists."""
        request_body: Dict[str, str] = {"name": self.machine_1.name, "location": self.location}
        response = self.client.post(self.url, data=request_body)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
